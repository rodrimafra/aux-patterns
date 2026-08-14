# Category illustration brief v2: Laws of UX grammar, phi armature, applied to Agentic UX Patterns

**Project:** Agentic UX Patterns (`aux-patterns`)
**Date:** 2026-08-13
**Version:** v2.1 (supersedes v1 of the same date; v2.1 adds the plate, section 3.3, by owner direction)
**Status:** Owner finals locked in Figma (`g81CTKZNVjYAqhjdVEPji4`, frame `categories` 28:353) and exported to `assets/illustrations/categories/cat-{1..10}.svg`. The recipes below are the probe grammar that led here. They do not override the Figma drawings. Do not run `tools/illustrations/generate.py` against these files.
**Owner:** Rodrigo Mafra

**Relationship to existing artifacts:**

- Deepens the algorithmic-art handoff (`docs/designpowers/briefs/2026-08-13-illustration-algorithmic-art-handoff.md`). Approach B holds. The handoff's one-line "abstract bias" table is superseded by the operators in section 4 and the category sheets in section 5.
- Governs the Editorial Geometry philosophy (`docs/designpowers/algorithmic-art/editorial-geometry-philosophy.md`, family `aup-editorial-v1`). Deltas are declared in section 7.
- Source analysis: 30 Laws of UX reference cards shared by the owner (section 10).

**What changed from v1:** v1 set direction but left colour, scale, and placement as "tuning during the generative pass". That is the gap where a system becomes ten one-off drawings. v2 closes it: one armature, three scales, one colour recipe, six operators, one artwork per category. Every number is derived, measured, and reproducible. Section 8 lists what v2 removed and why.

---

## 1. Purpose

Turn the observed Laws of UX card system into an explicit, reusable composition grammar, then lock one abstract poster per Agentic UX category, in enough numeric detail that a script can draw it and a reviewer can check it. This is the drawing instruction set for the generative pass. No viewer or `index.html` work happens in this pass.

---

## 2. What the Laws of UX cards teach

### 2.1 Card anatomy

Every card is one poster: a saturated hue field carrying a single geometric device, above a near-black panel with the title and a one-sentence definition. Four properties do the work:

1. The graphic states the definition. Cover the text and the device still argues the law.
2. Three tones per card: hue field, muted same-hue companion, one cream accent. Cream always marks the active idea (the lit choice, the current stage, the isolated item).
3. Composition is grid-locked or centered. Symmetry breaks only where the break is the message (a gap, an outlier, an endpoint).
4. The field around the device stays empty. Cards survive as thumbnails beside type.

### 2.2 Hard craft rules (extracted)

1. One device per still. If a still needs two ideas, it is two stills.
2. Primitive alphabet only: circle, bar or capsule, square and rounded square, triangle, thin rule, concentric ring.
3. Three tones: field, muted companion in the field's own hue, one near-neutral accent. The accent marks the active idea, never decoration.
4. Grid-locked or centered placement. Break symmetry only where the break is the meaning.
5. Depth comes from transparency and overlap. No lighting, no gloss.
6. Value gradients appear only as meaning (decay, uncertainty, momentum), never as polish.
7. Most of the field stays empty; the device survives at thumbnail size.
8. Meaning survives grayscale: value contrast carries the figure, hue is atmosphere.

### 2.3 Device families observed

- **Grid plus selective highlight:** Miller, Pareto, Peak-End, Serial Position, Similarity, Choice Overload, Chunking, Hick.
- **Capacity, fill, and fade:** Cognitive Load, Goal-Gradient, Working Memory, Zeigarnik.
- **Concentric focus and ripple:** Fitts, Doherty, Flow, Selective Attention, Common Region.
- **Pattern break and isolation:** Von Restorff.
- **Progressive reduction:** Pragnanz, Occam.
- **Network and lattice:** Mental Model, Tesler.
- **Overlap and filtration:** Cognitive Bias, Postel.
- **Expansion against a boundary:** Parkinson.
- **Grouping by space or line:** Proximity, Uniform Connectedness.
- **Familiar frame stack:** Jakob.
- **Paradox icon:** Paradox of the Active User.
- **Harmonic primitive stack:** Aesthetic-Usability.

Twelve families is an observation, not a specification. Section 4 compresses them into six operators we actually build.

### 2.4 Card-by-card catalog (30 cards)

