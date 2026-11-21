---
title: Verify Backup Creation Immediately After Running a Destructive Script
tags:
  - dev/debugging
  - tool/windows
status: distilled
publish: true
lang: en
translation: 10-Concepts/파괴적-스크립트는-백업-생성-여부를-즉시-검증해야-한다
created: 2026-07-26
sources: []
---

## Summary

Even a script documented as "creates a backup before overwriting" can silently fail at the backup step due to an environment issue and destroy the original with nothing to restore from — verify immediately after any destructive operation that the backup file actually exists and has content.

## Details

- A real case: in Windows Git Bash, `python3` wasn't real Python — it was the empty stub that Microsoft Store installs to prompt installation. The script appeared to "run" without errors, but no backup was created and the original file got truncated to 0 bytes.
- The shape of the trap: a tool's documented safety claim ("the original is kept as .bak") is **a promise, not evidence.** A different environment breaks the promise.
- Verification habit: right after running a destructive script, check `ls -la <backup file>` plus its size (0 bytes means it failed). Safer still: take a manual backup **before** running it.
- A Windows-specific trap: the `python`/`python3` commands can be Store stubs — if `python --version` prints nothing instead of a version, or opens the Store, it's a stub. Use the `py` launcher to be sure.
- Another Windows trap: running `git worktree remove` on a worktree whose `node_modules` was a junction followed the link and emptied the original `node_modules`. A lockfile allowed recovery with `npm ci`, after which 1,046 unit tests, the build, and the browser tests were rerun and passed — unlink links before cleaning up a folder that contains them.
- For a script that wipes and recreates shared data, count its targets read-only before running it. Before regenerating demo data on a shared backend, a read-only export of the accounts showed a real user's account mixed in among the test accounts. Instead of a full reset, a script limited to items owned by test-domain accounts was checked by dry-run (8 targets, 0 involving real users) before it ran, and "no full resets" went into project memory.

## Sources
-
