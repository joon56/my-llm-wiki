---
title: Create and Push a GitHub Repo With Only a PAT
tags:
  - tool/git
  - dev/security
status: distilled
publish: true
lang: en
translation: 10-Concepts/gh-CLI-없이-PAT만으로-repo를-만들고-push한다
created: 2026-08-04
sources: []
---

## Summary

Without the gh CLI, a single PAT is enough to go from repo creation to push — but verify the token's `X-OAuth-Scopes` response header before anything else, and strip the token from the remote URL immediately after pushing.

## Details

- Step 1 — verify the token: `curl -H "Authorization: token ghp_xxxx" https://api.github.com/user` confirms the token is alive and which account it belongs to.
- Step 2 — check scopes (the non-obvious diagnostic): inspect the **`X-OAuth-Scopes` header** on that same response. If it is empty, the token has no permissions — and the repo-creation API then returns a **misleading "Not Found" (404)** instead of a permission error. Check scopes before doubting your URL.
- Step 3 — create the repo: `POST https://api.github.com/user/repos` with a JSON body like `{"name": "...", "private": true}` (requires the `repo` scope).
- Step 4 — push: set the remote to a token-embedded URL — `git remote add origin https://ghp_xxxx@github.com/USER/REPO.git`, then `git push -u origin main`.
- Step 5 — clean up immediately: as soon as the push succeeds, run `git remote set-url origin https://github.com/USER/REPO.git` to remove the token from `.git/config`. Otherwise it sits there in plaintext.
- Issue the token with a short expiry and revoke it after the task — assume it may already persist in chat logs somewhere.

## Sources

- 
- Related: [[Secrets Pasted Into Chat Persist in Session Logs]]