| Law | Card concept | Composition device | Rule we take |
| --- | --- | --- | --- |
| Miller's Law | Working memory holds 7 plus or minus 2 items | 7x7 dot grid; one row of 7 lit, center 3 brightest | Light a bounded run inside a larger field to show a capacity window |
| Pareto Principle | 20% of causes drive 80% of effects | 5 of 25 dots lit along a diagonal | Make the ratio countable; light the critical few |
| Peak-End Rule | Memory keeps the peak and the end | 4x4 dot sequence; one mid dot and the final dot lit | Treat a grid as a timeline; lit positions carry the rule |
| Serial Position Effect | First and last items stick | 4x4 square sequence; first and last lit | Endpoint emphasis inside a neutral run |
| Law of Similarity | Alike elements read as one figure | 7 cream dots trace a zigzag through a 25-dot grid | Shared value binds scattered marks into a shape |
| Choice Overload | Too many options overwhelm | Dense 5x5 grid, near-checkerboard, no focal point | Uniform density with no hierarchy reads as overwhelm; useful as an anti-state |
| Chunking | Information lands when grouped | 7x7 dot grid split by a stepped diagonal into two masses | One geometric move can partition a field into readable chunks |
| Hick's Law | More choices slow decisions | Cream chip icon in a cleared center of a 6x6 dot grid | A single distinct figure ringed by uniform options shows decision burden |
| Cognitive Load | Mental resources are finite | Seven bars; three lit, four muted | Partial fill of repeated units reads as capacity in use |
| Goal-Gradient Effect | Effort rises near the goal | Bar stack brightening toward one end | A brightness ramp along a sequence shows momentum |
| Working Memory | Held information decays | 3x3 dots fading across the grid | Opacity decay encodes time and forgetting |
| Zeigarnik Effect | Unfinished tasks stay salient | Six full muted bars, one short cream bar | The incomplete element is the brightest thing on the card |
| Fitts's Law | Target time depends on distance and size | Thin-line bullseye with a solid center dot | Concentric rings plus a center dot read as acquisition |
| Doherty Threshold | Fast feedback keeps both sides flowing | Rings radiating from a bright center dot | Radiation from a point reads as response |
| Flow | Full immersion in an activity | Nested squares brightening to the center | Recession toward a lit center reads as being drawn in |
| Selective Attention | We see what serves the goal | Offset concentric circles rising to a bright hotspot | A spotlight gradient models attention |
| Law of Common Region | Boundaries create groups | Darker square region holds a dot grid; one bright dot still belongs | A drawn boundary outranks colour difference; containment is belonging |
| Von Restorff Effect | The different one is remembered | 15 muted squares, one cream circle | Break the pattern in shape and value at exactly one position |
| Law of Pragnanz | We settle on the simplest reading | Hexagon web simplifying stepwise to a bare circle | A reduction sequence shows interpretation settling |
| Occam's Razor | Fewest assumptions wins | Four cells: five, three, two overlapping blobs, then one solid circle | Stage a reduction race; light the simplest cell as the winner |
| Mental Model | A compressed model of a system | Hexagonal network: center node, six neighbours, thin edges | A small regular network reads as structured understanding |
| Tesler's Law | Some complexity cannot be removed | Hexagon with every vertex joined to every other | A saturated lattice reads as irreducible complexity |
| Cognitive Bias | Judgment passes through hidden filters | Translucent circles overlap into an eye with a bright pupil | Transparency stacks read as filtered perception |
| Postel's Law | Liberal input, conservative output | Triangle grid, cream top row fading and overlapping downward | A tolerance gradient reads as intake refined into stricter output |
| Parkinson's Law | Work inflates to fill the time | Diamond outline, center dot, four outward arrows | Outward vectors against a boundary read as inflation to fit the container |
| Law of Proximity | Near things group | 12-dot block, then a separated 4-dot column | The gap is the message; spacing alone forms groups |
| Law of Uniform Connectedness | Connected means related | Dots seated on shared thin circles | A shared line binds its occupants into a group |
| Jakob's Law | Users expect the familiar | Three identical square frames stepped diagonally | Repeating one frame says conventions transfer across contexts |
| Paradox of the Active User | People use first, read never | Penrose triangle in three tones | One impossible object can name a paradox |
| Aesthetic-Usability Effect | Pleasing reads as usable | Circle, square, and triangle stacked in classical balance | Harmony among primitives can itself be the subject |

---

## 3. Shared production rules

Everything in this section is fixed for all ten stills. A category may not opt out.

### 3.1 One grammar

Editorial Geometry (`aup-editorial-v1`) is the single algorithmic philosophy. Primitives: circle, capsule, rect, rounded rect, triangle, thin rule, quarter-arc. Nothing else. Construction coordinates (shape centres, rect origins, rule endpoints) and every size snap to the 8px grid. Angles are 0, 45, or 90 degrees only; quarter-arcs allowed.

One consequence, stated so nobody reads the emitted SVG as a mistake: sizes 24, 40, and 104 are odd multiples of 8, so centring one on the armature puts the derived edge on the 4px half-step. A 24px mend centred on x = 120 emits `x="108"`. Construction stays on 8; only derived edges land on 4, and the generator verifies exactly that. Depth comes from flat fill plus opacity and overlap, never from shadow, blur, filter, or gradient. Seeded randomness chooses among legal placements; it never invents a mark.

