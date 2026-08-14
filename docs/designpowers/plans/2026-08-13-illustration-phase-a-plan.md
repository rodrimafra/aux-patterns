# Design Plan: Agentic UX Patterns illustration system (Phase A)

> **For agentic workers:** REQUIRED: Use designpowers critique against this plan when Phase A tasks complete.

**Goal:** Ship ten category teaching-direction SVGs under one locked LoUX-near grammar, theme-token wired, mesh retired from teaching hero slots.

**Design Direction:** `docs/designpowers/briefs/2026-08-13-agentic-ux-illustration-style.md` + `docs/designpowers/strategy/2026-08-13-illustration-strategy.md`

**Inspiration:** `docs/designpowers/inspiration/2026-08-13-illustration-moodboard.md`

**Personas:** Designers/PMs (job mapping), researchers/writers (fast model), keyboard/SR users, colour-vision/low-vision, bilingual EN-US/PT-BR, reduced-motion (static bake).

**Pipeline mode:** auto

---

## Locked plan decisions (F8 / F9)

| Flag | Decision |
| --- | --- |
| F8 | Phase A ships **10 static SVGs**. Optional offline bake script deferred unless design-lead needs it for consistency; not a runtime path. |
| F9 | Assets live under `assets/illustrations/categories/` |

**Paths:**

- `assets/illustrations/categories/cat-{1..10}.svg` (geometry shared; fills use `var(--illu-*)`)
- Tokens defined in `index.html` (or shared CSS block) as `.theme-light` / `.theme-dark` (or existing theme attribute) mapping `--illu-canvas`, `--illu-fg`, `--illu-muted`, `--illu-accent`, `--illu-overlap`, optional `--illu-rule`
- Per-category accent: set `--illu-accent` to `cats[n].hex` on the card/hero that embeds the SVG

---

## Task 1: Token foundation in chrome

**Files:** `index.html` (CSS custom properties for illustration tokens under light/dark)

- [ ] Add `--illu-*` tokens for light theme (canvas warm off-white, fg near-black, muted mid gray, overlap 40–70%)
- [ ] Add matching dark theme twins (editorial dark canvas, near-white fg, mid-dark muted)
- [ ] Document contrast floors in a short comment: fg ≥4.5:1, large muted ≥3:1
- [ ] Hook: when a category surface is active, set `--illu-accent` to that category hex

**Accessibility check:** Sample computed contrast for fg/canvas and muted/canvas in both themes before drawing scenes.

**Verification:** Theme toggle changes token values; no geometry change required. Offline `file://` still works.

---

## Task 2: SVG template (shared grammar shell)

**Files:** `assets/illustrations/categories/_template.svg` (reference only) or first cat used as template

- [ ] ViewBox on 8px grid (e.g. 240×160 or 320×200; pick one and stick)
- [ ] Layers: canvas rect → overlap shapes → muted setting → fg figure/props → accent prop
- [ ] All fills = `var(--illu-…)` (no hardcoded hex except none; accent via token)
- [ ] No text nodes for EN/PT; `role="img"` + title via embedding `<img alt>` or inline `<title>` matching category name
- [ ] Empty space ≥40% of viewBox

**Accessibility check:** Accessible name = category title when embedded. No colour-alone meaning.

**Verification:** Template validates as SVG; opens offline; theme swap recolors.

---

## Task 3: Category stills 1–5 (Identity through Process)

**Files:**

- `assets/illustrations/categories/cat-1.svg` — lanyard/key handoff
- `assets/illustrations/categories/cat-2.svg` — first-day desk
- `assets/illustrations/categories/cat-3.svg` — helm/mixer
- `assets/illustrations/categories/cat-4.svg` — two figures + board
- `assets/illustrations/categories/cat-5.svg` — kitchen pass

