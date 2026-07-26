---
title: Authorization Must Not Trust Client Input
tags:
  - dev/security
  - dev/auth
status: distilled
publish: true
lang: en
translation: 10-Concepts/인가-판단은-클라이언트-입력을-신뢰하면-안-된다
created: 2026-07-26
sources: []
---

## Summary

If the server blindly trusts identity/permission values sent by the client (role, member type, target ID) to branch authorization logic, it becomes a privilege-escalation vulnerability — authorization must be decided only from a server-verified token or a database lookup.

## Details

- Values like `role`, `memberType`, `userId` in the request body/params can be freely manipulated by an attacker. Branching on `if (role === 'admin')` using these values is a direct path to OWASP A01 (Broken Access Control).
- Correct structure: use only the claims from a signature-verified access token, or permissions looked up from the DB via session ID, for authorization decisions. Client input may determine "what is being requested," never "what is permitted."
- Keep resource identifiers (which post) separate from the authorization subject (who, with what permission).
- The fix is nearly free (swap the branching source for token claims) — catching it at design time costs nothing; finding it after deployment is an incident.

## Sources
-