### 3.2 Frame and the phi armature

Frame is 320x200, which is 8:5, two adjacent Fibonacci numbers, so the frame sits 1.11% off phi while staying exactly on the 8px grid.

Golden sections of each edge, snapped to the grid:

| Axis | Exact section | Snapped | Snap error |
| --- | --- | --- | --- |
| x | 122.23 | 120 | 1.82% |
| x | 197.77 | 200 | 1.13% |
| y | 76.39 | 80 | 4.72% |
| y | 123.61 | 120 | 2.92% |

The grid wins ties. Snap error is stated, not hidden: this is a rounded armature, not a golden-ratio claim.

Four crossings result:

| Anchor | Coordinates |
| --- | --- |
| A | (120, 80) |
| B | (200, 80) |
| C | (120, 120) |
| D | (200, 120) |

**Rule:** each still's focal element (the single cream mark, or the lit stage of a sequence) is centered on its assigned anchor. The armature is never drawn.

### 3.3 The plate (series module, owner direction)

Every device is contained in one drawn perfect square, the plate: 168x168, stroke 2, sharp corners. Baseline: the cat 10 review variant with outlined cells and a stroke 2 boundary, generalized to the whole series by owner direction.

168 is the largest scale value and a Fibonacci square: 64 + 104 = 168, so the plate's own golden sections land exactly on 64 and 104 from its origin, on the 8px grid, with no snapping. The plate nests in the canvas armature:

| Anchor group | Plate origin | Anchor lands on plate crossing |
| --- | --- | --- |
| A, C (x = 120) | (56, 16) | (64, 64) for A; (64, 104) for C |
| B, D (x = 200) | (96, 16) | (104, 64) for B; (104, 104) for D |

Vertically the plate is always centered (16px margins both sides, exact, because 80 - 64 = 120 - 104 = 16). Horizontally it shifts 20px left of canvas center for A and C anchors and 20px right for B and D, so the wall alternates in pairs following the locked anchor sequence. The category's focal mark therefore sits simultaneously on the canvas armature and on the plate's internal golden crossing.

Rules:

