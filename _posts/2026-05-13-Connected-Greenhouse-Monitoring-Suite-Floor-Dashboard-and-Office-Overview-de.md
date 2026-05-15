---
layout: post
title: Vernetzte Gewächshaus-Überwachung - Hallen-Dashboard und Büro-Übersicht
date: 2026-05-13 00:00:00 +0000
tags: agriculture
image: /assets/2026-05-13-17-13-21/title.jpg
bg_alternative: true
description: 'Ein zweiteiliges Überwachungssystem für Gewächshäuser: ein Hallen-Dashboard in der Anbaufläche und eine Büro-Übersicht, die alle Häuser zusammenfasst. Im Büro quittierte Alarme verschwinden dank einer gemeinsamen Hub-Liste innerhalb von Sekunden vom Hallen-Screen.'
prompt: |
  Erstelle zwei verbundene Apps für einen kommerziellen Gewächshausbetrieb. Die erste ist ein wandmontiertes Dashboard im Gewächshaus, das Temperatur, Luftfeuchtigkeit, CO2 und Bodenfeuchte je Zone live mit Ampel-Statusanzeigen darstellt. Die zweite ist eine Büro-Übersicht, die alle Gewächshäuser zusammenfasst und eine kartenartige Anordnung mit Zonen-Statuskacheln und einem Alarm-Feed zeigt; beide Apps teilen sich eine Hub-Liste namens "ZoneReadings", sodass ein im Büro quittierter Alarm vom Hallen-Screen verschwindet.
downloads:
- name: GreenhouseFloorDashboard.pbmx
  url: /assets/2026-05-13-17-13-21/GreenhouseFloorDashboard.pbmx
- name: GreenhouseOfficeOverview.pbmx
  url: /assets/2026-05-13-17-13-21/GreenhouseOfficeOverview.pbmx
lang: de
permalink: /de/vernetzte-gewaechshaus-ueberwachung-hallen-dashboard-und-buero-uebersicht/
translation_url: /en/connected-greenhouse-monitoring-suite-floor-dashboard-and-office-overview/
redirect_from:
- /de/connected-greenhouse-monitoring-suite-floor-dashboard-and-office-overview/
---

Kommerzielle Gewächshausbetriebe haben ein wiederkehrendes Problem: Die Leute, die die Pflanzen sehen können, sind nicht diejenigen, die entscheiden, wann eskaliert wird, und die Entscheider können nicht riechen, fühlen oder hören, was tatsächlich zwischen den Reihen passiert. Die Folge ist entweder Überalarmierung (jeder Ausschlag löst einen Anruf aus) oder mangelnde Quittierung (Alarme stehen auf einem Bildschirm, den niemand beobachtet, während eine kritische Zone zwei Stunden lang überhitzt). Die beiden Dashboards in dieser Suite schließen diesen Kreislauf mit einem gemeinsamen Datenrückgrat, sodass eine Aktion im Büro sofort auf der Hallenfläche sichtbar wird und ein manueller Check vor Ort dort protokolliert wird, wo das Büro ihn sehen kann.

## Das Hallen-Dashboard

Die erste Anwendung ist für einen wandmontierten Touchscreen direkt in der Anbaufläche gebaut. Stellen Sie sich ein robustes 1920x1080-Panel vor, das in der Nähe des Hauptgangs eines Tomatenblocks an einer Stütze montiert ist und aus jeder Reihe sichtbar ist. Das vorbeigehende Team bekommt einen sofortigen, auf-einen-Blick-Überblick über jede Anbauzone in dieser Halle: Temperatur in Grad Celsius, relative Luftfeuchtigkeit, CO2-Konzentration in ppm und volumetrische Bodenfeuchte, jeweils in einem Sechser-Kachelraster mit Ampelfarbband (Grün für OK, Bernstein für WARN, Rot für CRIT) und Status-Pill.

![Hallen-Dashboard Übersicht](/assets/2026-05-13-17-13-21/GreenhouseFloorDashboard_010.png)

Der Header trägt ein Standort-Status-Badge, das den schlechtesten Zonenstatus über das gesamte Gelände zusammenfasst (vom Büro heruntergepusht), das heutige Datum und die Uhrzeit sowie den Namen des aktuell diensthabenden Bedieners.

![Zonen-Detail mit Feuchte-Dial und CO2-Balken](/assets/2026-05-13-17-13-21/GreenhouseFloorDashboard_020.png)

Ein Tipp auf eine beliebige Zonenkachel öffnet eine Detailansicht mit einer Feuchte-Anzeige, einem CO2-Balkendiagramm mit Zielbereich, einer animierten Bodenfeuchte-Anzeige und einer Temperatur-Sparkline der letzten 30 Minuten. Auf demselben Detailbildschirm gibt es eine besondere Geste zur Bestätigung des manuellen Checks: Statt eines schlichten "Ich habe diese Zone geprüft"-Buttons tippt der Mitarbeiter auf ein grünes Blatt und hält es zwei Sekunden lang gedrückt, während sich eine Fortschrittsleiste füllt und ein Countdown läuft. Diese bewusste Pause verhindert versehentliche Check-ins und schreibt eine Zeile in ein gemeinsames Check-Log, das das Büro später auditieren kann.

