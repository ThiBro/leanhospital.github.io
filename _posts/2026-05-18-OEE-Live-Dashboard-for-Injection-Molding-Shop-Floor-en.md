---
layout: post
title: OEE Live Dashboard for Injection Molding Shop Floor
date: 2026-05-18 00:00:00 +0000
tags: production
image: /assets/2026-05-18-14-35-10/title.jpg
bg_alternative: true
description: "A wall-mounted OEE command center for an eight-press injection molding shop that turns availability, performance, and quality into action."
prompt: |
  Build an Overall Equipment Effectiveness dashboard for an injection molding shop with eight machines. Display OEE, availability, performance, and quality as gauges per machine, plus a stacked bar chart showing planned vs. unplanned downtime by reason code for the current shift. Add a scrolling ticker at the bottom listing the last ten quality rejects with part number and operator.
downloads:
  - name: Peakboard.pbmx
    url: /assets/2026-05-18-14-35-10/Peakboard.pbmx
lang: en
permalink: /en/oee-live-dashboard-for-injection-molding-shop-floor/
translation_url: /de/oee-live-dashboard-for-injection-molding-shop-floor/
---
{% include youtube.html id="7ihX-Fm1mnc" %}


Walk onto the floor of an injection molding shop on any given Tuesday and you will hear the same question being shouted between the production supervisor and a shift lead: are we making our numbers, and if we are not, which press is dragging us down? Eight machines, three shifts, dozens of part numbers, and a hundred ways to lose minutes - the answer is rarely obvious from the machine HMIs alone. This dashboard is the answer made visible.

## One screen, eight presses, one truth

The screen is meant to live on a large wall-mounted display in the shop, positioned so that machine operators, shift leads, and the production supervisor can all read it from across the floor. A second deployment as a touchscreen kiosk near the shift office turns the same picture into an interactive workspace where a foreman can tap any machine to drill down.

The eight presses on this dashboard range from a 110 ton workhorse all the way up to an 1100 ton heavy hitter, and they are laid out as eight identical cards so the eye never has to hunt. Each card publishes the holy trinity of manufacturing KPIs plus the composite that ties them together: OEE, Availability, Performance, and Quality, each rendered as a circular gauge. Side by side, those four little dials let anyone compare M01 against M07 in a single glance.

![OEE dashboard overview with eight machine cards, downtime chart, and reject ticker](/assets/2026-05-18-14-35-10/010.png)

A bold status pill next to every machine name flips from green (RUNNING) to yellow (FAULT) to red (DOWN). Even seen from across the shop floor, the colors call out trouble before anyone has to read a number. In the sample data shown here, M04 is in FAULT with a wretched 42 percent OEE, and M06 is fully DOWN at zero. That is exactly the kind of signal that should drive an operator to walk over before the next reporting cycle.

## The downtime conversation, ready for the shift handover

Underneath the eight machine cards sits a stacked bar chart that breaks the current shift's downtime apart by reason code. Planned losses (mold changes, scheduled maintenance, setup, operator breaks) stack against unplanned ones (material feed issues, power outage, quality holds, awaiting material). This is the conversation starter for any shift handover: where did we lose time, and was the loss avoidable?

![Stacked downtime bar chart breaking the current shift apart by reason code](/assets/2026-05-18-14-35-10/020.png)

The Cycle Shift button in the header rotates through Day A, Day B, and Night without leaving the page, so the outgoing crew and the incoming crew can step through the day together and see exactly how the picture changed.

## Quality, in everyone's peripheral vision

The ribbon at the bottom is a continuously scrolling ticker that surfaces the last ten quality rejects with timestamp, machine, part number, operator name, and defect reason. It keeps quality concerns alive in everyone's peripheral vision instead of burying them in a report nobody opens. When someone needs to read an entry carefully, a Pause button (or a tap on the ticker itself) freezes the scroll until they are done.

## Drill down with a tap

Interaction is built around a couple of deliberate touches that make the kiosk worth installing. Tapping any of the eight machine cards opens a large modal dialog with much bigger gauges, the part being run right now, and an Acknowledge Alert action that lets the responding technician clear a flag before closing the dialog. It is a tiny ritual that turns a passive wall display into a real handover tool.

![Machine drill-down modal with enlarged gauges and acknowledge action](/assets/2026-05-18-14-35-10/030.png)

A live wall clock and a shift badge round out the header, so anyone glancing up always knows which shift's numbers they are looking at and how much of it is left.

## Conclusion

What this dashboard really delivers is a shared language for a noisy production floor. Operators see their own press in context, shift leads see the whole bay, and the supervisor sees the same single source of truth from the office. The KPIs are not new - any plant manager could recite OEE, Availability, Performance, and Quality in their sleep - but putting them in front of eight machines side by side, with status pills, a reason-coded downtime chart, and a live reject ticker, turns a daily reporting exercise into a moment-by-moment operational picture. That is the difference between knowing yesterday's number and changing today's.