- The plate is drawn first, in mute on mode A stills and cream on mode B stills (structure follows the card's tone roles; cream stays unique as the focal mark on mode A).
- All device ink stays inside the plate with at least 8px of clearance, verified per shape by the generator. Nothing touches or crosses the boundary.
- The plate counts against the ink budget. The field rect still does not.
- The plate is chrome, never the focal element, with one exception: category 10, where the plate is the policy boundary the operator calls for, so it doubles as the device's containment and no second boundary is drawn.

### 3.4 Anchor assignment (low-discrepancy, not taste)

Anchors are assigned by additive recurrence, the one property of phi that is provably useful here: `frac(n / phi)` distributes n points more evenly across an interval than random choice does. Map the fractional part into four buckets, buckets to anchors A, B, C, D:

| Cat | frac(n / phi) | Anchor |
| --- | --- | --- |
| 1 | 0.6180 | C (120, 120) |
| 2 | 0.2361 | A (120, 80) |
| 3 | 0.8541 | D (200, 120) |
| 4 | 0.4721 | B (200, 80) |
| 5 | 0.0902 | A (120, 80) |
| 6 | 0.7082 | C (120, 120) |
| 7 | 0.3262 | B (200, 80) |
| 8 | 0.9443 | D (200, 120) |
| 9 | 0.5623 | C (120, 120) |
| 10 | 0.1803 | A (120, 80) |

Distribution lands at A=3, B=2, C=3, D=2. No anchor is used twice in a row, so the wall never repeats a focal position on adjacent cards. This table is reproducible from one line of arithmetic; it is not a layout opinion.

### 3.5 Three scales

- **Size (Fibonacci times 8):** 8, 16, 24, 40, 64, 104, 168. Every diameter, side, length, and thickness comes from this set. Each value is a multiple of 8, so the additive scale and the grid never fight.
- **Stroke:** 1, 2, 3, 5. Exempt from the 8px rule.
- **Opacity (powers of 1/phi):** 1.0, 0.62, 0.38, 0.24, 0.15, 0.09. Opacity encodes meaning (decay, uncertainty, recession), never polish. Because `1/phi + 1/phi^2 = 1` exactly, a mark at 0.62 and its complement at 0.38 partition a value cleanly, which is what the decay and reduction operators need.

### 3.6 Ink budget

Frame area is 64000 px2. Painted area is capped at `64000 / phi^2 = 24446 px2`, so at least 61.8% of every still stays empty. The generator measures painted area per still and reports it. Over budget means remove elements, not shrink the margin.

This replaces v1's "at least 40% empty". Emptiness is now a measured gate, not an intention.

### 3.7 One colour recipe, two modes

Base tokens: ink `#14161b`, cream `#f2eee2`, neutral field `#242730`.

**Mode A (categories 1, 2, 3, 4, 5, 6, 8, 9), hue as field:**

- `field` = category hex mixed at `1/phi^2` (38.2%) over ink.
- `mute` = that field mixed at `1/phi^2` (38.2%) over ink again.
- `mark` = cream `#f2eee2`, on exactly one element.

**Mode B (categories 7 and 10), neutral field:**

- `field` = neutral `#242730`. Violet and indigo never become ground.
- `mute` = cream mixed at `1/phi^3` (23.6%) over the neutral field.
- `mark` = cream. The category hue lands on exactly one element.

One fraction, applied twice, generates every field and mute in the library. There is no per-category colour tuning, no eyeballing, and no palette file to drift. Computed values:

| Cat | Hue | Mode | Field | Mute | Mark vs field | Mute vs field |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `#f59e0b` | A | `#6a4a15` | `#352a19` | 6.95 | 1.74 |
| 2 | `#34d399` | A | `#205e4b` | `#19322d` | 6.55 | 1.80 |
| 3 | `#f87171` | A | `#6b393c` | `#352328` | 7.96 | 1.60 |
| 4 | `#f472b6` | A | `#6a3956` | `#352332` | 7.76 | 1.62 |
| 5 | `#38bdf8` | A | `#22566f` | `#192e3b` | 6.89 | 1.76 |
| 6 | `#a3e635` | A | `#4b6525` | `#29341f` | 5.68 | 1.99 |
| 7 | `#a78bfa` | B | `#242730` | `#55565a` | 12.86 | 2.04 |
| 8 | `#22d3ee` | A | `#195e6c` | `#16323a` | 6.33 | 1.84 |
| 9 | `#fb923c` | A | `#6c4528` | `#362820` | 7.19 | 1.70 |
| 10 | `#818cf8` | B | `#242730` | `#55565a` | 12.86 | 2.04 |

### 3.8 Contrast floors (measured, not aspirational)

| Relation | Floor | Measured |
| --- | --- | --- |
| Mark vs field | 4.5:1 | 5.68:1 (cat 6) to 12.86:1 (cats 7, 10) |
| Mute vs field | 1.5:1 | 1.60:1 (cat 3) to 2.04:1 (cats 7, 10) |
| Mode B accent vs field | 3:1 | 5.48:1 violet, 5.00:1 indigo |

Marks clear the WCAG non-text requirement of 3:1 at nearly double the margin across every category, which is why v1's per-hue tuning became unnecessary. Mutes are deliberately recessive: they sit above the perceptual floor where a shape still reads as a shape, and below the level where they compete with the mark. Grayscale export must still separate the device silhouette.

### 3.9 One artwork, both themes

A single SVG per category serves light paper and dark editorial. The still carries its own field, so it reads as a dark plate on light paper and as a soft-edged plate on dark chrome. No light twin, no dark twin, no theme-swapped duplicate, no CSS variables inside the art. Colours are baked literal hex.

This halves the asset count and removes the class of bug where one theme's twin drifts out of compliance.

### 3.10 Bans

No human figures, desks, kitchens, badges, lanyards, clipboards, gears, robots, avatars, brains, folders, bandages, magnifying glasses, warning triangles, X marks. No UI chrome recreations. No text, letters, numbers, or logos inside the artwork. No gradients, filters, blur, or shadows. No violet or indigo ground. No cloning of Laws of UX assets (qualities only, see section 10). No em dashes in any copy around the art.

### 3.11 Seeds

`seed = hash32("aup-editorial-v1|" + categoryId + "|" + hex)`, matching `tools/motifs/bake.py`. Pattern drills append `|patternNumber`. Re-running a generator produces byte-identical files.

---

## 4. Six operators

Ten categories, six composition machines. The operator is the machine; hue and parameters make the category. A new operator requires reopening this brief.

| Operator | Meaning | Used by |
| --- | --- | --- |
| **Containment** | A drawn boundary creates belonging. A muted frame holds the focal mark. | 1, 10 |
| **Sequence** | An ordered run of marks where exactly one is lit. | 2, 5, 9 |
| **Vector** | One directed force travels to a target and stops. | 3 |
| **Reduction** | Overlapping ambiguity resolves into one solid simple mark. | 4 |
| **Decay** | A monotonic opacity ramp encodes certainty or recall. | 6, 8 |
| **Relay** | Several centers joined by thin rules pass influence between them. | 7 |

Two categories sharing an operator are separated by hue, anchor, parameters, and silhouette, which is the same discipline that lets Laws of UX run eight grid cards without repetition.

---

## 5. Category sheets (locked)

Each still: field rect, then the plate (3.3), then the device inside it, then exactly one cream focal mark on the assigned anchor. Everything else stays empty. Plate origins per sheet follow from the anchor: (56, 16) for A and C, (96, 16) for B and D.

### 5.1 Category 1: Identity & Delegation

**Question:** What is this agent allowed to be?
**Hue:** `#f59e0b` amber. Mode A. Field `#6a4a15`, mute `#352a19`.
**Operator:** Containment. **Anchor:** C (120, 120).
**Serves:** 1.1 Agent identity & role contract, 1.2 Delegation modes.

**Concept:** a mandate made visible. The boundary, not the occupant, is the subject.

**Recipe:** inside the plate, one held contract frame (rounded rect 104px, stroke 3, mute, at 64, 40) and one ghost contract (rounded rect 104px, stroke 2, mute at 0.62, at 88, 64), stepped 24px diagonally so the two read as two: the contract transfers. The mandate, one cream rounded rect or circle, 40px, sits at C inside both. Containment within containment is the operator's own story; the plate is the outermost layer of it.

**Do:** crisp boundary; exactly one cream mark; asymmetric frame placement.
**Don't:** badges, keys, ID cards, figures; a second accent; texture inside the frame; centering everything.

**Drill knobs (Phase B):** frame count and nesting depth (1.1 one firm contract frame; 1.2 two or three frames at different sizes, looser modes drawn with a thinner edge); mark position, deep inside versus pressed against the edge; boundary weight.

**Craft siblings:** Law of Common Region, Jakob's Law.

### 5.2 Category 2: Learning & Onboarding

**Question:** How do people learn what an agent can do?
**Hue:** `#34d399` emerald. Mode A. Field `#205e4b`, mute `#19322d`.
**Operator:** Sequence. **Anchor:** A (120, 80).
**Serves:** 2.1 Sandboxed playgrounds, 2.2 Wayfinders, 2.3 Progressive disclosure modes, 2.4 Teach-me interfaces, 2.5 Scenario templates & recipes, 2.6 Feedback & rating controls.

**Concept:** sparse structure gaining order. The first step is lit; the path ahead is sketched but not yet earned.

**Recipe:** a staircase of 5 squares, 16px, pitch 24, rising left to right from (96, 88), each step 8px higher than the last. The second step lands on A and is cream at full opacity, with one climbed mute step behind it; later steps fade down the ladder (0.62, 0.38, 0.24) in mute. The plate's upper right stays empty: room not yet learned.

**Do:** growth direction reads in one glance; monotonic ramp.
**Don't:** mazes, maps, books, arrow clusters; full grids; more than one lit step.

**Drill knobs (Phase B):** step count; ramp position (2.3 shifts the ramp midpoint; 2.1 places the staircase inside a light containment frame; 2.2 traces a thin rule ahead of the lit step; 2.6 adds a small return arc from a later step back toward the lit one).

**Craft siblings:** Chunking, Goal-Gradient Effect.

### 5.3 Category 3: Control & Steering

**Question:** How do people stay in charge?
**Hue:** `#f87171` coral. Mode A. Field `#6b393c`, mute `#352328`.
**Operator:** Vector. **Anchor:** D (200, 120).
**Serves:** 3.1 Kill switch, pause & resume, 3.2 Human-in-the-loop gates, 3.3 Plan-then-execute workflow, 3.4 Steerability & polite interruption, 3.5 Scoped permissions & tool consent, 3.6 Rollback & version history, 3.7 User-directed tool use.

**Concept:** directed force without a hand. Control is the applied direction.

**Recipe:** a concentric target (two mute rings, radii 40 and 24, both stroke 3: cat 3 has the faintest mute of the ten, hairlines vanish) centered on D with a cream centre dot, 16px. One straight cream rule (stroke 3) crosses the plate from its inner clearance at x = 104 along y = 120 and stops at x = 184, a visible 8px short of the dot edge.

**Do:** one vector; a visible stop point.
**Don't:** steering wheels, joysticks, hands, stop signs; competing arrows; outward Parkinson arrows.

**Drill knobs (Phase B):** vector length and entry angle; stop treatment (3.1 halts short of the dot; 3.2 crosses one perpendicular rule before the target; 3.3 runs dashed then turns solid at the midpoint; 3.5 rings the target with a partial boundary arc; 3.6 adds a thin reversed echo vector).

**Craft siblings:** Fitts's Law, Doherty Threshold, Parkinson's Law (inverted).

### 5.4 Category 4: Clarification

**Question:** What happens when it doesn't know enough?
**Hue:** `#f472b6` pink. Mode A. Field `#6a3956`, mute `#352332`.
**Operator:** Reduction. **Anchor:** B (200, 80).
**Serves:** 4.1 Structured clarification prompts, 4.2 Edit request, 4.3 Confirmed assumptions.

**Concept:** ambiguity settling into one confirmed state.

**Recipe:** a left to right settle sequence of three groups on the y = 80 line: three overlapping mute circles, 16px, at 0.38 (centers 112, 120 with 8px jitter, 128), then two overlapping mute circles, 16px, at 0.62 (centers 160, 168), then the resolved cream circle, 40px, centered on B at full opacity. Ambiguity is smaller and fainter; the resolution is the largest and brightest thing on the card.

**Do:** transparency only in the unresolved groups; monotonic reduction.
**Don't:** question marks, speech bubbles, chat UI; more than one solid resolution.

**Drill knobs (Phase B):** overlap count and sequence length (4.1 keeps three even groups; 4.2 nudges the middle group out of line before settling; 4.3 gives the resolved circle one thin confirmation ring).

**Craft siblings:** Occam's Razor, Law of Pragnanz.

### 5.5 Category 5: Transparency of Process

**Question:** What is it doing right now?
**Hue:** `#38bdf8` sky. Mode A. Field `#22566f`, mute `#192e3b`.
**Operator:** Sequence. **Anchor:** A (120, 80).
**Serves:** 5.1 Reasoning glimpse, 5.2 Streaming results visualizations, 5.3 Tool usage indicators, 5.4 Activity timeline & audit log, 5.5 Execution progress view, 5.6 Confessions view.

**Concept:** a sequence made legible. The current stage is the only lit one.

**Recipe:** one horizontal mute baseline rule (stroke 1) from (64, 80) to (208, 80) carrying 6 stage circles, 16px, pitch 24 from x = 72. Stages before A are mute at 0.62; the stage on A is cream at full opacity and 24px; stages after A fade 0.24, 0.15, 0.09.

**Do:** time reads left to right; even spacing; one lit stage only.
**Don't:** spinners, gears, terminal text, log lines, progress percentages.

**Drill knobs (Phase B):** stage count and lit position (5.5 lights a late stage; 5.1 enlarges the lit stage and adds a thin aperture ring; 5.4 runs a longer, denser row; 5.2 trails the lit stage with two ghost marks; 5.6 drops one earlier stage half a step below the baseline).

**Craft siblings:** Serial Position Effect, Peak-End Rule, Goal-Gradient Effect.

### 5.6 Category 6: Transparency of Confidence

**Question:** How sure is it, and why?
**Hue:** `#a3e635` lime. Mode A. Field `#4b6525`, mute `#29341f`.
**Operator:** Decay. **Anchor:** C (120, 120).
**Serves:** 6.1 Source anchoring & grounding, 6.2 Confidence thermometer, 6.3 Semantic highlighting of uncertainty, 6.4 Multiple presented options, 6.5 Explanation on demand, 6.6 Counter-evidence.

**Concept:** partial commitment shown honestly: how much is grounded versus uncertain.

**Recipe:** six vertical bars, 16px wide and 64px tall, midline at y = 120, pitch 24 from x = 72. Bars up to and including the one on C are cream at full opacity; later bars step down 0.38, 0.24, 0.15 in mute. The break point carries the message; opacity is the second cue, so meaning survives hue-off.

**Do:** one continuous ramp; five to nine bars.
**Don't:** gauges, dials, traffic lights, percentage labels.

**Drill knobs (Phase B):** fill ratio (6.2 varies it); a dropped bar (6.3 sets one mid bar at low opacity inside an otherwise solid run); mirrored bars (6.6 reflects one bar below the baseline); a grounding tick (6.1 seats a small solid square under the solid run).

**Craft siblings:** Cognitive Load, Working Memory, Zeigarnik Effect.

### 5.7 Category 7: Multi-Agent Systems

**Question:** What happens when there's more than one?
**Hue:** `#a78bfa` violet. Mode B. Field `#242730`, mute `#55565a`.
**Operator:** Relay. **Anchor:** B (200, 80).
**Serves:** 7.1 Orchestration graph, 7.2 Agent registry & profiles, 7.3 Supervisor agent, 7.4 Agent handover briefs, 7.5 Assignment boards & work queues, 7.6 Escalation & fallback routing.

**Concept:** several centers sharing one field; influence relayed between them.

**Recipe:** four cream nodes (24px circles) at (120, 128), (152, 128), (200, 80) and (232, 80 or 112 by seed), joined by three thin cream rules (stroke 1, legs at 0 or 45 degrees) into an open relay, never a closed lattice. The node on B is the handover and is the only violet element. Air inside the plate does the multi-agent talking.

**Do:** open graph, generous spacing; one violet element; evenly sized nodes.
**Don't:** violet canvas; org charts, robots, avatars; a saturated full lattice (that is Tesler's irreducibility, the wrong story).

