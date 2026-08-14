# Illustration strategy: Agentic UX Patterns

**Date:** 2026-08-13  
**Project:** Agentic UX Patterns (`aux-patterns`)  
**Agent:** design-strategist  
**Status:** Locked for design-plan authoring (pipeline mode: auto)  
**Brief:** `docs/designpowers/briefs/2026-08-13-agentic-ux-illustration-style.md`  
**Mood board:** `docs/designpowers/inspiration/2026-08-13-illustration-moodboard.md`

---

## 1. Design principles

### P1. Teach the job, not the vibe

**Principle:** Every still must answer “where does this apply?” or “whose responsibility is this?” in one glance with the title.

**In practice:** Prefer workplace props and role poses (handoff, desk, helm, pass, archive, gate) over abstract geometry alone. The active object gets accent; setting stays muted.

**Rules out:** Decorative mesh heroes, robot mascots, vibe gradients, scenes that only look “AI.”

**How to test:** Cover the definition. Ask three readers (designer, PM, eng) to name a workplace moment or job from image + title. Pass if ≥2 of 3 name a matching domain without guessing from hue.

### P2. One alphabet, many subjects

**Principle:** The library shares one flat-vector grammar; categories differ by accent hue plus analogy domain; patterns later are variants inside that grammar.

**In practice:** Same primitives, grid, figure modules, and camera family for all ten directions. Change pose + prop + setting block, not style.

**Rules out:** Per-category kits, collage, isometric/3D branches, Humaaans-style casual doodle packs as the production look.

**How to test:** Lay all ten category directions in one strip. A stranger should say “same series” before naming differences. Differences must read as subject, not craft.

### P3. Meaning survives without colour (inclusive)

**Principle:** Silhouette, layout, and unique prop carry the metaphor; hue is accent only. Light and dark are first-class twins.

**In practice:** Unique silhouette per category. Recolor via `--illu-*` tokens, never wholesale invert. Categories 7 and 10 violet/indigo accents stay accent-only, never brand canvas or chrome.

**Rules out:** Colour-alone category identity, light-only cream cards, encoding “wrong” as red only, purple glow as library identity.

**How to test:** Gray (hue-off) pass still separates all ten categories by shape. Foreground vs canvas ≥4.5:1 in both themes; large muted shapes ≥3:1. Screen-reader users get title (and optional short description); definition remains the meaning source.

### P4. Empty space is the teaching surface

**Principle:** One idea per still. ≥40% empty. Illustration supports copy; it never replaces it.

**In practice:** Max one human-scale figure + one setting block + 1–2 props. No embedded EN/PT labels in the SVG when avoidable. Caption lives in UI type.

**Rules out:** Collage, multi-step comics as category directions, exploded-view clutter, ambient mesh as teaching art.

**How to test:** Thumbnail at card size (~160–240px wide): metaphor still readable. Cognitive check: reader names one idea, not a storyboard.

### P5. Generate assemblies, ship static

**Principle:** Generative means composing a closed kit; production assets are static baked SVGs (split OK).

**In practice:** Generator (if any) writes files offline. Seed ties grammar version + category + theme so light/dark share structure. Prefer static bake; gate any preview motion on `prefers-reduced-motion`.

**Rules out:** Runtime CDN/p5 as the ship path, freeform Bézier “style generation,” dual PNG as the primary system (fallback only).

**How to test:** Category direction SVGs open offline with no network. Swap theme tokens only; geometry unchanged.

---

## 2. Competitive / reference position

| Reference | We take | We differentiate |
| --- | --- | --- |
| **Laws of UX** | One idea per still, poster empty space, memorisable calm | Dual theme recolor; job/world analogies, not psychology posters; no clone of their characters, cream cards, or layout; no ND asset derivatives |
| **IBM Flat** | Primitives, 8px grid, engineered illustration | Stricter angle set (0/45/90); category hue accents from our `cats` hex; independent editorial site chrome (serif, dark editorial), not IBM blue |
| **Aicher 1972** | Shared figure modules; subject = pose + prop; language beside the mark | Workplace props (desk, gate, archive), not sports bodies; transparency layers + one accent; bilingual captions in UI, not Olympic austerity |
| **Albers** | Opacity/overlap as depth physics for tokens | Never colour-as-the-lesson; silhouette on top of stacking math |
| **Atlassian spots + low-fi UI** | Spot = one concept; low-fi stage for “where it applies”; theme-aware; collage banned | No meeple/skin-tone character system in the 10-direction pass; teaching library, not product empty-state kit |
| **IKEA manuals** | Language-light job teaching; one camera; highlight active part; optional wrong-way for Failure & Repair | Flat vector + empty space, not CAD line density or multi-step strips |
| **Isotype** | Roles/jobs as dignity of work; person + object = responsibility | Soft editorial layering; avoid woodcut heaviness and statistical repetition |

