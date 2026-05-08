---
layout: post
title: Warehouse Pick and Pack - Picker Terminal and Supervisor Dashboard
title_de: "Lager-Kommissionierung - Picker-Terminal und Supervisor-Dashboard"
date: 2026-03-13 00:00:00 +0000
tags: logistics
image: /assets/2026-03-13-13-53-07/title.jpg
bg_alternative: true
description: "A two-part warehouse management system with a handheld picker terminal and a supervisor dashboard for real-time pick and pack operations."
description_de: "Ein zweiteiliges Lagermanagement-System mit einem mobilen Picker-Terminal und einem Supervisor-Dashboard für Pick-and-Pack-Abläufe in Echtzeit."
downloads:
  - name: PickerTerminal.pbmx
    url: /assets/2026-03-13-13-53-07/PickerTerminal.pbmx
  - name: SupervisorDashboard.pbmx
    url: /assets/2026-03-13-13-53-07/SupervisorDashboard.pbmx
---
{% include youtube.html id="hnzZhZ7OOE0" %}

<div data-lang="en" markdown="1">

Warehouse pick and pack operations live and die by speed and accuracy. Pickers need a clear view of their next task, and supervisors need to know at a glance whether the team is on track or falling behind. This two-part system connects a handheld picker terminal with a wall-mounted supervisor dashboard, both communicating through Peakboard Hub in real time.

## The Picker Terminal

The picker terminal is designed for use on handheld devices or mounted stations on the warehouse floor. Workers log in with their worker ID, either by typing it in or scanning a badge. Once logged in, they see a filtered list of their open pick tasks, each showing the article number, article name, storage location, and required quantity.

When a picker arrives at the location and grabs the item, they confirm the pick through a simple dialog that includes a quantity check. Completed tasks are immediately marked as done in the Hub, and the progress bar at the bottom updates to show how many tasks the worker has finished versus how many remain. Color-coded status indicators make it easy to distinguish between open and in-progress tasks at a glance.

![Picker Terminal](/assets/2026-03-13-13-53-07/PickerTerminal_010.png)

## The Supervisor Dashboard

The supervisor dashboard is a wall-mounted screen that gives warehouse managers a bird's-eye view of the entire operation. Six KPI tiles across the top show the numbers that matter most: total tasks, open tasks, tasks in progress, completed tasks, active pickers, and tasks completed today.

A circular gauge in the center displays the overall completion percentage, making it immediately obvious how close the team is to finishing the current workload. Below that, a task table highlights overdue or critical items with color coding so nothing slips through the cracks. A separate worker performance table breaks down each picker's assigned, completed, and remaining tasks, while a bar chart visualizes the same data for quick comparison. Supervisors can spot bottlenecks, reassign work, or step in to help without ever leaving the dashboard screen.

![Supervisor Dashboard](/assets/2026-03-13-13-53-07/SupervisorDashboard_010.png)

## How they work together

Both applications share a common set of resources in Peakboard Hub. A Hub list called `wh_PickTasks` holds all pick tasks with their status, assigned worker, article details, and location. Two Hub variables, `wh_ActivePickers` and `wh_CompletedToday`, track workforce activity and daily progress. When a picker confirms a task on the terminal, the Hub list updates instantly, and the supervisor dashboard reflects the change on its next refresh cycle. This means the supervisor always has an accurate, up-to-date picture of warehouse throughput without any manual reporting.

## Result

Together, these two dashboards turn a chaotic pick and pack process into a streamlined, transparent operation. Pickers stay focused on their own task queue without distractions, while supervisors can monitor team performance, catch delays early, and make data-driven decisions about workload distribution. The system scales naturally as you add more pickers or expand to additional warehouse zones.

</div>

<div data-lang="de" markdown="1">

Pick-and-Pack-Abläufe im Lager stehen und fallen mit Geschwindigkeit und Genauigkeit. Picker brauchen einen klaren Blick auf ihre nächste Aufgabe, und Supervisor müssen auf einen Blick sehen, ob das Team im Plan liegt oder zurückfällt. Dieses zweiteilige System verbindet ein mobiles Picker-Terminal mit einem wandmontierten Supervisor-Dashboard - beide kommunizieren in Echtzeit über Peakboard Hub.

