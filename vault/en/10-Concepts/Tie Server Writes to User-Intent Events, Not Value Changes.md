---
title: Tie Server Writes to User-Intent Events, Not Value Changes
tags:
  - dev/frontend
  - dev/debugging
status: distilled
publish: true
lang: en
translation: 10-Concepts/서버-쓰기는-값-변경이-아니라-사용자-의도-이벤트에-건다
created: 2026-11-21
sources: []
---

## Summary

UI events do not map 1:1 to user intent — restoring state on screen rotation fires "value changed" with no user input, and one Enter press can submit twice. **Attach server-writing side effects only to intent events such as clicks, and guard against re-entry so they run exactly once.**

## Details

- Incident 1 — one rotation marked every task "done" on the server: the list was built by inflating the same item layout repeatedly, so every checkbox shared one view id. On rotation the system restored state keyed by id and pushed one item's checked state into all of them, and `setOnCheckedChangeListener` fired for that restore too, writing "done" to the server.
- Fix: move the server write to `setOnClickListener` (a user click) and exclude data-rendered list items from state restoration with `isSaveFromParentEnabled = false`. Rotating landscape↔portrait three times each on home, list, and detail (9 rotations) left the server stats unchanged, and every place where a value listener wrote to the server was then hunted down across all screens.
- Incident 2 — one Enter press sent two sign-up requests: the password field's key listener submitted only on ENTER's ACTION_UP and did not consume ACTION_DOWN (it returned false). The unconsumed DOWN reached the keyboard's "done" action and submitted again, creating two accounts with the same email at the same moment.
- The symptom showed up far from the cause: it looked like "a name changed on the server does not appear in the app". Only after listing accounts on the server side (`firebase auth:export`) did the two accounts show up — the app was watching account A while the edit went to account B.
- Fix: consume both DOWN and UP, and toggle a `submitting` flag that blocks re-submission at the same point that shows the loading indicator and disables the button.
- Generalization: "value changed" events also fire for programmatic changes — state restoration, data binding, setting initial values. One physical input can split into several events (DOWN/UP, an IME action, a fast double tap).
- Rule: tie server writes to intent events, guarantee a single run with a re-entry guard, and set initial values before attaching listeners. Put rotation, returning to a screen, and fast double input into your regression scenarios.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Refresh Token Rotation Is Vulnerable to Concurrent Calls]], [[In a Cache-First Listener, Absence Is Unconfirmed Until the Server Answers]]
