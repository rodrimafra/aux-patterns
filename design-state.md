# Design state: Agentic UX Patterns

**Final imagery ingested (2026-08-14).** Source of truth is the Figma component library on the "🧱 Components" page (node `47:219`, `pattern-*` sets, `style=color-light`): 10 category covers + 49 pattern stills. Ingested into `ILLUS` + `PAT` in `index.html` and `assets/illustrations/`. No commit unless asked.

## Brief summary

**Active brief:** category hub IA (home as source of truth).

Problem: 49-card wall. Home should teach the ten jobs; a category page lists that category's patterns. Primary persona: designers/PMs scanning for a job, then a pattern. Success: home is 10 category cards; hub is hero + question + full in-page pattern folio + related/next; Contact dialog stays.

Source brief: `docs/designpowers/briefs/2026-08-14-category-hub-pages.md`

Illustration system (still in force): `docs/designpowers/briefs/2026-08-13-agentic-ux-illustration-style.md`

Prior craft uplift: `docs/designpowers/briefs/2026-08-13-agentic-ux-lawsofux-uplift.md`

## Principles

Strategy principles (illustration system), see full definitions in strategy doc:

1. Teach the job, not the vibe.
2. One alphabet, many subjects (hue + analogy domain; patterns = variants later).
3. Meaning survives without colour (inclusive; one artwork serves both themes since brief v2; violet cats 7/10 accent only).
4. Empty space is the teaching surface (one idea; ≥61.8% empty, measured, since brief v2).
5. Generate assemblies, ship static.

Standing project constraints:

6. Independent identity over client brand (no Gemframe / purple-as-brand).
7. No em dashes; no client-named scenes.
8. Phase gate: 10 category directions before 49 pattern drills.