**Position statement:** We sit next to Laws of UX for craft calm, next to IBM Flat + Aicher for production grammar, and next to Isotype/IKEA for *job teaching*. We are not a LoUX clone, not an IBM sub-brand, and not a decorative empty-state pack.

---

## 3. Experience map (illustration system)

Illustrations appear in three primary slots (chrome may evolve; slots are fixed for strategy):

| Slot | Where | Job of the art |
| --- | --- | --- |
| **Index card** | Pattern or category card on browse/index | Instant triage: “is this about my problem?” Thumbnail readability is the bar |
| **Detail hero** | Pattern detail (and category sample when shown) | Confirm the analogy; deepen job mapping while title + definition carry meaning |
| **Category sample** | Category overview / sample strip | Show series grammar: ten siblings, same alphabet, different subjects |

### Journey stages

| Stage | Goal | Feel | Friction if we fail | Exit / recovery |
| --- | --- | --- | --- | --- |
| **0–5 s (first glance)** | Map image + title to workplace moment or job | Calm recognition | Vague vibe art, hue-only difference, busy collage | Reader skips to definition; we failed teaching success |
| **Scan (index)** | Choose which pattern/category to open | Confident triage | Cards look identical or like 10 unrelated styles | Filter by category hue + unique silhouette |
| **Commit (detail hero)** | Confirm fit before deep read | “This is about my work” | Screenshot clones, client-like UI, robot cliché | Title + definition still teach; art is support only |
| **Compare (category strip)** | Trust the system is one library | Series coherence | Mixed kits, violet brand bleed on cats 7/10 | Return to grammar checklist; regenerate from kit |
| **Theme swap** | Same scene in light and dark | Continuity | Invert breaks overlaps; muted fails contrast | Token map + contrast gate before ship |
| **Assistive path** | Get meaning without relying on picture | Equal access | Meaning only in image colour | Accessible name = title; definition is source; optional short description |

**Ability spectrum notes:** Keyboard users never need the image to navigate. Screen-reader users get text equivalent. Colour-vision / bright-sunlight users rely on silhouette + layout. Reduced-motion users get static bake. Bilingual readers get language-light art; EN-US / PT-BR live in UI type.

---

## 4. Locked grammar spec

**LOCKED** from scout handoff (IBM Flat + Aicher + LoUX empty space + Albers opacity physics).

### Primitives

- **Shapes:** circle, capsule, rounded-rect, triangle, 1–2px rule, quarter-arc  
- **Figure modules (shared):** head-circle + capsule torso + two limb capsules  
- **Props:** closed vocabulary per category (see §5); 1–2 props per scene  
- **Depth:** 2–4 layers only; opacity tokens (no drop shadow, no gradient fill as depth)  
- **Low-fi UI stage:** gray/muted rects + sharp corners + one accent object (Atlassian-style analogy stage, not product screenshot)

### Grid and angles

- **Grid:** 8px snap; minimum meaningful shape size 8px (avoid hairline “fake lines”)  
- **Angles:** 0° / 45° / 90° only (stricter than IBM’s six angles for generative reliability)

### Camera rule

- **One camera family** for the whole library: orthographic flat elevation (slight 3/4 allowed only if built from flat shapes, never true perspective or isometric).  
- **One viewpoint per category family** (IKEA-like consistency). Pattern variants later keep the same camera; change prop, second figure, or wrong-way mark only.  
- **Scale:** one human-scale figure for scale; figure is a role module, not a character brand.

### Empty-space and one-idea rules

- **≥40% empty** canvas (LoUX / IBM “don’t work too hard”).  
- **Max:** one human-scale figure + one setting block + 1–2 props.  
- **One idea per still.** No collage. No multi-step comic as a category direction.  
- **Highlight:** active object via `--illu-accent` or stronger fg fill; rest `--illu-muted`.  
- **Language-light:** no baked English/Portuguese words in SVG when avoidable.  
- **Wrong-way:** allowed as optional sibling only for category 9 (Failure & Repair); must use shape + UI label, not colour-alone “red X.”

### Figure and subject rule

- **Subject = pose + prop** (Aicher).  
- Roles via prop + pose (Isotype), not skin tone or gendered clothing as the only cue.  
- Series strip of all ten directions should make the shared alphabet obvious.

### Production

- Static baked SVG preferred; split assets OK.  
- Seed: `hash(grammarVersion + categoryId + theme)` so light/dark share structure.  
- `aup-mesh-v1` retired as teaching; interim chrome only until category directions land.

