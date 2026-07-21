#!/usr/bin/env python3
"""
update-llms-txt-lean-hospital.py

Regenerates the snapshot block in llms-full.txt for lean-hospital.de
from the live sitemap.xml.

Replaces only the content between <!-- AUTOGEN:START --> and <!-- AUTOGEN:END -->
markers, leaving the rest of llms-full.txt untouched.

Tailored for the bilingual Lean Hospital blog: posts live under /de/<slug>/ and
/en/<slug>/. Meta pages (about, impressum, search), the site roots, and stray
build artefacts (root-level .html files) are skipped. Posts are grouped by
language and listed reverse-chronologically by their <lastmod> date.

Usage:
    python update-llms-txt-lean-hospital.py                    # uses defaults
    python update-llms-txt-lean-hospital.py --dry-run          # prints without writing
    python update-llms-txt-lean-hospital.py --llms path/to/llms-full.txt --sitemap https://...
"""

import argparse
import re
import sys
import urllib.request
from datetime import date
from pathlib import Path
from xml.etree import ElementTree as ET

DEFAULT_SITEMAP = "https://lean-hospital.de/sitemap.xml"
DEFAULT_LLMS_PATH = "llms-full.txt"
SITE_BASE = "https://lean-hospital.de"

MARKER_START = "<!-- AUTOGEN:START — content between the AUTOGEN markers is regenerated from sitemap.xml; do not edit by hand -->"
MARKER_END = "<!-- AUTOGEN:END -->"

# Language prefixes that contain real posts
LANG_PREFIXES = ("de", "en")

# Path segments that are NOT posts and should be skipped (checked after the lang prefix)
SKIP_SLUGS = (
    "about",
    "impressum",
    "search",
)


def fetch_sitemap(url: str) -> str:
    """Download the sitemap and return its raw XML."""
    req = urllib.request.Request(url, headers={"User-Agent": "llms-txt-generator/1.0 (+https://lean-hospital.de)"})
    with urllib.request.urlopen(req, timeout=30) as response:
        return response.read().decode("utf-8")


def parse_posts(xml_text: str):
    """Extract blog posts from the sitemap as (lang, slug, date) tuples.

    A blog post is any URL that:
    - lives under /de/ or /en/
    - is not a meta page (about, impressum, search) and not a bare language root
    - has a <lastmod> date

    Returns posts sorted by date, newest first.
    """
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    root = ET.fromstring(xml_text)

    posts = []
    for url_elem in root.findall("sm:url", ns):
        loc_elem = url_elem.find("sm:loc", ns)
        lastmod_elem = url_elem.find("sm:lastmod", ns)
        if loc_elem is None or loc_elem.text is None:
            continue
        url = loc_elem.text.strip()
        if not url.startswith(SITE_BASE):
            continue
        path = url[len(SITE_BASE):].strip("/")          # e.g. "de/huddle-board" or "en/why-..."
        parts = path.split("/")
        if len(parts) < 2:
            continue                                     # bare "/de" or "/en" root → skip
        lang = parts[0]
        if lang not in LANG_PREFIXES:
            continue                                     # root .html artefacts, google-verify, etc.
        slug = "/".join(parts[1:])
        if parts[1] in SKIP_SLUGS:
            continue
        if lastmod_elem is None or lastmod_elem.text is None:
            continue                                     # meta pages have no lastmod → skip
        date_str = lastmod_elem.text[:10]                # YYYY-MM-DD
        posts.append((lang, slug, date_str))

    posts.sort(key=lambda p: p[2], reverse=True)         # newest first
    return posts


def display_title(slug: str) -> str:
    """Convert slug to a readable title — replace dashes with spaces, drop nesting."""
    return slug.rstrip("/").split("/")[-1].replace("-", " ")


def render_block(posts) -> str:
    """Render the snapshot block (everything between the markers)."""
    out = [MARKER_START, ""]
    out.append(f"### All blog posts ({len(posts)})")
    out.append("")
    for lang, label in (("de", "#### Deutsch"), ("en", "#### English")):
        lang_posts = [p for p in posts if p[0] == lang]
        if not lang_posts:
            continue
        out.append(label)
        out.append("")
        for _lang, slug, date_str in lang_posts:
            out.append(f"- {date_str} — {display_title(slug)}: {SITE_BASE}/{lang}/{slug}/")
        out.append("")
    out.append(MARKER_END)
    return "\n".join(out)


def update_snapshot_date(content: str, today: str) -> str:
    """Update the 'as of YYYY-MM-DD' date in the snapshot heading."""
    return re.sub(
        r"## Full post archive \(as of \d{4}-\d{2}-\d{2}\)",
        f"## Full post archive (as of {today})",
        content,
    )


def replace_block(content: str, new_block: str) -> str:
    """Replace everything between MARKER_START and MARKER_END (inclusive)."""
    pattern = re.compile(re.escape(MARKER_START) + r".*?" + re.escape(MARKER_END), re.DOTALL)
    if not pattern.search(content):
        sys.exit(
            f"ERROR: AUTOGEN markers not found in {DEFAULT_LLMS_PATH}.\n"
            f"Expected:\n  {MARKER_START}\n  ...\n  {MARKER_END}"
        )
    return pattern.sub(new_block, content)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--llms", default=DEFAULT_LLMS_PATH, help="Path to llms-full.txt")
    parser.add_argument("--sitemap", default=DEFAULT_SITEMAP, help="Sitemap URL")
    parser.add_argument("--dry-run", action="store_true", help="Print without writing")
    args = parser.parse_args()

    llms_path = Path(args.llms)
    if not llms_path.exists():
        sys.exit(f"ERROR: {llms_path} not found")

    print(f"Fetching {args.sitemap} ...")
    xml_text = fetch_sitemap(args.sitemap)

    print("Parsing URLs ...")
    posts = parse_posts(xml_text)
    de = sum(1 for p in posts if p[0] == "de")
    en = sum(1 for p in posts if p[0] == "en")
    print(f"  Blog posts: {len(posts)} ({de} de, {en} en)")
    if posts:
        print(f"  Newest: {posts[0][2]} — {posts[0][0]}/{posts[0][1]}")
        print(f"  Oldest: {posts[-1][2]} — {posts[-1][0]}/{posts[-1][1]}")

    today = date.today().isoformat()
    new_block = render_block(posts)

    original = llms_path.read_text(encoding="utf-8")
    updated = update_snapshot_date(original, today)
    updated = replace_block(updated, new_block)

    if updated == original:
        print("No changes — llms-full.txt already up to date.")
        return

    if args.dry_run:
        print("\n--- DRY RUN: would write the following changes ---\n")
        print(new_block[:600] + "\n... (truncated) ...\n" + new_block[-300:])
        return

    llms_path.write_text(updated, encoding="utf-8")
    print(f"Updated {llms_path} (snapshot date: {today})")


if __name__ == "__main__":
    main()
