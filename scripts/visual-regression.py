#!/usr/bin/env python3
"""Capture visual QA screenshots for the local example site."""

from __future__ import annotations

import asyncio
import os
import sys
from pathlib import Path
from urllib.parse import urljoin

try:
    from playwright.async_api import async_playwright
except ImportError:
    print(
        "Playwright is not installed. Run `.venv/bin/pip install -e '.[visual]'` "
        "and `.venv/bin/python -m playwright install chromium` first.",
        file=sys.stderr,
    )
    raise SystemExit(1)


BASE_URL = os.environ.get("BASE_URL", "http://127.0.0.1:8765")
OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "tests/visual/screenshots"))

PAGES = [
    ("/", "home"),
    ("/getting-started/installation/", "installation"),
    ("/getting-started/configuration/", "configuration"),
    ("/components/code/", "code"),
    ("/components/callouts/", "callouts"),
    ("/components/tables/", "tables"),
    ("/components/charts/", "charts"),
    ("/components/kitchen-sink/", "kitchen-sink"),
    ("/theming/", "theming"),
    ("/architecture/", "architecture"),
    ("/quality/", "quality"),
    ("/contributing/", "contributing"),
]

VIEWPORTS = [
    ("desktop", {"width": 1440, "height": 1000}),
    ("mobile", {"width": 390, "height": 844}),
]

MODES = [
    ("light", "light", "default", "white"),
    ("dark", "dark", "slate", "black"),
]


async def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for screenshot in OUTPUT_DIR.glob("*.png"):
        screenshot.unlink()

    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch()
        context = await browser.new_context(device_scale_factor=1)
        page = await context.new_page()

        for viewport_name, viewport in VIEWPORTS:
            await page.set_viewport_size(viewport)

            for mode_name, media_scheme, color_scheme, primary in MODES:
                await page.emulate_media(color_scheme=media_scheme)

                for path, name in PAGES:
                    await page.goto(urljoin(BASE_URL, path), wait_until="networkidle")
                    await page.evaluate(
                        """([scheme, primary]) => {
                            document.body.setAttribute("data-md-color-scheme", scheme);
                            document.body.setAttribute("data-md-color-primary", primary);
                            document.body.setAttribute("data-md-color-accent", "orange");
                        }""",
                        [color_scheme, primary],
                    )
                    await page.add_style_tag(
                        content="""
                            *, *::before, *::after {
                              animation-duration: 0s !important;
                              transition-duration: 0s !important;
                              scroll-behavior: auto !important;
                            }
                        """
                    )
                    await page.screenshot(
                        path=OUTPUT_DIR / f"{viewport_name}-{mode_name}-{name}.png",
                        full_page=True,
                    )

        await browser.close()

    print(f"Wrote screenshots to {OUTPUT_DIR}")


if __name__ == "__main__":
    asyncio.run(main())