**Drill knobs (Phase B):** node count and relay shape; which element takes violet (7.3 accents the topmost node; 7.4 accents the connecting edge; 7.6 shifts the accent up a rising edge; 7.1 branches the relay; 7.5 seats the nodes along one rule).

**Craft siblings:** Mental Model, Law of Uniform Connectedness.

### 5.8 Category 8: Memory & Context

**Question:** What does it know about me?
**Hue:** `#22d3ee` cyan. Mode A. Field `#195e6c`, mute `#16323a`.
**Operator:** Decay. **Anchor:** D (200, 120).
**Serves:** 8.1 Memory inspector & editor, 8.2 Preference persona settings, 8.3 Privacy & data usage controls, 8.4 Context repository & workspace profiles, 8.5 Personal context profiles.

**Concept:** layers of prior state; one remembered thing brought forward for inspection.

**Recipe:** a recall stack of four mute capsules, 64px long and 16px thick, at x = 104, stacked 24px apart from y = 56, receding 0.62, 0.38, 0.24, 0.15 downward (older equals fainter). One cream mark, 40px (circle or capsule by seed), is pulled forward and clearly detached, centered on D: the inspected memory.

**Do:** recession by even opacity steps; the recalled mark visibly offset; keep the stack quiet.
**Don't:** brains, folders, databases, clocks; more than one pulled mark.

