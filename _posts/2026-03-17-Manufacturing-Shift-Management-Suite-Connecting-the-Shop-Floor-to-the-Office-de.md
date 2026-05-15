---
layout: post
title: Schichtmanagement-Suite für die Fertigung - Produktion und Büro verbinden
date: 2026-03-17 00:00:00 +0000
tags: production
image: /assets/2026-03-17-15-59-45/title.jpg
bg_alternative: true
description: Eine zweiteilige App-Suite, die Werker und Büromanagement über drei Fertigungslinien und rotierende Schichten hinweg verbindet - mit Echtzeit-Produktionsverfolgung, Qualitätskennzahlen und Schichtübergabe-Notizen.
downloads:
- name: ShopFloorShiftApp.pbmx
  url: /assets/2026-03-17-15-59-45/ShopFloorShiftApp.pbmx
- name: OfficeShiftOverview.pbmx
  url: /assets/2026-03-17-15-59-45/OfficeShiftOverview.pbmx
lang: de
permalink: /de/manufacturing-shift-management-suite-connecting-the-shop-floor-to-the-office/
translation_url: /en/manufacturing-shift-management-suite-connecting-the-shop-floor-to-the-office/
---

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
