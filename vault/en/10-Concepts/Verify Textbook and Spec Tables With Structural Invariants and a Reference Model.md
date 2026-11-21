---
title: Verify Textbook and Spec Tables With Structural Invariants and a Reference Model
tags:
  - dev/testing
  - dev/debugging
status: distilled
publish: true
lang: en
translation: 10-Concepts/교재·명세의-표는-구조-불변식과-참조-모델로-검증한다
created: 2026-11-21
sources: []
---

## Summary

Tables and pseudocode printed in textbooks and specs contain misprints too — **reproduce the worked examples step by step with an independent reference model you first validated against standard vectors, and check the structural invariants the tables must satisfy (permutation, invertibility, every input used)**. That turns "the textbook is wrong" from a claim into a proof.

## Details

- Validate the judge first: a Python reference model (never submitted) was matched against standard test vectors and 300 random OpenSSL comparisons before it was allowed to judge the textbook examples. Expected values for the real implementation's tests were generated from this model too, so the implementation never grades itself.
- Localize errors by "how many rounds still match": against the DES textbook's 16-round trace, the corrected tables matched 16/16, the printed expansion P-box 0/16 (wrong from round 1), the printed S-box 11/16 (wrong from round 12), and the printed mixer step 0/16.
- Structural invariants are the decisive evidence. The expansion table must use every input bit, but the printed one dropped bit 30 and used bit 31 twice. Each DES S-box row must be a permutation of 0-15, but 03 appeared twice and 01 never; the AES S-box must be a 256-entry permutation that inverts the inverse S-box, but the printed one had CB twice, no C8, and contradicted the inverse table (InvS[C8]=B1).
- Check invertibility too: the printed mixer overwrote one half of the block, so two different plaintexts produced the same ciphertext — one colliding pair is stronger than any argument that decryption is impossible.
- Round-trip checks (decrypt(encrypt(x)) == x) cannot catch table errors: a Feistel structure returns the plaintext even with a wrong S-box or expansion table. Correctness is only proven against known answers (the textbook's intermediate values, standard vectors).
- Separate errors that affect the implementation (table values) from errors that live only in the document (typos in example tables or figures). Of five misprints found in the AES material, one affected the implementation; the rest only changed test expectations and the report.
- To answer "why didn't you follow the textbook?", implement the printed version inside the test code as an evidence group that prints a comparison table when run. Ship only the corrected version — two coexisting versions blur which one is the answer.
- Record the limits: cells that no worked example touches are settled only by the permutation rule and the standard values, not by the examples.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Never Trust PDF Table Extraction Without Cross-Checking the Prose]], [[A Validation Reference Must Come From a Source Independent of What It Checks]], [[Give Independent Reviewer Agents the Source, Not Your Conclusions]]
