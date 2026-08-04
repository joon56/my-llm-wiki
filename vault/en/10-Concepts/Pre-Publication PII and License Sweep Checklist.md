---
title: Pre-Publication PII and License Sweep Checklist
tags:
  - dev/security
  - dev/workflow
status: distilled
publish: true
lang: en
translation: 10-Concepts/공개-전환-전-개인정보·라이선스-스위프-체크리스트
created: 2026-08-04
sources: []
---

## Summary

A checklist to sweep PII, licensing issues, and secrets in one pass before flipping a repo to public — every item here traces back to a real near-miss in one session.

## Details

- (1) **Regex sweep for phones and emails**: Grep the entire repo with phone-number and email patterns — not just code, but data files, docs, and PDFs. Skimming by eye is not a sweep.
- (2) **Exclude license-restricted data**: raw sources with redistribution restrictions, such as government survey microdata, must not enter a public repo — add `data/raw/` to `.gitignore` to block it at the source.
- (3) **Exclude tool artifacts**: leave out files created by local tooling, such as the `.claude/` directory. Session config and log-like files can carry unintended information.
- (4) **Flag author contact info on paper PDFs**: attached paper PDFs have author emails and phone numbers printed in them. Mark them for redaction and process before publishing.
- (5) **Run a secret scan**: scan for token and API key patterns, and halt publication on any finding. The scan must block, not merely warn.
- Each item corresponds to one actual near-miss from the session — this is a list of almost-incidents, not generic advice.

## Sources

- 
- Related: [[Secret Scans Must Fail the Pipeline, Not Just Warn]]
- Related: [[Remove PDF PII With True Redaction, Not Overlays]]
