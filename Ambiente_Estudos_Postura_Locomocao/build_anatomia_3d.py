from __future__ import annotations

import base64
import mimetypes
from pathlib import Path


ROOT = Path(__file__).resolve().parent
WORKSPACE = ROOT.parent
IMAGES = WORKSPACE / "page_images"
THREE_JS = ROOT / "three.r128.min.js"

SLIDE_META = [
    ("page01.png", "Capa",                     "Aula de Postura e Locomoção"),
    ("page02.png", "Introdução",               "Sistema motor integrado"),
    ("page03.png", "Organização",              "NMS → sinapse → NMI → músculo"),
    ("page04.png", "Córtex Motor",             "Giro pré-central e M1"),
    ("page05.png", "Áreas Corticais",          "Motor + sensorial + cerebelo"),
    ("page06.png", "Homúnculo",                "Mapa corporal distorcido"),
    ("page07.png", "Áreas Motoras",            "M1, PMC e SMA"),
    ("page08.png", "Feixe Corticoespinal",     "Via principal descendente"),
    ("page09.png", "Org. Corticoespinal",      "Via com interneurônios"),
    ("page10.png", "Diagrama CE",              "Etapas da via descendente"),
    ("page11.png", "Tronco Encefálico",        "Mesencéfalo, ponte, bulbo"),
    ("page12.png", "Vias Descendentes",        "CE lateral vs rubroespinal"),
    ("page13.png", "Extrapiramidais",          "Vestibulo/reticulo/rubro"),
    ("page14.png", "Núcleos do Tronco",        "Nervos cranianos"),
    ("page15.png", "Postura",                  "Estabilidade e gravidade"),
    ("page16.png", "Integração Sensorial",     "Propriocepção+vestibular+visão"),
    ("page17.png", "NMS e NMI",                "Comando vs via final"),
    ("page18.png", "Síndrome NMS",             "Hiperreflexia e espasticidade"),
    ("page19.png", "Doenças NMS",              "AVC, PC, EM, ELA..."),
    ("page20.png", "Síndrome NMI",             "Hipotonia e atrofia"),
    ("page21.png", "Cerebelar",                "Ataxia e dismetria"),
]


def data_uri(path: Path) -> str:
    mime = mimetypes.guess_type(path.name)[0] or "image/png"
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode('ascii')}"


def build_slide_data_js() -> str:
    """Build JavaScript array of slide metadata with base64 reference images."""
    rows = []
    for index, (filename, title, subtitle) in enumerate(SLIDE_META):
        src = data_uri(IMAGES / filename)
        rows.append(
            f'  {{number:{index+1},title:{title!r},subtitle:{subtitle!r},src:{src!r}}}'
        )
    return "const SLIDES = [\n" + ",\n".join(rows) + "\n];\n"


