from __future__ import annotations

import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TARGETS = [ROOT / "ANATOMIA_3D.html", ROOT.parent / "ANATOMIA_3D.html"]


def check(path: Path) -> None:
    html = path.read_text(encoding="utf-8")
    failures: list[str] = []

    required = [
        "new THREE.WebGLRenderer",
        "SphereGeometry",
        "TubeGeometry",
        "TorusKnotGeometry",
        "buildScene1",
        "buildScene21",
        "sceneBuilders",
        "switchScene",
        "Arraste para girar 360°",
    ]
    for item in required:
        if item not in html:
            failures.append(f"missing expected 3D content: {item}")

    # 21 reference images embedded
    img_count = html.count("data:image/png;base64,")
    if img_count != 21:
        failures.append(f"expected 21 embedded images, found {img_count}")

    if re.search(r"<script[^>]+src=", html, flags=re.IGNORECASE):
        failures.append("external script dependency found")

    scripts = re.findall(r"<script>\s*(.*?)\s*</script>", html, flags=re.DOTALL)
    if len(scripts) < 2:
        failures.append("expected embedded Three.js and app script")
    else:
        for index, script in enumerate(scripts, start=1):
            tmp = ROOT / f"_anatomia_3d_check_{index}.js"
            # Strip huge base64 literals to avoid OOM in node
            sanitised = re.sub(r'"[A-Za-z0-9+/=]{100,}"', '"dummy"', script)
            tmp.write_text(sanitised, encoding="utf-8")
            try:
                result = subprocess.run(["node", "--check", str(tmp)], capture_output=True, text=True)
                if result.returncode != 0:
                    failures.append(result.stderr or result.stdout or f"node --check failed for script {index}")
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

    print(f"OK {path.name}: 21 interactive Three.js scenes")


def main() -> None:
    for target in TARGETS:
        check(target)


if __name__ == "__main__":
    main()
