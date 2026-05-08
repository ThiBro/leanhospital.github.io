# Blog Writing Guide for Claude

This guide documents all conventions for writing articles on the Jekyll blog **"Peakboard Guru"**. Follow these rules exactly when creating new posts.

**Language:** Every article is **bilingual (English + German)**. The original article is written in English; an equivalent German translation is added in the same file. Only the downloadable `.pbmx` project files stay single-language.

**Content focus:** Articles describe a **real-world use case** and the business value it delivers. Focus on the problem being solved, who benefits, and the outcome. Do NOT explain Peakboard internals, technical implementation details, or how the dashboard was built step by step.

---

## 1. File Naming

**Pattern:** `YYYY-MM-DD-Title-With-Hyphens.md`

- Date prefix must match the `date:` field in front matter
- Spaces in the title become hyphens
- Preserve title case
- Remove special characters (apostrophes, colons, etc.)
- Place in `_posts/`

**Example:**
```
_posts/2026-03-03-Fun-with-Shelly-Plug-S-Switching-Power-on-and-off.md
```

---

## 2. Front Matter

### Required Fields

```yaml
---
layout: post
title: Your Article Title Here
title_de: Dein Artikeltitel hier
date: 2026-03-03 00:00:00 +0000
tags: tag1 tag2
image: /assets/2026-03-03-14-30-00/title.png
---
```

| Field | Description |
|-------|-------------|
| `layout` | Always `post` |
| `title` | English title. Human-readable, often uses ` - ` as separator for subtitles |
| `title_de` | German translation of the title. Required for every post |
| `date` | Format: `YYYY-MM-DD HH:MM:SS +0000` |
| `tags` | **Space-separated** tag slugs (not a YAML list!). First tag = primary category. Tag slugs stay in English |
| `image` | Path to hero image. Pattern: `/assets/YYYY-MM-DD-HH-MM-SS/title.png` (or `title.jpg`). Match the actual file extension. The folder name matches the post's `date:` field with hyphens |

### Recommended Fields

Always include `bg_alternative`, `description`, and `description_de` for new posts:

```yaml
bg_alternative: true
description: "One or two sentences summarizing what this article covers."
description_de: "Ein oder zwei Sätze, die zusammenfassen, worum es in diesem Artikel geht."
downloads:
  - name: ProjectFile.pbmx
    url: /assets/2026-03-03-14-30-00/ProjectFile.pbmx
```

### Multi-Project Downloads

Some articles cover a multi-project system (e.g., an ordering dashboard + a kitchen display). In this case, list **all** project files in the `downloads` field with descriptive names:

```yaml
downloads:
  - name: OrderDashboard.pbmx
    url: /assets/2026-03-03-14-30-00/OrderDashboard.pbmx
  - name: KitchenDisplay.pbmx
    url: /assets/2026-03-03-14-30-00/KitchenDisplay.pbmx
```

Each download gets its own download button in the sidebar. Use meaningful names that describe what each project does.

### Optional Fields

```yaml
prompt: >
  The exact prompt that was given to the AI to generate the Peakboard
  project for this article. Use the YAML folded scalar (>) so single
  line breaks in the source become spaces and the text flows naturally
  in the rendered box. Use a blank line for an explicit paragraph break.
prompt_de: >
  Optionaler deutscher Prompt-Text, falls der Prompt selbst übersetzt
  wurde. Wenn nicht gesetzt, wird der englische Prompt für beide
  Sprachen angezeigt.
read_more_links:
  - name: Display Text
    name_de: Anzeigetext
    url: https://example.com
  - name: Related Article
    name_de: Verwandter Artikel
    url: /Related-Article-Title.html
downloads:
  - name: ProjectFile.pbmx
    url: /assets/2026-03-03-14-30-00/ProjectFile.pbmx
```

| Field | Description |
|-------|-------------|
| `bg_alternative` | `true` = light hero box style with a semi-transparent text box over the image. Always use for new posts |
| `description` | English summary shown below title and used for SEO meta tags. Always include for new posts |
| `description_de` | German translation of the description. Always include for new posts |
| `prompt` | **Required for every NEW post.** The exact AI prompt used to create the Peakboard project. Rendered in a visually distinct box at the bottom of the article body so readers know the project is AI-generated. Use the YAML folded scalar (`>`) syntax so single line breaks in the source become spaces and the text flows naturally - use a blank line for an explicit paragraph break. Older posts without this field continue to render without the box - the field is purely additive |
| `prompt_de` | Optional German translation of the prompt. If omitted, the English prompt is shown in both language modes |
| `downloads` | List of `{name, url}` rendered as Guru download button images at the top of the right sidebar. The `.pbmx` filename and the URL stay single-language - do not translate them |
| `read_more_links` | List of `{name, url}` shown in sidebar under "Related Links". Add `name_de` for the German label. The URL stays the same |

