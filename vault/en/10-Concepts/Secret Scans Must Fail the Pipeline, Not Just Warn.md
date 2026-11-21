---
title: Secret Scans Must Fail the Pipeline, Not Just Warn
tags:
  - dev/security
  - dev/automation
status: distilled
publish: true
lang: en
translation: 10-Concepts/비밀정보-검사는-경고가-아닌-실패로-자동화를-막는다
created: 2026-07-26
sources: []
---

## Summary

A safety check that only prints a warning stops nothing. Gates like secret scans must **exit non-zero** so the next pipeline stage (commit, deploy) physically cannot proceed — and irreversible automation steps need explicit human-confirmation STOP gates designed in.

## Details

- Why warnings fail: automation doesn't read logs. Print "⚠️ API key found" and exit 0, and the pipeline still commits and deploys to completion. Humans miss scrolling warnings too.
- The correct structure: on severe (HIGH) findings the scanner **exits 1** → the CI step fails → downstream steps are skipped automatically. Blocking is the default; passing is the exception.
- As applied in this wiki: `secret_scan.py` exits 1 on HIGH → the GitHub Actions build step fails → deploy blocked. Severity separation matters — only unambiguous patterns (API key formats) block as HIGH; fuzzy patterns (generic `password:`) stay MEDIUM warnings to avoid false-positive fatigue.
- Extension: for automation that's hard to undo (bulk generation, deletion, commits), design **STOP gates** (wait for human approval) independent of any scanner. "The script took care of everything" is the most dangerous status report.
- Scan more than the repo: build-time environment variables can get baked into the bundle, so scan the deployed JS bundle too.
- Stop on FAIL, but add a triage step. One bundle FAIL turned out to be a supabase-js library string that compares against the `sb_secret_` prefix, and once all six secret-scan hits were the scanner's own regex strings (treat the scanner file separately). Let it pass only after deciding whether it is a real key or a pattern string.
- Resolve warnings about public keys by narrowing scope, not deleting: the Firebase API key (`AIza…`) flagged by GitHub secret scanning is a client identifier shipped in every APK, and protecting data is the security rules' job. Instead of removing the key, its API allowlist went from the default 27 APIs to the 4 actually used (settings backed up first); a feature added later was then blocked by the list, so update the list whenever you add a feature.

## Sources

- (Korean source session is a local-only archive)
