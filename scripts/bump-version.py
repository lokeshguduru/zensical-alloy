#!/usr/bin/env python3
"""Synchronize or verify package version and theme asset cache-bust strings.

Cache-busting is centralized on main.html (the only file the browser loads
with a ``?v=`` query). main.css has no busts because it is only a source
file - main.bundle.css is what ships and is referenced. The bumper also
regenerates the bundle so it picks up the new version comment cleanly.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PYPROJECT = ROOT / "pyproject.toml"
MAIN_HTML = ROOT / "zensical_alloy" / "main.html"
BUNDLER = ROOT / "scripts" / "bundle-css.py"


VERSION_RE = re.compile(r"\d+\.\d+\.\d+(?:[a-zA-Z0-9._-]+)?")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def replace(path: Path, pattern: str, repl: str) -> None:
    text = read_text(path)
    updated = re.sub(pattern, repl, text)
    if updated == text:
        raise SystemExit(f"No version string matched in {path}")
    write_text(path, updated)


def package_version() -> str:
    match = re.search(r'^version = "([^"]+)"', read_text(PYPROJECT), re.MULTILINE)
    if not match:
        raise SystemExit(f"No project version found in {PYPROJECT}")
    return match.group(1)


def cache_versions(path: Path) -> set[str]:
    return set(re.findall(r"\?v=([0-9A-Za-z._-]+)", read_text(path)))


def check_versions() -> None:
    expected = package_version()
    versions = cache_versions(MAIN_HTML)
    if versions != {expected}:
        seen = ", ".join(sorted(versions)) or "none"
        raise SystemExit(
            f"Version/cache-bust mismatch. Expected {expected}.\n"
            f"- {MAIN_HTML.relative_to(ROOT)} has cache versions: {seen}"
        )
    print(f"Version/cache-bust strings are in sync: {expected}")


def run_bundler() -> None:
    subprocess.run([sys.executable, str(BUNDLER)], check=True)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Update pyproject.toml and theme asset ?v= cache busts."
    )
    parser.add_argument("version", nargs="?", help="New version, for example 0.1.20")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Verify pyproject.toml and main.html use the same version.",
    )
    args = parser.parse_args()

    if args.check:
        if args.version:
            raise SystemExit("--check does not accept a version argument")
        check_versions()
        return

    if not args.version:
        raise SystemExit("Provide a version or pass --check")

    if not VERSION_RE.fullmatch(args.version):
        raise SystemExit("Version must look like 0.1.20")

    replace(PYPROJECT, r'version = "[^"]+"', f'version = "{args.version}"')
    replace(MAIN_HTML, r"\?v=[0-9A-Za-z._-]+", f"?v={args.version}")
    run_bundler()
    print(f"Updated theme version/cache busts to {args.version}")


if __name__ == "__main__":
    main()
