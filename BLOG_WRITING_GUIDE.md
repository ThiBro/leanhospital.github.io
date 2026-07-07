# Blog Writing Guide - Lean Hospital

This guide documents the conventions for writing articles on the Jekyll blog **"Lean Hospital"**. Follow these rules when creating new posts.

## What an article is

Each article is a **thorough, evidence-based essay about an efficient-process or patient-safety topic in healthcare** - lean management, patient flow, waiting times, hand-offs, checklists, waste reduction. An article is not a listicle and not marketing. It tells the story of a real problem and what the evidence says actually works.

**Non-negotiable rule: every factual claim, statistic, and quote must come from a real, verifiable source. Never invent numbers, quotes, or citations.** If a figure cannot be confirmed against a primary or authoritative source, leave it out. When sources disagree or a claim is weak, say so in the article - honest nuance is a feature, not a flaw.

### The house style, in short

- **Lead with a concrete hook** - a scene or a stakes-setting paragraph, not a definition.
- **Use real primary sources**: peer-reviewed journals (NEJM, BMJ, Annals of Emergency Medicine, etc.), WHO, AHRQ, The Joint Commission, IHI, named books, and reputable reporting.
- **Quote real people verbatim** where it strengthens the piece (e.g., a study author, Atul Gawande), using exact wording in quotation marks with attribution.
- **Include the counter-evidence.** Our best articles show where an intervention *failed* or where evidence is "mixed" (e.g., the Urbach 2014 checklist null result, SBAR's mixed record). This builds trust.
- **End with the transferable lesson**, not a summary.
- **Length:** roughly 800-1,200 words.

## Languages

The blog is bilingual (English + German). Every article is written as **two files**, one per language, that link to each other via `translation_url`. Keep the two versions in sync in structure, figures, and citations. Translate faithfully; do not add claims to one language that are not in the other.

- English file suffix: `-en.md`
- German file suffix: `-de.md`

## File naming

Posts live in `_posts/` and are named:

```
_posts/YYYY-MM-DD-Title-With-Hyphens-en.md
_posts/YYYY-MM-DD-Title-With-Hyphens-de.md
```

> **Gotcha:** Jekyll silently skips posts whose `date` is in the future (in UTC). Always use `00:00:00 +0000` (or a clearly past time) so the post builds. If a new post does not appear, check the date/time first.

## Front matter

Required fields for every new post:

| Field | Notes |
| --- | --- |
| `layout` | Always `post` |
| `title` | Human-readable title in the file's language |
| `date` | `YYYY-MM-DD 00:00:00 +0000` (see the future-date gotcha above) |
| `tags` | One topic tag. Use the established set below |
| `description` | 1-2 sentence summary; used for cards, SEO, and social previews. Make it concrete and specific |
| `lang` | `en` or `de` |
| `permalink` | `/en/<slug>/` or `/de/<slug>/` |
| `translation_url` | Permalink of the counterpart-language article |
| `redirect_from` | Optional legacy `.html` path |

The slug is the lower-cased, hyphenated form of the title. For example,
`_posts/2026-07-02-My-Article-en.md` becomes
`https://lean-hospital.de/en/my-article/`.

### Established tags

Keep tags consistent so the archive and cards stay clean. Currently in use:

- English: `lean-management`, `patient-flow`, `communication`, `patient-safety`
- German: `lean-management`, `patientenfluss`, `kommunikation`, `patientensicherheit`

Add a new tag only when a topic genuinely does not fit these.

### Example front matter (English)

```yaml
---
layout: post
title: What Virginia Mason and ThedaCare Proved About Lean in Hospitals
date: 2026-06-24 00:00:00 +0000
tags: lean-management
description: Two American health systems adopted the Toyota Production System and measured the results - freed space, shorter lead times, and safer care.
lang: en
permalink: /en/what-virginia-mason-and-thedacare-proved-about-lean-in-hospitals/
translation_url: /de/was-virginia-mason-und-thedacare-ueber-lean-im-krankenhaus-bewiesen-haben/
redirect_from:
- /What-Virginia-Mason-and-ThedaCare-Proved-About-Lean-in-Hospitals.html
---
```

## Body structure

1. **Opening hook** (1 paragraph) - a scene or the stakes. No heading.
2. **`##` sections** - 3-6 of them, each advancing the argument (the problem, the intervention, the results, the counter-evidence, the lesson).
3. **Inline attribution** - name the source in the prose, e.g. *"(Starmer et al., New England Journal of Medicine, 2014)"* or *"Lead author Alex Haynes described..."*.
4. **Direct quotes** in Markdown blockquotes (`>`) with clear attribution.
5. **A closing `## Sources` (English) / `## Quellen` (German) section** - a numbered list of every source, with author/title/publication/year and a working URL in angle brackets, e.g. `<https://...>`.

### Sources section - the standard

Every article ends with a numbered reference list. Format each entry as:

```
1. Author(s). "Title." *Publication*, Year. <https://working-url>
```

Only list sources you actually relied on, and only URLs that resolve. Prefer the most authoritative link (journal/PubMed/official body over a blog summary).

## Handling uncertainty

- If a well-known figure cannot be verified against a primary source, **omit it** (e.g., avoid the widely-circulated but uncited "80% of errors" handoff statistic).
- Attribute figures to the *right* source: a number that appears only in a journalist's account (e.g., Gawande's *New Yorker* estimate of "1,500 lives") should be attributed to that account, not to the underlying study.
- When two studies conflict, present both and explain the likely reason (usually implementation quality, not the tool itself).

## Optional front matter

- `image` - hero/card image path under `/assets/...`. If omitted, the post uses a clean text hero and the card renders without an image. For AI-generated hero images, follow [IMAGE_PROMPT_GUIDE.md](IMAGE_PROMPT_GUIDE.md) so the set stays visually consistent.
- `image_header` - a wider hero image used only at the top of the article.
- `read_more_links` - list of `{title, url}` related links shown in the right sidebar under "Resources".

## Reference articles

The five launch articles are the canonical examples of this style - read them before writing a new one:

- Virginia Mason / ThedaCare (lean management)
- Emergency-department crowding and patient flow
- I-PASS and SBAR hand-offs (communication)
- The WHO Surgical Safety Checklist (patient safety, with counter-evidence)
- The Keystone ICU central-line checklist (patient safety)
