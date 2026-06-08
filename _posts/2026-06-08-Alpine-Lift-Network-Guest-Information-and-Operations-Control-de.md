---
layout: post
title: Alpines Liftnetz – Gästeinformation und Betriebssteuerung
date: 2026-06-08 00:00:00 +0000
tags: transportation
image: /assets/2026-06-08-11-25-06/title.jpg
bg_alternative: true
description: "Ein gekoppeltes Digital-Signage-System für ein Skigebiet: ein ruhiger Gästebildschirm im Tal und eine telemetriereiche Betriebsleitstelle – beide synchronisiert über eine gemeinsame Hub-Datenliste."
prompt: |
  Entwirf zwei Apps für ein Skigebiet. Der Gästebildschirm an der Talstation zeigt den aktuellen Liftstatus (offen/geschlossen/Wartezeit), die Pistenverhältnisse, das Wetter und eine Übersicht der Pistenschwierigkeiten für die Besucher. Die App der Betriebsleitstelle zeigt dieselben Lifte, aber mit technischen Details: Seilspannung, Motortemperatur, Personendurchsatz pro Stunde und ein Störungsprotokoll. Beide Apps greifen auf dieselbe Hub-Liste "LiftStatus" zu, sodass der öffentliche Bildschirm in dem Moment aktualisiert wird, in dem der Betrieb einen Liftstatus ändert.
downloads:
  - name: SkiGuestScreen.pbmx
    url: /assets/2026-06-08-11-25-06/SkiGuestScreen_de.pbmx
  - name: SkiOpsControlRoom.pbmx
    url: /assets/2026-06-08-11-25-06/SkiOpsControlRoom_de.pbmx
lang: de
permalink: /de/alpine-lift-network-guest-information-and-operations-control/
translation_url: /en/alpine-lift-network-guest-information-and-operations-control/
---
{% include youtube.html id="_7pZZ3JLI8s" %}


Ein Skigebiet steht und fällt mit einer einzigen simplen Frage, die sich Tausende von Menschen jeden Morgen aufs Neue stellen: Welche Lifte laufen eigentlich gerade? Wintersportler im Tal wollen es wissen, bevor sie ihre Skischuhe schnallen. Die Mitarbeiter in der Leitstelle wollen genau diese Antwort in dem Moment ändern können, in dem eine Windböe oder ein Wartungsfall einen Lift in den Haltebetrieb zwingt. In diesem Artikel werfen wir einen Blick auf eine gekoppelte Digital-Signage-Lösung, die beide Seiten perfekt synchron hält, indem sie alles um eine einzige gemeinsame Wahrheit herum aufbaut: den Live-Status jedes einzelnen Lifts am Berg.

Der Clou dabei ist, dass es zwei völlig unterschiedliche Apps für zwei völlig unterschiedliche Zielgruppen gibt, die aber dieselbe gemeinsame **LiftStatus**-Datenliste lesen und beschreiben. Wenn ein Mitarbeiter in der Leitstelle einen Lift von „Offen" auf „Halt" umschaltet, spiegelt der Gästebildschirm unten im Tal diese Änderung innerhalb von Sekunden wider – ohne manuelles Neuveröffentlichen und ohne dass jemand bei der Talstation anrufen muss, um zu melden: „Lift 4 ist gerade in den Haltebetrieb gegangen."

## Der Gästebildschirm

Die erste App, **SkiGuestScreen**, ist die öffentliche Anzeige. Sie platzieren sie in der Schalterhalle der Talstation, im Einstiegsbereich der Gondel oder im Eingang eines Restaurants oder Hotels an der Talstation. Sie begrüßt ankommende Skifahrer und Snowboarder mit einer ruhigen, großformatigen Übersicht darüber, welche Lifte laufen, wie lang die Schlangen sind und wie Schnee und Wetter oben am Berg aussehen.

![Gästebildschirm Liftübersicht](/assets/2026-06-08-11-25-06/de_SkiGuestScreen_010.png)

Das Design ist bewusst aufgeräumt. Eine Familie, die überlegt, ob sie für eine letzte Abfahrt noch einmal hochfährt, oder ein Anfänger, der prüft, ob die leichten Pisten überhaupt erreichbar sind, kann mit einem Blick auf diesen Bildschirm sofort den Zustand des Skigebiets erfassen. Jeder Lift bekommt seine eigene Kachel mit einem klaren Status und einer aktuellen Wartezeit – so gibt es in der Schlange keine bösen Überraschungen.

![Gästebildschirm Liftdetailkarte](/assets/2026-06-08-11-25-06/de_SkiGuestScreen_020.png)