### Post Template (Single Project)

```yaml
---
layout: post
title: Article Title - With Subtitle
title_de: Artikeltitel - Mit Untertitel
date: 2026-03-03 00:00:00 +0000
tags: fitness
image: /assets/2026-03-03-14-30-00/title.png
bg_alternative: true
description: "Short summary of the article for SEO and hero display."
description_de: "Kurze Zusammenfassung des Artikels für SEO und Hero-Anzeige."
prompt: >
  Build a Peakboard dashboard that shows the daily class schedule for a
  fitness studio with KPI tiles, an occupancy bar chart, and a countdown
  to the next class.
downloads:
  - name: SampleProject.pbmx
    url: /assets/2026-03-03-14-30-00/SampleProject.pbmx
---
```

### Post Template (Multi-Project)

```yaml
---
layout: post
title: Restaurant Ordering System - Order Kiosk and Kitchen Display
title_de: Restaurant-Bestellsystem - Bestellkiosk und Küchenanzeige
date: 2026-03-03 00:00:00 +0000
tags: gastronomy
image: /assets/2026-03-03-14-30-00/title.jpg
bg_alternative: true
description: "A complete restaurant ordering system with a customer-facing kiosk and a kitchen display."
description_de: "Ein komplettes Restaurant-Bestellsystem mit einem Kundenkiosk und einer Küchenanzeige."
prompt: >
  Build a two-part Peakboard system for a restaurant: a customer-facing
  ordering kiosk on a touchscreen, and a kitchen display that shows
  incoming orders sorted by time.
downloads:
  - name: OrderKiosk.pbmx
    url: /assets/2026-03-03-14-30-00/OrderKiosk.pbmx
  - name: KitchenDisplay.pbmx
    url: /assets/2026-03-03-14-30-00/KitchenDisplay.pbmx
---
```

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

You can use multiple tags if applicable (e.g. `production logistics`). The first tag is used as the primary category shown on the article card. Add new tags as needed when no existing tag fits - keep them lowercase, use hyphens for multi-word tags.

---

## 4. Article Content Structure

### Bilingual Body Structure

The article body consists of two language blocks that wrap the actual content. Shared elements (video tags, YouTube embeds) live **outside** the language blocks at the top of the body so they appear in both languages.

```markdown
---
...front matter...
---
{% include youtube.html id="VIDEO_ID" %}

<div data-lang="en" markdown="1">

...full English content here, including all headings and images...

</div>

<div data-lang="de" markdown="1">

...complete German translation here, including all headings and images...

</div>
```

Important rules:

- The `markdown="1"` attribute is mandatory - kramdown only renders Markdown inside HTML blocks when this attribute is set
- Leave a blank line directly after the opening `<div ...>` and directly before the closing `</div>` so kramdown enters Markdown mode correctly
- Both language blocks must contain the **same set of images, screenshots, and structural headings** - just translated text
- Image paths, URLs, and `assets/.../*.pbmx` references stay identical in both blocks
- Tag links (`/category/...`) stay in English (tags are slugs)
- The language toggle in the header chooses which block is visible at runtime; both are present in the rendered HTML

### Opening Paragraph (No Header!)

Every language block starts with a direct intro paragraph **without** any heading. No `# Introduction`, no `---` separator. Just text immediately after the opening `<div ...>` line and its blank line.

```markdown
<div data-lang="en" markdown="1">

In this article, we will discuss how to...

</div>
```

### Headers

- **`##` (H2)** for main sections - the primary structural divisions
- **`###` (H3)** for subsections within a section
- **Never use `#` (H1)** in the body - the layout renders the title from front matter
- Common section patterns:
  - Setup / context section
  - Step-by-step procedural sections (one H2 per step)
  - `## Result` or `## Result and conclusion` or `## Conclusion` at the end

### Images

Store images in `/assets/YYYY-MM-DD-HH-MM-SS/` folder matching the post date.

**Naming conventions:**
- Hero image: `title.png` or `title.jpg` (match the actual file extension)
- Screenshot (single project): `010.png` - named `010.png`
- Screenshots (multi-project): `{ProjectName}_010.png` for each sub-project (e.g., `OrderDashboard_010.png`, `KitchenDisplay_010.png`)
- Downloadable files (`.pbmx`, `.pbfx`, `.py`, `.txt`) go in the same folder

