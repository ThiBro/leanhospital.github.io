---
layout: post
title: Prozess-Dashboard für eine Kläranlage - Der Leitstand-Blick mit Peakboard
date: 2026-05-26 00:00:00 +0000
tags: energy
image: /assets/2026-05-26-14-23-26/title.jpg
bg_alternative: true
description: "Ein einziges, dauerhaft aktives Leitstand-Dashboard, das das Abwasser durch jede Reinigungsstufe begleitet, vom Zulauf bis zum Ablauf, mit Live-Werten für Durchfluss, pH, Sauerstoff und Trübung."
prompt: |
  Erstelle ein Prozess-Dashboard für eine Kläranlage, das den Durchfluss durch jede Reinigungsstufe abbildet: Zulauf, Vorklärung, biologische Reinigung, Nachklärung und Ablauf. Zeige für jede Stufe Live-Durchflussraten, pH, gelösten Sauerstoff und Trübung mit Gauges und Schwellenwert-Anzeigen. Ergänze ein 24-Stunden-Liniendiagramm des Zulaufvolumens sowie eine Tabelle der Chemikalien-Dosierpumpen mit ihren aktuellen Sollwerten.
downloads:
  - name: Peakboard.pbmx
    url: /assets/2026-05-26-14-23-26/Peakboard_de.pbmx
lang: de
permalink: /de/wastewater-treatment-plant-process-dashboard-a-control-room-view-with-peakboard/
translation_url: /en/wastewater-treatment-plant-process-dashboard-a-control-room-view-with-peakboard/
---
{% include youtube.html id="SnPWHGJfOxA" %}


Eine Kläranlage lässt sich nicht an einem einzigen Punkt beurteilen. Das Rohabwasser, das in den Zulauf gelangt, hat mit dem sauberen Ablauf am Ende der Anlage nichts mehr gemein, und das Wasser verändert sich auf jeder Stufe dazwischen grundlegend. Genau das macht den Überblick so schwierig: Ein Betreiber braucht nicht nur die aktuellen Messwerte, er muss wissen, ob jede Stufe innerhalb ihres gesunden Betriebsfensters arbeitet und welche Stufe, falls überhaupt, in Richtung einer Grenzwertüberschreitung driftet. In diesem Artikel schauen wir uns ein Leitstand-Dashboard an, das die gesamte Reinigungsstraße auf einen Bildschirm bringt, sodass ein Blick quer durch den Raum der Schicht sofort verrät, wie es um die Anlage steht.

## Ein Board, das die Anlage spiegelt

Das Dashboard ist dafür gemacht, auf einer großen Wandanzeige im Leitstand oder auf einem Touchpanel direkt an der Prozesslinie zu laufen. Schichtbetreiber, Anlagenleiter und Instandhalter lesen dieselbe Darstellung und handeln unmittelbar danach. Die fünf Reinigungsstufen, Zulauf, Vorklärung, biologische Reinigung, Nachklärung und Ablauf, sind von links nach rechts angeordnet, mit Durchflusspfeilen dazwischen, sodass das Board die physische Anlage abbildet.

Genau darin liegt der Sinn. Weil die Stufen in derselben Reihenfolge laufen wie das Wasser, wird die Ausbreitung eines Problems offensichtlich. Ist die Trübung am Zulauf hoch, hat sich aber bis zum Ablauf wieder normalisiert, leistet der Prozess seine Arbeit. Bleibt sie weiter hinten hoch, stimmt etwas nicht, und der Betreiber erkennt sofort, wie weit sich die Störung ausgebreitet hat.

![Prozess-Dashboard einer Kläranlage mit allen fünf Reinigungsstufen](/assets/2026-05-26-14-23-26/de_010.png)

Ein Streifen am oberen Rand trägt den Anlagennamen und eine Live-Statuspille für den Gesamtzustand, Normal, Warnung oder Alarm, daneben eine große Uhr mit Datum. Quer durch den Raum bestätigt schon diese eine Pille den Zustand des Betriebs, bevor irgendjemand auch nur eine Zahl liest. Jede der fünf Stufenkarten hebt dann die vier wichtigsten Parameter hervor: Durchflussrate in Litern pro Sekunde, pH, gelöster Sauerstoff in mg/l und Trübung in NTU, jeweils unterlegt mit einem farbigen Statusbalken und einem Ampel-Signalfeld.

