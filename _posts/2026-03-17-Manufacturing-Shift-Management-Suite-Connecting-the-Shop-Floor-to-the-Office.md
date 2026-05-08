---
layout: post
title: Manufacturing Shift Management Suite - Connecting the Shop Floor to the Office
title_de: "Schichtmanagement-Suite für die Fertigung - Produktion und Büro verbinden"
date: 2026-03-17 00:00:00 +0000
tags: production
image: /assets/2026-03-17-15-59-45/title.jpg
bg_alternative: true
description: "A two-app suite that bridges shop floor operators and office management across three production lines and rotating shifts, with real-time production tracking, quality metrics, and cross-shift handover notes."
description_de: "Eine zweiteilige App-Suite, die Werker und Büromanagement über drei Fertigungslinien und rotierende Schichten hinweg verbindet - mit Echtzeit-Produktionsverfolgung, Qualitätskennzahlen und Schichtübergabe-Notizen."
downloads:
  - name: ShopFloorShiftApp.pbmx
    url: /assets/2026-03-17-15-59-45/ShopFloorShiftApp.pbmx
  - name: OfficeShiftOverview.pbmx
    url: /assets/2026-03-17-15-59-45/OfficeShiftOverview.pbmx
---
{% include youtube.html id="Qv4jYyPafNk" %}

<div data-lang="en" markdown="1">

On a busy production floor running three parallel manufacturing lines across rotating Early, Late, and Night shifts, keeping everyone aligned on output targets, quality metrics, and cross-shift communication is a constant challenge. Verbal handovers get lost in the noise of the factory, paper logs are outdated by the time anyone reads them, and managers in the office have no real-time visibility into what is happening on the floor. This two-application suite solves that problem by giving shop floor operators and office management each exactly the information and interaction they need - displayed on screens placed where decisions happen.

## The Shop Floor App

The Shop Floor App is designed for large touchscreen displays mounted at the end of each production area, visible to line operators, team leads, and shift supervisors as they move between stations. When operators clock in at the start of their shift, the screen immediately prompts them to enter their name, ensuring every data update is attributed to the right person.

The main view shows three large cards, one per production line, each displaying the current product being manufactured, a live actual-vs-target counter, defect counts, and a gradient progress bar that fills toward the shift goal. The left border of each card glows green when the line is running, red when stopped, and yellow during maintenance - giving an instant visual pulse of the entire factory floor from across the room.

![Shop Floor App](/assets/2026-03-17-15-59-45/ShopFloorShiftApp_010.png)

Operators interact directly with the display: tapping a line card opens an edit dialog with large stepper buttons for updating actual and defect quantities, plus a free-text notes field for flagging issues like "Conveyor belt tension needs adjustment" or "Material batch #4872 running slightly off-spec." These notes carry forward to the next shift - the bottom section of the screen permanently displays handover notes left by the previous shift, so incoming operators know exactly what to watch for without relying on a verbal briefing.

A History screen lets operators scroll through the full shift log, with rows color-coded red when production fell below 85% of target and green when targets were exceeded. This makes it easy to spot patterns and recurring issues at a glance.

## The Office Overview App

The Office Overview App lives on a wall-mounted display in the production manager's office or a shared management area. It is a read-only dashboard that pulls the same data but presents it through an analytical lens.

Three circular gauge widgets show efficiency percentages per line at a glance, with card borders that turn red when any line drops below 85% efficiency - a visual alarm that draws the eye immediately. A detailed table below breaks down every product run in the current shift, with rows color-coded by performance: green for on-track, red for behind, and blue for lines exceeding their targets.

![Office Overview App](/assets/2026-03-17-15-59-45/OfficeShiftOverview_010.png)

The lower section surfaces the same handover notes from the previous shift, so managers reviewing morning performance can see what the Night shift flagged without walking to the floor.

For deeper analysis, managers can tap through to an Analytics screen showing a grouped bar chart comparing target versus actual production across all three lines, and a doughnut chart breaking down how defects are distributed by line - quickly revealing whether quality problems are concentrated on one line or spread evenly.

## Real-time synchronization

The two apps share state through Peakboard Hub MQTT variables. When a shop floor operator switches the active shift, the office dashboard updates automatically. Line status changes - Running, Stopped, or Maintenance - propagate instantly across both displays. This shared-state architecture means the office always sees what the floor sees, without anyone needing to make a phone call or send an email.

Shift toggle buttons on both apps let users switch between Early, Late, and Night views to compare performance across the day, making it simple to identify which shifts consistently hit their targets and which need support.

## Conclusion

This two-app suite eliminates the communication gap between the shop floor and the office. Operators get a purpose-built touchscreen interface for logging production data and leaving handover notes, while managers get a real-time analytical dashboard with efficiency gauges, performance tables, and defect breakdowns. Because both apps share the same live data, every stakeholder works from a single source of truth - no delays, no miscommunication, and no information lost between shifts.

</div>

<div data-lang="de" markdown="1">

Auf einem ausgelasteten Produktionsboden mit drei parallelen Fertigungslinien und rotierenden Früh-, Spät- und Nachtschichten ist es eine ständige Herausforderung, alle auf Ausstoßziele, Qualitätskennzahlen und schichtübergreifende Kommunikation auszurichten. Mündliche Übergaben gehen im Lärm der Fabrik verloren, Papierprotokolle sind veraltet, sobald jemand sie liest, und Manager im Büro haben keinen Echtzeitblick auf das, was im Werk passiert. Diese zweiteilige App-Suite löst dieses Problem, indem sie Werker und Büromanagement jeweils genau die Informationen und Interaktionen bietet, die sie brauchen - angezeigt auf Bildschirmen genau dort, wo Entscheidungen fallen.