**Drill knobs (Phase B):** layer count; source depth of the pulled mark (8.1 adds one thin ring to it; 8.3 draws one layer as an outlined boundary instead of a fill; 8.4 runs two stacks sharing one pulled mark; 8.2 seats the pulled mark closest to the stack).

**Craft siblings:** Working Memory, Selective Attention, Law of Common Region.

### 5.9 Category 9: Failure & Repair

**Question:** What happens when it gets it wrong?
**Hue:** `#fb923c` orange. Mode A. Field `#6c4528`, mute `#362820`.
**Operator:** Sequence. **Anchor:** C (120, 120).
**Serves:** 9.1 Safe failure states, 9.2 Guided repair flows, 9.3 Sentiment-aware response styles, 9.4 Apology & remedy bundle.

**Concept:** continuity interrupted, then mended. The break is honest; the repair is visible.

**Recipe:** an unbroken run along y = 120, 16px thick, in two mute capsules (24px from x = 64, then 64px from x = 152 to the plate's inner clearance), interrupted once by a 64px break. One cream capsule, 24px, centered on C, sits inside the break: the mend, leaving 20px of shoulder on each side. Crisp end faces.

**Why these numbers:** the run carries no interior joints, so the break is the only spacing in the still. An earlier version broke a three-capsule run and seated a 24px mend in a 40px gap, which left 8px shoulders, exactly the width of the run's own joints. The break stopped reading as an event, the still collapsed into a rhythm of dashes with one lit, and the operator's meaning fell back onto hue alone. Shoulders must stay wider than any other gap in the run, or there is no break.

**Do:** one break; the mend is the only cream element.
**Don't:** warning triangles, X marks, bandages; colour-alone failure signalling.

**Drill knobs (Phase B):** gap position along the run; mend state (9.1 caps the gap with two end stops and no mend yet; 9.2 slides the cream segment into the gap; 9.4 seats the mend plus one small cream dot beside it, the remedy; 9.3 loosens the bar spacing around the gap).

**Craft siblings:** Zeigarnik Effect, Von Restorff Effect.

### 5.10 Category 10: Governance & Oversight

**Question:** How does an organisation supervise a fleet?
**Hue:** `#818cf8` indigo. Mode B. Field `#242730`, mute `#55565a`.
**Operator:** Containment. **Anchor:** A (120, 80).
**Serves:** 10.1 Fleet health dashboard, 10.2 Risk & policy heatmaps, 10.3 Access & permission tiers for agents, 10.4 Workflow & policy template library.

**Concept:** a lattice watched from above; the checked cell is the act of oversight.

**Recipe:** the plate itself is the policy boundary (cream, stroke 2, per mode B tone roles), and no second boundary is drawn. Inside it, an even 4x4 lattice of outlined mute cells (16px squares, stroke 2, pitch 24 from center 96, 56). Exactly one cell, the one on A, is a filled indigo square: the cell under review. Calm rhythm, no heatmap. This card is the series baseline the plate rule generalizes from.

**Do:** even rhythm; a single indigo element; crisp outer frame.
**Don't:** indigo canvas; dashboards, gauges, magnifying glasses, clipboards; heatmap rainbows.

**Drill knobs (Phase B):** lattice size; accent position (10.1 lights one cell in an even grid; 10.2 steps two or three cells in opacity while only one takes indigo; 10.3 sets the lattice rows at three opacity tiers; 10.4 outlines one cell and repeats it as a ghost outside the frame).

**Craft siblings:** Tesler's Law, Pareto Principle, Law of Common Region, Von Restorff Effect.

---

## 6. Where phi is load-bearing, and where it is not

Stated plainly so nobody inherits a superstition.

**Load-bearing (mathematical properties we use):**

- **Additive plus geometric scale.** Fibonacci times 8 is the only integer sequence that is both additive and near-geometric while landing on the 8px grid. Sizes relate by construction.
- **Complementarity.** `1/phi + 1/phi^2 = 1` exactly, so the opacity ladder partitions a value without a leftover.
- **Low-discrepancy distribution.** `frac(n / phi)` spreads n choices more evenly than random. This is what assigns the anchors (3.4) and it is a real, provable property.
- **The Fibonacci plate.** 64 + 104 = 168, so the 168 square's internal golden sections sit exactly on the 8px grid with zero snap error, and the plate nests in the canvas armature with the focal anchor on one of its own crossings (3.3).
- **Numeric constraint generation.** One fraction (38.2%) generates every field and mute, so the palette cannot drift.

**Not load-bearing (claims we refuse to make):**

- Phi is not "naturally beautiful". Perceptual research does not support a preferred rectangle ratio.
- Phi does not decide what a still means. The operator and silhouette do.
- Phi does not override the grid. Every section is snapped, with error stated in 3.2.

We use phi as a constraint generator, because a system that derives its numbers is auditable, and a system that eyeballs them is not.

---

## 7. Declared deltas against philosophy v1

The philosophy doc (`aup-editorial-v1`) inherits these:

1. **Colour deployment is two-mode.** v1 said accent hue lands on the active mark alone for every category. The LoUX analysis shows the hue field is what makes a wall read as one collection with ten voices, so eight categories move their hue into the field and use cream as the active mark. Violet and indigo still never become ground.
2. **One artwork, not light and dark twins.** See 3.9.
3. **Emptiness is measured.** "At least two-fifths" becomes a hard 61.8% floor with a reported number.
4. **The plate (v2.1).** Every device is contained in a drawn 168x168 square nested in the armature, per owner direction. The philosophy's "field mass" role is now carried by the plate.

---

## 8. What v2 removed, and why

Less, but better. Each cut buys something specific.

| Removed | Why |
| --- | --- |
| Light and dark twins per category | One artwork proves out in both themes. Twenty assets become ten, and a whole class of drift bug disappears. |
| Twelve device families | Six operators cover ten categories. Fewer machines, better tuned. |
| Per-category colour tuning | One fraction generates all twenty values and clears the floors everywhere. Tuning was an invitation to drift. |
| The "wrong-way sibling" graphic (cat 9) | It existed to say what not to do, and was never going to be published. Unbuilt is better than unused. |
| "At least 40% empty" | Replaced by a measured 61.8% gate. An intention nobody checks is not a rule. |
| CSS variables inside the art | Baked hex is honest about what the file is: a fixed plate, not a themeable component. |

---

## 9. Phase gate and success criteria

**Gate:**

1. Generate the ten stills from these sheets by deterministic script (one philosophy, ten parameter sets, one artwork each), plus a review strip.
2. Creative-director review of the ten-up strip on light paper, on dark editorial, in grayscale, and at thumbnail size. This also pays the standing series-strip debt item.
3. Only after sign-off: Phase B, the 49 pattern drills as seed and knob variants inside these sheets. The drill knobs are the sanctioned variation axes; a new operator requires reopening this brief.

**Criteria:**

- Glance test: still plus category name lets a reader sense the category question without reading it.
- One alphabet: differences across the ten read as hue, operator, and parameters, never as a style change.
- The grayscale strip separates all ten by silhouette.
- One artwork per category reads correctly on both themes.
- Thumbnail survival at roughly 240px card width, and legible at 120px.
- Every still at or under 24446 px2 of ink, with the number reported.
- Contrast floors in 3.8 hold, measured not assumed.
- Every device contained in its plate with 8px clearance, verified per shape.
- No figurative objects, no UI chrome, no text in the art, no violet or indigo ground.

---

## 10. Asset and licence note

The 30 reference PNGs live outside the repo in the local Cursor project assets folder and are analysis input only. Laws of UX (lawsofux.com) publishes its content under a no-derivatives licence: this project studies qualities (grammar, restraint, device thinking) and clones no asset, character, or card. Do not commit the reference PNGs to the repo.
