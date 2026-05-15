#!/usr/bin/env python3
"""
Rewrite DE post permalinks to use German-title-derived slugs.

For each pair (*-en.md, *-de.md):
  - Compute a German slug from the DE title (umlaut transliteration + lowercasing)
  - Update DE `permalink:` to `/de/<de-slug>/`
  - Add `redirect_from: ['/de/<old-en-derived-slug>/']` to the DE file so old
    URLs continue to work
  - Update EN `translation_url:` to `/de/<de-slug>/`

Idempotent: if the DE permalink already matches the computed German slug,
the file is left alone.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
POSTS_DIR = REPO_ROOT / "_posts"

FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", re.DOTALL)


def str_block_representer(dumper, data):
    if "\n" in data:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


yaml.add_representer(str, str_block_representer, Dumper=yaml.SafeDumper)


UMLAUT_MAP = str.maketrans({
    "ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss",
    "Ä": "Ae", "Ö": "Oe", "Ü": "Ue",
    "à": "a", "á": "a", "â": "a",
    "è": "e", "é": "e", "ê": "e",
    "ì": "i", "í": "i", "î": "i",
    "ò": "o", "ó": "o", "ô": "o",
    "ù": "u", "ú": "u", "û": "u",
})


def de_slugify(text: str) -> str:
    text = text.translate(UMLAUT_MAP)
    text = re.sub(r"[^A-Za-z0-9]+", "-", text).strip("-").lower()
    return text


def split_front_matter(text: str) -> tuple[dict, str]:
    m = FRONT_MATTER_RE.match(text)
    if not m:
        raise ValueError("no front matter")
    return yaml.safe_load(m.group(1)) or {}, m.group(2)


def dump_post(path: Path, fm: dict, body: str) -> None:
    yaml_text = yaml.safe_dump(
        fm, allow_unicode=True, sort_keys=False, width=10_000,
    )
    path.write_text(f"---\n{yaml_text}---\n\n{body.lstrip()}", encoding="utf-8")


def find_en_counterpart(de_path: Path) -> Path | None:
    name = de_path.name
    if not name.endswith("-de.md"):
        return None
    candidate = de_path.with_name(name[:-6] + "-en.md")
    return candidate if candidate.exists() else None


def update_pair(de_path: Path) -> bool:
    en_path = find_en_counterpart(de_path)
    if not en_path:
        print(f"!! no EN counterpart for {de_path.name}")
        return False

    de_text = de_path.read_text(encoding="utf-8-sig")
    en_text = en_path.read_text(encoding="utf-8-sig")
    de_fm, de_body = split_front_matter(de_text)
    en_fm, en_body = split_front_matter(en_text)

    de_title = de_fm.get("title")
    if not de_title:
        print(f"!! no title in {de_path.name}")
        return False

    new_slug = de_slugify(de_title)
    new_de_url = f"/de/{new_slug}/"
    old_de_url = de_fm.get("permalink")

    if old_de_url == new_de_url:
        return False  # idempotent

    de_fm["permalink"] = new_de_url
    # Track redirect from previous DE URL so old links keep working
    redirects = de_fm.get("redirect_from") or []
    if old_de_url and old_de_url not in redirects:
        redirects.append(old_de_url)
    if redirects:
        de_fm["redirect_from"] = redirects

    en_fm["translation_url"] = new_de_url

    dump_post(de_path, de_fm, de_body)
    dump_post(en_path, en_fm, en_body)
    print(f"ok  {de_path.name}: {old_de_url} -> {new_de_url}")
    return True


def main() -> int:
    n = 0
    for p in sorted(POSTS_DIR.glob("*-de.md")):
        if update_pair(p):
            n += 1
    print(f"updated {n} pairs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
