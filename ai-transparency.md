---
title: AI Transparency
layout: about
lang: en
permalink: /ai-transparency/
translation_url: /de/ki-transparenz/
description: "AI transparency on lean-hospital.de: which texts and images come from artificial intelligence, how they are labelled, and who holds editorial responsibility."
hero:
  title: AI Transparency
  subtitle: What on this blog comes from artificial intelligence — and how you can tell
---

**In short:** The articles on lean-hospital.de are written with the support of AI language models, and most header images are AI-generated illustrations. Every article says so in three places: as a label in the article's top line, as a marker on an AI-generated header image, and as a detailed box at the end of the text. On top of that, every article page carries a machine-readable label in its source. Editorial responsibility for every published article rests with Martin Neumann.

## What artificial intelligence does on this blog

**Text.** Articles are drafted and written out with an AI language model. The model works against a fixed rulebook: structure, audience, tone and sourcing requirements are all prescribed.

**Images.** The header images of most articles are AI-generated editorial illustrations (model `gpt-image-1`). They show symbolic scenes — an emergency department, a handover, a checklist — with no real people, real places or real devices. Where an article shows a concrete dashboard, the header image is a real screen capture of the running application instead.

**This page too** was written with AI support and reviewed and released by Martin Neumann.

## What a human does

Martin Neumann releases every article before publication. That includes:

- **Checking sources.** Every figure and every claim that goes back to a study, a law or a regulation is checked against the original source. The sources are listed at the end of each article with a resolving URL.
- **Judging the substance.** Whether a method holds up in a German hospital's daily routine is decided by practical experience, not by the model.
- **Taking responsibility.** Martin Neumann is liable for the published content as the operator of this blog. The details are in the [legal notice](/impressum/).

What an AI model is **not** allowed to do here: estimate figures, invent studies, construct quotations. Where a claim cannot be evidenced, it is dropped from the article.

## How an article is labelled

Every article carries the label in three places, so that it lands even when the page is only skimmed:

1. **In the article's top line**, next to the date and reading time, sits the label "AI disclosure". It jumps straight to the detailed box.
2. **On an AI-generated header image** sits the marker "AI-generated image" — visible as soon as the image is.
3. **At the end of the article** stands the box "AI disclosure: how this article was made", with one statement each for text and image.

An article whose text was written entirely without AI says so in the same box. The label is therefore never missing — it just says something different.

## The machine-readable label

Article 50(2) of the AI Act requires AI-generated content to be detectable as such in a **machine-readable** format. Every article page therefore carries this in the head of its source:

```html
<meta name="ai-disclosure" content="text=ai-generated; image=ai-generated">
<meta name="ai-disclosure-policy" content="https://lean-hospital.de/ai-transparency/">
<meta name="ai-generated" content="true">
```

Alongside it sits a JSON-LD block that uses the **IPTC Digital Source Type** — the established controlled vocabulary for how a piece of media came about:

```json
{
  "@type": "schema:CreativeWork",
  "digitalSourceType": "http://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia",
  "schema:associatedMedia": {
    "@type": "schema:ImageObject",
    "digitalSourceType": "http://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia"
  }
}
```

The values in use:

| Value | Meaning |
|---|---|
| `trainedAlgorithmicMedia` | Created by a trained AI model |
| `compositeWithTrainedAlgorithmicMedia` | Real capture, post-processed with AI tools |
| `softwareImage` | Real screen capture of running software |
| `digitalCapture` | Real photograph |

Every header image additionally carries the attributes `data-ai-generated` and `data-digital-source-type` in the source, so its origin can be read off the image element itself.

## The legal basis

The basis is **Article 50 of Regulation (EU) 2024/1689** on artificial intelligence, known as the AI Act. It has been applicable since **2 August 2026** and asks for two things:

- **Paragraph 2:** Anyone operating an AI system that generates synthetic image, text, audio or video content ensures that the outputs are marked in a machine-readable format as artificially generated.
- **Paragraph 4:** Anyone publishing AI-generated or AI-manipulated text in order to inform the public on matters of public interest discloses that fact.

Paragraph 4 carries an exception for content that has undergone editorial review and for which a natural or legal person holds responsibility. That exception would apply to lean-hospital.de — **we deliberately do not rely on it.** Anyone reading about hospital processes should know how the text came about.

## Frequently asked questions about the AI label

### Are the figures in the articles invented by an AI?

No. Every figure goes back to a named source, listed at the end of the article with a resolving URL. Claims without an evidenced source are cut rather than filled in with an estimate.

### How do I tell whether an image is real?

An AI-generated header image carries the visible marker "AI-generated image" in its top right corner. The box at the end of the article names the origin explicitly, and the source carries it machine-readably on the image element itself.

### Does the label apply to older articles too?

Yes. Every article already published was labelled retroactively, each one according to how it was actually made.

### Who is liable for the content?

Martin Neumann as the operator of this blog. The details under § 5 DDG are in the [legal notice](/impressum/).

## Found a mistake?

If you spot a wrong figure, a wrong source attribution or a missing label in an article, write to **kontakt@lean-hospital.de**. Corrections are carried into the article and become visible in its modification date.
