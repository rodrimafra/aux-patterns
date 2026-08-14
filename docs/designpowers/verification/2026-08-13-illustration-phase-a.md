# Phase A verification: illustration system

Date: 2026-08-13  
Scope: Tasks 1–6 after fix round (light accent, featured pill, All-view motif softening).  
Gate: No Phase B (49 pattern drills) until this checklist holds.

## Applicability smoke (one line per cat)

| Cat | Job / world vs still | Result |
| --- | --- | --- |
| 1 | Reception badge handoff: figure + lanyard/badge to receiving palm | Verified (matches strategy §5) |
| 2 | First-day desk: seated figure, map sheet, empty chair | Verified |
| 3 | Mixer booth: figure, vertical fader + dial | Verified |
| 4 | Shared board: two figures, question → accent check | Verified |
| 5 | Kitchen pass: figure at window, ordered steps, last accent | Verified |
| 6 | Fill vessel: hand on vessel, accent fill level, muted shelf | Verified |
| 7 | Relay: two figures, violet baton only | Verified |
| 8 | Archive: figure at cabinet, accent record pulled | Verified |
| 9 | Workshop: bench, accent spare gear in reach | Verified |
| 10 | Gate: figure + indigo clipboard only, muted threshold | Verified |

## Series coherence

- Shared grammar: circle / capsule / rounded-rect / triangle / rule / quarter-arc; viewBox 320×200; angles 0/45/90.
- Verified by composition notes in `design-state.md` + static files under `assets/illustrations/categories/`.
- Screenshot strip: deferred (no automated capture in this pass); visual series check done via asset review, not a saved 10-up PNG.

## Contrast (after fix)

### Light theme (`--illu-canvas: #f7f4ee`)

- Recipe: `--illu-accent: color-mix(in srgb, var(--accent) 58%, #17181c)`.
- Dark theme unchanged: `--illu-accent: var(--accent)` (raw hex).
- Spot-check (sRGB mix vs canvas, large-shape ≥3:1 target):

| Cat | Hex | Mixed ratio vs canvas | ≥3:1 |
| --- | --- | --- | --- |
| 1 | `#f59e0b` | ~4.52:1 | Pass |
| 2 | `#34d399` | ~4.16:1 | Pass |
| 3 | `#f87171` | ~5.47:1 | Pass |
| 4 | `#f472b6` | ~5.29:1 | Pass |
| 5 | `#38bdf8` | ~4.50:1 | Pass |
| 6 | `#a3e635` | ~3.43:1 | Pass (was ~1.37 raw) |
| 7 | `#a78bfa` | ~5.33:1 | Pass |
| 8 | `#22d3ee` | ~3.97:1 | Pass |
| 9 | `#fb923c` | ~4.70:1 | Pass |
| 10 | `#818cf8` | ~5.69:1 | Pass |

- Featured pill light: `color: var(--ink)` on accent fill (text ≥4.5:1 target). Dark keeps `color: var(--bg)`.
- fg / muted floors: carried from prior a11y pass (dark + light); not re-measured pixel-by-pixel this round.

### Dark theme

- Raw category accents vs dark canvas previously passed ≥3:1; geometry unchanged. Re-spot deferred to re-review of C1 only if needed.

## Grayscale / hue-off

- Shape + pose/prop vocabulary intended to separate cats without hue.
- Formal grayscale screenshot pass: deferred (manual note: warm family 3/4/9 rely on prop/pose; cats 7/10 accent-only violet/indigo).

## Offline / no network

- Verified by design: single-file `index.html`, inline `ILLUS`, no CDN fetches for teaching art.
- `file://` open path unchanged.

## Independence audit

- No client product names, no Gemframe-as-brand field, violet/indigo only on accent props (cats 7/10).
- Spot-check of teaching SVGs + chrome: no Verena / Invictus strings in illustration layer.

## Phase gate

- Phase A = 10 category directions only.
- Phase B (49 pattern drills): not started.

## Fix round items tied to this checklist

| Item | Status |
| --- | --- |
| Light `--illu-accent` darken | Done |
| Featured pill off teaching band + light ink | Done |
| Dialog `aria-label` bilingual | Done |
| All-view same-art soften (first card full motif; siblings compact) + category-art cue on `catq` | Done |
| `contain-intrinsic-size` ~300px | Done |
| Optional cat 5/6 prop sharpening | Skipped (not needed for gate) |

## Deferred

- Saved 10-up series strip screenshot
- Formal grayscale screenshot board
- Dark-theme contrast re-measure after this pass (expected still pass)
- Optional prop sharpening for cats 5/6
- Landing mesh retirement decision
- Generator bake script (F8)
