---
layout: post
title: Solar Home Energy Suite – Ein Dual-App-Dashboard, um die Hitzewelle mit Solarstrom zu überstehen
date: 2026-06-24 00:00:00 +0000
tags: energy
image: /assets/2026-06-24-10-46-31/title.jpg
bg_alternative: true
description: "Ein Peakboard-System aus zwei Apps für einen Solarhaushalt: ein wandmontiertes Heim-Dashboard mit Live-PV-Daten und animierter Batterieanzeige sowie ein Energieplaner im Smartphone-Stil, der Verbraucher in das sonnenreiche Mittagsfenster legt."
prompt: |
  Ein Dual-App-System für einen Haushalt mit Photovoltaikanlage auf dem Dach während der aktuellen Hitzewelle. Die erste App ist ein wandmontiertes Heim-Dashboard, das die Live-PV-Erzeugung (kW), den heutigen kumulierten Ertrag, den Ladezustand der Batterie als animierte Anzeige und den aktuellen Hausverbrauch zeigt, mit einem interaktiven Umschalter, mit dem der Nutzer das Laden der Batterie gegenüber der Netzeinspeisung priorisieren kann. Die zweite App ist ein Energieplaner im Smartphone-Stil, in dem der Nutzer Verbraucher (Spülmaschine, E-Auto-Ladegerät, Poolpumpe) auf eine Zeitleiste tippt, um sie in das sonnenreiche Mittagsfenster zu legen. Beide Apps teilen sich eine SQL-Datenquelle für die Live-Wechselrichterwerte und eine Hub-Liste für den Verbraucherplan, sodass Änderungen im Planer sofort die prognostizierte Batteriekurve des Dashboards aktualisieren.
downloads:
  - name: SolarHomeDashboard.pbmx
    url: /assets/2026-06-24-10-46-31/SolarHomeDashboard_de.pbmx
  - name: SolarEnergyPlanner.pbmx
    url: /assets/2026-06-24-10-46-31/SolarEnergyPlanner_de.pbmx
lang: de
permalink: /de/solar-home-energy-suite/
translation_url: /en/solar-home-energy-suite/
---
{% include youtube.html id="NS1RxII51KE" %}


Während einer anhaltenden Hitzewelle steht ein Haushalt mit Photovoltaikanlage auf dem Dach täglich vor einem Balanceakt: Mittags liefert die Sonne eine Flut kostenloser Energie, die Klimaanlage und andere Geräte ziehen kräftig, und der Hausspeicher fasst nur eine begrenzte Menge. Das richtige Timing zu treffen – die Batterie zu laden, energiehungrige Geräte dann laufen zu lassen, wenn die Sonne am stärksten scheint, und zu entscheiden, ob überschüssiger Strom gespeichert oder ins Netz verkauft werden soll – macht aus einer passiven Solaranlage ein aktiv gesteuertes Mini-Kraftwerk. In diesem Artikel sehen wir uns ein Gespann aus zwei sich ergänzenden Peakboard-Apps an, die der Familie genau diese Kontrolle geben.

## Das Problem: Energie umsonst, aber nur im richtigen Moment

Solarstrom ist nur dann „umsonst", wenn man ihn auch tatsächlich nutzt, sobald er anfällt. Eine Modulfläche liefert ihr Maximum gegen Mittag – aber genau dann ist oft niemand zu Hause, um die Spülmaschine laufen zu lassen oder das Auto zu laden. Am späten Nachmittag hingegen belastet die Klimaanlage das Netz, während die Module bereits nachlassen. Mittendrin steht der Hausspeicher, und jede Entscheidung – laden, entladen oder ins Netz verkaufen – verändert die Rechnung für den Rest des Tages.

Der Haushalt braucht zwei Dinge: ein klares, jederzeit sichtbares Bild dessen, was gerade passiert, und eine einfache Möglichkeit zu planen, wann die großen Verbraucher laufen sollen. Genau diese Aufteilung spiegeln die beiden Apps wider.

## Das Solar Home Dashboard

Das **Solar Home Dashboard** ist ein wandmontiertes Always-On-Display, idealerweise im Flur, in der Küche oder im Hauswirtschaftsraum platziert – überall dort, wo jeder vorbeikommt. Auf einen Blick beantwortet es die Fragen, die den Haushalt den ganzen Tag beschäftigen: Wie viel Strom erzeugen die Module gerade? Wie viel haben wir heute schon geerntet, und liegen wir auf Kurs für unser Tagesziel? Wie voll ist die Batterie? Wie viel zieht das Haus, und fließt Strom ins Netz oder aus dem Netz?

