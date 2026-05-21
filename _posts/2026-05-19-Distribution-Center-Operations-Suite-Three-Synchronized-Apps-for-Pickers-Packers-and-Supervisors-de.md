---
layout: post
title: Distribution-Center-Suite – Drei synchronisierte Apps für Picker, Packer und Schichtleitung
date: 2026-05-19 00:00:00 +0000
tags: logistics
image: /assets/2026-05-19-11-44-47/title.jpg
bg_alternative: true
description: "Eine dreiteilige Peakboard-Suite, die Picker, Packer und die Schichtleitung in Echtzeit über ein gemeinsames Rückgrat an Auftragsdaten verbindet."
prompt: |
  Erstelle drei Apps für ein Distributionszentrum. App eins ist die Picker-Anzeige im Handheld-Stil und zeigt die aktuelle Pickliste, den Lagerplatz und die Menge mit einem großen Fortschrittsbalken. App zwei ist der Bildschirm der Packstation und zeigt eingehende Behälter sowie Packanweisungen. App drei ist das Dashboard der Schichtleitung mit Durchsatz-KPIs, einem Picker-Ranking und einer Heatmap der Zonenaktivität – alle drei Apps lesen und schreiben in eine gemeinsame Hub-Liste „PickOrders", damit der Zustand konsistent bleibt.
downloads:
  - name: Packstation.pbmx
    url: /assets/2026-05-19-11-44-47/PackingStation_de.pbmx
  - name: Picker-Handheld.pbmx
    url: /assets/2026-05-19-11-44-47/PickerHandheld_de.pbmx
  - name: Schichtleitungs-Dashboard.pbmx
    url: /assets/2026-05-19-11-44-47/SupervisorDashboard_de.pbmx
lang: de
permalink: /de/distribution-center-operations-suite/
translation_url: /en/distribution-center-operations-suite/
---
{% include youtube.html id="iu5JdbdrMh0" %}


In einem modernen Distributionszentrum müssen drei sehr unterschiedliche Rollen denselben Betrieb aus drei sehr unterschiedlichen Blickwinkeln betrachten – und das in Echtzeit. Diese dreiteilige App-Suite verwandelt ein gemeinsames Rückgrat aus Auftragsdaten in ein synchronisiertes Pick-, Pack- und Steuerungserlebnis, das den Alltag auf einer echten Fulfillment-Fläche abbildet. Der Picker, der einen Artikel abhakt, der Packer, der einen Behälter versiegelt, und die Schichtleitung, die den KPI nach oben springen sieht – das sind drei Sichten auf exakt denselben Vorgang.

## Das Picker-Handheld

Die erste Zielgruppe ist der Picker auf der Lagerfläche. Er trägt einen robusten Handheld oder ein am Handgelenk befestigtes Tablet und läuft durch Gänge in Zonen wie A1, B3 oder D5. Die Picker-App ist für Handschuhe, laute Umgebungen und schnelles visuelles Erfassen gemacht – deshalb wird alles Wichtige groß und kontrastreich dargestellt.

![Picker-Handheld – aktueller Pick-Auftrag mit Lagerplatz und Menge](/assets/2026-05-19-11-44-47/de_PickerHandheld_010.png)

In der nächsten Sekunde muss der Picker genau vier Dinge wissen: was er greifen soll, wo es liegt, wie viel er nehmen soll und wie dringend es ist. SKU und Beschreibung stehen oben, ein riesiges cyanfarbenes Lagerplatz-Label wie „B3-12-04" dominiert die Mitte, damit es auch im Gehen lesbar bleibt, die Menge erscheint in überdimensionierten Ziffern, und ein farbiges Prioritäts-Badge wird orange für „Dringend" oder bernsteinfarben für „Hoch".

![Picker-Handheld – Wellenfortschritt und Schicht-Statistik](/assets/2026-05-19-11-44-47/de_PickerHandheld_020.png)

