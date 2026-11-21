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
- (6) **Sweep history and soon-to-be-committed files too**: even on a repo that is already public, the first push of local-only commits publishes that history, so scan the full history rather than the current tree (print only match/no-match, never the values). A repo that looked clean right after going public still had three uncommitted records containing a third party's name, so the moment before a "push everything" request is the riskiest; and if you are handed an empty repo, check its visibility before the first push — "only I will use it" is not permission to publish.
- (7) **Derived outputs and new output paths**: derivatives inherit the source's personal data. Nineteen simulated recording zips, made by only stretching the time axis, copied the real GPS tracks verbatim — and the new output folder was not in `.gitignore`. Check whether each new output path is ignored as soon as you create it, and register local-only files in the unshared `.git/info/exclude` so that even the ignore rule stays private.
- (8) **Commit metadata and third-party data**: the commit author email shows in public history, so switch to a GitHub noreply address before the first public commit (commits already pushed require a history rewrite). Third-party data such as teammates' body measurements or recording dates and times (which reveal daily routines) stays in local commits until they consent or the repo goes private.

## Sources

- 
- Related: [[Secret Scans Must Fail the Pipeline, Not Just Warn]]
- Related: [[Remove PDF PII With True Redaction, Not Overlays]]
