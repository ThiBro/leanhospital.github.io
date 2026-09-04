# Redaktionsplan Lean Hospital Blog

Arbeitsdatei zum Abarbeiten der geplanten Artikel. Quelle: `redaktionsplan/Lean-Hospital-Blog_Keywordanalyse_Redaktionsplan_v2.xlsx`
(Keywordanalyse Sistrix, Markt DE, Stand 14.07.2026).

**Diese Datei ist von Jekyll ausgeschlossen** (`_config.yml` → `exclude`), erscheint also nicht auf der
Website. Sie ist seit 11.08.2026 versioniert, damit der Skill `/blogartikel` auf jedem Checkout darauf
zugreifen kann — und damit im öffentlichen GitHub-Repo lesbar.

> **Verbindlichkeit:** Ausführungsregeln (SEO, GEO, CTA, Brand, Stil, Länge) stehen seit 11.08.2026 in
> [SCHREIBANWEISUNG.md](SCHREIBANWEISUNG.md); repo-spezifische Ergänzungen (Zweisprachigkeit, Front Matter,
> Quellenformat) in [BLOG_WRITING_GUIDE.md](BLOG_WRITING_GUIDE.md). Dieser Plan liefert die Artikeldaten
> (Keyword, H1, Metas, Briefing). **Bei Widerspruch gilt die SCHREIBANWEISUNG**, außer bei der Quellenpflicht:
> Jede Zahl stammt aus einer verifizierbaren Primärquelle, Gegenevidenz gehört dazu.

## Status-Legende

| Zeichen | Bedeutung |
| --- | --- |
| ✅ | veröffentlicht (DE + EN) |
| 🟡 | in Arbeit |
| ⬜ | offen |
| ⚠️ | Überschneidung mit einem bestehenden Post — vor dem Schreiben klären |

## Abweichungen von der Excel-Vorlage (bewusst, gelten für alle Artikel)

1. **Zweisprachig.** Der Plan ist rein deutsch. Der Blog ist DE + EN — jeder Artikel wird als zwei Dateien
   angelegt (`-de.md` / `-en.md`), verlinkt über `translation_url`.
2. **Flache Permalinks.** Die Plan-Slugs sind hierarchisch (`daily-management/huddle-board`). Das Repo nutzt
   `/de/<slug>/` und `/en/<slug>/`. Der Plan-Slug ist unten jeweils als Referenz notiert; verwendet wird der
   letzte Pfadabschnitt. Die Hub-Zugehörigkeit wird über interne Links und `read_more_links` abgebildet.
3. ~~**Länge.** Plan: 2.500–3.500 W (Pillar). Writing Guide: 800–1.200 W.~~ **Aufgehoben am 11.08.2026:**
   Es gelten die Längen der SCHREIBANWEISUNG — Spoke 1.200–1.800 W, Hub 1.800–2.500 W, Pillar 2.500–3.500 W.
4. **Zahlen mit `[verify]`.** Nicht verifizierbare Zahlen fallen raus, nicht rein. Siehe offene Punkte unten.

---

## Fortschritt

**1 von 32 fertig.**

| # | Cluster | Rolle | Prio | Fokuskeyword | SV | Status |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Pillar | Pillar | P1 | lean hospital | 40 | ✅ |
| 2 | C1 Daily Management | Hub | P1 | daily management | 40 | ⬜ |
| 3 | C1 Daily Management | Spoke | P1 | huddle board | 100 | ⬜ |
| 4 | C1 Daily Management | Spoke | P2 | kennzahlen krankenhaus | 30 | ⬜ |
| 5 | C1 Daily Management | Spoke | P2 | leading lagging indicators | 70 | ⬜ |
| 6 | C1 Daily Management | Spoke | P2 | visual management | 100 | ⚠️ |
| 7 | C2 Kultur & Führung | Hub | P1 | change management krankenhaus | 10 | ⬜ |
| 8 | C2 Kultur & Führung | Spoke | P2 | lean leadership | 100 | ⬜ |
| 9 | C2 Kultur & Führung | Spoke | P2 | gemba walk | 2400 | ⬜ |
| 10 | C2 Kultur & Führung | Spoke | P2 | kontinuierlicher verbesserungsprozess | 150 | ⬜ |
| 11 | C2 Kultur & Führung | Spoke | P3 | kata coaching | 90 | ⬜ |
| 12 | C2 Kultur & Führung | Spoke | P3 | a3 report | 200 | ⬜ |
| 13 | C3 Patient Flow | Hub | P1 | patientensteuerung | 70 | ⬜ |
| 14 | C3 Patient Flow | Spoke | P1 | entlassmanagement | 1300 | ⬜ |
| 15 | C3 Patient Flow | Spoke | P2 | bettenmanagement | 90 | ⬜ |
| 16 | C3 Patient Flow | Spoke | P2 | verweildauer krankenhaus | 60 | ⬜ |
| 17 | C3 Patient Flow | Spoke | P2 | op planung | 90 | ⬜ |
| 18 | C3 Patient Flow | Spoke | P2 | 7 arten der verschwendung | 250 | ⬜ |
| 19 | C3 Patient Flow | Spoke | P3 | wertstromanalyse krankenhaus | 10 | ⬜ |
| 20 | C4 Lean in der Pflege | Hub | P1 | lean management pflege | 10 | ⬜ |
| 21 | C4 Lean in der Pflege | Spoke | P1 | pdca zyklus pflege | 250 | ⬜ |
| 22 | C4 Lean in der Pflege | Spoke | P2 | 5s methode krankenhaus | 0 | ⬜ |
| 23 | C4 Lean in der Pflege | Spoke | P3 | schichtübergabe pflege | 10 | ⚠️ |
| 24 | C5 Digitalisierung | Hub | P1 | digitalisierung krankenhaus | 150 | ⬜ |
| 25 | C5 Digitalisierung | Spoke | P2 | krankenhauszukunftsgesetz | 550 | ⬜ |
| 26 | C5 Digitalisierung | Spoke | P2 | digitalisierung pflege | 100 | ⬜ |
| 27 | C5 Digitalisierung | Spoke | P2 | stations-dashboard | 0 | ⬜ |
| 28 | C6 Strategie | Hub | P2 | hoshin kanri | 1100 | ⬜ |
| 29 | C6 Strategie | Spoke | P3 | strategieumsetzung | 80 | ⬜ |
| 30 | C6 Strategie | Spoke | P3 | klinisches risikomanagement | 20 | ⬜ |
| 31 | C7 International | Spoke | P3 | magnetkrankenhaus | 100 | ⬜ |
| 32 | C7 International | Spoke | P3 | lean healthcare usa | 0 | ⚠️ |