---

## 5. Locked category analogy domains

**Source:** scout seeds, refined for pose/prop clarity. Marked **LOCKED RECOMMENDATION** (user may reverse; see §10).

Category names and hex from `data/en.json` → `cats`.

| Cat | Name | Hex (accent only) | Job / world | Pose + prop cue (LOCKED RECOMMENDATION) |
| --- | --- | --- | --- | --- |
| 1 | Identity & Delegation | `#f59e0b` | Reception / badge desk; authority handoff | Standing figure extends lanyard or key to second hand or open palm |
| 2 | Learning & Onboarding | `#34d399` | First-day desk | Seated or standing figure at sparse desk; map sheet or empty chair being claimed |
| 3 | Control & Steering | `#f87171` | Helm or mixer booth | Hand on wheel or vertical fader; body oriented to controls |
| 4 | Clarification | `#f472b6` | Two people at one board | Two figures face a shared board; question mark object resolves toward a check mark |
| 5 | Transparency of Process | `#38bdf8` | Kitchen pass / service line | Figure at pass window; ordered steps visible through opening |
| 6 | Transparency of Confidence | `#a3e635` | Dimmer or fill vessel (not rainbow gauge) | Hand on dimmer or vessel with clear fill level; muted surroundings |
| 7 | Multi-Agent Systems | `#a78bfa` | Relay / ensemble | Two figures, one task; baton or shared tool mid-handoff (violet accent only) |
| 8 | Memory & Context | `#22d3ee` | Archive room | Figure at file drawer or pin board; one record pulled forward |
| 9 | Failure & Repair | `#fb923c` | Workshop | Figure with spare part; optional wrong-way sibling (blocked path mark + UI label) |
| 10 | Governance & Oversight | `#818cf8` | Gate / threshold checklist | Figure at gate or threshold with clipboard stamp/checklist (indigo accent only) |

**Series test:** Unique silhouette per row. Hue-off still separates cats 3, 4, 9 (warm family) by prop/pose.

---

## 6. Locked `--illu-*` token map

**Do not invert whole SVGs.** Bind fills to tokens (`fill="var(--illu-…)"`). Dual PNG is fallback only.

| Token | Role | Light (intent) | Dark (intent) | Contrast target |
| --- | --- | --- | --- | --- |
| `--illu-canvas` | Scene ground | Warm off-white / paper | Editorial dark field (site-aligned, not pure black) | Base for all ratios |
| `--illu-fg` | Silhouettes, limbs, metaphor-carrying marks | Near-black | Near-white (not pure `#fff`) | **≥4.5:1** vs `--illu-canvas` in both themes |
| `--illu-muted` | Furniture, low-fi UI, inactive props | Mid gray | Mid-dark gray (not inverted black) | **≥3:1** vs canvas for large shapes (≥3×3 CSS px equivalent at ship size) |
| `--illu-accent` | One active object | `cats[n].hex` | Same hex, or +10–15% lightness if accent-on-canvas fails | Accent object must remain distinguishable; if accent is metaphor-critical, also keep shape cue; prefer **≥3:1** large-shape vs canvas when accent carries “active” highlight |
| `--illu-overlap` | Albers layer fill | Accent or muted at **40–70%** opacity | Same opacity tokens; re-check fg on overlap | Overlap must not drop metaphor-carrying fg below **4.5:1** vs effective background |
| `--illu-rule` (optional) | 1–2px dividers, pass window edges | Dark muted | Light muted | **≥3:1** vs canvas |

**Violet guardrail:** Cats 7 (`#a78bfa`) and 10 (`#818cf8`) use accent token only on the active prop. Never set `--illu-canvas` or site brand chrome to those hues.

**Theme twin rule:** Geometry identical across themes; only token values change.

---

## 7. Success metrics

| Metric | Target | Method |
| --- | --- | --- |
| **Applicability / job mapping** | ≥2 of 3 target readers name matching workplace moment or job from image + title (definition covered) | Moderated or async panel (designer, PM, eng) |
| **Series coherence** | “Same series” named before “different styles” when viewing all 10 | Strip test |
| **Theme parity** | Same scene readable in light and dark; no invert artifacts | Side-by-side review + token checklist |
| **A11y contrast (required)** | Metaphor-carrying marks ≥4.5:1 vs canvas; large muted ≥3:1; both themes | Automated contrast sample on token pairs + spot-check overlaps |
| **Not colour-alone** | All 10 categories separable in hue-off / grayscale | Grayscale export pass |
| **Assistive equivalence** | Every shipped asset has accessible name (= category/pattern title); definition remains available | SR pass on index card + detail |
| **Phase gate** | 10 category directions approved before any of 49 pattern drills | Pipeline checklist |
| **Independence** | Zero client brand / Gemframe-as-brand / client product UI in art | Content audit |
| **Offline** | Assets load with no CDN | Network-blocked smoke test |

