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

Six recurring encoding traps on Korean Windows (cp949) — the common pattern is: route Korean text through UTF-8 files, never through argv or the console.

## Details

- Trap 1 — Korean mangled in curl JSON payloads: passing JSON containing Korean as a command-line argument corrupts it through cp949 conversion. Fix: save the payload to a **UTF-8 file** and pass it by reference with `curl --data @file.json`.
- Trap 2 — pypdf Korean extraction mojibake: extracting text from Korean PDFs with pypdf yields broken encoding. However, ASCII characters (phone numbers, emails, URLs) survive, so searching for those still works.
- Trap 3 — console UnicodeEncodeError: a Python script printing Korean or Unicode symbols dies with `UnicodeEncodeError` on a cp949 console. Write output to a UTF-8 file instead, or explicitly set the output encoding to UTF-8.
- The common pattern: every one of these traps triggers the moment Korean text crosses a cp949 boundary (argv, console, default encoding). **Detour Korean text through UTF-8 files** as the consistent fix.
- When writing files, also pass `encoding="utf-8"` explicitly — the default file encoding of Python on Windows is cp949 as well.
- Trap 4 — PowerShell 5.1 scripts: a `.ps1` saved as UTF-8 without a BOM is read as ANSI (cp949), so Korean strings and paths inside the script break. A mangled Korean comment even swallowed the next line (`Add-Type`) and produced a baffling error. Save scripts that PS 5.1 will run as UTF-8 with BOM, and write source or XML that other tools read with `UTF8Encoding($false)` (no BOM) — decide on the BOM by who reads the file.
- Trap 5 — MSVC: without `/utf-8`, it reads BOM-less UTF-8 source in the system code page (cp949), raising warning C4819, and a Korean file name in `#include` gets mangled into error C1083 (file not found). Save sources as UTF-8 with BOM, or write Korean strings used at runtime as `\uXXXX` escapes (for checking each re-save encoding, see [[Verify Paste Portability With a Clean Project and Encoding Matrix]]).
- Trap 6 — IDE default encoding: Eclipse on Korean Windows may default to MS949 for text files (it depends on the version), so Korean comments written in UTF-8 break. Ship distributed projects with a project-level UTF-8 setting, and put the recovery path in the instructions (Properties → Resource → Text file encoding → UTF-8).

## Sources

- 
- Related: [[Windows PowerShell Execution Policy Blocks npm Global CLIs]], [[Verify Paste Portability With a Clean Project and Encoding Matrix]]
