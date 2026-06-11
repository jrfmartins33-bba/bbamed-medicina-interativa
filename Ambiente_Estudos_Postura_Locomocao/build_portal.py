from __future__ import annotations

import base64
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
WORKSPACE = ROOT.parent

TARGETS = {
    "index": WORKSPACE / "Postura_Locomocao_Estudo_COMPLETO.html",
    "laminas3d": WORKSPACE / "LAMINAS_3D.html",
    "guia": ROOT / "GUIA_DE_ESTUDOS.html",
    "questoes": ROOT / "QUESTOES_REVISAO.html",
    "flashcards": ROOT / "FLASHCARDS.html",
    "readme": ROOT / "README.html",
}


def b64_html(path: Path) -> str:
    html = path.read_text(encoding="utf-8")
    if path.name != "Postura_Locomocao_Estudo_COMPLETO.html":
        html = re.sub(r"\s*<nav aria-label=\"Links do pacote\">.*?</nav>", "", html, flags=re.DOTALL)
    return base64.b64encode(html.encode("utf-8")).decode("ascii")


def script_payload() -> str:
    items = ",\n".join(f'      "{key}": "{b64_html(path)}"' for key, path in TARGETS.items())
    return f"""
    <script>
      const portableMaterials = {{
{items}
      }};

      function decodePortableHtml(payload) {{
        const binary = atob(payload);
        const bytes = new Uint8Array(binary.length);
        for (let i = 0; i < binary.length; i += 1) bytes[i] = binary.charCodeAt(i);
        return new TextDecoder("utf-8").decode(bytes);
      }}

      function openPortableMaterial(key) {{
        const payload = portableMaterials[key];
        if (!payload) return;
        const html = decodePortableHtml(payload);
        const opened = window.open("", "_blank");
        const target = opened || window;
        target.document.open();
        target.document.write(html);
        target.document.close();
      }}

      document.addEventListener("DOMContentLoaded", () => {{
        document.querySelectorAll("[data-open-material]").forEach((link) => {{
          link.addEventListener("click", (event) => {{
            event.preventDefault();
            openPortableMaterial(link.dataset.openMaterial);
          }});
        }});
      }});
    </script>
"""


def build_portal_html() -> str:
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Iniciar Aqui | Postura e Locomoção</title>
  <style>
    :root {{
      --paper: #f7f5ef;
      --surface: #ffffff;
      --ink: #17202a;
      --muted: #66707a;
      --line: #d9d5c9;
      --teal: #176b70;
      --wine: #8c2f39;
      --amber: #b06f18;
      --soft: #e8f3f1;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      color: var(--ink);
      background: var(--paper);
      font-family: Arial, Helvetica, sans-serif;
      line-height: 1.6;
    }}
    header {{
      padding: 36px 28px;
      color: #fff;
      background: linear-gradient(110deg, #17202a, #176b70);
      border-bottom: 4px solid var(--amber);
    }}
    main {{
      width: min(1120px, calc(100% - 32px));
      margin: 24px auto 48px;
    }}
    h1 {{
      margin: 0 0 8px;
      font-size: clamp(2rem, 5vw, 3.35rem);
      line-height: 1.05;
      letter-spacing: 0;
    }}
    h2 {{ margin: 0 0 10px; color: var(--teal); }}
    p {{ margin: 0 0 14px; }}
    code {{
      padding: 2px 5px;
      background: #eee9dc;
      border-radius: 5px;
    }}
    .eyebrow {{
      margin: 0 0 6px;
      font-size: .78rem;
      font-weight: 700;
      letter-spacing: .08em;
      text-transform: uppercase;
      opacity: .86;
    }}
    .notice {{
      margin: 0 0 18px;
      padding: 16px;
      background: #fff7e8;
      border: 1px solid #efd3a5;
      border-left: 5px solid var(--amber);
      border-radius: 0 8px 8px 0;
    }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 16px;
    }}
    .card {{
      display: flex;
      min-height: 190px;
      flex-direction: column;
      justify-content: space-between;
      padding: 20px;
      background: var(--surface);
      border: 1px solid var(--line);
      border-radius: 8px;
      box-shadow: 0 16px 38px rgba(23, 32, 42, .10);
    }}
    .card p {{ color: var(--muted); }}
    .actions {{
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      margin-top: 14px;
    }}
    a.button, button.button {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-height: 42px;
      padding: 8px 13px;
      color: #fff;
      background: var(--teal);
      border: 0;
      border-radius: 8px;
      font: inherit;
      font-weight: 700;
      text-decoration: none;
      cursor: pointer;
    }}
    a.button.secondary, button.button.secondary {{
      color: var(--teal);
      background: var(--soft);
    }}
    .full {{ grid-column: 1 / -1; }}
    @media (max-width: 760px) {{
      header {{ padding: 28px 18px; }}
      .grid {{ grid-template-columns: 1fr; }}
      .card {{ min-height: 0; }}
    }}
  </style>