**Markdown syntax (single project):**
```markdown
![screenshot](/assets/2026-03-03-14-30-00/010.png)
```

**Markdown syntax (multi-project):**
For multi-project articles, show each project's screenshot with a descriptive heading or label:
```markdown
## The Order Dashboard

![Order Dashboard](/assets/2026-03-03-14-30-00/OrderDashboard_010.png)

## The Kitchen Display

![Kitchen Display](/assets/2026-03-03-14-30-00/KitchenDisplay_010.png)
```

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

Supported language identifiers: `json`, `lua`, `sql`, `csharp`, `python`, `abap`, `xml`, `powershell`, `html`, `url` (for URL snippets), `text` (plain text)

### Links

- Internal links use the **title slug** with `.html` extension (no date in URL!):
  ```markdown
  [Related Article](/Related-Article-Title-Slug.html)
  ```
- External links use full URLs:
  ```markdown
  [Shelly API Docs](https://shelly-api-docs.shelly.cloud/gen1/)
  ```
- No category links (categories have been removed)

### Formatting

- **Bold** (`**text**`) for UI element names, field names, key terms
- `Inline code` (backticks) for values, variable names, file names, API endpoints
- Standard Markdown lists (unordered `- item` and ordered `1. item`)
- Standard Markdown tables when needed

### Videos

```liquid
{% include youtube.html id="VIDEO_ID_HERE" %}
```

Always placed at the very top of the article, before the first text paragraph. No heading needed above the video.

---

## 5. URL Structure

The blog uses flat permalinks: `/:title:output_ext`

A post file named `2026-03-03-My-Cool-Article.md` becomes the URL:
```
/My-Cool-Article.html
```

The URL preserves the exact filename casing (not lowercased). There is no date in the URL path.

---

## 6. Writing Style

- **Language:** Bilingual - English first, then a complete German translation in a separate `data-lang="de"` block
- **Voice:** The blog author is "Thilo" - write in first person plural ("we") or instructional second person ("you")
- **Tone:** Technical but approachable, sometimes playful/punny titles
- **Structure:** Problem → Setup → Step-by-step walkthrough → Result/Conclusion
- **Use-case focus:** Describe the real-world scenario, the problem, and how the dashboard helps. Do NOT describe Peakboard internals or technical implementation
- **Screenshots:** Heavy use of annotated screenshots showing each configuration step
- **Practical focus:** Every article typically includes a downloadable `.pbmx` sample project
- **Download button:** Do NOT add download links as text in the article body. The Guru download button image is rendered automatically in the right sidebar from the `downloads` front matter field
- **Cross-linking:** Reference related articles and categories using internal links
- **Punctuation:** Never use em dashes (---) or en dashes (--). Use only regular hyphens (-)

---

## 7. Complete Example Posts

### Single-Project Example

```markdown
---
layout: post
title: Gym Class Schedule Display - Building a Fitness Studio Dashboard with Peakboard
title_de: Kursplan-Display - Ein Fitnessstudio-Dashboard mit Peakboard bauen
date: 2026-03-03 00:00:00 +0000
tags: fitness
image: /assets/2026-03-03-14-30-00/title.png
bg_alternative: true
description: "Build a dynamic gym class schedule display with Peakboard."
description_de: "Ein dynamisches Fitnessstudio-Kursplan-Display mit Peakboard bauen."
downloads:
  - name: GymClassSchedule.pbmx
    url: /assets/2026-03-03-14-30-00/GymClassSchedule.pbmx
---
<video width="100%" controls><source src="{{ site.baseurl }}/assets/2026-03-03-14-30-00/video.mp4" type="video/mp4"></video>

<div data-lang="en" markdown="1">

Fitness studios often need a way to present their daily class schedule.
In this article, we build a complete dashboard with a course timetable,
KPI cards, and an occupancy bar chart.

## The layout concept

The dashboard runs at 1920x1080 with a dark design and neon cyan accents.

## Setting up the data

The application uses two Peakboard lists as its data backbone.

![image](/assets/2026-03-03-14-30-00/010.png)

## Result

The finished dashboard provides an at-a-glance overview of the schedule.

</div>

<div data-lang="de" markdown="1">

Fitnessstudios brauchen oft einen Weg, ihren Tageskursplan zu präsentieren.
In diesem Artikel bauen wir ein komplettes Dashboard mit einer Kurstabelle,
KPI-Karten und einem Auslastungsbalkendiagramm.

## Das Layout-Konzept

Das Dashboard läuft mit 1920x1080 in dunklem Design mit Neon-Cyan-Akzenten.

## Die Daten einrichten

Die Anwendung nutzt zwei Peakboard-Listen als Datengrundlage.

![image](/assets/2026-03-03-14-30-00/010.png)

## Ergebnis

Das fertige Dashboard liefert einen Auf-einen-Blick-Überblick über den Kursplan.

</div>
```

