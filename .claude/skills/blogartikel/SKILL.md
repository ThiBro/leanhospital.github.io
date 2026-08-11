---
name: blogartikel
description: Lädt die Schreibanweisung für den Lean-Hospital-Blog als Arbeitsgrundlage. Nutze diesen Skill, wenn ein Blogartikel für lean-hospital.de geschrieben, überarbeitet oder SEO-/GEO-optimiert werden soll.
---

Alle Pfade in diesem Skill sind **relativ zum Repo-Root** (dem Ordner mit `_config.yml`) — lokal ist das
`C:\Source\leanhospital.github.io`, auf dem Server das jeweilige Checkout. Die Regelwerke sind versioniert,
der Skill funktioniert damit überall. **Lies sie vor dem Schreiben** und nutze sie als Grundlage:

1. `SCHREIBANWEISUNG.md` — **das verbindliche Regelwerk.** SEO (Meta Title ≤ 60 Zeichen, Meta Description
   ≤ 155, Slug, H1, Keyword-Platzierung), GEO (TL;DR, Definitionsblock, Chunking, FAQ, JSON-LD), Längen,
   CTA-System, Brand-/Peakboard-Regeln, Stilverbote, Selbstcheck.
2. `REDAKTIONSPLAN.md` — die **Artikeldaten** je Artikel: Fokuskeyword, Suchvolumen, H1, Slug, Metas,
   interne Pflichtlinks, CTA-Vorgabe, Content-Briefing mit Entities, FAQ-Vorschlägen und Abgrenzung.
   Enthält außerdem den Fortschritt (welche der 32 geplanten Artikel fertig sind) und die offenen Punkte.
3. `BLOG_WRITING_GUIDE.md` — repo-spezifische Ergänzungen: Front Matter, Dateinamen, Tags, Quellenformat.

**Bei Widerspruch gilt die SCHREIBANWEISUNG** — mit zwei Ausnahmen, in denen der Writing Guide gewinnt:
Zweisprachigkeit (DE + EN) und die Quellenpflicht (jede Zahl aus verifizierbarer Primärquelle, dazu die
nummerierte `## Quellen`-Liste am Artikelende). Artikeldaten kommen immer aus dem Redaktionsplan.

## Ausgabe: zwei Posts, gebaut und geprüft

Das Arbeitsergebnis ist **nicht** nur ein Markdown-Text, sondern **zwei gebaute Posts (DE + EN), die den
Selbstcheck der Schreibanweisung bestehen**. Vorgehen:

1. **Planzeile ziehen** — den Artikel im `REDAKTIONSPLAN.md` suchen und Fokuskeyword, H1, Metas,
   Pflichtlinks, CTA und Briefing übernehmen. Abweichungen von der Planzeile explizit begründen und im
   Redaktionsplan nachtragen.

2. **Deutsche Fassung schreiben** — `_posts/YYYY-MM-DD-Titel-de.md`, Rollenlänge einhalten
   (Spoke 1.200–1.800 / Hub 1.800–2.500 / Pillar 2.500–3.500 Wörter). Aufbau: TL;DR-Block direkt unter
   der H1 → erster H2 „Was ist [Fokuskeyword]?" mit 40–60-Wort-Definition → Hauptteil mit H2 alle
   150–300 Wörter → sichtbarer FAQ-Block → `## Quellen`.

3. **Englische Fassung strukturgleich nachziehen** — `-en.md`, gleiche H2s, gleiche Zahlen, gleiche FAQ,
   verknüpft über `permalink` / `translation_url`.