- [ ] Primitives only: circle, capsule, rounded-rect, triangle, rule, quarter-arc
- [ ] Angles 0/45/90; figure = head-circle + capsule torso + limb capsules
- [ ] Subject = pose + prop per strategy §5
- [ ] Max one human-scale figure (cat 4: two figures allowed) + one setting block + 1–2 props
- [ ] Unique silhouette vs other cats

**Accessibility check:** Hue-off sketch still distinguishable; accent only on active prop; cats use warm accents carefully so shape differs.

**Verification:** Thumbnail ~200px wide readable; series strip with 1–5 looks same alphabet.

---

## Task 4: Category stills 6–10 (Confidence through Governance)

**Files:**

- `assets/illustrations/categories/cat-6.svg` — dimmer/fill level
- `assets/illustrations/categories/cat-7.svg` — relay/baton (violet accent only)
- `assets/illustrations/categories/cat-8.svg` — archive
- `assets/illustrations/categories/cat-9.svg` — workshop (+ optional wrong-way sibling `cat-9-wrong.svg` if needed)
- `assets/illustrations/categories/cat-10.svg` — gate/checklist (indigo accent only)

- [ ] Same grammar as Task 3
- [ ] Cats 7 and 10: violet/indigo on accent prop only; never canvas
- [ ] Cat 9 wrong-way (if shipped): shape + UI label plan, not red-only X

**Accessibility check:** Grayscale pass separates all ten; violet never reads as brand field.

**Verification:** Full strip of 10 = “same series”; offline open all files.

---

## Task 5: Wire teaching slots in prototype

**Files:** `index.html` (and any motif helpers)

- [x] Index/category card: show category SVG instead of mesh as teaching visual where category art is the hero
- [x] Detail hero sample: category SVG for patterns in that category (Phase A: category-level art, not 49)
- [x] Keep `aup-mesh-v1` only if still needed as non-teaching chrome; remove from teaching hero
- [x] Ensure `alt` / accessible name = category name (EN from UI strings / DB)
- [x] Light/dark: SVG recolors via tokens

**Accessibility check:** Keyboard path unchanged; image not required for navigation; SR hears category name.

**Verification:** Hard-refresh `file://`: themes, langs, filter, dialog; no CDN; no em dashes introduced.

---

## Task 6: Phase A acceptance checklist

**Files:** optional `docs/designpowers/verification/2026-08-13-illustration-phase-a.md` (checklist results)

- [ ] Applicability smoke: for each cat, one sentence “job/world” matches strategy table
- [ ] Series coherence strip screenshot or note
- [ ] Contrast spot-check both themes
- [ ] Grayscale / hue-off pass
- [ ] Offline / no network
- [ ] Independence audit (no client, no Gemframe-as-brand)
- [ ] Phase gate: no pattern-level drills started

**Accessibility check:** This task *is* the a11y gate.

**Verification:** Checklist complete; failures listed as blockers before Phase B.

---

## Out of this plan

- 49 pattern drills (Phase B)
- Full `design-taste` calibration
- Runtime generative preview
- Content/copy edits to patterns
- Astro/Hugo migration

---

## Agent order (auto)

1. **design-lead** — visual decisions for template + cats 1–10 (composition notes, accent placement); may author or tightly specify SVGs  
2. **design-builder** — implement tokens, SVGs, `index.html` wiring per Tasks 1–5  
3. **content-writer** — skip unless alt strings need PT-BR chrome hooks (prefer existing category names)  
4. **motion-designer** — skip (static bake)  
5. **Reviewers** (after builder): design-critic, accessibility-reviewer, heuristic-evaluator in parallel  
6. Fix round → synthetic checks as needed → verification

## Handoff

**writing-design-plans → design-lead:** Phase A plan is buildable: `assets/illustrations/categories/cat-{n}.svg`, `--illu-*` twins in chrome, mesh out of teaching heroes. Execute visual lock for the shared template then ten stills from strategy §4–§5. Do not reopen Approach B or analogy table unless user reverses an open flag. Hand specs to design-builder for implementation.
