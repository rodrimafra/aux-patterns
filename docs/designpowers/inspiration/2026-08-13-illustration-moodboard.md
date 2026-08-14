# Inspiration board: Agentic UX Patterns illustration style

**Date:** 2026-08-13  
**Agent:** inspiration-scout  
**Project:** Agentic UX Patterns (`aux-patterns`)  
**Audience:** design-strategist (lock next), then design-lead  
**Mode:** Auto pipeline

---

## 1. Inspiration brief confirmation

**Feel we are going for:** clear, teachable, professional, calm editorial. The analogy lands in one glance. A reader can map the picture to a workplace moment or a job responsibility before they finish the definition.

**Feel we are avoiding:** photoreal, 3D gloss, noisy generative mesh-as-hero, purple glow as identity, stock AI-robot clichés, decoration-without-teaching.

**Taste constraints (this project):** Near Laws of UX craft, not a clone of that brand. Flat vector scenes, basic shapes, transparency, soft layering, generous empty space. Category hue as accent inside theme-aware neutrals. Must recolor for light and dark. Meaning not colour-alone. Independent identity (no client brand, no purple-as-brand). Approach B: one shared grammar. Categories differ by hue plus subject domain. Patterns later are variants.

**Filtered out (interesting, but wrong for this brief):**
- Open Peeps / Humaaans: mix-and-match figure kits are a good *system idea*, the doodle/casual look fights editorial calm.
- unDraw and similar stock packs: recolorable, usually decorative empty-state filler, not teaching analogies.
- Material 3 / IBM isometric 3D: spatial and glossy, violates the flat-vector constraint.
- Atlassian collage and later photoreal-leaning meeples: too much character rendering for a 10-category direction pass.

Went with production-system references (IBM Flat, Aicher, Atlassian low-fi) over character kits. Flag if you would reverse toward mix-and-match people libraries.

---

## 2. Curated mood board (7 references)

### 1. Laws of UX pattern cards

