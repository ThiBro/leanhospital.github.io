# Blog Writing Guide for Claude

This guide documents all conventions for writing articles on the Jekyll blog **"Peakboard Guru"**. Follow these rules exactly when creating new posts.

**Language:** Every article is **bilingual (English + German)**. Each post lives as **two sibling files** in `_posts/`: one English file (`*-en.md`) and one German file (`*-de.md`), each containing the content for that language only. Both files are deployed at their own URL (`/en/<slug>/` and `/de/<slug>/`) and link to each other through a `translation_url:` field. There are no `<div data-lang>` wrappers and no `*_de` front matter fields.

**Content focus:** Articles describe a **real-world use case** and the business value it delivers. Focus on the problem being solved, who benefits, and the outcome. Do NOT explain Peakboard internals, technical implementation details, or how the dashboard was built step by step.

---

## 1. File Naming

**Pattern:** two files per post, sharing the same date and slug:

```
_posts/YYYY-MM-DD-Title-With-Hyphens-en.md
_posts/YYYY-MM-DD-Title-With-Hyphens-de.md
```

- Date prefix must match the `date:` field in front matter and must be identical in both files
- Slug portion mirrors the English title (so the EN and DE files sort next to each other in the file list)
- Spaces in the title become hyphens, preserve title case, remove apostrophes/colons
- The `-en` / `-de` suffix is what splits the two language variants

**Example:**
```
_posts/2026-03-03-Fitness-Studio-Class-Schedule-Display-en.md
_posts/2026-03-03-Fitness-Studio-Class-Schedule-Display-de.md
```

Both files generate URLs derived from the slug portion only, lower-cased:
- `https://peakboard-guru.com/en/fitness-studio-class-schedule-display/`
- `https://peakboard-guru.com/de/fitness-studio-class-schedule-display/`

---

## 2. Front Matter

Each language file has its own simple front matter — no `*_de` paired fields anymore. The two files differ in `title`, `description`, `prompt`, `lang`, `permalink`, and `translation_url`; everything else (date, tags, image, downloads urls, etc.) is identical.

### Required Fields

```yaml
---
layout: post
title: Your Article Title Here
date: 2026-03-03 00:00:00 +0000
tags: tag1 tag2
image: /assets/2026-03-03-14-30-00/title.png
lang: en                                              # or `de`
permalink: /en/your-article-title-here/               # or `/de/your-article-title-here/`
translation_url: /de/your-article-title-here/         # or `/en/...`
---
```

| Field | Description |
|-------|-------------|
| `layout` | Always `post` |
| `title` | The article title in this file's language. Human-readable, often uses ` - ` as separator for subtitles |
| `date` | Format: `YYYY-MM-DD HH:MM:SS +0000`. Identical in both language files |
| `tags` | **Space-separated** tag slugs (not a YAML list!). First tag = primary category. Tag slugs stay in English. Identical in both files |
| `image` | Path to hero image. Pattern: `/assets/YYYY-MM-DD-HH-MM-SS/title.png` (or `.jpg`). Shared by both languages |
| `lang` | `en` or `de`. Drives `<html lang>`, language-filtered listings, and hreflang tags |
| `permalink` | Output URL of this file. Pattern: `/en/<slug>/` or `/de/<slug>/`. The slug is the lower-cased, hyphenated title |
| `translation_url` | Pointer to the sibling file's URL. Used by the language toggle and hreflang `<link rel="alternate">` tags |

### Recommended Fields

Always include `bg_alternative` and `description` for new posts. `description` is per-language and is used for the SEO meta tag and the hero subtitle.

```yaml
bg_alternative: true
description: "One or two sentences summarizing what this article covers."
```

### Downloads

`downloads` is a per-language list of `.pbmx` (and similar) files shown as Guru download buttons in the right sidebar. Each entry needs a `name` and a `url`.

```yaml
downloads:
  - name: ProjectFile.pbmx
    url: /assets/2026-03-03-14-30-00/ProjectFile.pbmx
```

#### Multi-Project Downloads

Some articles cover a multi-project system (e.g., an ordering kiosk + a kitchen display). List all project files with descriptive names:

```yaml
downloads:
  - name: OrderDashboard.pbmx
    url: /assets/2026-03-03-14-30-00/OrderDashboard.pbmx
  - name: KitchenDisplay.pbmx
    url: /assets/2026-03-03-14-30-00/KitchenDisplay.pbmx
```

#### Bilingual Downloads

If a `.pbmx` project exists in both an English and a German variant (e.g., translated labels inside the dashboard), reference the **language-matched file** in each language's front matter:

```yaml
# in *-en.md
downloads:
  - name: GymClassSchedule.pbmx
    url: /assets/2026-03-03-14-30-00/GymClassSchedule_en.pbmx

# in *-de.md
downloads:
  - name: Kursplan.pbmx
    url: /assets/2026-03-03-14-30-00/Kursplan_de.pbmx
```

If the project has no translatable text (icons/numbers only), reference the same `.pbmx` URL in both files.

### Optional Fields

```yaml
prompt: |
  The exact prompt that was given to the AI to generate the Peakboard
  project for this article. Use the YAML block scalar (|) so explicit
  line breaks in the source are preserved.
read_more_links:
  - name: Other UI design articles
    url: /category/ui
  - name: More use case examples
    url: /category/usecase
redirect_from:
  - /Old-Article-Title.html
```

| Field | Description |
|-------|-------------|
| `bg_alternative` | `true` = light hero box style with a semi-transparent text box over the image. Always use for new posts |
| `description` | Summary in this file's language. Used for the SEO `<meta name="description">` and below the hero title. Always include |
| `prompt` | **Required for every NEW post.** The exact AI prompt used to create the Peakboard project, in this file's language. Rendered in a visually distinct box at the bottom of the article body. Use YAML block scalar (`\|`) so line breaks survive |
| `downloads` | List of `{name, url}` rendered as Guru download button images in the right sidebar |
| `read_more_links` | List of `{name, url}` shown in the sidebar under "Related Links". Each language file uses names in that language; URLs may be identical |
| `redirect_from` | Optional list of legacy paths (from `jekyll-redirect-from`) that should 301 to this file. Only the **English** file should redirect from the pre-migration `/<Title>.html` URL |

### Post Template (Single Project)

**`_posts/2026-03-03-Sample-Article-en.md`**:
```yaml
---
layout: post
title: Sample Article - With Subtitle
date: 2026-03-03 00:00:00 +0000
tags: fitness
image: /assets/2026-03-03-14-30-00/title.png
bg_alternative: true
description: "Short summary of the article for SEO and hero display."
prompt: |
  Build a Peakboard dashboard that shows the daily class schedule for a
  fitness studio with KPI tiles, an occupancy bar chart, and a countdown
  to the next class.
downloads:
  - name: SampleProject.pbmx
    url: /assets/2026-03-03-14-30-00/SampleProject.pbmx
lang: en
permalink: /en/sample-article-with-subtitle/
translation_url: /de/sample-article-with-subtitle/
---
```

**`_posts/2026-03-03-Sample-Article-de.md`**:
```yaml
---
layout: post
title: Beispielartikel - Mit Untertitel
date: 2026-03-03 00:00:00 +0000
tags: fitness
image: /assets/2026-03-03-14-30-00/title.png
bg_alternative: true
description: "Kurze Zusammenfassung des Artikels für SEO und Hero-Anzeige."
prompt: |
  Erstelle ein Peakboard-Dashboard, das den Tageskursplan eines
  Fitnessstudios mit KPI-Kacheln, einem Auslastungsbalkendiagramm und
  einem Countdown zum nächsten Kurs zeigt.
downloads:
  - name: Beispielprojekt.pbmx
    url: /assets/2026-03-03-14-30-00/SampleProject.pbmx
lang: de
permalink: /de/sample-article-with-subtitle/
translation_url: /en/sample-article-with-subtitle/
---
```

The DE file's `permalink` slug mirrors the EN slug (we keep one slug per post so the URLs stay aligned and easy to spot-check).

---

## 3. Tags

Tags are space-separated in front matter. Use an **industry-specific** tag that best describes the use case. Available tags:

| Tag | Industry |
|-----|----------|
| `production` | Manufacturing, factory floors, assembly lines |
| `logistics` | Warehousing, shipping, supply chain |
| `hotel` | Hotels, hospitality |
| `gastronomy` | Restaurants, catering, food service |
| `retail` | Shops, supermarkets, point of sale |
| `healthcare` | Hospitals, clinics, dental practices |
| `fitness` | Gyms, sports studios |
| `food-and-beverage` | Breweries, food production, beverages |
| `office` | Office environments, meeting rooms |
| `energy` | Energy, utilities, sustainability |
| `transportation` | Public transit, airports, fleet management |

Tag slugs stay in **English** in both files. The first tag is used as the primary category shown on the article card. You can use multiple tags if applicable (e.g. `production logistics`). Add new tags as needed when no existing tag fits - keep them lowercase, use hyphens for multi-word tags.

---

## 4. Article Content Structure

The body is plain markdown for **just this file's language**. No language wrappers, no `data-lang` divs, no `markdown="1"` boilerplate.

```markdown
---
...front matter...
---
{% include youtube.html id="VIDEO_ID" %}

In this article we...

## First section

...
```