def build() -> str:
    three = THREE_JS.read_text(encoding="utf-8")
    slide_data_js = build_slide_data_js()

    return f"""<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Anatomia 3D — 21 Cenas | Postura e Locomoção</title>
  <style>
    :root {{
      --ink: #f8f4ec;
      --muted: #c9d1d8;
      --panel: rgba(18, 25, 32, .78);
      --panel-strong: rgba(18, 25, 32, .92);
      --line: rgba(255,255,255,.18);
      --teal: #38b2ac;
      --wine: #c94f56;
      --green: #2f9b63;
      --amber: #e2a541;
      --brain: #c99f68;
      --blue: #4a90d9;
      --purple: #9b59b6;
    }}
    * {{ box-sizing: border-box; }}
    html, body {{ width: 100%; height: 100%; margin: 0; overflow: hidden; }}
    body {{
      color: var(--ink);
      background: #0e141b;
      font-family: Arial, Helvetica, sans-serif;
      display: grid;
      grid-template-columns: 62px 1fr;
      grid-template-rows: 1fr;
    }}
    #scene {{
      width: 100%;
      height: 100%;
      display: block;
      background: #0e141b;
    }}
    .sidebar {{
      grid-column: 1;
      display: flex;
      flex-direction: column;
      gap: 2px;
      padding: 6px 4px;
      background: var(--panel-strong);
      border-right: 1px solid var(--line);
      overflow-y: auto;
      overflow-x: hidden;
      z-index: 10;
    }}
    .sidebar::-webkit-scrollbar {{ width: 4px; }}
    .sidebar::-webkit-scrollbar-thumb {{ background: rgba(255,255,255,.2); border-radius: 4px; }}
    .sb {{
      width: 52px;
      height: 38px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--muted);
      background: transparent;
      border: 1px solid transparent;
      border-radius: 6px;
      font-size: .82rem;
      font-weight: 700;
      cursor: pointer;
      transition: all .18s;
      flex-shrink: 0;
    }}
    .sb:hover {{ background: rgba(255,255,255,.08); color: #fff; }}
    .sb.active {{
      background: var(--wine);
      border-color: var(--wine);
      color: #fff;
    }}
    .main-area {{
      grid-column: 2;
      position: relative;
      overflow: hidden;
    }}
    .topbar {{
      position: absolute;
      left: 16px; right: 16px; top: 14px;
      z-index: 5;
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 14px;
      pointer-events: none;
    }}
    .title {{
      max-width: 680px;
      padding: 12px 14px;
      background: linear-gradient(115deg, rgba(23,107,112,.78), rgba(18,25,32,.72));
      border: 1px solid var(--line);
      border-radius: 8px;
      backdrop-filter: blur(10px);
      pointer-events: auto;
    }}
    .eyebrow {{
      margin: 0 0 4px;
      font-size: .72rem;
      font-weight: 700;
      letter-spacing: .08em;
      text-transform: uppercase;
      color: #e8d39a;
    }}
    h1 {{
      margin: 0;
      font-size: clamp(1.2rem, 3vw, 2rem);
      line-height: 1.1;
    }}
    .title p {{
      margin: 6px 0 0;
      color: var(--muted);
      font-size: .88rem;
      line-height: 1.35;
    }}
    .toolbar {{
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
      justify-content: flex-end;
      pointer-events: auto;
    }}
    button {{
      min-height: 36px;
      padding: 6px 10px;
      color: #fff;
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 6px;
      font: inherit;
      font-size: .85rem;
      font-weight: 700;
      cursor: pointer;
      backdrop-filter: blur(10px);
      white-space: nowrap;
    }}
    button.active {{ background: var(--wine); border-color: var(--wine); }}
    button:focus-visible {{ outline: 3px solid var(--amber); outline-offset: 2px; }}
    .info-panel {{
      position: absolute;
      left: 16px; bottom: 16px;
      z-index: 5;
      width: min(360px, calc(100% - 32px));
      padding: 12px;
      background: var(--panel-strong);
      border: 1px solid var(--line);
      border-radius: 8px;
      backdrop-filter: blur(12px);
    }}
    .info-panel h2 {{ margin: 0 0 6px; font-size: 1rem; }}
    .info-panel p {{ margin: 0; color: var(--muted); font-size: .88rem; line-height: 1.4; }}
    .legend {{
      display: grid;
      gap: 6px;
      margin: 10px 0 0;
      padding: 0;
      list-style: none;
    }}
    .legend li {{
      display: grid;
      grid-template-columns: 12px 1fr;
      gap: 8px;
      align-items: center;
      color: #eef3f6;
      font-size: .84rem;
    }}
    .swatch {{
      width: 12px; height: 12px;
      border-radius: 50%;
      border: 1px solid rgba(255,255,255,.36);
    }}
    .reference {{
      position: absolute;
      right: 16px; bottom: 16px;
      z-index: 5;
      width: min(220px, calc(100% - 32px));
      background: var(--panel-strong);
      border: 1px solid var(--line);
      border-radius: 8px;
      overflow: hidden;
      backdrop-filter: blur(12px);
      cursor: pointer;
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    .reference:hover {{
      transform: scale(1.02);
      border-color: var(--amber);
    }}
    .reference.expanded {{
      right: 50%; bottom: 50%;
      transform: translate(50%, 50%);
      width: min(85vw, 620px);
      z-index: 1000;
      box-shadow: 0 0 0 9999px rgba(0,0,0,.65), 0 24px 64px rgba(0,0,0,.5);
    }}
    .reference img {{
      display: block;
      width: 100%;
      height: auto;
      background: #fff;
    }}
    .reference strong {{
      display: block;
      padding: 8px 10px;
      color: #fff;
      font-size: .78rem;
    }}
    .hint {{
      position: absolute;
      left: 50%; bottom: 16px;
      z-index: 5;
      transform: translateX(-50%);
      padding: 7px 10px;
      color: #fff;
      background: rgba(0,0,0,.36);
      border: 1px solid var(--line);
      border-radius: 8px;
      backdrop-filter: blur(10px);
      font-size: .8rem;
      white-space: nowrap;
      pointer-events: none;
    }}
    @media (max-width: 760px) {{
      body {{ grid-template-columns: 48px 1fr; }}
      .sb {{ width: 40px; height: 34px; font-size: .76rem; }}
      .topbar {{ left: 10px; right: 10px; top: 10px; display: grid; gap: 8px; }}
      .title {{ padding: 10px; }}
      .toolbar {{ justify-content: flex-start; }}
      .info-panel {{ left: 10px; bottom: 10px; }}
      .reference {{ display: none; }}
      .reference.expanded {{ display: block; right: 50%; bottom: 50%; transform: translate(50%,50%); width: min(90vw, 400px); }}
      .hint {{ display: none; }}
    }}
  </style>
</head>
<body>
  <nav class="sidebar" id="sidebar" aria-label="Navegação de cenas"></nav>

  <div class="main-area">
    <canvas id="scene" aria-label="Modelo anatômico 3D interativo"></canvas>

    <header class="topbar">
      <section class="title">
        <p class="eyebrow" id="eyebrow">Cena 1 de 21</p>
        <h1 id="sceneTitle">Capa</h1>
        <p id="sceneSubtitle">Aula de Postura e Locomoção</p>
      </section>
      <nav class="toolbar" aria-label="Controles do modelo">
        <button id="prevScene" type="button">◀ Anterior</button>
        <button id="nextScene" type="button">Próxima ▶</button>
        <button id="autoBtn" type="button">Automático</button>
        <button id="labelsBtn" class="active" type="button">Rótulos</button>
        <button id="resetBtn" type="button">Centralizar</button>
        <button id="refBtn" type="button">Ver Lâmina</button>
      </nav>
    </header>

    <aside class="info-panel" id="infoPanel">
      <h2 id="infoTitle">Cena</h2>
      <p id="infoDesc">Descrição da cena</p>
      <ul class="legend" id="legend"></ul>
    </aside>

    <figure class="reference" id="refPanel">
      <img id="refImg" src="" alt="Lâmina de referência">
      <strong id="refLabel">Referência</strong>
    </figure>

    <div class="hint">Arraste para girar 360° · roda do mouse para zoom</div>
  </div>

  <script>{three}</script>
  <script>
    {slide_data_js}

    /* ===== GLOBAL STATE ===== */
    let currentScene = 0;
    let autoRotate = false;
    let labelsVisible = true;
    let distance = 6;
    let yaw = -0.55;
    let pitch = -0.18;
    let dragging = false;
    let startX = 0, startY = 0, startYaw = 0, startPitch = 0;

    /* ===== THREE.JS SETUP ===== */
    const canvas = document.getElementById("scene");
    const renderer = new THREE.WebGLRenderer({{ canvas, antialias: true, alpha: false }});
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
    renderer.outputEncoding = THREE.sRGBEncoding;
    renderer.shadowMap.enabled = true;

    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x0e141b);
    scene.fog = new THREE.Fog(0x0e141b, 8, 18);

    const camera = new THREE.PerspectiveCamera(42, 1, 0.1, 100);

    const root = new THREE.Group();
    scene.add(root);

    const labelGroup = new THREE.Group();
    root.add(labelGroup);

    /* ===== LIGHTING ===== */
    const ambient = new THREE.HemisphereLight(0xfff2db, 0x26394a, 0.75);
    scene.add(ambient);
    const keyLight = new THREE.DirectionalLight(0xffffff, 1.2);
    keyLight.position.set(3.6, 4.2, 4.5);
    keyLight.castShadow = true;
    keyLight.shadow.mapSize.set(1024, 1024);
    scene.add(keyLight);
    const rimLight = new THREE.PointLight(0x38b2ac, 1.4, 8);
    rimLight.position.set(-3.6, 1.8, -3.2);
    scene.add(rimLight);

    /* ===== MATERIALS PALETTE ===== */
    const MAT = {{
      brain:    new THREE.MeshStandardMaterial({{ color: 0xc99f68, roughness: 0.86 }}),
      wine:     new THREE.MeshStandardMaterial({{ color: 0xc94f56, roughness: 0.72 }}),
      green:    new THREE.MeshStandardMaterial({{ color: 0x2f9b63, roughness: 0.72 }}),
      teal:     new THREE.MeshStandardMaterial({{ color: 0x38b2ac, roughness: 0.72 }}),
      amber:    new THREE.MeshStandardMaterial({{ color: 0xe2a541, roughness: 0.72 }}),
      blue:     new THREE.MeshStandardMaterial({{ color: 0x4a90d9, roughness: 0.72 }}),
      purple:   new THREE.MeshStandardMaterial({{ color: 0x9b59b6, roughness: 0.72 }}),
      dark:     new THREE.MeshStandardMaterial({{ color: 0x2b1a10, roughness: 0.90 }}),
      sulcus:   new THREE.MeshStandardMaterial({{ color: 0x6b4829, roughness: 0.94 }}),
      base:     new THREE.MeshStandardMaterial({{ color: 0x1b2732, roughness: 0.85 }}),
      white:    new THREE.MeshStandardMaterial({{ color: 0xeeeeee, roughness: 0.70 }}),
      red:      new THREE.MeshStandardMaterial({{ color: 0xe74c3c, roughness: 0.72 }}),
      orange:   new THREE.MeshStandardMaterial({{ color: 0xe67e22, roughness: 0.72 }}),
      gold:     new THREE.MeshStandardMaterial({{ color: 0xf1c40f, roughness: 0.65 }}),
      pink:     new THREE.MeshStandardMaterial({{ color: 0xe08090, roughness: 0.72 }}),
      cyan:     new THREE.MeshStandardMaterial({{ color: 0x00bcd4, roughness: 0.72 }}),
      lime:     new THREE.MeshStandardMaterial({{ color: 0x8bc34a, roughness: 0.72 }}),
      grey:     new THREE.MeshStandardMaterial({{ color: 0x7f8c8d, roughness: 0.80 }}),
      muscle:   new THREE.MeshStandardMaterial({{ color: 0xd35400, roughness: 0.75 }}),
      lesion:   new THREE.MeshStandardMaterial({{ color: 0xff2222, roughness: 0.50, emissive: 0x661111 }}),
    }};

    /* ===== SHARED GEOMETRY HELPERS ===== */
    function addSphere(parent, x, y, z, radius, mat) {{
      const mesh = new THREE.Mesh(new THREE.SphereGeometry(radius, 32, 24), mat);
      mesh.position.set(x, y, z);
      mesh.castShadow = true;
      parent.add(mesh);
      return mesh;
    }}

    function addCylinder(parent, x, y, z, rTop, rBot, h, mat, rx, rz) {{
      const mesh = new THREE.Mesh(new THREE.CylinderGeometry(rTop, rBot, h, 32), mat);
      mesh.position.set(x, y, z);
      if (rx) mesh.rotation.x = rx;
      if (rz) mesh.rotation.z = rz;
      mesh.castShadow = true;
      parent.add(mesh);
      return mesh;
    }}

    function addBox(parent, x, y, z, w, h, d, mat) {{
      const mesh = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), mat);
      mesh.position.set(x, y, z);
      mesh.castShadow = true;
      parent.add(mesh);
      return mesh;
    }}

    function addTube(parent, points, radius, mat) {{
      const curve = new THREE.CatmullRomCurve3(points);
      const geom = new THREE.TubeGeometry(curve, 36, radius, 10, false);
      const mesh = new THREE.Mesh(geom, mat);
      mesh.castShadow = true;
      parent.add(mesh);
      return mesh;
    }}

    function addArrow(parent, from, to, radius, mat) {{
      const dir = new THREE.Vector3().subVectors(to, from);
      const len = dir.length();
      const mid = new THREE.Vector3().addVectors(from, to).multiplyScalar(0.5);
      const shaft = new THREE.Mesh(new THREE.CylinderGeometry(radius, radius, len * 0.8, 12), mat);
      shaft.position.copy(mid);
      shaft.lookAt(to);
      shaft.rotateX(Math.PI / 2);
      shaft.castShadow = true;
      parent.add(shaft);
      const head = new THREE.Mesh(new THREE.ConeGeometry(radius * 2.5, len * 0.2, 12), mat);
      head.position.copy(to);
      head.lookAt(new THREE.Vector3().addVectors(to, dir.normalize()));
      head.rotateX(Math.PI / 2);
      head.castShadow = true;
      parent.add(head);
      return shaft;
    }}

    function addBase(parent) {{
      const mesh = new THREE.Mesh(
        new THREE.CylinderGeometry(2.2, 2.4, 0.08, 96),
        MAT.base
      );
      mesh.position.y = -1.5;
      mesh.receiveShadow = true;
      parent.add(mesh);
      return mesh;
    }}

    if (!CanvasRenderingContext2D.prototype.roundRect) {{
      CanvasRenderingContext2D.prototype.roundRect = function(x, y, w, h, r) {{
        this.moveTo(x + r, y);
        this.arcTo(x + w, y, x + w, y + h, r);
        this.arcTo(x + w, y + h, x, y + h, r);
        this.arcTo(x, y + h, x, y, r);
        this.arcTo(x, y, x + w, y, r);
        return this;
      }};
    }}

    function labelTexture(text, color) {{
      const c = document.createElement("canvas");
      c.width = 512; c.height = 128;
      const ctx = c.getContext("2d");
      ctx.clearRect(0, 0, c.width, c.height);
      ctx.fillStyle = "rgba(14,20,27,.82)";
      ctx.strokeStyle = "rgba(255,255,255,.28)";
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.roundRect(8, 8, 496, 112, 18);
      ctx.fill(); ctx.stroke();
      ctx.fillStyle = color;
      ctx.font = "700 32px Arial, Helvetica, sans-serif";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText(text, 256, 64);
      const texture = new THREE.CanvasTexture(c);
      texture.encoding = THREE.sRGBEncoding;
      return texture;
    }}

    function addLabel(parent, text, pos, color) {{
      const mat = new THREE.SpriteMaterial({{ map: labelTexture(text, color), transparent: true, depthTest: false }});
      const sprite = new THREE.Sprite(mat);
      sprite.position.copy(pos);
      sprite.scale.set(1.2, 0.3, 1);
      labelGroup.add(sprite);
      return sprite;
    }}

    function addPointer(a, b) {{
      const mat = new THREE.LineBasicMaterial({{ color: 0xf0d38a, transparent: true, opacity: 0.75 }});
      const geom = new THREE.BufferGeometry().setFromPoints([a, b]);
      labelGroup.add(new THREE.Line(geom, mat));
    }}

    function addBrain(parent) {{
      /* Two hemispheres + fissure */
      const brainGrp = new THREE.Group();
      [-1, 1].forEach(side => {{
        const hemi = new THREE.Mesh(new THREE.SphereGeometry(1, 64, 40), MAT.brain);
        hemi.scale.set(1.18, 0.72, 1.02);
        hemi.position.x = side * 0.62;
        hemi.castShadow = true;
        brainGrp.add(hemi);
      }});
      const fissure = addBox(brainGrp, 0, 0.64, 0, 0.08, 0.075, 2.04, MAT.dark);
      parent.add(brainGrp);
      return brainGrp;
    }}

    function clearScene() {{
      while (root.children.length > 0) root.remove(root.children[0]);
      while (labelGroup.children.length > 0) labelGroup.remove(labelGroup.children[0]);
      root.add(labelGroup);
      root.rotation.set(0, 0, 0);
    }}

    /* ============================================================
       21 SCENE BUILDER FUNCTIONS
       ============================================================ */

    function buildScene1() {{
      /* Capa: Torus knot animado com esferas orbitais */
      const torusKnot = new THREE.Mesh(
        new THREE.TorusKnotGeometry(0.9, 0.3, 128, 24, 2, 3),
        new THREE.MeshStandardMaterial({{ color: 0x176b70, roughness: 0.4, metalness: 0.3 }})
      );
      torusKnot.castShadow = true;
      root.add(torusKnot);
      for (let i = 0; i < 8; i++) {{
        const angle = (i / 8) * Math.PI * 2;
        addSphere(root, Math.cos(angle) * 1.8, Math.sin(angle) * 0.6, Math.sin(angle) * 1.8, 0.12, MAT.amber);
      }}
      addBase(root);
      addLabel(root, "Postura e Locomoção", new THREE.Vector3(0, 1.8, 0), "#f4c772");
      return {{ title: "Capa", desc: "Nó tórico com esferas orbitais representando neurônios.", legend: [["#176b70","Nó tórico"],["#e2a541","Esferas orbitais"]] }};
    }}

    function buildScene2() {{
      /* Introdução: Pilha CNS vertical */
      addSphere(root, 0, 1.2, 0, 0.6, MAT.brain);
      addLabel(root, "Córtex", new THREE.Vector3(1.4, 1.4, 0), "#ffb4b9");
      addPointer(new THREE.Vector3(1, 1.3, 0), new THREE.Vector3(0.6, 1.2, 0));
      addCylinder(root, 0, 0.3, 0, 0.22, 0.18, 0.7, MAT.teal);
      addLabel(root, "Tronco", new THREE.Vector3(-1.4, 0.35, 0), "#7ee8d3");
      addPointer(new THREE.Vector3(-1, 0.35, 0), new THREE.Vector3(-0.22, 0.3, 0));
      addCylinder(root, 0, -0.5, 0, 0.18, 0.14, 0.8, MAT.green);
      addLabel(root, "Medula", new THREE.Vector3(1.4, -0.45, 0), "#9af0bf");
      addPointer(new THREE.Vector3(1, -0.45, 0), new THREE.Vector3(0.18, -0.5, 0));
      addBox(root, 0, -1.2, 0, 0.8, 0.35, 0.4, MAT.muscle);
      addLabel(root, "Músculo", new THREE.Vector3(-1.4, -1.15, 0), "#f0a86e");
      addPointer(new THREE.Vector3(-1, -1.15, 0), new THREE.Vector3(-0.4, -1.2, 0));
      addArrow(root, new THREE.Vector3(0.3, 0.85, 0), new THREE.Vector3(0.3, 0.5, 0), 0.04, MAT.amber);
      addArrow(root, new THREE.Vector3(-0.25, -0.05, 0), new THREE.Vector3(-0.25, -0.4, 0), 0.04, MAT.amber);
      addArrow(root, new THREE.Vector3(0.3, -0.75, 0), new THREE.Vector3(0.3, -1.0, 0), 0.04, MAT.amber);
      addBase(root);
      return {{ title: "Introdução ao Sistema Motor", desc: "Pilha CNS: Córtex → Tronco → Medula → Músculo. Setas indicam o fluxo descendente de comandos motores.", legend: [["#c99f68","Córtex"],["#38b2ac","Tronco encefálico"],["#2f9b63","Medula espinhal"],["#d35400","Músculo"]] }};
    }}

    function buildScene3() {{
      /* Organização: NMS → sinapse → NMI → músculo */
      addSphere(root, -1.2, 0.8, 0, 0.35, MAT.wine);
      addLabel(root, "NMS", new THREE.Vector3(-1.2, 1.5, 0), "#ffb4b9");
      addPointer(new THREE.Vector3(-1.2, 1.3, 0), new THREE.Vector3(-1.2, 1.15, 0));
      const synPts = [new THREE.Vector3(-1.2, 0.45, 0), new THREE.Vector3(-0.4, 0, 0), new THREE.Vector3(0.4, 0, 0)];
      addTube(root, synPts, 0.04, MAT.amber);
      addSphere(root, 0, 0, 0, 0.15, MAT.gold);
      addLabel(root, "Sinapse", new THREE.Vector3(0, 0.55, 0), "#f4c772");
      const nmiPts = [new THREE.Vector3(0.4, 0, 0), new THREE.Vector3(1.2, -0.3, 0)];
      addTube(root, nmiPts, 0.04, MAT.teal);
      addSphere(root, 1.2, -0.3, 0, 0.35, MAT.teal);
      addLabel(root, "NMI", new THREE.Vector3(1.2, 0.3, 0), "#7ee8d3");
      addPointer(new THREE.Vector3(1.2, 0.15, 0), new THREE.Vector3(1.2, 0.05, 0));
      addArrow(root, new THREE.Vector3(1.2, -0.65, 0), new THREE.Vector3(1.2, -1.0, 0), 0.04, MAT.amber);
      addBox(root, 1.2, -1.2, 0, 0.7, 0.3, 0.35, MAT.muscle);
      addLabel(root, "Músculo", new THREE.Vector3(1.2, -0.75, 0.6), "#f0a86e");
      addBase(root);
      return { title: "Organização do Sistema Motor", desc: "Cadeia: NMS (vinho) → sinapse → NMI (teal) → músculo. Feedback sensorial não mostrado.", legend: [["#c94f56","NMS"],["#f1c40f","Sinapse"],["#38b2ac","NMI"],["#d35400","Músculo"]] };
    }

    function buildScene4() {
      /* Córtex motor: Cérebro com M1 destacada */
      const brain = addBrain(root);
      /* M1 strip on both hemispheres - Coronal orientation */
      [-1, 1].forEach(side => {
        const pts = [];
        for (let i = 0; i <= 30; i++) {
          const t = i / 30;
          const x = side * (0.05 + t * 1.62);
          const z = 0.15 - side * 0.05 * (1 - t) + Math.sin(t * Math.PI * 2) * 0.04;
          const rx = x - side * 0.62;
          const nx = rx / 1.18;
          const nz = z / 1.02;
          const y = Math.sqrt(Math.max(0.01, 1 - nx * nx - nz * nz)) * 0.72 + 0.055;
          pts.push(new THREE.Vector3(x, y, z));
        }
        addTube(root, pts, 0.06, MAT.wine);
      });
      addLabel(root, "M1 — Córtex Motor Primário", new THREE.Vector3(0, 1.35, 0), "#ffb4b9");
      addLabel(root, "Giro pré-central", new THREE.Vector3(-1.8, 0.6, 0.3), "#f4c772");
      addPointer(new THREE.Vector3(-1.4, 0.55, 0.3), new THREE.Vector3(-0.62, 0.78, 0.21));
      addBase(root);
      return { title: "Córtex Motor", desc: "Cérebro com faixa do giro pré-central (M1) destacada em vinho. A M1 é a principal origem de comandos voluntários.", legend: [["#c99f68","Córtex"],["#c94f56","M1 — Motor primário"],["#2b1a10","Fissura longitudinal"]] };
    }

    function buildScene5() {
      /* Áreas Corticais — modelo existente expandido */
      const brain = addBrain(root);
      /* Motor + sensorial bands - Coronal orientation */
      [-1, 1].forEach(side => {
        [0.16, -0.12].forEach((zBase, bi) => {
          const mat = bi === 0 ? MAT.wine : MAT.green;
          const pts = [];
          for (let i = 0; i <= 34; i++) {
            const t = i / 34;
            const x = side * (0.05 + t * 1.62);
            const wave = Math.sin(t * Math.PI * 2.5 + side * 0.45) * 0.04;
            const z = zBase - side * 0.05 * (1 - t) + wave;
            const rx = x - side * 0.62;
            const nx = rx / 1.18;
            const nz = z / 1.02;
            const y = Math.sqrt(Math.max(0.02, 1 - nx * nx - nz * nz)) * 0.72 + 0.055;
            pts.push(new THREE.Vector3(x, y, z));
          }
          addTube(root, pts, 0.055, mat);
        });
      });
      /* Cerebellum */
      const cb = addSphere(root, 0, -0.38, -0.68, 0.44, MAT.brain);
      cb.scale.set(1.05, 0.6, 0.75);
      /* Brainstem */
      addCylinder(root, 0, -0.45, -0.15, 0.24, 0.16, 0.85, MAT.brain, 0.12, 0);
      /* Labels */
      addLabel(root, "Área motora", new THREE.Vector3(-1.8, 1.22, -0.25), "#ffb4b9");
      addLabel(root, "Área sensorial", new THREE.Vector3(1.85, 1.16, 0.28), "#9af0bf");
      addLabel(root, "Cerebelo", new THREE.Vector3(1.6, -0.42, -0.85), "#d7b07c");
      addLabel(root, "Tronco", new THREE.Vector3(-1.6, -0.5, 0.1), "#f1d39a");
      addPointer(new THREE.Vector3(-1.3, 1.0, 0.1), new THREE.Vector3(-0.62, 0.78, 0.21));
      addPointer(new THREE.Vector3(1.3, 0.98, -0.1), new THREE.Vector3(0.7, 0.77, -0.19));
      addPointer(new THREE.Vector3(1.15, -0.42, -0.78), new THREE.Vector3(0.38, -0.38, -0.68));
      addPointer(new THREE.Vector3(-1.15, -0.5, 0.08), new THREE.Vector3(-0.16, -0.45, -0.15));
      addBase(root);
      return { title: "Áreas Corticais em 360°", desc: "Modelo completo: faixas motora e sensorial, cerebelo e tronco encefálico.", legend: [["#c94f56","Área motora"],["#2f9b63","Área sensorial"],["#c99f68","Córtex/cerebelo"],["#2b1a10","Fissura"]] };
    }

    function buildScene6() {
      /* Homúnculo: Corte coronal do córtex com o homúnculo mapeado */
      
      const MAT_H = {
        whiteMatter: new THREE.MeshStandardMaterial({ color: 0xf5ebd5, roughness: 0.85 }),
        greyMatter:  new THREE.MeshStandardMaterial({ color: 0xd2b48c, roughness: 0.75 }),
        skin:        new THREE.MeshStandardMaterial({ color: 0xf0d5c0, roughness: 0.65 }),
        lips:        new THREE.MeshStandardMaterial({ color: 0xe57373, roughness: 0.60 }),
        tongue:      new THREE.MeshStandardMaterial({ color: 0xff5252, roughness: 0.50, emissive: 0x441111 }),
        eyeWhite:    new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.40 }),
        eyeIris:     new THREE.MeshStandardMaterial({ color: 0x4e342e, roughness: 0.50 }),
        eyePupil:    new THREE.MeshStandardMaterial({ color: 0x000000, roughness: 0.10 })
      };

      // Desenha o fatiado do hemisfério (white matter interior)
      // Usando Shape e ExtrudeGeometry para criar um bloco 3D sólido de hemisfério
      const shape = new THREE.Shape();
      shape.moveTo(-0.5, -1.2);
      shape.lineTo(-0.5, 0.9);
      shape.quadraticCurveTo(-0.5, 1.25, -0.2, 1.25);
      
      // Ondulações de giros e sulcos
      shape.quadraticCurveTo(0.0, 1.3, 0.18, 1.15); // sulco 1
      shape.quadraticCurveTo(0.35, 1.35, 0.5, 1.2); // giro 1
      shape.quadraticCurveTo(0.65, 1.0, 0.8, 1.15); // sulco 2
      shape.quadraticCurveTo(0.95, 1.3, 1.1, 0.95); // giro 2 (mão)
      
      // Fissura lateral / Sulco de Sylvius (profundo)
      shape.quadraticCurveTo(1.2, 0.75, 0.95, 0.65);
      shape.quadraticCurveTo(0.7, 0.55, 0.9, 0.4);
      
      // Lobo temporal
      shape.quadraticCurveTo(1.25, 0.25, 1.15, -0.15);
      shape.quadraticCurveTo(1.05, -0.55, 0.65, -0.75);
      shape.lineTo(0.0, -0.75);
      shape.lineTo(-0.5, -1.2);

      const extrudeSettings = {
        depth: 0.3,
        bevelEnabled: true,
        bevelSegments: 4,
        steps: 1,
        bevelSize: 0.02,
        bevelThickness: 0.02
      };
      
      const geom = new THREE.ExtrudeGeometry(shape, extrudeSettings);
      const mesh = new THREE.Mesh(geom, MAT_H.whiteMatter);
      mesh.position.z = -0.15; // centralizar em Z
      mesh.receiveShadow = true;
      mesh.castShadow = true;
      root.add(mesh);

      // Fita externa do córtex (Grey matter ribbon) usando tubos para contornar
      const borderPts = [
        new THREE.Vector3(-0.5, -1.2, 0.15),
        new THREE.Vector3(-0.5, 0.9, 0.15),
        new THREE.Vector3(-0.2, 1.25, 0.15),
        new THREE.Vector3(0.0, 1.3, 0.15),
        new THREE.Vector3(0.18, 1.15, 0.15),
        new THREE.Vector3(0.35, 1.35, 0.15),
        new THREE.Vector3(0.5, 1.2, 0.15),
        new THREE.Vector3(0.65, 1.0, 0.15),
        new THREE.Vector3(0.8, 1.15, 0.15),
        new THREE.Vector3(0.95, 1.3, 0.15),
        new THREE.Vector3(1.1, 0.95, 0.15),
        new THREE.Vector3(0.95, 0.65, 0.15),
        new THREE.Vector3(0.9, 0.4, 0.15),
        new THREE.Vector3(1.15, 0.25, 0.15),
        new THREE.Vector3(1.15, -0.15, 0.15),
        new THREE.Vector3(0.65, -0.75, 0.15)
      ];
      addTube(root, borderPts, 0.075, MAT_H.greyMatter);

      // 1. Membro Inferior (Perna e Pé hanging no córtex medial)
      const legGroup = new THREE.Group();
      // Hip joint
      addSphere(legGroup, -0.1, 1.22, 0.15, 0.05, MAT_H.skin);
      // Thigh (horizontal cylinder)
      addCylinder(legGroup, -0.3, 1.22, 0.15, 0.045, 0.045, 0.4, MAT_H.skin, 0, 0, Math.PI / 2);
      // Knee
      addSphere(legGroup, -0.5, 1.22, 0.15, 0.045, MAT_H.skin);
      // Shin (vertical cylinder, hanging down)
      addCylinder(legGroup, -0.5, 0.9, 0.15, 0.038, 0.038, 0.64, MAT_H.skin);
      // Ankle
      addSphere(legGroup, -0.5, 0.58, 0.15, 0.03, MAT_H.skin);
      // Foot (horizontal box pointing left/out)
      addBox(legGroup, -0.58, 0.58, 0.15, 0.16, 0.035, 0.06, MAT_H.skin);
      root.add(legGroup);

      // 2. Torso (Tronco e braço no topo do córtex)
      const bodyGroup = new THREE.Group();
      // Torso (horizontal cylinder)
      addCylinder(bodyGroup, 0.15, 1.3, 0.15, 0.06, 0.06, 0.3, MAT_H.skin, 0, 0, Math.PI / 2);
      // Shoulder
      addSphere(bodyGroup, 0.3, 1.3, 0.15, 0.05, MAT_H.skin);
      // Neck & Head
      addCylinder(bodyGroup, 0.15, 1.38, 0.15, 0.03, 0.03, 0.1, MAT_H.skin);
      addSphere(bodyGroup, 0.15, 1.48, 0.15, 0.07, MAT_H.skin);
      // Arm (drapes down along the sulcus 1/giro 1 border)
      addCylinder(bodyGroup, 0.38, 1.18, 0.15, 0.025, 0.025, 0.28, MAT_H.skin, 0, 0, -Math.PI / 6);
      root.add(bodyGroup);

      // 3. Mão Gigante (Lateral do córtex, tamanho exagerado)
      addCylinder(root, 0.88, 1.05, 0.15, 0.035, 0.035, 0.24, MAT_H.skin, 0, 0, -Math.PI / 4);
      const handGroup = new THREE.Group();
      handGroup.position.set(1.02, 0.92, 0.15);
      handGroup.rotation.z = -Math.PI / 5;
      const palm = addSphere(handGroup, 0, 0, 0, 0.11, MAT_H.skin);
      palm.scale.set(1.1, 0.5, 1.2);
      // 5 dedos longos e articulados
      const fingerData = [
        { angle: 0.6, len: 0.12, bend: 0.4 },
        { angle: 0.2, len: 0.18, bend: 0.5 },
        { angle: -0.1, len: 0.20, bend: 0.5 },
        { angle: -0.4, len: 0.18, bend: 0.5 },
        { angle: -0.7, len: 0.14, bend: 0.4 }
      ];
      fingerData.forEach(f => {
        const bx = Math.cos(f.angle) * 0.08;
        const bz = Math.sin(f.angle) * 0.08;
        addSphere(handGroup, bx, 0, bz, 0.025, MAT_H.skin);
        
        const sx = bx + Math.cos(f.angle) * f.len * 0.4;
        const sy = -f.len * 0.2;
        const sz = bz + Math.sin(f.angle) * f.len * 0.4;
        addCylinder(handGroup, sx, sy, sz, 0.018, 0.016, f.len * 0.8, MAT_H.skin, 0.2, 0, f.angle + Math.PI/2);
        
        const tx = sx + Math.cos(f.angle - f.bend) * f.len * 0.4;
        const ty = sy - f.len * 0.6;
        const tz = sz + Math.sin(f.angle - f.bend) * f.len * 0.4;
        addSphere(handGroup, sx + Math.cos(f.angle) * f.len * 0.4, sy - f.len * 0.1, sz + Math.sin(f.angle) * f.len * 0.4, 0.018, MAT_H.skin);
        addCylinder(handGroup, tx, ty, tz, 0.015, 0.012, f.len * 0.8, MAT_H.skin, 0.6, 0, f.angle - f.bend + Math.PI/2);
      });
      root.add(handGroup);

      // 4. Face Gigante (Perfil e partes modeladas)
      const profileShape = new THREE.Shape();
      profileShape.moveTo(0.95, 0.4);
      profileShape.quadraticCurveTo(1.15, 0.38, 1.2, 0.3); // forehead
      profileShape.lineTo(1.12, 0.15); // eye indent
      profileShape.lineTo(1.28, 0.05); // nose tip
      profileShape.lineTo(1.14, -0.05); // under nose
      profileShape.quadraticCurveTo(1.28, -0.15, 1.22, -0.22); // upper lip
      profileShape.quadraticCurveTo(1.28, -0.3, 1.16, -0.34); // lower lip
      profileShape.quadraticCurveTo(1.22, -0.42, 1.14, -0.48); // chin
      profileShape.lineTo(0.95, -0.52);
      profileShape.lineTo(0.95, 0.4);

      const faceGeom = new THREE.ExtrudeGeometry(profileShape, {
        depth: 0.2,
        bevelEnabled: true,
        bevelSegments: 3,
        steps: 1,
        bevelSize: 0.015,
        bevelThickness: 0.015
      });
      const faceMesh = new THREE.Mesh(faceGeom, MAT_H.skin);
      faceMesh.position.z = -0.1;
      faceMesh.castShadow = true;
      faceMesh.receiveShadow = true;
      root.add(faceMesh);

      // Globo ocular
      addSphere(root, 1.12, 0.22, 0.12, 0.06, MAT_H.eyeWhite);
      addSphere(root, 1.15, 0.22, 0.16, 0.03, MAT_H.eyeIris);
      addSphere(root, 1.16, 0.22, 0.18, 0.015, MAT_H.eyePupil);

      // Lábios
      const upperLip = addSphere(root, 1.2, -0.18, 0.1, 0.045, MAT_H.lips);
      upperLip.scale.set(1.4, 0.5, 0.8);
      const lowerLip = addSphere(root, 1.18, -0.28, 0.1, 0.045, MAT_H.lips);
      lowerLip.scale.set(1.4, 0.5, 0.8);

      // Língua
      const tonguePts = [
        new THREE.Vector3(1.15, -0.24, 0.1),
        new THREE.Vector3(1.26, -0.26, 0.1),
        new THREE.Vector3(1.34, -0.38, 0.1)
      ];
      addTube(root, tonguePts, 0.048, MAT_H.tongue);

      // Rótulos / Linhas de Chamada
      addLabel(root, "Genitais / Pé", new THREE.Vector3(-1.3, -0.8, 0), "#e2a541");
      addPointer(new THREE.Vector3(-0.95, -0.8, 0), new THREE.Vector3(-0.5, -0.8, 0.15));

      addLabel(root, "Perna / Quadril", new THREE.Vector3(-1.3, 0.2, 0), "#38b2ac");
      addPointer(new THREE.Vector3(-0.95, 0.2, 0), new THREE.Vector3(-0.5, 0.4, 0.15));

      addLabel(root, "Torso / Braço", new THREE.Vector3(-0.2, 1.75, 0), "#c99f68");
      addPointer(new THREE.Vector3(-0.2, 1.6, 0), new THREE.Vector3(0.2, 1.3, 0.15));

      addLabel(root, "Mão (Exagerada)", new THREE.Vector3(1.5, 1.4, 0.2), "#f4c772");
      addPointer(new THREE.Vector3(1.4, 1.25, 0.2), new THREE.Vector3(1.05, 0.88, 0.15));

      addLabel(root, "Olho / Nariz", new THREE.Vector3(1.8, 0.35, 0.2), "#4a90d9");
      addPointer(new THREE.Vector3(1.42, 0.35, 0.2), new THREE.Vector3(1.12, 0.28, 0.18));

      addLabel(root, "Lábios / Boca", new THREE.Vector3(1.8, -0.15, 0.2), "#c94f56");
      addPointer(new THREE.Vector3(1.42, -0.15, 0.2), new THREE.Vector3(1.15, -0.16, 0.22));

      addLabel(root, "Língua / Faringe", new THREE.Vector3(1.8, -0.65, 0.2), "#ff6666");
      addPointer(new THREE.Vector3(1.42, -0.65, 0.2), new THREE.Vector3(1.22, -0.22, 0.22));

      addBase(root);
      return {
        title: "Homúnculo Sensorial",
        desc: "Corte coronal do córtex com o homúnculo correspondente: a face, os lábios, a língua e as mãos possuem representação ampliada devido à alta densidade de receptores sensoriais.",
        legend: [
          ["#f5ebd5", "Substância Branca"],
          ["#d2b48c", "Substância Cinzenta (Córtex)"],
          ["#f0d5c0", "Partes do Corpo"],
          ["#e57373", "Boca e Lábios"],
          ["#ff5252", "Língua"]
        ]
      };
    }

    function buildScene7() {
      /* Áreas motoras: cérebro com 3 zonas */
      const brain = addBrain(root);
      /* M1 - Coronal orientation */
      [-1, 1].forEach(side => {
        const pts = [];
        for (let i = 0; i <= 20; i++) {
          const t = i / 20;
          const x = side * (0.05 + t * 1.62);
          const z = 0.16 - side * 0.05 * (1 - t) + Math.sin(t * Math.PI * 2) * 0.03;
          const rx = x - side * 0.62;
          const nx = rx / 1.18;
          const nz = z / 1.02;
          const y = Math.sqrt(Math.max(0.01, 1 - nx * nx - nz * nz)) * 0.72 + 0.06;
          pts.push(new THREE.Vector3(x, y, z));
        }
        addTube(root, pts, 0.06, MAT.wine);
      });
      /* PMC — pré-motora - Coronal orientation, anterior to M1 */
      [-1, 1].forEach(side => {
        const pts = [];
        for (let i = 0; i <= 20; i++) {
          const t = i / 20;
          const x = side * (0.05 + t * 1.62);
          const z = 0.44 - side * 0.05 * (1 - t) + Math.sin(t * Math.PI * 2) * 0.03;
          const rx = x - side * 0.62;
          const nx = rx / 1.18;
          const nz = z / 1.02;
          const y = Math.sqrt(Math.max(0.01, 1 - nx * nx - nz * nz)) * 0.72 + 0.05;
          pts.push(new THREE.Vector3(x, y, z));
        }
        addTube(root, pts, 0.05, MAT.blue);
      });
      /* SMA — suplementar (medial) */
      const smapts = [];
      for (let i = 0; i <= 20; i++) {
        const t = i / 20;
        const z = -0.3 + t * 0.6;
        smapts.push(new THREE.Vector3(0, 0.72 + 0.02, z));
      }
      addTube(root, smapts, 0.05, MAT.purple);
      addLabel(root, "M1 — Primária", new THREE.Vector3(-1.8, 1.1, 0.16), "#ffb4b9");
      addLabel(root, "PMC — Pré-motora", new THREE.Vector3(1.8, 0.9, 0.44), "#8cb4e8");
      addLabel(root, "SMA — Suplementar", new THREE.Vector3(0, 1.4, 0.1), "#c9a3d9");
      addBase(root);
      return { title: "Áreas Motoras", desc: "Cérebro com 3 zonas: M1 (vermelho), PMC pré-motora (azul) e SMA suplementar (roxo).", legend: [["#c94f56","M1 — Primária"],["#4a90d9","PMC — Pré-motora"],["#9b59b6","SMA — Suplementar"]] };
    }

    function buildScene8() {
      /* Feixe CE: via vertical com decussação */
      addSphere(root, 0, 2.0, 0, 0.5, MAT.brain);
      addLabel(root, "Córtex", new THREE.Vector3(1.2, 2.1, 0), "#d7b07c");
      /* Descending tract */
      const tract1 = [new THREE.Vector3(0, 1.5, 0), new THREE.Vector3(0, 0.6, 0)];
      addTube(root, tract1, 0.06, MAT.wine);
      /* Tronco */
      addCylinder(root, 0, 0.2, 0, 0.35, 0.3, 0.6, MAT.teal);
      addLabel(root, "Tronco", new THREE.Vector3(-1.3, 0.2, 0), "#7ee8d3");
      /* Decussation X */
      const decL = [new THREE.Vector3(-0.25, -0.2, 0), new THREE.Vector3(0.25, -0.6, 0)];
      const decR = [new THREE.Vector3(0.25, -0.2, 0), new THREE.Vector3(-0.25, -0.6, 0)];
      addTube(root, decL, 0.04, MAT.wine);
      addTube(root, decR, 0.04, MAT.amber);
      addLabel(root, "Decussação", new THREE.Vector3(1.3, -0.4, 0), "#f4c772");
      addPointer(new THREE.Vector3(0.9, -0.4, 0), new THREE.Vector3(0.25, -0.4, 0));
      /* Medula */
      addCylinder(root, 0, -1.1, 0, 0.2, 0.15, 0.8, MAT.green);
      addLabel(root, "Medula", new THREE.Vector3(-1.3, -1.1, 0), "#9af0bf");
      addBase(root);
      return {{ title: "Feixe Corticoespinal", desc: "Via voluntária principal. O X marca a decussação das pirâmides no bulbo.", legend: [["#c94f56","Via corticoespinal"],["#e2a541","Cruzamento (decussação)"],["#c99f68","Córtex"],["#38b2ac","Tronco"],["#2f9b63","Medula"]] }};
    }}

    function buildScene9() {{
      /* Org. CE com interneurônios */
      addSphere(root, 0, 2.0, 0, 0.45, MAT.brain);
      addLabel(root, "Córtex", new THREE.Vector3(1.2, 2.1, 0), "#d7b07c");
      addTube(root, [new THREE.Vector3(0, 1.55, 0), new THREE.Vector3(0, 0.6, 0)], 0.05, MAT.wine);
      addCylinder(root, 0, 0.2, 0, 0.3, 0.25, 0.5, MAT.teal);
      addLabel(root, "Tronco", new THREE.Vector3(-1.3, 0.2, 0), "#7ee8d3");
      addTube(root, [new THREE.Vector3(0, -0.05, 0), new THREE.Vector3(0, -0.7, 0)], 0.05, MAT.wine);
      addCylinder(root, 0, -1.0, 0, 0.2, 0.15, 0.5, MAT.green);
      addLabel(root, "Medula", new THREE.Vector3(-1.3, -1.0, 0), "#9af0bf");
      /* Interneurônios */
      addSphere(root, 0.35, -0.85, 0, 0.12, MAT.gold);
      addSphere(root, -0.35, -0.95, 0, 0.12, MAT.gold);
      addSphere(root, 0.25, -1.1, 0, 0.1, MAT.gold);
      addLabel(root, "Interneurônios", new THREE.Vector3(1.3, -0.9, 0), "#f4c772");
      addPointer(new THREE.Vector3(0.9, -0.85, 0), new THREE.Vector3(0.47, -0.85, 0));
      /* Músculo */
      addBox(root, 0, -1.6, 0, 0.7, 0.3, 0.35, MAT.muscle);
      addLabel(root, "Músculo", new THREE.Vector3(0, -1.15, 0.6), "#f0a86e");
      addArrow(root, new THREE.Vector3(0, -1.25, 0), new THREE.Vector3(0, -1.42, 0), 0.03, MAT.amber);
      addBase(root);
      return {{ title: "Organização Corticoespinal", desc: "Via com interneurônios (dourados) na medula que modulam o sinal antes do músculo.", legend: [["#c94f56","Via CE"],["#f1c40f","Interneurônios"],["#c99f68","Córtex"],["#38b2ac","Tronco"],["#2f9b63","Medula"],["#d35400","Músculo"]] }};
    }}

    function buildScene10() {{
      /* Diagrama CE: 5 caixas empilhadas com setas */
      const labels = ["Córtex Motor", "Tronco Encefálico", "Decussação (Bulbo)", "Medula Espinhal", "Músculo"];
      const colors = [MAT.brain, MAT.teal, MAT.amber, MAT.green, MAT.muscle];
      const labelColors = ["#d7b07c", "#7ee8d3", "#f4c772", "#9af0bf", "#f0a86e"];
      for (let i = 0; i < 5; i++) {{
        const y = 1.5 - i * 0.8;
        addBox(root, 0, y, 0, 1.4, 0.5, 0.6, colors[i]);
        addLabel(root, labels[i], new THREE.Vector3(0, y, 0.5), labelColors[i]);
        if (i < 4) {{
          addArrow(root, new THREE.Vector3(0, y - 0.25, 0.35), new THREE.Vector3(0, y - 0.55, 0.35), 0.04, MAT.white);
        }}
      }}
      addBase(root);
      return {{ title: "Diagrama da Via Corticoespinal", desc: "5 etapas: Córtex → Tronco → Decussação → Medula → Músculo.", legend: [["#c99f68","Córtex"],["#38b2ac","Tronco"],["#e2a541","Decussação"],["#2f9b63","Medula"],["#d35400","Músculo"]] }};
    }}

    function buildScene11() {{
      /* Tronco Encefálico: 3 segmentos + cerebelo */
      addCylinder(root, 0, 0.85, 0, 0.32, 0.30, 0.55, MAT.purple);
      addLabel(root, "Mesencéfalo", new THREE.Vector3(1.4, 0.9, 0), "#c9a3d9");
      addPointer(new THREE.Vector3(1, 0.85, 0), new THREE.Vector3(0.32, 0.85, 0));
      addCylinder(root, 0, 0.25, 0, 0.35, 0.32, 0.55, MAT.blue);
      addLabel(root, "Ponte", new THREE.Vector3(-1.4, 0.3, 0), "#8cb4e8");
      addPointer(new THREE.Vector3(-1, 0.25, 0), new THREE.Vector3(-0.35, 0.25, 0));
      addCylinder(root, 0, -0.35, 0, 0.30, 0.22, 0.55, MAT.teal);
      addLabel(root, "Bulbo", new THREE.Vector3(1.4, -0.3, 0), "#7ee8d3");
      addPointer(new THREE.Vector3(1, -0.35, 0), new THREE.Vector3(0.3, -0.35, 0));
      /* Cerebelo */
      const cb = addSphere(root, 0, 0.15, -0.65, 0.45, MAT.brain);
      cb.scale.set(1.2, 0.6, 0.8);
      addLabel(root, "Cerebelo", new THREE.Vector3(0, 0.15, -1.5), "#d7b07c");
      addPointer(new THREE.Vector3(0, 0.15, -1.2), new THREE.Vector3(0, 0.15, -0.9));
      addBase(root);
      return {{ title: "Tronco Encefálico", desc: "3 segmentos coloridos: Mesencéfalo (roxo), Ponte (azul), Bulbo (teal) + cerebelo.", legend: [["#9b59b6","Mesencéfalo"],["#4a90d9","Ponte"],["#38b2ac","Bulbo"],["#c99f68","Cerebelo"]] }};
    }}

    function buildScene12() {{
      /* Vias Descendentes: CE lateral vs Rubroespinal */
      /* Left: CE lateral */
      const ceTop = new THREE.Vector3(-0.6, 1.5, 0);
      const ceBot = new THREE.Vector3(-0.6, -1.3, 0);
      addTube(root, [ceTop, ceBot], 0.07, MAT.wine);
      addLabel(root, "CE Lateral", new THREE.Vector3(-0.6, 1.8, 0), "#ffb4b9");
      /* Right: Rubroespinal */
      const ruTop = new THREE.Vector3(0.6, 1.5, 0);
      const ruBot = new THREE.Vector3(0.6, -1.3, 0);
      addTube(root, [ruTop, ruBot], 0.07, MAT.amber);
      addLabel(root, "Rubroespinal", new THREE.Vector3(0.6, 1.8, 0), "#f4c772");
      /* Medula spine */
      addCylinder(root, 0, -0.2, 0, 0.15, 0.12, 3.0, MAT.grey);
      addLabel(root, "Medula", new THREE.Vector3(1.5, -0.5, 0), "#bbb");
      addPointer(new THREE.Vector3(1.2, -0.5, 0), new THREE.Vector3(0.15, -0.5, 0));
      addBase(root);
      return {{ title: "Vias Descendentes", desc: "Duas vias paralelas: CE lateral (vinho) para movimentos finos vs Rubroespinal (âmbar) para flexores.", legend: [["#c94f56","CE Lateral"],["#e2a541","Rubroespinal"],["#7f8c8d","Medula"]] }};
    }}

    function buildScene13() {{
      /* Extrapiramidais: 3 vias divergindo do tronco */
      addCylinder(root, 0, 0.5, 0, 0.35, 0.28, 1.2, MAT.teal);
      addLabel(root, "Tronco Encefálico", new THREE.Vector3(0, 1.4, 0), "#7ee8d3");
      /* Vestibuloespinal */
      addTube(root, [new THREE.Vector3(-0.2, -0.1, 0), new THREE.Vector3(-1.2, -1.3, -0.3)], 0.05, MAT.blue);
      addLabel(root, "Vestibuloespinal", new THREE.Vector3(-1.8, -1.0, -0.3), "#8cb4e8");
      /* Reticuloespinal */
      addTube(root, [new THREE.Vector3(0, -0.1, 0), new THREE.Vector3(0, -1.3, 0.3)], 0.05, MAT.green);
      addLabel(root, "Reticuloespinal", new THREE.Vector3(0, -1.6, 0.5), "#9af0bf");
      /* Rubroespinal */
      addTube(root, [new THREE.Vector3(0.2, -0.1, 0), new THREE.Vector3(1.2, -1.3, -0.3)], 0.05, MAT.amber);
      addLabel(root, "Rubroespinal", new THREE.Vector3(1.8, -1.0, -0.3), "#f4c772");
      addBase(root);
      return {{ title: "Vias Extrapiramidais", desc: "Tronco central com 3 vias divergindo: vestibuloespinal, reticuloespinal e rubroespinal.", legend: [["#4a90d9","Vestibuloespinal"],["#2f9b63","Reticuloespinal"],["#e2a541","Rubroespinal"],["#38b2ac","Tronco"]] }};
    }}

    function buildScene14() {{
      /* Núcleos do Tronco: esferas de nervos cranianos */
      addCylinder(root, 0, 0, 0, 0.35, 0.22, 2.5, MAT.teal);
      addLabel(root, "Tronco Encefálico", new THREE.Vector3(0, 1.6, 0), "#7ee8d3");
      const cranialNerves = [
        [0.4, 0.9, 0.15, "III — Oculomotor", MAT.purple],
        [-0.4, 0.6, 0.2, "V — Trigêmeo", MAT.blue],
        [0.4, 0.3, 0.15, "VII — Facial", MAT.amber],
        [-0.4, 0, 0.2, "IX — Glossofaríngeo", MAT.green],
        [0.4, -0.3, 0.15, "X — Vago", MAT.wine],
        [-0.4, -0.6, 0.15, "XII — Hipoglosso", MAT.gold],
      ];
      cranialNerves.forEach(([x, y, z, name, mat]) => {{
        addSphere(root, x, y, z, 0.12, mat);
        addLabel(root, name, new THREE.Vector3(x > 0 ? 1.5 : -1.5, y, z), x > 0 ? "#c9a3d9" : "#8cb4e8");
        addPointer(new THREE.Vector3(x > 0 ? 1.1 : -1.1, y, z), new THREE.Vector3(x > 0 ? 0.52 : -0.52, y, z));
      }});
      addBase(root);
      return {{ title: "Núcleos do Tronco Encefálico", desc: "Esferas marcando posição dos nervos cranianos no tronco.", legend: [["#9b59b6","III Oculomotor"],["#4a90d9","V Trigêmeo"],["#e2a541","VII Facial"],["#2f9b63","IX Glossofaríngeo"],["#c94f56","X Vago"],["#f1c40f","XII Hipoglosso"]] }};
    }}

    function buildScene15() {{
      /* Postura: Figura humana com setas de gravidade/propriocepção */
      /* Head */
      addSphere(root, 0, 1.4, 0, 0.22, MAT.brain);
      /* Torso */
      addCylinder(root, 0, 0.6, 0, 0.25, 0.2, 1.0, MAT.teal);
      /* Legs */
      addCylinder(root, -0.2, -0.3, 0, 0.1, 0.08, 0.8, MAT.teal);
      addCylinder(root, 0.2, -0.3, 0, 0.1, 0.08, 0.8, MAT.teal);
      /* Platform */
      addBox(root, 0, -0.8, 0, 1.5, 0.1, 0.8, MAT.grey);
      /* Gravity arrow */
      addArrow(root, new THREE.Vector3(0.9, 1.2, 0), new THREE.Vector3(0.9, -0.6, 0), 0.04, MAT.wine);
      addLabel(root, "Gravidade", new THREE.Vector3(0.9, 1.5, 0), "#ffb4b9");
      /* Proprioception arrows */
      addArrow(root, new THREE.Vector3(-0.15, -0.6, 0), new THREE.Vector3(-0.15, 0.2, 0), 0.03, MAT.green);
      addArrow(root, new THREE.Vector3(0.15, -0.6, 0), new THREE.Vector3(0.15, 0.2, 0), 0.03, MAT.green);
      addLabel(root, "Propriocepção", new THREE.Vector3(-1.3, -0.2, 0), "#9af0bf");
      addPointer(new THREE.Vector3(-0.9, -0.2, 0), new THREE.Vector3(-0.25, -0.2, 0));
      /* Vestibular */
      addSphere(root, 0, 1.4, -0.3, 0.1, MAT.amber);
      addLabel(root, "Vestibular", new THREE.Vector3(0, 1.8, -0.5), "#f4c772");
      addPointer(new THREE.Vector3(0, 1.65, -0.45), new THREE.Vector3(0, 1.5, -0.3));
      addBase(root);
      return {{ title: "Controle da Postura", desc: "Figura humana em plataforma com setas de gravidade (descendente) e propriocepção (ascendente).", legend: [["#c94f56","Gravidade"],["#2f9b63","Propriocepção"],["#e2a541","Vestibular"],["#38b2ac","Corpo"],["#7f8c8d","Plataforma"]] }};
    }}

    function buildScene16() {{
      /* Integração Sensorial: 3 esferas convergindo */
      /* 3 input spheres */
      addSphere(root, -1.3, 0.5, -0.5, 0.35, MAT.green);
      addLabel(root, "Propriocepção", new THREE.Vector3(-1.3, 1.2, -0.5), "#9af0bf");
      addSphere(root, 0, 0.5, -1.2, 0.35, MAT.blue);
      addLabel(root, "Vestibular", new THREE.Vector3(0, 1.2, -1.2), "#8cb4e8");
      addSphere(root, 1.3, 0.5, -0.5, 0.35, MAT.amber);
      addLabel(root, "Visão", new THREE.Vector3(1.3, 1.2, -0.5), "#f4c772");
      /* Convergence center */
      addSphere(root, 0, 0, 0, 0.4, MAT.wine);
      addLabel(root, "Integração", new THREE.Vector3(0, -0.7, 0.8), "#ffb4b9");
      /* Convergence tubes */
      addTube(root, [new THREE.Vector3(-1.3, 0.5, -0.5), new THREE.Vector3(-0.3, 0.1, -0.1)], 0.04, MAT.green);
      addTube(root, [new THREE.Vector3(0, 0.5, -1.2), new THREE.Vector3(0, 0.1, -0.3)], 0.04, MAT.blue);
      addTube(root, [new THREE.Vector3(1.3, 0.5, -0.5), new THREE.Vector3(0.3, 0.1, -0.1)], 0.04, MAT.amber);
      /* Output */
      addArrow(root, new THREE.Vector3(0, -0.4, 0), new THREE.Vector3(0, -1.1, 0.4), 0.05, MAT.teal);
      addLabel(root, "Saída motora", new THREE.Vector3(0, -1.35, 0.6), "#7ee8d3");
      addBase(root);
      return {{ title: "Integração Sensorial", desc: "3 fontes sensoriais (propriocepção, vestibular, visão) convergindo para um centro de integração → saída motora.", legend: [["#2f9b63","Propriocepção"],["#4a90d9","Vestibular"],["#e2a541","Visão"],["#c94f56","Centro integrador"],["#38b2ac","Saída motora"]] }};
    }}

    function buildScene17() {{
      /* NMS e NMI: cadeia com rótulos */
      addSphere(root, -1.0, 0.8, 0, 0.4, MAT.wine);
      addLabel(root, "NMS", new THREE.Vector3(-1.0, 1.5, 0), "#ffb4b9");
      addTube(root, [new THREE.Vector3(-1.0, 0.4, 0), new THREE.Vector3(0, 0, 0)], 0.05, MAT.wine);
      /* Sinapse */
      addSphere(root, 0, 0, 0, 0.12, MAT.gold);
      /* NMI */
      addTube(root, [new THREE.Vector3(0, 0, 0), new THREE.Vector3(1.0, -0.4, 0)], 0.05, MAT.teal);
      addSphere(root, 1.0, -0.4, 0, 0.4, MAT.teal);
      addLabel(root, "NMI", new THREE.Vector3(1.0, 0.3, 0), "#7ee8d3");
      /* Muscle */
      addArrow(root, new THREE.Vector3(1.0, -0.8, 0), new THREE.Vector3(1.0, -1.2, 0), 0.04, MAT.amber);
      addBox(root, 1.0, -1.4, 0, 0.7, 0.3, 0.35, MAT.muscle);
      addLabel(root, "Músculo", new THREE.Vector3(1.0, -1.0, 0.6), "#f0a86e");
      /* Comparison labels */
      addLabel(root, "Comando superior", new THREE.Vector3(-1.0, -0.8, 0), "#ffb4b9");
      addLabel(root, "Via final comum", new THREE.Vector3(1.8, -0.4, 0.5), "#7ee8d3");
      addBase(root);
      return {{ title: "NMS e NMI", desc: "Cadeia NMS→sinapse→NMI→músculo. NMS = comando; NMI = via final.", legend: [["#c94f56","NMS"],["#f1c40f","Sinapse"],["#38b2ac","NMI"],["#d35400","Músculo"]] }};
    }}

    function buildScene18() {{
      /* Sínd. NMS: medula com lesão */
      addCylinder(root, 0, 0.2, 0, 0.25, 0.2, 2.0, MAT.green);
      addLabel(root, "Medula", new THREE.Vector3(-1.3, 0.2, 0), "#9af0bf");
      /* Lesion marker */
      addSphere(root, 0.3, 0.5, 0.15, 0.18, MAT.lesion);
      addLabel(root, "Lesão NMS", new THREE.Vector3(1.5, 0.7, 0), "#ff6666");
      addPointer(new THREE.Vector3(1.1, 0.6, 0), new THREE.Vector3(0.48, 0.5, 0.15));
      /* Signs arrows pointing up */
      addArrow(root, new THREE.Vector3(-0.7, 0.2, 0.4), new THREE.Vector3(-0.7, 1.2, 0.4), 0.03, MAT.amber);
      addLabel(root, "↑ Hiperreflexia", new THREE.Vector3(-0.7, 1.5, 0.4), "#f4c772");
      addArrow(root, new THREE.Vector3(0.7, 0.2, 0.4), new THREE.Vector3(0.7, 1.2, 0.4), 0.03, MAT.wine);
      addLabel(root, "↑ Espasticidade", new THREE.Vector3(0.7, 1.5, 0.4), "#ffb4b9");
      addArrow(root, new THREE.Vector3(0, -0.5, 0.4), new THREE.Vector3(0, -1.2, 0.4), 0.03, MAT.purple);
      addLabel(root, "Babinski +", new THREE.Vector3(0, -1.5, 0.4), "#c9a3d9");
      addBase(root);
      return {{ title: "Síndrome NMS", desc: "Medula com marcador de lesão. Setas indicam hiperreflexia, espasticidade e Babinski positivo.", legend: [["#ff2222","Lesão NMS"],["#e2a541","Hiperreflexia"],["#c94f56","Espasticidade"],["#9b59b6","Babinski"],["#2f9b63","Medula"]] }};
    }}

    function buildScene19() {{
      /* Doenças NMS: nó central com esferas orbitando */
      addSphere(root, 0, 0, 0, 0.45, MAT.wine);
      addLabel(root, "NMS", new THREE.Vector3(0, 0.8, 0), "#ffb4b9");
      const diseases = [
        ["AVC", 0, MAT.red],
        ["PC", 1, MAT.purple],
        ["EM", 2, MAT.blue],
        ["ELA", 3, MAT.amber],
        ["ELP", 4, MAT.teal],
        ["PEH", 5, MAT.green],
      ];
      diseases.forEach(([name, i, mat]) => {{
        const angle = (i / 6) * Math.PI * 2;
        const x = Math.cos(angle) * 1.5;
        const z = Math.sin(angle) * 1.5;
        addSphere(root, x, 0, z, 0.25, mat);
        addLabel(root, name, new THREE.Vector3(x * 1.35, 0.55, z * 1.35), "#ffffff");
        addTube(root, [new THREE.Vector3(x * 0.3, 0, z * 0.3), new THREE.Vector3(x * 0.8, 0, z * 0.8)], 0.025, mat);
      }});
      addBase(root);
      return {{ title: "Doenças do NMS", desc: "Nó central NMS com 6 doenças orbitando: AVC, Paralisia Cerebral, Esclerose Múltipla, ELA, ELP, PEH.", legend: [["#e74c3c","AVC"],["#9b59b6","Paralisia Cerebral"],["#4a90d9","Esclerose Múltipla"],["#e2a541","ELA"],["#38b2ac","ELP"],["#2f9b63","PEH"]] }};
    }}

    function buildScene20() {{
      /* Sínd. NMI: NMI lesado + músculo atrofiado vs normal */
      /* Normal side */
      addSphere(root, -1.0, 0.5, 0, 0.3, MAT.teal);
      addLabel(root, "NMI Normal", new THREE.Vector3(-1.0, 1.1, 0), "#7ee8d3");
      addArrow(root, new THREE.Vector3(-1.0, 0.2, 0), new THREE.Vector3(-1.0, -0.5, 0), 0.03, MAT.teal);
      addBox(root, -1.0, -0.8, 0, 0.7, 0.4, 0.35, MAT.muscle);
      addLabel(root, "Músculo normal", new THREE.Vector3(-1.0, -0.2, 0.5), "#f0a86e");
      /* Lesion side */
      addSphere(root, 1.0, 0.5, 0, 0.3, MAT.grey);
      addSphere(root, 1.15, 0.55, 0.1, 0.1, MAT.lesion);
      addLabel(root, "NMI Lesado", new THREE.Vector3(1.0, 1.1, 0), "#ff6666");
      addArrow(root, new THREE.Vector3(1.0, 0.2, 0), new THREE.Vector3(1.0, -0.5, 0), 0.02, MAT.grey);
      addBox(root, 1.0, -0.7, 0, 0.4, 0.2, 0.2, MAT.grey);
      addLabel(root, "Músculo atrofiado", new THREE.Vector3(1.0, -0.2, 0.5), "#bbb");
      /* Signs */
      addLabel(root, "Hipotonia / Hiporreflexia", new THREE.Vector3(0, -1.3, 0), "#ffb4b9");
      addBase(root);
      return {{ title: "Síndrome NMI", desc: "Comparação: NMI normal com músculo saudável vs NMI lesado com músculo atrofiado.", legend: [["#38b2ac","NMI normal"],["#7f8c8d","NMI lesado"],["#d35400","Músculo normal"],["#ff2222","Lesão"],["#bbb","Músculo atrofiado"]] }};
    }}

    function buildScene21() {{
      /* Cerebelar: caminho reto vs ondulado */
      const cb = addSphere(root, 0, 0.8, -0.5, 0.5, MAT.brain);
      cb.scale.set(1.2, 0.65, 0.85);
      addLabel(root, "Cerebelo", new THREE.Vector3(0, 1.6, -0.5), "#d7b07c");
      /* Intended straight path */
      addTube(root, [new THREE.Vector3(-1.5, -0.5, 0.5), new THREE.Vector3(1.5, -0.5, 0.5)], 0.04, MAT.green);
      addLabel(root, "Caminho pretendido", new THREE.Vector3(0, -0.2, 1.0), "#9af0bf");
      /* Ataxic wavy path */
      const wavyPts = [];
      for (let i = 0; i <= 40; i++) {{
        const t = i / 40;
        const x = -1.5 + t * 3.0;
        const y = -0.5 + Math.sin(t * Math.PI * 5) * 0.3;
        const z = 0.5 + Math.cos(t * Math.PI * 3.5) * 0.25;
        wavyPts.push(new THREE.Vector3(x, y, z));
      }}
      addTube(root, wavyPts, 0.04, MAT.wine);
      addLabel(root, "Caminho real (ataxia)", new THREE.Vector3(0, -1.1, 0.8), "#ffb4b9");
      /* Target */
      addSphere(root, 1.5, -0.5, 0.5, 0.15, MAT.amber);
      addLabel(root, "Alvo", new THREE.Vector3(1.5, -0.1, 0.5), "#f4c772");
      addBase(root);
      return {{ title: "Síndrome Cerebelar", desc: "Cerebelo + caminho pretendido (reto, verde) vs caminho real com ataxia (ondulado, vinho).", legend: [["#c99f68","Cerebelo"],["#2f9b63","Caminho pretendido"],["#c94f56","Caminho real (ataxia)"],["#e2a541","Alvo"]] }};
    }}

    const sceneBuilders = [
      buildScene1, buildScene2, buildScene3, buildScene4, buildScene5,
      buildScene6, buildScene7, buildScene8, buildScene9, buildScene10,
      buildScene11, buildScene12, buildScene13, buildScene14, buildScene15,
      buildScene16, buildScene17, buildScene18, buildScene19, buildScene20,
      buildScene21
    ];

    /* ===== UI ===== */
    const sidebar = document.getElementById("sidebar");
    const eyebrow = document.getElementById("eyebrow");
    const sceneTitle = document.getElementById("sceneTitle");
    const sceneSubtitle = document.getElementById("sceneSubtitle");
    const infoTitle = document.getElementById("infoTitle");
    const infoDesc = document.getElementById("infoDesc");
    const legendEl = document.getElementById("legend");
    const refImg = document.getElementById("refImg");
    const refLabel = document.getElementById("refLabel");
    const refPanel = document.getElementById("refPanel");

    function buildSidebar() {{
      sidebar.innerHTML = SLIDES.map((s, i) =>
        `<button class="sb ${{i === currentScene ? 'active' : ''}}" data-scene="${{i}}" type="button">${{s.number}}</button>`
      ).join("");
      sidebar.querySelectorAll("[data-scene]").forEach(btn => {{
        btn.addEventListener("click", () => {{
          switchScene(Number(btn.dataset.scene));
        }});
      }});
    }}

    function switchScene(index) {{
      currentScene = index;
      clearScene();
      const info = sceneBuilders[index]();
      const slide = SLIDES[index];
      /* Update UI */
      eyebrow.textContent = `Cena ${{index + 1}} de 21`;
      sceneTitle.textContent = info.title;
      sceneSubtitle.textContent = slide.subtitle;
      infoTitle.textContent = info.title;
      infoDesc.textContent = info.desc;
      legendEl.innerHTML = (info.legend || []).map(([color, text]) =>
        `<li><span class="swatch" style="background:${{color}}"></span><span>${{text}}</span></li>`
      ).join("");
      refImg.src = slide.src;
      refImg.alt = `Lâmina ${{slide.number}}: ${{slide.title}}`;
      refLabel.textContent = `Referência: Lâmina ${{slide.number}}`;
      refPanel.classList.remove("expanded");
      document.getElementById("refBtn").textContent = "Ver Lâmina";
      document.getElementById("refBtn").classList.remove("active");
      /* Reset camera */
      yaw = -0.55;
      pitch = -0.18;
      distance = window.innerWidth < 700 ? 8.25 : 5.7;
      autoRotate = false;
      syncButtons();
      buildSidebar();
    }}

    function syncButtons() {{
      document.getElementById("autoBtn").classList.toggle("active", autoRotate);
      document.getElementById("labelsBtn").classList.toggle("active", labelsVisible);
      labelGroup.visible = labelsVisible;
    }}

    /* ===== CONTROLS ===== */
    document.getElementById("prevScene").addEventListener("click", () => switchScene((currentScene - 1 + 21) % 21));
    document.getElementById("nextScene").addEventListener("click", () => switchScene((currentScene + 1) % 21));
    document.getElementById("autoBtn").addEventListener("click", () => {{ autoRotate = !autoRotate; syncButtons(); }});
    document.getElementById("labelsBtn").addEventListener("click", () => {{ labelsVisible = !labelsVisible; syncButtons(); }});
    document.getElementById("resetBtn").addEventListener("click", () => {{
      yaw = -0.55; pitch = -0.18;
      distance = window.innerWidth < 700 ? 8.25 : 5.7;
      autoRotate = false; syncButtons();
    }});
    document.getElementById("refBtn").addEventListener("click", () => {{
      refPanel.classList.toggle("expanded");
      const expanded = refPanel.classList.contains("expanded");
      document.getElementById("refBtn").textContent = expanded ? "Fechar Lâmina" : "Ver Lâmina";
      document.getElementById("refBtn").classList.toggle("active", expanded);
    }});
    refPanel.addEventListener("click", () => {{
      refPanel.classList.remove("expanded");
      document.getElementById("refBtn").textContent = "Ver Lâmina";
      document.getElementById("refBtn").classList.remove("active");
    }});

    /* ===== DRAG / ZOOM ===== */
    canvas.addEventListener("pointerdown", (e) => {{
      canvas.setPointerCapture(e.pointerId);
      dragging = true; startX = e.clientX; startY = e.clientY;
      startYaw = yaw; startPitch = pitch;
      autoRotate = false; syncButtons();
    }});
    canvas.addEventListener("pointermove", (e) => {{
      if (!dragging) return;
      yaw = startYaw + (e.clientX - startX) * 0.008;
      pitch = Math.max(-1.05, Math.min(0.85, startPitch + (e.clientY - startY) * 0.006));
    }});
    canvas.addEventListener("pointerup", () => dragging = false);
    canvas.addEventListener("pointercancel", () => dragging = false);
    canvas.addEventListener("wheel", (e) => {{
      e.preventDefault();
      distance = Math.max(3.2, Math.min(9.2, distance + e.deltaY * 0.006));
    }}, {{ passive: false }});

    /* ===== KEYBOARD ===== */
    document.addEventListener("keydown", (e) => {{
      if (e.key === "ArrowLeft") switchScene((currentScene - 1 + 21) % 21);
      if (e.key === "ArrowRight") switchScene((currentScene + 1) % 21);
    }});

    /* ===== postMessage for external navigation ===== */
    window.addEventListener("message", (event) => {{
      if (event.data && event.data.type === "setScene") {{
        const idx = event.data.index;
        if (idx >= 0 && idx < 21) switchScene(idx);
      }}
    }});

    /* ===== RENDER LOOP ===== */
    function resize() {{
      const w = canvas.parentElement.clientWidth;
      const h = canvas.parentElement.clientHeight;
      renderer.setSize(w, h, false);
      camera.aspect = w / h;
      camera.fov = w < 700 ? 50 : 42;
      camera.updateProjectionMatrix();
    }}

    function animate() {{
      requestAnimationFrame(animate);
      if (autoRotate) yaw += 0.008;
      root.rotation.y = yaw;
      root.rotation.x = pitch;
      camera.position.set(0, 0.35, distance);
      camera.lookAt(0, 0.1, 0);
      renderer.render(scene, camera);
    }}

    window.addEventListener("resize", resize);
    resize();
    switchScene(0);
    animate();
  </script>
</body>
</html>
"""


def main() -> None:
    html = build()
    (ROOT / "ANATOMIA_3D.html").write_text(html, encoding="utf-8", newline="\n")
    (WORKSPACE / "ANATOMIA_3D.html").write_text(html, encoding="utf-8", newline="\n")
    print("anatomia 3d written (21 scenes)")


if __name__ == "__main__":
    main()
