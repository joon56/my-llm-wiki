---
title: JS-Rendered Sites Are a Blind Spot for Static Fetch Verification
tags:
  - tool/web
  - dev/debugging
status: distilled
publish: true
lang: en
translation: 10-Concepts/JS-렌더링-사이트는-정적-fetch-검증의-사각지대다
created: 2026-08-14
sources: []
---

## Summary

Verifying an official site with a static fetch (grab HTML, extract text) **cannot distinguish "no information" from "information present but unreadable" on JS-rendered sites** — concluding "schedule not announced" from an empty result is how you get it wrong.

## Details

- Real case: an official contest site fetched on two separate days returned only a title line, so it was recorded as "no schedule posted." In reality the application window, prelims, finals, and even an extension notice were all there — as strings **inside the JS bundle**.
- When a static fetch comes back thin, run this checklist:
  1. Record it as "**could not read**," not "not announced" (unverified ≠ unannounced).
  2. **Fetch the JS bundle directly** — SPA notice strings and countdown targets (ISO dates like `2026-08-18T18:00:00+09:00`) are often hardcoded in the bundle.
  3. Look for secondary sources that repost the same announcement — university notice boards, job/contest boards, and press releases frequently carry the official text verbatim.
  4. Guess at API endpoints — ticketing/registration systems often expose closing info via a separate REST API (fields like `orderable_ends_at`).
- The same trap applies to automated link checkers: HTTP 200 with an empty body is both "site alive" and "site unreadable." URLError/403 from a urllib-grade checker is usually bot-blocking, not a dead link — re-check with a browser-grade fetch before declaring links dead.
- The real cost of reading absence as "not announced": when web search could not find one contest's call, it was logged as "ten days later than usual — anomaly" and the tracker's tentative deadline was pushed back. In fact the official SPA's application-period API had been returning an empty 200 (meaning applications were open) all through September, and that kept being misread as "not announced" until the submission window was missed. When an absence looks later than usual, suspect your means of observation before assuming the event slipped, and confirm what an API's empty response actually means.

## Sources

- Related: [[Passed Deadlines Get Extended - Schedule Facts Need Re-Verification]], [[Split Web Research Into Verifier and Discovery Agents]], [[Offline HTML Copies May Lack Required Meta Tags]]
