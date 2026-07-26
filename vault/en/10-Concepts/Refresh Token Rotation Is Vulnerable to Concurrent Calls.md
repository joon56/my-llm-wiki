---
title: Refresh Token Rotation Is Vulnerable to Concurrent Calls
tags:
  - dev/security
  - dev/auth
status: distilled
publish: true
lang: en
translation: 10-Concepts/리프레시-토큰-로테이션은-동시-호출에-취약하다
created: 2026-07-26
sources: []
---

## Summary

Introducing refresh token rotation (single-use renewal) creates a race where concurrent refresh calls from the client invalidate each other's valid tokens — refresh calls must be serialized with single-flight (a mutex).

## Details

- Rotation mechanics: on a successful refresh, the old refresh token is revoked and a new one issued. Reuse of a revoked token triggers full session invalidation (a security feature).
- The problem: if the client fires two refresh calls concurrently (two tabs, React StrictMode's double mount, duplicate interceptor triggers), the first call rotates the token and the second gets flagged as "reuse of a revoked token" — logging out a legitimate user.
- Fix: make refresh requests single-flight on the client — if a refresh Promise is already in flight, don't fire a new one; share its result. A server-side variant adds a short grace period instead.
- React StrictMode double-invokes mount in development — which is exactly what surfaces concurrency bugs like this early. An auth bug that only breaks under StrictMode is, in most cases, a real race.

## Sources
- Related: [[Authorization Must Not Trust Client Input]]
