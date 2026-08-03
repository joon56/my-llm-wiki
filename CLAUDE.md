# LLM WIKI — repo guide

Personal LLM wiki: Obsidian vault (`vault/`) distilled from Claude Code session logs, built with Quartz 4 (`site/`), deployed to GitHub Pages via `.github/workflows/deploy.yml`. Live: <https://joon56.github.io/my-llm-wiki/>.

**Read `vault/CLAUDE.md` first** — it is the vault rulebook (note format, frontmatter, tag hierarchy, publish rules). This file only covers the repo level.

## Layout

- `vault/` — all content. `10-Concepts/` is the actual wiki (one concept = one note); `50-MOC/` topic maps are the site entry point; `90-Archive/claude-sessions/` is auto-collected session logs — read-only, NEVER published; `en/` holds English translation pairs; `vault/CLAUDE.md` is the rulebook.
- `site/` — Quartz 4 build, uses `vault/` as content source.
- `scripts/` — Python (stdlib only): `archive_session.py` (SessionEnd hook), `cc2obsidian.py` (JSONL → md), `secret_scan.py` (CI gate), `tests/` (unit tests).
- `_dropbox/` — gitignored inbox for claude.ai exports; processed by `/ingest`.
- `.claude/commands/` — `/distill` (weekly: promote archive logs to concept notes) and `/ingest`.

## Hard rules

- **`publish: true` implies an English twin**: create the mirror note under `vault/en/`, link both via frontmatter `lang` + `translation`, set `publish: true` on the EN side too, and add it to `vault/en/50-MOC/LLM MOC (EN).md`. Publishing only the KR side breaks the site's KR/EN toggle.
- `90-Archive/` is never edited and never published.
- Deploy is gated by `secret_scan.py` — any HIGH finding blocks the build. Run it locally before pushing content that quotes session logs.
- Wikilinks (`[[Note Title]]`) only inside the vault; no markdown links between notes.
- Everything committed to GitHub (commits, comments, scripts, README) is English; note content may be Korean (with EN pairs when published).