### Multi-Project Example

```markdown
---
layout: post
title: Restaurant Ordering System - Customer Kiosk and Kitchen Display
title_de: Restaurant-Bestellsystem - Kundenkiosk und Küchenanzeige
date: 2026-03-03 00:00:00 +0000
tags: gastronomy
image: /assets/2026-03-03-14-30-00/title.jpg
bg_alternative: true
description: "A two-part restaurant system with a self-service ordering kiosk and a real-time kitchen display."
description_de: "Ein zweiteiliges Restaurant-System mit einem Selbstbedienungskiosk und einer Echtzeit-Küchenanzeige."
downloads:
  - name: OrderKiosk.pbmx
    url: /assets/2026-03-03-14-30-00/OrderKiosk.pbmx
  - name: KitchenDisplay.pbmx
    url: /assets/2026-03-03-14-30-00/KitchenDisplay.pbmx
---
<video width="100%" controls><source src="{{ site.baseurl }}/assets/2026-03-03-14-30-00/video.mp4" type="video/mp4"></video>

<div data-lang="en" markdown="1">

Managing orders in a busy restaurant can be chaotic. This two-part system
connects a customer-facing ordering kiosk with a kitchen display that
shows incoming orders in real time.

## The Order Kiosk

Customers browse the menu and place orders directly on a touchscreen.

![Order Kiosk](/assets/2026-03-03-14-30-00/OrderKiosk_010.png)

## The Kitchen Display

As orders come in, they appear on the kitchen screen sorted by time.

![Kitchen Display](/assets/2026-03-03-14-30-00/KitchenDisplay_010.png)

## Result

The two dashboards work together to streamline the ordering process.

</div>

<div data-lang="de" markdown="1">

Bestellungen in einem belebten Restaurant zu verwalten kann chaotisch sein.
Dieses zweiteilige System verbindet einen Kundenkiosk mit einer Küchenanzeige,
die eingehende Bestellungen in Echtzeit zeigt.

## Der Bestellkiosk

Kunden stöbern im Menü und geben Bestellungen direkt am Touchscreen auf.

![Order Kiosk](/assets/2026-03-03-14-30-00/OrderKiosk_010.png)

## Die Küchenanzeige

Eingehende Bestellungen erscheinen auf dem Küchenbildschirm sortiert nach Zeit.

![Kitchen Display](/assets/2026-03-03-14-30-00/KitchenDisplay_010.png)

## Ergebnis

Die beiden Dashboards arbeiten zusammen und verschlanken den Bestellprozess.

</div>
```

---

## 8. Checklist Before Publishing

- [ ] File name matches pattern `YYYY-MM-DD-Title.md`
- [ ] `layout: post` is set
- [ ] `date:` matches the file name date
- [ ] `tags:` uses valid tags from the list above (space-separated)
- [ ] `image:` points to an existing hero image
- [ ] `title_de` and `description_de` are set with German translations
- [ ] `prompt:` is set (the AI prompt used to create the project) - mandatory for new posts
- [ ] Body has both `<div data-lang="en" markdown="1">` and `<div data-lang="de" markdown="1">` blocks
- [ ] Both blocks contain blank lines after the opening `<div ...>` and before the closing `</div>`
- [ ] Both blocks share the same headings, images, and structure
- [ ] No `#` (H1) headers in the body
- [ ] First paragraph in each block has no heading
- [ ] Internal links use `/Title-Slug.html` format (no date in URL)
- [ ] Images are in `/assets/YYYY-MM-DD-HH-MM-SS/` folder
- [ ] Article ends with a `## Result` or `## Conclusion` section (both languages)
- [ ] Download link(s) in `downloads:` front matter only (not as text in the article body)
- [ ] `read_more_links` entries have `name_de` for the German label
- [ ] For multi-project articles: all project files listed in `downloads:` with descriptive names
- [ ] For multi-project articles: each project has its own screenshot shown in the article body
