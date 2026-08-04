---
title: Remove PDF PII With True Redaction, Not Overlays
tags:
  - dev/security
  - dev/data
status: distilled
publish: true
lang: en
translation: 10-Concepts/PDF-개인정보는-오버레이가-아니라-redaction으로-지운다
created: 2026-08-04
sources: []
---

## Summary

Covering phone numbers and emails in a PDF with black boxes is fake deletion — the text remains extractable. Adding pymupdf redaction annotations and applying them actually deletes the content.

## Details

- The overlay trap: drawing a rectangle over text hides it on screen, but the text layer is untouched — copy, extraction, and search recover everything. Visual concealment is not deletion.
- True deletion: with pymupdf (fitz), add a **redaction annotation** over the target area, then call `apply_redactions()` — the content in that region is removed from the PDF itself.
- Key insight for Korean PDFs: even when text extraction comes out as mojibake due to Korean encoding issues, **phone numbers and emails are ASCII**, so their positions (coordinates) can still be located by search. Broken Korean extraction does not make redaction impossible.
- Verification is mandatory: after applying redactions, **re-extract the text** and confirm no phone/email patterns remain. "The box is visible, so it must be gone" is not verification.
- Preserve the original: redaction is irreversible, so keep the original PDF as a backup outside the repo. Only the redacted version goes into the repo.

## Sources

- 
- Related: [[Pre-Publication PII and License Sweep Checklist]]