Gäste können über einen Schwierigkeitsfilter nur die Abfahrten anzeigen lassen, die sie interessieren, und durch Antippen einer einzelnen Liftkachel deren vollständige Details in einer Pop-up-Karte aufrufen. Außerdem lässt der Bildschirm Besucher zwischen der Liftübersicht, einem eigenen Wetterpanel und einer Pistenschwierigkeits-Übersicht wechseln, die ihnen verrät, wie viele blaue, rote und schwarze Abfahrten gerade tatsächlich erreichbar sind – und nicht nur, wie viele es laut Pistenplan gibt.

![Gästebildschirm Wetter und Pistenübersicht](/assets/2026-06-08-11-25-06/de_SkiGuestScreen_030.png)

## Die Betriebsleitstelle

Die zweite App, **SkiOpsControlRoom**, ist das Gegenstück für das Personal. Sie läuft auf einem Touch-Terminal oder Wandbildschirm im Büro der Liftbetriebsleitung. Dieselben Lifte tauchen auch hier auf, allerdings ohne jeglichen Marketing-Glanz und stattdessen vollgepackt mit technischer Telemetrie: Live-Seilspannung, Motortemperatur, Personendurchsatz pro Stunde und ein farbiges Status-Badge für jeden Lift.

![Übersicht der Betriebsleitstelle](/assets/2026-06-08-11-25-06/de_SkiOpsControlRoom_010.png)

Hier wird das Skigebiet tatsächlich gesteuert. Durch Antippen eines Lifts öffnet sich ein Steuerungsdialog, in dem die Mitarbeiter dessen Status festlegen – **Offen**, **Halt** oder **Geschlossen** – und die Wartezeit nach oben oder unten regeln. Das Schließen eines Lifts löst eine bewusste Bestätigungsabfrage aus, denn diese Aktion ist sofort für jeden Gast im Tal sichtbar. Die kleine Hürde ist Absicht: Ein versehentlicher Fehlgriff soll niemals einen öffentlichen Bildschirm verdunkeln.

![Steuerungsdialog der Betriebsleitstelle](/assets/2026-06-08-11-25-06/de_SkiOpsControlRoom_020.png)

Ein eigener **Störungsprotokoll**-Bildschirm erlaubt es Technikern, neue Störungen mit Schweregrad und Beschreibung zu erfassen, die jüngsten Vorfälle zu durchsuchen und sie als erledigt zu markieren, sobald ein Problem behoben ist. Außerdem gibt es einen Wetter-Sendebildschirm, auf dem die Leitstelle die Temperatur-, Wind- und Himmel-/Schnee-Texte pflegt, die der Gästebildschirm anzeigt – inklusive einer Live-Vorschau darauf, wie die Gäste unten im Tal das Ganze sehen werden.

![Störungsprotokoll der Betriebsleitstelle](/assets/2026-06-08-11-25-06/de_SkiOpsControlRoom_030.png)

## Eine gemeinsame Liste, ein geschlossener Kreislauf

Was dieses Gespann funktionieren lässt, ist, dass keine der beiden Apps die Daten allein besitzt. Beide lesen aus derselben **LiftStatus**-Hub-Liste und schreiben in sie hinein. Die Leitstelle schreibt die Wahrheit – Status, Wartezeiten, Wettertexte –, und der Gästebildschirm liest sie. Weil die Liste der einzige Koordinationspunkt ist, besteht keine Gefahr, dass die beiden Bildschirme einander widersprechen, und es gibt keinen Integrationskleber, der zwischen ihnen gepflegt werden müsste.

Das Ergebnis ist ein sauberer Betriebskreislauf: Der Betrieb verändert die Realität, die Gäste sehen die Wahrheit, und die Lücke zwischen „Wir haben gerade Lift 4 auf Halt gesetzt" und „Der Talbildschirm sagt, Lift 4 ist im Haltebetrieb" schrumpft von einem Telefonanruf auf wenige Sekunden.

## Fazit

Dieses Projekt zeigt, wie zwei sehr unterschiedliche Zielgruppen – entspannte Gäste im Tal und fokussierte Mitarbeiter in der Leitstelle – aus einer einzigen gemeinsamen Datenquelle bedient werden können. Der Gästebildschirm bleibt ruhig und einladend, die Betriebs-App bleibt technisch und präzise, und die gemeinsame Hub-Liste hält beide automatisch ehrlich zueinander. Laden Sie sich beide Projekte unten herunter und passen Sie die Liftnamen, Pistenschwierigkeiten und Telemetriefelder an Ihren eigenen Berg an.