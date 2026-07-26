---
title: Windows PowerShell Execution Policy Blocks npm Global CLIs
tags:
  - tool/windows
  - tool/npm
status: distilled
publish: true
lang: en
translation: 10-Concepts/Windows-PowerShell-실행-정책이-npm-전역-CLI를-차단한다
created: 2026-07-26
sources: []
---

## Summary

When a globally installed npm CLI dies in PowerShell with "running scripts is disabled on this system", the CLI isn't broken — **PowerShell's default execution policy (Restricted) is blocking npm's `.ps1` wrapper**. Fix with `Set-ExecutionPolicy RemoteSigned` or by calling the `.cmd` wrapper directly.

## Details

- The mechanics: npm creates three wrappers per global CLI — `foo` (bash), `foo.cmd` (cmd), `foo.ps1` (PowerShell). Typing `foo` in PowerShell resolves to the `.ps1`, which the default policy blocks as an unsigned script.
- Fix 1 (recommended): relax the policy for the current user only —

  ```powershell
  Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```

  Local scripts run; unsigned scripts downloaded from the internet stay blocked. No admin rights needed.
- Fix 2 (one-off): call the `.cmd` wrapper explicitly — `foo.cmd ...` — bypassing the policy without changing it.
- Diagnosis tip: `Get-ExecutionPolicy -List` shows per-scope policy. If the error message mentions a `.ps1` path, it's this issue, always.

## Sources

- Related: [[Verify Backup Creation Immediately After Running a Destructive Script]] (Windows toolchain traps)
