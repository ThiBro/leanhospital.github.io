#!/usr/bin/env python3
"""
One-shot migration: split each _posts/<date>-<slug>.md into
  _posts/<date>-<slug>-en.md  (permalink /en/<slug>/)
  _posts/<date>-<slug>-de.md  (permalink /de/<slug>/)

After the run, the originals are deleted. Re-running on already-migrated
files (any *-en.md / *-de.md) is a no-op for those files.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
POSTS_DIR = REPO_ROOT / "_posts"

FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", re.DOTALL)
DATA_LANG_RE = re.compile(
    r'<div\s+data-lang="(en|de)"[^>]*>\s*\n?(.*?)\n?\s*</div>',
    re.DOTALL,
)


def str_block_representer(dumper, data):
    if "\n" in data:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


yaml.add_representer(str, str_block_representer, Dumper=yaml.SafeDumper)


def slugify(text: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "-", text).strip("-").lower()


def split_front_matter(text: str) -> tuple[dict, str]:
    m = FRONT_MATTER_RE.match(text)
    if not m:
        raise ValueError("no front matter")
    fm = yaml.safe_load(m.group(1)) or {}
    return fm, m.group(2)


def extract_lang_blocks(body: str) -> dict[str, str]:
    blocks: dict[str, str] = {}
    for lang, content in DATA_LANG_RE.findall(body):
        blocks[lang] = content.strip()
    return blocks


def build_lang_front_matter(fm: dict, lang: str) -> dict:
    """Return a per-language flat front matter.

    For each `<key>` / `<key>_de` pair the EN file gets the bare key, the DE
    file gets the `_de` value (or the bare value as fallback). Bare keys
    without a `_de` counterpart are kept on both sides.
    """
    out: dict = {}
    # First pass: collect bare keys (skip *_de — handled below)
    for k, v in fm.items():
        if k.endswith("_de"):
            continue
        out[k] = v
    # Second pass: for DE, override with *_de values
    if lang == "de":
        for k, v in fm.items():
            if k.endswith("_de"):
                base = k[:-3]
                out[base] = v
    return out


def localise_downloads(fm: dict, lang: str) -> list | None:
    if "downloads" not in fm:
        return None
    out = []
    for dl in fm["downloads"]:
        if lang == "en":
            name = dl.get("name") or dl.get("name_de")
            url = dl.get("url") or dl.get("url_de")
        else:
            name = dl.get("name_de") or dl.get("name")
            url = dl.get("url_de") or dl.get("url")
        entry = {}
        if name is not None:
            entry["name"] = name
        if url is not None:
            entry["url"] = url
        out.append(entry)
    return out


def dump_post(path: Path, fm: dict, body: str) -> None:
    yaml_text = yaml.safe_dump(
        fm,
        allow_unicode=True,
        sort_keys=False,
        width=10_000,
    )
    out = f"---\n{yaml_text}---\n\n{body.rstrip()}\n"
    path.write_text(out, encoding="utf-8")


def migrate(path: Path) -> tuple[Path, Path] | None:
    name = path.stem
    if name.endswith("-en") or name.endswith("-de"):
        return None  # already migrated

    text = path.read_text(encoding="utf-8-sig")
    try:
        fm, body = split_front_matter(text)
    except ValueError:
        print(f"!! no front matter: {path}")
        return None

    blocks = extract_lang_blocks(body)
    if "en" not in blocks or "de" not in blocks:
        print(f"!! missing data-lang blocks in {path}; got keys={list(blocks)}")
        return None

    if len(name) < 11 or name[10] != "-":
        print(f"!! unexpected filename pattern: {path}")
        return None
    date_prefix = name[:10]
    slug_raw = name[11:]
    slug = slugify(slug_raw)
    old_url = f"/{slug_raw}.html"

    en_fm = build_lang_front_matter(fm, "en")
    de_fm = build_lang_front_matter(fm, "de")

    # Remove *_de keys from EN side (they live as bare keys on DE side now)
    for k in list(en_fm.keys()):
        if k.endswith("_de"):
            del en_fm[k]
    for k in list(de_fm.keys()):
        if k.endswith("_de"):
            del de_fm[k]

    # Downloads need per-language flattening
    en_dl = localise_downloads(fm, "en")
    de_dl = localise_downloads(fm, "de")
    if en_dl is not None:
        en_fm["downloads"] = en_dl
    if de_dl is not None:
        de_fm["downloads"] = de_dl

    en_fm["lang"] = "en"
    de_fm["lang"] = "de"
    en_fm["permalink"] = f"/en/{slug}/"
    de_fm["permalink"] = f"/de/{slug}/"
    en_fm["translation_url"] = f"/de/{slug}/"
    de_fm["translation_url"] = f"/en/{slug}/"
    en_fm.setdefault("redirect_from", []).append(old_url)

    en_path = path.with_name(f"{name}-en.md")
    de_path = path.with_name(f"{name}-de.md")
    dump_post(en_path, en_fm, blocks["en"])
    dump_post(de_path, de_fm, blocks["de"])

    path.unlink()
    print(f"ok  {path.name} -> {en_path.name} + {de_path.name}")
    return en_path, de_path


def main() -> int:
    if not POSTS_DIR.is_dir():
        print(f"missing posts dir: {POSTS_DIR}", file=sys.stderr)
        return 1
    n = 0
    for p in sorted(POSTS_DIR.glob("*.md")):
        result = migrate(p)
        if result:
            n += 1
    print(f"migrated {n} posts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
