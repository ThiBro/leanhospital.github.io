---
layout: post
title: Steuerungs-Dashboard für eine Recycling-Sortieranlage – Der Materialüberblick mit Peakboard
date: 2026-07-01 00:00:00 +0000
tags: energy production
image: /assets/2026-07-01-10-14-11/title.jpg
bg_alternative: true
description: "Tonnagen, Reinheitsgrade, Durchsatz, Bunkerfüllstände und Marktpreise einer Recycling-Sortieranlage auf einem einzigen großformatigen Leitstand-Bildschirm zusammenführen."
prompt: |
  Entwirf ein Dashboard für eine Recycling-Sortieranlage, das die Tonnage
  nach Materialkategorie (Papier, Kunststoff, Glas, Metall, Bioabfall) für
  den aktuellen Tag und die Woche anzeigt. Stelle die Reinheitsgrade je
  Stoffstrom als Rundinstrumente dar, ergänze ein Liniendiagramm für den
  stündlichen Durchsatz sowie ein Füllstandsdiagramm für jeden Ausgabe-Silo.
  Füge einen Marktpreis-Ticker hinzu, der die aktuellen Erlöse pro Tonne für
  die sortierten Ausgabematerialien zeigt.
downloads:
  - name: Peakboard.pbmx
    url: /assets/2026-07-01-10-14-11/Peakboard_de.pbmx
lang: de
permalink: /de/recycling-sorting-facility-control-dashboard/
translation_url: /en/recycling-sorting-facility-control-dashboard/
---
{% include youtube.html id="U_hl-4GrJ8M" %}


Eine moderne Sortieranlage (MRF, Material Recovery Facility) nimmt gemischte Abfälle auf und macht daraus wieder saubere, vermarktbare Fraktionen: Papier, Kunststoff, Glas, Metall und Bioabfall. Ob dieser Betrieb rentabel und regelkonform läuft, hängt an einer Handvoll Kennzahlen, die jederzeit sichtbar sein müssen – wie viel Material durch die Anlage läuft, wie sauber jeder sortierte Stoffstrom ist, wie voll die Ausgabesilos sind und was jede Fraktion aktuell am Rohstoffmarkt wert ist. In diesem Beitrag bringen wir all das auf einen einzigen Großbildschirm, sodass die gesamte Sortierhalle den Zustand der Linie auf einen Blick ablesen kann.

## Für wen das Board gedacht ist

Das Dashboard richtet sich an die Menschen in der Sortierhalle: Schichtführer, Anlagenverantwortliche und Qualitätsmanager – dazu die Betriebsleitung, die sich schnell ein Bild vom Zustand der Linie machen will, ohne einzelne SCADA-Masken zu öffnen. Es ist als Wandanzeige im Leitstand oder über der Sortierkabine konzipiert und läuft im Dauerbetrieb auf einem 1920x1080-Bildschirm. Das Team überwacht die gesamte Anlage von einem Ort aus, statt zwischen mehreren Steuerungsbildschirmen zu wechseln.

![Übersicht des Dashboards für die Recycling-Sortieranlage](/assets/2026-07-01-10-14-11/de_010.png)

## Tonnage: Wie viel haben wir sortiert?

Der obere Bereich des Boards beantwortet die erste betriebliche Frage, die sich jede Schicht stellt. Jede Materialkategorie erhält eine eigene Kachel, die die sortierte Tonnage für den **aktuellen Tag** neben der laufenden **Wochensumme** zeigt. Diese Gegenüberstellung lässt Bediener sofort erkennen, ob der Durchsatz im Plan liegt oder hinterherhinkt – ganz ohne Kopfrechnen.

## Reinheitsgrade als Rundinstrumente

Unter den Tonnage-Kacheln meldet eine Reihe kreisförmiger Instrumente den **Reinheitsgrad je Stoffstrom**. Das ist die wichtigste Qualitätskennzahl im Recycling überhaupt: Verunreinigte Ballen verlieren an Wert oder werden vom Abnehmer schlicht abgelehnt. Die Darstellung der Reinheit als Rundinstrument macht einen Stoffstrom außerhalb der Spezifikation sofort sichtbar, sodass ein Qualitätsmanager reagieren kann, bevor eine ganze Charge verdorben ist.

## Stündlicher Durchsatz

Ein Liniendiagramm zum stündlichen Durchsatz zeigt den Rhythmus der Linie über den Tag. Stillstände, Anlaufphasen und ungewöhnliche Einbrüche schlagen sich als Formänderungen in der Kurve nieder – so lässt sich ein Rückgang der Ausbringung leicht mit einem Ereignis in der Halle in Verbindung bringen.

![Bunkerfüllstände und Marktpreis-Ticker](/assets/2026-07-01-10-14-11/de_020.png)

## Bunkerfüllstände

Rechts zeigt ein hohes Füllstandsdiagramm den aktuellen Füllstand jedes Ausgabesilos als senkrechten Balken mit Prozentanzeige. Dieser Teil des Bildschirms verhindert das teuerste Problem einer Sortierlinie: einen überlaufenden oder verstopften Bunker, der einen ungeplanten Stopp erzwingt. Wer sieht, dass ein Silo auf „voll“ zusteuert, kann rechtzeitig einen Ballenpress- oder Abtransportlauf einplanen, bevor es kritisch wird.

Jede Silo-Beschriftung ist antippbar. Eine Berührung öffnet einen Detaildialog mit Kapazitäts- und Füllstandsangaben für genau diesen Bunker – ein genauerer Blick, ohne die Übersicht zu verlassen. Eine deutliche Schaltfläche **Schließen** blendet den Dialog wieder aus und führt zurück zum vollständigen Board.

## Marktpreis-Ticker

Am unteren Rand läuft ein scrollender Marktpreis-Ticker, der den aktuellen Erlös pro Tonne für jedes sortierte Ausgabematerial zeigt. Er verbindet das betriebliche Bild mit dem kaufmännischen: Wenn die Preise für Stahl oder PET nach oben schießen, weiß das Team, welche Stoffströme sich gerade zu priorisieren lohnen – aus einem reinen Überwachungsbildschirm wird so ein kleines Werkzeug zur Entscheidungsunterstützung.

## Ergebnis

Die Interaktion ist bewusst zurückhaltend und für die Bedienung per Touch ausgelegt. Der Bildschirm ist überwiegend ein passiver Monitor, doch die antippbaren Silo-Beschriftungen erlauben es einem interessierten Bediener, in einen einzelnen Bunker einzutauchen und den Dialog ebenso schnell wieder zu schließen. Das Ergebnis ist ein großformatiges Board, das Tonnage, Qualität, Durchsatz, Silokapazität und Marktwert gleichzeitig im Blick behält – damit die Sortierhalle die Anlage auf Basis von Fakten statt Vermutungen fahren kann.