## Last vorausahnen und die Chemie im Blick behalten

Die untere Hälfte des Boards teilt sich in zwei Arbeitsbereiche. Links zeichnet ein 24-Stunden-Flächendiagramm mit weicher Spline-Linie das Zulaufvolumen in Kubikmetern pro Stunde nach. Damit erfasst es das klassische Tagesprofil, mit dem jede Anlage lebt: geringer Durchfluss in der Nacht, eine Morgenspitze, wenn die Stadt erwacht, und eine Abendspitze nach dem Essen. Diese Kurve frühzeitig zu sehen, erlaubt es den Betreibern, die hydraulische Belastung vorauszuahnen und Rückspülung oder Schlammabzug in die ruhigen Stunden zu legen, statt gegen eine Spitze anzukämpfen.

Rechts liegt eine Live-Tabelle der Chemikalien-Dosierpumpen. Jede Zeile nennt die Pumpe, die dosierte Chemikalie (etwa ein Flockungsmittel, ein pH-Korrekturmittel oder ein Desinfektionsmittel), ihren aktuellen Sollwert, ihren Betriebsmodus und ihren Laufstatus. Die Zeilenfarben übernehmen die Triage für Sie: Eine gestörte Pumpe färbt sich rot und zieht den Blick sofort auf sich, sodass sich ein Dosierproblem nie in einer Textwand verstecken kann.

![24-Stunden-Diagramm des Zulaufvolumens und Tabelle der Chemikalien-Dosierpumpen](/assets/2026-05-26-14-23-26/de_020.png)

## Ins Detail gehen, ohne den Bildschirm zu verlassen

Alles auf dem Board ist für einen Touchscreen ausgelegt, und der eigentliche Mehrwert zeigt sich, wenn ein Betreiber einer Sache auf den Grund gehen muss. Ein Tippen auf eine beliebige Stufenkarte öffnet einen Detaildialog mit vier großen Rundinstrumenten, jedes mit seinem Zielbereich beschriftet und farblich gegen die Schwellenwerte abgesetzt. Ein Betreiber, der eine Warnung auf der Karte der biologischen Reinigung entdeckt, kann direkt in diese Stufe eintauchen, die exakten Gauge-Werte gegen ihre gesunden Bänder ablesen und entscheiden, was zu tun ist, ganz ohne den Weg zu einem separaten SCADA-Terminal.

Die Pumpentabelle ist genauso praxisnah. Ein Tippen auf eine Zeile öffnet einen Steuerdialog, in dem der Betreiber per Schieberegler einen neuen Sollwert einstellen, ihn in feinen Schritten nach oben oder unten korrigieren oder mit einem einzigen Tippen auf Min, 50 % oder Max springen kann. Ein Dropdown wechselt den Betriebsmodus, und die Änderung wird in die geteilte Pumpenliste zurückgeschrieben, oder der Betreiber bricht ab, ohne etwas zu übernehmen. Ein Aktualisieren-Button lädt die Pumpendaten neu und berechnet die Live-Werte auf Wunsch neu. Beide Dialoge dimmen den Hintergrund hinter sich ab, und ein Tippen auf diesen abgedunkelten Hintergrund schließt den Dialog, was dem Bildschirm das Gefühl einer modernen industriellen HMI verleiht statt eines statischen Schilds.

![Detaildialog einer Stufe mit Rundinstrumenten und der Steuerdialog der Pumpe](/assets/2026-05-26-14-23-26/de_030.png)

## Ergebnis

Das fertige Dashboard verwandelt einen mehrstufigen Prozess, der naturgemäß über die gesamte Anlage verteilt ist, in ein zusammenhängendes, dauerhaft aktives Bild. Betreiber sehen den Gesamtstatus, die vier Schlüsselparameter jeder Stufe, das hydraulische Tagesprofil und den Zustand jeder Dosierpumpe auf einem einzigen Bildschirm, und sie können mit einem Tippen in jede Stufe eintauchen oder jede Pumpe anpassen. Statt Messwerte aus mehreren Tafeln zusammenzusetzen, um zu beurteilen, ob die Anlage gesund läuft, bekommt die Schicht die Antwort auf einen Blick, und ein sich anbahnendes Problem wird sichtbar, lange bevor es zu einer Grenzwertüberschreitung wird.