## Das Picker-Terminal

Das Picker-Terminal ist für Handgeräte oder feste Stationen im Lager ausgelegt. Mitarbeitende melden sich mit ihrer Mitarbeiter-ID an - entweder durch Eintippen oder durch Scannen eines Ausweises. Nach dem Login sehen sie eine gefilterte Liste ihrer offenen Pick-Aufgaben, jeweils mit Artikelnummer, Artikelname, Lagerplatz und benötigter Menge.

Sobald der Picker am Lagerplatz angekommen ist und das Teil greift, bestätigt er den Pick über einen einfachen Dialog inklusive Mengenprüfung. Erledigte Aufgaben werden sofort im Hub als fertig markiert, und der Fortschrittsbalken am unteren Rand zeigt, wie viele Aufgaben der Mitarbeiter abgeschlossen hat und wie viele noch offen sind. Farbcodierte Statusanzeigen machen offene und in Bearbeitung befindliche Aufgaben auf einen Blick unterscheidbar.

![Picker Terminal](/assets/2026-03-13-13-53-07/PickerTerminal_010.png)

## Das Supervisor-Dashboard

Das Supervisor-Dashboard ist ein wandmontierter Bildschirm, der Lagerleitern einen Vogelperspektiven-Blick auf den gesamten Ablauf gibt. Sechs KPI-Kacheln am oberen Rand zeigen die wichtigsten Zahlen: gesamte Aufgaben, offene Aufgaben, Aufgaben in Bearbeitung, abgeschlossene Aufgaben, aktive Picker und heute abgeschlossene Aufgaben.

Ein kreisförmiges Messgerät in der Mitte zeigt den Gesamtfertigstellungsgrad in Prozent und macht sofort sichtbar, wie nah das Team am Abschluss des aktuellen Arbeitsvolumens ist. Darunter hebt eine Aufgabentabelle überfällige oder kritische Posten farblich hervor, damit nichts durchrutscht. Eine separate Performance-Tabelle gliedert für jeden Picker die zugewiesenen, abgeschlossenen und verbleibenden Aufgaben auf, während ein Balkendiagramm dieselben Daten für den schnellen Vergleich visualisiert. Supervisor erkennen Engpässe, verteilen Aufgaben um oder springen helfend ein - alles ohne den Dashboard-Bildschirm zu verlassen.

![Supervisor Dashboard](/assets/2026-03-13-13-53-07/SupervisorDashboard_010.png)

## Wie sie zusammenarbeiten

Beide Anwendungen teilen sich einen gemeinsamen Satz von Ressourcen im Peakboard Hub. Eine Hub-Liste namens `wh_PickTasks` enthält alle Pick-Aufgaben mit Status, zugewiesenem Mitarbeitenden, Artikeldetails und Lagerplatz. Zwei Hub-Variablen, `wh_ActivePickers` und `wh_CompletedToday`, verfolgen die Personalaktivität und den Tagesfortschritt. Wenn ein Picker eine Aufgabe am Terminal bestätigt, aktualisiert sich die Hub-Liste sofort, und das Supervisor-Dashboard zeigt die Änderung beim nächsten Refresh. So hat der Supervisor immer ein aktuelles Bild des Lagerdurchsatzes - ganz ohne manuelles Reporting.

## Ergebnis

Zusammen verwandeln diese beiden Dashboards einen chaotischen Pick-and-Pack-Prozess in einen verschlankten, transparenten Ablauf. Picker bleiben ohne Ablenkung auf ihre Aufgabenliste konzentriert, während Supervisor die Teamleistung beobachten, Verzögerungen früh erkennen und datenbasierte Entscheidungen über die Arbeitsverteilung treffen. Das System skaliert ganz natürlich mit, wenn weitere Picker hinzukommen oder zusätzliche Lagerbereiche eingebunden werden.

</div>
