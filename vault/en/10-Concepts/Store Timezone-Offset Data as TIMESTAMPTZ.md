---
title: Store Timezone-Offset Data as TIMESTAMPTZ
tags:
  - dev/db
status: distilled
publish: true
lang: en
translation: 10-Concepts/타임존-오프셋-있는-데이터는-TIMESTAMPTZ로-저장해야-한다
created: 2026-07-26
sources: []
---

## Summary

If an external payload includes a timezone offset but you store it in a `TIMESTAMP` (WITHOUT TIME ZONE) column, the offset is silently discarded — distinct moments in time end up stored as the same value, and the data loss is unrecoverable after the fact.

## Details

- PostgreSQL's `TIMESTAMP` type, given `2026-07-16T09:00:00+09:00`, simply drops the `+09:00` and stores `09:00:00`. No error, no warning.
- `2026-07-16T09:00:00+09:00` (KST) and `2026-07-16T09:00:00Z` (UTC) are two moments 9 hours apart, but they end up as the same stored value — once stored, there is no way to tell which one it was.
- `TIMESTAMPTZ` interprets the input's offset, normalizes it to UTC for storage, and converts it back to the session timezone on read. The original moment in time is preserved.
- Principle: timestamp data loss can only be prevented **at write time**. There is no "migrate it later" — a value that has already been collapsed cannot be recovered. Default to `TIMESTAMPTZ` when designing schemas for external APIs or log ingestion.

## Sources
- Related: [[Wrap SQL Scripts in a Transaction to Surface the First Error]]
