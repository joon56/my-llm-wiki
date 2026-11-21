---
title: Verify Round-Trip Identity Before Extracting Text for Human Edits
tags:
  - dev/workflow
  - dev/tooling
status: distilled
publish: true
lang: en
translation: 10-Concepts/사람이-고칠-텍스트는-왕복-항등성부터-검증하고-빼낸다
created: 2026-11-21
sources: []
---

## Summary

When a person needs to edit **prose that lives inside code**, such as comments, **extract only the text into external files and put it back by position through a round-trip pipeline** — but first verify that an untouched round trip reproduces the source byte for byte. After reinsertion, prove behavior is unchanged with a comment-stripped token comparison, and check meaning changes paragraph by paragraph against the original.

## Details

- The pipeline: 272 Korean comments from six source files were exported to one txt per file (one comment = one paragraph, a blank line between). The person edits only the txt files; a script puts each paragraph back in order. Editing rules travel with the files: do not merge or split paragraphs, do not type comment delimiters, do not change numbers or identifiers.
- Round-trip identity first: reinserting the unedited txt must leave the source unchanged down to the byte (272/272 rebuilt exactly). A copy with altered sentences was also built in advance, and file-format details such as BOM and CRLF are preserved on rewrite.
- Structural check before reinserting: if paragraph counts do not match, leave the source untouched and report only which file is off and by how many. In practice three files came back with paragraphs merged or turned into lists, and they were split back into the original order.
- Prove behavior is unchanged: a comment-stripped code-token comparison confirms "same tokens, same line count". That immediately tells you whether line numbers cited in documents (29 in a submitted report) and screenshots are still valid; documents are regenerated only when the line count changed.
- Meaning drift that actually showed up in the edited prose: a condition whose meaning changed (when a key-expansion step runs), reference numbers altered (slide 7.28 became "figure 7.28"), honorific endings mixed in, a reason clause turned into a purpose clause ("since it can only process multiples" → "so that it processes only multiples"), and one phrase dropped. Compare numbers, identifiers and references against the original mechanically.
- Invisible and special characters sneak in: 286 narrow no-break spaces (U+202F), special hyphens, ×, ⊕, ←, ≠ and superscripts were normalized to the project's character rules, and a non-ASCII scan joined the checks. Rule-based rewrites such as switching every sentence ending need a review of the changed-word list — that is how a malformed conversion of "동일하다" ("is identical") into "동일하임" was caught.
- Files that pass the structural check still need a meaning review: two files whose paragraph counts matched were left out of the report; after the user asked, a side-by-side comparison with the original found three more issues (one a change in meaning).

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Verify Version Drift Between Planning Docs and Final Deliverables]], [[Generate Change Reports From the Diff, Not From Memory]], [[Data Architecture That Generates Derivatives From a Single Source of Truth]]
