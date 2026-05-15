---
layout: post
title: Restaurant-Tisch-Belegungs-Dashboard - 20 Tische auf einen Blick verwalten
date: 2026-03-11 00:00:00 +0000
tags: gastronomy
image: /assets/2026-03-11-15-12-57/title.jpg
image_header: /assets/2026-03-11-15-12-57/title.jpg
bg_alternative: true
description: Ein farbcodiertes Touchscreen-Dashboard hilft Restaurant-Empfangsmitarbeitenden, Tischbelegung, Reservierungen und Platzierung über vier Gastbereiche in Echtzeit zu verwalten.
downloads:
- name: Peakboard.pbmx
  url: /assets/2026-03-11-15-12-57/Peakboard.pbmx
lang: de
permalink: /de/restaurant-table-occupancy-dashboard-managing-20-tables-at-a-glance/
translation_url: /en/restaurant-table-occupancy-dashboard-managing-20-tables-at-a-glance/
---

Ein gut besuchtes Restaurant mit 20 Tischen verteilt auf vier Bereiche zu führen, ist eine Koordinationsherausforderung. Die Empfangskraft am Eingang muss wissen, welche Tische frei, welche belegt und welche reserviert sind - alles ohne in Papierlisten zu blättern oder durch den Raum zu rufen. In diesem Artikel bauen wir ein lebendiges, interaktives Grundriss-Dashboard, das die Tischverwaltung von einem Gedächtnisspiel in einen Drei-Sekunden-Blick auf eine farbcodierte Karte verwandelt.

## Das Problem klassischer Tischverwaltung

Die meisten Restaurants verlassen sich noch auf eine Mischung aus Klebezetteln, Gedächtnisleistung und gemeinsamen Tabellen, die niemand konsequent aktualisiert. In der Stoßzeit muss die Empfangskraft sich merken, welcher der 20 Tische gerade frei wurde, ob die Reservierung für sechs Personen um 19 Uhr im Hauptraum oder im Séparée war und ob das Paar am Fenster vor zehn Minuten die Rechnung verlangt hat. Fehler führen zu Doppelbuchungen, scheinbar belegten Tischen, die in Wahrheit leer sind, und einer wachsenden Schlange frustrierter Gäste an der Tür.

## Das Dashboard-Konzept

Die Lösung ist ein Touchscreen am Empfangstresen nahe dem Eingang. Er zeigt einen Grundriss, der das physische Layout des Restaurants spiegelt, unterteilt in vier klar beschriftete Zonen:

- **Hauptraum** (oben links) - acht Tische verschiedener Größen, vom Zweier- bis zum Achtertisch
- **Bar Lounge** (unten links) - vier kleinere Tische in gemütlichem Ambiente
- **Séparée** (unten Mitte) - vier mittlere bis große Tische für Gruppen und Veranstaltungen
- **Gartenterrasse** (rechts) - vier Außentische

Jeder Tisch erscheint als beschriftetes Rechteck. Die Hintergrundfarbe sagt alles, was man auf einen Blick wissen muss: **Grün** heißt frei, **Rot** heißt belegt, **Gelb** heißt reserviert. Eine Kopfleiste oben zeigt das aktuelle Datum und die Uhrzeit zusammen mit einer laufenden Zählung freier, belegter und reservierter Tische - so beurteilt die Empfangskraft die Gesamtverfügbarkeit, ohne einzelne Kästchen zu zählen.

![screenshot](/assets/2026-03-11-15-12-57/010.png)

## Eine Laufkundschaft platzieren

Wenn Gäste ohne Reservierung eintreffen, dauert der Ablauf etwa fünf Sekunden. Die Empfangskraft schaut auf den Grundriss, findet einen grünen Tisch passender Größe, tippt ihn an und drückt **Platzieren**. Ein kleiner Dialog fragt nach dem Gastnamen und der Personenzahl. Nach Bestätigung wechselt der Tisch sofort von Grün auf Rot, und der Belegungszähler oben aktualisiert sich. Kein Papier, keine Funkrufe, kein Raten.

## Reservierungen handhaben

Telefonreservierungen folgen einem ähnlichen Ablauf. Die Empfangskraft tippt den Zieltisch an, drückt **Reservieren** und füllt Gastname, Personenzahl, Datum und Uhrzeit aus. Der Tisch wird gelb, und ein Buchungseintrag wird automatisch angelegt. Wenn die reservierte Gruppe eintrifft, wandelt ein einzelner Tipp auf **Platzieren** die Reservierung in eine aktive Belegung um, und der Tisch wechselt von Gelb auf Rot.

Die Kalenderansicht ergänzt die Live-Karte um eine Planungsschicht. Das Personal kann für jeden Tisch einen Wochenplan öffnen und kommende Reservierungen sehen. Ein Tipp auf eine Buchung im Kalender zeigt alle Details - Gastname, Personenzahl, Anfangs- und Endzeit. So lässt sich für volle Abende leicht planen oder große Gruppenbuchungen über mehrere Tische im Séparée koordinieren.

## Einen Tisch räumen

Wenn eine Gruppe geht, tippt die Empfangskraft den roten Tisch an und drückt **Frei**. Der Tisch springt zurück auf Grün, die Gastdaten werden gelöscht, und der Verfügbarkeitszähler steigt. Die Einfachheit zählt hier - in der Stoßzeit ist jede Sekunde wichtig, und ein einzelner Tipp ist schneller als das Durchstreichen einer Zeile auf einer Papierliste.

## Warum das in der Praxis funktioniert

Der wahre Wert zeigt sich in der Stoßzeit. Stell dir einen typischen Freitagabend vor: das Restaurant ist zu 80 % ausgelastet, drei Reservierungen kommen in den nächsten 30 Minuten, und eine Gruppe von sechs ist gerade hereingekommen und hofft auf einen Tisch. Ohne Dashboard muss die Empfangskraft den Zustand von 20 Tischen mental rekonstruieren, eine Papier-Buchungsliste prüfen und unter Druck eine Entscheidung treffen. Mit Dashboard zeigt ein Blick: zwei grüne Tische im Hauptraum, ein gelber Tisch im Séparée, der für 20 Uhr reserviert ist (noch 45 Minuten), und drei freie Plätze auf der Gartenterrasse.

Das farbcodierte System verhindert auch den häufigsten Empfangs-Fehler: Doppelbuchungen. Wenn ein Tisch gelb ist, sieht das jeder sofort. Keine Mehrdeutigkeiten, kein "Ich dachte, das war für morgen", keine peinlichen Momente, in denen zwei Gruppen denselben Tisch erwarten.

## Fazit

Dieses Dashboard ersetzt Raterei durch Echtzeit-Sichtbarkeit. Zwanzig Tische über vier Bereiche, alle gesteuert über einen einzigen Touchscreen am Eingang. Die Empfangskraft sieht das Gesamtbild auf einen Blick, platziert Gäste in Sekunden, verwaltet Reservierungen ohne Papierkram und hält den Service auch an den vollsten Abenden flüssig. Für jedes Restaurant, das den Klebezetteln entwachsen ist, aber keine schwergewichtige Reservierungsplattform braucht, ist das eine praktische, ressourcenschonende Lösung, die ab Tag eins zahlt.
