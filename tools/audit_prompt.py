#!/usr/bin/env python3
"""Compare a prompt-like text file against transparency registry entries."""

from __future__ import annotations

import argparse
import json
from difflib import SequenceMatcher
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
REGISTRY_ROOT = REPO_ROOT / "registry" / "vendors"


def _load_text(path: Path) -> str:
    if path.suffix == ".json":
        data = json.loads(path.read_text(encoding="utf-8"))
        parts = [
            data.get("prompt_summary", ""),
            data.get("known_prompt_excerpt", ""),
            " ".join(data.get("limitations", [])),
        ]
        return "\n".join(part for part in parts if part)
    return path.read_text(encoding="utf-8")


def _iter_vendor_entries() -> list[Path]:
    if not REGISTRY_ROOT.exists():
        return []
    return sorted(REGISTRY_ROOT.rglob("*.json"))


def _score(candidate: str, registry_text: str) -> float:
    return SequenceMatcher(
        None,
        " ".join(candidate.lower().split()),
        " ".join(registry_text.lower().split()),
    ).ratio()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prompt", type=Path, help="Prompt text or registry JSON to audit")
    args = parser.parse_args()

    candidate = _load_text(args.prompt)
    results = []
    for entry_path in _iter_vendor_entries():
        entry_text = _load_text(entry_path)
        results.append((_score(candidate, entry_text), entry_path))

    if not results:
        print("No vendor registry entries found")
        return 1

    for ratio, entry_path in sorted(results, reverse=True):
        print(f"{ratio:.3f}\t{entry_path.relative_to(REPO_ROOT)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
