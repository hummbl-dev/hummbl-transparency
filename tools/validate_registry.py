#!/usr/bin/env python3
"""Validate HUMMBL transparency registry files.

This repository is intentionally stdlib-only. The validator keeps the current
bootstrap state honest and adds checks that become active as registry files land.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
REGISTRY_ROOT = REPO_ROOT / "registry"
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
REMOTE_SCHEMES = ("http://", "https://", "mailto:")


def _iter_files(suffix: str) -> list[Path]:
    return sorted(
        path
        for path in REPO_ROOT.rglob(f"*{suffix}")
        if ".git" not in path.parts
    )


def _validate_json() -> list[str]:
    failures: list[str] = []
    for path in _iter_files(".json"):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            failures.append(f"{path.relative_to(REPO_ROOT)}: invalid JSON: {exc}")
    return failures


def _validate_markdown_links() -> list[str]:
    failures: list[str] = []
    for path in _iter_files(".md"):
        text = path.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK_RE.finditer(text):
            target = match.group(1).split("#", 1)[0]
            if not target or target.startswith(REMOTE_SCHEMES):
                continue
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            if Path(target).is_absolute():
                failures.append(
                    f"{path.relative_to(REPO_ROOT)}: absolute local link {target!r}"
                )
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(REPO_ROOT)
            except ValueError:
                failures.append(
                    f"{path.relative_to(REPO_ROOT)}: link escapes repo {target!r}"
                )
                continue
            if not resolved.exists():
                failures.append(
                    f"{path.relative_to(REPO_ROOT)}: missing linked file {target!r}"
                )
    return failures


def _validate_registry_shape() -> list[str]:
    failures: list[str] = []
    if not REGISTRY_ROOT.exists():
        return failures

    for entry in REGISTRY_ROOT.rglob("*"):
        if entry.is_dir() or ".git" in entry.parts:
            continue
        relative = entry.relative_to(REGISTRY_ROOT)
        if len(relative.parts) < 2:
            failures.append(
                f"{entry.relative_to(REPO_ROOT)}: registry files must live under a category directory"
            )
    return failures


def main() -> int:
    failures = [
        *_validate_json(),
        *_validate_markdown_links(),
        *_validate_registry_shape(),
    ]
    if failures:
        for failure in failures:
            print(f"FAIL {failure}", file=sys.stderr)
        return 1

    print("Transparency registry validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
