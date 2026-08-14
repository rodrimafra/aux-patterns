# Design Brief: Category hub pages

**Date:** 2026-08-14
**Project:** Agentic UX Patterns (`aux-patterns`)
**Owner:** Rodrigo Mafra
**Status:** Approved direction (hub + implement in prototype)

## Problem Statement

Designers and PMs hit a 49-card wall on the index. Home should teach the ten jobs first. A category page should answer what lives here, then send people into a pattern. The Figma home already does that. The Figma "detail" frame still wears a Laws of UX law-page skeleton (Takeaways, Origins, Buy poster, related laws). The live prototype still lists every pattern behind filter chips.

## Users

- Designers and PMs scanning for a job, then a pattern.
- Keyboard and screen-reader users: one `h1` per view, cards as buttons, existing pattern dialog.
- Bilingual readers (EN-US default, PT-BR toggle).
- People using `prefers-reduced-motion`, light or dark theme, small viewports, or 40px-minimum targets.
- People under cognitive load: ten cards on home, search still finds a named pattern.

## Design Direction

Category page is a hub, not an essay. Home Figma (`70:2972`) is the visual source of truth. Category Figma (`48:893`) donates structure only (back, hero, list, related, next), not leftover LoUX copy or full-bleed hue chrome.

Rebuild `index.html` now. Skip further Figma drafting.

- Home: ten category cards (hue field + 224 still + name + question), search, EN/PT-BR, theme, quiet footer.
- Hub: back, split hero (title + question | still), that category's pattern cards in the same card language, related categories, next category.
- Pattern detail: keep the existing dialog, share hash, markdown download.

## Constraints

- Single-file prototype, zero runtime deps, `file://` must work.
- Independent identity: dark editorial, serif display, category hue as contained field (`FIELDS` in `index.html`). No Gemframe purple-as-brand. No client names.
- No em dashes. No pattern copy edits.
- Preserve theme persistence, View Transitions, reduced motion, container queries, dialog-as-sheet under 640px, safe-area, bilingual `html lang`.
- Chrome strings in both `index.html` embedded `DB.ui` and `data/ui-strings.json`.

## Existing Design System

Prototype tokens in `index.html` (`--s*`, `--t*`, `--bg`, `--ink`, `--serif` / `--sans`). Teaching stills: `ILLUS` (categories) and `PAT` (patterns). Poster fields: `FIELDS`.

## Taste Direction (Early Signal)

Generous dark field, 16px rounded cards, stills as the teaching surface, quiet chrome. Hub must feel like the same site one click deeper, not a Laws of UX clone with AUX titles pasted on.

## Success Criteria

- Home shows 10 categories unless search is active.
- Category hub lists only that category's patterns, with real `ILLUS` / `PAT` art.
- Search from home finds patterns by title, definition, or number. Empty query returns the ten-card home. Search on a hub filters within that category.
- Deep links: `#cat-1` through `#cat-10` for hubs, existing `#slug` for patterns. Closing a pattern opened from a hub restores the category hash.
- Keyboard, screen reader, both themes, both languages, reduced motion.
- No LoUX leftover copy.

## Out of Scope

Figma polish pass, Astro/Hugo, Contact page, poster CTAs, new category essays, replacing the pattern dialog with a full page, content review of the 98 markdown files.