![Solar Home Dashboard mit animierter Batterieanzeige und KPI-Kacheln](/assets/2026-06-24-10-46-31/de_SolarHomeDashboard_010.png)

Eine große, animierte Ladezustandsanzeige bildet den Mittelpunkt des Bildschirms, umrahmt von KPI-Kacheln und einem Live-Energieflussdiagramm mit gerichteten Pfeilen, die zeigen, wie der Strom zwischen Sonne, Batterie, Haus und Netz wandert. Ein Prognosediagramm sagt die Batteriekurve für den restlichen Tag voraus und berücksichtigt dabei die Geräte, die im begleitenden Planer eingeplant wurden.

![Energieflussdiagramm und prognostizierte Batteriekurve für den Rest des Tages](/assets/2026-06-24-10-46-31/de_SolarHomeDashboard_020.png)

Die wichtigste Interaktion ist der **Energiepriorität-Umschalter**: Mit einem Fingertipp wählt der Nutzer, ob überschüssiger Solarstrom die Batterie auffüllen oder ins Netz eingespeist werden soll. Die Änderung wird über einen Dialog bestätigt, sodass die Entscheidung immer bewusst und nicht versehentlich getroffen wird.

![Der Energiepriorität-Umschalter und das Batterie-Detail-Popup mit Min-, Max- und Durchschnittsladung](/assets/2026-06-24-10-46-31/de_SolarHomeDashboard_030.png)

Ein Tipp auf die Batterieanzeige öffnet ein Detail-Popup mit dem niedrigsten, höchsten und durchschnittlichen Ladestand des Tages – praktisch, um zu erkennen, ob die Batterie während der Hitze zu stark zyklisiert wird.

## Der Solar Energy Planner

Der **Solar Energy Planner** ist die Begleit-App, in einem hohen Smartphone-Layout für Tablet oder Handy gestaltet. Hier plant der Nutzer aktiv energiehungrige Geräte – die Spülmaschine, das E-Auto-Ladegerät, die Poolpumpe – in das sonnenreiche Mittagsfenster ein.

![Zeitleiste des Solar Energy Planner mit hervorgehobenem Peak-Sun-Band](/assets/2026-06-24-10-46-31/de_SolarEnergyPlanner_010.png)

Eine vertikale Zeitleiste hebt das goldene **Peak-Sun**-Band hervor, und jedes Gerät lässt sich antippen, um einen Planungsdialog zu öffnen, in dem ein Schieberegler sowie Plus-/Minus-Tasten die Startstunde festlegen. Der Dialog berechnet die voraussichtliche Energiebilanz in Echtzeit und warnt den Nutzer, wenn er ein Gerät außerhalb des optimalen Sonnenfensters einplant.

![Planungsdialog mit Echtzeit-Berechnung der Energiebilanz und Warnung außerhalb des optimalen Fensters](/assets/2026-06-24-10-46-31/de_SolarEnergyPlanner_020.png)

Bestätigte Pläne erscheinen in einer scrollbaren Liste und werden – das ist der entscheidende Punkt – in eine gemeinsame Hub-Liste geschrieben, die das Wand-Dashboard sofort ausliest. So formt eine im Planer vorgenommene Änderung augenblicklich die prognostizierte Batteriekurve auf dem Dashboard quer durch den Raum neu.

## Zwei Apps, ein gemeinsames Bild

Was das Gespann zu mehr als der Summe seiner Teile macht, ist die gemeinsame Datenebene. Beide Apps lesen die Live-Wechselrichterwerte aus derselben SQL-Datenquelle, und der Verbraucherplan liegt in einer einzigen Hub-Liste. Wenn jemand im Planer das E-Auto-Ladegerät auf die Mittagszeit verschiebt, aktualisiert sich die prognostizierte Batteriekurve des Dashboards, ohne dass jemand hinübergehen und etwas antippen muss. Die Familie plant auf dem Sofa und sieht die Folgen an der Wand erscheinen.

## Fazit

Zusammen verwandeln die beiden Apps abstrakte Energiedaten in konkrete Alltagsentscheidungen und helfen dem Haushalt, den Eigenverbrauch zu maximieren, die Batterie zu schonen und die Hitzewelle mit so viel kostenlosem Solarstrom wie möglich zu überstehen. Das Dashboard macht den aktuellen Zustand unübersehbar, und der Planer macht das Handeln zur Sache weniger Fingertipps – genau die Art alltäglicher Kontrolle, die aus einer Dachanlage ein aktiv gesteuertes Mini-Kraftwerk macht.