**Source:** [lawsofux.com](https://lawsofux.com/) by Jon Yablonski. Each law is a poster-like graphic: flat geometry, generous empty space, one idea per card. Yablonski has said the graphics were inspired by classic Penguin covers to aid memorization. Assets are CC BY-NC-ND 4.0 (non-commercial, no derivatives).

**Why relevant:** This is the craft north star named in the brief. It proves that a pattern library can teach with a still image plus a title, without screenshots or photoreal people.

**What to take:** One scene, one idea. Basic shapes and transparency instead of illustration noise. Poster-like emptiness so the metaphor reads at thumbnail size. Series identity: same craft, different subject per card.

**What to leave:** Their specific character/icon vocabulary. Light-only cream cards (we must recolor). Penguin-cover nostalgia as *our* brand. Any copy or derivative of their SVGs (ND license). Their layout chrome.

**Taste alignment:** Matches flat vector, empty space, editorial calm. Closest visual neighbour. Risk is cloning, so take qualities only.

**Layer:** Visual + Emotional

**A11y:** Light-only cards fail our dual-theme requirement. Some laws (similarity, proximity) use colour grouping as the metaphor; we must keep shape/layout as the carrier. Image is not a substitute for title plus definition.

---

### 2. IBM Design Language, Flat style

**Source:** [IBM Design Language, Illustration overview](https://www.ibm.com/design/language/illustration/overview/) and [Flat style design](https://www.ibm.com/design/language/illustration/flat-style/design/). Engineered illustration: squares, circles, rectangles, triangles on an 8px grid. Standard angles (15°, 30°, 45°, 60°, 75°, 90°). Curves from quarter/semi/full circles. Minimum shape size 8px so thin bits do not read as lines.

**Why relevant:** This is the most complete *production grammar* for Approach B. It is already a generative-friendly rule set: primitives, grid, angles, “only essential elements,” purpose over decoration.

**What to take:** Primitive kit (circle, rect, triangle, capsule). 8px snap. Standard angles. “Never work too hard or be burdened with too many ideas.” Flat people and objects built from the same geometry. Treat illustration as engineered, not painterly.

**What to leave:** IBM blue as identity. Isometric and Hybrid UI styles (dimension, product chrome). “Delightful / lighthearted” as a required tone (we want calm professional). Their multi-style family (we lock *one* grammar).

**Taste alignment:** Strong. Basic shapes, systematic, teachable. Professional without stock-AI gloss.

**Layer:** Visual

**A11y:** Bold flat colour can drop contrast when overlapping at low opacity. Their diversity guidance is people-representation, not contrast tokens. We still need a luminance pair for every fill in light *and* dark.

---

### 3. Otl Aicher, 1972 Munich Olympic pictograms

**Source:** Aicher and team for the Munich Games. Documented by [Cooper Hewitt](https://www.cooperhewitt.org/2017/12/29/faster-higher-stronger/), [Smithsonian](https://www.smithsonianmag.com/innovation/this-graphic-artists-olympic-pictograms-changed-urban-design-forever-180978256/), and [Munich 72 Collected](https://www.munich72collected.com/post/pictograms-for-munich-1972-poster). One modular grid. Figures from shared head/torso/limb modules. Sports and services use the same alphabet. Grammar groups (one negation bar, spatial border bars). Captions in multiple languages sit *beside* the mark, not inside it.

**Why relevant:** Best historical proof of Approach B. One grammar unifies a series. Categories differ by *what the body is doing* (subject domain), not by a new drawing style. Language-light, bilingual-friendly.

**What to take:** Shared figure modules. Subject = pose + prop, not a new kit. Series poster that shows all marks together so the grammar is obvious. Caption beside the image (EN-US / PT-BR can live in type, not in the drawing). Strict “one way to say no.”

**What to leave:** Pure black-on-white austerity (we have transparency and a category accent). Sports-body vocabulary (we need desks, gates, files, dashboards). Olympic colour system. Stick-figure reduction so far that job context disappears.

**Taste alignment:** Perfect for “one grammar, hue + subject vary.” Geometric, calm, teachable. Not decorative.

**Layer:** Visual (series identity)

**A11y:** High figure/ground contrast in the originals. Some sports share similar silhouettes; they rely on a unique prop (ball, racket) so meaning is not colour. Do not encode category only in hue: keep a unique silhouette per category.

---

### 4. Atlassian in-product illustrations (spot + low-fi UI)

**Source:** [Atlassian Design, Illustrations](https://atlassian.design/foundations/illustrations). Three types: spot (one concept), low-fidelity UI (workflows without screenshots), ambient pattern (background only). Explicit rule: illustration supports the goal, never replaces copy. Image component supports dark mode. Collage banned in-product as too busy.

**Why relevant:** Closest *product* analogue to a teaching library: explain a workflow, empty/error states, onboarding. Low-fi UI (basic shapes, sharp corners, mostly gray, accent sparingly) is a ready recipe for “where this pattern applies” without cloning a real product UI (and without client product chrome).

**What to take:** Spot = one concept per category direction. Low-fi UI as the analogy stage (desk, queue, gate, dashboard made of gray rects + one accent). “Illustration works with the message, not instead of it.” Theme-aware image variants. Ban collage and decorative-only art in the library.

**What to leave:** Atlassian meeple character system and skin-tone rendering (too much identity for our 10-direction pass). Brand personality as a goal. Ambient pattern as teaching art (that is our retired `aup-mesh-v1` role: chrome, not teaching). Their blue identity.

**Taste alignment:** Teaching over decoration is a direct hit. Low-fi UI matches basic shapes. Ambient pattern is a caution: do not let mesh return as the hero.

**Layer:** Visual + Interaction (illustration system rules)

**A11y:** They state excessive illustration raises cognitive load: good. Dark-mode images can be a second asset *or* a tokenized SVG; if they swap PNGs, contrast can drift. Low-fi gray on dark needs a checked muted token, not inverted black. Meaning still needs title + definition.

---

### 5. Josef Albers, *Interaction of Color* (transparence and space-illusion)

**Source:** [The Josef & Anni Albers Foundation](https://www.albersfoundation.org/alberses/teaching/interaction-of-color). Exercises in overlapping rectangles that simulate transparency and stacking without 3D. Homage to the Square as a series: one format, infinite variants. Colour is studied as relational, not as a brand.

**Why relevant:** The brief asks for transparency and a generative system. Albers is the grammar of *opacity as depth*. A generator can layer 2–4 basic shapes, compute overlap fills, and get “soft layering” without gradients or mesh.

**What to take:** Overlap as the only depth cue. A closed set of opacities (for example 100 / 70 / 40). Same composition recolored by swapping the accent and the neutral stack. Series logic: one canvas recipe, many instances.

**What to leave:** Colour-as-the-lesson (our lesson is the workplace analogy). Nested-square compositions with no subject. Optical tricks that fail in dark theme or for colour-vision difference. Painterly paper texture.

**Taste alignment:** Transparency, basic shapes, series variants. Highest generative feasibility of anything on this board. Weakest *teaching* reference, so it is a *material* not a *scene*.

**Layer:** Visual (generative primitives)

**A11y:** Cautionary tale. Albers *intends* colour-alone meaning. We use his stacking math, then put a readable silhouette on top. Overlaps must keep WCAG contrast for the foreground figure against the scene background in both themes. Never let the category hue be the only difference between two categories.

---

### 6. IKEA wordless assembly instructions (wild card)

**Source:** IKEA “informative communicators” in Älmhult. Discussed in [Justin Zhuang, Wordless Instructions](http://justinzhuang.com/posts/wordless-instructions/) and [Sketchboat on the IKEA manual as UX](https://www.sketchboat.com/blog/the-ikea-manual-the-ux-of-building-furniture-and-why-it-works). No (or almost no) words. One viewpoint. Step sequence. Human figure for scale. Occasional “wrong way” glyph. Gray used to highlight the active part.

**Why relevant:** Cross-domain. This is how you teach a physical job in one glance, across languages. Directly serves bilingual readers and “job responsibility” mapping. Sequence and “wrong vs right” map to Control, Clarification, Failure & Repair, Governance.

**What to take:** Language-light scenes. One camera angle per category family. A small human for scale, not a character brand. Highlight the *active* object with accent or a lighter/darker fill, rest in muted neutrals. Optional “wrong way” sibling for Failure & Repair. Test: a person can name the job or the situation without reading the pattern title (title still required in UI).

**What to leave:** 3D CAD line rendering. Multi-step comic strips (one still per category direction). Exploded-view clutter. Their yellow/blue identity. Instructional density that fights generous empty space.

**Taste alignment:** Teaching, analogy, language-light: strong. 3D technical drawing: leave. Empty space must be added back.

**Layer:** Emotional + Interaction (how a teaching image behaves)

**A11y:** Gray-on-white line art can fail contrast, especially in dark theme if naively inverted. Wordless images fail when two parts look alike: we keep unique silhouettes and we never ship the picture without accessible name/description. “Wrong way” needs more than a red X (shape plus label in the pattern UI).

---

### 7. Isotype (Otto Neurath, Gerd Arntz)

**Source:** International System of Typographic Picture Education. Pictograms of workers, industries, and civic roles. Archive: [gerdarntz.org](https://www.gerdarntz.org/content/gerd-arntz.html). Wikipedia overview: [Isotype (picture language)](https://en.wikipedia.org/wiki/Isotype_(picture_language)). Repeatable, combinable signs (worker + factory = that job). Meant to teach across literacy and language.

**Why relevant:** The missing piece in LoUX-like pattern art: *jobs*, not only abstract psychology diagrams. Identity & Delegation, Governance, Multi-Agent, Memory all map to civic/workplace pictograms more honestly than to UI chrome.

**What to take:** People as roles (operator, reviewer, clerk, crew), not as fashion characters. Combinable pictogram logic: person + object = responsibility. Repeatable modules so a generator can assemble scenes. High figure/ground contrast.

**What to leave:** 1930s woodcut heaviness. Statistical repetition (ten identical workers to mean “ten”). Gendered or reductive body defaults. Black-only prints (we layer transparency and a category accent). Treating quantity as the message.

**Taste alignment:** Professional, teachable, independent of tech-product clichés. Geometric enough to sit next to IBM Flat and Aicher. Slightly more “poster civic” than “editorial UX”: keep our empty space and serif site chrome so it does not look like a museum chart.

**Layer:** Emotional (job mapping) + Visual

**A11y:** Strong contrast in originals. Combinatorial signs can be culturally opaque (a visor vs a hard hat). Pair every scene with text. Avoid skin-tone or gendered clothing as the only role cue; use prop + pose.

---

## 3. Group presentation blocks

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  INSPIRATION BOARD
  For: Agentic UX Patterns (teaching illustrations)
  Feel: clear, teachable, professional, calm editorial
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  VISUAL DIRECTION
  ◆ Laws of UX cards: one idea per still, empty space, poster craft
  ◆ IBM Flat style: primitive kit, 8px grid, standard angles
  ◆ Aicher 1972 pictograms: one alphabet, subject = pose + prop
  ◆ Albers transparence: overlap/opacity as the only depth

  INTERACTION PATTERNS (illustration systems)
  ◆ Atlassian spots + low-fi UI: teaching asset types, theme swap,
     illustration supports copy, collage banned in-product
  ◆ IKEA manuals: one viewpoint, highlight the active part,
     optional wrong-way sibling (not a comic strip)

  EMOTIONAL TONE
  ◆ Laws of UX: memorisable, serious, not cute
  ◆ Isotype: dignity of work, civic clarity, no robot mascots

  CROSS-DOMAIN WILD CARD
  ◆ IKEA wordless instructions: job-scale teaching without
     embedded English; bilingual-safe if labels live in UI type

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Closest to the brief’s feel: **IBM Flat (#2)** for grammar, **Aicher (#3)** for series logic, **Laws of UX (#1)** for editorial empty space. Wild card **IKEA (#6)** pushes scenes toward real work instead of abstract posters. **Albers (#5)** is the generator’s physics, not the picture’s subject.

---

## 4. Production notes (generative, recolor, a11y)

### Generative / algorithmic feasibility (flat-vector)

Feasible. Do not generate freeform Bézier “style.” Generate *assemblies* from a closed kit.

**Proposed primitive kit (for strategist / later generator):**
- Shapes: circle, capsule, rounded-rect, triangle, 1px–2px rule, quarter-arc
- Figure: head-circle + capsule torso + two limb capsules (Aicher-like modules)
- Props: closed vocabulary per category (see handoff), 1–2 props per scene
- Depth: 2–4 layers, opacity tokens only (no drop shadow, no gradient)
- Grid: 8px, angles 0 / 45 / 90 (stricter than IBM’s six angles, easier to generate)
- Density: ≥40% empty. Max one human-scale figure + one setting block
- Seed: `hash(grammarVersion + categoryId + theme)` so light/dark share structure

Phase gate stays: 10 category *directions* (same camera, same figure modules, different prop/setting) before 49 pattern variants (swap prop, add a second figure, or a wrong-way mark).

Retire `aup-mesh-v1` as teaching. Mesh may remain chrome only.

Prefer **static baked SVG** for ship. If a generator script lives in-repo, it writes files, it does not run in the reader’s browser.

### Light / dark recolor

Do not invert whole SVGs (Albers overlaps and IKEA grays break).

**Token map to lock next:**

| Token | Role | Light (intent) | Dark (intent) |
| --- | --- | --- | --- |
| `--illu-canvas` | scene ground | paper / warm off-white | editorial dark field |
| `--illu-fg` | silhouettes, limbs | near-black | near-white, not pure |
| `--illu-muted` | furniture, low-fi UI | mid gray | mid-dark gray, still ≥3:1 vs canvas for large shapes |
| `--illu-accent` | one active object | `cats[n].hex` | same hex, or +10–15% lightness if contrast fails |
| `--illu-overlap` | Albers layer | accent or muted at 40–70% | same opacity, check fg on overlap |

Implementation: inline or `<symbol>` SVG with `fill="var(--illu-…)"`. `currentColor` is enough for icons (Primer Octicons), not for multi-fill scenes. Dual PNG export is a fallback, not the system.

Category 7 (`#a78bfa`) and 10 (`#818cf8`) are violet/indigo *accents only*. They are not library identity. Never let those hues dominate canvas or chrome.

### Accessibility

- **Contrast:** Foreground silhouette vs canvas ≥ 4.5:1 for any mark that carries the metaphor. Large muted furniture ≥ 3:1. Check both themes, and hue-off (gray) rendering.
- **Not colour-alone:** Each category keeps a unique silhouette (prop + pose). A deuteranopia pass must still separate categories 3, 4, 9 (red/pink/orange family) by shape.
- **Picture is not the content:** Accessible name = pattern or category title. Short description optional. Definition in text remains the source of meaning (brief users include SR users).
- **Language-light:** No English (or Portuguese) words baked into the SVG when possible. UI type handles EN-US / PT-BR.
- **Motion:** Static bake. If a generator preview ever animates overlap, gate on `prefers-reduced-motion`.
- **Cognitive:** One idea per still (Atlassian + IBM “don’t work too hard”). No collage. No robot mascots.

---

## 5. Suggested analogy domains (input for strategist, not locked)

These are scouting seeds, not decisions. Strategist should lock or replace.

| # | Category | Hue (accent only) | Seed setting | Seed prop / job |
| --- | --- | --- | --- | --- |
| 1 | Identity & Delegation | `#f59e0b` | reception / badge desk | lanyard or key handoff |
| 2 | Learning & Onboarding | `#34d399` | first-day desk | map or empty chair being filled |
| 3 | Control & Steering | `#f87171` | helm or mixer | wheel / fader under a hand |
| 4 | Clarification | `#f472b6` | two figures, one board | question object, then a check |
| 5 | Transparency of Process | `#38bdf8` | kitchen pass / line | window onto steps |
| 6 | Transparency of Confidence | `#a3e635` | weather glass or dimmer | fill level, not a rainbow gauge |
| 7 | Multi-Agent Systems | `#a78bfa` | relay or ensemble | baton / two figures, one task |
| 8 | Memory & Context | `#22d3ee` | archive | file drawer or pin board |
| 9 | Failure & Repair | `#fb923c` | workshop | spare part, wrong-way sibling allowed |
| 10 | Governance & Oversight | `#818cf8` | gate or clipboard | stamp / checklist at a threshold |

---

## 6. Handoff babble

**inspiration-scout → design-strategist:** IBM Flat plus Aicher is the grammar to lock: primitives, 8px grid, shared figure modules, subject = pose + prop, category hue as one accent. Albers is only the opacity physics for light/dark tokens, never the picture’s meaning. Please lock three things next: (1) the ten analogy domains (job/world), I left seeds in the table, (2) the primitive kit and camera rule so a generator cannot invent a new style, (3) the `--illu-*` token map with contrast targets in both themes. Do not let categories 7 and 10 turn violet into the library’s identity.

---

## Artifact

This board: `docs/designpowers/inspiration/2026-08-13-illustration-moodboard.md`
