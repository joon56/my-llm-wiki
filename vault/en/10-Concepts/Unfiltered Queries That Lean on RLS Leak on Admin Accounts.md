---
title: Unfiltered Queries That Lean on RLS Leak on Admin Accounts
tags:
  - dev/security
  - dev/db
  - dev/auth
status: distilled
publish: true
lang: en
translation: 10-Concepts/RLS에-기댄-무필터-쿼리는-관리자-계정에서-샌다
created: 2026-10-05
sources: []
---

## Summary

A "my history" page ran `select('*')` with no filter and looked correct for regular users because RLS returned only their own rows — but **on admin accounts, where the policy says `is_admin() or ...`, everyone's history showed up on screen.**

## Details

- Setup: the query was `supabase.from('mileage_history').select('*')` with no user condition. The RLS policy was `is_admin() or owner-email match`.
- Why it hides: it is correct forever on regular accounts. And the admin account is usually the developer's own account, so "seeing a lot" passes as normal. A derived value computed from the same array (this month's total) was wrong too.
- Principle: RLS defines **the maximum a user may see (authorization)**; the query filter defines **what this page should show (intent)**. They answer different questions. State the page's intent in the query.
- Fix: add `.eq('student_id', me)` with the user's own identifier. Leave RLS as is — the admin's right to read everything is legitimate.
- Habit: open the same page with accounts at each privilege level, and always check "my ..." pages with an admin account.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Authorization Must Not Trust Client Input]]
