---
title: Bridge Joins Connect Tables Without Shared Keys
tags:
  - ml/data
  - dev/data
status: distilled
publish: true
lang: en
translation: 10-Concepts/키가-안-겹치는-테이블은-브릿지-조인으로-잇는다
created: 2026-08-04
sources: []
---

## Summary

When two tables share no key, route through an intermediate table as a bridge with two left joins — and after joining, validate numerically: key overlap and missing rates, not visual inspection.

## Details

- Context: in the NHIS sample cohort, the detailed claims table m20 did not directly share RN_INDI (the person key) with the subject table XY.
- Solution: use m40, which carries both keys, as a bridge — XY ←(left join, RN_INDI)─ m40 ←(left join, RN_KEY)─ m20.
- Keep left joins anchored on the analysis unit (patients in XY) so no subject rows are dropped along the way.
- Post-join verification: confirm with actual numbers — key overlap 100%, missing rate 0% — before moving on.
- Generalization: "the keys don't match" is not a dead end; it is a signal to look for a bridge table. Even without schema docs, measuring key-column overlap rates reveals the join path.
- A join is not done when the code looks right; it is done when the statistics of the resulting table prove it right.

## Sources

- Related: [[Reverse-Engineer Undocumented Datasets With Statistics]]
