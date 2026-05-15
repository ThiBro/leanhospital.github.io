---
layout: post
title: Lager-Kommissionierung - Picker-Terminal und Supervisor-Dashboard
date: 2026-03-13 00:00:00 +0000
tags: logistics
image: /assets/2026-03-13-13-53-07/title.jpg
bg_alternative: true
description: Ein zweiteiliges Lagermanagement-System mit einem mobilen Picker-Terminal und einem Supervisor-Dashboard für Pick-and-Pack-Abläufe in Echtzeit.
downloads:
- name: PickerTerminal.pbmx
  url: /assets/2026-03-13-13-53-07/PickerTerminal.pbmx
- name: SupervisorDashboard.pbmx
  url: /assets/2026-03-13-13-53-07/SupervisorDashboard.pbmx
lang: de
permalink: /de/lager-kommissionierung-picker-terminal-und-supervisor-dashboard/
translation_url: /en/warehouse-pick-and-pack-picker-terminal-and-supervisor-dashboard/
redirect_from:
- /de/warehouse-pick-and-pack-picker-terminal-and-supervisor-dashboard/
---

Pick-and-Pack-Abläufe im Lager stehen und fallen mit Geschwindigkeit und Genauigkeit. Picker brauchen einen klaren Blick auf ihre nächste Aufgabe, und Supervisor müssen auf einen Blick sehen, ob das Team im Plan liegt oder zurückfällt. Dieses zweiteilige System verbindet ein mobiles Picker-Terminal mit einem wandmontierten Supervisor-Dashboard - beide kommunizieren in Echtzeit über Peakboard Hub.

## Das Picker-Terminal

Das Picker-Terminal ist für Handgeräte oder feste Stationen im Lager ausgelegt. Mitarbeitende melden sich mit ihrer Mitarbeiter-ID an - entweder durch Eintippen oder durch Scannen eines Ausweises. Nach dem Login sehen sie eine gefilterte Liste ihrer offenen Pick-Aufgaben, jeweils mit Artikelnummer, Artikelname, Lagerplatz und benötigter Menge.

Sobald der Picker am Lagerplatz angekommen ist und das Teil greift, bestätigt er den Pick über einen einfachen Dialog inklusive Mengenprüfung. Erledigte Aufgaben werden sofort im Hub als fertig markiert, und der Fortschrittsbalken am unteren Rand zeigt, wie viele Aufgaben der Mitarbeiter abgeschlossen hat und wie viele noch offen sind. Farbcodierte Statusanzeigen machen offene und in Bearbeitung befindliche Aufgaben auf einen Blick unterscheidbar.

![Picker Terminal](/assets/2026-03-13-13-53-07/PickerTerminal_010.png){: loading="lazy" width="1920" height="1080"}

## Das Supervisor-Dashboard

Das Supervisor-Dashboard ist ein wandmontierter Bildschirm, der Lagerleitern einen Vogelperspektiven-Blick auf den gesamten Ablauf gibt. Sechs KPI-Kacheln am oberen Rand zeigen die wichtigsten Zahlen: gesamte Aufgaben, offene Aufgaben, Aufgaben in Bearbeitung, abgeschlossene Aufgaben, aktive Picker und heute abgeschlossene Aufgaben.

Ein kreisförmiges Messgerät in der Mitte zeigt den Gesamtfertigstellungsgrad in Prozent und macht sofort sichtbar, wie nah das Team am Abschluss des aktuellen Arbeitsvolumens ist. Darunter hebt eine Aufgabentabelle überfällige oder kritische Posten farblich hervor, damit nichts durchrutscht. Eine separate Performance-Tabelle gliedert für jeden Picker die zugewiesenen, abgeschlossenen und verbleibenden Aufgaben auf, während ein Balkendiagramm dieselben Daten für den schnellen Vergleich visualisiert. Supervisor erkennen Engpässe, verteilen Aufgaben um oder springen helfend ein - alles ohne den Dashboard-Bildschirm zu verlassen.

![Supervisor Dashboard](/assets/2026-03-13-13-53-07/SupervisorDashboard_010.png){: loading="lazy" width="1920" height="1080"}

## Wie sie zusammenarbeiten

Beide Anwendungen teilen sich einen gemeinsamen Satz von Ressourcen im Peakboard Hub. Eine Hub-Liste namens `wh_PickTasks` enthält alle Pick-Aufgaben mit Status, zugewiesenem Mitarbeitenden, Artikeldetails und Lagerplatz. Zwei Hub-Variablen, `wh_ActivePickers` und `wh_CompletedToday`, verfolgen die Personalaktivität und den Tagesfortschritt. Wenn ein Picker eine Aufgabe am Terminal bestätigt, aktualisiert sich die Hub-Liste sofort, und das Supervisor-Dashboard zeigt die Änderung beim nächsten Refresh. So hat der Supervisor immer ein aktuelles Bild des Lagerdurchsatzes - ganz ohne manuelles Reporting.

## Ergebnis

Zusammen verwandeln diese beiden Dashboards einen chaotischen Pick-and-Pack-Prozess in einen verschlankten, transparenten Ablauf. Picker bleiben ohne Ablenkung auf ihre Aufgabenliste konzentriert, während Supervisor die Teamleistung beobachten, Verzögerungen früh erkennen und datenbasierte Entscheidungen über die Arbeitsverteilung treffen. Das System skaliert ganz natürlich mit, wenn weitere Picker hinzukommen oder zusätzliche Lagerbereiche eingebunden werden.
