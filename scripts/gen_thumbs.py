#!/usr/bin/env python
"""Generate on-brand article hero images via the OpenAI image API.

See IMAGE_PROMPT_GUIDE.md for the rules. Edit the JOBS map below (slug -> one
scene sentence), then run:  python scripts/gen_thumbs.py
PNGs are written to assets/img/posts/<slug>.png. The API key is read from the
BatchRunner config; it is never hardcoded or committed.
"""
import json, os, base64, urllib.request, urllib.error, ssl, time

CONFIG = os.path.expandvars(r"%LOCALAPPDATA%\PBMXCreator\batchrunner_config.json")
OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "img", "posts")

# Fixed style suffix — do NOT edit (keeps every image in one visual family).
STYLE = (" — Editorial vector illustration, flat modern minimal style, clean geometric shapes, "
         "dark slate and deep teal background with bright cyan and warm amber accent highlights, "
         "professional healthcare theme, calm and precise mood, soft depth, no text, no words, "
         "no letters, no numbers, no logos, centered balanced composition, wide 16:9 hero banner.")

# slug -> one concrete scene sentence (the article's visual metaphor).
JOBS = {
    # "ed-crowding": "An emergency department viewed from above transitioning from ...",
}


def main():
    key = json.load(open(CONFIG))["OpenAiApiKey"]
    out = os.path.abspath(OUT)
    os.makedirs(out, exist_ok=True)
    ctx = ssl.create_default_context()
    for slug, scene in JOBS.items():
        body = json.dumps({
            "model": "gpt-image-1",
            "prompt": scene + STYLE,
            "size": "1536x1024",
            "quality": "high",
            "n": 1,
        }).encode()
        req = urllib.request.Request(
            "https://api.openai.com/v1/images/generations", data=body,
            headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
        print(f"generating {slug} ...", flush=True)
        try:
            with urllib.request.urlopen(req, context=ctx, timeout=300) as r:
                data = json.load(r)
            path = os.path.join(out, slug + ".png")
            open(path, "wb").write(base64.b64decode(data["data"][0]["b64_json"]))
            print(f"  saved {path} ({os.path.getsize(path)} bytes)", flush=True)
        except urllib.error.HTTPError as e:
            print(f"  HTTP {e.code}: {e.read().decode()[:500]}", flush=True)
        time.sleep(1)
    print("done")


if __name__ == "__main__":
    main()
