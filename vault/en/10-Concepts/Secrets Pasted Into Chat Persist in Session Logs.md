---
title: Secrets Pasted Into Chat Persist in Session Logs
tags:
  - dev/security
  - tool/claude-code
status: distilled
publish: true
lang: en
translation: 10-Concepts/채팅에-붙여넣은-시크릿은-세션-로그에-영구-보존된다
created: 2026-08-04
sources: []
---

## Summary

Claude Code writes every message to a local JSONL transcript, so a secret pasted into chat — like a GitHub PAT — lives there in plaintext indefinitely. Treat chat input as write-once permanent storage.

## Details

- Claude Code records every message of a session to a local JSONL transcript file. A token pasted into the chat is preserved there in plaintext, permanently — observed firsthand in this session.
- The log does not disappear when the session ends. If a pipeline archives or distills logs (as this wiki does), the secret can propagate into further stores.
- Mitigation actually used, 1: issue the token with a **short expiry (7 days)** from the start, so even a leak has a small damage window.
- Mitigation actually used, 2: **revoke immediately** after the task is done. You cannot erase the token from the log, but you can make it a dead token.
- Mitigation actually used, 3: strip the token from the remote URL in `.git/config` right after pushing. A token embedded in a remote URL is another plaintext persistence point.
- General rule: pass secrets via environment variables or credential helpers, never by pasting into chat. The moment you paste, assume it is recorded somewhere you cannot delete, and plan expiry and revocation accordingly.

## Sources

- 
- Related: [[Secret Scans Must Fail the Pipeline, Not Just Warn]]