## Decisions log

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-08-18 | Rail ticker matches the category hero field | Owner: `.sec-nav a.on` uses `--illu-field` (`FIELDS`), the same canvas as the hub hero, not `cats[n].hex`. |
| 2026-08-18 | Category hue is chrome; type is greyscale | Owner: rail `.on` keeps `cats[n].hex`. Titles, kickers, featured, Related hover, and Next category use `--ink` / `--ink2` / `--ink3` only. |
| 2026-08-18 | Folio chunks divide by space, not hairlines | Owner: drop list and end-beat rules. Why to use/avoid and use/avoid to Examples use `--s7`. List rows stack on `--s2`. |
| 2026-08-18 | Hub pattern title stays cream at rest | Owner: in-view no longer paints the serif title in category hue. Hover/focus still lift. Kickers and catalog squares keep the hue. |
| 2026-08-18 | Hub patterns are a full folio, not an accordion | Owner: drop More details / Close / peek. Rail and title scroll. Category hue on title, kickers, catalog squares. Serif subheads for Overview / Why / Examples. Related + Further reading close the folio. |
| 2026-08-17 | Hub topbar fades to reading-paper after the hero | Owner: full-bleed bar, `--bg` to match `#gridWrap`. Mark + Back as a start cluster; rail sticks below the bar. |
| 2026-08-17 | Hub article uses masthead then a 38rem reading column | Owner: italic serif lemma under the title; Overview and body share `--s5` section cadence; labels `--t-xs` tight to copy. |
| 2026-08-17 | Collapsed pattern shows Overview plus a faded peek; More details sits below | Owner: teaser peeks the rest of the body; pill label More details / Close. |
| 2026-08-17 | Search removed from category hubs | Owner: search is a home-index tool. Hubs list the aisle in full. |
| 2026-08-17 | Copy link recedes as a caption mark | Owner: 44px hit kept; drop the raised fill, hairline, and blur. 16px stroke in Gallery Stone Deep so the title leads. |
| 2026-08-17 | Copy link is an icon on the pattern title row | Owner: right of the title, 44px icon-only, not a labeled pill under the definition. |
| 2026-08-17 | Download markdown removed from hub accordion | Owner: expanded pattern tools keep Copy link only. |
| 2026-08-17 | Hub accordion has a labeled Read pattern trigger | Teaser looked like a static card (still + heading). Pill + chevron on every `.psec`; whole teaser opens; label becomes Close when open. |
| 2026-08-17 | Hub search stays on; museum wall kept | Critique pass: search on every aisle with token match, result count, all-categories escape. Hub copy on darkened plate for AA. Rail `.on` follows open pattern; chips hidden under 800px. Chrome 44px, labeled share/download, Featured 12px. Home stills unchanged. |
| 2026-08-17 | Alt master-symbol direction scout completed (inspiration only; P1 remains locked) | Moodboard proposes two competing directions vs keyhole seal: **Open Caliper** (open jaws hold) and **Punched Plate** (mass + counterform stamp). Artifact: `docs/designpowers/inspiration/2026-08-17-master-symbol-alt-directions.md`. No redraw; next is human Figma probes A1-A3 / B1-B3. |
| 2026-08-17 | Master-symbol alphabet: circle/round = human, sharp square = agent | Owner: judgement practices for designing AI agents. Chase coin lesson kept as counterform/mass, not octagon clone. HTML probes before Figma: `docs/designpowers/probes/2026-08-17-master-symbol-circle-square.html` (M1 Coin, M2 Caliper, M3 Soft plate). |
| 2026-08-17 | Alphabet rule added: lines = controlling the agent | Logo-generator skill Phase 2: 6 variants (V1–V6) with human/agent/control grammar. Probe: `docs/designpowers/probes/2026-08-17-master-symbol-logo-generator.html`. SVGs: `assets/illustrations/mark/logo-generator/`. |
| 2026-08-17 | Agent shape pivot: triangle (point up) replaces square; reads as letter A | V1 Gate selected as baseline. Square retired for agent role. Three iterates: T1 Gate A, T2 Vertex Rein, T3 Letter Bar. Probe: `docs/designpowers/probes/2026-08-17-master-symbol-v1-triangle.html`. Alphabet now: round = human, triangle = agent, lines = control. |
| 2026-08-17 | T3 Letter Bar locked and sent to Figma for refinement | Component set `aux-master-symbol-t3` (`94:207`) modes dark (`94:193`) / light (`94:200`). Probe board `probe/master-symbol-T3` (`94:208`) with 16/32/64/224 + white/cream/night grounds. Edit component; do not detach. P1 keyhole set remains as prior direction. |
| 2026-08-17 | Category art brand alphabet strategy + probes (provisional) | Round=human, triangle=agent, lines=control (curves OK), square=frame only. φ stills grammar. Logo-generator probe SVGs for cats 3/1/10 A–C. Strategy: `docs/designpowers/strategy/2026-08-17-category-art-brand-alphabet.md`. Board: `docs/designpowers/probes/2026-08-17-category-art-alphabet.html`. SVGs: `assets/illustrations/categories/probes-alphabet/`. Await look-then-pick. |
| 2026-08-17 | **FINAL master mark locked** on `aux-master-symbol` (`89:559`) | Owner refined Letter-A seal in Figma. Round = human, triangle = agent (A), lines = control (crossbar + base). `mode=dark` cream `#F2EEE2` (`85:109`); `mode=light` ink `#0D0D0D` (`89:560`). Union plate 168 on 224 canvas. Repo: `assets/illustrations/mark/aux-master-symbol.svg` (+ plate-168, mode-dark, mode-light). Keyhole P1 superseded (`archive-keyhole-figma-152.svg`). |
| 2026-08-17 | Master mark on home hero + favicon | Inline plate-168 beside home `h1` (`currentColor`: cream dark / ink light). Hidden on category hubs. `favicon.svg` at repo root with `prefers-color-scheme`. |
| 2026-08-17 | Master mark moved to top nav | 40px home control, left of topbar. Cream on dark / ink on light; cream on category hubs. Click returns home. Favicon unchanged. |
| 2026-08-17 | Default color mode is dark | First visit and any non-`light` stored value load dark. Light only after explicit toggle. `color-scheme` meta follows the active theme. |
| 2026-08-17 | Pattern detail is an in-page accordion on the category hub | One expanded at a time. Teaser is still + title + definition. Full sections (Overview through Further reading) sit in `.psec-body`. Hash `#slug` expands; collapse restores `#cat-n`. Search cards and related chips expand in place (other category goes to that hub). Pattern `<dialog>` retired. Contact dialog stays. Supersedes 2026-08-14 keep-dialog lock. |
| 2026-08-17 | Master symbol P1 locked in Figma as component `aux-master-symbol` (`85:109`) | Probe `probe/master-symbol-P1` (`86:109`) uses instances at 16/32/64/224 plus white/cream/night grounds. Edit the component; do not detach. Sketch 152 renamed `aux-master-symbol/figma-152` (`82:109`). Page: 🧱 Components. Superseded by FINAL Letter-A seal on the same component set. |
| 2026-08-17 | Path presentations include visual probes before a pick | Owner: review by looking, then select. Text-only forks are incomplete. Probe page for master-symbol A/B/C: `docs/designpowers/probes/2026-08-17-master-symbol-paths.html` |
| 2026-08-14 | Home = 10 category cards; category page = hub (hero + question + pattern cards + related/next); keep pattern dialog | Owner lock: Figma home is visual source of truth; LoUX detail frame donates structure only |
| 2026-08-14 | Implement in `index.html` now; skip further Figma drafting this pass | Owner chose html_now |
| 2026-08-13 | Craft uplift, not full Laws of UX visual mirror | Keep deliberate identity; port qualities only |
| 2026-08-13 | Category-keyed motifs, not 49 images (craft pass) | Reusable interim system; posters out of that pass |
| 2026-08-13 | Offline algorithmic-art bake (inline SVG) | Seeded generative craft without breaking zero-deps |
| 2026-08-13 | Share = copy `#slug` deep-link; Download = `.md` Blob from DB | Chrome only; no new pattern copy |
| 2026-08-13 | Public repo `rodrimafra/aux-patterns`; first push out of craft pass | Remote exists; commit/push on explicit ask |
| 2026-08-13 | Illustration goal = teach + real-world / job analogy | Success = applicability or job mapping, not vibe |
| 2026-08-13 | Per-pattern teaching images (phased) | Category directions first, then 49 drills |
| 2026-08-13 | Split assets OK | Unblocks 10→49 without single-file bake |
| 2026-08-13 | Style near Laws of UX: flat vector, basic shapes, transparency | User taste signal |
| 2026-08-13 | Recolor for dark + light themes | Not light-only LoUX cards |
| 2026-08-13 | Generative/algorithmic under that style | Production path |
| 2026-08-13 | Approach B: one grammar; hue + subject vary | Library coherence over per-category kits |
| 2026-08-13 | `aup-mesh-v1` no longer teaching system | Interim chrome only until category directions land |
| 2026-08-13 | Lock grammar: IBM Flat primitives + 8px grid + angles 0/45/90; Aicher figure modules; subject = pose + prop; ≥40% empty; one idea per still; Albers opacity for tokens only | Scout handoff; generative-friendly series identity |
| 2026-08-13 | Lock 10 category analogy domains (job/world + pose/prop) from scout seeds | Approach B subject domains; LOCKED RECOMMENDATION in strategy §5 |
| 2026-08-13 | Lock `--illu-*` token map (canvas, fg, muted, accent, overlap) with contrast floors 4.5:1 / 3:1; no whole-SVG invert; cats 7/10 violet accent only | Dual theme + a11y; independent identity |
| 2026-08-13 | Camera: flat elevation family; one viewpoint per category; max one figure + one setting + 1–2 props | IKEA language-light teaching without comic strips |
| 2026-08-13 | Wrong-way sibling allowed only for cat 9 (Failure & Repair) | Scoped a11y labeling; shape + UI label, not colour-alone |
| 2026-08-13 | Phase A viewBox locked at **320×200** (8px grid) for all category SVGs | Shared camera frame; thumbnail room; ≥40% empty feasible |
| 2026-08-13 | Asset path `assets/illustrations/categories/cat-{1..10}.svg` (+ optional `cat-9-wrong.svg`, `_template.svg`) | Plan F9 |
| 2026-08-13 | `--illu-*` defined under `[data-theme="light|dark"]` in `index.html`; `--illu-accent: var(--accent)` so category surfaces that already set `--accent` to `cats[n].hex` auto-hook | Task 1 without breaking chrome |
| 2026-08-13 | SVG fills use `var(--illu-*, light-fallback)`; theme swap requires **inline** SVG (or equivalent), not `<img>` alone | CSS variables do not cascade into `<img>` documents |
| 2026-08-13 | Cats 7/10: violet/indigo on accent prop only; overlap panels use muted gray mix, never violet canvas | Independence + a11y |
| 2026-08-13 | Ship optional `cat-9-wrong.svg` (ban ring + diagonal bar on muted spare part) | Clean wrong-way sibling; UI must label "wrong way", not colour-alone |
| 2026-08-13 | Task 5 card/hero wiring deferred to design-builder | Avoid risky mesh/dialog regressions; tokens + assets ready |
| 2026-08-13 | Task 5: teaching slots use inline `ILLUS` map (`cat-1`…`cat-10` markup in `index.html`) | `file://` cannot fetch assets reliably; CSS `var(--illu-*)` only resolves on inline SVG |
| 2026-08-13 | Accessible name = bilingual `db().cats[n].name` via `role="img"` + `aria-label` on `.motif` wrapper; SVG `aria-hidden` | Avoid duplicate titles across cards; language switch rebuilds labels |
| 2026-08-13 | `--illu-accent` continues via `--accent` set on card/sheet from `cats[n].hex` | No separate accent hook required |
| 2026-08-13 | Landing `aup-mesh-v1` retained as non-teaching chrome only (`#landingMotif`) | Mesh retired from card + detail teaching heroes |
| 2026-08-13 | `cat-9-wrong.svg` left unused in UI | Wrong-way sibling requires visible UI label if shown; Phase A does not surface it |
| 2026-08-13 | Heuristic eval (Phase A): proceed with fix round, not rethink | Same-art-per-category is intentional Phase A; flag scan friction + missing category-art cue + no series strip as Major/Minor. Job analogies and grammar coherence pass. Mesh-out-of-teaching heroes passes H4/H8. |
| 2026-08-13 | **design-critic Phase A:** verdict **revise** (not proceed / not rethink) | Grammar + analogies hold (P1–P5). Blockers: featured badge on teaching band; light accent-on-canvas < preferred ≥3:1 (aligns A11Y-01); Task 6 checklist incomplete. No Phase B until fix round + Task 6. |
| 2026-08-13 | A11y review Phase A (Task 5): **fail light accent + featured text**; dark fg/muted/rule pass floors; cats 7/10 accent-only OK; `cat-9-wrong` unused OK; bilingual motif labels OK | Measured contrast; Design Debt A11Y-01..07 |
| 2026-08-13 | Light `--illu-accent`: `color-mix(in srgb, var(--accent) 58%, #17181c)`; dark keeps raw `--accent` | All 10 cats ≥3:1 vs `#f7f4ee` (cat 6 ~3.43:1); geometry unchanged |
| 2026-08-13 | Featured `.feat` moved into `.card .body` (not motif band); light `color: var(--ink)`, dark `color: var(--bg)` | Stops occlusion on cats 3/5/6; fixes light pill text contrast |
| 2026-08-13 | **a11y re-review (criticals only):** **Pass**. C1 light mix all 10 ≥3:1 (worst cat 6 ~3.43:1); C2 feat in `.body`, light ink ≥5.95:1 / dark bg ≥6.43:1; A11Y-03 `u.detail` EN/PT on `renderChrome` + `openP`. No new blockers | Measured sRGB mix + markup audit |
| 2026-08-13 | All filter: full motif on first card per category only; siblings `.card-compact` (no motif); `catq` bilingual category-art cue | Softens same-art wall without new illustration styles; category filter keeps full motif |
| 2026-08-13 | Dialog `aria-label` from UI `detail` (EN/PT); `contain-intrinsic-size` 300px | A11Y M1 + scroll-jump minor |
| 2026-08-13 | Task 6 verification artifact written | `docs/designpowers/verification/2026-08-13-illustration-phase-a.md` |
| 2026-08-13 | **design-critic re-review (fix round only):** verdict **proceed** | C1 featured off band, C2 light accent ≥3:1 (cat 6 ~3.43), C3 Task 6 doc all confirmed in `index.html` + verification md. All-view first-card motif + `catArt` cue holds. No craft blockers. Phase B unblocked at critic gate (deferred strip/grayscale remain debt, not blockers). |
| 2026-08-13 | LoUX 30-card grammar extracted; 10 category composition sheets locked in `docs/designpowers/briefs/2026-08-13-category-illustration-from-loux.md`; colour deployment two-mode (hue-as-field cats 1-6/8/9, neutral field + violet/indigo single mark cats 7/10). Generation on hold pending creative-director review | Owner-shared LoUX reference cards analyzed; deepens algorithmic-art handoff, supersedes its seeds table |
| 2026-08-13 | **Brief v2 approved (3 decisions).** (1) φ armature: frame 320×200 (8:5, 1.11% off φ), golden sections snapped to grid → anchors A(120,80) B(200,80) C(120,120) D(200,120); anchor per category assigned by `frac(n/φ)` low-discrepancy, landing A=3 B=2 C=3 D=2. (2) Three scales: size = Fibonacci×8 (8,16,24,40,64,104,168), stroke 1/2/3/5, opacity = φ^-n (1, .62, .38, .24, .15, .09). (3) One colour recipe: mode A field = hue at 38.2% over ink `#14161b`, mute = field at 38.2% over ink; mode B (cats 7/10) field = `#242730`, mute = cream at 23.6% into field, hue on one element. Ink budget ≤ 24446 px² of 64000 (61.8% empty, measured) | Numbers derived and measured, not eyeballed: marks 5.68:1 to 12.86:1 vs field, mutes 1.60:1 to 2.04:1, mode B accents 5.48:1 violet / 5.00:1 indigo. φ used as constraint generator (additive scale, exact complementarity, low-discrepancy), never as a beauty claim |
| 2026-08-13 | **Six operators replace twelve device families:** containment (1,10), sequence (2,5,9), vector (3), reduction (4), decay (6,8), relay (7). New operator requires reopening brief v2 | Fewer machines, better tuned; ten categories separate by hue, anchor, parameters, silhouette |
| 2026-08-13 | **One artwork per category, not light/dark twins.** Colours baked literal hex; no `--illu-*` variables inside the art; no `cat-9-wrong` graphic | Still carries its own field, reads on both themes. 20 assets → 10, removes the twin-drift bug class. Unbuilt beats unused |
| 2026-08-13 | **Cat 9 recipe fixed at generation:** run without interior joints, single 64px break, 24px mend with 20px shoulders | First build's 8px shoulders equalled the run's own joints, so the break stopped reading; only hue said "mend". Shoulders must exceed every other gap in the run |
| 2026-08-13 | **The plate (brief v2.1, owner direction):** every device contained in a drawn 168×168 square, stroke 2, mute on mode A / cream on mode B; origins (56,16) for anchors A/C, (96,16) for B/D so the focal anchor lands on the plate's internal Fibonacci crossings (64/104, exact on grid); 8px device clearance verified per shape; cat 10's plate doubles as its policy boundary. Baseline: cat10 stroke-2 outlined-lattice variant | Owner: "all generations contained in a perfect square", cat10-meio as baseline. 64+104=168 makes the square's golden sections land on the 8px grid with zero snap error; wall gains one repeated module with an alternating left/right rhythm |
| 2026-08-13 | **Verification honesty pass on the generator:** mute floor asserted at 1.5 raw (cat 3 measures 1.5998; no two-decimal rounding), derived-edge check added (4px half-step) and proven by falsification, ImageMagick dropped for review renders (it silently omits stroke-only shapes), Chrome headless is the reference renderer | A check that cannot fail is not a check; review decisions were briefly made on a renderer that hid every outline |
| 2026-08-14 | **Phase B: 49 pattern stills.** Knob variants of the Figma 224 squares (`assets/illustrations/patterns/{n}.svg`, inlined as `PAT`). Card thumbs and detail heroes use `p.n`. Chip hero still uses parent `ILLUS`. Baker: `tools/illustrations/bake_patterns.py`. Review: `docs/designpowers/probes/2026-08-14-pattern-stills-strip.html`. `generate.py` still probe-only. | Owner chose agent-drawn SVG variants, all 49, wired in prototype |
| 2026-08-14 | **Figma refinements ingested** for pattern stills 1.x–8.x and 10.x from Phase B page `37:2`. Category 9 parent and 9.1–9.4 held: gap/mend mark does not work; new alphabet pending. | Owner refined stills in Figma except cat 9 |
| 2026-08-14 | **Cat 9 rebuilt on "missing course"** alphabet (stack of bars, empty course, remedy variations); **Cat 10 rebuilt** after re-interview against the moodboard (ghost grid, cream at 100/55/30, winners P-B, 1-C, 2-A, 3-B, 4-B pushed to Phase B page). | Owner picked alphabets in canvas reviews |
| 2026-08-14 | **Final approved imagery ingested** from the Figma component library (`47:219`, `pattern-one`..`pattern-ten`, 59 `style=color-light` variants). All 10 covers (`ILLUS`, `assets/illustrations/categories/`) and all 49 stills (`PAT`, `assets/illustrations/patterns/`) replaced; clip/mask IDs sanitized. Owner refined every still by hand in Figma; the components are canonical over the Phase B working page. | Owner declared `47:219` final |
| 2026-08-13 | **Figma frame `categories` (28:353) is source of truth for the ten stills.** Square 224 (the card *is* the square). Structure: black at ~20% opacity, stroke 4. On-state: cream `#F2EEE2` with opacity steps. Empty cells are outline, not faded fills. Shared 4x4 module: padding 12, gap 10, cell 42.5. Owner overrode Mode B: cats 7 and 10 use hue fields (`#A6307F`, `#297AA3`), not a neutral ground. Poster fields are a separate saturated LoUX-like palette; they do not replace `data/en.json` `cats[n].hex` UI accents. Files: `assets/illustrations/categories/cat-{1..10}.svg`, inlined as `ILLUS` in `index.html`. `tools/illustrations/generate.py` is probe-only and refuses overwrite without `--force`. | Owner drew the finals. Generator recipes stay as history. Do not regenerate. |

