---
title: Review Capacity-Based Matching Plans for Failure States and Demand Dilution First
tags:
  - product/mvp
  - dev/architecture
status: distilled
publish: true
lang: en
translation: 10-Concepts/정원제-매칭-기획은-실패-상태와-수요-분산부터-검토한다
created: 2026-11-21
sources: []
---

## Summary

A matching plan of the form "connect people once N sign up" should be reviewed for **state transitions, number definitions, commitment order, and demand dilution** before any screen design — reviewing a real plan surfaced missing failure states, a minimum confused with a capacity, no notion of rounds, and more options than active members.

## Details

- Fill in failure states first: the plan had only four states — recruiting → full → connecting → scheduled — with no state for the host declining or scheduling falling through. Adding a "fell through" path and "open next round" (a fresh card starting from zero) is what closes the state machine for an always-on program.
- One definition per number: one page read "2–3 or more" (a minimum) and another "3 / 3" (a capacity), leaving the fourth applicant undefined. Unify them into a single seat count per card, and mark the card full automatically once the seats fill.
- Commitment order: asking the host for consent only after the seats fill promises someone else's time in advance. Get consent before the card opens.
- Compute demand dilution: with N active members and K open cards, expected applicants per card is roughly N/K. In the community reviewed, N/K was below 1, so few cards would ever reach a capacity of 2-3; the fix was to cap the number of cards, run topic-first recruiting alongside, and let an operator start early ("connect now") before a card fills.
- Cold-start screens: show the reviews section only once at least one session has completed, and use cards of varying sizes so an early page full of 1/3 cards looks less empty. An empty reviews box signals "nobody does this".
- When operators are few: a full card sits unnoticed if the person in charge never opens the admin tab, so gather "needs action" items at the top of the admin screen and add copy buttons for contact messages and rosters, plus email alerts to every admin.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Each MVP Round Tests One Core Risk Hypothesis]], [[Speed Up Design Consensus With Mockups Instead of Verbal Descriptions]]
