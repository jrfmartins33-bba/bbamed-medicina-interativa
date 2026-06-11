from __future__ import annotations

import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TARGETS = [ROOT / "MATERIAIS.html", ROOT.parent / "INICIAR_AQUI.html"]
BAD_HREFS = [
    'href="index.html"',
    'href="GUIA_DE_ESTUDOS.html"',
    'href="QUESTOES_REVISAO.html"',
    'href="FLASHCARDS.html"',
    'href="README.html"',
    'href="LAMINAS_3D.html"',
]


def check(path: Path) -> None:
    failures: list[str] = []
    keys_to_find = {"index", "laminas3d", "guia", "questoes", "flashcards", "readme"}
    found_keys = set()
    found_portable_materials = False
    found_blob_mechanics = False
    bad_hrefs_found = set()

    with path.open("r", encoding="utf-8") as f:
        for line in f:
            for href in BAD_HREFS:
                if href in line:
                    bad_hrefs_found.add(href)
            for key in keys_to_find:
                if f'data-open-material="{key}"' in line:
                    found_keys.add(key)
            if "const portableMaterials" in line:
                found_portable_materials = True
            if "URL.createObjectURL" in line or "new Blob" in line or "blob:" in line:
                found_blob_mechanics = True

    for href in bad_hrefs_found:
        failures.append(f"fragile relative link remains: {href}")

    missing_keys = keys_to_find - found_keys
    for key in missing_keys:
        failures.append(f"missing portable button: {key}")

    if not found_portable_materials:
        failures.append("portable payload script missing")
    if found_blob_mechanics:
        failures.append("portal still uses blob URL mechanics")

    if failures:
        print(f"FAIL {path}")
        for item in failures:
            print(f"- {item}")
        raise SystemExit(1)
    print(f"OK {path.name}")


def main() -> None:
    for target in TARGETS:
        check(target)


if __name__ == "__main__":
    main()