## Motif seeds (algorithmic-art family), interim

Family: `aup-mesh-v1`, layered arcs + dots on dark field, accent from category hex. **Interim chrome only.** Task 5 retired mesh from card/detail teaching heroes; landing `#landingMotif` still uses mesh.

Seed formula: `seed = hash32("aup-mesh-v1|" + categoryId + "|" + hex)`  
Landing: `seed = hash32("aup-mesh-v1|landing|#7d7b75")`

| Key | Hex | Seed (uint32) |
|-----|-----|---------------|
| landing | #7d7b75 | 735787257 |
| 1 | #f59e0b | 566578788 |
| 2 | #34d399 | 2627929235 |
| 3 | #f87171 | 481185840 |
| 4 | #f472b6 | 3179054019 |
| 5 | #38bdf8 | 332830822 |
| 6 | #a3e635 | 1349316555 |
| 7 | #a78bfa | 492053502 |
| 8 | #22d3ee | 2900757611 |
| 9 | #fb923c | 848816946 |
| 10 | #818cf8 | 2847066021 |

Do not treat mesh family as final teaching art.




## Correction (2026-08-13)

User feedback: Phase A literal workplace stills are **wrong abstraction**. Target = Laws of UX–level abstract poster geometry, not figurative job scenes.
Desired deliverable was an **illustration brief for `/algorithmic-art`**, not the SVG scene system.
Handoff brief: `docs/designpowers/briefs/2026-08-13-illustration-algorithmic-art-handoff.md`
Literal `cat-*.svg` / ILLUS wiring = provisional wrong turn; do not treat as craft north star.
Literal category SVGs stripped from `index.html` (2026-08-13). Cards/heroes back on interim `aup-mesh-v1` MOTIFS. Assets under `assets/illustrations/` removed. Await `/algorithmic-art` from handoff brief.


