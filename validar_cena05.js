const fs = require("fs");
const http = require("http");
const net = require("net");
const os = require("os");
const path = require("path");
const { spawn } = require("child_process");

const ROOT = process.cwd();
const OUT_DIR = path.join(ROOT, "validacoes");
const HERO_HTML = "cena05_tronco_encefalico.html";
const MODEL_HTML = "Imagens/Cena 05/cena05_v7.html";
const GLB = "Imagens/Cena 05/tronco-encefalico.glb";
const MODEL_VIEWER = "Imagens/Cena 05/model-viewer.min.js";
const MODE = process.argv.includes("--full")
  ? "full"
  : process.argv.includes("--interactive")
    ? "interactive"
    : process.argv.includes("--hero")
      ? "hero"
      : process.argv.includes("--static")
        ? "static"
        : "fast";

const MIME = {
  ".html": "text/html; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".glb": "model/gltf-binary",
  ".gltf": "model/gltf+json",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".webp": "image/webp",
  ".svg": "image/svg+xml",
};

function checkFile(relativePath) {
  const file = path.join(ROOT, relativePath);
  if (!fs.existsSync(file)) {
    throw new Error(`Arquivo obrigatorio nao encontrado: ${relativePath}`);
  }
}

function findChrome() {
  const envPath = process.env.CHROME_PATH;
  const candidates = [
    envPath,
    "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
    path.join(os.homedir(), "AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"),
    "C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe",
    "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
    path.join(os.homedir(), "AppData\\Local\\Microsoft\\Edge\\Application\\msedge.exe"),
  ].filter(Boolean);

  const found = candidates.find((candidate) => fs.existsSync(candidate));
  if (!found) {
    throw new Error("Chrome/Edge nao encontrado. Defina CHROME_PATH apontando para chrome.exe ou msedge.exe.");
  }
  return found;
}

function getFreePort() {
  return new Promise((resolve, reject) => {
    const server = net.createServer();
    server.once("error", reject);
    server.listen(0, "127.0.0.1", () => {
      const { port } = server.address();
      server.close(() => resolve(port));
    });
  });
}

function serveFile(req, res) {
  const requestPath = decodeURIComponent(new URL(req.url, "http://127.0.0.1").pathname);
  const relative = requestPath === "/" ? HERO_HTML : requestPath.replace(/^\/+/, "");
  const target = path.resolve(ROOT, relative);

  if (!target.startsWith(ROOT)) {
    res.writeHead(403);
    res.end("Forbidden");
    return;
  }

  fs.readFile(target, (err, data) => {
    if (err) {
      res.writeHead(404);
      res.end("Not found");
      return;
    }
    const ext = path.extname(target).toLowerCase();
    res.writeHead(200, {
      "Content-Type": MIME[ext] || "application/octet-stream",
      "Access-Control-Allow-Origin": "*",
      "Cache-Control": ext === ".html" ? "no-store" : "public, max-age=3600",
    });
    res.end(data);
  });
}

function startServer(port) {
  const server = http.createServer(serveFile);
  return new Promise((resolve, reject) => {
    server.once("error", reject);
    server.listen(port, "127.0.0.1", () => resolve(server));
  });
}