Shared assets (the YouTube include, an opening `<video>` element) sit at the top of the body in **both** files — they are just markdown, not language-specific.

### Opening Paragraph (No Header!)

Every article starts with a direct intro paragraph **without** any heading. No `# Introduction`, no `---` separator. Just text immediately after the front matter and any shared video include.

### Headers

- **`##` (H2)** for main sections - the primary structural divisions
- **`###` (H3)** for subsections within a section
- **Never use `#` (H1)** in the body - the layout renders the title from front matter
- Common section patterns:
  - Setup / context section
  - Step-by-step procedural sections (one H2 per step)
  - `## Result` or `## Conclusion` at the end

### Images

Store images in `/assets/YYYY-MM-DD-HH-MM-SS/` folder matching the post date. The folder is shared by both language files.

**Naming conventions:**
- Hero image: `title.png` or `title.jpg` (match the actual file extension). The hero is language-neutral and not localized
- Screenshot (single project, English/default): `010.png`
- Screenshot (single project, German variant): `010_de.png` - same base name with `_de` suffix
- Screenshots (multi-project): `{ProjectName}_010.png` for each sub-project (e.g., `OrderDashboard_010.png`); the German variant adds the `_de` suffix
- Downloadable files (`.pbmx`, `.pbfx`, `.py`, `.txt`) go in the same folder

**Bilingual screenshots:**

Provide screenshots in both languages whenever the dashboard contains visible text (labels, headers, KPI names). Each file references its own variant:

`*-en.md`:
```markdown
![dashboard overview](/assets/2026-03-03-14-30-00/010.png)
```

`*-de.md`:
```markdown
![Dashboard-Übersicht](/assets/2026-03-03-14-30-00/010_de.png)
```

**Fallback rule:** If a screenshot exists in only one language (because the dashboard shows numbers/icons only), reference the same file in both files. The alt text is always written in the file's own language.

### Code Blocks

**Method 1 - Liquid highlight tag:**
```liquid
{% highlight json %}
{ "key": "value" }
{% endhighlight %}
```

**Method 2 - Fenced code blocks (also fine):**
````markdown
```json
{ "key": "value" }
```
````

Supported language identifiers: `json`, `lua`, `sql`, `csharp`, `python`, `abap`, `xml`, `powershell`, `html`, `url`, `text`.

### Links

- Internal links use the **language-prefixed permalink**:
  ```markdown
  [Related Article](/en/related-article-title-slug/)
  ```
  In the German file, link to the matching `/de/...` URL.
- External links use full URLs:
  ```markdown
  [Shelly API Docs](https://shelly-api-docs.shelly.cloud/gen1/)
  ```

### Formatting

- **Bold** (`**text**`) for UI element names, field names, key terms
- `Inline code` (backticks) for values, variable names, file names, API endpoints
- Standard Markdown lists (unordered `- item` and ordered `1. item`)
- Standard Markdown tables when needed

### Videos

```liquid
{% include youtube.html id="VIDEO_ID_HERE" %}
```

Always placed at the very top of the article body, before the first text paragraph. No heading needed above the video. Each language file usually has its own `id` value pointing to the language-matched YouTube upload.

---

## 5. URL Structure

The blog uses language-prefixed pretty URLs:

```
/en/<slug>/      (English version of every post)
/de/<slug>/      (German version of every post)
```

The slug is the lower-cased, hyphenated form of the file's title portion. For example, `_posts/2026-03-03-My-Cool-Article-en.md` becomes `https://peakboard-guru.com/en/my-cool-article/`.

The non-prefixed root pages stay on `/` (EN) and `/de/` (DE):

| Page | English | German |
|------|---------|--------|
| Home | `/` | `/de/` |
| About | `/about/` | `/de/about/` |
| Impressum | `/impressum/` | `/de/impressum/` |
| Search | `/search/` | `/de/search/` |

Each post HTML includes `<link rel="alternate" hreflang>` tags pointing at the sibling language, plus a per-language `<link rel="canonical">`. The language toggle in the header is a real `<a href>` to `page.translation_url` (no JavaScript needed) so search engines can crawl both languages independently.

---

## 6. Writing Style

- **Language:** Bilingual - two separate files, one per language. Each file is written natively (not as a literal translation)
- **Voice:** The blog author is "Thilo" - write in first person plural ("we") or instructional second person ("you")
- **Tone:** Technical but approachable, sometimes playful/punny titles
- **Structure:** Problem → Setup → Step-by-step walkthrough → Result/Conclusion
- **Use-case focus:** Describe the real-world scenario, the problem, and how the dashboard helps. Do NOT describe Peakboard internals or technical implementation
- **Screenshots:** Heavy use of annotated screenshots showing each configuration step
- **Practical focus:** Every article typically includes a downloadable `.pbmx` sample project
- **Download button:** Do NOT add download links as text in the article body. The Guru download button image is rendered automatically in the right sidebar from the `downloads` front matter field
- **Cross-linking:** Reference related articles via the language-prefixed `/en/...` or `/de/...` URL
- **Punctuation:** Never use em dashes (—) or en dashes (–). Use only regular hyphens (-)

