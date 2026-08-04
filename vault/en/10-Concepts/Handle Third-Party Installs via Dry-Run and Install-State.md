---
title: Handle Third-Party Installs via Dry-Run and Install-State
tags:
  - dev/tooling
  - tool/claude-code
  - dev/security
status: distilled
publish: true
lang: en
translation: 10-Concepts/서드파티-설치는-dry-run과-install-state-기준으로-다룬다
created: 2026-08-04
sources: []
---

## Summary

Inspect a third-party pack's plan with `--dry-run` before installing, and treat the recorded install-state as the sole source of truth for removal — never guess paths or package names.

## Details

- Before installing a 618-file skill pack, printed the install plan with `--dry-run` and reviewed it: is the namespace isolated? does it leave `settings.json` untouched?
- Two key things to check in the dry-run output: (1) where files will be written (any overwrite of existing files), (2) whether any global config file gets modified.
- Removal was driven by the install-state recorded at install time (603 entries in this case) — deleting by guessed paths risks removing unrelated files or leaving residue behind.
- Never execute a guessed package name: verify the actual bin name in the repo's `package.json` before running anything, which also shuts down the typosquatting-package failure mode.
- Condensed procedure: verify bin via the repo's package.json, review the plan with `--dry-run`, install, and on removal trust only the install-state.

## Sources

- 