function wait(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function fetchJson(url) {
  return fetch(url).then((res) => {
    if (!res.ok) throw new Error(`HTTP ${res.status}: ${url}`);
    return res.json();
  });
}

class Cdp {
  constructor(wsUrl) {
    this.ws = new WebSocket(wsUrl);
    this.nextId = 1;
    this.pending = new Map();
    this.events = [];
    this.ws.addEventListener("message", (event) => this.onMessage(event));
  }

  async open() {
    if (this.ws.readyState === WebSocket.OPEN) return;
    await new Promise((resolve, reject) => {
      this.ws.addEventListener("open", resolve, { once: true });
      this.ws.addEventListener("error", reject, { once: true });
    });
  }

  onMessage(event) {
    const msg = JSON.parse(event.data);
    if (msg.id && this.pending.has(msg.id)) {
      const { resolve, reject } = this.pending.get(msg.id);
      this.pending.delete(msg.id);
      if (msg.error) reject(new Error(JSON.stringify(msg.error)));
      else resolve(msg.result || {});
      return;
    }
    this.events.push(msg);
  }

  send(method, params = {}, sessionId) {
    const id = this.nextId++;
    const payload = { id, method, params };
    if (sessionId) payload.sessionId = sessionId;
    this.ws.send(JSON.stringify(payload));
    return new Promise((resolve, reject) => {
      this.pending.set(id, { resolve, reject });
      setTimeout(() => {
        if (this.pending.has(id)) {
          this.pending.delete(id);
          reject(new Error(`Timeout CDP: ${method}`));
        }
      }, 30000);
    });
  }

  async waitEvent(method, sessionId, timeout = 30000) {
    const started = Date.now();
    while (Date.now() - started < timeout) {
      const index = this.events.findIndex((event) => {
        return event.method === method && (!sessionId || event.sessionId === sessionId);
      });
      if (index >= 0) return this.events.splice(index, 1)[0];
      await wait(50);
    }
    throw new Error(`Timeout aguardando evento: ${method}`);
  }

  close() {
    this.ws.close();
  }
}

async function startChrome(chromePath, debugPort) {
  const profile = fs.mkdtempSync(path.join(os.tmpdir(), "cena05-chrome-"));
  const args = [
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--no-first-run",
    "--no-default-browser-check",
    `--remote-debugging-port=${debugPort}`,
    `--user-data-dir=${profile}`,
    "about:blank",
  ];
  const child = spawn(chromePath, args, { stdio: "ignore" });
  return { child, profile };
}

async function connectChrome(debugPort) {
  const versionUrl = `http://127.0.0.1:${debugPort}/json/version`;
  const started = Date.now();
  while (Date.now() - started < 15000) {
    try {
      const version = await fetchJson(versionUrl);
      const cdp = new Cdp(version.webSocketDebuggerUrl);
      await cdp.open();
      return cdp;
    } catch {
      await wait(250);
    }
  }
  throw new Error("Nao foi possivel conectar ao Chrome DevTools.");
}

async function createPage(cdp, url) {
  const { targetId } = await cdp.send("Target.createTarget", { url: "about:blank" });
  const { sessionId } = await cdp.send("Target.attachToTarget", { targetId, flatten: true });
  await cdp.send("Page.enable", {}, sessionId);
  await cdp.send("Runtime.enable", {}, sessionId);
  await cdp.send("Network.enable", {}, sessionId);
  await cdp.send("Emulation.setDeviceMetricsOverride", {
    width: 1280,
    height: 1200,
    deviceScaleFactor: 1,
    mobile: false,
  }, sessionId);
  await cdp.send("Page.navigate", { url }, sessionId);
  await cdp.waitEvent("Page.loadEventFired", sessionId, 60000);
  return sessionId;
}

async function evaluate(cdp, sessionId, expression, timeout = 30000) {
  const result = await cdp.send("Runtime.evaluate", {
    expression,
    awaitPromise: true,
    returnByValue: true,
    timeout,
  }, sessionId);
  if (result.exceptionDetails) {
    throw new Error(`Erro no browser: ${JSON.stringify(result.exceptionDetails)}`);
  }
  return result.result.value;
}

async function waitModelViewer(cdp, sessionId) {
  return evaluate(cdp, sessionId, `(() => new Promise((resolve) => {
    const mv = document.querySelector("model-viewer");
    if (!mv) {
      resolve({ ok:false, label:"no-model-viewer" });
      return;
    }
    const finish = (label) => resolve({
      ok: !!(mv.loaded || mv.modelIsVisible || label === "load" || label === "already"),
      label,
      loaded: !!mv.loaded,
      modelIsVisible: !!mv.modelIsVisible,
      complete: !!mv.complete,
      src: mv.getAttribute("src"),
      hasCanvas: !!(mv.shadowRoot && mv.shadowRoot.querySelector("canvas"))
    });
    if (mv.loaded || mv.modelIsVisible || mv.complete) {
      finish("already");
      return;
    }
    mv.addEventListener("load", () => finish("load"), { once:true });
    mv.addEventListener("model-visibility", () => finish("model-visibility"), { once:true });
    mv.addEventListener("error", (event) => resolve({
      ok:false,
      label:"error",
      src: mv.getAttribute("src"),
      detail: String(event.detail && (event.detail.sourceError || event.detail) || event)
    }), { once:true });
    setTimeout(() => finish("timeout"), 45000);
  }))()`, 60000);
}

async function screenshot(cdp, sessionId, file) {
  const { data } = await cdp.send("Page.captureScreenshot", { format: "png" }, sessionId);
  fs.writeFileSync(file, Buffer.from(data, "base64"));
}

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

function staticChecks() {
  const heroHtml = fs.readFileSync(path.join(ROOT, HERO_HTML), "utf8");
  const modelHtml = fs.readFileSync(path.join(ROOT, MODEL_HTML), "utf8");

  const checks = {
    heroUsesLocalModelViewer: heroHtml.includes('src="Imagens/Cena 05/model-viewer.min.js"'),
    heroUsesModelGlb: heroHtml.includes('src="Imagens/Cena 05/tronco-encefalico.glb"'),
    interactiveUsesLocalModelViewer: modelHtml.includes('src="model-viewer.min.js"'),
    interactiveUsesModelGlb: modelHtml.includes('src="tronco-encefalico.glb"'),
    interactiveHasCardContentCode: modelHtml.includes("ipDetailList.innerHTML") && modelHtml.includes("ipClinList.innerHTML"),
    interactiveHasCallout: modelHtml.includes('id="callout-layer"') && modelHtml.includes("strokeDashoffset"),
    interactiveHasManualArrowhead: modelHtml.includes('id="callout-arrowhead"') && !modelHtml.includes("marker-end"),
    interactiveHasRotationResume: modelHtml.includes("pointerleave") && modelHtml.includes("resumeRotation"),
  };

  for (const [name, ok] of Object.entries(checks)) {
    assert(ok, `Falha em checagem estatica: ${name}`);
  }

  return checks;
}

async function validateHero(cdp, baseUrl) {
  const session = await createPage(cdp, `${baseUrl}/${HERO_HTML}`);
  const model = await waitModelViewer(cdp, session);
  await wait(1200);
  const dom = await evaluate(cdp, session, `(() => {
    const mv = document.querySelector("section.hero model-viewer");
    return {
      hasHeroModelViewer: !!mv,
      src: mv && mv.getAttribute("src"),
      scriptLocal: [...document.scripts].some((s) => s.src.includes("model-viewer.min.js"))
    };
  })()`);
  const file = path.join(OUT_DIR, "cena05-hero.png");
  await screenshot(cdp, session, file);

  assert(dom.hasHeroModelViewer, "Hero nao contem model-viewer.");
  assert(dom.src === "Imagens/Cena 05/tronco-encefalico.glb", `Hero aponta para GLB errado: ${dom.src}`);
  assert(dom.scriptLocal, "Hero nao carrega model-viewer.min.js local.");
  assert(model.ok, `Model-viewer do hero nao carregou: ${JSON.stringify(model)}`);

  return { model, dom, screenshot: file };
}

async function validateInteractive(cdp, baseUrl) {
  const session = await createPage(cdp, `${baseUrl}/Imagens/Cena%2005/cena05_v7.html`);
  const model = await waitModelViewer(cdp, session);
  await evaluate(cdp, session, `document.querySelector(".viewer-grid").scrollIntoView({ block:"start" })`);
  await wait(500);
  const callouts = [];
  for (const key of ["cerebro", "mesencefalo", "ponte", "bulbo", "coluna", "nervos"]) {
    await evaluate(cdp, session, `document.querySelector("#btn-${key}").click()`);
    await wait(900);
    callouts.push(await evaluate(cdp, session, `(() => {
      const target = document.querySelector("#callout-target");
      const arrow = document.querySelector("#callout-arrowhead");
      return {
        key: "${key}",
        title: document.querySelector("#ip-title")?.textContent || "",
        visible: !!document.querySelector("#callout-layer.visible"),
        cx: Number(target?.getAttribute("cx") || 0),
        cy: Number(target?.getAttribute("cy") || 0),
        arrowPoints: arrow?.getAttribute("points") || ""
      };
    })()`));
    await screenshot(cdp, session, path.join(OUT_DIR, `cena05-card-${key}.png`));
  }
  await evaluate(cdp, session, `document.querySelector("#btn-ponte").click()`);
  await wait(1200);
  const card = await evaluate(cdp, session, `(() => ({
    title: document.querySelector("#ip-title")?.textContent || "",
    active: document.querySelector(".struct-btn.active")?.id || "",
    funcs: document.querySelectorAll("#ip-detail-list li").length,
    clinical: document.querySelectorAll("#ip-clinical-list li").length,
    calloutVisible: !!document.querySelector("#callout-layer.visible")
  }))()`);
  const cardShot = path.join(OUT_DIR, "cena05-card-ponte.png");
  await screenshot(cdp, session, cardShot);

  await evaluate(cdp, session, `document.querySelector("#btn-ponte").dispatchEvent(new PointerEvent("pointerleave", { bubbles:true }))`);
  await wait(300);
  const resume = await evaluate(cdp, session, `(() => {
    const mv = document.querySelector("model-viewer");
    return {
      autoRotate: !!mv.autoRotate,
      calloutVisible: !!document.querySelector("#callout-layer.visible"),
      title: document.querySelector("#ip-title")?.textContent || ""
    };
  })()`);

  assert(model.ok, `Model-viewer interativo nao carregou: ${JSON.stringify(model)}`);
  assert(callouts.every((item) => item.visible), `Nem todas as setas ficaram visiveis: ${JSON.stringify(callouts)}`);
  assert(callouts.every((item) => item.arrowPoints.trim().split(/\s+/).length === 3), `Ponta da seta nao foi desenhada corretamente: ${JSON.stringify(callouts)}`);
  const uniqueTargets = new Set(callouts.map((item) => `${Math.round(item.cx / 8) * 8},${Math.round(item.cy / 8) * 8}`));
  assert(uniqueTargets.size >= 5, `Setas parecem apontar para o mesmo lugar: ${JSON.stringify(callouts)}`);
  assert(card.title === "Ponte (Pons)", `Card nao preencheu titulo esperado: ${card.title}`);
  assert(card.active === "btn-ponte", `Card ativo incorreto: ${card.active}`);
  assert(card.funcs > 0, "Funcoes do card nao apareceram.");
  assert(card.clinical > 0, "Clinica do card nao apareceu.");
  assert(card.calloutVisible, "Seta/callout nao ficou visivel.");
  assert(resume.autoRotate, "Auto-rotate nao retornou apos sair do card.");
  assert(!resume.calloutVisible, "Seta nao sumiu apos retorno da rotacao.");
  assert(resume.title === "Ponte (Pons)", "Texto do card foi apagado ao retomar rotacao.");

  const posteriorShot = path.join(OUT_DIR, "cena05-model-posterior.png");
  await evaluate(cdp, session, `setView("180deg 75deg 2m")`);
  await wait(1200);
  await screenshot(cdp, session, posteriorShot);

  const lateralShot = path.join(OUT_DIR, "cena05-model-lateral.png");
  await evaluate(cdp, session, `setView("90deg 75deg 2m")`);
  await wait(1200);
  await screenshot(cdp, session, lateralShot);

  return { model, callouts, card, resume, screenshot: cardShot, viewScreenshots: { posterior: posteriorShot, lateral: lateralShot } };
}

async function main() {
  checkFile(HERO_HTML);
  checkFile(MODEL_HTML);
  checkFile(GLB);
  checkFile(MODEL_VIEWER);
  fs.mkdirSync(OUT_DIR, { recursive: true });

  const statics = staticChecks();
  const runHero = MODE === "fast" || MODE === "full" || MODE === "hero";
  const runInteractive = MODE === "full" || MODE === "interactive";

  if (MODE === "static") {
    console.log("PASS cena05");
    console.log(JSON.stringify({ mode: MODE, static: statics }, null, 2));
    return;
  }

  const chromePath = findChrome();
  const appPort = await getFreePort();
  const debugPort = await getFreePort();
  const server = await startServer(appPort);
  const chrome = await startChrome(chromePath, debugPort);
  let cdp;

  try {
    const baseUrl = `http://127.0.0.1:${appPort}`;
    cdp = await connectChrome(debugPort);
    const hero = runHero ? await validateHero(cdp, baseUrl) : { skipped: true };
    const interactive = runInteractive ? await validateInteractive(cdp, baseUrl) : { skipped: true };

    console.log("PASS cena05");
    console.log(JSON.stringify({
      mode: MODE,
      baseUrl,
      chromePath,
      static: statics,
      hero,
      interactive,
    }, null, 2));
  } finally {
    if (cdp) {
      try {
        cdp.close();
      } catch {}
    }
    await new Promise((resolve) => server.close(resolve));
    if (chrome.child) {
      try {
        chrome.child.kill();
      } catch {}
      await Promise.race([
        new Promise((resolve) => chrome.child.once("exit", resolve)),
        wait(1800),
      ]);
    }
    for (let attempt = 0; attempt < 4; attempt += 1) {
      try {
        fs.rmSync(chrome.profile, { recursive: true, force: true });
        break;
      } catch (error) {
        if (attempt === 3) {
          console.warn(`Aviso: nao foi possivel remover perfil temporario: ${chrome.profile}`);
        } else {
          await wait(500);
        }
      }
    }
  }
}

main().catch((error) => {
  console.error("FAIL cena05");
  console.error(error.stack || error.message);
  process.exit(1);
});
