# Design brief: Agentic UX Patterns craft uplift

**Date:** 2026-08-13  
**Project:** Agentic UX Patterns (`aux-patterns`)  
**Owner:** Rodrigo Mafra  
**Status:** Implementation brief for craft uplift pass

## Problem

The prototype is structurally complete (49 patterns, 10 categories, EN/PT-BR, dark/light, filterable index + detail dialog) but visual craft sits below the bar set by Laws of UX: spacing rhythm, modular type, consistent iconography, and a signature per-item visual. The site must feel like a finished editorial reference, not a functional draft, while keeping its independent identity.

## Users (ability spectrum)

- Designers and PMs scanning patterns for agentic UI decisions.
- Researchers and writers citing definitions and further reading.
- Keyboard and screen-reader users; touch users on small viewports.
- Bilingual readers (EN-US default, PT-BR toggle).
- Users with `prefers-reduced-motion` and light/dark preference.

## Direction

Craft uplift modeled on Laws of UX *qualities* (whitespace, type scale, line icons, filterable index, signature visual, polished detail), not a visual clone. Keep dark editorial + serif display (Iowan / Palatino / Georgia) + one accent hue per category from `data/en.json` → `cats[n].hex`. No purple-as-brand. No client Gemframe identity.

**Imagery:** offline algorithmic-art. One generative family; seed from category id + hex → 10 category motifs + 1 neutral landing motif. Bake compact inline SVG into `index.html`. Zero p5/CDN at runtime. Cards and detail hero share the category motif.

## Constraints (from HANDOFF.md / CLAUDE.md)

- Single-file prototype, zero runtime deps, no build step.
- Client detachment: no Verena / Invictus AI / client copy or visuals.
- No em dashes in any language.
- Preserve behavior: embedded DB, en/pt-br, theme persistence, View Transitions, reduced-motion, container queries, dialog / under-640px bottom sheet, touch targets, safe-area.
- No content/copy edits in this pass.

## Taste signal

Dark editorial reference site. Generous 8pt rhythm. Tight display leading. Single-stroke icons. Category hue as the only accent system. Motifs feel generative and reproducible, not stock illustration.

## Success criteria

- Spacing and type driven by token scales (`--s*`, `--t*`).
- Chrome uses inline SVG icons (theme, close, search, share, download, etc.).
- Each category has a distinct baked SVG motif; landing has a shared backdrop; motifs work offline.
- Detail dialog: motif hero, oversized number, share (hash deep-link), download `.md` from existing fields.
- Dark + light AA-usable ink; keyboard focus; reduced-motion respected.
- Hard-refresh `file://` verify: themes, langs, filter/search, dialog sizes, no em dashes, hues intact, no p5 tags.

## Out of scope

49 per-pattern posters; Astro/Hugo migration; single-source content refactor; content review; domain/hosting; external web fonts; runtime p5/CDN; initial git commit/push unless explicitly requested.
