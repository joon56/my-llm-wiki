---
title: Windows cp949 Encoding Pitfalls
tags:
  - tool/windows
  - dev/debugging
status: distilled
publish: true
lang: en
translation: 10-Concepts/Windows-cp949-인코딩-함정-모음
created: 2026-08-04
sources: []
---

## Summary

Three recurring encoding traps on Korean Windows (cp949) — the common pattern is: route Korean text through UTF-8 files, never through argv or the console.

## Details

- Trap 1 — Korean mangled in curl JSON payloads: passing JSON containing Korean as a command-line argument corrupts it through cp949 conversion. Fix: save the payload to a **UTF-8 file** and pass it by reference with `curl --data @file.json`.
- Trap 2 — pypdf Korean extraction mojibake: extracting text from Korean PDFs with pypdf yields broken encoding. However, ASCII characters (phone numbers, emails, URLs) survive, so searching for those still works.
- Trap 3 — console UnicodeEncodeError: a Python script printing Korean or Unicode symbols dies with `UnicodeEncodeError` on a cp949 console. Write output to a UTF-8 file instead, or explicitly set the output encoding to UTF-8.
- The common pattern: all three traps trigger the moment Korean text crosses a cp949 boundary (argv, console, default encoding). **Detour Korean text through UTF-8 files** as the consistent fix.
- When writing files, also pass `encoding="utf-8"` explicitly — the default file encoding of Python on Windows is cp949 as well.

## Sources

- 
- Related: [[Windows PowerShell Execution Policy Blocks npm Global CLIs]]
