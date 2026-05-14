#!/usr/bin/env python3
"""Score vendor transparency practices from registry entries."""

from __future__ import annotations

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
VENDOR_ROOT = REPO_ROOT / "registry" / "vendors"
PRACTICE_WEIGHTS = {
    "publishes_system_prompt": 25,
    "versioned_prompt_history": 25,
    "change_highlighting": 20,
    "machine_readable_artifact": 15,
    "reproducible_capture_method": 15,
}


def _score_entry(path: Path) -> tuple[str, int]:
    data = json.loads(path.read_text(encoding="utf-8"))
    practices = data.get("transparency_practices", {})
    score = sum(
        weight for practice, weight in PRACTICE_WEIGHTS.items() if practices.get(practice)
    )
    label = f"{data.get('vendor', 'unknown')} / {data.get('model', path.stem)}"
    return label, score


def main() -> int:
    entries = sorted(VENDOR_ROOT.rglob("*.json")) if VENDOR_ROOT.exists() else []
    if not entries:
        print("No vendor entries found")
        return 1

    total = 0
    for path in entries:
        label, score = _score_entry(path)
        total += score
        print(f"{score:3d}/100\t{label}\t{path.relative_to(REPO_ROOT)}")

    print(f"average={total / len(entries):.1f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
