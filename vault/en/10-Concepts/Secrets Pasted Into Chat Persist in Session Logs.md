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
- Addendum (2026-11-21): the raw transcript itself is not permanent. At startup Claude Code deletes JSONL files whose last activity is older than `cleanupPeriodDays` (default 30 days). The rule still stands — before that happens, copies spread into archive notes, memory imports, and backups, and you cannot easily trace how far, so keep treating a pasted secret as permanently recorded.
- A handoff path that keeps values out of chat: the agent creates an empty template file outside the repo (or in a git-ignored folder, e.g. `secrets.env`), and the user types the values in with Notepad and replies only "saved". Scripts only read the file, and checks print pass/fail, a prefix and length, or row counts — never the value. Commands that may echo a password (such as starting a tunnel) get their output redirected to a file so only the needed line is read, and location data such as coordinates gets the same treatment.
- Leaks beyond typing: a screenshot is a paste too — when a capture of a credentials screen landed in the conversation, that value was never used; the credential was reissued and only the new value was used. IDE integration auto-attaches the current selection and open-file info to the next message, so after handling a sensitive file, clear the selection and close the file before chatting. Web-console SQL editors keep keys in query tabs and saved snippets as well — clear them after running.

## Sources

- 
- Related: [[Secret Scans Must Fail the Pipeline, Not Just Warn]]