## Phase A exit (2026-08-13)

Gate **CLEAR**. Critic proceed ([7d073ca2](7d073ca2-a898-469e-ba09-eed080cdb637)). A11y critical re-check PASS ([3d7b3ebe](3d7b3ebe-4a25-4ec8-8378-107a81a0e710)). Fix round ([624abc19](624abc19-c8d6-48cd-9c0c-e28cbf10cf84)).
Verification: `docs/designpowers/verification/2026-08-13-illustration-phase-a.md`.
Phase B (49 pattern drills) **not started** (await creative director). Debt: series strip screenshot, formal grayscale, A11Y-04..07.

## Reconciliation (2026-08-13 fix round)

Aligned: light accent contrast (a11y C1 + critic); featured pill off motif + light text (a11y C2 + critic + heuristic occlusion).
Complementary: All-view first-card motif + category cue (heuristic); dialog bilingual label (a11y M1); Task 6 verification (critic); contain-intrinsic-size (heuristic minor).
Rules applied: accessibility over aesthetics; brief Phase A same-art intentional (softened, not abandoned).
Fix agent: design-builder 624abc19. Re-review: a11y 3d7b3ebe + critic 7d073ca2 (criticals only).

## Open questions

- Full `design-taste` calibration still pending (flag F7 light canvas warmth; current light `--illu-canvas: #f7f4ee`).
- User may reverse locked analogy domains or angle set (flags F1–F2 in strategy).
- Generator bake script is probe-only. Shipped stills are Figma 224 squares. Do not run `generate.py` against `assets/illustrations/categories/` without `--force`.
- Whether to drop landing mesh entirely once category art feels enough atmosphere on the index.
- Content duplication: `ILLUS` inlines duplicate disk SVGs under `assets/illustrations/categories/` (same class of problem as DB/markdown). Acceptable for Phase A offline.
- Heuristic (open): Is a dedicated 10-up category sample strip needed for the Compare journey stage, or is consecutive first-card art enough?
- Resolved: All-view category-art cue + first-card-only full motif.
- Resolved: light `--illu-accent` 58% mix; featured pill in body; Task 6 verification doc.