</head>
<body>
  <header>
    <p class="eyebrow">Portal compartilhável corrigido</p>
    <h1>Postura e Locomoção</h1>
    <p>Abra qualquer material abaixo sem depender de links frágeis entre arquivos.</p>
  </header>

  <main>
    <section class="notice">
      <h2>Importante</h2>
      <p>Este portal abre os materiais a partir de conteúdo embutido. Por isso os botões funcionam mesmo quando o arquivo é aberto dentro do ZIP. Para compartilhar, envie este arquivo ou o ZIP corrigido.</p>
    </section>

    <section class="grid" aria-label="Materiais disponíveis">
      <article class="card full">
        <div>
          <h2>Ambiente principal completo</h2>
          <p>App de estudo com módulos, lâminas, flashcards, quiz, casos, revisão e progresso.</p>
        </div>
        <div class="actions">
          <a class="button" href="#" data-open-material="index">Abrir ambiente completo</a>
        </div>
      </article>

      <article class="card full">
        <div>
          <h2>Lâminas 3D</h2>
          <p>Experiência visual com as 21 lâminas em perspectiva, rotação, linha do tempo, controles e modo automático.</p>
        </div>
        <div class="actions">
          <a class="button" href="#" data-open-material="laminas3d">Abrir lâminas 3D</a>
        </div>
      </article>

      <article class="card">
        <div>
          <h2>Guia de estudos</h2>
          <p>Explicação estruturada da matéria, tabelas comparativas, roteiro de estudo e respostas-modelo.</p>
        </div>
        <div class="actions">
          <a class="button" href="#" data-open-material="guia">Abrir guia</a>
        </div>
      </article>

      <article class="card">
        <div>
          <h2>Questões de revisão</h2>
          <p>Questões abertas, múltipla escolha, casos clínicos e gabarito comentado.</p>
        </div>
        <div class="actions">
          <a class="button" href="#" data-open-material="questoes">Abrir questões</a>
        </div>
      </article>

      <article class="card">
        <div>
          <h2>Flashcards HTML</h2>
          <p>Cartões interativos para revisar os conceitos-chave no navegador.</p>
        </div>
        <div class="actions">
          <a class="button" href="#" data-open-material="flashcards">Abrir flashcards</a>
        </div>
      </article>

      <article class="card">
        <div>
          <h2>Instruções</h2>
          <p>Modo de uso e orientação de compartilhamento do pacote.</p>
        </div>
        <div class="actions">
          <a class="button" href="#" data-open-material="readme">Abrir instruções</a>
        </div>
      </article>
    </section>
  </main>

{script_payload()}
</body>
</html>
"""


def main() -> None:
    html = build_portal_html()
    (ROOT / "MATERIAIS.html").write_text(html, encoding="utf-8", newline="\n")
    (WORKSPACE / "INICIAR_AQUI.html").write_text(html, encoding="utf-8", newline="\n")
    print("portable portal written")


if __name__ == "__main__":
    main()
