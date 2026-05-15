---
layout: post
title: Greenfields Dairy Tagesertrags-Dashboard - Gesundheitsprobleme früh erkennen
date: 2026-05-13 00:00:00 +0000
tags: production
image: /assets/2026-05-13-15-08-52/title.jpg
bg_alternative: true
description: Ein wandmontiertes Dashboard für den Milchviehbetrieb, das das tägliche Melkprotokoll in einen Auf-einen-Blick-Gesundheits- und Ertragsmonitor verwandelt.
prompt: |
  Erstelle ein Dashboard für einen Milchviehbetrieb, das die tägliche Milchleistung pro Kuh visualisiert, aufgeschlüsselt nach Herdengruppe und Melkzeit (morgens/abends). Füge eine große KPI-Kachel hinzu, die die Gesamtliter heute im Vergleich zum 7-Tage-Durchschnitt zeigt, ein Balkendiagramm der Top-10-produzierenden Kühe sowie ein Liniendiagramm, das den Herdendurchschnitt der letzten 30 Tage anzeigt. Ergänze einen Heatmap-Kalender, der die Tagessummen des aktuellen Monats zeigt, damit der Betriebsleiter schnell Einbrüche erkennen kann, die auf gesundheitliche Probleme hindeuten.
downloads:
- name: Peakboard.pbmx
  url: /assets/2026-05-13-15-08-52/Peakboard.pbmx
lang: de
permalink: /de/greenfields-dairy-daily-yield-dashboard-spotting-health-dips-before-they-become-problems/
translation_url: /en/greenfields-dairy-daily-yield-dashboard-spotting-health-dips-before-they-become-problems/
---

{% include youtube.html id="DcvQmngPF3I" %}

Einen Milchviehbetrieb zu führen ist ein Zahlenspiel, das zweimal täglich gespielt wird, jeden Tag, ohne Ausnahme. Auf der Greenfields Dairy laufen 68 Kühe, aufgeteilt in die Herdengruppen Holstein, Jersey und Guernsey, durch die morgendliche und abendliche Melkschicht, und die Liter jeder Kuh werden von Hand erfasst. Die Herausforderung besteht darin, aus diesem wachsenden Stapel an Melkdaten etwas zu machen, mit dem der Betriebsleiter tatsächlich arbeiten kann, idealerweise bevor aus einem kleinen Ertragsrückgang eine Tierarztrechnung wird. Genau das leistet dieses Dashboard.

![Greenfields Dairy Hauptansicht](/assets/2026-05-13-15-08-52/010.png)

## Die Haupt-KPI beantwortet die meistgestellte Frage auf dem Hof

Wer morgens in ein Milchviehbüro kommt, hört immer dieselbe Frage: "Wie viel haben wir gemolken?" Die große Kachel links auf dem Dashboard beantwortet sie, ohne dass jemand eine Tabelle öffnen muss. Die heutige Gesamtmenge steht bei **1.847,5 Litern**, knapp über dem rollierenden 7-Tage-Durchschnitt von 1.792,3 L, mit einem grünen **+3,1%**-Delta, das "wir sind auf Kurs" zu einer Ein-Sekunden-Entscheidung macht.

Zwei unterstützende KPIs liegen darunter: 68 aktive Kühe und ein Durchschnitt von 27,2 Litern pro Kopf. Die Headline-Zahl in "wie viele Tiere wurden gemolken" und "wie viel hat jedes gegeben" aufzuteilen, ist der Trick, der einen normalen Tag von einem alarmierenden trennt. Ein Rückgang der Gesamtliter bei gleichbleibendem Pro-Kopf-Schnitt bedeutet, dass eine Kuh aus der Rotation ist. Ein Rückgang des Pro-Kopf-Schnitts bei gleicher Tieranzahl bedeutet, dass in der Herde selbst etwas passiert.

## Top 10 Milchgeber, sortiert und farbcodiert

Das Balkendiagramm oben rechts listet die heute leistungsstärksten Milchgeber. **Bella #214**, **Daisy #107** und **Buttercup #318** führen das Feld an, in gestaffelten Grüntönen eingefärbt, damit das Auge zuerst oben auf der Liste landet. Für einen Herdenmanager hat diese Liste eine Doppelfunktion: Sie identifiziert die Kandidatinnen für das Zuchtprogramm und die wertvollen Tiere, die man im Blick behalten sollte, aber sie kennzeichnet auch das stille Versagen, das Papierprotokolle übersehen, den Moment, in dem eine sonst stets führende Kuh aus der Bestenliste fällt.

