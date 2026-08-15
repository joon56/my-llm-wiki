---
title: Passed Deadlines Get Extended - Schedule Facts Need Re-Verification
tags:
  - dev/data
  - research/verification
status: distilled
publish: true
lang: en
translation: 10-Concepts/지난-마감도-연장된다-—-일정-사실은-재검증-대상이다
created: 2026-08-14
sources: []
---

## Summary

Schedule and deadline data is **only true as of its observation time**. Even a fact you recorded as "applications closed" can be reversed by a single extension notice, so treat time-bound data as **perishable observations, not permanent state**.

## Details

- Three real cases in a single week:
  - Contest A: recorded "closed" on deadline day → two days later the official site announced a **6-day extension**. Even a deadline that has passed remains subject to re-verification.
  - Contest B: the launch date **silently moved** from the 10th to the 17th — and the official site briefly returned 404.
  - Contest C: the official site's schedule table said "TBD" while the announcement text (reposted elsewhere) gave an exact closing time — **official sources contradicting each other**.
- Working principles:
  - Stamp every item with a `checked` timestamp, and shorten the re-verification interval as a deadline approaches.
  - Never finalize a status transition (open → closed) from date arithmetic alone — extensions and early closings happen outside the calendar math.
  - When sources conflict, don't pick one: **record both**, and give conservative guidance for user action (treat the earlier date as binding, submit early).
  - Quarantine unconfirmed dates in a note field marked "estimated" instead of the structured event fields — mixing confirmed and estimated dates in one field contaminates downstream derivatives (calendars, D-day badges).

## Sources

- Related: [[Split Web Research Into Verifier and Discovery Agents]], [[JS-Rendered Sites Are a Blind Spot for Static Fetch Verification]], [[Data Architecture That Generates Derivatives From a Single Source of Truth]]
