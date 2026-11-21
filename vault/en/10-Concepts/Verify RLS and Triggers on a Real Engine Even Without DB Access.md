---
title: Verify RLS and Triggers on a Real Engine Even Without DB Access
tags:
  - dev/db
  - dev/security
  - dev/testing
status: distilled
publish: true
lang: en
translation: 10-Concepts/DB-권한이-없어도-RLS·트리거는-실제-엔진에서-검증한다
created: 2026-11-21
sources: []
---

## Summary

Migrations were run by hand in the Supabase SQL Editor and the agent had neither DB access nor a test framework, yet splitting verification into **four layers — embedded Postgres → the real app on a fake backend → public-key probes after deploy → a self-check SQL for the human** — confirmed most of the change before its first production run.

## Details

- Principle: if lacking DB access means deferring every check to a human's production test, production becomes the first test. Each layer catches different failures — SQL semantics and trigger order (engine), UI wiring and permission-error handling (fake backend), the policies actually applied (probes), and settings the agent cannot see (self-check).
- Layer 1, DB logic: run the migrations unchanged on PGlite (real Postgres compiled to WASM), with stubs for the auth schema, a profiles table, Vault, pg_net, and Supabase's default grants. Writing failing scenario tests first and then the SQL got 46 RLS, trigger, and constraint scenarios passing.
- Layer 2, UI: start the real app from outside the repo with Vite `createServer` (`configFile:false`, `envFile:false`) and use a `resolveId` hook to swap the Supabase client module for a fake — it structurally cannot reach the real DB. The fake mimics the same RLS, column grants, triggers, constraints, and unknown-column errors, and 63 admin-screen checks ran with DB write requests pinned at zero.
- Layer 3, external probes after deploy: query the production DB with the public (anon) key to confirm private tables are unreadable and every table rejects writes. Write probes use only nonexistent ids and empty arrays so that zero rows can change, and they also confirm Vault, pg_net, and trigger functions are not callable through the API.
- Layer 4, self-check SQL: hand the human a CTE shaped `item / actual / expected / ok` to run in the SQL Editor. It compares the RLS-enabled table count, policy count, enabled triggers, security-definer functions, and `has_table_privilege('anon', …)` results against expected values without printing secrets or personal data. The SQL itself was first verified on the layer-1 engine across 25 items.
- Write the boundary into the report: state that auth, Vault, and mail sending ran in a simulated environment and that "logged-in production writes and real application saves are unconfirmed", and hand those to the human as the first production test.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Unfiltered Queries That Lean on RLS Leak on Admin Accounts]], [[Wrap SQL Scripts in a Transaction to Surface the First Error]]
