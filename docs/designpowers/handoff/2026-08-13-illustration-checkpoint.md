# Checkpoint: category stills in the prototype

**Updated:** 2026-08-14. Phase B (49 pattern stills) is in the prototype. Do not commit unless asked.
**Read this file first**, then `HANDOFF.md` and `CLAUDE.md`.

Prior thread: [Category stills in prototype](4391cca6-24e6-49ea-903b-43c64b0cd3bf)

---

## What is true now

The ten category drawings are **owner finals in Figma**, not generator output.

- File: https://www.figma.com/design/g81CTKZNVjYAqhjdVEPji4/Untitled?node-id=28-353
- Frame: `categories` (`28:353`), ten 224x224 squares
- Disk: `assets/illustrations/categories/cat-1.svg` … `cat-10.svg`
- Live: inlined in `index.html` as `const ILLUS`
- Review strip (art only, 224 squares): `docs/designpowers/probes/2026-08-13-editorial-geometry-ten-strip.html`

**Phase B (2026-08-14):** 49 pattern stills as knob variants of those squares. Owner Figma refinements ingested for cats 1–8 and 10 (page `37:2`). Category 9 parent and 9.1–9.4 held pending a new mark.

**Final (2026-08-14, later):** Owner declared the Figma component library canonical (page `47:219`, `pattern-one`..`pattern-ten`, `style=color-light`, 59 variants = 10 covers + 49 stills). Cat 9 uses the "missing course" alphabet; Cat 10 uses the ghost-grid + cream-opacity alphabet. All ingested into `ILLUS` + `PAT` in `index.html` and `assets/illustrations/`.

- Disk: `assets/illustrations/patterns/{n}.svg`
- Live: `const PAT` in `index.html`
- Baker: `tools/illustrations/bake_patterns.py` (does not touch category files)
- Plan: `docs/designpowers/plans/2026-08-14-illustration-phase-b-plan.md`
- Review: `docs/designpowers/probes/2026-08-14-pattern-stills-strip.html`

**Do not run** `tools/illustrations/generate.py` against category files. It emits the superseded 320x200 probe and will refuse without `--force`.

### How the prototype uses the art

Open `index.html` in a browser (`file://` is fine).

Landing (`filter === "all"`): `aup-mesh-v1` behind the site title. Not category art.

Category chip selected: `header.hero-h.cat-on`, parent category still (`ILLUS`). Title and sub become category name and question.

Pattern cards: text plus 48px greyscale `.thumb` of that pattern (`PAT[p.n]`).

Grid section labels: text `.catq`. No art banners in the grid.

Pattern detail sheet: colour 16:9 / 4:3 hero of that pattern.

Poster field hexes (`FIELDS` in `index.html`) are not `data/en.json` `cats[n].hex`. UI accents stay the JSON hexes.

Owner overrode Mode B: cats 7 and 10 use hue fields, not a neutral ground.

---

## Known leftover

**Cat 3** parent export still has a clipped cream diamond. Pattern `3.x` files omit it. Re-export the parent only if the owner deletes that mark in Figma.

---

## What not to do unless asked

- Commit or push
- Overwrite Figma category SVGs from `generate.py`
- Put large colour art back on pattern cards
- Put category art banners back into the grid
- Client names, client examples, Gemframe purple-as-brand
- The em dash character (U+2014) anywhere

---

## Sensible next moves (owner chooses)

1. Review the 49-up strip and live thumbs (All, one chip, one detail, light + dark). Featured: 3.2, 5.1, 6.3.
2. Optional: clean cat 3 parent in Figma, re-export.
3. Optional: first git commit.
4. Posters or JSON single-source refactor (`HANDOFF.md` §5 / §7).
