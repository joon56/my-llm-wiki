---
title: plugin uninstall Ignores the Marketplace Qualifier
tags:
  - tool/claude-code
  - dev/debugging
status: distilled
publish: true
lang: en
translation: 10-Concepts/plugin-uninstall은-마켓플레이스-한정자를-무시한다
created: 2026-08-04
sources: []
---

## Summary

Even when you specify `claude plugin uninstall name@marketplace` precisely, **the CLI ignores the marketplace qualifier after `@` and matches by plugin name only** — so if a same-named plugin is installed from two marketplaces, the wrong copy can get deleted.

## Details

- Real case: the user asked to remove `superpowers@superpowers-marketplace`, but the CLI dropped the qualifier, matched only on the name `superpowers`, and deleted the copy from the other marketplace (claude-plugins-official).
- In other words, the `name@marketplace` syntax does not guarantee precise targeting on uninstall — which copy dies depends on the CLI's name matching.
- Prevention: **never install a same-named plugin from two marketplaces at once.** If the name is unique, this failure mode cannot occur.
- Recovery: if the wrong copy was removed, uninstall the remaining copy too, then reinstall from the marketplace you actually want (there is no way to "undo" the deletion).
- Mitigating factor: if both copies are the same version, the duplicate only exposes the skills twice with identical content, so losing either copy loses nothing — the problem bites when versions differ or you want to keep a specific one.

## Sources
- 
