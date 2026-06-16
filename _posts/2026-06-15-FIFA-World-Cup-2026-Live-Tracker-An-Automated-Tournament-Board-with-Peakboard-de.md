---
layout: post
title: FIFA WM 2026 Live-Tracker – Ein automatisches Turnierboard mit Peakboard
date: 2026-06-15 00:00:00 +0000
tags: office
image: /assets/2026-06-15-13-20-25/title.jpg
bg_alternative: true
description: "Ein sich selbst aktualisierendes Digital-Signage-Board für die FIFA WM 2026, das die echten Gruppen und Live-Ergebnisse über eine kostenlose, schlüsselfreie Online-API abruft und Tabellen sowie K.-o.-Baum eigenständig neu berechnet."
prompt: |
  Erstelle ein Digital-Signage-Board für die FIFA WM 2026, das automatisch die echten Gruppen und Ergebnisse über eine frei verfügbare Online-API ohne Schlüssel anzeigt. Es soll zwei Screens geben: eine Gruppenphase mit Tabellen für alle zwölf Gruppen (A bis L) inklusive Länderflaggen und Punkten sowie eine K.-o.-Phase als richtigen Turnierbaum vom Sechzehntelfinale bis zum Finale. Tabelle, Tordifferenz und Platzierung sollen aus den Spielergebnissen berechnet und bei jeder Aktualisierung neu aufgebaut werden.
downloads:
  - name: Peakboard.pbmx
    url: /assets/2026-06-15-13-20-25/Peakboard_de.pbmx
lang: de
permalink: /de/fifa-world-cup-2026-live-tracker/
translation_url: /en/fifa-world-cup-2026-live-tracker/
---

Sobald ein großes Turnier ansteht, will plötzlich jedes Büro, jede Sportsbar und jede Fanzone die Tabellen an der Wand hängen haben. Das Problem dabei: Eine Wandanzeige während eines vierwöchigen Events mit 48 Teams, zwölf Gruppen und 104 Spielen von Hand aktuell zu halten, ist mühsam und fehleranfällig. In diesem Artikel bauen wir ein Board, das einem genau diese Arbeit komplett abnimmt: einen vollautomatischen Tracker für die FIFA WM 2026, der unbeaufsichtigt auf einem großen Bildschirm läuft und immer den echten Stand zeigt.

## Das Problem, das es löst

Ein Turnierboard verdient sich seinen Platz an der Wand nur, wenn es korrekt bleibt, ohne dass jemand eingreifen muss. Ergebnisse nach jedem Spiel von Hand einzutippen und Tabellen neu zu sortieren ist genau die Art von Fleißarbeit, die niemand machen möchte – und ein einziges verpasstes Update lässt die ganze Anzeige veraltet wirken.

Dieses Board nimmt einem diese Arbeit ab. Es holt die echte Auslosung und die Live-Ergebnisse aus einem kostenlosen, frei verfügbaren WM-Datenfeed (ohne API-Schlüssel) und berechnet alles selbst. Tabellenstand, Tordifferenz und Platzierung werden komplett aus den Spielergebnissen abgeleitet und bei jeder Aktualisierung neu aufgebaut, sodass das Bild an der Wand stets der Realität entspricht.

![Übersicht der WM-Gruppenphase](/assets/2026-06-15-13-20-25/de_010.png)

## Die Gruppenphase auf einen Blick

Der erste Screen zeigt die Gruppenphase: alle zwölf Gruppen von A bis L, jede als kompakte Karte mit Länderflaggen, Platzierung und Punkten. Die Idee dahinter ist, dass sich jede Gruppe in wenigen Sekunden auch quer durch den Raum ablesen lässt, sodass ein Vorbeigehender im Vorbeigehen checken kann, wo sein Team steht.

Da die Tabelle aus den Ergebnissen berechnet und nicht von Hand gepflegt wird, spiegeln die Karten immer die neuesten Spiele wider. Sobald neue Ergebnisse aus dem Feed eintreffen, ordnen sich Punkte und Positionen automatisch neu.

![Gruppenkarten mit Flaggen und Punkten](/assets/2026-06-15-13-20-25/de_020.png)

## Der K.-o.-Baum

Der zweite Screen zeigt die K.-o.-Phase als richtigen Turnierbaum, der vom Sechzehntelfinale bis zum Finale Stück für Stück wächst. Als echter Turnierbaum angelegt, lässt sich auf einen Blick erkennen, wer gegen wen spielt und wie sich der Weg zum Titel mit jeder Runde abzeichnet.

![K.-o.-Baum vom Sechzehntelfinale bis zum Finale](/assets/2026-06-15-13-20-25/de_030.png)

## Auf einen Blick lesbar gebaut

Die Bedienung ist bewusst minimal gehalten. Das Board ist darauf ausgelegt, aus der Distanz gelesen zu werden, und wechselt mit einem einzigen Tipp zwischen Gruppenphase und K.-o.-Baum. Das passt zu einem wandmontierten Touchscreen genauso gut wie zu einer passiven Anzeige, die auf einem Timer läuft – und macht es zur idealen Lösung für Büros, Sportsbars, Fanzonen, Betriebskantinen oder Empfangsbereiche.

## Ergebnis

Das fertige Board ist eine aufgeräumte, gebrandete Fußball-Übersicht, die sich um sich selbst kümmert. Es bezieht die echten Gruppen und Live-Ergebnisse aus einem kostenlosen Online-Feed, berechnet die Tabellen bei jeder Aktualisierung neu und zeigt sowohl die zwölf Gruppentabellen als auch den kompletten K.-o.-Baum in einem Format, das jeder auf einen Blick erfassen kann. Einmal einrichten, an die Wand hängen – und es begleitet die gesamte WM 2026 ganz von allein.