![Liste aktiver Alarme auf dem Hallen-Screen](/assets/2026-05-13-17-13-21/GreenhouseFloorDashboard_030.png)

Ein dritter Bildschirm listet aktive, unquittierte Alarme im lokalen Haus auf, und der Footer trägt einen einzeiligen Hinweis, dass die Quittierung im Büro erfolgt, nicht hier auf der Hallenfläche.

## Das Operations Center

Die zweite Anwendung ist für ein Desktop- oder Wand-Display im Büro oder Leitstand gedacht und gibt dem Supervisor eine geländeweite Kartenansicht. Ein stilisiertes Kartenpanel links zeigt vier Gewächshäuser (GH-North, GH-South, GH-East, GH-West) als beschriftete Kacheln in geografischer Anordnung, jede standardmäßig orange, aber rot blinkend, sobald die unquittierte Alarmzahl je Gewächshaus über null steigt. Ein cyanfarbenes Badge auf jeder Kachel zeigt die Live-Anzahl.

![Operations Center Kartenansicht mit Alarm-Feed](/assets/2026-05-13-17-13-21/GreenhouseOfficeOverview_010.png)

Die rechte Seite der Übersicht ist ein Live-Alarm-Feed, der von der gemeinsamen Zonen-Messliste gespeist wird, gefiltert auf nur aktive, unquittierte Alarme über das gesamte Gelände, sortiert nach Schweregrad, mit einem farbigen Severity-Streifen und einer Inline-Schaltfläche **Quittieren** in jeder Zeile. Der große Call-to-Action unten ist ein türkisfarbener Button **Sammelquittierung**, der einen Vollbild-Dialog öffnet: eine Checkbox-Liste aller aktiven Alarme, Verknüpfungen für Alle auswählen / Zurücksetzen, ein Kommentarfeld, das an jede ausgewählte Zeile angehängt wird, und eine einzige Bestätigung, die die Quittierung zurück in die gemeinsame Liste schreibt.

![Gelände-Trends mit Balkendiagrammen](/assets/2026-05-13-17-13-21/GreenhouseOfficeOverview_020.png)

Der Trends-Bildschirm zeigt vier nebeneinanderliegende Balkendiagramme, die durchschnittliche Temperatur, Luftfeuchtigkeit, CO2 und Bodenfeuchte über die vier Gewächshäuser hinweg vergleichen.

![Heatmap der Zonenabweichungen](/assets/2026-05-13-17-13-21/GreenhouseOfficeOverview_030.png)

Der Heatmap-Bildschirm ist ein scrollbares Kachelraster, in dem jede Zone des Geländes nach einem berechneten Abweichungswert (Distanz zum Zielbereich) eingefärbt ist, sodass der Supervisor auf einen Blick triagieren kann, ohne Zahlen zu lesen.

## Das gemeinsame Rückgrat

Was die beiden Apps "verbunden" und nicht nur "nebeneinander" macht, ist eine einzelne Hub-Liste namens **ZoneReadings** (auf dem Hub eindeutig adressiert als `greenhouse_ZoneReadings`). Beide Apps lesen aus derselben Liste. Das Büro schreibt die Quittierungsfelder (`Acknowledged`, `AcknowledgedBy`, `AcknowledgedAt`, `AcknowledgeComment`) direkt auf dem Hub. Die Hallen-App, die dieselbe Liste auf ihre eigene `GreenhouseId` filtert, sieht die Zeile innerhalb von fünfzehn Sekunden aus ihrem aktiven Alarm-Screen verschwinden.

Eine zweite gemeinsame Liste, `greenhouse_ZoneCheckLog`, erfasst die manuellen Checks. Drei Hub-MQTT-Variablen (aktiver Bediener, globale Alarmstufe, letzter Quittierungszeitstempel) werden vom Büro auf jeden Hallen-Screen gepusht, damit die Hallenfläche weiß, wer Dienst hat und wie die Lage geländeweit aussieht, ohne eigene Aggregationsabfragen zu machen.

## Ergebnis

Das Ergebnis ist ein geschlossener Kreislauf: Jeder Alarm hat genau einen offiziellen Quittierungsweg (das Büro), jeder Hallen-Screen sieht die Welt gleich (weil sie aus derselben Liste lesen), und jeder manuelle Check ist belastbare Evidenz, die der Supervisor später auditieren kann. Überalarmierung sinkt, weil die Quittierung im Büro sofort die Hallenfläche bereinigt; mangelnde Quittierung sinkt, weil das Büro auf dieselbe Liste schaut wie die Hallenfläche. Das bewusste Zwei-Sekunden-Halten des Blatts auf der Hallenfläche und der Sammelquittierungs-Dialog im Büro sind kleine ergonomische Details, aber zusammen verhindern sie die beiden häufigsten Ausfallarten von Dashboards in lauten Industrieumgebungen: versehentliche Taps und Quittierungs-Müdigkeit.
