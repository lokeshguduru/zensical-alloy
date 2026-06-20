#!/usr/bin/env python3
"""Validate the generated accent fixture page."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "examples" / "zensical-toml" / "docs" / "accent-validation.md"
DEFAULT_HTML = ROOT / "examples" / "zensical-toml" / "site" / "accent-validation" / "index.html"
DEFAULT_TEMPLATE = ROOT / "zensical_alloy" / "main.html"
DEFAULT_TOKENS = ROOT / "zensical_alloy" / "assets" / "stylesheets" / "zensical-alloy" / "tokens.css"

NAMED_ACCENTS = (
    "red",
    "pink",
    "purple",
    "deep-purple",
    "indigo",
    "blue",
    "light-blue",
    "cyan",
    "teal",
    "green",
    "light-green",
    "lime",
    "yellow",
    "amber",
    "orange",
    "deep-orange",
)

CURATED_PRESETS = ("orange", "slate", "cyan", "violet")
SCHEMES = ("default", "slate")


class AccentFixtureParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.cases: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = {name: value or "" for name, value in attrs}
        classes = attr.get("class", "").split()
        if "alloy-accent-validation__case" in classes:
            self.cases.append(attr)


def compact(value: str) -> str:
    return " ".join(value.split())


def load_curated_presets(path: Path) -> dict[str, dict[str, str]]:
    text = path.read_text(encoding="utf-8")
    pattern = re.compile(
        r'"(?P<name>[^"]+)":\s*\(\s*"(?P<light>[^"]+)"\s*,\s*"(?P<dark>[^"]+)"\s*\)'
    )
    raw = {match.group("name"): match.groupdict() for match in pattern.finditer(text)}
    presets: dict[str, dict[str, str]] = {}
    for name in CURATED_PRESETS:
        if name in raw:
            presets[name] = {
                "default": compact(raw[name]["light"]),
                "slate": compact(raw[name]["dark"]),
            }
    return presets


def style_var(style: str, name: str) -> str | None:
    for declaration in style.split(";"):
        if ":" not in declaration:
            continue
        key, value = declaration.split(":", 1)
        if key.strip() == name:
            return compact(value.strip())
    return None


def parse_cases(path: Path) -> list[dict[str, str]]:
    parser = AccentFixtureParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser.cases


def selector_for(scheme: str, accent: str) -> str:
    return f'[data-md-color-scheme="{scheme}"][data-md-color-accent="{accent}"]'


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--html", type=Path, default=DEFAULT_HTML)
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument("--tokens", type=Path, default=DEFAULT_TOKENS)
    args = parser.parse_args()

    errors: list[str] = []
    for path in (args.source, args.html, args.template, args.tokens):
        if not path.exists():
            errors.append(f"Missing required file: {path}")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    presets = load_curated_presets(args.template)
    missing_presets = sorted(set(CURATED_PRESETS) - set(presets))
    if missing_presets:
        errors.append(f"Missing curated presets in {args.template}: {', '.join(missing_presets)}")

    tokens = args.tokens.read_text(encoding="utf-8")
    cases = parse_cases(args.html)

    named_counts: Counter[tuple[str, str]] = Counter()
    preset_counts: Counter[tuple[str, str]] = Counter()

    for case in cases:
        kind = case.get("data-accent-kind")
        scheme = case.get("data-md-color-scheme")

        if kind == "named":
            name = case.get("data-accent-name", "")
            named_counts[(name, scheme)] += 1
            if case.get("data-md-color-accent") != name:
                errors.append(f"Named accent {name}/{scheme} does not set matching data-md-color-accent")
        elif kind == "preset":
            name = case.get("data-accent-preset", "")
            preset_counts[(name, scheme)] += 1
            expected = presets.get(name, {}).get(scheme)
            actual = style_var(case.get("style", ""), "--brand-accent")
            if expected and actual != expected:
                errors.append(
                    f"Preset {name}/{scheme} uses {actual or 'no --brand-accent'}, expected {expected}"
                )
        else:
            errors.append(f"Unexpected accent fixture kind: {kind or '<missing>'}")

    expected_named = {(name, scheme) for name in NAMED_ACCENTS for scheme in SCHEMES}
    expected_presets = {(name, scheme) for name in CURATED_PRESETS for scheme in SCHEMES}
    missing_token_selectors = sorted(
        (name, scheme) for name, scheme in expected_named if selector_for(scheme, name) not in tokens
    )

    missing_named = sorted(expected_named - set(named_counts))
    extra_named = sorted(set(named_counts) - expected_named)
    duplicate_named = sorted(key for key, count in named_counts.items() if count > 1)

    missing_preset_cases = sorted(expected_presets - set(preset_counts))
    extra_preset_cases = sorted(set(preset_counts) - expected_presets)
    duplicate_preset_cases = sorted(key for key, count in preset_counts.items() if count > 1)

    if missing_named:
        errors.append(f"Missing named accent cases: {missing_named}")
    if missing_token_selectors:
        errors.append(f"Missing named accent token selectors: {missing_token_selectors}")
    if extra_named:
        errors.append(f"Unexpected named accent cases: {extra_named}")
    if duplicate_named:
        errors.append(f"Duplicate named accent cases: {duplicate_named}")
    if missing_preset_cases:
        errors.append(f"Missing preset accent cases: {missing_preset_cases}")
    if extra_preset_cases:
        errors.append(f"Unexpected preset accent cases: {extra_preset_cases}")
    if duplicate_preset_cases:
        errors.append(f"Duplicate preset accent cases: {duplicate_preset_cases}")

    if errors:
        print("Accent validation fixture failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        "Accent validation fixture OK: "
        f"{len(expected_named)} named cases and {len(expected_presets)} preset cases."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