## Die Shop-Floor-App

Die Shop-Floor-App ist für große Touchscreen-Displays gedacht, die am Ende jedes Produktionsbereichs montiert sind und für Linienführer, Teamleiter und Schichtleiter beim Stationswechsel sichtbar sind. Wenn Werker zu Schichtbeginn einchecken, fordert der Bildschirm sie sofort auf, ihren Namen einzugeben - so wird jede Datenaktualisierung der richtigen Person zugeordnet.

Die Hauptansicht zeigt drei große Karten, eine pro Fertigungslinie, jede mit dem aktuell gefertigten Produkt, einem Live-Ist-gegen-Soll-Zähler, Ausschussmengen und einem Fortschrittsbalken, der sich Richtung Schichtziel füllt. Der linke Rand jeder Karte leuchtet grün, wenn die Linie läuft, rot bei Stillstand und gelb während der Wartung - so liefert die App einen visuellen Puls der gesamten Fabrik aus jeder Ecke des Raums.

![Shop Floor App](/assets/2026-03-17-15-59-45/ShopFloorShiftApp_010.png)

Werker interagieren direkt mit dem Display: Ein Tipp auf eine Linienkarte öffnet einen Bearbeitungsdialog mit großen Schrittknöpfen zum Aktualisieren der Ist- und Ausschussmengen sowie ein Freitextfeld für Hinweise wie "Förderbandspannung muss nachgestellt werden" oder "Materialcharge #4872 läuft leicht außerhalb der Spezifikation". Diese Notizen werden in die nächste Schicht übernommen - der untere Bereich des Bildschirms zeigt dauerhaft die Übergabenotizen der vorherigen Schicht, damit ankommende Werker wissen, worauf sie achten müssen, ohne auf eine mündliche Übergabe angewiesen zu sein.

Ein Historie-Bildschirm lässt Werker durch das vollständige Schichtprotokoll scrollen, wobei Zeilen rot eingefärbt sind, wenn die Produktion unter 85 % des Ziels fiel, und grün, wenn Ziele übertroffen wurden. So lassen sich Muster und wiederkehrende Probleme auf einen Blick erkennen.

## Die Office-Overview-App

Die Office-Overview-App lebt auf einem wandmontierten Display im Büro des Produktionsleiters oder einem gemeinsamen Managementbereich. Sie ist ein reines Anzeige-Dashboard, das dieselben Daten zieht, aber durch eine analytische Brille präsentiert.

Drei kreisförmige Messgeräte zeigen die Effizienz pro Linie auf einen Blick - Kartenränder werden rot, sobald eine Linie unter 85 % Effizienz fällt - ein optischer Alarm, der sofort ins Auge springt. Eine detaillierte Tabelle darunter listet jeden Produktionslauf der aktuellen Schicht, mit nach Leistung farbcodierten Zeilen: grün für im Plan, rot für im Rückstand, blau für Linien, die ihre Ziele überschreiten.

![Office Overview App](/assets/2026-03-17-15-59-45/OfficeShiftOverview_010.png)

Der untere Bereich zeigt dieselben Übergabenotizen der vorherigen Schicht, sodass Manager beim morgendlichen Performance-Review sehen, was die Nachtschicht gemeldet hat - ohne in die Produktion gehen zu müssen.

Für tiefere Analysen können Manager zu einem Analytics-Bildschirm wechseln, der ein gruppiertes Balkendiagramm mit Soll-gegen-Ist-Produktion über alle drei Linien sowie ein Donut-Diagramm mit der Verteilung des Ausschusses pro Linie zeigt - so wird schnell sichtbar, ob Qualitätsprobleme auf einer Linie konzentriert oder gleichmäßig verteilt sind.

## Echtzeit-Synchronisation

Die beiden Apps teilen den Zustand über Peakboard-Hub-MQTT-Variablen. Wenn ein Werker die aktive Schicht wechselt, aktualisiert sich das Büro-Dashboard automatisch. Linienstatus-Änderungen - laufend, gestoppt oder Wartung - propagieren sofort über beide Displays. Diese Architektur mit geteiltem Zustand bedeutet, dass das Büro immer dasselbe sieht wie die Fertigung - ohne Telefonanruf oder E-Mail.

Schichtumschalter in beiden Apps lassen Nutzer zwischen Früh-, Spät- und Nachtschicht wechseln, um die Performance über den Tag zu vergleichen - so wird leicht erkennbar, welche Schichten konsequent ihre Ziele erreichen und welche Unterstützung brauchen.

## Fazit

Diese zweiteilige App-Suite beseitigt die Kommunikationslücke zwischen Fertigung und Büro. Werker bekommen eine zweckgebaute Touchscreen-Oberfläche zum Erfassen von Produktionsdaten und Hinterlassen von Übergabenotizen, Manager bekommen ein analytisches Echtzeit-Dashboard mit Effizienzanzeigen, Performance-Tabellen und Ausschuss-Aufschlüsselungen. Weil beide Apps dieselben Live-Daten nutzen, arbeiten alle Beteiligten aus einer einzigen Wahrheit - ohne Verzögerung, ohne Missverständnisse und ohne verlorene Informationen zwischen Schichten.

</div>
