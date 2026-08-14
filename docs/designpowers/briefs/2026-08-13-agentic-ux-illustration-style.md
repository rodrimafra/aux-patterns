# Design Brief: Agentic UX Patterns illustration style

**Date:** 2026-08-13  
**Project:** Agentic UX Patterns (`aux-patterns`)  
**Owner:** Rodrigo Mafra  
**Status:** Approved discovery brief

## Problem Statement

Pattern library needs teaching images, not abstract decoration. Each illustration should show where the pattern applies in real work, or map to a human job responsibility, so readers relate fast. Style sits near Laws of UX: flat vector scenes, basic shapes, transparency. Assets may split from `index.html`. Ship generative direction per category first (10), then drill to 49 pattern scenes. Light and dark themes both required (recolor, not light-only LoUX cards).

## Users

- Designers and PMs scanning patterns to decide if one fits their product or workflow.
- Researchers and writers who need a fast mental model before reading the definition.
- People mapping patterns to job responsibility (PM, designer, eng, ops, compliance), not only to UI chrome.
- Keyboard and screen-reader users; meaning must not live in the picture alone (title/definition still carry the idea).
- Colour vision / low vision / bright-sunlight readers: theme-aware recolor; contrast in light and dark; shape and layout, not hue alone, carry the teaching metaphor.
- Bilingual readers (EN-US / PT-BR); illustration is language-light, analogy still readable without relying on embedded English labels when possible.
- `prefers-reduced-motion` users if generative motion ever appears (static bake preferred for ship).

## Design Direction

**Approach B:** one shared Laws-of-UX-near grammar for the whole library.

- **Craft:** flat vector scenes; basic shapes; transparency; editorial calm; generous empty space.
- **System:** one shape/transparency language. Categories differ by **accent hue** (existing `cats[n].hex`) plus **analogy subject domain** (what job/world the scene is about). Patterns later = scene variants inside that grammar, not new styles.
- **Theme:** recolor for dark and light; same scene structure, theme token map for fills/strokes/opacity.
- **Job of the image:** teach where the pattern applies, or map to a human job responsibility. Not vibe decoration.
- **Phasing:** ship generative **illustration direction for each of 10 categories** first; then drill to 49 pattern scenes.
- **Production:** generative/algorithmic under that style; assets may live outside single-file bake (split OK).
- **Retire/evolve:** abstract `aup-mesh-v1` arcs+dots no longer the teaching system; may keep only as interim chrome until category directions land, or replace when first kit ships.

## Constraints

- Keep independent identity: no client brand, no Gemframe purple-as-brand, no Verena / Invictus references in art.
- Category accents stay the existing hex system from `data/en.json` → `cats[n].hex`.
- Must work in **light and dark** themes (recolor system, not light-only LoUX paste).
- Teaching meaning must survive without colour: shape, silhouette, layout.
- Prefer **static** baked outputs for ship; respect `prefers-reduced-motion` if any generative preview motion exists.
- Split assets OK; no requirement to keep everything inline in `index.html`.
- Zero runtime CDN for viewing the library still preferred (local/static assets).
- No em dashes in any accompanying copy.
- Examples in pattern content stay real public products; illustrations teach via analogy, not by depicting client work.
- Phase gate: **10 category directions before 49 pattern drills.**

## Existing Design System

Prototype chrome and craft uplift: dark editorial + serif display + per-category hue. Prior imagery: `aup-mesh-v1` algorithmic motifs (interim only for teaching). Tokens and layout live in `index.html` / craft uplift brief. No separate illustration component library yet.

## Taste Direction (Early Signal)

- **North star:** Laws of UX pattern art (feel and craft, not a clone of their brand).
- **Look:** flat vector scenes; basic shapes; transparency; soft layering; calm editorial.
- **Not:** photoreal, 3D gloss, noisy generative mesh-as-hero, purple glow, stock “AI robot” clichés.
- **Colour role:** category hue as accent inside a theme-aware neutral base (dark editorial site + light theme twin).
- **Emotional target:** clear, teachable, professional; analogy lands in one glance.
- Seeds full `design-taste` later; this is early signal only.

## Success Criteria

- Reader can tell **where the pattern applies**, or relate it to a **human job responsibility**, from the image plus title (not from vibe alone).
- All 10 category illustration directions share one recognisable LoUX-near grammar; difference reads as hue + subject, not as 10 styles.
- Same scene reads correctly in **light and dark** (contrast and transparency checked in both).
- Colour-blind / hue-off check: metaphor still readable from shape and layout.
- Generative system can produce category directions first, then pattern variants without inventing a new style language.
- Assets load as static files (split OK); library stays usable offline / without CDN.
- No client identity leakage in any scene.

## Out of Scope

- Shipping all 49 pattern illustrations in this discovery pass (category directions only as first ship gate).
- Pixel-perfect clone of Laws of UX brand, layout, or characters.
- Photoreal / 3D / video / Lottie-as-required runtime.
- Runtime p5/CDN generative preview as the production path.
- Content/copy edits to pattern markdown or definitions.
- Astro/Hugo migration; single-source content refactor.
- Reopening craft-uplift chrome work except where illustration slots need hookup.
- Client-named scenes or proprietary product UI recreations.