Resolved this pass: analogy domains; `--illu-*` twins; viewBox 320×200 (probe, superseded); ten Figma 224 stills as canonical; Task 5 teaching-slot wire; mesh kept only as landing chrome; F8/F9 path lock.

## Artifact index

- Algorithmic philosophy: `docs/designpowers/algorithmic-art/editorial-geometry-philosophy.md`
- Probes (review): `docs/designpowers/probes/2026-08-13-editorial-geometry-probes.html`
- Algorithmic-art handoff brief: `docs/designpowers/briefs/2026-08-13-illustration-algorithmic-art-handoff.md`
- Category illustration brief **v2** (LoUX grammar + φ armature + scales + one colour recipe + 6 operators + category sheets): `docs/designpowers/briefs/2026-08-13-category-illustration-from-loux.md`
- Ten-strip generator (deterministic, stdlib only): `tools/illustrations/generate.py`
- Ten-strip review page (light / dark / grayscale / thumbnail): `docs/designpowers/probes/2026-08-13-editorial-geometry-ten-strip.html`
- Illustration brief (discovery): `docs/designpowers/briefs/2026-08-13-agentic-ux-illustration-style.md`
- Design plan (Phase A): `docs/designpowers/plans/2026-08-13-illustration-phase-a-plan.md`
- Inspiration moodboard: `docs/designpowers/inspiration/2026-08-13-illustration-moodboard.md`
- Illustration strategy: `docs/designpowers/strategy/2026-08-13-illustration-strategy.md`
- Category hub brief: `docs/designpowers/briefs/2026-08-14-category-hub-pages.md`
- Craft uplift brief: `docs/designpowers/briefs/2026-08-13-agentic-ux-lawsofux-uplift.md`
- Prototype: `index.html` (now includes `--illu-*` under theme selectors)
- Category stills, owner finals (viewBox 224×224, one artwork per category, baked hex from Figma 28:353):
  - `assets/illustrations/categories/cat-1.svg` … `cat-10.svg`
  - Inlined in `index.html` as `const ILLUS`
  - Probe generator `tools/illustrations/generate.py` must not overwrite these (guarded; `--force` only)
  - Historical: Phase A literal `_template.svg` / `cat-9-wrong.svg` and the 320×200 plate system are not the shipped art
