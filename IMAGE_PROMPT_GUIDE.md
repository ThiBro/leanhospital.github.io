# Image Prompt Guide - Lean Hospital

This guide keeps the article hero/thumbnail images **visually consistent**. Every
post image is an AI-generated editorial illustration built from a fixed *style
frame* plus a short, topic-specific *scene* sentence. Follow this whenever you
add or regenerate a post image.

## The rule in one line

`<one concrete scene sentence>` **+** `<the fixed style suffix below>` - nothing else.

Keep the scene short (one sentence, the visual metaphor of the article). The style
suffix never changes - that is what makes the set look like one family.

## The fixed style suffix (do not edit)

Append this verbatim to every scene prompt:

```
 — Editorial vector illustration, flat modern minimal style, clean geometric shapes,
dark slate and deep teal background with bright cyan and warm amber accent highlights,
professional healthcare theme, calm and precise mood, soft depth, no text, no words,
no letters, no numbers, no logos, centered balanced composition, wide 16:9 hero banner.
```

### Why each part matters
- **Editorial vector / flat modern minimal** - the house look; not photoreal, not 3D.
- **Dark slate + deep teal background, cyan + amber accents** - the brand palette. This
  is the single most important line for consistency. Do not introduce other hues.
- **no text / no words / no letters / no numbers / no logos** - AI-rendered text is
  garbled. Keep images text-free; the article supplies the words.
- **wide 16:9 hero banner, centered** - matches the `image_header` slot and the card crop.

## Writing the scene sentence

- Describe **one visual metaphor** for the article's core idea (a lean flow, a handover,
  a checklist), with concrete stylized objects (beds, stretchers, clipboard, IV line).
- Anonymize / abstract - no real people, no readable signage, no brand marks.
- Prefer symbolic clarity over detail; the flat style rewards simple compositions.

### The five launch images (reference set)

| Article topic | Scene sentence used |
|---|---|
| Virginia Mason / ThedaCare (lean) | *A hospital corridor reimagined as an efficient, streamlined lean production flow: clean directional arrows guiding stylized patient beds and caregivers smoothly along a path, a sense of removed clutter and freed space, kaizen continuous-improvement feeling.* |
| ED crowding (patient flow) | *An emergency department viewed from above transitioning from a congested crowded waiting area on one side into an orderly, flowing, well-managed space on the other, a large clock motif, stylized patients and stretchers moving through.* |
| Handoffs I-PASS / SBAR (communication) | *Two clinicians at a shift change carefully handing over a glowing patient chart between them like passing a relay baton, a bridge of connected dots symbolizing structured communication, one shift ending and the next beginning.* |
| WHO surgical checklist (patient safety) | *An operating room seen from above with a surgical team in gowns gathered around a table, a prominent clipboard checklist with glowing checkmarks floating beside them, a calm sense of pre-operative safety verification.* |
| Central-line checklist (patient safety) | *An ICU bedside scene with a stylized central-line catheter and IV, a clean five-step vertical checklist with checkmarks glowing beside it, sterile blue tones, an emphasis on infection prevention and precision.* |

> Note: the *visual-management / real-time board* article uses a real compiled Peakboard
> dashboard **screenshot** as its hero (`assets/img/posts/ward-status-board.png`), not an
> AI illustration. When an article is *about* a concrete Peakboard board, prefer a real
> rendered screenshot over an illustration.

## Generation parameters

- **API:** OpenAI Images (`POST /v1/images/generations`)
- **Model:** `gpt-image-1`
- **Size:** `1536x1024` (landscape 16:9-ish hero)
- **Quality:** `high`
- **n:** `1`
- Response is base64 (`b64_json`) - decode and write the PNG.
- **API key:** stored in the BatchRunner config at
  `%LOCALAPPDATA%\PBMXCreator\batchrunner_config.json` under `OpenAiApiKey`. Read it at
  runtime; never hardcode or commit it.

A reusable generator script lives outside the repo (scratchpad `gen_thumbs.py`) - it loads
the key from that config, loops over a `{slug: scene}` map, and writes PNGs to
`assets/img/posts/`.

## File + front-matter conventions

- **Location:** `assets/img/posts/<slug>.png`
- **Filename slug:** short and topic-based (`ed-crowding.png`, `handoff-ipass-sbar.png`),
  not the full article slug.
- **Shared across languages:** the DE and EN version of an article use the **same** image.
- **Front matter (both language files):**
  ```yaml
  image: /assets/img/posts/<slug>.png
  image_header: /assets/img/posts/<slug>.png
  ```
  `image` drives the card/social preview; `image_header` is the wide hero at the top.

## Regenerating

Same scene sentence + same suffix keeps a new render on-brand. `gpt-image-1` is not
deterministic, so re-runs differ in composition but not in style. Regenerate if a render
shows stray text, off-palette colors, or an unclear metaphor - then re-review before commit.
