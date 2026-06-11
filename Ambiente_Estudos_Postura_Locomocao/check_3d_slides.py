from __future__ import annotations

import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TARGETS = [ROOT / "LAMINAS_3D.html", ROOT.parent / "LAMINAS_3D.html"]


def check(path: Path) -> None:
    html = path.read_text(encoding="utf-8")
    failures: list[str] = []

    if "const slides = [" not in html:
        failures.append("slide payload missing")
    if html.count("data:image/png;base64,") != 21:
        failures.append("expected 21 embedded slide images")
    for label in ["Anterior", "Próxima", "Automático", "Abrir lâmina"]:
        if label not in html:
            failures.append(f"missing control label: {label}")

    scripts = re.findall(r"<script>\s*(.*?)\s*</script>", html, flags=re.DOTALL)
    if not scripts:
        failures.append("no script found")
    else:
        tmp = ROOT / "_3d_check.js"
        tmp.write_text(scripts[-1], encoding="utf-8")
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

    print(f"OK {path.name}: 21 embedded 3D slides")


def main() -> None:
    for target in TARGETS:
        check(target)


if __name__ == "__main__":
    main()
