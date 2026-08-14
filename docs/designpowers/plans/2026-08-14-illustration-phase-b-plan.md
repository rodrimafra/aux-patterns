# Design Plan: Agentic UX Patterns illustration system (Phase B)

**Goal:** 49 pattern stills as knob variants of the ten Figma category squares. Unique greyscale thumbs on cards. Colour heroes on pattern detail. Category chip hero stays the parent still.

**Parent art:** Figma `categories` 28:353, `assets/illustrations/categories/cat-{1..10}.svg`

**Not this pass:** `tools/illustrations/generate.py`, 320x200 plate recipes, posters, JSON single-source refactor, commit.

---

## Locked

- Frame 224x224. Field from `FIELDS` in `index.html`. Cream `#F2EEE2`. Empty cells: black stroke 4 at 0.2.
- One operator per category. Knobs remap onto the drawn Figma motifs.
- Unique clip ids (`clip-pat-n-n`).
- No em dash. No client names. Do not overwrite `cat-{1..10}.svg`.
- Cat 3 diamond omitted in every `3.x` file.

## Wiring

- Chip hero: `ILLUS[c]`
- Card thumb: `PAT[p.n]` greyscale 48px
- Detail hero: `PAT[p.n]` colour 16:9 / 4:3 plate

## Paths

- `assets/illustrations/patterns/{n}.svg`
- `const PAT` in `index.html`
- Review: `docs/designpowers/probes/2026-08-14-pattern-stills-strip.html`

## Knob sheet

See implementation in `tools/illustrations/bake_patterns.py`. Summary:

**1 Containment** (frames + cream circle): 1.1 one firm frame, circle inside. 1.2 two frames, thinner loose edge, circle nearer edge.

**2 Sequence** (4x4 fill ramp): 2.1 2x2 island. 2.2 one row path + next lit. 2.3 midpoint shifted. 2.4 one cell 1.0, neighbours 0.5. 2.5 three discrete slots. 2.6 second-brightest return.

**3 Vector** (nested squares + bar + cream square, no diamond): 3.1 bar short. 3.2 perpendicular gate. 3.3 dashed then solid. 3.4 bar offset y. 3.5 extra nested outline. 3.6 reversed echo. 3.7 square on bar end.

**4 Reduction** (vertical bars): 4.1 four even. 4.2 middle shorter. 4.3 rightmost plus confirmation stroke.

**5 Sequence** (4x4 outlines, timeline row): 5.1 larger lit + ring. 5.2 two ghost trail. 5.3 extra filled off-row. 5.4 two fill rows. 5.5 lit later. 5.6 earlier cell dropped a row.

**6 Decay** (column opacities): 6.1 tick under solid. 6.2 more outline. 6.3 one mid cell dropped. 6.4 two equal cream options. 6.5 one cream cell. 6.6 faint opposing cell.

**7 Relay** (scattered cream cells): 7.1 extra branch cell. 7.2 two clusters. 7.3 topmost 1.0 others 0.5. 7.4 two adjacent. 7.5 one cream row. 7.6 rising diagonal.

**8 Decay** (bars + pulled square): 8.1 ring. 8.2 square close. 8.3 one bar missing. 8.4 second column. 8.5 larger detached square.

**9 Sequence** (gap + mend): 9.1 gap no mend. 9.2 mend in gap. 9.3 looser gap. 9.4 mend plus dot.

**10 Containment** (4x4 one cream cell): 10.1 different cell. 10.2 stepped opacities. 10.3 row tiers. 10.4 ghost outline inside 224.

## Verification

- 49 files, 49 `PAT` keys, match `data/en.json`
- Thumbs differ inside a category
- Chip hero still parent
- Detail hero is the pattern
- No `--illu-*` inside SVG
- `generate.py` still refuses category overwrite