- Content mirrors: `data/en.json`, `data/pt-br.json`, `data/ui-strings.json`, `patterns/**`
- Agent guidance: `CLAUDE.md`, `HANDOFF.md`
- Phase A verification: `docs/designpowers/verification/2026-08-13-illustration-phase-a.md`
- GitHub: https://github.com/rodrimafra/aux-patterns
- **Resume checkpoint (2026-08-13 stop, superseded 2026-08-14 Phase B):** `docs/designpowers/handoff/2026-08-13-illustration-checkpoint.md`
- Pattern detail folio (2026-08-18): full in-page `.psec` on category hubs in `index.html`; Contact remains `#contactDlg`
- **FINAL master mark (2026-08-17):** Figma `aux-master-symbol` [`89:559`](https://www.figma.com/design/g81CTKZNVjYAqhjdVEPji4/Untitled?node-id=89-559); repo `assets/illustrations/mark/aux-master-symbol.svg`, `aux-master-symbol-plate-168.svg` (`currentColor`), `aux-master-symbol-mode-dark.svg`, `aux-master-symbol-mode-light.svg`
- Category art alphabet strategy + probes (2026-08-17): `docs/designpowers/strategy/2026-08-17-category-art-brand-alphabet.md`, probe `docs/designpowers/probes/2026-08-17-category-art-alphabet.html`, SVGs `assets/illustrations/categories/probes-alphabet/`
- Master symbol T3 Letter Bar in Figma (2026-08-17): component set `aux-master-symbol-t3` `94:207`; probe `probe/master-symbol-T3` `94:208` (exploration; final lives on `89:559`)
- Master symbol V1 triangle iterates T1–T3 (2026-08-17): `docs/designpowers/probes/2026-08-17-master-symbol-v1-triangle.html` + `assets/illustrations/mark/logo-generator/t{1,2,3}-*.svg`
- Master symbol logo-generator V1–V6 (2026-08-17): `docs/designpowers/probes/2026-08-17-master-symbol-logo-generator.html` + `assets/illustrations/mark/logo-generator/`
- Master symbol circle/square probes (2026-08-17): `docs/designpowers/probes/2026-08-17-master-symbol-circle-square.html`
- Master symbol alt directions moodboard (2026-08-17): `docs/designpowers/inspiration/2026-08-17-master-symbol-alt-directions.md` (Open Caliper + Punched Plate; compete with locked keyhole seal)
- Master symbol path probes (2026-08-17): `docs/designpowers/probes/2026-08-17-master-symbol-paths.html`
- Master symbol B2 phi refine: `docs/designpowers/probes/2026-08-17-master-symbol-b2-phi.html`
- Superseded keyhole: `assets/illustrations/mark/archive-keyhole-figma-152.svg` (and `aux-master-symbol-figma-152.svg`)
- Phase B plan: `docs/designpowers/plans/2026-08-14-illustration-phase-b-plan.md`
- Pattern stills: `assets/illustrations/patterns/{n}.svg` (49), review `docs/designpowers/probes/2026-08-14-pattern-stills-strip.html`

### Category composition notes (Phase A, superseded)

Historical record of the literal workplace stills (the wrong turn, see Correction above). Current compositions live in brief v2, section 5.

| Cat | File | Composition (one line) |
| --- | --- | --- |
| 1 | cat-1.svg | Standing figure extends lanyard/badge to a receiving palm at a reception desk |
| 2 | cat-2.svg | Seated figure at sparse desk with accent map sheet; empty chair waiting |
| 3 | cat-3.svg | Figure at mixer booth, hand on accent vertical fader; quarter-arc dial |
| 4 | cat-4.svg | Two figures face a shared board; muted question resolves to accent check |
| 5 | cat-5.svg | Figure at kitchen pass window; ordered steps, last step accent |
| 6 | cat-6.svg | Hand on fill vessel; accent fill level; muted shelf |
| 7 | cat-7.svg | Two figures mid-relay; violet baton only; muted platform panels |
| 8 | cat-8.svg | Figure at file cabinet; one accent record pulled forward |
| 9 | cat-9.svg | Workshop bench; accent spare-part gear in hand reach |
| 9w | cat-9-wrong.svg | Same workshop; spare muted; accent ban ring + diagonal bar |
| 10 | cat-10.svg | Figure at gate/threshold with indigo clipboard only; muted triangle marker |

## Pipeline mode

Stopped overnight (owner, 2026-08-13). Was: auto.

## Handoff chain

- discovery → inspiration-scout ([board](docs/designpowers/inspiration/2026-08-13-illustration-moodboard.md), model cursor-grok-4.6-high-fast)
- inspiration-scout → design-strategist ([strategy](docs/designpowers/strategy/2026-08-13-illustration-strategy.md), auto)
- design-strategist → writing-design-plans ([plan](docs/designpowers/plans/2026-08-13-illustration-phase-a-plan.md), auto)
- writing-design-plans → design-lead (Phase A Tasks 1–4): tokens + ten category stills + optional wrong-way
- design-lead → design-builder (Task 5): teaching slots wired
- **design-builder → design-critic / accessibility-reviewer / heuristic-evaluator (parallel next):** Phase A Task 5 implemented in `index.html`. Cards + detail heroes show category teaching SVGs (inline `ILLUS`); landing mesh remains non-teaching chrome. Review against plan Task 5 + principles 1–5. Do not start Phase B (49 patterns).
- **heuristic-evaluator → design-builder / design-lead (reconciliation):** Verdict **Proceed** (fix round, not rethink). No Critical. Worst usability risk: identical category art on every pattern card (cats with 6–7 patterns) harms index triage (H6/H8) and can read as a bug without a category-art cue (H1). Job analogies + one-alphabet grammar pass. Taller teaching band improves metaphor readability vs old mesh. Fix: light category cue and/or soften All-view repetition; optional 10-up strip for Compare; bump `contain-intrinsic-size`; watch featured pill occlusion.
- **accessibility-reviewer → design-builder (fix round):** Verdict **Fail gate** until A11Y-01/02/03 fixed. Dark base tokens pass. Light accents + featured text fail AA. Cats 7/10 violet accent-only OK; static + reduced-motion OK; bilingual motif names OK; `cat-9-wrong` unused OK.

**accessibility-reviewer → design-builder:** Two light-theme blockers. Darken `--illu-accent` in light (reuse accent+ink mix; raw hex fails all ten, worst cat 6). Featured pill: `color: var(--ink)` in light, keep `var(--bg)` in dark. Wire dialog `aria-label` from UI strings for PT-BR. Then re-check contrast only.

- **design-critic → design-builder (fix round):** Verdict **revise**. Move featured badge off the teaching band (not just recolor text); apply light `--illu-accent` recipe (A11Y-01); complete Task 6 checklist + verification note. Grammar/analogies stay locked. No Phase B until Task 6 passes.
- **design-critic → design-lead (if needed):** Confirm light accent composition rule (token mix vs restage props on muted). Heuristic category-art cue can ship in same fix round without reopening Approach B.

- **design-builder → accessibility-reviewer + design-critic (re-review, criticals only):** Fix round shipped. (1) Light `--illu-accent` 58% accent+#17181c mix; dark raw accents unchanged. (2) Featured pill in `.body`, light ink / dark bg. (3) Dialog `aria-label` from `u.detail`. (4) All-view same-art soften: first card full motif, siblings compact; `catq` category-art cue. (5) Task 6 doc at `docs/designpowers/verification/2026-08-13-illustration-phase-a.md`. Re-check **C1/C2/featured move + A11Y-01/02/03 only**. No Phase B.

- **design-critic → design-builder / design-lead (re-review fix round):** Verdict **proceed**. C1/C2/C3 cleared in code + Task 6 artifact. All-view first-card motif softening accepted. Phase B unblocked at critic gate; deferred 10-up strip / grayscale stay as debt.

**design-critic → design-builder:** Verdict: proceed. Featured is off the teaching band, light accents clear ≥3:1, Task 6 verification doc is enough for the gate. Phase B can start when you are ready; keep strip/grayscale as debt, not blockers.

**accessibility-reviewer → design-builder / design-lead (re-review, criticals only):** Verdict **PASS**. C1 light `--illu-accent` 58% mix: all 10 cats ≥3:1 vs `#f7f4ee` (worst cat 6 ~3.43:1). C2 `.feat` in `.body`, light `var(--ink)` ≥5.95:1 / dark `var(--bg)` ≥6.43:1. A11Y-03 `u.detail` EN/PT on `renderChrome` + `openP`. No new regressions. Minors A11Y-04..07 remain debt.





## Design debt register (accessibility)

| ID | Severity | Item | Who | Fix when |
|----|----------|------|-----|----------|
| A11Y-01 | Critical | Light `--illu-accent` (raw `cats[n].hex`) fails ≥3:1 vs `--illu-canvas` (#f7f4ee) for all 10 cats; cat 6 `#a3e635` ≈1.37:1. Recipe: light `--illu-accent: color-mix(in srgb, var(--accent) 58%, #17181c)` (or darker until ≥3:1; cat 6 needs ≤~63% accent) | design-builder (+ design-lead if token recipe) | Cleared (re-review; all 10 ≥3:1) |
| A11Y-02 | Critical | Featured `.feat` uses `color: var(--bg)` on accent; light fails 4.5:1 all cats (≈1.4–2.8:1). Fix: light `color: var(--ink)` (passes ≥5.9:1); keep dark `color: var(--bg)` | design-builder | Cleared (body + light ink; re-review) |
| A11Y-03 | Major | `<dialog aria-label="Pattern detail">` not bilingual with UI lang | design-builder | Cleared (`u.detail` EN/PT) |
| A11Y-04 | Minor | Card/hero motif `aria-label` = category name duplicates nearby title/cat copy (COGA verbosity) | design-builder | Polish / debt |
| A11Y-05 | Minor | Disk SVGs EN-only `<title>`; OK while inline+`aria-hidden`; breaks if `<img>` path | Phase B | When `<img>` used |
| A11Y-06 | Minor | Chips `role="tab"` without `aria-selected` / tabpanels (pre-existing) | design-builder | Later chrome |
| A11Y-07 | Minor | Hero actions Share → Download → Close; close-first stronger | design-builder | Polish |

## Design debt register (critic)

| ID | Severity | Finding | Status |
| --- | --- | --- | --- |
| C1 | major | Featured `.feat` pill overlays teaching band; hurts featured cats 3/5/6 teaching props | cleared (in `.body`) |
| C2 | major | Light `--illu-accent` vs canvas below preferred ≥3:1 (same as A11Y-01) | cleared (58% mix; re-measured) |
| C3 | major | Task 6 acceptance checklist incomplete; no verification doc | cleared (verification md) |
| C4 | minor | Cat 4 question-mark may read as pin/dot at thumbnail | deferred |
| C5 | note | Cat 8 densest still; watch series strip | deferred |
| C6 | note | `ILLUS` / disk SVG duplication | accepted Phase A |

## Design debt register (heuristic deferred Minors)

- Featured pill moved to `.body` (occlusion resolved).
- `contain-intrinsic-size` bumped to 420px (square 224 motif + body).
- No dedicated category sample strip for Compare journey; consecutive cards only.
- Cat 5 pass / cat 6 vessel metaphors slightly soft at ~240px without title.

**Pay attention (reviewers):**
1. Theme toggle must recolor teaching art live (inline SVG + `--illu-*`); cards already set `--accent` → `--illu-accent`.
2. Accessible name = category name (EN/PT via `db().cats`); SVG itself is `aria-hidden`.
3. Featured pill lives in `.card .body` (not on the teaching band); light ink / dark bg on accent fill.
4. `cat-9-wrong.svg` is on disk but not shown; if critic wants a wrong-way sample, require a visible UI label.
5. Contrast / grayscale / series coherence still belong to Task 6 acceptance; builder did not run full strip screenshots.
6. Keyboard/dialog/filter/View Transitions/`file://` should be unchanged; flag regressions.
7. **A11y fix round:** C1/C2/A11Y-01/02/03 **PASS** re-review 2026-08-13; no remaining blockers in scope.
8. **Critic:** Fix-round re-review **proceed**; C1/C2/C3 cleared; Phase B unblocked at critic gate.

**Screenshot checkpoint (orchestrator):** Open `index.html` (`file://` OK). Look at: (1) index cards under any category, calm SVG ~240px max width on `--illu-canvas`; (2) open a pattern, detail hero illustration; (3) toggle theme, confirm fills flip dark/light without reload; (4) switch EN/PT, confirm category chip names and that re-open still works; (5) landing header still shows mesh chrome, not category stills.


**Screenshot checkpoint (after critic fix):** (1) featured cards with badge not covering accent prop; (2) light theme accent readability ≥3:1; (3) series strip of all 10; (4) theme toggle; (5) Task 6 checklist filled.
- Phase A exit clear → await user for Phase B or team presentation close
