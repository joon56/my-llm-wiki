---
title: Wrap SQL Scripts in a Transaction to Surface the First Error
tags:
  - dev/db
  - dev/debugging
status: distilled
publish: true
lang: en
translation: 10-Concepts/SQL-스크립트는-트랜잭션으로-감싸야-첫-에러가-드러난다
created: 2026-07-26
sources: []
---

## Summary

The error message you see from a multi-statement SQL script is often just "the last statement that failed" — since the client keeps executing after an earlier failure, you get a cascade of errors, so wrapping the script in BEGIN/COMMIT is what actually stops it at the real culprit statement.

## Details

- Many SQL clients, including psql, execute statement-by-statement by default: if statement 3 fails, statements 4 and 5 still run. They cascade-fail because the table/column statement 3 should have created doesn't exist — and what's left on screen is the last error.
- Misdiagnosing the last error as the cause leads you to fix the wrong statement.
- Wrapping in `BEGIN; ... COMMIT;` puts the transaction into an aborted state at the first failure, and every statement after that is skipped with "current transaction is aborted" — so the first error message is the actual cause.
- Bonus: this also prevents partially-applied schemas (half-created state). Schema migration scripts should be wrapped in a transaction by default.

## Sources
-