4. **Front Matter setzen** — die Felder, über die die Regeln technisch wirken:
   - `meta_title` — überschreibt `<title>` und OG-/Twitter-Titel **vollständig**, inklusive des sonst
     automatischen Suffixes `- Lean Hospital`. Nur so ist die 60-Zeichen-Regel exakt einzuhalten; die
     Pillar-Seite bleibt damit suffixlos.
   - `faq:` — Liste aus `{q, a}`. Rendert **kein** HTML, sondern speist ausschließlich das
     FAQPage-JSON-LD in `_includes/schema.html`. Muss **wortgleich** zum sichtbaren FAQ-Block sein.
   - `last_modified_at` — bei jeder Überarbeitung setzen, speist `dateModified`.
   - `downloads:` — Board-Vorlagen (`.pbmx`); so bleibt der Peakboard-Designer-CTA im Blog, ohne auf
     peakboard.com zu verlinken.
   - `image` / `image_header`, `tags`, `read_more_links` wie im Writing Guide beschrieben.

5. **Bauen und messen** — nicht behaupten, sondern prüfen. Im Repo-Root ausführen:

   ```
   bundle exec jekyll build --quiet
   ```

   Schlägt das fehl, weil die Ruby-Umgebung nicht steht (typisch auf frischen Servern), zuerst
   `bundle install` versuchen; ist auch das nicht möglich, die Messungen ersatzweise am Markdown-Quelltext
   vornehmen (Front-Matter-Werte direkt zählen) und **explizit vermerken**, dass ohne Build geprüft wurde.

   Danach an der gebauten Seite unter `_site/de/<slug>/index.html` verifizieren: `<title>`-Länge ≤ 60,
   `meta name="description"`-Länge ≤ 155, genau **eine** `<h1>`, `FAQPage` im Markup vorhanden, **kein**
   sichtbarer `href` auf `peakboard.com`. Wortzahl über den Body ohne Front Matter zählen.

6. **Selbstcheck der Schreibanweisung** — die Liste am Ende von `SCHREIBANWEISUNG.md` Zeile für Zeile mit
   ✓ / ✗ abarbeiten und ✗ begründen. Erst dann gilt der Artikel als fertig.

7. **Redaktionsplan nachziehen** — Status auf ✅, verwendete Quellen, Abweichungen und offene Punkte
   (fehlende Bilder, ungeprüfter Rechtsstand, fehlende Hub-Links) eintragen.

## Häufige Fallstricke (vorab vermeiden)

- **Erfundene Zahlen sind ein Abbruchkriterium.** Nicht gegen eine Primärquelle belegbare Zahlen fallen
  raus statt rein; unsichere als `[verify]` markieren. Gegenevidenz gehört in den Artikel, nicht weg.
- **Peakboard nie als Klinik-Software framen.** Bei Erstnennung der Standardsatz aus der Schreibanweisung:
  Low-Code-Plattform für Echtzeit-Dashboards **aus der Industrie** (Produktion und Logistik), deren Boards
  sich genauso für Stationen, Notaufnahmen und OP-Bereiche einsetzen lassen. Keine sichtbaren Links auf
  peakboard.com, kein Peakboard in Meta Title, Meta Description, H1 oder Slug.
- **CTA-Dosierung** — maximal 2 pro Artikel (1 inline + 1 am Ende). Planzeilen mit „kein Produkt-CTA"
  (Kultur-, Führungs-, Pflege- und Ausbildungsthemen) bekommen keinen, auch nicht nebenbei erwähnt.
- **Kein `x, nicht y`** — im Deutschen unnatürlich. Positiv formulieren, was etwas ist.
- **FAQ-Dopplung** — keine Frage, die im Fließtext schon als H2 beantwortet wird.
- **Zukunftsdatum** — Jekyll überspringt Posts mit `date` in der Zukunft (UTC) stillschweigend. Immer
  `00:00:00 +0000`. Taucht ein neuer Post nicht auf, zuerst das Datum prüfen.
- **`llms-full.txt`** — `scripts/update-llms-txt-lean-hospital.py` liest die **live** sitemap.xml, läuft
  also erst nach dem Deploy, nicht vor dem Commit.

Referenzartikel für den Aufbau: `_posts/2026-07-28-Lean-Hospital-…-de.md` / `-en.md`.
