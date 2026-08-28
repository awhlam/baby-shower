#!/usr/bin/env python3
"""Bundle index.html into a single self-contained file.

Hosts that serve the page from a sandbox (the shared Artifact preview, an email
attachment, a file: URL) can't fetch sibling files, so the images and fonts are
inlined as data URIs. The .ics link is dropped because those hosts block
downloads the page starts itself; the Google Calendar link still works.

Usage: python3 build_preview.py [output.html]
"""

import base64
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).parent
MEDIA_TYPES = {".png": "image/png", ".jpg": "image/jpeg", ".woff2": "font/woff2"}


def data_uri(relative_path):
    path = ROOT / relative_path
    media_type = MEDIA_TYPES[path.suffix]
    payload = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{media_type};base64,{payload}"


def build(html):
    # Inline every local asset the page references.
    for relative_path in sorted(set(re.findall(r'(?:src|href)="(assets/[^"]+\.(?:png|jpg|woff2))"', html))):
        html = html.replace(f'"{relative_path}"', f'"{data_uri(relative_path)}"')

    # Preload hints and the favicon links are the host's job once inlined.
    html = re.sub(r'\s*<link rel="(?:preload|icon|apple-touch-icon)"[^>]*>', "", html)

    # Drop the .ics link — a sandboxed host won't let the page hand over a
    # file — along with its "or" separator, leaving the Google Calendar link.
    html = re.sub(
        r'\s*<span class="link-row__or">or</span>\s*<a class="link-row__link" href="assets/baby-shower\.ics".*?</a>',
        "",
        html,
        flags=re.S,
    )

    # The host supplies <!doctype>, <head> and <body>, so hand back the parts.
    title = re.search(r"<title>.*?</title>", html, re.S).group(0)
    style = re.search(r"<style>.*?</style>", html, re.S).group(0)
    body = re.search(r"<body>(.*)</body>", html, re.S).group(1).strip()
    return f"{title}\n{style}\n\n{body}\n"


if __name__ == "__main__":
    output = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "preview.html")
    output.write_text(build((ROOT / "index.html").read_text()))
    print(f"{output} — {output.stat().st_size / 1024:.0f} KB")