**Empfohlene Reihenfolge:** alle P1 zuerst (#1 ✅, #2, #3, #7, #13, #14, #20, #24), dann P2, dann P3.
Innerhalb P1 zuerst #14 Entlassmanagement (1.300 SV, größte Einzelchance) und #3 Huddle Board.

---

## Bestehende Posts

### Bereits veröffentlicht, im Plan vorgesehen

| Artikel | Permalink DE | Plan-Bezug |
| --- | --- | --- |
| Lean Hospital (Pillar) | `/de/lean-hospital/` | #1 ✅ |

### Bereits veröffentlicht, überschneidet sich mit einem Planeintrag ⚠️

| Bestehender Post | Permalink DE | Kollidiert mit | Vorschlag |
| --- | --- | --- | --- |
| Die Arbeit sichtbar machen – Visuelles Management | `/de/die-arbeit-sichtbar-machen-visuelles-management-im-krankenhaus/` | #6 visual management | Bestandspost auf das Fokuskeyword optimieren statt neu schreiben |
| Die Übergabe ist die Bruchstelle (I-PASS/SBAR) | `/de/die-uebergabe-ist-die-bruchstelle-wie-i-pass-und-sbar-sie-reparieren/` | #23 schichtübergabe pflege | Bestandspost erweitern; kein zweiter Artikel (Kannibalisierung) |
| Was Virginia Mason und ThedaCare bewiesen haben | `/de/was-virginia-mason-und-thedacare-ueber-lean-im-krankenhaus-bewiesen-haben/` | #32 lean healthcare usa | weitgehend deckungsgleich — #32 streichen oder auf ThedaCare/IHI verengen |

### Bereits veröffentlicht, nicht im Plan

- ✅ **Berichtspflichten im Krankenhaus** — `/de/berichtspflichten-krankenhaus/` · EN: `/en/hospital-reporting-obligations/`
  (14.08.2026, Auftragsartikel außerhalb des Plans, nach SCHREIBANWEISUNG geschrieben)
  - **Fokuskeyword:** berichtspflichten krankenhaus · **Sekundär:** dokumentationsaufwand krankenhaus,
    qualitätsbericht krankenhaus, § 21 KHEntgG, bundes-klinik-atlas, pflegepersonalbemessung
  - **Rolle:** Spoke (nach der Ergänzung vom 14.08.2026 rund 1.770 W DE / 1.870 W EN; EN liegt damit knapp
    über der Spoke-Spanne — die zusätzlichen Sätze waren vom Auftraggeber verlangt und werden nicht
    zurückgekürzt). **Interne Links:** → Pillar #1, → Visuelles Management
  - **Abgrenzung zu #4 (kennzahlen krankenhaus):** dieser Artikel behandelt die *Meldepflichten*, die den
    Kennzahlenaufwand erzeugen (Gesetze, Fristen, Adressaten). Der KPI-**Katalog** mit Formeln und Zielwerten
    bleibt #4. Beim Schreiben von #4 hierher verlinken und Doppelungen zum Gesetzesteil vermeiden.
  - **Abweichung von der Brand-Regel (bewusst, vom Auftraggeber vorgegeben):** Der Artikel enthält **einen**
    sichtbaren Link auf `templates.peakboard.com` (fertige Klinik-Vorlage „Digitales Huddle Board für das Daily
    Management im Klinikum"). Der Auftrag verlangte ausdrücklich, dass Leser die Vorlage aus dem Artikel
    erreichen. Sonst kein sichtbarer Peakboard-Link; das Herkunfts-Framing der Schreibanweisung steht wörtlich
    im Text. Sauberer wäre langfristig, die `.pbmx` wie bei `ward-status-board.pbmx` über `downloads:` im Blog
    selbst anzubieten.
  - **Nachtrag 14.08.2026 (Auftrag des Auftraggebers):** Die Vorlage liegt jetzt zusätzlich im Blog selbst —
    `assets/pbmx/team-huddle-board-klinikum.pbmx` über `downloads:` und als Inline-Link, dazu das Board-Bild
    und ein sichtbarer Link auf die Live-Demo
    `templates.peakboard.rocks/Team-Huddle-Board-Klinikum/index`. Beides stammt von der Vorlagenseite. Damit ist
    der oben genannte „sauberere" Weg umgesetzt; der eine Link auf `templates.peakboard.com` bleibt daneben stehen.
  - **Nachtrag 14.08.2026 (Reklamation des Auftraggebers):** Das Hero-Bild war eine generierte Illustration
    (`reporting-obligations.png`). Verlangt war der echte Screenshot der Anwendung. Hero ist jetzt das
    Board-Bild der Vorlagenseite (`assets/img/posts/huddle-board-klinikum.png`, 2880×1620), die generierte
    Illustration ist gelöscht; im Fließtext steht statt des identischen Vollbilds der Kennzahlen-Ausschnitt
    `huddle-board-klinikum-kennzahlen.webp`. Regel dazu in SCHREIBANWEISUNG und IMAGE_PROMPT_GUIDE nachgezogen.
  - **Nachtrag 14.08.2026 (zweite Reklamation des Auftraggebers):** Der Screenshot war angeschnitten — der
    Hero schnitt per `object-cover` + `max-height: 70vh` rund 29 % der Bildhöhe weg, und im Fließtext stand
    ohnehin nur ein Ausschnitt. Jetzt gilt: Screenshots werden immer vollständig gezeigt. Neuer Schalter
    `image_full: true` in beiden Sprachdateien; `_layouts/post.html` rendert das Hero-Bild damit ungeschnitten
    und setzt Titelkarte und Teaser darunter statt darüber. Der Ausschnitt
    `huddle-board-klinikum-kennzahlen.webp` ist gelöscht, inline steht das vollständige Board.
  - **Offen:** Ein zweites Inline-Bild fehlt (`berichtspflichten-krankenhaus-fristen.webp` — Zeitstrahl
    31.03. / Quartalsmeldung / monatlicher Atlas). Hero-Bild und das
    Stationsboard-Motiv sind gesetzt. Autorenbox/CTA-Bausteine wie bei #1.
- ✅ **Clinical Operations im Krankenhaus** — `/de/clinical-operations-krankenhaus/` · EN: `/en/clinical-operations-hospital/`
  (04.09.2026, Auftragsartikel außerhalb des Plans, nach SCHREIBANWEISUNG geschrieben)
  - **Fokuskeyword:** clinical operations krankenhaus · **Sekundär:** operative Steuerung Krankenhaus,
    Reifegrad Krankenhaus, Transformations-Perspektive, Patientenfluss, Clinical Operations Framework
  - **Rolle:** Spoke (1.619 W DE / 1.783 W EN, gemessen am Markdown-Body). **Plan-Slug:**
    `daily-management/clinical-operations-krankenhaus`. **Interne Links:** → Pillar #1,
    → Visuelles Management, → Berichtspflichten
  - **Anlass:** Der erste Clinical Operations Ergebnisreport von Ralf Volkmer (LeanBase, 29.08.2026,
    1.260 Einzelantworten aus D/A/CH). Alle sieben Themenfelder liegen im IST unter 3,0 Punkten; bei
    „Daten & KI nutzen" (2,33 → 2,12) und „Clinical Operations steuern" (2,95 → 2,90) liegt die
    Transformations-Perspektive sogar unter dem IST-Wert. Alle Zahlen des Artikels stammen aus dieser
    Quelle und wurden gegen den Originalartikel geprüft.
  - **Abgrenzung zu #4 (kennzahlen krankenhaus):** Hier steht die *operative Steuerungsfähigkeit* als
    Reifegradthema im Mittelpunkt (Report, IST vs. Transformations-Perspektive, Tagessteuerung). Der
    KPI-**Katalog** mit Formeln und Zielwerten bleibt #4; die Kennzahlenliste hier ist bewusst auf fünf
    Positionen ohne Formeln begrenzt.
  - **Abgrenzung zu #24 (digitalisierung krankenhaus) und #27 (stations-dashboard):** #24 bleibt die
    Digitalstrategie-Ebene (KHZG, Systeme, Förderung), #27 das *Stations*-Dashboard. Dieser Artikel
    liegt auf der Haus-Ebene: bereichsübergreifende Tagessteuerung über Notaufnahme, Station, OP und
    Diagnostik hinweg.
  - **Board-Vorlage:** `assets/pbmx/clinical-operations-cockpit.pbmx` (eigens für den Artikel gebaut,
    zwei Bildschirmseiten, gegen den Designer kompiliert und in der Peakboard Runtime abgespielt) über
    `downloads:` und als Inline-Link. Kein sichtbarer Link auf `peakboard.com` oder
    `templates.peakboard.com` — die Brand-Regel gilt hier unverändert.
  - **Bilder:** Alle drei sind echte Screenshots der gebauten Anwendung, deshalb `image_full: true` +
    `bg_alternative: true` und `ai_disclosure.image: screenshot`. Hero:
    `assets/img/posts/clinical-operations-krankenhaus.png` (Bildschirmseite „Reifegrad"). Inline:
    `clinical-operations-tagessteuerung.webp` (Bildschirmseite „Tagessteuerung"),
    `clinical-operations-designer.webp` (Projekt im Peakboard Designer). Kein generiertes Motiv.
  - **Offen:** Beim Schreiben von #4, #24 und #27 hierher verlinken.
- ✅ **Clinical Operations Framework** — `/de/clinical-operations-framework/` · EN: `/en/clinical-operations-framework/`
  (04.09.2026, Auftragsartikel außerhalb des Plans, nach SCHREIBANWEISUNG geschrieben)
  - **Fokuskeyword:** clinical operations framework · **Sekundär:** Managementsystem Krankenhaus,
    Zielkonflikte Krankenhaus, Bereichsoptimum, Toyota Kata Krankenhaus, integratives Managementsystem
  - **Rolle:** Spoke (1.679 W DE / 1.799 W EN, gemessen am Markdown-Body). **Interne Links:** → Pillar #1,
    → Clinical Operations im Krankenhaus, → Visuelles Management
  - **Anlass:** Die Rezension "Braucht das Krankenhaus ein neues Framework?" von Götz Müller (LeanBase,
    Channel LeanHospital, 31.08.2026) zum Clinical Operations Framework von Ralf Volkmer, dazu die
    Podcast-Folge Kaizen 2 go 394. Der Artikel antwortet begleitend darauf und zeigt, wo Digitalisierung
    zu den drei offenen Punkten der Rezension beiträgt. Der Artikel enthält **keine** erfundenen
    Statistiken; die einzige Zahlenquelle ist Destatis (17,5 Mio. Behandlungsfälle 2024, Verweildauer
    7,1 Tage, Pressemitteilung Nr. 398 vom 06.11.2025).
  - **Abgrenzung zum Nachbarartikel „Clinical Operations im Krankenhaus" (clinical operations krankenhaus):**
    Dort steht der **Ergebnisreport** mit seinen Reifegradzahlen und die Tagessteuerung im Mittelpunkt.
    Hier steht das **Framework selbst** im Mittelpunkt — die drei Dimensionen, die Frage nach dem einen
    Managementsystem, Bereichsoptimum gegen Gesamtsystem, Zielkonflikte und das Lernexperiment. Zahlen des
    Ergebnisreports werden hier bewusst nicht wiederholt.
  - **Abgrenzung zu #4 (kennzahlen krankenhaus) und #17 (op planung):** Die Kennzahlenliste hier ist auf
    fünf Systemgrößen ohne Formeln begrenzt; der KPI-Katalog bleibt #4. Das OP-Beispiel dient der
    Systemsicht, die Planungsmethodik bleibt #17.
  - **Board-Vorlage:** `assets/pbmx/clinical-operations-framework-cockpit.pbmx` (eigens für den Artikel
    gebaut, drei Bildschirmseiten — Bereichsoptimum, Zielkonflikte, Lernexperiment; gegen den Designer
    kompiliert und in der Peakboard Runtime abgespielt) über `downloads:` und als Inline-Link. Kein
    sichtbarer Link auf `peakboard.com`.
  - **Bilder:** Vier echte Screenshots der gebauten Anwendung, deshalb `image_full: true` +
    `bg_alternative: true` und `ai_disclosure.image: screenshot`. Hero:
    `assets/img/posts/clinical-operations-framework.png` (Bildschirmseite „Bereichsoptimum"). Inline:
    `clinical-operations-framework-zielkonflikte.webp`, `clinical-operations-framework-lernexperiment.webp`,
    `clinical-operations-framework-designer.webp`. Kein generiertes Motiv.
  - **Sämtliche Board-Werte sind erfundene Beispieldaten** und im Text beider Sprachen als solche benannt.
  - **Offen:** Beim Schreiben von #4, #17 und #27 hierher verlinken.
- ✅ **Silodenken im Krankenhaus** — `/de/silodenken-krankenhaus/` · EN: `/en/silo-thinking-hospital/`
  (04.09.2026, Auftragsartikel außerhalb des Plans, nach SCHREIBANWEISUNG geschrieben)
  - **Fokuskeyword:** silodenken krankenhaus · **Sekundär:** Methodenparadox, Schnittstellen Krankenhaus,
    Abteilungssilos, Entlassmanagement, Bettenauslastung, bereichsübergreifende Zusammenarbeit
  - **Rolle:** Spoke (1.636 W DE / 1.797 W EN, gemessen am Markdown-Body). **Interne Links:** → Pillar #1,
    → Clinical Operations Framework, → Visuelles Management
  - **Anlass:** Der Beitrag "Das Methodenparadox der Krankenhäuser" von Ralf Volkmer (LeanBase,
    Channel LeanHospital, 24.08.2026). Der Artikel antwortet darauf und nimmt die vier Beispiele der
    Montagmorgen-Szene (Notaufnahme, Entlassung, OP-Plan, Personalausfall) als Aufbau. Der Beitrag
    veröffentlicht **keine** Zahlen; die einzige Zahlenquelle ist Destatis (Bettenauslastung 72,0 %
    2024, 472 900 Betten in 1 841 Krankenhäusern, Pressemitteilung Nr. 398 vom 06.11.2025).
  - **Abgrenzung zu den beiden Nachbarartikeln vom selben Tag:** "Clinical Operations im Krankenhaus"
    (clinical operations krankenhaus) gehört der **Ergebnisreport** mit seinen Reifegradzahlen,
    "Clinical Operations Framework" (clinical operations framework) gehören die **drei Dimensionen**,
    Zielkonflikte und das Lernexperiment. Hier steht die **Schnittstelle im Tagesbetrieb** im
    Mittelpunkt: Warum eine Aufnahme wartet, woran eine Entlassung hängt, wo eine OP-Verspätung
    entsteht. Reifegradzahlen und Framework-Dimensionen werden hier bewusst nicht wiederholt.
  - **Abgrenzung zu #17 (op planung) und #27 (stations-dashboard):** Das OP-Beispiel dient der
    Schnittstellensicht, die Planungsmethodik bleibt #17; das Board liegt auf der Haus-Ebene und
    nicht auf der Stations-Ebene von #27.
  - **Board-Vorlage:** `assets/pbmx/schnittstellen-board.pbmx` (eigens für den Artikel gebaut, drei
    Bildschirmseiten — Morgenlage, Entlassung, OP und Dienste; gegen den Designer kompiliert und in
    der Peakboard Runtime abgespielt) über `downloads:` und als Inline-Link. Kein sichtbarer Link auf
    `peakboard.com`.
  - **Bilder:** Vier echte Screenshots der gebauten Anwendung, deshalb `image_full: true` +
    `bg_alternative: true` und `ai_disclosure.image: screenshot`. Hero:
    `assets/img/posts/silodenken-krankenhaus.png` (Bildschirmseite „Morgenlage"). Inline:
    `silodenken-krankenhaus-entlassung.webp`, `silodenken-krankenhaus-op-dienste.webp`,
    `silodenken-krankenhaus-designer.webp`. Kein generiertes Motiv.
  - **Sämtliche Board-Werte sind erfundene Beispieldaten** und im Text beider Sprachen als solche benannt.
  - **Offen:** Beim Schreiben von #17 und #27 hierher verlinken.
- ✅ **Standardarbeit in der Pflege** — `/de/standardarbeit-pflege/` · EN: `/en/standard-work-nursing/`
  (04.09.2026, Auftragsartikel außerhalb des Plans, nach SCHREIBANWEISUNG geschrieben)
  - **Fokuskeyword:** standardarbeit pflege · **Sekundär:** Stationsorganisation, Suchzeiten Pflege,
    Tagesstandard Station, Fixpunkte Schicht, Schwester Philin, pflegefremde Tätigkeiten
  - **Rolle:** Spoke (1.734 W DE / 1.795 W EN, gemessen am Markdown-Body). **Interne Links:** → Pillar #1,
    → Silodenken im Krankenhaus, → Visuelles Management
  - **Anlass:** Der Beitrag „Je komplexer die Medizin, desto einfacher muss die Organisation sein" der
    LKB Redaktion (LeanBase, Channel LeanHospital, 17.08.2026). Er fasst die Folge „Die schöne Welt der
    Schwester Philin" aus Jörg Gottschalks Podcast „Krankenhausführung neu denken" zusammen: der Dienst
    einer Pflegekraft auf einer Station, deren Abläufe tragen. Weder Beitrag noch Podcastfolge
    veröffentlichen Zahlen; die beiden Zahlenquellen des Artikels sind Destatis (553 400 Beschäftigte im
    Pflegedienst 2024, 44,6 % des nichtärztlichen Personals, Pressemitteilung Nr. 398 vom 06.11.2025)
    und das Deutsche Krankenhausinstitut (rund 2:10 Stunden pflegefremde/patientenferne Tätigkeiten je
    Pflegekraft und Arbeitstag, gut 28 % der Arbeitszeit — **Erhebungsjahr 2002, im Text ausdrücklich
    genannt**).
  - **Abgrenzung zu den drei Nachbarartikeln vom selben Tag:** „Clinical Operations im Krankenhaus"
    gehört der Ergebnisreport, „Clinical Operations Framework" gehören die drei Dimensionen,
    „Silodenken im Krankenhaus" gehört die Schnittstelle zwischen Bereichen. Hier steht die **Station
    selbst** im Mittelpunkt: der Tagesstandard einer Schicht, Material und sein Ort, Zuständigkeit und
    die bewusst entschiedene Abweichung. Reifegradzahlen, Framework-Dimensionen und die
    Bettenauslastung werden hier bewusst nicht wiederholt.
  - **Abgrenzung zu #22 (5s methode krankenhaus) und #27 (stations-dashboard):** #22 bleibt die
    **Methode** mit ihren fünf S und der Einführungsanleitung; hier steht die Ordnung nur als eine von
    drei Bildschirmseiten und ohne Methodenschritte. #27 bleibt das **Dashboard als Kategorie**
    (Datenquellen, KIS/SAP, Anforderungen an die Technik) mit Peakboard-Haupt-CTA; hier ist das Board
    ein Beispiel für Standardarbeit und der Designer-Download der einzige Inline-CTA.
  - **Abgrenzung zu #20 (lean management pflege) und #23 (schichtübergabe pflege):** #20 bleibt der
    Hub über Lean in der Pflege insgesamt; die Übergabe wird hier nur als einer von acht Fixpunkten
    genannt, SBAR und I-PASS bleiben beim Bestandspost zur Übergabe.
  - **Board-Vorlage:** `assets/pbmx/stationsstandard-board.pbmx` (eigens für den Artikel gebaut, drei
    Bildschirmseiten — Tagesstandard, Material und Ort, Zuständigkeit und Abweichung; gegen den
    Designer kompiliert, in der Peakboard Runtime abgespielt und im Designer gegengeprüft) über
    `downloads:` und als Inline-Link. Kein sichtbarer Link auf `peakboard.com`.
  - **Bilder:** Vier echte Screenshots der gebauten Anwendung, deshalb `image_full: true` +
    `bg_alternative: true` und `ai_disclosure.image: screenshot`. Hero:
    `assets/img/posts/standardarbeit-pflege.png` (Bildschirmseite „Tagesstandard"). Inline:
    `standardarbeit-pflege-material.webp`, `standardarbeit-pflege-designer.webp`,
    `standardarbeit-pflege-zustaendigkeit.webp`. Kein generiertes Motiv.
  - **Sämtliche Board-Werte sind erfundene Beispieldaten** und im Text beider Sprachen als solche benannt.
  - **Offen:** Beim Schreiben von #20, #22 und #27 hierher verlinken.
- Warum Überfüllung der Notaufnahme ein Sicherheitsproblem ist — `/de/warum-ueberfuellung-der-notaufnahme-ein-sicherheitsproblem-ist/`
- Die OP-Sicherheitscheckliste: Was die Evidenz wirklich zeigt — `/de/die-op-sicherheitscheckliste-was-die-evidenz-wirklich-zeigt/`
- Die Fünf-Punkt-Checkliste, die Infektionen auf null brachte — `/de/die-fuenf-punkt-checkliste-die-infektionen-auf-null-brachte/`

---

## Offene Punkte

- [ ] **Nicht verifizierte Zahlen aus dem Plan.** Gottschalk („bis zu 1/3 der Arbeitszeit ist Verschwendung") und
      Andreux/Wacogne („bis zu 70 % der Durchlaufzeit nicht wertschöpfend") ließen sich nicht gegen eine
      Primärquelle belegen und wurden in #1 weggelassen. Beide werden im Plan mehrfach als quotable Zahlen
      eingeplant (#13, #18). Belege beschaffen oder Zahlen dauerhaft streichen.
- [ ] **Rechts-/Standprüfung vor Veröffentlichung** bei #14 (§ 39 SGB V, Rahmenvertrag), #25 (KHZG-Förderstand,
      Sanktionen § 5 Abs. 3h KHEntgG), #30 (§ 136a SGB V), #21 (QM-Pflicht Pflege).
- [ ] **Interne Verlinkung nachziehen.** #1 enthält die 7 Handlungsfelder als Tabelle noch **ohne** Links, weil
      die Hubs fehlen. Nach jedem neuen Hub die Pillar aktualisieren.
- [ ] **llms.txt.** `scripts/update-llms-txt-lean-hospital.py` liest die **live** sitemap.xml — also erst nach
      dem Deploy ausführen, nicht vor dem Commit.
- [ ] **Hero-Bilder.** #1 hat inzwischen `lean-hospital.png`. Die Schreibanweisung verlangt 2–4 Bilder je
      Artikel mit sprechendem Dateinamen (`fokuskeyword-kontext.webp`) und Alt-Text — für #1 fehlen die
      Inline-Bilder noch (Kandidaten: Wertstrom Aufnahme→Entlassung, Stationsboard mit Huddle).
- [ ] **Peakboard-Designer-Download im Blog.** Die Schreibanweisung verbietet sichtbare Links auf
      peakboard.com und sieht den Designer-Download direkt im Blog vor. Aktuell liegt nur die
      `.pbmx`-Boardvorlage unter `/assets/pbmx/` — der Inline-CTA in #1 verweist deshalb auf den
      Visual-Management-Post. Eigene Download-Seite für den Designer klären.
- [ ] **Downloads.** Der Plan sieht Downloads als CTA vor (#3 Board-Vorlage, #12 A3-Vorlage, #14 Checkliste,
      #22 5S-Audit). Format über das `downloads:`-Front-Matter-Feld, siehe Visual-Management-Post.

---

# Artikeldetails

Je Artikel: Fokuskeyword, Sekundärkeywords, H1, Meta-Daten, interne Pflichtlinks, CTA und Content-Briefing
aus dem Redaktionsplan. „Plan-Slug" ist der hierarchische Slug der Vorlage; im Repo wird der letzte
Pfadabschnitt als flacher Permalink verwendet.

---

## ✅ 1. Lean Hospital *(Pillar, P1)*

- **Status:** veröffentlicht 28.07.2026 — `/de/lean-hospital/` · `/en/lean-hospital/`
- **Dateien:** `_posts/2026-07-28-Lean-Hospital-Was-Lean-Management-im-Krankenhaus-wirklich-leistet-de.md` (+ `-en`)
- **Fokuskeyword:** lean hospital (40 SV, Know)
- **Sekundär:** lean management krankenhaus (20), lean healthcare (10), lean krankenhaus, lean hospital management

**Überarbeitet am 11.08.2026 nach SCHREIBANWEISUNG.md** (DE + EN): TL;DR-Block unter der H1,
Definitions-H2 „Was ist ein Lean Hospital?" mit 55-Wort-Definition, Womack/Jones-Prinzipien, 7 Arten der
Verschwendung als Tabelle, 5-Schritte-Einstieg, Scheiter-Muster, sichtbarer FAQ-Block (5 Fragen) plus
wortgleiches `faq:`-Front-Matter für das FAQPage-Schema, `meta_title` (42 Zeichen, ohne Suffix — Pillar-Ausnahme),
Meta Description 142 Zeichen, inline-CTA Peakboard Designer, Peakboard mit Industrie-Herkunftsframing.
Länge jetzt 2.659 W (DE) / 2.881 W (EN).

**Abweichungen zur Vorlage:** Titel geändert („Was Lean Management im Krankenhaus wirklich leistet – und was
nicht" statt „Wie Lean Management Krankenhäuser aus dem Chaos führt"), weil der Plan-Titel mehr verspricht als
die Evidenz hergibt. Hub-Links fehlen noch (Artikel existieren nicht) — stattdessen auf die vier bestehenden
Posts verlinkt. Bildvorschläge aus der Schreibanweisung (2–4 je Artikel) noch offen, siehe unten.

**Verwendete Quellen:** Womack/Jones *Lean Thinking* 1996 · Wang et al., IJHPM 2025 (60 Studien) ·
Moraros/Lemstra/Nwankwo, IJQHC 2016 (Gegenevidenz: keine Wirkung auf 30-Tage-Mortalität, negative Assoziation
mit Mitarbeiterzufriedenheit und Kosten) · Andersen/Røvik/Ingebrigtsen, BMJ Open 2014 · DKI Krankenhaus-Barometer
2025 · DKG Fachkräfte-Pressemitteilung 03/2026.

---

## ⬜ 2. Daily Management *(C1, Hub, P1)*

- **Fokuskeyword:** daily management (40 SV, Know 100)
- **Sekundär:** daily management system, tagessteuerung klinik, shopfloor management krankenhaus (10)
- **H1:** Daily Management im Krankenhaus: Kennzahlenbasierte Steuerung, die auf Station ankommt
- **Plan-Slug:** `daily-management`
- **Meta Title:** Daily Management im Krankenhaus | Lean Hospital
- **Meta Description:** Daily Management System im Krankenhaus einführen: Kennzahlen-Kaskade, tägliche Huddles und Boards – mit Einführungs-Roadmap in 5 Schritten.
- **Interne Links:** → Pillar; → Huddle Board, Kennzahlen, Leading/Lagging, Visual Management
- **CTA:** Peakboard Designer kostenlos laden inline nach der Board-/Kennzahlen-Sektion → Kontaktformular am Ende

**Briefing:** Hub-Artikel. Definition Daily Management (System aus täglichen Kurzbesprechungen + Kennzahlen +
Eskalationswegen) → die 4 Bausteine (Board, Kennzahlen, Routine, Eskalation) je als eigener Chunk mit Link auf
Spoke → Kennzahlen-Kaskade Vorstand→Klinik→Station → Einführungs-Roadmap in 5 Schritten → Stolpersteine
(manuelle Erhebung, fehlende Qualifikation). **Entities:** Daily Management System (DMS), Dr. Axel Mechtler,
Teamboards, KIS-/SAP-Anbindung. **FAQ:** Was ist Daily Management im Krankenhaus? / Wie läuft ein Daily Huddle
ab? / Welche Kennzahlen gehören auf ein Stationsboard? **Abgrenzung:** Board-Gestaltung → #3, KPI-Auswahl → #4.

---

## ⬜ 3. Huddle Board *(C1, Spoke, P1)*

- **Fokuskeyword:** huddle board (100 SV, Know+Do 90/50)
- **Sekundär:** teamboard (400, **nur sekundär** – SERP software-dominiert), huddle meeting (90), teamboard krankenhaus, stationsboard
- **H1:** Huddle Board: So funktioniert das Team-Board für Station und Klinik
- **Plan-Slug:** `daily-management/huddle-board`
- **Meta Title:** Huddle Board: Aufbau, Ablauf & Vorlage | Lean Hospital
- **Meta Description:** Was gehört auf ein Huddle Board? Aufbau, 15-Minuten-Ablauf und Vorlage für interprofessionelle Team-Boards auf Station – analog & digital.
- **Interne Links:** → Hub #2; → Visual Management (#6), Stations-Dashboard (#27)
- **CTA:** Peakboard Designer kostenlos laden inline in der Sektion „analog vs. digital" → LinkedIn-Kontakt am Ende

**Briefing:** Do-Anteil bedienen — kostenlose Vorlage/Template-Sektion einplanen (SERP zeigt Miro-Template).
Definition → Was gehört aufs Board (Kennzahlen, Maßnahmen, Verantwortliche, Eskalation) als Tabelle →
15-Minuten-Huddle-Ablauf als nummerierte Schrittliste → interprofessionell (Ärzte, Pflege, Verwaltung gemeinsam)
→ analog vs. digital (Brücke zu #27). **Entities:** Huddle, ZHAW LeanHealth, Teamboard, Kaizen-Board.
**FAQ:** Was ist ein Huddle Board? / Wie lange dauert ein Huddle? / Was steht auf einem Huddle Board? / Huddle
Board digital oder analog? **Abgrenzung:** KEINE eigene Teamboard-Seite anlegen.

---

## ⬜ 4. Kennzahlen Krankenhaus *(C1, Spoke, P2)*

- **Fokuskeyword:** kennzahlen krankenhaus (30 SV, Know)
- **Sekundär:** krankenhaus kpi, kennzahlen pflege, qualitätsindikatoren krankenhaus, kennzahlen station
- **H1:** Kennzahlen im Krankenhaus: Die wichtigsten KPIs für Station, OP und Klinikleitung
- **Plan-Slug:** `daily-management/kennzahlen-krankenhaus`
- **Meta Title:** Kennzahlen im Krankenhaus: Top-KPIs | Lean Hospital
- **Meta Description:** Welche Kennzahlen braucht ein Krankenhaus wirklich? Die wichtigsten KPIs für Station, OP und Verwaltung – mit Formeln und Zielwerten.
- **Interne Links:** → Hub #2; → Leading/Lagging (#5), Verweildauer (#16), OP-Planung (#17)
- **CTA:** Peakboard Designer kostenlos laden inline nach KPI-Tabelle → LinkedIn-Kontakt am Ende

**Briefing:** Listicle-Struktur. KPI-Katalog als Tabelle mit Name, Formel, Ebene (Station/OP/Klinik), Frequenz.
Sektionen: Belegungs-KPIs (Auslastung, Verweildauer), OP-KPIs (Erstschnittzeit, Wechselzeit, Auslastung),
Pflege-KPIs (Pflegequote, Ausfallquote), Qualitäts-KPIs (Wiederaufnahmerate, Dekubitusrate). Kaskade nur
anreißen. **Entities:** G-BA-Qualitätsindikatoren, InEK, DRG, Case Mix Index. **FAQ:** Welche Kennzahlen sind im
Krankenhaus wichtig? / Was ist der Case Mix Index? / Wie viele Kennzahlen gehören auf ein Stationsboard?
**Abgrenzung:** keine Leading/Lagging-Theorie (→ #5).

---

## ⬜ 5. Leading & Lagging Indicators *(C1, Spoke, P2)*

- **Fokuskeyword:** leading lagging indicators (70 SV, Know)
- **Sekundär:** frühindikatoren spätindikatoren, leading kpi, lagging kpi, vorlaufende kennzahlen
- **H1:** Leading und Lagging Indicators: Frühindikatoren, mit denen Kliniken steuern statt reagieren
- **Plan-Slug:** `daily-management/leading-lagging-indicators`
- **Meta Title:** Leading vs. Lagging Indicators erklärt | Lean Hospital
- **Meta Description:** Leading und Lagging Indicators einfach erklärt: Unterschied, Beispiele aus dem Krankenhaus und wie Frühindikatoren die Steuerung verbessern.
- **Interne Links:** → Hub #2; → Kennzahlen (#4)
- **CTA:** LinkedIn-Kontakt am Ende → Peakboard Designer dezent in der Klinik-Beispiel-Sektion

**Briefing:** Generisches Fokuskeyword, Klinik-Beispiele als Differenzierung. Definitionsblock beider Begriffe →
Gegenüberstellungstabelle (steuerbar vs. rückblickend) → Klinik-Beispiele als Kern-Chunk (Leading: geplante
Entlassungen heute, freie Betten 14 Uhr, offene Konsile; Lagging: Verweildauer, Wiederaufnahmerate, CMI) → wie
man aus einem Lagging-KPI den Leading-KPI ableitet (3 Schritte). **Entities:** KPI, Kennzahlen-Kaskade, Balanced
Scorecard. **FAQ:** Unterschied Leading/Lagging? / Beispiele für Leading Indicators im Krankenhaus? / Warum
reichen Lagging-KPIs nicht?

---

## ⚠️ 6. Visual Management *(C1, Spoke, P2)*

> **Überschneidung:** Der Post „Die Arbeit sichtbar machen – Visuelles Management im Krankenhaus" (07.07.2026)
> deckt das Thema bereits ab, inklusive Andon, Cincinnati-Huddles und der Whiteboard-zu-Bildschirm-Passage.
> **Empfehlung:** keinen neuen Artikel schreiben, sondern den Bestandspost auf das Fokuskeyword optimieren
> (Title/Description/H1 anpassen, Definitionsblock ergänzen, FAQ anhängen).

- **Fokuskeyword:** visual management (100 SV, Know)
- **Sekundär:** visuelles management, visualisierung kennzahlen, andon krankenhaus, visual board
- **Meta Title (Vorlage):** Visual Management im Krankenhaus | Lean Hospital
- **Meta Description (Vorlage):** Visual Management macht Probleme auf einen Blick sichtbar. Definition, Prinzipien und Einsatz im Krankenhaus – vom Whiteboard bis zum Dashboard.
- **Noch fehlend im Bestandspost:** die 5 Prinzipien als Liste, Umsetzungsformen als eigener Chunk
  (Bettenbelegungstafel, Patientenstatus-Farben, Bodenmarkierungen/5S), FAQ-Sektion.
- **Entities:** Andon, Toyota, Mieruka, Obeya.

---

## ⬜ 7. Change Management Krankenhaus *(C2, Hub, P1)*

- **Fokuskeyword:** change management krankenhaus (10 SV, Know)
- **Sekundär:** kulturwandel krankenhaus, veränderungsmanagement klinik, change im gesundheitswesen
- **H1:** Change Management im Krankenhaus: Warum Lean eine Haltung ist – und wie der Wandel gelingt
- **Plan-Slug:** `change-management-krankenhaus`
- **Meta Title:** Change Management im Krankenhaus | Lean Hospital
- **Meta Description:** Change Management im Krankenhaus scheitert selten an Methoden, oft an Haltung. Wie Kliniken Teams für Lean gewinnen – mit Praxisbeispielen.
- **Interne Links:** → Pillar; → Lean Leadership (#8), Gemba Walk (#9), KVP (#10), Kata (#11), A3 (#12)
- **CTA:** LinkedIn-Kontakt am Ende → Kontaktformular sekundär; **kein Produkt-CTA** (Kulturthema)

**Briefing:** Narrativ stärker als die anderen Hubs. Kernthese als quotable Sentence: „Lean ist kein
Werkzeugkasten, sondern eine Haltung." Warum Wandel scheitert (Top-down, Werkzeug-Fixierung) → Haltung vor
Methode → interne „Lean-Übersetzer" zwischen Methode und Stationsalltag → Qualifikation gibt Sicherheit →
dezentrale Verbesserungsteams → Perspektive junger Führungskräfte → „Story of the Boat" (Arnout Orelio).
**Entities:** Jörg Gottschalk, Arnout Orelio, John Kotter (8 Stufen kurz), psychologische Sicherheit.
**FAQ:** Warum scheitert Change Management im Krankenhaus? / Wie nimmt man ein Stationsteam mit? / Wie lange
dauert Kulturwandel? **Abgrenzung:** Führungsverhalten im Detail → #8.

> **Hinweis Writing Guide:** Die im Plan genannten Vortrags-/Buchbezüge (Gottschalk, Ruf, Jaha/Huber) sind
> keine belastbaren Primärquellen für Zahlen. Als benannte Stimmen zitierbar, nicht als Beleg.

---

## ⬜ 8. Lean Leadership *(C2, Spoke, P2)*

- **Fokuskeyword:** lean leadership (100 SV, Know)
- **Sekundär:** lean führung, führung im krankenhaus (10), lean leader, führungskraft lean
- **H1:** Lean Leadership: Führung im Lean Hospital – vom Anordnen zum Befähigen
- **Plan-Slug:** `change-management-krankenhaus/lean-leadership`
- **Meta Title:** Lean Leadership: Führen im Krankenhaus | Lean Hospital
- **Meta Description:** Lean Leadership heißt befähigen statt anordnen. Die 4 Prinzipien und was sie für Chefärzte, Pflegedienst- und Stationsleitungen bedeuten.
- **Interne Links:** → Hub #7; → Gemba Walk (#9), Kata Coaching (#11)
- **CTA:** LinkedIn-Kontakt am Ende → kein Produkt-CTA

**Briefing:** Definition → die 4 Entwicklungsstufen nach Dombrowski/Mielke (Selbstentwicklung, Andere
entwickeln, Kaizen unterstützen, Zielorientierung/Hoshin) → Übersetzung auf Klinik-Rollen: Chefarzt,
Pflegedienstleitung, Stationsleitung (je eigener Chunk) → Anti-Muster (Feuerwehr-Führung, Anordnungs-Kultur) →
tägliche Führungsroutinen (Verbindung #9 und Daily Huddle). **Entities:** Toyota Way, Respect for People,
Servant Leadership, Stationsleitung. **FAQ:** Was ist Lean Leadership? / Wie führt man im Lean Hospital? / Was
unterscheidet es von klassischer Führung?

---

## ⬜ 9. Gemba Walk *(C2, Spoke, P2)* — größtes generisches Volumen

- **Fokuskeyword:** gemba walk (2.400 SV, Know 100 / Do 50, CPC 3,70 €)
- **Sekundär:** gemba, go and see, gemba walk checkliste, gemba walk fragen
- **H1:** Gemba Walk: Führen am Ort der Wertschöpfung – Ablauf, Fragen, Checkliste
- **Plan-Slug:** `change-management-krankenhaus/gemba-walk`
- **Meta Title:** Gemba Walk: Ablauf, Fragen & Checkliste | Lean Hospital
- **Meta Description:** Gemba Walk einfach erklärt: Ablauf in 5 Schritten, die richtigen Fragen und eine Checkliste – mit Beispiel von der Krankenhausstation.
- **Interne Links:** → Hub #7; → Lean Leadership (#8), 7 Arten der Verschwendung (#18)
- **CTA:** LinkedIn-Kontakt am Ende (Checklisten-Download) → kein Produkt-CTA

**Briefing:** Generischen Know-Intent VOLL bedienen (Definition, Herkunft, Ablauf, Checkliste), Krankenhaus als
durchgängiges Beispiel statt als Nische framen. Definitionsblock → Herkunft (Gemba = „der wahre Ort", Toyota) →
Ablauf in 5 Schritten → die 3 Gemba-Fragen + 10 Beispielfragen für die Station → Checklisten-Sektion (Do-Anteil!)
→ Fehler beim Gemba Walk → Beispiel: Gemba Walk auf einer chirurgischen Station (durcherzählt).
**Entities:** Taiichi Ohno, Genchi Genbutsu, Toyota-Produktionssystem, Management by Walking Around (Abgrenzung!).
**FAQ:** Was ist ein Gemba Walk? / Wie oft? / Welche Fragen? / Unterschied zu MBWA?

---

## ⬜ 10. Kontinuierlicher Verbesserungsprozess (KVP) *(C2, Spoke, P2)*

- **Fokuskeyword:** kontinuierlicher verbesserungsprozess (150 SV, Know)
- **Sekundär:** kvp, kvp methoden, kvp krankenhaus, kaizen krankenhaus, kvp beispiele
- **H1:** Kontinuierlicher Verbesserungsprozess (KVP): So gelingt KVP im Krankenhaus
- **Plan-Slug:** `change-management-krankenhaus/kontinuierlicher-verbesserungsprozess`
- **Meta Title:** Kontinuierlicher Verbesserungsprozess | Lean Hospital
- **Meta Description:** Was ist der kontinuierliche Verbesserungsprozess? KVP einfach erklärt – Methoden, Beispiele und Einführung im Krankenhaus in 6 Schritten.
- **Interne Links:** → Hub #7; → PDCA Pflege (#21), A3 Report (#12), Kata (#11)
- **CTA:** LinkedIn-Kontakt am Ende → Kontaktformular sekundär

**Briefing:** Definitionsblock KVP/Kaizen (+ Abgrenzung: Kaizen = Philosophie, KVP = institutionalisierter
Prozess) → die 3 Ebenen (Management-, Gruppen-, Individual-KVP) → KVP-Werkzeuge als Tabelle mit Links →
Einführung im Krankenhaus in 6 Schritten → Beispiele von Station (Wegezeiten, Materialsuche, Doppeldokumentation)
→ warum KVP-Programme einschlafen. **Entities:** Kaizen, Masaaki Imai, Ideenmanagement, Verbesserungsteam.
**FAQ:** Was ist KVP? / Unterschied KVP und Kaizen? / Wie führt man KVP im Krankenhaus ein?

---

## ⬜ 11. Kata Coaching *(C2, Spoke, P3)*

- **Fokuskeyword:** kata coaching (90 SV, Know)
- **Sekundär:** verbesserungskata (10), coaching kata, toyota kata, kata fragen
- **H1:** Kata Coaching: Mit Verbesserungskata und Coaching-Kata Routinen für den Wandel schaffen
- **Plan-Slug:** `change-management-krankenhaus/kata-coaching`
- **Meta Title:** Kata Coaching: Kata-Routinen & 5 Fragen | Lean Hospital
- **Meta Description:** Kata Coaching macht Verbesserung zur täglichen Routine. Verbesserungskata, Coaching-Kata und die 5 Fragen – erklärt am Klinikbeispiel.
- **Interne Links:** → Hub #7; → KVP (#10), Lean Leadership (#8)
- **CTA:** LinkedIn-Kontakt am Ende → kein Produkt-CTA

**Briefing:** Definitionsblock (Kata = eingeübte Routine) → Verbesserungskata: die 4 Schritte (Richtung,
Ist-Zustand, Ziel-Zustand, Experimentieren) → Coaching-Kata: die 5 Fragen als zitierfähige Liste → Rollen
(Lernender/Coach/Second Coach) → Klinik-Beispiel: Stationsleitung als Lernende, PDL als Coach, Ziel-Zustand
„Visite bis 10 Uhr abgeschlossen" → Verbindung zu #10 und #2. **Entities:** Mike Rother, Toyota Kata,
Ziel-Zustand, PDCA. **FAQ:** Was ist Kata Coaching? / Wie lauten die 5 Kata-Fragen? / Unterschied
Verbesserungskata / Coaching-Kata?

---

## ⬜ 12. A3 Report *(C2, Spoke, P3)*

- **Fokuskeyword:** a3 report (200 SV, Know, CPC 23 € — kommerzieller Trainingsmarkt)
- **Sekundär:** a3 methode, a3 problemlösung, a3 report vorlage, a3 denken
- **H1:** A3 Report: Strukturierte Problemlösung auf einer Seite – Aufbau, Vorlage, Klinikbeispiel
- **Plan-Slug:** `change-management-krankenhaus/a3-report`
- **Meta Title:** A3 Report: Aufbau, Vorlage & Beispiel | Lean Hospital
- **Meta Description:** Der A3 Report löst Probleme strukturiert auf einer Seite. Die 7 Felder, eine Vorlage und ein durchgerechnetes Beispiel aus dem Krankenhaus.
- **Interne Links:** → Hub #7; → KVP (#10), PDCA Pflege (#21)
- **CTA:** **A3-Vorlage-Download als Haupt-CTA** → LinkedIn-Kontakt am Ende

**Briefing:** Edukativ bleiben trotz kommerzieller SERP. Definitionsblock → warum A3 (eine Seite erzwingt
Klarheit; quotable) → die 7 Felder als nummerierte Liste mit je 2–3 Sätzen → A3 = PDCA auf Papier (→ #21) →
durcherzähltes Klinikbeispiel: „Notfall-Labor-Befunde kommen zu spät auf Station" als A3 → Vorlage
(Download-Sektion) → typische Fehler. **Entities:** Toyota, PDCA, Ursachenanalyse, 5-Why, Ishikawa.
**FAQ:** Was ist ein A3 Report? / Welche Felder hat ein A3? / Wann A3 statt Maßnahmenliste?

---

## ⬜ 13. Patientensteuerung *(C3, Hub, P1)*

- **Fokuskeyword:** patientensteuerung (70 SV, Know)
- **Sekundär:** patientenfluss (10), patient flow, patientenlogistik, patientenpfad
- **H1:** Patientensteuerung: Patient Flow von der Aufnahme bis zur Entlassung
- **Plan-Slug:** `patientensteuerung`
- **Meta Title:** Patientensteuerung: Patient Flow steuern | Lean Hospital
- **Meta Description:** Patientensteuerung entscheidet über Wartezeiten, Auslastung und Qualität. Wie Kliniken den Patient Flow von Aufnahme bis Entlassung steuern.
- **Interne Links:** → Pillar; → #14, #15, #16, #17, #18, #19
- **CTA:** Kontaktformular am Ende → Peakboard Designer inline in der Echtzeitdaten-Sektion

**Briefing:** Kern-These (quotable): „Nicht Kapazität, sondern Patient Flow bestimmt die Leistungsfähigkeit eines
Krankenhauses." Definition Patientensteuerung/Patient Flow → das Fluss-Paradigma vs. Kapazitäts-Paradigma → die
Wertschöpfungskette Aufnahme→Diagnostik→OP→Station→Entlassung, je Station ein Chunk mit Link auf Spoke →
Nivellierung/Heijunka („Takt statt Zufall") → Kennzahlen des Patient Flow → Rolle von Echtzeitdaten (Brücke C5).
**Entities:** Patient Flow, Heijunka, Durchlaufzeit, Belegungsmanagement, Wertstrom.
**FAQ:** Was ist Patientensteuerung? / Was bedeutet Patient Flow? / Warum ist Flow wichtiger als Kapazität?
**Abgrenzung:** Entlassung, Betten, OP je eigene Spokes – hier nur je 1 Absatz.

> ⚠️ Die geplante 70-%-Durchlaufzeit-Zahl (Andreux/Wacogne) ist **unbelegt** — siehe offene Punkte. Ersatz:
> Wang et al. 2025 liefert belastbare Spannweiten zu Verweildauer und Wartezeit.
> Querverweis auf den bestehenden Notaufnahme-Crowding-Post anbieten.

---

## ⬜ 14. Entlassmanagement *(C3, Spoke, P1)* — **größte SEO-Chance des Plans**

- **Fokuskeyword:** entlassmanagement (1.300 SV, Know 100 / Do 31, Wettbewerb 43, CPC 1,20 €)
- **Sekundär:** entlassmanagement krankenhaus, entlassmanagement checkliste, rahmenvertrag entlassmanagement, entlassplan
- **H1:** Entlassmanagement im Krankenhaus: Prozess, Rahmenvertrag und Checkliste
- **Plan-Slug:** `patientensteuerung/entlassmanagement`
- **Meta Title:** Entlassmanagement: Prozess & Checkliste | Lean Hospital
- **Meta Description:** Entlassmanagement einfach erklärt: gesetzliche Grundlagen (§ 39 SGB V), der Prozess in 6 Schritten und eine Checkliste für die Station.
- **Interne Links:** → Hub #13; → Verweildauer (#16), Bettenmanagement (#15)
- **CTA:** **Checklisten-Download als Haupt-CTA** → LinkedIn-Kontakt am Ende; kein Produkt-CTA (früh im Funnel)

**Briefing:** SERP-Intent: Ratgeber mit rechtlichem Unterbau – beides liefern. Definitionsblock → gesetzliche
Grundlage (§ 39 Abs. 1a SGB V, Rahmenvertrag Entlassmanagement, Einwilligung des Patienten) → der Prozess in
6 Schritten ab Aufnahme (Assessment innerhalb 24 h) → Rollen (Ärzte, Pflege, Sozialdienst, Case Management) →
Checkliste als Tabelle → Lean-Sicht: Entlassung beginnt bei Aufnahme, geplantes Entlassdatum als Steuerungsgröße
→ häufige Fehler. **Entities:** § 39 SGB V, GKV-Spitzenverband, DKG, KBV, Rahmenvertrag Entlassmanagement, Case
Management, Sozialdienst. **FAQ:** Was ist Entlassmanagement? / Ist es Pflicht? / Wer ist zuständig? / Was
gehört in einen Entlassplan?

> ⚠️ **Rechtsstand vor Veröffentlichung prüfen.**

---

## ⬜ 15. Bettenmanagement *(C3, Spoke, P2)*

- **Fokuskeyword:** bettenmanagement (90 SV, Know+Do 100/50)
- **Sekundär:** bettenmanagement krankenhaus (20), belegungsmanagement, bettenplanung, bettensteuerung
- **H1:** Bettenmanagement im Krankenhaus: Belegung steuern, Engpässe vermeiden
- **Plan-Slug:** `patientensteuerung/bettenmanagement`
- **Meta Title:** Bettenmanagement im Krankenhaus | Lean Hospital
- **Meta Description:** Zentrales Bettenmanagement senkt Wartezeiten und glättet Belastungsspitzen. Aufgaben, Kennzahlen und Methoden – inkl. Nivellierung nach Lean.
- **Interne Links:** → Hub #13; → Verweildauer (#16), Entlassmanagement (#14), Stations-Dashboard (#27)
- **CTA:** Peakboard Designer inline in „Digitale Bettenübersicht" → Kontaktformular am Ende

**Briefing:** Do-Anteil = Software-Interesse → Sektion „Digitale Bettenübersicht" mit neutraler Anforderungsliste.
Definitionsblock → zentral vs. dezentral (Vor-/Nachteile-Tabelle) → Aufgaben → Kennzahlen (Auslastung, freie
Betten 14 Uhr als Leading Indicator → #5) → Nivellierung: elektive Aufnahmen takten statt Montags-Peak
(Heijunka) → Zusammenspiel mit Entlassmanagement (geplantes Entlassdatum). **Entities:** Belegungsmanagement,
Heijunka, Patientenlogistik. **FAQ:** Was macht ein Bettenmanagement? / Zentral oder dezentral? / Welche
Kennzahlen?

---

## ⬜ 16. Verweildauer Krankenhaus *(C3, Spoke, P2)*

- **Fokuskeyword:** verweildauer krankenhaus (60 SV, Know)
- **Sekundär:** durchschnittliche verweildauer krankenhaus, verweildauer senken, durchlaufzeit krankenhaus, verweildauer drg
- **H1:** Verweildauer im Krankenhaus: Kennzahl verstehen – und aktiv senken
- **Plan-Slug:** `patientensteuerung/verweildauer-krankenhaus`
- **Meta Title:** Verweildauer im Krankenhaus: Die Hebel | Lean Hospital
- **Meta Description:** Was sagt die Verweildauer im Krankenhaus aus? Definition, aktuelle Durchschnittswerte und die wirksamsten Hebel, um sie ohne Qualitätsverlust zu senken.
- **Interne Links:** → Hub #13; → Entlassmanagement (#14), Bettenmanagement (#15), Kennzahlen (#4)
- **CTA:** LinkedIn-Kontakt am Ende → Peakboard Designer dezent bei Kennzahlen-Hebeln

**Briefing:** Definitionsblock (Berechnung, Abgrenzung prä-/postoperative VWD, Katalog-VWD im DRG-System) →
aktuelle Durchschnittswerte DE **mit Quelle (Destatis/InEK, beim Schreiben verifizieren)** → warum lange VWD
selten am Patienten liegt (Wartezeiten auf Diagnostik, Konsile, Entlasspapiere → #18) → die 5 wirksamsten Hebel
als Liste (geplantes Entlassdatum, Visitenstandard, Diagnostik-Taktung, Entlassmanagement ab Tag 1,
Wochenend-Entlassungen) → Fehlanreiz-Diskussion kurz (untere Grenzverweildauer). **Entities:** DRG, InEK,
Destatis, mittlere Verweildauer, Grenzverweildauer. **FAQ:** Wie berechnet man die Verweildauer? / Wie hoch ist
sie in Deutschland? / Wie kann man sie senken?

---

## ⬜ 17. OP-Planung *(C3, Spoke, P2)*

- **Fokuskeyword:** op planung (90 SV, Know+Do, CPC 15 €)
- **Sekundär:** op auslastung, op management, op plan krankenhaus, op saal effizienz
- **H1:** OP-Planung: Auslastung, Taktung und Kennzahlen im OP-Management
- **Plan-Slug:** `patientensteuerung/op-planung`
- **Meta Title:** OP-Planung: Kennzahlen & Best Practices | Lean Hospital
- **Meta Description:** Der OP ist der teuerste Ort der Klinik. Wie gute OP-Planung Auslastung erhöht und Wechselzeiten senkt – Kennzahlen, Taktung, Best Practices.
- **Interne Links:** → Hub #13; → Kennzahlen (#4), Stations-Dashboard (#27)
- **CTA:** Peakboard Designer inline in der Echtzeit-Transparenz-Sektion → Kontaktformular am Ende

**Briefing:** Edukativ halten trotz starkem Software-Markt, neutrale Anforderungssektion am Ende.
Definitionsblock → warum der OP der Engpass ist (quotable: teuerste Ressource) → OP-Kennzahlen als Tabelle
(Erstschnittzeit, Naht-Schnitt-Zeit/Wechselzeit, Auslastung, Absetzquote, Notfallquote) → Taktung &
Saalprogramm-Planung (Blockzeiten, Puffer für Notfälle) → OP-Statut & Rollen (OP-Manager, OP-Koordinator) →
Echtzeit-Transparenz im OP (→ #27). **Entities:** OP-Management, Erstschnittzeit, Wechselzeit, OP-Statut.
**FAQ:** Was macht ein OP-Manager? / Welche Kennzahlen sind im OP wichtig? / Wie verbessert man die Auslastung?

> Querverweis: der bestehende Post zur OP-Sicherheitscheckliste passt hier als `read_more_link`.

---

## ⬜ 18. 7 Arten der Verschwendung *(C3, Spoke, P2)*

- **Fokuskeyword:** 7 arten der verschwendung (250 SV, Know)
- **Sekundär:** muda mura muri (250 — **bewusst auf derselben Seite**), verschwendung lean (20), verschwendungsarten, timwood
- **H1:** Die 7 Arten der Verschwendung – und wo sie im Krankenhaus stecken
- **Plan-Slug:** `patientensteuerung/7-arten-der-verschwendung`
- **Meta Title:** 7 Arten der Verschwendung im Krankenhaus | Lean Hospital
- **Meta Description:** Die 7 Arten der Verschwendung (TIMWOOD) einfach erklärt – mit konkreten Beispielen aus dem Krankenhaus und dem Unterschied zu Muda, Mura, Muri.
- **Interne Links:** → Hub #13; → Wertstromanalyse (#19), Gemba Walk (#9), 5S (#22)
- **CTA:** LinkedIn-Kontakt am Ende → kein Produkt-CTA

**Briefing:** Zwei 250er-Keywords auf EINER Seite — getrennte Seiten würden kannibalisieren.
Definitionsblock Verschwendung/Muda → die 7 Arten als je eigener H3-Chunk mit Kurzdefinition +
Krankenhaus-Beispiel (Transport = Patiententransporte, Bestände = volle Lagerräume, Bewegung = Laufwege der
Pflege, Warten, Überproduktion = Doppeldokumentation, Überbearbeitung = unnötige Diagnostik, Fehler =
Wiederaufnahmen) → 8. Verschwendung: ungenutztes Mitarbeiterpotenzial → **eigene H2-Sektion „Muda, Mura, Muri:
der Unterschied"** (bedient das Zweit-Keyword als eigener Chunk) → TIMWOOD-Merkhilfe. **Entities:** Taiichi Ohno,
TIMWOOD, Muda/Mura/Muri. **FAQ:** Was sind die 7 Arten? / Was bedeutet TIMWOOD? / Unterschied Muda/Mura/Muri? /
Was ist die 8. Verschwendung?

---

## ⬜ 19. Wertstromanalyse Krankenhaus *(C3, Spoke, P3)*

- **Fokuskeyword:** wertstromanalyse krankenhaus (10 SV, Know)
- **Sekundär:** wertstromanalyse (2.050, Longshot), value stream mapping healthcare, patientenpfad analyse, wertstromdesign
- **H1:** Wertstromanalyse im Krankenhaus: Den Patientenpfad als Wertstrom abbilden
- **Plan-Slug:** `patientensteuerung/wertstromanalyse-krankenhaus`
- **Meta Title:** Wertstromanalyse im Krankenhaus | Lean Hospital
- **Meta Description:** Wertstromanalyse im Krankenhaus: Wie Sie den Patientenpfad als Wertstrom abbilden, Wartezeiten sichtbar machen und Prozesse neu gestalten.
- **Interne Links:** → Hub #13; → 7 Arten (#18), Verweildauer (#16)
- **CTA:** LinkedIn-Kontakt am Ende → Kontaktformular sekundär

**Briefing:** Nischen-Fokus bewusst; generische Grundfragen (Definition, Symbole, Vorgehen) trotzdem beantworten,
damit Long-Tail greift. Definitionsblock → Besonderheit im Krankenhaus: der Patient ist das „Werkstück",
Wertstrom = Patientenpfad → Anleitung in 6 Schritten (Patientengruppe wählen, Ist-Wertstrom am Gemba aufnehmen,
Zeiten erfassen, Kennzahlen berechnen, Soll-Wertstrom, Maßnahmen) → Beispiel: elektive Hüft-TEP von Aufnahme bis
Entlassung → Flussgrad als quotable KPI. **Entities:** Value Stream Mapping, Flussgrad, Durchlaufzeit, Mike
Rother/John Shook („Learning to See"). **FAQ:** Was ist eine Wertstromanalyse im Krankenhaus? / Wie läuft sie
ab? / Was ist der Flussgrad?

---

## ⬜ 20. Lean Management Pflege *(C4, Hub, P1)*

- **Fokuskeyword:** lean management pflege (10 SV, Know)
- **Sekundär:** lean pflege, lean in der pflege, lean nursing, lean methoden pflege
- **H1:** Lean Management in der Pflege: Mehr Zeit für Patienten statt für Wege und Suchen
- **Plan-Slug:** `lean-management-pflege`
- **Meta Title:** Lean Management in der Pflege | Lean Hospital
- **Meta Description:** Lean Management in der Pflege heißt: Laufwege halbieren, Unterbrechungen eliminieren, Zeit für Patienten gewinnen. Methoden und Praxisbeispiele.
- **Interne Links:** → Pillar; → 5S (#22), PDCA Pflege (#21), Schichtübergabe (#23), Digitalisierung Pflege (#26)
- **CTA:** LinkedIn-Kontakt am Ende → Kontaktformular sekundär; Produkt-CTA nur dezent (**sensibles Thema:
  Rationalisierungs-Verdacht**)

**Briefing:** Einstieg über den provokanten Frame „Wer stört? Der Patient?" → Kernproblem: Pflegezeit fließt in
Wege, Suchen, Unterbrechungen, Dokumentation statt in Patienten (Zahlen zu Laufwegen **verifizieren**) → die 4
größten Hebel je als Chunk: Laufwege (Spaghetti-Diagramm, Materiallogistik/5S), Unterbrechungen
(Störungsanalyse, stille Stunde), Standards (Übergabe, Visite), kontinuierliche Verbesserung (PDCA,
Pflegekonferenz) → berufsgruppenübergreifende Zuständigkeiten → Pflege als treibende Kraft.
**FAQ:** Was bringt Lean in der Pflege? / **Ist Lean in der Pflege nur Rationalisierung?** (Einwand ernst
nehmen — hier gehört die Moraros-Gegenevidenz zur Mitarbeiterzufriedenheit hin) / Wie startet eine Station?

---

## ⬜ 21. PDCA-Zyklus Pflege *(C4, Spoke, P1)*

- **Fokuskeyword:** pdca zyklus pflege (250 SV, Know)
- **Sekundär:** pdca pflege beispiel, demingkreis pflege, pdca zyklus (7.300, Longshot), plan do check act pflege
- **H1:** PDCA-Zyklus in der Pflege: Der Qualitätskreislauf einfach erklärt – mit Beispielen
- **Plan-Slug:** `lean-management-pflege/pdca-zyklus-pflege`
- **Meta Title:** PDCA-Zyklus in der Pflege: Beispiele | Lean Hospital
- **Meta Description:** Der PDCA-Zyklus in der Pflege einfach erklärt: die 4 Phasen, Bezug zum Qualitätsmanagement und zwei ausgearbeitete Beispiele von Station.
- **Interne Links:** → Hub #20; → KVP (#10), A3 Report (#12)
- **CTA:** LinkedIn-Kontakt am Ende; kein Produkt-CTA (Azubi-/Examens-Publikum)

**Briefing:** Ausbildungs-/Examens-Publikum → didaktisch schreiben. Definitionsblock (Deming-Kreis) → die 4
Phasen je als H3 mit Pflege-Bezug → Verankerung im QM (Expertenstandards, QM-Pflicht — **Rechtsstand
verifizieren**) → Beispiel 1 ausgearbeitet: Sturzprophylaxe verbessern (kompletter Zyklus) → Beispiel 2 kurz:
Dekubitusrate → **Abgrenzung PDCA vs. Pflegeprozess (6 Schritte) als eigene Sektion** (häufige Prüfungsfrage) →
Fehler (Check überspringen). **Entities:** W. Edwards Deming, Demingkreis, Pflegeprozess, Expertenstandards,
DNQP. **FAQ:** Was ist der PDCA-Zyklus in der Pflege? / Beispiel? / Unterschied PDCA und Pflegeprozess?

---

## ⬜ 22. 5S-Methode Krankenhaus *(C4, Spoke, P2)*

- **Fokuskeyword:** 5s methode krankenhaus (0 SV — bewusste GEO-/Long-Tail-Wette)
- **Sekundär:** 5s methode (2.800, Longshot), 5s pflege, 5s arbeitsplatz, 5s beispiele
- **H1:** 5S-Methode im Krankenhaus: Ordnung und Standards, die Suchzeiten eliminieren
- **Plan-Slug:** `lean-management-pflege/5s-methode-krankenhaus`
- **Meta Title:** 5S-Methode im Krankenhaus: Anleitung | Lean Hospital
- **Meta Description:** Die 5S-Methode im Krankenhaus: Wie Stationen mit Sortieren, Systematisieren und Standardisieren Suchzeiten eliminieren – Anleitung in 5 Schritten.
- **Interne Links:** → Hub #20; → 7 Arten (#18), Visual Management (#6)
- **CTA:** **5S-Audit-Checkliste als Download-CTA** → LinkedIn-Kontakt am Ende

**Briefing:** Generische Grundfragen trotzdem beantworten. Definitionsblock mit den 5 japanischen Begriffen +
deutscher Übersetzung als Tabelle (Seiri/Sortieren, Seiton/Systematisieren, Seiso/Säubern,
Seiketsu/Standardisieren, Shitsuke/Selbstdisziplin) → warum 5S im Krankenhaus doppelt zählt (Suchzeiten +
Hygiene + Patientensicherheit; quotable) → Anleitung je S mit Stations-Beispiel (Medikamentenschrank,
Verbandswagen, Lagerraum) → Vorher/Nachher-Fotostrecke empfehlen → 5S-Audit-Checkliste → Verbindung zu Visual
Management (Schattenbretter, Markierungen). **Entities:** Seiri–Shitsuke, Toyota, Arbeitsplatzorganisation,
Schattenbrett. **FAQ:** Was ist die 5S-Methode? / Wie führt man 5S auf einer Station ein? / Was bringt 5S?

---

## ⚠️ 23. Schichtübergabe Pflege *(C4, Spoke, P3)*

> **Überschneidung:** „Die Übergabe ist die Bruchstelle – wie I-PASS und SBAR sie reparieren" (29.06.2026) deckt
> SBAR und die Evidenzlage bereits ab. **Empfehlung:** Bestandspost um die Lean-/Ablauf-Perspektive erweitern
> statt neuen Artikel anlegen.

- **Fokuskeyword:** schichtübergabe pflege (10 SV, Know)
- **Sekundär:** übergabe pflege, sbar schema, dienstübergabe pflege, strukturierte übergabe
- **Meta Title (Vorlage):** Schichtübergabe Pflege: Ablauf & SBAR | Lean Hospital
- **Noch fehlend im Bestandspost:** Übergabeformen im Vergleich (Tabelle: klassisch im Dienstzimmer / am
  Patientenbett / digital gestützt), Lean-Sicht (Übergabe als Standard mit Timebox, Verbindung zum Huddle),
  Einführung in 4 Schritten, FAQ.

---

## ⬜ 24. Digitalisierung Krankenhaus *(C5, Hub, P1)*

- **Fokuskeyword:** digitalisierung krankenhaus (150 SV, Know)
- **Sekundär:** digitales krankenhaus, krankenhaus 4.0, digitale transformation krankenhaus, ehealth klinik
- **H1:** Digitalisierung im Krankenhaus: Vom Papier-Board zum Echtzeit-Dashboard
- **Plan-Slug:** `digitalisierung-krankenhaus`
- **Meta Title:** Digitalisierung im Krankenhaus | Lean Hospital
- **Meta Description:** Digitalisierung im Krankenhaus: Wo deutsche Kliniken stehen, welche Hürden bremsen und wie Echtzeit-Daten Lean-Prozesse beschleunigen.
- **Interne Links:** → Pillar; → KHZG (#25), Digitalisierung Pflege (#26), Stations-Dashboard (#27); Querlink #2
- **CTA:** Peakboard Designer inline nach der Low-Code-Sektion → Kontaktformular am Ende

**Briefing:** Lean-Perspektive als Differenzierung (SERP ist voll mit Beratungs-Content): „Erst der Prozess, dann
das Tool" als quotable Kernthese. Status quo DE (DigitalRadar/Digitalisierungsgrad — **aktuelle Zahlen
verifizieren**) → Handlungsfelder als Chunks (KIS/Dokumentation, Echtzeit-Transparenz/Dashboards, digitale
Assistenzsysteme im OP, Pflege) → Hürden ehrlich benennen (IT-Ressourcen als Flaschenhals, Interoperabilität,
Datenschutz) → Low-Code als Antwort auf den IT-Engpass (1 Absatz, neutral) → Praxispfad: vom Papier-Aushang zum
Dashboard, als Reifegradmodell in 4 Stufen. **Entities:** KHZG, DigitalRadar, KIS, Interoperabilität, HL7/FHIR,
Low-Code. **FAQ:** Wie digital sind deutsche Krankenhäuser? / Größte Hürden? / Was bringt es dem Personal?

---

## ⬜ 25. Krankenhauszukunftsgesetz (KHZG) *(C5, Spoke, P2)*

- **Fokuskeyword:** krankenhauszukunftsgesetz (550 SV, Know)
- **Sekundär:** khzg, khzg fördertatbestände, krankenhauszukunftsfonds, khzg nachfolge
- **H1:** Krankenhauszukunftsgesetz (KHZG): Bilanz, Fördertatbestände und was jetzt kommt
- **Plan-Slug:** `digitalisierung-krankenhaus/krankenhauszukunftsgesetz`
- **Meta Title:** Krankenhauszukunftsgesetz (KHZG): Bilanz | Lean Hospital
- **Meta Description:** Das Krankenhauszukunftsgesetz hat die Klinik-Digitalisierung angeschoben. Bilanz der Fördertatbestände, Stand 2026 und was nach dem KHZG kommt.
- **Interne Links:** → Hub #24; → Stations-Dashboard (#27), Digitalisierung Pflege (#26)
- **CTA:** Kontaktformular am Ende → LinkedIn-Kontakt sekundär

**Briefing:** **WICHTIG: Gesetzes-/Förderstand vor dem Schreiben verifizieren** (Förderphase weitgehend
ausgelaufen) — Artikel als **Bilanz + Einordnung + „Was kommt danach"** framen, NICHT als Antragsratgeber.
Definitionsblock KHZG (Krankenhauszukunftsfonds, Volumen verifizieren) → die 11 Fördertatbestände als Tabelle
mit je 1-Satz-Erklärung (starkes GEO-Asset) → Bilanz: was wurde erreicht, wo hakt es (DigitalRadar-Evaluation) →
Sanktionsregelung § 5 Abs. 3h KHEntgG → Ausblick: Anschlussfinanzierung/Krankenhausreform → was Kliniken jetzt
tun sollten. **Entities:** KHZG, Krankenhauszukunftsfonds, BAS, DigitalRadar, KHEntgG.
**FAQ:** Was ist das KHZG? / Welche Fördertatbestände? / Was passiert danach? / Drohen Sanktionen?

---

## ⬜ 26. Digitalisierung Pflege *(C5, Spoke, P2)*

- **Fokuskeyword:** digitalisierung pflege (100 SV, Know)
- **Sekundär:** digitale pflege, pflege 4.0, digitale pflegedokumentation, technik in der pflege
- **H1:** Digitalisierung in der Pflege: Entlastung statt Extra-Aufwand
- **Plan-Slug:** `digitalisierung-krankenhaus/digitalisierung-pflege`
- **Meta Title:** Digitalisierung in der Pflege | Lean Hospital
- **Meta Description:** Digitalisierung in der Pflege muss entlasten, nicht belasten. Welche Anwendungen wirklich Zeit sparen – von Dokumentation bis Echtzeit-Boards.
- **Interne Links:** → Hub #24; → Lean Pflege (#20), Schichtübergabe (#23), Stations-Dashboard (#27)
- **CTA:** Peakboard Designer inline bei digitalen Boards → LinkedIn-Kontakt am Ende

**Briefing:** These als quotable Sentence: „Digitalisierung in der Pflege ist nur dann erfolgreich, wenn sie
messbar Zeit für Patienten freisetzt." Handlungsfelder je als Chunk: digitale Pflegedokumentation
(Doppeldokumentation als Verschwendung → #18), digitale Übergabe/Boards (→ #23, #3), Sensorik/Rufsysteme,
Dienstplanung → Akzeptanzfaktoren (Beteiligung, Schulung) → **Kritik ernst nehmen: Technikstress, doppelte
Systeme** → Pflege als Treiber. **Entities:** Pflege 4.0, elektronische Patientenakte, DVPMG, Entbürokratisierung.
**FAQ:** Wie verändert Digitalisierung die Pflege? / Welche Tools entlasten wirklich? / Ersetzt Technik
Pflegekräfte? (klar verneinen)

---

## ⬜ 27. Stations-Dashboard *(C5, Spoke, P2)* — **Peakboard-Brücke**

- **Fokuskeyword:** stations-dashboard (0 SV — bewusste GEO-/Kategorie-Besetzung)
- **Sekundär:** krankenhaus dashboard, klinik dashboard, echtzeit dashboard krankenhaus, kennzahlen visualisierung klinik
- **H1:** Stations-Dashboard: Echtzeit-Daten für Station, OP und Ambulanz
- **Plan-Slug:** `digitalisierung-krankenhaus/stations-dashboard`
- **Meta Title:** Stations-Dashboard für die Klinik | Lean Hospital
- **Meta Description:** Was gehört auf ein Stations-Dashboard? Aufbau, Datenquellen (KIS, SAP) und Beispiele für Echtzeit-Dashboards in Station, OP und Ambulanz.
- **Interne Links:** → Hub #24; → Huddle Board (#3), Kennzahlen (#4), Bettenmanagement (#15), OP-Planung (#17)
- **CTA:** **Peakboard Designer kostenlos laden als Haupt-CTA** (natürlichste Brücke im ganzen Plan) →
  Kontaktformular am Ende

**Briefing:** Einziger Artikel mit explizitem kommerziellen Anteil — **trotzdem 80 % edukativ**.
Definitionsblock → Dashboard vs. Huddle Board (Abgrenzung + Querlink: Board = Routine, Dashboard = Datenquelle)
→ was gehört drauf je Einsatzort (3 Chunks: Station [Belegung, Entlassungen, Personalstatus], OP [Saalstatus,
Verzögerungen], Ambulanz [Wartezeiten, Aufkommen]) → Datenquellen & Anbindung (KIS, SAP, manuelle Erfassung als
Übergangslösung) → Anforderungen an die Technik als Checkliste (Echtzeit, Drilldown, Rechte, ohne
IT-Großprojekt/Low-Code) → dezente Peakboard-Erwähnung als ein Umsetzungsweg + Beispiel. **Entities:** KIS, SAP,
HL7/FHIR, Low-Code, Drilldown, Peakboard. **FAQ:** Was ist ein Stations-Dashboard? / Welche Daten gehören drauf?
/ Woher kommen die Daten?

> **Writing-Guide-Hinweis:** Peakboard-Einsätze sind industriell dokumentiert, nicht klinisch. Die Übertragung
> als Erweiterung der Idee kennzeichnen, nicht als belegtes klinisches Ergebnis — Formulierung siehe
> Visual-Management-Post und #1.

---

## ⬜ 28. Hoshin Kanri *(C6, Hub, P2)*

- **Fokuskeyword:** hoshin kanri (1.100 SV, Know 100)
- **Sekundär:** hoshin kanri x matrix, policy deployment, hoshin planning, zielentfaltung
- **H1:** Hoshin Kanri: Strategieumsetzung mit System – von der X-Matrix bis zur Stationsebene
- **Plan-Slug:** `hoshin-kanri`
- **Meta Title:** Hoshin Kanri: Methode & X-Matrix erklärt | Lean Hospital
- **Meta Description:** Hoshin Kanri einfach erklärt: die Methode, die X-Matrix und der Catchball-Prozess – mit einem Umsetzungsbeispiel aus dem Krankenhaus.
- **Interne Links:** → Pillar; → Strategieumsetzung (#29), Klinisches Risikomanagement (#30); Querlink #2
- **CTA:** LinkedIn-Kontakt am Ende → Kontaktformular sekundär; Peakboard nur dezent bei Kaskaden-Visualisierung

**Briefing:** Generischen Intent voll bedienen, Krankenhaus als Anwendungsbeispiel. Definitionsblock (Hoshin
Kanri = Kompassnadel-Management/Policy Deployment) → die 7 Schritte des Hoshin-Prozesses → **X-Matrix erklärt mit
beschrifteter Grafik** (die 4 Quadranten; starkes Snippet-/GEO-Asset) → Catchball-Prinzip → Verbindung zu Daily
Management: Hoshin liefert die Ziele, das DMS die tägliche Steuerung (Kaskaden-Grafik) → Klinik-Beispiel:
Jahresziel „Verweildauer −0,5 Tage" über X-Matrix auf Stationsziele heruntergebrochen → Abgrenzung zu
MbO/Balanced Scorecard. **Entities:** X-Matrix, Catchball, Policy Deployment, True North, Walter Petschnig.
**FAQ:** Was ist Hoshin Kanri? / Wie funktioniert die X-Matrix? / Was ist Catchball? / vs. Balanced Scorecard?

---

## ⬜ 29. Strategieumsetzung Krankenhaus *(C6, Spoke, P3)*

- **Fokuskeyword:** strategieumsetzung (80 SV, Know)
- **Sekundär:** strategie krankenhaus, strategieumsetzung krankenhaus, zielkaskade, strategy deployment
- **H1:** Strategieumsetzung im Krankenhaus: Von der Vision bis zur Stationsebene
- **Plan-Slug:** `hoshin-kanri/strategieumsetzung-krankenhaus`
- **Meta Title:** Strategieumsetzung im Krankenhaus | Lean Hospital
- **Meta Description:** Warum Klinikstrategien im Alltag versanden – und wie Zielkaskaden, Beteiligung und Innovationsräume die Strategieumsetzung wirksam machen.
- **Interne Links:** → Hub #28; → Change Management (#7), Daily Management (#2)
- **CTA:** Kontaktformular am Ende → LinkedIn-Kontakt sekundär

**Briefing:** **ABGRENZUNG ZUM HUB BEACHTEN:** #28 = Methode generisch erklärt; diese Seite = Umsetzungs-How-to
spezifisch fürs Krankenhaus, Methode wird nur referenziert. Warum Strategien versanden (Strategie-Papier vs.
Stationsalltag; quotable) → die Zielkaskade Vorstand→Klinik→Abteilung→Station als Kern-Chunk → Beteiligung statt
Top-down: Innovationsräume am Universitätsklinikum Heidelberg als ausführliches Praxisbeispiel → Review-Rhythmen
(Monats-/Quartals-Reviews) → typische Fehler (zu viele Ziele, keine Messgrößen). **Entities:**
Universitätsklinikum Heidelberg, Zielkaskade, Innovationsräume, OKR (kurze Abgrenzung).
**FAQ:** Warum scheitert Strategieumsetzung? / Was ist eine Zielkaskade? / Wie beteiligt man Mitarbeitende?

---

## ⬜ 30. Klinisches Risikomanagement *(C6, Spoke, P3)*

- **Fokuskeyword:** klinisches risikomanagement (20 SV, Know)
- **Sekundär:** risikomanagement krankenhaus, cirs, patientensicherheit, risikomanagement pflege
- **H1:** Klinisches Risikomanagement: Patientensicherheit systematisch verankern
- **Plan-Slug:** `hoshin-kanri/klinisches-risikomanagement`
- **Meta Title:** Klinisches Risikomanagement: CIRS & Co. | Lean Hospital
- **Meta Description:** Klinisches Risikomanagement erklärt: gesetzliche Pflichten, CIRS, Methoden wie FMEA – und warum Lean und Risikomanagement zusammengehören.
- **Interne Links:** → Hub #28; → KVP (#10), Schichtübergabe (#23)
- **CTA:** LinkedIn-Kontakt am Ende → kein Produkt-CTA

**Briefing:** Definitionsblock → rechtlicher Rahmen (§ 136a SGB V, G-BA-QM-Richtlinie — **Stand verifizieren**) →
Instrumente je als Chunk: CIRS (anonymes Fehlermeldesystem), M&M-Konferenzen, FMEA, Sicherheits-Checklisten (WHO
Surgical Safety Checklist) → Lean × Risikomanagement: stabile Standards senken Risiko, Verschwendung erzeugt
Risiko (quotable) → Sicherheitskultur statt Schuldkultur (Just Culture) → Einführung in 5 Schritten.
**Entities:** CIRS, § 136a SGB V, G-BA, FMEA, WHO Surgical Safety Checklist, Aktionsbündnis Patientensicherheit,
Just Culture. **FAQ:** Was ist klinisches Risikomanagement? / Ist es Pflicht? / Was ist CIRS?

> Querverweis: die bestehenden Posts zur OP-Sicherheitscheckliste und zur Keystone-Checkliste sind hier die
> naheliegenden `read_more_links`.

---

## ⬜ 31. Magnetkrankenhaus *(C7, Spoke, P3)*

- **Fokuskeyword:** magnetkrankenhaus (100 SV, Know)
- **Sekundär:** magnet hospital, magnet krankenhaus deutschland, magnet recognition program, magnet4europe
- **H1:** Magnetkrankenhaus: Was das Magnet-Konzept aus den USA für Pflege und Klinik bedeutet
- **Plan-Slug:** `international/magnetkrankenhaus`
- **Meta Title:** Magnetkrankenhaus: Konzept & Kriterien | Lean Hospital
- **Meta Description:** Was ist ein Magnetkrankenhaus? Das US-Konzept für exzellente Pflege, die Kriterien der Magnet-Anerkennung und der Stand in Deutschland.
- **Interne Links:** → Pillar; → Lean Pflege (#20), Lean Healthcare USA (#32)
- **CTA:** LinkedIn-Kontakt am Ende → kein Produkt-CTA

**Briefing:** Definitionsblock (Magnetkrankenhaus = Klinik, die Pflegekräfte anzieht und hält wie ein Magnet) →
Herkunft (ANCC Magnet Recognition Program, USA 1980er-Pflegenotstand) → die 5 Magnet-Modellkomponenten als Liste
(Transformational Leadership, Structural Empowerment, Exemplary Professional Practice, New Knowledge, Empirical
Outcomes) → belegte Effekte (Personalbindung, Outcomes — **Studienlage verifizieren, z. B. Aiken**) → Stand in
Deutschland/Europa (Magnet4Europe, beteiligte deutsche Kliniken **verifizieren**) → Verbindung zu Lean: beide
setzen auf Befähigung und Shared Governance. **Entities:** ANCC, Magnet Recognition Program, Magnet4Europe,
Linda Aiken, Shared Governance. **FAQ:** Was ist ein Magnetkrankenhaus? / Welche Kriterien? / Gibt es welche in
Deutschland?

---

## ⚠️ 32. Lean Healthcare USA *(C7, Spoke, P3)*

> **Überschneidung:** „Was Virginia Mason und ThedaCare über Lean im Krankenhaus bewiesen haben" (24.06.2026)
> deckt beide Hauptfälle bereits ab. **Empfehlung:** #32 streichen und den Bestandspost als USA-Artikel führen —
> oder #32 auf das verengen, was dort fehlt (Cleveland Clinic, IHI, die „was ist übertragbar"-Gegenüberstellung
> DRG vs. US-Vergütung, die 5 übertragbaren Lektionen).

- **Fokuskeyword:** lean healthcare usa (0 SV — reiner GEO-/Autoritäts-Artikel)
- **Sekundär:** virginia mason, thedacare, lean hospital usa, virginia mason production system
- **Meta Title (Vorlage):** Lean Healthcare USA: Virginia Mason & Co | Lean Hospital
- **Entities:** Virginia Mason Production System, Gary Kaplan, ThedaCare, John Toussaint, IHI, Toyota.
- **FAQ:** Welche US-Kliniken sind Lean-Vorreiter? / Was ist das Virginia Mason Production System? / Lässt sich
  US-Lean auf deutsche Kliniken übertragen?
