# Illustration brief for algorithmic-art

**Project:** Agentic UX Patterns (`aux-patterns`)  
**Date:** 2026-08-13  
**Status:** Handoff brief for `/algorithmic-art`  
**Owner:** Rodrigo Mafra  

**Related:** Discovery brief `docs/designpowers/briefs/2026-08-13-agentic-ux-illustration-style.md` (Approach B still holds).  
**Deep dive:** `docs/designpowers/briefs/2026-08-13-category-illustration-from-loux.md` (30-card LoUX grammar analysis plus locked per-category composition sheets; read before generating, it supersedes the seeds table in this file).  
**Correction:** Do **not** treat the Phase A literal workplace SVGs (`assets/illustrations/categories/cat-*.svg`) as the target craft. Those are too narrative. Target abstraction sits next to **Laws of UX** pattern art.

---

## What to make

A **seeded generative illustration system** (p5.js / algorithmic-art workflow) that produces **abstract, poster-like stills**: one idea per frame, flat geometry, basic shapes, transparency, generous empty space.

Output path for the skill: algorithmic philosophy → interactive seeded viewer → stills we can bake later into the library.

**Phase gate:** 10 category directions first (one seed family + category params). 49 pattern variants later as parametric drills inside the same philosophy. Not 49 new styles.

---

## Abstraction level (critical)

**Like Laws of UX:**
- Conceptual geometry that *evokes* a principle
- Readable in one glance next to a title
- Poster emptiness; calm; editorial
- Metaphor lives in arrangement, weight, tension, overlap, not in depicted furniture or jobs

**Not like what we built before:**
- No literal desks, kitchens, lanyards, mixers, file cabinets, gates, workshop benches
- No Isotype workers, IKEA assembly figures, low-fi UI chrome recreations
- No “scene with a person doing a job”

**Subtle conceptual DNA (algorithmic-art rule):** Someone who knows the category question should feel it in the parameters. Everyone else should still see a strong abstract composition. Quiet reference, not a rebus puzzle of props.

---

## Feel

**Going for:** clear, teachable, professional, calm editorial; LoUX-near craft; soft layering via transparency; one accent hue; empty space as teaching surface.

**Avoiding:** photoreal, 3D gloss, noisy mesh-as-hero, purple glow as brand, stock AI-robot, decorative noise without a readable idea, literal workplace illustration.

---

## System rules (Approach B)

1. **One grammar / one algorithmic philosophy** for the whole library.
2. **Categories differ by:** accent hue (`data/en.json` → `cats[n].hex`) + parametric “subject bias” (forces, density, symmetry break, tension), not by a new drawing style.
3. **Patterns later:** seed / param variants inside the same philosophy.
4. **Light and dark:** same structure; recolor via palette params (do not invert). Meaning must survive hue-off (shape and layout carry the idea).
5. **Violet guardrail:** cats 7 (`#a78bfa`) and 10 (`#818cf8`) are accents only, never canvas or brand field.
6. **Language-light:** no embedded EN/PT labels in the art.
7. **Static bake preferred** for library ship; generative viewer is for exploration and export.

---

## Category conceptual seeds (abstract, not literal)

Use these as **quiet parametric biases**, not scenes to draw:

| # | Category | Hex | Abstract bias (for the algorithm) |
| --- | --- | --- | --- |
| 1 | Identity & Delegation | `#f59e0b` | Mandate boundary; a clear figure vs field; permission edge |
| 2 | Learning & Onboarding | `#34d399` | Threshold / first asymmetry; sparse structure gaining order |
| 3 | Control & Steering | `#f87171` | Directed force; vector dominance; hand-on-system without a hand |
| 4 | Clarification | `#f472b6` | Ambiguity resolving; two states converging; question → settle |
| 5 | Transparency of Process | `#38bdf8` | Sequence / stages visible as structure; process made legible |
| 6 | Transparency of Confidence | `#a3e635` | Gradient of certainty; partial fill / fade of commitment |
| 7 | Multi-Agent Systems | `#a78bfa` | Multiple centers; relay of influence; shared field |
| 8 | Memory & Context | `#22d3ee` | Nested recall; layers of prior state; selective highlight |
| 9 | Failure & Repair | `#fb923c` | Break then mend; interrupted continuity; optional “wrong” variant via param |
| 10 | Governance & Oversight | `#818cf8` | Frame / threshold rule; oversight lattice; check without clipboard |

---

## Algorithmic-art inputs

### Suggested movement name (starting point, skill may rename)

**Editorial Geometry** or **Quiet Mandate** (skill owns final philosophy name).

### Philosophy constraints for the skill

Express through: seeded randomness, basic geometric primitives (circle, capsule, rect, triangle, arc), limited angles, transparency/overlap as depth, empty space ≥40%, one accent hue + neutrals, reproducible seeds.

Emphasize: meticulously crafted, parametric, LoUX-adjacent poster calm. **Not** particle soup for its own sake; **not** figurative staging.

### Seed formula (recommendation)

```
seed = hash("aup-editorial-v1" + "|" + categoryId + "|" + hex)
```

Pattern drills later: append `|" + patternNumber`.

Light/dark: same seed and geometry; swap palette tokens only.

### Parameters the viewer should expose

- `seed`
- `accent` (hex, default category)
- `density` / `emptiness`
- `overlapOpacity`
- `tension` or `asymmetry` (category bias strength)
- `paletteMode` (light paper / dark editorial)
- Optional: `wrongWay` (cat 9 only)

### Craft bar

Each still should feel like a LoUX card sibling: one idea, poster scale, refined restraint. Master-level tuning; controlled chaos, not noise wallpaper.

---

## Success (for generated stills)

- Image + title → reader senses *where the idea applies* or *what kind of responsibility it touches*, without needing a drawn workplace.
- All 10 share one recognisable alphabet; differences read as hue + parametric bias.
- Light and dark twins; grayscale still separates categories by structure.
- No client identity; no violet-as-brand.

---

## Out of scope for this handoff

- Literal job/scene illustration
- Cloning Laws of UX assets or characters (qualities only; their SVGs are ND-licensed)
- Shipping 49 pattern stills in the first generative pass
- Runtime p5 inside the public `index.html` library (explore in algorithmic-art artifact; bake static exports later)

---

## How to run

Invoke `/algorithmic-art` with this file as the input brief.

Ask it to:
1. Write the algorithmic philosophy `.md` from this brief.
2. Build the seeded interactive viewer from its template.
3. Produce explorables for categories 1–10 (shared philosophy, category accent + bias params).
4. Keep abstraction LoUX-near; refuse figurative workplace staging.

---

## Correction log

| Date | Note |
| --- | --- |
| 2026-08-13 | User rejected literal workplace SVGs. Wanted LoUX abstraction + this algorithmic-art handoff brief. |
