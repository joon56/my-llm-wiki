---
title: In a Cache-First Listener, Absence Is Unconfirmed Until the Server Answers
tags:
  - dev/db
  - dev/debugging
  - dev/architecture
status: distilled
publish: true
lang: en
translation: 10-Concepts/캐시-우선-리스너가-본-부재는-서버-확인-전까지-미확정이다
created: 2026-11-21
sources: []
---

## Summary

In an offline-first client, a real-time listener's first snapshot may come from the local cache, and a single permission error ends the listener for good. **Defer any decision that creates something or shows an error because something is "missing" until the server has confirmed it, and give subscriptions attached right after a write a re-subscribe policy.**

## Details

- Symptom 1 — right after creating a new project, member changes stopped arriving in real time: the subcollection listener was attached right after an optimistic local write, but the parent document did not exist on the server yet, so the security rule that checks membership returned PERMISSION_DENIED. Firestore ends a listener on error and does not retry it.
- Fix 1: on a permission denial, re-subscribe after a short delay (up to 6 times, 1.5 s apart). When stopping the subscription (`stop()`), clear the pending retries and counters as well.
- Symptom 2 — after sign-up, the user tag hung at "issuing": the first snapshot came from the local cache (no document), and events where only metadata changes — such as moving from cache to server confirmation — are not delivered to a default listener. So the "if it is still missing after server confirmation, issue one" branch never ran.
- Fix 2: use `addSnapshotListener(MetadataChanges.INCLUDE)` to receive the server-confirmation event too, and only conclude "missing" when `fromCache == false` (in two places: the profile and the chat-room list).
- The same principle went into screen design: an item that was never received shows "not found" only after a 5-second wait (items you just created or joined via an invite code arrive late). An item that was seen and then disappears closes immediately, and "no members" is judged only after that item's member list has arrived.
- Generalization: in a cache-first, optimistic-UI client, "missing" in the first snapshot means "not known yet". Defer hard-to-undo reactions — creating things (issuing IDs, creating documents) or showing errors — until the server confirms.
- Subscriptions that drop on auth or permission errors need an app-side re-subscribe policy. Paths where a security rule depends on the result of a write you just made (document existence, membership) are the riskiest.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Tie Server Writes to User-Intent Events, Not Value Changes]], [[Unfiltered Queries That Lean on RLS Leak on Admin Accounts]]
