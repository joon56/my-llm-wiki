---
title: Client-Persisted IDs Are Immutable Contracts
tags:
  - dev/architecture
status: distilled
publish: true
lang: en
translation: 10-Concepts/클라이언트에-영구-저장되는-ID는-불변-계약이다
created: 2026-07-26
sources: []
---

## Summary

The moment a value permanently stored on the client — a browser localStorage bookmark, a calendar subscription's event UID — uses an entity ID as its key, that ID becomes a public contract that's effectively unchangeable after deployment.

## Details

- If the ID scheme changes on the server (source-of-truth) side: users' localStorage bookmarks end up pointing at IDs that no longer exist, and calendar apps treat an event whose UID changed as "deleted and recreated," wiping out notification and edit history.
- Unlike a server-side DB migration, **values that have already spread to clients can't be recalled or bulk-converted** — they're scattered across each user's device.
- Design-time principles:
  - Don't derive IDs from content (using a title-based slug as the ID means editing the title changes the ID)
  - Assign a separate, immutable identifier at creation time (a sequence number, a UUID), kept distinct from the display name
  - Add "does this value get stored on the user's device?" to the checklist before any schema change
- If you've already shipped: the only option left is permanently maintaining an old-ID-to-new-ID mapping table. Not changing it in the first place is overwhelmingly cheaper.

## Sources
-