---

## 8. Constraints and trade-offs (what we will NOT optimise)

**We will not optimise for:**

- Pixel-perfect Laws of UX brand mirror or Penguin-cover nostalgia as *our* identity  
- Photoreal, 3D gloss, Lottie-as-required runtime, runtime generative preview  
- Shipping all 49 pattern illustrations in the first ship gate  
- Mix-and-match people libraries (Open Peeps / Humaaans look) as the production craft  
- Atlassian meeple skin-tone character systems in the 10-direction pass  
- Ambient mesh / `aup-mesh-v1` as teaching heroes  
- Violet/indigo as library brand (cats 7/10 accent only)  
- Embedded multilingual labels inside SVGs  
- Single-file inline bake of all art into `index.html`  
- Content/copy edits to pattern markdown in this workstream  
- Client-named scenes or proprietary product UI recreations  

**Accepted costs:**

- Less “cute character” warmth than meeple systems  
- Stricter generative limits (closed kit) vs freeform AI illustration  
- Category directions may feel sparse until pattern variants add richness  
- Dual-theme token work costs more than light-only LoUX-like cards  

---

## 9. Phase plan

### Phase A (this gate): 10 category directions

1. Codify grammar + tokens in a short design plan (next agent).  
2. Produce **one direction still per category** (1–10) under the locked grammar and analogy table.  
3. Ship as static SVG (split folder OK), wired to index card / category sample / detail sample slots as plan specifies.  
4. Run contrast, hue-off, series-strip, and offline checks.  
5. Retire mesh as teaching wherever category art replaces it; mesh may remain interim chrome until replaced.

**Exit criteria:** All ten pass success metrics in §7; principles P1–P5 satisfied.

### Phase B (after Phase A exit): 49 pattern drills

1. Treat each pattern as a **variant** inside its category grammar (swap prop, add second figure, wrong-way mark for failure patterns, low-fi UI detail).  
2. Do not invent new styles per pattern.  
3. Keep accessible naming and bilingual UI type rules.

**Explicit non-goal for Phase A:** finishing all 49.

---

## 10. Open flags (user may reverse)

| Flag | Locked recommendation | If reversed |
| --- | --- | --- |
| F1 | Ten analogy domains as in §5 (scout seeds refined) | Rework pose/prop table; keep grammar |
| F2 | Angles limited to 0/45/90 (stricter than IBM) | Allow IBM’s 15/30/60/75 if generator can stay consistent |
| F3 | No mix-and-match people kits as production look | Would reopen Humaaans/Open Peeps; fights editorial calm |
| F4 | No meeple/skin-tone system in Phase A | Defer character diversity rendering to a later pass if desired |
| F5 | Static SVG primary; generator writes files offline | Runtime preview only if gated and still not the ship path |
| F6 | Optional wrong-way sibling only for cat 9 | Extending wrong-way to other cats needs new a11y labels |
| F7 | Warm off-white light canvas (LoUX-adjacent paper) vs pure white | Taste calibration / full `design-taste` still pending |
| F8 | First ship = 10 static SVGs; generator script in-repo optional | Decide in design plan: SVGs-only vs SVGs + small bake script |
| F9 | Asset folder convention (path names) | Design plan must name folder; strategy only requires split OK + offline |

---

## Handoff

**Next:** writing-design-plans / design plan author (then design-lead for visual execution).

**Critical strategic decisions:** Approach B grammar locked (primitives, 8px, 0/45/90, Aicher modules, ≥40% empty, one idea). Ten analogy domains locked as recommended from scout seeds. `--illu-*` token map + contrast targets locked. Phase A = 10 directions before 49.

**Constraints to respect:** Independent identity; cats hex accents; violet 7/10 accent only; meaning not colour-alone; light + dark twins; no em dashes; no client brand in art; static bake preferred.

**design-strategist → writing-design-plans:** Strategy is locked for Auto: one LoUX-near alphabet, ten job-world analogies, and `--illu-*` twins with contrast floors. Please write the design plan that turns §4–§6 into a buildable kit (folder convention, SVG token wiring, Phase A acceptance checklist) without reopening style forks. Watch cats 7 and 10 so violet never becomes brand, and keep mesh out of the teaching hero slot. Hand the plan to design-lead for the ten category stills.