---

## 7. Complete Example Posts

### Single-Project Example

**`_posts/2026-03-03-Gym-Class-Schedule-Display-en.md`**:
```markdown
---
layout: post
title: Gym Class Schedule Display - Building a Fitness Studio Dashboard with Peakboard
date: 2026-03-03 00:00:00 +0000
tags: fitness
image: /assets/2026-03-03-14-30-00/title.png
bg_alternative: true
description: "Build a dynamic gym class schedule display with Peakboard."
downloads:
  - name: GymClassSchedule.pbmx
    url: /assets/2026-03-03-14-30-00/GymClassSchedule.pbmx
lang: en
permalink: /en/gym-class-schedule-display-building-a-fitness-studio-dashboard-with-peakboard/
translation_url: /de/gym-class-schedule-display-building-a-fitness-studio-dashboard-with-peakboard/
---
{% include youtube.html id="EN_VIDEO_ID" %}

Fitness studios often need a way to present their daily class schedule.
In this article, we build a complete dashboard with a course timetable,
KPI cards, and an occupancy bar chart.

## The layout concept

The dashboard runs at 1920x1080 with a dark design and neon cyan accents.

![image](/assets/2026-03-03-14-30-00/010.png)

## Result

The finished dashboard provides an at-a-glance overview of the schedule.
```

**`_posts/2026-03-03-Gym-Class-Schedule-Display-de.md`**:
```markdown
---
layout: post
title: Kursplan-Display - Ein Fitnessstudio-Dashboard mit Peakboard bauen
date: 2026-03-03 00:00:00 +0000
tags: fitness
image: /assets/2026-03-03-14-30-00/title.png
bg_alternative: true
description: "Ein dynamisches Fitnessstudio-Kursplan-Display mit Peakboard bauen."
downloads:
  - name: Kursplan.pbmx
    url: /assets/2026-03-03-14-30-00/GymClassSchedule.pbmx
lang: de
permalink: /de/gym-class-schedule-display-building-a-fitness-studio-dashboard-with-peakboard/
translation_url: /en/gym-class-schedule-display-building-a-fitness-studio-dashboard-with-peakboard/
---
{% include youtube.html id="DE_VIDEO_ID" %}

Fitnessstudios brauchen oft einen Weg, ihren Tageskursplan zu präsentieren.
In diesem Artikel bauen wir ein komplettes Dashboard mit einer Kurstabelle,
KPI-Karten und einem Auslastungsbalkendiagramm.

## Das Layout-Konzept

Das Dashboard läuft mit 1920x1080 in dunklem Design mit Neon-Cyan-Akzenten.

![image](/assets/2026-03-03-14-30-00/010_de.png)

## Ergebnis

Das fertige Dashboard liefert einen Auf-einen-Blick-Überblick über den Kursplan.
```

---

## 8. Checklist Before Publishing

For each post you need to ship **both** an `-en.md` and a `-de.md` file. Run this check against each side:

- [ ] File name follows `YYYY-MM-DD-Title-<lang>.md`
- [ ] `layout: post` is set
- [ ] `date:` matches the file name date and is identical in both files
- [ ] `tags:` uses valid tags from the list above (space-separated, English)
- [ ] `image:` points to an existing hero image
- [ ] `lang:` is set (`en` or `de`)
- [ ] `permalink:` is `/en/<slug>/` or `/de/<slug>/` with the same slug on both sides
- [ ] `translation_url:` points to the sibling file's permalink
- [ ] `description:` is set in this file's language
- [ ] `prompt:` is set in this file's language - mandatory for new posts
- [ ] Body is single-language markdown (no `<div data-lang>` wrappers)
- [ ] No `#` (H1) headers in the body
- [ ] First paragraph has no heading
- [ ] Internal links use `/en/<slug>/` (in the EN file) or `/de/<slug>/` (in the DE file)
- [ ] Images are in `/assets/YYYY-MM-DD-HH-MM-SS/` folder; alt text matches the file's language
- [ ] Article ends with a `## Result` or `## Conclusion` section
- [ ] Download link(s) in `downloads:` front matter only (not as text in the article body)
- [ ] `read_more_links` entries use names in this file's language
- [ ] Multi-project articles: all project files listed in `downloads:` with descriptive names; each project has its own screenshot