![Top-Milchgeber und 30-Tage-Trend](/assets/2026-05-13-15-08-52/020.png)

## Der 30-Tage-Trend zeigt, was die Tagessumme verbirgt

Unter der Bestenliste zeichnet ein 30-Tage-Liniendiagramm den Herdendurchschnitt pro Kuh nach, mit einer pfirsichfarbenen Linie für die Morgenschicht und einer violetten für den Abend. Das Diagramm lässt den V-förmigen Einbruch am **8. und 9. Mai** klar erkennbar stehen, mit einem Tief von 22,7 L pro Kuh kombiniert. Darunter spricht eine Status-Notiz Klartext: "Health-dip alert: May 8 to 9, herd average dropped 5.5L. Investigate Holstein group."

Das ist die Art von Muster, die in Papierprotokollen schlicht nicht überlebt. Ein einzelner schlechter Tag sieht nach einem schlechten Tag aus. Zwei schlechte Tage in Folge, isoliert in einer Rassegruppe, sehen nach Mastitis, Lahmheit, Hitzestress oder einem sich anbahnenden Futterproblem aus. Das Liniendiagramm verwandelt dieses Muster in etwas, das der Manager noch vor dem Morgenkaffee bemerkt.

## Der Heatmap-Kalender bringt einen Monat Melken auf einen Bildschirm

Auf der rechten Seite wird der aktuelle Monat als Raster farbiger Kacheln dargestellt. Bernstein für niedrige Erträge, gestaffelte Grüntöne für normale Erträge und ein harter **Rot-Alarm am 9. Mai**, an dem das Auge unweigerlich hängenbleibt. Die heutige Kachel, der **13. Mai**, erhält eine pfirsichfarbene Umrandung, damit der Manager immer weiß, wo er im Zyklus steht. Beim Antippen eines Tages öffnet sich ein Detaildialog mit der Tagessumme, der Aufteilung Morgen vs. Abend und dem Vergleich gegen den 7-Tage-Durchschnitt, sodass der Weg von "in der Heatmap sieht etwas seltsam aus" zu einer konkreten Zahl genau einen Tap dauert.

![Melkung-erfassen-Dialog und Kalender](/assets/2026-05-13-15-08-52/030.png)

## Erfassung aus dem Melkstand, nicht vom Schreibtisch

Das Dashboard ist nicht nur ein Anzeigeprogramm. Der prominente **Log Milking**-Button im Header öffnet einen Dialog, den das Melkpersonal direkt nutzt: Kuhname oder Ohrmarke, Herdengruppe, Schicht (morgens oder abends) und Liter über einen 0-bis-50-L-Schieberegler mit 5-L-Schritten. Der Eintrag wird an eine gemeinsame `dairyfarm_milklog`-Liste auf dem Peakboard Hub angehängt, sodass jedes Display auf dem Hof, die Bürowand, der Flur zwischen Melkstand und Milchtank, das Tablet im Melkgraben, die neue Zeile sofort sieht.

Eine zweite Hub-gestützte Liste, `dairyfarm_healthalerts`, gibt dem besuchenden Tierarzt einen Weg, Alarme zurück in dasselbe Ökosystem zu schicken. Und weil der Herdenfilter oben (All / Holstein / Jersey / Guernsey) über MQTT zwischen allen Dairy-Boards geteilt wird, folgt das Bürodisplay automatisch, wenn der Nachtmanager am Melkstand-Bildschirm auf "Jersey" umschaltet. Ein Filter, ein Hof.

## Ergebnis

Was früher ein Klemmbrett-Ritual war, ist jetzt ein arbeitender Betriebsbildschirm. Der Betriebsleiter sieht die heutige Gesamtmenge, die heutigen Spitzenreiter, den 30-Tage-Trend und den Monat-auf-einen-Blick-Kalender, ohne eine einzige Datei zu öffnen. Der Einbruch vom 8. auf den 9. Mai ist keine nachträgliche Entdeckung mehr, sondern eine sichtbare rote Kachel und ein geschriebener Alarm, der auf die Holstein-Gruppe zeigt. Für einen Hof, auf dem die Spanne zwischen einer gesunden und einer kranken Kuh in Tagen gemessen wird, ist genau dieser Vorsprung der eigentliche Sinn des Boards.
