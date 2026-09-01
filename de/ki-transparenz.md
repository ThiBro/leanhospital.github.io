---
title: KI-Transparenz
layout: about
lang: de
permalink: /de/ki-transparenz/
translation_url: /ai-transparency/
description: "KI-Transparenz auf lean-hospital.de: welche Texte und Bilder von künstlicher Intelligenz stammen, wie sie gekennzeichnet sind und wer die redaktionelle Verantwortung trägt."
hero:
  title: KI-Transparenz
  subtitle: Was auf diesem Blog von künstlicher Intelligenz stammt — und wie Sie es erkennen
---

**Das Wichtigste in Kürze:** Die Artikel auf lean-hospital.de entstehen mit Unterstützung von KI-Sprachmodellen, die Titelbilder sind überwiegend KI-generierte Illustrationen. Jeder Artikel sagt das an drei Stellen selbst: als Kennzeichnung oben in der Artikelzeile, als Markierung auf einem KI-generierten Titelbild und als ausführlicher Kasten am Ende des Textes. Zusätzlich trägt jede Artikelseite eine maschinenlesbare Kennzeichnung im Quelltext. Die redaktionelle Verantwortung für jeden veröffentlichten Artikel liegt bei Martin Neumann.

## Was künstliche Intelligenz auf diesem Blog macht

**Texte.** Die Artikel werden mit einem KI-Sprachmodell entworfen und ausformuliert. Das Modell arbeitet gegen ein festes Regelwerk: Struktur, Zielgruppe, Tonalität und Quellenanforderungen sind vorgegeben.

**Bilder.** Die Titelbilder der meisten Artikel sind KI-generierte Editorial-Illustrationen (Modell `gpt-image-1`). Sie zeigen symbolische Szenen — eine Notaufnahme, eine Übergabe, eine Checkliste — ohne reale Personen, reale Orte und reale Geräte. Zeigt ein Artikel dagegen ein konkretes Dashboard, ist das Titelbild eine echte Bildschirmaufnahme der laufenden Anwendung.

**Auch diese Seite** ist mit KI-Unterstützung entstanden und von Martin Neumann geprüft und freigegeben.

## Was ein Mensch macht

Martin Neumann gibt jeden Artikel vor der Veröffentlichung frei. Dazu gehört:

- **Quellen prüfen.** Jede Zahl und jede Aussage, die auf eine Studie, ein Gesetz oder eine Verordnung zurückgeht, wird gegen die Originalquelle geprüft. Die Quellen stehen am Ende jedes Artikels mit auflösender URL.
- **Fachlich einordnen.** Ob eine Methode im deutschen Klinikalltag trägt, entscheidet die Praxiserfahrung, nicht das Modell.
- **Verantworten.** Für den veröffentlichten Inhalt haftet Martin Neumann als Anbieter dieses Blogs. Die Angaben dazu stehen im [Impressum](/de/impressum/).

Was ein KI-Modell hier **nicht** darf: Zahlen schätzen, Studien erfinden, Zitate konstruieren. Lässt sich eine Angabe nicht belegen, fällt sie aus dem Artikel heraus.

## Wie ein Artikel gekennzeichnet ist

Jeder Artikel trägt die Kennzeichnung an drei Stellen, damit sie auch beim Überfliegen ankommt:

1. **In der Artikelzeile ganz oben** steht neben Datum und Lesezeit die Kennzeichnung „KI-Kennzeichnung". Sie führt direkt zum ausführlichen Kasten.
2. **Auf einem KI-generierten Titelbild** liegt die Markierung „KI-generiertes Bild" — sichtbar, sobald das Bild zu sehen ist.
3. **Am Ende des Artikels** steht der Kasten „KI-Kennzeichnung: Wie dieser Artikel entstanden ist" mit je einer Angabe für Text und Bild.

Ein Artikel, dessen Text vollständig ohne KI entstanden ist, sagt das im selben Kasten. Die Kennzeichnung fehlt also nie — sie sagt nur etwas anderes.

