---
title: App installieren
layout: about
lang: de
permalink: /de/how-to-install/
translation_url: /how-to-install/
description: "Schritt-für-Schritt-Anleitung: Wie du ein heruntergeladenes Peakboard-Guru-Projekt (PBMX) auf eine Peakboard Box oder deine eigene BYOD-Hardware bekommst - im Peakboard Designer öffnen, Box koppeln und hochladen."
hero:
  title: Das Projekt auf den Bildschirm bringen
  subtitle: Vom PBMX-Download zur laufenden Peakboard Box / BYOD
  image_header: /assets/img/header.jpg
redirect_from:
  - /de/deploy.html
  - /de/how-to-deploy/
---

Du hast dir eines der Projekte des Gurus geschnappt. Jetzt soll es auf einem echten Bildschirm an der Wand laufen - nicht nur in der Vorschau auf deinem Laptop. So findet die PBMX-Datei ihren Weg auf eine **Peakboard Box** (die kleine Box, die wir verkaufen) oder auf deine eigene **BYOD**-Hardware (Bring Your Own Device - jeder Windows-Rechner mit installierter Peakboard Runtime).

Die ganze Reise dauert fünf Schritte und ungefähr genauso viele Minuten.

## Was du brauchst

1. Die **PBMX-Datei** aus dem Artikel, der dir gefallen hat. Jedes Projekt hier hat einen Download-Button.
2. Den **Peakboard Designer** auf deinem Windows-PC. Er ist kostenlos - hol dir die [Community Edition](https://www.peakboard.com/downloads/peakboard-designer), falls du ihn noch nicht hast.
3. Ein Ziel zum Ausführen: eine **Peakboard Box** oder ein beliebiges Windows-Gerät, das als **BYOD** mit installierter Peakboard Runtime eingerichtet ist.
4. Einen Monitor (HDMI), eine Netzwerkverbindung und Strom für dieses Ziel.

## Schritt 1 - Das Projekt im Peakboard Designer öffnen

Doppelklicke die heruntergeladene `.pbmx`-Datei oder zieh sie auf das Peakboard-Designer-Fenster. Das komplette Projekt öffnet sich - Screens, Datenquellen, Skripte, alles dabei. Schau dich ruhig um, ändere die Farben, richte eine Datenquelle auf dein eigenes System. Es gehört dir zum Umbauen.

Wenn du zufrieden bist, schau in die obere rechte Ecke. Mit dem Button **Vorschau** testest du das Projekt lokal; der Button **Upload** schickt es auf eine Box.

![Der Peakboard Designer - Vorschau und Upload sitzen oben rechts]({{ site.baseurl }}/assets/img/deploy/de_designer-03.png)

## Optional - Die Datenstrukturen im Peakboard Hub anlegen

Viele der Projekte hier lesen und schreiben ihre Daten über **Peakboard Hub Listen** - geteilte Tabellen und Variablen, die in deinem Peakboard Hub liegen. Das Projekt spricht sie über ihren Namen an, also müssen diese Listen und Variablen im Hub existieren, bevor die Visualisierung etwas zum Reden hat. Die gute Nachricht: Der Designer legt sie dir alle in einem Rutsch an.

Öffne den **Peakboard-Hub**-Dialog über die Symbolleiste (das **h**-Symbol). Trag deine Hub-URL und die Zugangsdaten ein und klick auf **Connect** - der Status-Bereich leuchtet grün, sobald du drin bist.

![Der Peakboard-Hub-Dialog im Designer, unten der Button Transfer to Hub]({{ site.baseurl }}/assets/img/deploy/Peakboard-Hub_Transfer-open.png)

Klick jetzt auf **Transfer to Hub**. Der Designer durchsucht das Projekt und listet jede Hub Liste und Variable auf, die es erwartet, samt dem Namen, den sie im Hub bekommt. Die Spalte **Status** zeigt dir, was schon vorhanden ist (*Found*) und was noch angelegt werden muss. Wähl, ob du ein paar Vorschaudaten mitschicken willst, und klick auf **Transfer**, um die fehlenden zu erstellen.

![Der Transfer-to-Hub-Dialog mit den Hub Listen und Variablen des Projekts und ihrem Status]({{ site.baseurl }}/assets/img/deploy/Peakboard-Hub_Transfer-data.png)

Sobald überall *Found* steht, enthält dein Hub alle Strukturen, die das Projekt braucht, und du kannst mit dem Deployment loslegen.

## Schritt 2 - Box / BYOD starten und verbinden

Steck den Monitor an HDMI, schließ das Netzwerkkabel an und verbinde den Strom. Das Gerät bootet in seinen Startbildschirm und zeigt dir seine **IP-Adresse** an, sobald es im Netzwerk ist.

Notiere dir diese IP - du brauchst sie im nächsten Schritt. (Kein Netzwerkkabel zur Hand? Du kannst WLAN auch direkt über diesen Bildschirm einrichten.)

![Der Startbildschirm der Box mit IP-Adresse und Einrichtungsoptionen]({{ site.baseurl }}/assets/img/deploy/Peakboard-Box_InitialScreen_de.png)

## Schritt 3 - Die Box im Designer koppeln

Zurück im Peakboard Designer registrierst du das Gerät, damit es als Upload-Ziel auftaucht. Öffne die **Peakboard-Box**-Einstellungen, füge eine neue Box über die **IP-Adresse** aus Schritt 2 hinzu und bestätige mit den Box-Zugangsdaten (Hostname und Passwort vom Startbildschirm).

Sobald sie gekoppelt ist, erscheint die Box in deiner Liste und bleibt dort für das nächste Mal.

## Schritt 4 - Die Visualisierung hochladen

Klick oben rechts auf **Upload**, wähl deine Box aus der Liste und drück auf **Visualisierung hochladen**. Der Designer packt das Projekt zusammen und schickt es übers Netzwerk an das Gerät.

![Die Box auswählen und die Visualisierung hochladen]({{ site.baseurl }}/assets/img/deploy/Peakboard-Box_Upload_de.png)

## Schritt 5 - Zusehen, wie es live geht

Wenn der Upload klappt und nicht bereits etwas anderes läuft, erscheint das Projekt sofort auf dem angeschlossenen Monitor. Das war's - dein Dashboard ist live.

Eine Box kann mehrere Projekte speichern, aber nur eines läuft gleichzeitig. Lade einfach ein anderes hoch, wann immer du wechseln willst.

---

Das war die Kurzfassung. Für jede Schraube, jedes Kabel und jeden Sonderfall hat die offizielle Doku alles parat: [help.peakboard.com](https://help.peakboard.com/get_started/de-peakboard-box.html).

Mögen deine Uploads stets im ersten Anlauf gelingen.
