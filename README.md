# Agentic UX Patterns

A pattern library for interfaces that act, 49 patterns across 10 categories.
Independent work by Rodrigo Mafra. License: CC BY-NC-ND 4.0.

## Structure

- `index.html`, self-contained bilingual prototype (open in any browser; no build step).
  - Languages: EN-US (default) and PT-BR, persistent toggle, sets `<html lang>`.
  - Responsive: fluid type via clamp(), container queries, mobile bottom-sheet detail view,
    horizontally scrollable filter chips with scroll-snap, safe-area insets, dvh units.
  - Modern CSS/JS: native <dialog> + ::backdrop, @starting-style entry animations,
    View Transitions API on filtering, text-wrap balance/pretty, color-mix(),
    content-visibility for render performance, prefers-reduced-motion respected,
    dark/light theme toggle with persistent preference.
- `patterns/*.md`, 49 EN-US markdown files (front-matter + sections, Laws-of-UX style)
- `patterns/pt-br/*.md`, 49 PT-BR markdown files, same slugs (Hugo/Astro multilingual ready)

## Migrating to a real site

- **Astro** (recommended): content collections per locale, i18n routing (`/` EN, `/pt-br/`).
- **Hugo** (what lawsofux.com uses): languages config + per-locale content dirs.

## Content status

All 98 files are complete first drafts. PT-BR is a faithful translation, not a localization pass , 
review for Brazilian market idiom before publishing. Product examples cite behaviors as of early
2026 and should be re-verified.