## Die maschinenlesbare Kennzeichnung

Artikel 50 Absatz 2 der KI-Verordnung verlangt, dass KI-erzeugte Inhalte **maschinenlesbar** als solche erkennbar sind. Auf jeder Artikelseite steht dafür im Kopfbereich des Quelltextes:

```html
<meta name="ai-disclosure" content="text=ai-generated; image=ai-generated">
<meta name="ai-disclosure-policy" content="https://lean-hospital.de/de/ki-transparenz/">
<meta name="ai-generated" content="true">
```

Dazu kommt ein JSON-LD-Block, der den **IPTC Digital Source Type** benutzt — die eingeführte Werteliste dafür, wie ein Medium entstanden ist:

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

Die verwendeten Werte:

| Wert | Bedeutung |
|---|---|
| `trainedAlgorithmicMedia` | Von einem trainierten KI-Modell erzeugt |
| `compositeWithTrainedAlgorithmicMedia` | Echte Aufnahme, mit KI-Werkzeugen nachbearbeitet |
| `softwareImage` | Echte Bildschirmaufnahme einer laufenden Anwendung |
| `digitalCapture` | Echte Fotografie |

Zusätzlich trägt jedes Titelbild im Quelltext die Attribute `data-ai-generated` und `data-digital-source-type`, sodass sich die Herkunft auch am Bild selbst ablesen lässt.

## Der rechtliche Rahmen

Grundlage ist **Artikel 50 der Verordnung (EU) 2024/1689** über künstliche Intelligenz, kurz KI-Verordnung oder AI Act. Er ist seit dem **2. August 2026** anwendbar und verlangt zweierlei:

- **Absatz 2:** Wer ein KI-System betreibt, das synthetische Bilder, Texte, Audio- oder Videoinhalte erzeugt, sorgt dafür, dass die Ausgaben maschinenlesbar als künstlich erzeugt markiert sind.
- **Absatz 4:** Wer KI-erzeugte oder KI-veränderte Texte veröffentlicht, um die Öffentlichkeit über Angelegenheiten von öffentlichem Interesse zu informieren, legt das offen.

Absatz 4 kennt eine Ausnahme für Inhalte, die redaktionell geprüft wurden und für die eine natürliche oder juristische Person die Verantwortung trägt. Auf lean-hospital.de wäre diese Ausnahme anwendbar — **wir berufen uns bewusst nicht darauf.** Wer über Prozesse im Krankenhaus liest, soll wissen, wie der Text entstanden ist.

## Häufige Fragen zur KI-Kennzeichnung

### Sind die Zahlen in den Artikeln von einer KI erfunden?

Nein. Jede Zahl geht auf eine benannte Quelle zurück, die am Ende des Artikels mit auflösender URL steht. Angaben ohne belegbare Quelle werden gestrichen, statt sie mit einer Schätzung zu füllen.

### Woran erkenne ich, ob ein Bild echt ist?

Ein KI-generiertes Titelbild trägt die sichtbare Markierung „KI-generiertes Bild" in der oberen rechten Ecke. Der Kasten am Ende des Artikels benennt die Herkunft ausdrücklich, und im Quelltext steht sie maschinenlesbar am Bild selbst.

### Gilt die Kennzeichnung auch für ältere Artikel?

Ja. Alle bereits veröffentlichten Artikel wurden nachträglich gekennzeichnet, jeder einzeln nach seiner tatsächlichen Entstehung.

### Wer haftet für den Inhalt?

Martin Neumann als Anbieter dieses Blogs. Die Angaben nach § 5 DDG stehen im [Impressum](/de/impressum/).

## Einen Fehler gefunden?

Wenn Ihnen in einem Artikel eine falsche Zahl, eine falsche Quellenangabe oder eine fehlende Kennzeichnung auffällt: Schreiben Sie an **kontakt@lean-hospital.de**. Korrekturen werden im Artikel nachgezogen und im Änderungsdatum sichtbar.
