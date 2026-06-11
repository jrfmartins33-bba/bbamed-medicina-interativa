from __future__ import annotations

import base64
import mimetypes
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
WORKSPACE = ROOT.parent
INDEX = ROOT / "index.html"
TEMPLATE = ROOT / "index.template.html"
CSS = ROOT / "styles.css"
JS = ROOT / "app.js"
IMAGES = WORKSPACE / "page_images"
BRAIN_IMAGE = WORKSPACE / "Imagens" / "Imagem 01 - Cerebro transparente.png"
SCENE02_IMAGE = WORKSPACE / "Imagens" / "Cena 02" / "Imagem_cena02_04_transparente.png"
SCENE03_IMAGES = {
    "../Imagens/Cena 03/Cena03_homunculo.png": WORKSPACE / "Imagens" / "Cena 03" / "Cena03_homunculo.png",
    "../Imagens/Cena 03/Cena03_face.png": WORKSPACE / "Imagens" / "Cena 03" / "Cena03_face.png",
    "../Imagens/Cena 03/Cena03_lingua.png": WORKSPACE / "Imagens" / "Cena 03" / "Cena03_lingua.png",
    "../Imagens/Cena 03/Cena03_mão.png": WORKSPACE / "Imagens" / "Cena 03" / "Cena03_mão.png",
    "../Imagens/Cena 03/Cena03_Pés.png": WORKSPACE / "Imagens" / "Cena 03" / "Cena03_Pés.png",
}
ANATOMY = WORKSPACE / "ANATOMIA_3D.html"
SLIDES3D = WORKSPACE / "LAMINAS_3D.html"
ROOT_STANDALONE = WORKSPACE / "Postura_Locomocao_Estudo_COMPLETO.html"


def data_uri(path: Path) -> str:
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    payload = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{payload}"


def load_images() -> dict[str, str]:
    images: dict[str, str] = {}
    for number in range(1, 22):
        name = f"page{number:02d}.png"
        path = IMAGES / name
        if not path.exists():
            raise FileNotFoundError(path)
        images[name] = data_uri(path)
    return images


def make_embedded_js(js: str, images: dict[str, str]) -> str:
    image_lines = [f'  "{name}": "{uri}"' for name, uri in images.items()]
    image_map = "const embeddedSlides = {\n" + ",\n".join(image_lines) + "\n};\n\n"
    anatomy_payload = base64.b64encode(ANATOMY.read_text(encoding="utf-8").encode("utf-8")).decode("ascii")
    anatomy_map = f'window.embeddedAnatomyHtml = "{anatomy_payload}";\n\n'
    slides3d_payload = base64.b64encode(SLIDES3D.read_text(encoding="utf-8").encode("utf-8")).decode("ascii")
    slides3d_map = f'window.embeddedSlides3dHtml = "{slides3d_payload}";\n\n'
    js = js.replace(
        'src: `../page_images/${item[0]}`,',
        'src: embeddedSlides[item[0]],',
    )
    return anatomy_map + slides3d_map + image_map + js


def make_embedded_css(css: str, images: dict[str, str]) -> str:
    css = css.replace('url("../page_images/page05.png")', f'url("{images["page05.png"]}")')
    css = css.replace('url("../page_images/page10.png")', f'url("{images["page10.png"]}")')
    return css


def make_standalone_html() -> str:
    images = load_images()
    html = TEMPLATE.read_text(encoding="utf-8")
    brain_image = data_uri(BRAIN_IMAGE)
    scene02_image = data_uri(SCENE02_IMAGE)
    scene03_images = {relative: data_uri(path) for relative, path in SCENE03_IMAGES.items()}
    css = make_embedded_css(CSS.read_text(encoding="utf-8"), images)
    js = make_embedded_js(JS.read_text(encoding="utf-8"), images)
    for relative, uri in scene03_images.items():
        js = js.replace(f'"{relative}"', f'"{uri}"')

    # Remove the external material link from the autonomous build. Inside a ZIP,
    # relative links can open without their siblings; the core app must be solid.
    html = re.sub(r'\s*<a class="nav-link" href="MATERIAIS\.html">Materiais HTML</a>', "", html)
    html = html.replace('src="../Imagens/Imagem 01 - Cerebro transparente.png"', f'src="{brain_image}"')
    html = html.replace('src="../Imagens/Cena 02/Imagem_cena02_04_transparente.png"', f'src="{scene02_image}"')
    for relative, uri in scene03_images.items():
        html = html.replace(f'src="{relative}"', f'src="{uri}"')
    html = html.replace('<link rel="stylesheet" href="styles.css">', f"<style>\n{css}\n</style>")
    html = html.replace('<script src="app.js"></script>', f"<script>\n{js}\n</script>")
    html = html.replace(
        "<title>Ambiente de Estudos | Postura e Locomoção</title>",
        "<title>Postura e Locomoção | Ambiente Completo</title>",
    )
    return html


def main() -> None:
    html = make_standalone_html()
    INDEX.write_text(html, encoding="utf-8", newline="\n")
    ROOT_STANDALONE.write_text(html, encoding="utf-8", newline="\n")
    print(f"standalone written: {INDEX}")
    print(f"standalone written: {ROOT_STANDALONE}")


if __name__ == "__main__":
    main()
