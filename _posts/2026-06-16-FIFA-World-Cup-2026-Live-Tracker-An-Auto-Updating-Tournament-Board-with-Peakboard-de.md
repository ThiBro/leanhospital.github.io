---
layout: post
title: FIFA Weltmeisterschaft 2026 Live-Tracker – Ein sich selbst aktualisierendes Turnier-Board mit Peakboard
date: 2026-06-16 00:00:00 +0000
tags: office
image: /assets/2026-06-16-10-19-49/title.jpg
bg_alternative: true
description: "Bauen Sie ein vollautomatisches Signage-Board zur FIFA-WM 2026, das die echten Gruppen und Live-Ergebnisse über eine kostenlose Online-API abruft und die Tabellen sowie den K.-o.-Baum von ganz allein neu berechnet."
prompt: |
  Erstelle ein digitales Signage-Board für die FIFA-Weltmeisterschaft 2026, das
  über eine frei verfügbare Online-API ohne Schlüssel automatisch die echten
  Gruppen und Ergebnisse anzeigt. Es soll zwei Screens geben: eine Gruppenphase
  mit Tabellen für alle zwölf Gruppen (A bis L) inklusive Länderflaggen und
  Punkten, sowie eine K.-o.-Phase, dargestellt als richtiger Turnierbaum vom
  Sechzehntelfinale bis zum Finale. Tabelle, Tordifferenz und Platzierung sollen
  aus den Spielergebnissen berechnet und bei jeder Aktualisierung neu aufgebaut
  werden.
downloads:
  - name: Peakboard.pbmx
    url: /assets/2026-06-16-10-19-49/Peakboard_de.pbmx
lang: de
permalink: /de/fifa-world-cup-2026-live-tracker/
translation_url: /en/fifa-world-cup-2026-live-tracker/
---
{% include youtube.html id="9r_vm5Qa5CI" %}


Ein vierwöchiges Turnier mit 48 Mannschaften, zwölf Gruppen und 104 Spielen ist wunderbar mitzuverfolgen – und ein Albtraum, wenn man es von Hand aktuell halten will. Wer schon einmal versucht hat, während eines großen Fußballturniers eine Tabelle auf Papier zu pflegen oder eine handgepflegte Folie an der Wand laufend zu korrigieren, kennt das Spiel: Jedes Ergebnis bedeutet neue Punkte, eine neue Tordifferenz, eine neue Platzierung – und wieder einmal Ausradieren und Neuschreiben. In diesem Artikel bauen wir ein Board, das Ihnen genau diese Arbeit für die FIFA-WM 2026 komplett abnimmt.

Die Idee ist denkbar einfach: Das Board zieht die echte Auslosung und die Live-Ergebnisse aus einem kostenlosen, frei verfügbaren WM-Datenfeed, berechnet jede Tabelle selbstständig neu und hält das Bild an der Wand stets im Einklang mit dem, was tatsächlich auf dem Platz passiert. Einmal eingerichtet, muss niemand mehr Hand anlegen.

## Wofür das Board gedacht ist

Es handelt sich um einen vollautomatischen Turnier-Tracker, der unbeaufsichtigt auf großen Bildschirmen läuft. Denken Sie an Büros, Sportsbars, Fanzonen, Kantinen oder Empfangsbereiche – überall dort, wo Menschen die WM auf einen Blick verfolgen wollen, ohne auf eine überladene TV-Übertragung starren zu müssen. Das Board ist so gestaltet, dass man es quer durch den Raum erfassen kann: klar, im eigenen Look gehalten und immer aktuell.

Die Zielgruppe ist jeder, der einen öffentlichen oder halböffentlichen Bildschirm betreibt und sich eine aufgeräumte Fußballübersicht statt einer hektischen Sendegrafik wünscht. Weil alles aus dem Live-Feed berechnet wird, läuft das Board nie aus dem Takt, und es gibt keine manuelle Dateneingabe, bei der etwas schiefgehen könnte.

![Übersicht der Gruppenphase der FIFA-WM 2026](/assets/2026-06-16-10-19-49/de_010.png)

## Der Gruppenphasen-Screen

Der erste Screen zeigt die Gruppenphase: alle zwölf Gruppen von A bis L, jede als kompakte Karte mit Länderflaggen, Platzierung und Punkten. Das Layout ist so aufgebaut, dass man den Stand einer einzelnen Gruppe in wenigen Sekunden ablesen und das gesamte Turnier mit ein paar Blicken mehr überfliegen kann.

Das Entscheidende an diesem Screen: Die Tabellen sind nicht fest hinterlegt. Tabelle, Tordifferenz und Platzierung werden allesamt aus den tatsächlichen Spielergebnissen abgeleitet und bei jeder Aktualisierung von Grund auf neu aufgebaut. Sobald ein Spiel beendet ist und der Feed sich aktualisiert, springen die Punkte um, die Tordifferenz wird neu berechnet, und die Teams sortieren sich von selbst in die korrekte Reihenfolge – ganz ohne Zutun.

![Gruppenkarten mit Flaggen, Punkten und Platzierung](/assets/2026-06-16-10-19-49/de_020.png)

## Der K.-o.-Baum

Der zweite Screen zeigt die K.-o.-Phase als richtigen Turnierbaum. Er wächst vom Sechzehntelfinale über das Achtelfinale, das Viertelfinale und das Halbfinale bis hin zum Finale, sodass man auf einen Blick sieht, wer gegen wen spielt und wie sich der Weg zum Titel abzeichnet.

Während sich die Gruppenphase entscheidet und Teams weiterkommen, füllt sich der Baum automatisch aus demselben Live-Feed. Das Ergebnis ist ein einziger Screen, der die gesamte Geschichte der K.-o.-Runden auf einen Blick erzählt – die natürliche Ergänzung zur Gruppenansicht und genau das, worum sich ein Publikum versammelt, sobald das Turnier in seine entscheidende Phase geht.

![Turnierbaum der K.-o.-Phase](/assets/2026-06-16-10-19-49/de_030.png)

## Bewusst minimale Interaktion

Die Interaktion ist absichtlich auf ein Minimum reduziert. Das Board wechselt mit einem einzigen Tippen zwischen Gruppenphase und K.-o.-Baum – das passt sowohl zum wandmontierten Touchscreen als auch zum passiven Display, das über einen Timer läuft. Es gibt keine Menüs zum Navigieren und keine Einstellungen zum Herumprobieren – es ist dafür gebaut, in Ruhe gelassen und einfach nur angeschaut zu werden.

Genau diese Zurückhaltung ist der Punkt. Ein Signage-Board verdient sich seinen Platz, indem es zuverlässig und mühelos ist – und dieses hier liefert beides, weil die Daten die ganze Arbeit übernehmen.

## Ergebnis

Das fertige Board ist ein sich selbst pflegendes WM-Display. Es liest die echte Auslosung und die Live-Ergebnisse aus einem kostenlosen Online-Feed, berechnet jede Gruppentabelle und den kompletten K.-o.-Baum eigenständig neu und präsentiert beides als klare, auf einen Blick erfassbare Screens, die das Publikum quer durch den Raum lesen kann. Sie richten es einmal ein, hängen es an die Wand, und es hält sich für das gesamte Turnier von selbst aktuell – keine manuellen Updates, keine Fehler, kein Aufwand. Laden Sie die Projektdatei aus der Seitenleiste herunter und bringen Sie Ihr eigenes WM-2026-Board in wenigen Minuten zum Laufen.