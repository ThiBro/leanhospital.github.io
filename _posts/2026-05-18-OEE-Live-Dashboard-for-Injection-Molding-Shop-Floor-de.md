---
layout: post
title: OEE Live Dashboard für die Spritzguss-Fertigung
date: 2026-05-18 00:00:00 +0000
tags: production
image: /assets/2026-05-18-14-35-10/title.jpg
bg_alternative: true
description: "Ein wandmontiertes OEE-Cockpit für eine Spritzgießerei mit acht Pressen, das Verfügbarkeit, Leistung und Qualität in konkrete Aktionen verwandelt."
prompt: |
  Erstelle ein Overall-Equipment-Effectiveness-Dashboard für einen Spritzgussbetrieb mit acht Maschinen. Zeige OEE, Verfügbarkeit, Leistung und Qualität pro Maschine als Tachoanzeigen sowie ein gestapeltes Balkendiagramm mit geplanten und ungeplanten Stillstandszeiten nach Grundcode für die aktuelle Schicht. Ergänze einen scrollenden Ticker am unteren Rand, der die letzten zehn Qualitätsausschüsse mit Teilenummer und Bediener auflistet.
downloads:
  - name: Peakboard.pbmx
    url: /assets/2026-05-18-14-35-10/Peakboard_de.pbmx
lang: de
permalink: /de/oee-live-dashboard-for-injection-molding-shop-floor/
translation_url: /en/oee-live-dashboard-for-injection-molding-shop-floor/
---
{% include youtube.html id="kh13E6QQGUg" %}


Wer an einem beliebigen Dienstag durch eine Spritzgießerei läuft, hört zwischen Produktionsleiter und Schichtführer immer dieselbe Frage: Schaffen wir gerade die Zahlen, und wenn nicht, welche Presse zieht uns runter? Acht Maschinen, drei Schichten, Dutzende Teilenummern und hundert Möglichkeiten, Minuten zu verlieren - aus den einzelnen Maschinen-HMIs ergibt sich die Antwort selten von selbst. Dieses Dashboard macht sie sichtbar.

## Ein Bildschirm, acht Pressen, eine Wahrheit

Das Dashboard ist für eine große Wandanzeige in der Halle gedacht, so platziert, dass Maschinenführer, Schichtleiter und Produktionsleiter es quer durch die Halle ablesen können. Eine zweite Installation als Touchscreen-Kiosk neben dem Schichtbüro macht aus dem gleichen Bild einen interaktiven Arbeitsplatz, an dem ein Vorarbeiter jede Maschine antippen und in die Details springen kann.

Die acht Pressen reichen vom 110-Tonnen-Arbeitstier bis zum 1100-Tonnen-Brocken und sind als acht identische Kacheln angeordnet, damit das Auge nicht suchen muss. Jede Kachel zeigt die klassische Kennzahlen-Dreifaltigkeit der Fertigung plus die Gesamtbewertung: OEE, Verfügbarkeit, Leistung und Qualität, jeweils als Kreis-Gauge. Nebeneinander gestellt machen es diese vier kleinen Anzeigen jedem leicht, M01 in einem Blick mit M07 zu vergleichen.

![OEE-Dashboard-Übersicht mit acht Maschinenkacheln, Stillstandsdiagramm und Ausschuss-Ticker](/assets/2026-05-18-14-35-10/de_010.png)

Eine deutlich sichtbare Status-Pille neben jedem Maschinennamen wechselt von Grün (RUNNING) über Gelb (FAULT) auf Rot (DOWN). Auch quer durch die Halle melden die Farben Ärger, bevor irgendjemand eine Zahl ablesen muss. In den hier gezeigten Beispieldaten steht M04 mit mageren 42 Prozent OEE auf FAULT, und M06 ist mit null komplett ausgefallen. Genau das ist die Art Signal, die einen Bediener veranlassen sollte, sofort hinüberzulaufen, statt auf die nächste Reporting-Runde zu warten.

## Das Stillstands-Gespräch, fertig für die Schichtübergabe

Unter den acht Maschinenkacheln zerlegt ein gestapeltes Balkendiagramm die Stillstandszeit der laufenden Schicht nach Grundcode. Geplante Verluste (Werkzeugwechsel, geplante Wartung, Rüsten, Bedienerpausen) stapeln sich gegen ungeplante (Materialzufuhr-Probleme, Stromausfall, Qualitätssperren, fehlendes Material). Das ist der Gesprächseinstieg für jede Schichtübergabe: Wo haben wir Zeit verloren, und war der Verlust vermeidbar?

![Gestapeltes Balkendiagramm der Stillstände der aktuellen Schicht, aufgeschlüsselt nach Grundcode](/assets/2026-05-18-14-35-10/de_020.png)

Der Cycle-Shift-Button in der Kopfzeile schaltet ohne Seitenwechsel zwischen Day A, Day B und Nachtschicht um, sodass die ausgehende und die einkommende Crew den Tag gemeinsam durchgehen und genau sehen können, wie sich das Bild verändert hat.

## Qualität, im Augenwinkel aller Beteiligten

Das Band am unteren Rand ist ein durchgehend laufender Ticker, der die letzten zehn Qualitätsausschüsse mit Zeitstempel, Maschine, Teilenummer, Bedienername und Fehlergrund präsentiert. Er hält Qualitätsthemen im Augenwinkel aller Beteiligten lebendig, statt sie in einem Bericht zu vergraben, den ohnehin niemand öffnet. Wer einen Eintrag genau lesen will, hält den Lauf mit einem Pause-Button (oder einem Tipp auf den Ticker selbst) an, bis er fertig ist.

## Drill-down per Fingertipp

Die Interaktion lebt von ein paar bewussten Details, die den Kiosk erst wirklich nützlich machen. Ein Tipp auf eine der acht Maschinenkacheln öffnet einen großen modalen Dialog mit deutlich größeren Gauges, dem aktuell laufenden Teil und einer Acknowledge-Alert-Aktion, mit der die zuständige Technikerin oder der Techniker die Meldung quittieren und den Dialog schließen kann. Ein kleines Ritual, das aus einer passiven Wandanzeige ein echtes Übergabewerkzeug macht.

![Maschinen-Detaildialog mit vergrößerten Gauges und Quittierung](/assets/2026-05-18-14-35-10/de_030.png)

Eine Live-Uhr und ein Schicht-Badge runden die Kopfzeile ab, sodass jeder, der hochschaut, sofort weiß, welche Schichtzahlen er gerade sieht und wie viel davon noch übrig ist.

## Fazit

Was dieses Dashboard wirklich liefert, ist eine gemeinsame Sprache für eine laute Produktionshalle. Maschinenführer sehen ihre eigene Presse im Kontext, Schichtleiter sehen die ganze Bay, und der Produktionsleiter blickt vom Büro aus auf dieselbe einzige Wahrheit. Die Kennzahlen sind nicht neu - jeder Werkleiter kann OEE, Verfügbarkeit, Leistung und Qualität im Schlaf herunterbeten -, aber sie für acht Maschinen nebeneinander aufzustellen, mit Status-Pillen, einem nach Gründen aufgeschlüsselten Stillstandsdiagramm und einem Live-Ausschuss-Ticker, verwandelt eine tägliche Berichtsroutine in ein Lagebild im Minutentakt. Das ist der Unterschied zwischen der Zahl von gestern kennen und die Zahl von heute verändern.
