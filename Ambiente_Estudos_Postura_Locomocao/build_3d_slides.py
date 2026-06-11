from __future__ import annotations

import base64
import mimetypes
from pathlib import Path


ROOT = Path(__file__).resolve().parent
WORKSPACE = ROOT.parent
IMAGES = WORKSPACE / "page_images"

SLIDES = [
    ("page01.png", "Capa", "Postura e Locomoção", False),
    ("page02.png", "Introdução", "Sistema motor integrado: córtex, tronco, medula, músculos e sentidos.", True),
    ("page03.png", "Organização", "Neurônio motor superior, inferior e feedback sensorial.", True),
    ("page04.png", "Córtex motor", "Giro pré-central, movimento voluntário e somatotopia.", True),
    ("page05.png", "Áreas corticais", "Faixas motoras e sensoriais no córtex.", False),
    ("page06.png", "Homúnculo", "Representação cortical de regiões com controle fino.", False),
    ("page07.png", "Áreas associadas", "Pré-motora, suplementar e aprendizagem motora.", True),
    ("page08.png", "Corticoespinal", "Via voluntária principal para movimento consciente fino.", True),
    ("page09.png", "Organização corticoespinal", "Córtex, tronco, medula, interneurônios e músculo.", True),
    ("page10.png", "Trato corticoespinal", "Diagrama da via descendente e decussação.", False),
    ("page11.png", "Tronco encefálico", "Controle automático de tônus, reflexos e equilíbrio.", True),
    ("page12.png", "Vias descendentes", "Trato corticoespinal lateral e rubroespinal.", False),
    ("page13.png", "Extrapiramidais", "Vestibuloespinal, reticuloespinal e rubroespinal.", True),
    ("page14.png", "Núcleos do tronco", "Mesencéfalo, ponte, bulbo e nervos cranianos.", False),
    ("page15.png", "Postura", "Estabilidade, reflexos e ajustes contra a gravidade.", True),
    ("page16.png", "Integração sensorial", "Propriocepção, vestibular, visão e feedback.", True),
    ("page17.png", "NMS e NMI", "Comando superior e via final para o musculo.", False),
    ("page18.png", "Sindrome NMS", "Espasticidade, hiperreflexia, Babinski e fraqueza central.", True),
    ("page19.png", "Doencas NMS", "AVC, paralisia cerebral, EM, ELA e outras.", False),
    ("page20.png", "Síndrome NMI", "Fraqueza, hipotonia, hiporreflexia e atrofia.", True),
    ("page21.png", "Cerebelar", "Ataxia, dismetria, tremor de intencao e marcha instavel.", True),
]


def data_uri(path: Path) -> str:
    mime = mimetypes.guess_type(path.name)[0] or "image/png"
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode('ascii')}"


