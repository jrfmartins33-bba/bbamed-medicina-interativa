from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TARGETS = [
    ROOT / "index.html",
    ROOT.parent / "Postura_Locomocao_Estudo_COMPLETO.html",
]


def check(path: Path) -> None:
    html = path.read_text(encoding="utf-8")
    failures: list[str] = []

    for needle in ('<link rel="stylesheet"', '<script src=', "../page_images/"):
        if needle in html:
            failures.append(f"external dependency remains: {needle}")

    embedded_count = html.count("data:image/png;base64")
    if embedded_count < 21:
        failures.append(f"expected at least 21 embedded png images, found {embedded_count}")

    for needle in ('data-view="anatomy"', 'id="anatomyFrame"', "window.embeddedAnatomyHtml"):
        if needle not in html:
            failures.append(f"integrated anatomy 3D missing: {needle}")

    scripts = re.findall(r"<script>\s*(.*?)\s*</script>", html, flags=re.DOTALL)
    if not scripts:
        failures.append("no inline script found")
    else:
        tmp = ROOT / "_inline_check.js"
        # Strip huge base64 literals to avoid OOM / MemoryError
        sanitised = re.sub(r'"[A-Za-z0-9+/=]{100,}"', '"dummy"', scripts[-1])
        tmp.write_text(sanitised, encoding="utf-8")
        try:
            result = subprocess.run(["node", "--check", str(tmp)], capture_output=True, text=True)
            if result.returncode != 0:
                failures.append(result.stderr or result.stdout or "node --check failed")
        finally:
            try:
                tmp.unlink()
            except OSError:
                pass

    if failures:
        print(f"FAIL {path}")
        for item in failures:
            print(f"- {item}")
        raise SystemExit(1)

    print(f"OK {path.name}: inline assets={embedded_count}")


def main() -> None:
    for target in TARGETS:
        check(target)


if __name__ == "__main__":
    main()
