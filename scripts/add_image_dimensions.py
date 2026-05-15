#!/usr/bin/env python3
"""
Walk _posts/*.md and append a kramdown IAL block

  ![alt](url)  -->  ![alt](url){: loading="lazy" width="W" height="H"}

with `width`/`height` read from the PNG/JPG header on disk. Idempotent:
images that already carry an IAL with the same width/height key are skipped.
"""
from __future__ import annotations

import re
import struct
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
POSTS_DIR = REPO_ROOT / "_posts"

# Match `![alt](url)`, optionally followed by an existing {: ...} IAL.
IMG_RE = re.compile(
    r"(!\[(?P<alt>[^\]]*)\]\((?P<url>[^)]+)\))(?P<ial>\{:[^}]*\})?",
)


def png_dimensions(path: Path) -> tuple[int, int] | None:
    with path.open("rb") as f:
        sig = f.read(8)
        if sig[:8] != b"\x89PNG\r\n\x1a\n":
            return None
        f.read(4)  # length
        if f.read(4) != b"IHDR":
            return None
        w = struct.unpack(">I", f.read(4))[0]
        h = struct.unpack(">I", f.read(4))[0]
        return w, h


def jpeg_dimensions(path: Path) -> tuple[int, int] | None:
    """Tiny JPEG SOF parser."""
    with path.open("rb") as f:
        data = f.read()
    if data[:2] != b"\xff\xd8":
        return None
    i = 2
    while i < len(data) - 1:
        if data[i] != 0xFF:
            return None
        marker = data[i + 1]
        # Skip standalone markers
        if marker in (0xD8, 0xD9):
            i += 2
            continue
        if 0xD0 <= marker <= 0xD7 or marker == 0x01:
            i += 2
            continue
        seg_len = struct.unpack(">H", data[i + 2 : i + 4])[0]
        # SOF0..SOF15 (except DHT=0xC4, DAC=0xCC, DNL=0xDC)
        if 0xC0 <= marker <= 0xCF and marker not in (0xC4, 0xC8, 0xCC):
            h = struct.unpack(">H", data[i + 5 : i + 7])[0]
            w = struct.unpack(">H", data[i + 7 : i + 9])[0]
            return w, h
        i += 2 + seg_len
    return None


def image_dimensions(path: Path) -> tuple[int, int] | None:
    suffix = path.suffix.lower()
    if suffix == ".png":
        return png_dimensions(path)
    if suffix in (".jpg", ".jpeg"):
        return jpeg_dimensions(path)
    return None


SITE_BASEURL_RE = re.compile(r"\{\{\s*site\.baseurl\s*\}\}")


def resolve_image_path(url: str) -> Path | None:
    """Map a Markdown image URL to a filesystem path under the repo."""
    # Strip Liquid {{ site.baseurl }} and trailing query/fragment
    cleaned = SITE_BASEURL_RE.sub("", url).strip()
    cleaned = cleaned.split("?", 1)[0].split("#", 1)[0]
    # Only handle site-relative paths (skip http(s):// etc.)
    if cleaned.startswith(("http://", "https://", "//")):
        return None
    cleaned = cleaned.lstrip("/")
    candidate = REPO_ROOT / cleaned
    return candidate if candidate.is_file() else None


def update_post(path: Path) -> bool:
    text = path.read_text(encoding="utf-8-sig")
    changed = False

    def replace(m: re.Match) -> str:
        nonlocal changed
        whole = m.group(1)
        url = m.group("url").strip()
        existing_ial = m.group("ial") or ""
        img_path = resolve_image_path(url)
        if img_path is None:
            return whole + existing_ial
        dims = image_dimensions(img_path)
        if dims is None:
            return whole + existing_ial
        w, h = dims
        # If existing IAL already has a width=, leave the markup alone.
        if "width=" in existing_ial:
            return whole + existing_ial
        new_ial = f'{{: loading="lazy" width="{w}" height="{h}"}}'
        # Merge with any extra IAL attrs the author already set
        if existing_ial:
            inner = existing_ial[2:-1].strip()
            new_ial = '{: loading="lazy" width="' + str(w) + '" height="' + str(h) + '" ' + inner + '}'
        changed = True
        return whole + new_ial

    new_text = IMG_RE.sub(replace, text)
    if changed and new_text != text:
        path.write_text(new_text, encoding="utf-8")
        return True
    return False


def main() -> int:
    n = 0
    for p in sorted(POSTS_DIR.glob("*.md")):
        if update_post(p):
            n += 1
            print(f"ok  {p.name}")
    print(f"updated {n} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