def build() -> str:
    slide_rows = []
    for index, (file_name, title, note, rotate) in enumerate(SLIDES):
        src = data_uri(IMAGES / file_name)
        slide_rows.append(
            "{"
            f"number:{index + 1},"
            f"title:{title!r},"
            f"note:{note!r},"
            f"rotate:{str(rotate).lower()},"
            f"src:{src!r}"
            "}"
        )

    return f"""<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Lâminas 3D | Postura e Locomoção</title>
  <style>
    :root {{
      --ink: #17202a;
      --paper: #f7f5ef;
      --teal: #176b70;
      --wine: #8c2f39;
      --amber: #d99a35;
      --line: rgba(255,255,255,.22);
    }}
    * {{ box-sizing: border-box; }}
    html, body {{ min-height: 100%; }}
    body {{
      margin: 0;
      color: #fff;
      background:
        radial-gradient(circle at 18% 18%, rgba(217,154,53,.22), transparent 32%),
        linear-gradient(132deg, #111820 0%, #176b70 62%, #23342f 100%);
      font-family: Arial, Helvetica, sans-serif;
      overflow-x: hidden;
    }}
    header {{
      display: flex;
      align-items: flex-end;
      justify-content: space-between;
      gap: 18px;
      padding: 26px 28px 10px;
    }}
    h1 {{
      margin: 0 0 6px;
      font-size: 2.4rem;
      line-height: 1.05;
      letter-spacing: 0;
    }}
    p {{ margin: 0; }}
    .eyebrow {{
      margin-bottom: 5px;
      font-size: .78rem;
      font-weight: 700;
      letter-spacing: .08em;
      text-transform: uppercase;
      color: #f4c772;
    }}
    .stage {{
      position: relative;
      min-height: 620px;
      perspective: 1500px;
      transform-style: preserve-3d;
      overflow: hidden;
      padding: 14px 0 28px;
    }}
    .deck {{
      position: relative;
      width: min(92vw, 1180px);
      height: 560px;
      margin: 0 auto;
      transform-style: preserve-3d;
    }}
    .slide {{
      position: absolute;
      left: 50%;
      top: 50%;
      display: grid;
      grid-template-rows: minmax(0, 1fr) auto;
      width: min(72vw, 820px);
      height: 500px;
      overflow: hidden;
      color: var(--ink);
      background: #fff;
      border: 1px solid rgba(255,255,255,.5);
      border-radius: 8px;
      box-shadow: 0 34px 80px rgba(0,0,0,.35);
      transform-style: preserve-3d;
      transition: transform .42s ease, opacity .42s ease, filter .42s ease, border-color 0.2s ease;
    }}
    .slide[aria-hidden="false"] {{
      cursor: pointer;
    }}
    .slide[aria-hidden="false"]:hover {{
      border-color: var(--amber);
    }}
    .modal-overlay {{
      position: fixed;
      inset: 0;
      z-index: 2000;
      background: rgba(0, 0, 0, 0.72);
      backdrop-filter: blur(10px);
      display: none;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      opacity: 0;
      transition: opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    .modal-overlay.active {{
      display: flex;
      opacity: 1;
    }}
    .modal-content {{
      position: relative;
      margin: 0;
      padding: 0;
      max-width: 90vw;
      max-height: 90vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      transform: scale(0.95);
      transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    .modal-overlay.active .modal-content {{
      transform: scale(1);
    }}
    .modal-content img {{
      max-width: 100%;
      max-height: 80vh;
      object-fit: contain;
      border-radius: 8px;
      box-shadow: 0 24px 64px rgba(0, 0, 0, 0.5);
      background: #fff;
    }}
    .modal-content img.rotate {{
      transform: rotate(90deg);
      max-width: 78vh;
      max-height: 78vw;
      width: auto;
      height: auto;
    }}
    .modal-content figcaption {{
      margin-top: 14px;
      color: #fff;
      font-size: 1.1rem;
      font-weight: 700;
      text-align: center;
      text-shadow: 0 2px 4px rgba(0,0,0,0.5);
    }}
    .image-wrap {{
      display: grid;
      place-items: center;
      min-height: 0;
      background: #f3efe4;
      overflow: hidden;
    }}
    .slide img {{
      display: block;
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
    }}
    .slide img.rotate {{
      width: auto;
      height: 76%;
      max-height: 390px;
      transform: rotate(90deg);
      transform-origin: center;
    }}
    .caption {{
      padding: 12px 15px 14px;
      border-top: 1px solid #ddd8cb;
      background: #fff;
    }}
    .caption strong {{
      display: block;
      color: var(--wine);
      font-size: 1rem;
    }}
    .caption span {{
      display: block;
      color: #5d6670;
      font-size: .94rem;
    }}
    .controls {{
      display: flex;
      justify-content: center;
      gap: 10px;
      flex-wrap: wrap;
      padding: 0 20px 18px;
    }}
    button {{
      min-height: 42px;
      padding: 9px 13px;
      color: #fff;
      background: rgba(255,255,255,.13);
      border: 1px solid var(--line);
      border-radius: 8px;
      font: inherit;
      font-weight: 700;
      cursor: pointer;
      backdrop-filter: blur(6px);
    }}
    button.primary {{ background: var(--wine); border-color: var(--wine); }}
    button:focus-visible {{ outline: 3px solid #f4c772; outline-offset: 2px; }}
    .timeline {{
      display: flex;
      width: min(92vw, 1180px);
      gap: 6px;
      margin: 0 auto 24px;
      overflow-x: auto;
      padding: 4px 4px 10px;
    }}
    .thumb {{
      flex: 0 0 auto;
      width: 42px;
      height: 42px;
      border-radius: 8px;
      border: 1px solid var(--line);
      color: #fff;
      background: rgba(255,255,255,.1);
    }}
    .thumb.active {{
      background: var(--amber);
      color: #1b1f24;
    }}
    .status {{
      min-width: 170px;
      padding: 12px 14px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: rgba(255,255,255,.12);
    }}
    .status strong {{ display: block; font-size: 1.35rem; }}
    @media (max-width: 760px) {{
      header {{ display: grid; padding: 22px 18px 8px; }}
      h1 {{ font-size: 2rem; }}
      .stage {{ min-height: 520px; }}
      .deck {{ height: 470px; }}
      .slide {{
        width: min(86vw, 620px);
        height: 430px;
      }}
      .slide img.rotate {{ height: 62%; }}
    }}
  </style>
</head>
<body>
  <header>
    <div>
      <p class="eyebrow">Lâminas em perspectiva 3D</p>
      <h1>Postura e Locomoção</h1>
      <p>Visualização imersiva das 21 lâminas do material.</p>
    </div>
    <div class="status" aria-live="polite">
      <span>Lâmina atual</span>
      <strong id="status">1/21</strong>
    </div>
  </header>

  <main>
    <section class="stage" aria-label="Palco 3D das lâminas">
      <div class="deck" id="deck"></div>
    </section>

    <div class="controls">
      <button id="prev" type="button">Anterior</button>
      <button id="toggle" class="primary" type="button">Automático</button>
      <button id="next" type="button">Próxima</button>
      <button id="open" type="button">Abrir lâmina</button>
    </div>

    <div class="timeline" id="timeline" aria-label="Miniaturas numéricas"></div>
  </main>

  <div id="modalOverlay" class="modal-overlay" aria-hidden="true">
    <figure class="modal-content">
      <img id="modalImage" src="" alt="">
      <figcaption id="modalCaption"></figcaption>
    </figure>
  </div>

  <script>
    const slides = [{",".join(slide_rows)}];
    let active = 0;
    let auto = false;
    let timer = null;

    const deck = document.getElementById("deck");
    const status = document.getElementById("status");
    const timeline = document.getElementById("timeline");

    function signedOffset(index) {{
      const total = slides.length;
      let offset = index - active;
      if (offset > total / 2) offset -= total;
      if (offset < -total / 2) offset += total;
      return offset;
    }}

    function render() {{
      deck.innerHTML = slides.map((slide, index) => {{
        const offset = signedOffset(index);
        const visible = Math.abs(offset) <= 3;
        const x = offset * 175;
        const z = -Math.abs(offset) * 115;
        const ry = offset * -22;
        const scale = 1 - Math.min(Math.abs(offset) * .08, .28);
        const opacity = visible ? 1 - Math.abs(offset) * .2 : 0;
        const filter = offset === 0 ? "none" : "saturate(.72) brightness(.82)";
        const style = `transform: translate(-50%, -50%) translateX(${{x}}px) translateZ(${{z}}px) rotateY(${{ry}}deg) scale(${{scale}}); opacity:${{opacity}}; z-index:${{100 - Math.abs(offset)}}; filter:${{filter}}; pointer-events:${{offset === 0 ? "auto" : "none"}};`;
        return `<article class="slide" style="${{style}}" aria-hidden="${{offset === 0 ? "false" : "true"}}">
          <div class="image-wrap"><img class="${{slide.rotate ? "rotate" : ""}}" src="${{slide.src}}" alt="Lâmina ${{slide.number}} - ${{slide.title}}"></div>
          <div class="caption"><strong>${{slide.number}}. ${{slide.title}}</strong><span>${{slide.note}}</span></div>
        </article>`;
      }}).join("");

      status.textContent = `${{active + 1}}/${{slides.length}}`;
      timeline.innerHTML = slides.map((slide, index) => `<button class="thumb ${{index === active ? "active" : ""}}" data-index="${{index}}" type="button">${{slide.number}}</button>`).join("");
      timeline.querySelectorAll("[data-index]").forEach((button) => {{
        button.addEventListener("click", () => {{
          active = Number(button.dataset.index);
          render();
        }});
      }});

      const activeCard = deck.querySelector('.slide[aria-hidden="false"]');
      if (activeCard) {{
        activeCard.addEventListener("click", openCurrentSlide);
      }}
    }}

    function move(delta) {{
      active = (active + delta + slides.length) % slides.length;
      render();
    }}

    function setAuto(value) {{
      auto = value;
      document.getElementById("toggle").textContent = auto ? "Pausar" : "Automático";
      if (timer) clearInterval(timer);
      timer = auto ? setInterval(() => move(1), 2600) : null;
    }}

    const modalOverlay = document.getElementById("modalOverlay");
    const modalImage = document.getElementById("modalImage");
    const modalCaption = document.getElementById("modalCaption");

    function openCurrentSlide() {{
      const slide = slides[active];
      modalImage.src = slide.src;
      modalImage.className = slide.rotate ? "rotate" : "";
      modalCaption.textContent = `${{slide.number}}. ${{slide.title}} - ${{slide.note}}`;
      modalOverlay.classList.add("active");
    }}

    modalOverlay.addEventListener("click", () => {{
      modalOverlay.classList.remove("active");
    }});

    window.addEventListener("message", (event) => {{
      if (event.data && event.data.type === "setSlide") {{
        const num = event.data.index;
        if (num >= 0 && num < slides.length) {{
          active = num;
          render();
        }}
      }}
    }});

    document.getElementById("prev").addEventListener("click", () => move(-1));
    document.getElementById("next").addEventListener("click", () => move(1));
    document.getElementById("toggle").addEventListener("click", () => setAuto(!auto));
    document.getElementById("open").addEventListener("click", openCurrentSlide);
    document.addEventListener("keydown", (event) => {{
      if (event.key === "ArrowLeft") move(-1);
      if (event.key === "ArrowRight") move(1);
      if (event.key === " ") {{ event.preventDefault(); setAuto(!auto); }}
    }});

    render();
  </script>
</body>
</html>
"""


def main() -> None:
    html = build()
    (ROOT / "LAMINAS_3D.html").write_text(html, encoding="utf-8", newline="\n")
    (WORKSPACE / "LAMINAS_3D.html").write_text(html, encoding="utf-8", newline="\n")
    print("3d slides written")


if __name__ == "__main__":
    main()