Der Fortschritt der Welle wird durch eine horizontale Anzeige („47 von 120") sichtbar, damit der Picker jederzeit weiß, wie nah er am Ende ist. Seine persönlichen Schichtkennzahlen – Artikel pro Stunde, Genauigkeit, Fehlmengen – stehen rechts daneben, damit er sich auf einen Blick mit einer normalen Schicht vergleichen kann.

![Picker-Handheld – Aktionsbuttons GEPICKT, FEHLT und ÜBERSPRINGEN](/assets/2026-05-19-11-44-47/de_PickerHandheld_030.png)

Hat der Picker einen Artikel erledigt, tippt er auf einen großen grünen GEPICKT-Button. Fehlt Ware, tippt er auf den orangen FEHLT-Button. Will er später zurückkehren, drückt er den bernsteinfarbenen ÜBERSPRINGEN-Button. Weicht die gepickte Menge von der erwarteten ab, öffnet ein Tipp auf die Mengenanzeige ein bildschirmfüllendes Ziffernfeld, in dem die tatsächliche Anzahl eingegeben werden kann.

## Die Packstation

Die zweite Zielgruppe ist der Packer an einer festen Packstation. Er steht am Terminal „PACK-03", einen Barcode-Scanner griffbereit am Tisch, und ein 1920×1080-Breitbildschirm führt ihn vom eingehenden Behälter bis zum versandbereiten Paket.

![Packstation – Warteschlange eingehender Behälter und Checkliste](/assets/2026-05-19-11-44-47/de_PackingStation_010.png)

Sobald die von den Pickern fertiggestellten Behälter über das Förderband ankommen, sieht der Packer sie links in einer Warteschlange. Jede Karte zeigt Behälter-ID, Zielort, Spediteur, Artikelanzahl und eine farbige linke Kante, die die Dringlichkeit signalisiert. Der Packer tippt entweder auf eine Behälterkarte oder scannt den Barcode am Behälter selbst – daraufhin füllt sich das mittlere Panel mit der Packliste, einer empfohlenen Kartongröße und Hinweisen wie „Zerbrechlich" oder „Gefahrgut". Jede Zeile wird grün, sobald sie abgehakt ist.

![Packstation – Live-Vorschau des Versandlabels mit QR-Code und Barcode](/assets/2026-05-19-11-44-47/de_PackingStation_020.png)

Rechts zeigt eine Vorschau des Versandlabels die Lieferadresse, den Spediteur, die Sendungsnummer, einen QR-Code und einen stilisierten Barcode – alles live aus dem ausgewählten Behälter gerendert. So kann der Packer vor dem Druck visuell prüfen, was Adress- und Spediteurverwechslungen abfängt, bevor sie auf das Förderband gelangen. Sind alle Punkte abgehakt, wird der Button „Versiegeln und Versenden" aktiv. Ein Tipp schließt den Behälter ab, erhöht den lokalen Zähler „Behälter heute" und schreibt ein Ereignis in das gemeinsame Event-Log.

![Packstation – Schadensmeldung mit drei Grund-Buttons](/assets/2026-05-19-11-44-47/de_PackingStation_030.png)

Ist ein Artikel beschädigt oder falsch, öffnet ein Warnbutton pro Zeile einen Schadensmeldedialog mit drei großen Grund-Buttons: Transportschaden, Falscher Artikel, Qualitätsproblem. Die Auswahl wird als Ereignis protokolliert, sodass die Schichtleitung das Problem in dem Moment sieht, in dem es gemeldet wird – und nicht erst beim Schichtabschluss.

## Das Schichtleitungs-Dashboard

Die dritte Zielgruppe ist die Schichtleitung in einem Glasbüro mit Blick über die Lagerhalle. Auf einem großen Wandbildschirm läuft das Supervisor-Dashboard, und sie sieht den gesamten Betrieb in einer einzigen Ansicht.

![Schichtleitungs-Dashboard – Durchsatz-KPIs und Trendchart](/assets/2026-05-19-11-44-47/de_SupervisorDashboard_010.png)

Die Kopfzeile trägt die Durchsatz-KPIs – Aufträge heute, Picks pro Stunde, Packrate, Pünktlichkeitsquote – gefolgt von einem 12-Buckets-Flächendiagramm zum Durchsatzverlauf, damit Spitzen und Einbrüche während der Schicht auch aus der Entfernung sofort auffallen.

![Schichtleitungs-Dashboard – Bestenlisten für Picker und Packer](/assets/2026-05-19-11-44-47/de_SupervisorDashboard_020.png)

Eine podestartige Bestenliste rangiert die Top-Picker mit Gold-, Silber- und Bronzezeilen, eine zweite tut dasselbe für die Packer. Der sportliche Rahmen belohnt konstant gute Leistung und macht sichtbar, wer Unterstützung braucht.

![Schichtleitungs-Dashboard – Zonen-Heatmap und Live-Event-Ticker](/assets/2026-05-19-11-44-47/de_SupervisorDashboard_030.png)

Eine interaktive Zonen-Heatmap zeigt acht Zonenkacheln, die die Aktivität farblich codieren – grün für gering, limette für niedrig, bernstein für warm, rot für heiß, grau für pausiert. Ein Live-Event-Ticker streamt die jüngsten Picks, Packs, Schäden und Durchsagen. Erkennt die Schichtleitung eine heiße Zone, öffnet ein Tipp auf die Kachel einen Zonendetail-Dialog mit allen aktuell dort arbeitenden Pickern sowie Optionen, die Zone zu pausieren oder einen Picker umzudisponieren. In der Kopfzeile öffnet ein Broadcast-Button einen mehrzeiligen Textdialog, der eine Nachricht live in den Header jedes Picker-Handhelds und jeder Packstation pusht – so kann die Schichtleitung „Welle 4 startet in 5 Min." oder „Gang C blockiert, bitte D nutzen" auf einen Schlag an die gesamte Halle senden.

## Wie die drei Apps synchron bleiben

Die drei Apps bleiben deshalb konsistent, weil sie alle auf denselben Hub-Listen lesen und schreiben – `distcenter_pickorders`, `distcenter_totes`, `distcenter_events`, `distcenter_pickerstats`, `distcenter_zonestatus` – und auf gemeinsame Hub-Variablen für den aktuellen Picker, die aktuelle Packstation, die Broadcast-Nachricht und die Schicht. Picker-Handheld und Packstation sind keine isolierten Apps mit eigenen kleinen Datenbanken. Sie sind Fenster auf denselben Betrieb, und das Schichtleitungs-Dashboard ist das dritte Fenster, das alles aggregiert, was in den anderen beiden geschieht.

## Fazit

Ein Distributionszentrum ist kein Ein-Bildschirm-Problem. Der Picker braucht großflächige, handschuhtaugliche Aktionsbuttons. Der Packer braucht eine Checkliste und eine Label-Vorschau. Die Schichtleitung braucht KPIs, Rankings und eine Heatmap. Indem der Betrieb in drei rollenspezifische Apps aufgeteilt wird, die sich ein gemeinsames Hub-Rückgrat teilen, bekommt jeder auf der Fläche genau die Sicht, die er braucht – und jede Aktion ist sofort für alle anderen sichtbar, die davon abhängen.