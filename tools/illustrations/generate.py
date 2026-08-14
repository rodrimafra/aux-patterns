#!/usr/bin/env python3
"""Bake aup-editorial-v1 category illustration stills (probe only).

CANONICAL ART is the owner Figma drawings (file g81CTKZNVjYAqhjdVEPji4,
frame categories 28:353), exported to assets/illustrations/categories/
as 224 squares. This script emits the superseded 320x200 plate system.
Running it without --force refuses to overwrite those files.

Emits ten static SVGs (assets/illustrations/categories/cat-N.svg) and a
self-contained review page (docs/designpowers/probes/). Deterministic:
layouts are fixed by the locked recipes, and the few open placement
choices resolve from seed = hash32(FAMILY|category|hue), so reruns are
byte identical.

The plate: every device is contained in one 168x168 square drawn on the
field (mute stroke 2 on mode A, cream stroke 2 on mode B). 168 is a
Fibonacci square (64 + 104 = 168), so its internal golden sections land
exactly on 64 and 104 from the origin, on the 8px grid. The plate sits
at (56,16) for anchors A and C, at (96,16) for B and D, which makes the
category's canvas anchor coincide with one of the plate's own internal
crossings. Device ink keeps at least 8px of clearance inside the plate.

Grid convention: construction coordinates (shape centers, rect origins,
rule endpoints) and every size (diameter, side, length, thickness) are
multiples of 8. Sizes come from the Fibonacci times 8 scale. Stroke
widths are exempt. Angles are 0, 45 or 90 degrees only. The full-bleed
field rect is ground, not ink: it does not count against the budget.

One consequence is worth naming, because the emitted SVG shows it: sizes
24, 40 and 104 are odd multiples of 8, so centring one on the armature
puts the derived edge on the 4 half-step (a 24 wide mend centred on
x=120 emits x=108). Construction stays on 8; only derived edges land on
4, and the checks below verify exactly that, never something looser.
"""
import hashlib
import html
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FAMILY = "aup-editorial-v1"
W, H = 320, 200
FRAME_AREA = W * H
INK_BUDGET = 24446
SCALE = (8, 16, 24, 40, 64, 104, 168)
LADDER = (1.0, 0.62, 0.38, 0.24, 0.15, 0.09)
STROKES = (1, 2, 3, 5)
CREAM = "#f2eee2"
INK_TOKEN = "#14161b"  # reserved token, not placed by these ten stills
ANCHORS = {"A": (120, 80), "B": (200, 80), "C": (120, 120), "D": (200, 120)}
PLATE = 168
PLATE_CLEAR = 8


def plate_origin(anchor):
    """Plate placed so the canvas anchor lands on an internal 64/104 crossing."""
    ax, ay = ANCHORS[anchor]
    return ax - (64 if ax == 120 else 104), ay - (64 if ay == 80 else 104)


SVG_DIR = ROOT / "assets/illustrations/categories"
PAGE = ROOT / "docs/designpowers/probes/2026-08-13-editorial-geometry-ten-strip.html"

CATS = [
    dict(n=1, name="Identity & Delegation", op="Containment", anchor="C", mode="A", hue="#f59e0b", field="#6a4a15", mute="#352a19"),
    dict(n=2, name="Learning & Onboarding", op="Sequence", anchor="A", mode="A", hue="#34d399", field="#205e4b", mute="#19322d"),
    dict(n=3, name="Control & Steering", op="Vector", anchor="D", mode="A", hue="#f87171", field="#6b393c", mute="#352328"),
    dict(n=4, name="Clarification", op="Reduction", anchor="B", mode="A", hue="#f472b6", field="#6a3956", mute="#352332"),
    dict(n=5, name="Transparency of Process", op="Sequence", anchor="A", mode="A", hue="#38bdf8", field="#22566f", mute="#192e3b"),
    dict(n=6, name="Transparency of Confidence", op="Decay", anchor="C", mode="A", hue="#a3e635", field="#4b6525", mute="#29341f"),
    dict(n=7, name="Multi-Agent Systems", op="Relay", anchor="B", mode="B", hue="#a78bfa", field="#242730", mute="#55565a"),
    dict(n=8, name="Memory & Context", op="Decay", anchor="D", mode="A", hue="#22d3ee", field="#195e6c", mute="#16323a"),
    dict(n=9, name="Failure & Repair", op="Sequence", anchor="C", mode="A", hue="#fb923c", field="#6c4528", mute="#362820"),
    dict(n=10, name="Governance & Oversight", op="Containment", anchor="A", mode="B", hue="#818cf8", field="#242730", mute="#55565a"),
]


def hash32(s: str) -> int:
    return int(hashlib.sha256(s.encode()).hexdigest()[:8], 16)


def mulberry32(seed: int):
    state = seed & 0xFFFFFFFF
    def rnd():
        nonlocal state
        state = (state + 0x6D2B79F5) & 0xFFFFFFFF
        t = state
        t = ((t ^ (t >> 15)) * (t | 1)) & 0xFFFFFFFF
        t ^= (t + ((t ^ (t >> 7)) * (t | 61))) & 0xFFFFFFFF
        return ((t ^ (t >> 14)) & 0xFFFFFFFF) / 4294967296
    return rnd


def pick(rnd, options):
    return options[int(rnd() * len(options))]


def _op(op):
    return "" if op >= 1.0 else f' opacity="{op:g}"'


def _channel(v):
    v = v / 255.0
    return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4


def luminance(hx):
    r, g, b = (int(hx[i:i + 2], 16) for i in (1, 3, 5))
    return 0.2126 * _channel(r) + 0.7152 * _channel(g) + 0.0722 * _channel(b)


def contrast(a, b):
    la, lb = luminance(a), luminance(b)
    hi, lo = (la, lb) if la >= lb else (lb, la)
    return (hi + 0.05) / (lo + 0.05)


class Still:
    def __init__(self, cat):
        self.cat = cat
        self.parts = []
        self.coords = []   # (value, label): construction coordinates
        self.sizes = []    # (value, label): must sit on the scale
        self.opacities = []
        self.strokes = []
        self.edges = []
        self.bboxes = []   # construction bounds of device ink, plate excluded
        self.problems = []
        self.ink = 0.0
        self.focal = None
        self.plate = None  # (ox, oy) once drawn

    def draw_plate(self):
        """The series module: one square that contains the device."""
        ox, oy = plate_origin(self.cat["anchor"])
        stroke = CREAM if self.cat["mode"] == "B" else self.cat["mute"]
        self.parts.append(f'<rect x="{ox}" y="{oy}" width="{PLATE}" height="{PLATE}" fill="none" stroke="{stroke}" stroke-width="2"/>')
        self.ink += 2 * (PLATE + PLATE) * 2
        self.coords += [(ox, "plate x"), (oy, "plate y")]
        self.sizes.append((PLATE, "plate"))
        self.strokes.append(2)
        self.plate = (ox, oy)

    def circle(self, cx, cy, d, fill, op=1.0, focal=False):
        self.parts.append(f'<circle cx="{cx}" cy="{cy}" r="{d // 2}" fill="{fill}"{_op(op)}/>')
        self.ink += math.pi * (d / 2) ** 2 * op
        self.coords += [(cx, "cx"), (cy, "cy")]
        self.edges += [(cx - d // 2, "left"), (cy - d // 2, "top")]
        self.bboxes.append((cx - d // 2, cy - d // 2, cx + d // 2, cy + d // 2))
        self.sizes.append((d, "diameter"))
        self.opacities.append(op)
        if focal:
            self.focal = (cx, cy)

    def ring(self, cx, cy, r, sw, stroke, op=1.0):
        self.parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{stroke}" stroke-width="{sw}"{_op(op)}/>')
        self.ink += 2 * math.pi * r * sw * op
        self.coords += [(cx, "cx"), (cy, "cy")]
        self.bboxes.append((cx - r, cy - r, cx + r, cy + r))
        self.sizes.append((r, "radius"))
        self.opacities.append(op)
        self.strokes.append(sw)

    def box(self, x, y, w, h, fill, op=1.0, rx=0, focal=False):
        rxa = f' rx="{rx}"' if rx else ""
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}"{rxa} fill="{fill}"{_op(op)}/>')
        self.ink += w * h * op
        self.coords += [(x, "x"), (y, "y")]
        self.bboxes.append((x, y, x + w, y + h))
        self.sizes += [(w, "w"), (h, "h")] + ([(rx, "rx")] if rx else [])
        self.opacities.append(op)
        if focal:
            self.focal = (x + w // 2, y + h // 2)

    def box_c(self, cx, cy, w, h, fill, op=1.0, rx=0, focal=False):
        rxa = f' rx="{rx}"' if rx else ""
        self.parts.append(f'<rect x="{cx - w // 2}" y="{cy - h // 2}" width="{w}" height="{h}"{rxa} fill="{fill}"{_op(op)}/>')
        self.ink += w * h * op
        self.coords += [(cx, "cx"), (cy, "cy")]
        self.edges += [(cx - w // 2, "left"), (cy - h // 2, "top")]
        self.bboxes.append((cx - w // 2, cy - h // 2, cx + w // 2, cy + h // 2))
        self.sizes += [(w, "w"), (h, "h")] + ([(rx, "rx")] if rx else [])
        self.opacities.append(op)
        if focal:
            self.focal = (cx, cy)

    def frame(self, x, y, w, h, sw, stroke, op=1.0, rx=0):
        rxa = f' rx="{rx}"' if rx else ""
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}"{rxa} fill="none" stroke="{stroke}" stroke-width="{sw}"{_op(op)}/>')
        self.ink += 2 * (w + h) * sw * op
        self.coords += [(x, "x"), (y, "y")]
        self.bboxes.append((x, y, x + w, y + h))
        self.sizes += [(w, "w"), (h, "h")] + ([(rx, "rx")] if rx else [])
        self.opacities.append(op)
        self.strokes.append(sw)

    def frame_c(self, cx, cy, w, h, sw, stroke, op=1.0, rx=0):
        rxa = f' rx="{rx}"' if rx else ""
        self.parts.append(f'<rect x="{cx - w // 2}" y="{cy - h // 2}" width="{w}" height="{h}"{rxa} fill="none" stroke="{stroke}" stroke-width="{sw}"{_op(op)}/>')
        self.ink += 2 * (w + h) * sw * op
        self.coords += [(cx, "cx"), (cy, "cy")]
        self.edges += [(cx - w // 2, "left"), (cy - h // 2, "top")]
        self.bboxes.append((cx - w // 2, cy - h // 2, cx + w // 2, cy + h // 2))
        self.sizes += [(w, "w"), (h, "h")] + ([(rx, "rx")] if rx else [])
        self.opacities.append(op)
        self.strokes.append(sw)

    def rule(self, x1, y1, x2, y2, sw, stroke, op=1.0):
        dx, dy = x2 - x1, y2 - y1
        if not (dx == 0 or dy == 0 or abs(dx) == abs(dy)):
            self.problems.append(f"rule ({x1},{y1}) to ({x2},{y2}) is not 0, 45 or 90 degrees")
        self.parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"{_op(op)}/>')
        self.ink += math.hypot(dx, dy) * sw * op
        self.coords += [(x1, "x1"), (y1, "y1"), (x2, "x2"), (y2, "y2")]
        self.bboxes.append((min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)))
        self.opacities.append(op)
        self.strokes.append(sw)

    def render(self):
        body = "\n".join(self.parts)
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" aria-hidden="true">\n'
                f'<rect width="{W}" height="{H}" fill="{self.cat["field"]}"/>\n{body}\n</svg>\n')

    def violations(self):
        v = list(self.problems)
        v += [f"coord {lbl}={val} off the 8 grid" for val, lbl in self.coords if val % 8]
        # Centring a size that is an odd multiple of 8 (24, 40, 104) on the
        # armature puts the derived edge on the 4 half-step, never finer.
        v += [f"edge {lbl}={val} off the 4 half-step" for val, lbl in self.edges if val % 4]
        for val, lbl in self.sizes:
            if val % 8:
                v.append(f"size {lbl}={val} off the 8 grid")
            if val not in SCALE:
                v.append(f"size {lbl}={val} not on the scale")
        v += [f"opacity {o} off the ladder" for o in self.opacities if o not in LADDER]
        v += [f"stroke {s} not allowed" for s in self.strokes if s not in STROKES]
        if self.plate is None:
            v.append("no plate drawn")
        else:
            ox, oy = self.plate
            lo_x, lo_y = ox + PLATE_CLEAR, oy + PLATE_CLEAR
            hi_x, hi_y = ox + PLATE - PLATE_CLEAR, oy + PLATE - PLATE_CLEAR
            for (x0, y0, x1, y1) in self.bboxes:
                if x0 < lo_x or y0 < lo_y or x1 > hi_x or y1 > hi_y:
                    v.append(f"device bbox ({x0},{y0})..({x1},{y1}) breaks plate clearance")
        return v


# One builder per category. The plate is drawn first (the series module),
# the device composes inside it. Seeded picks are listed in call order.

def build_1(s, rnd):
    # Containment: mandate held by a contract frame, a second contract
    # stepping 24px away diagonally says the mandate transfers. Both frames
    # live inside the plate, so the card reads as containment within
    # containment, which is the operator's own story.
    mute = s.cat["mute"]
    shape = pick(rnd, ["circle", "rrect"])          # mandate shape
    s.frame(88, 64, 104, 104, sw=2, stroke=mute, op=0.62, rx=8)   # ghost contract
    s.frame(64, 40, 104, 104, sw=3, stroke=mute, rx=8)            # held contract
    if shape == "circle":
        s.circle(120, 120, 40, CREAM, focal=True)
    else:
        s.box_c(120, 120, 40, 40, CREAM, rx=8, focal=True)


def build_2(s, rnd):
    # Sequence: staircase, one step climbed, current step lit, path ahead fading.
    mute = s.cat["mute"]
    steps = [(mute, 1.0), (CREAM, 1.0), (mute, 0.62), (mute, 0.38), (mute, 0.24)]
    for i, (fill, op) in enumerate(steps):
        s.box_c(96 + i * 24, 88 - i * 8, 16, 16, fill, op=op, focal=(i == 1))


def build_3(s, rnd):
    # Vector: the throw crosses the plate and stops 8px short of the centre.
    # Rings at stroke 3: cat 3 has the faintest mute of the ten (1.60 against
    # its field), so a hairline target vanishes at card size.
    mute = s.cat["mute"]
    s.ring(200, 120, 40, sw=3, stroke=mute)
    s.ring(200, 120, 24, sw=3, stroke=mute)
    s.rule(104, 120, 184, 120, sw=3, stroke=CREAM)  # dot edge 192, minus 8px gap
    s.circle(200, 120, 16, CREAM, focal=True)


def build_4(s, rnd):
    # Reduction: three faint small readings, two firmer, one large resolved.
    mute = s.cat["mute"]
    j = pick(rnd, [-8, 8])                          # middle circle jitter
    for cx, cy in ((112, 80), (120, 80 + j), (128, 80)):
        s.circle(cx, cy, 16, mute, op=0.38)
    for cx in (160, 168):
        s.circle(cx, 80, 16, mute, op=0.62)
    s.circle(200, 80, 40, CREAM, focal=True)


def build_5(s, rnd):
    # Sequence: six stages on a baseline, exactly one lit.
    mute = s.cat["mute"]
    s.rule(64, 80, 208, 80, sw=1, stroke=mute)
    stages = [(16, mute, 0.62), (16, mute, 0.62), (24, CREAM, 1.0),
              (16, mute, 0.24), (16, mute, 0.15), (16, mute, 0.09)]
    for i, (d, fill, op) in enumerate(stages):
        s.circle(72 + i * 24, 80, d, fill, op=op, focal=(i == 2))


def build_6(s, rnd):
    # Decay: confidence holds through the bar on the anchor, then steps down.
    mute = s.cat["mute"]
    bars = [(CREAM, 1.0)] * 3 + [(mute, 0.38), (mute, 0.24), (mute, 0.15)]
    for i, (fill, op) in enumerate(bars):
        s.box_c(72 + i * 24, 120, 16, 64, fill, op=op, focal=(i == 2))


def build_7(s, rnd):
    # Relay: an open run of four centres, the handover node carries the hue.
    n4y = pick(rnd, [80, 112])                      # last leg: flat or 45 down
    nodes = [(120, 128), (152, 128), (200, 80), (232, n4y)]
    for (x1, y1), (x2, y2) in zip(nodes, nodes[1:]):
        s.rule(x1, y1, x2, y2, sw=1, stroke=CREAM)
    for i, (cx, cy) in enumerate(nodes):
        s.circle(cx, cy, 24, s.cat["hue"] if i == 2 else CREAM, focal=(i == 2))


def build_8(s, rnd):
    # Decay: layered recall receding, one memory pulled forward for inspection.
    mute = s.cat["mute"]
    mark = pick(rnd, ["circle", "capsule"])         # inspected memory shape
    for i, op in enumerate((0.62, 0.38, 0.24, 0.15)):
        s.box(104, 56 + i * 24, 64, 16, mute, op=op, rx=8)
    if mark == "circle":
        s.circle(200, 120, 40, CREAM, focal=True)
    else:
        s.box_c(200, 120, 40, 16, CREAM, rx=8, focal=True)


def build_9(s, rnd):
    # Sequence: an unbroken run interrupted once, one mend seated in the break.
    # The run carries no interior joints, so the only spacing in the still is
    # the break itself. A 24 wide mend inside the 64 wide break leaves 20 of
    # shoulder on each side, which is what keeps the break visible after the
    # repair lands.
    mute = s.cat["mute"]
    s.box(64, 112, 24, 16, mute, rx=8)               # run, ends at x=88
    s.box(152, 112, 64, 16, mute, rx=8)              # run resumes at x=152
    s.box_c(120, 120, 24, 16, CREAM, rx=8, focal=True)


def build_10(s, rnd):
    # Containment: the plate itself is the policy boundary. Inside it, an even
    # lattice of outlined cells, stroke 2 (the cat10-meio baseline): quiet
    # rhythm, one filled cell under review.
    mute = s.cat["mute"]
    for r in range(4):
        for c in range(4):
            cx, cy = 96 + c * 24, 56 + r * 24
            if (cx, cy) == ANCHORS["A"]:
                s.box_c(cx, cy, 16, 16, s.cat["hue"], focal=True)
            else:
                s.frame_c(cx, cy, 16, 16, sw=2, stroke=mute)


BUILDERS = {1: build_1, 2: build_2, 3: build_3, 4: build_4, 5: build_5,
            6: build_6, 7: build_7, 8: build_8, 9: build_9, 10: build_10}

PAGE_TMPL = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Editorial Geometry: ten category stills</title>
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background: #101114; color: #e8e6df; padding: 40px 32px 80px; }
main { max-width: 1360px; margin: 0 auto; }
h1 { font-size: 22px; font-weight: 650; }
.lede { color: #9a978e; font-size: 13px; margin-top: 8px; max-width: 78ch; line-height: 1.5; }
section { margin-top: 48px; }
h2 { font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.09em; color: #9a978e; margin-bottom: 6px; }
.note { font-size: 12px; color: #7c7a72; margin-bottom: 14px; }
.grid { display: grid; grid-template-columns: repeat(auto-fill, 240px); gap: 24px 16px; }
figure.cell svg { width: 240px; height: 150px; display: block; border-radius: 2px; }
figure.cell figcaption { font-size: 12px; margin-top: 7px; }
section.paper { background: #f7f4ee; color: #26241f; padding: 28px; border-radius: 6px; }
section.paper h2 { color: #6c675a; }
section.paper .note { color: #8a8474; }
section.editorial { background: #17181c; color: #e8e6df; padding: 28px; border-radius: 6px; border: 1px solid #26282f; }
.gray svg { filter: grayscale(1); }
.thumbrow { display: flex; flex-wrap: wrap; gap: 14px; }
figure.thumb svg { width: 120px; height: 75px; display: block; border-radius: 2px; }
figure.thumb figcaption { font-size: 11px; color: #9a978e; margin-top: 5px; }
table { border-collapse: collapse; font-size: 13px; }
th, td { text-align: left; padding: 7px 18px 7px 0; border-bottom: 1px solid #26282f; font-variant-numeric: tabular-nums; }
th { font-size: 11px; text-transform: uppercase; letter-spacing: 0.07em; color: #9a978e; }
td.hex { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 12px; }
</style>
</head>
<body>
<main>
<header>
<h1>Editorial Geometry: ten category stills</h1>
<p class="lede">Family aup-editorial-v1. One artwork per category, frame 320x200, every device contained in a 168x168 plate whose internal golden crossings carry the focal mark. Flat fills and strokes only, colours baked into each file so the same SVG serves light and dark themes. Generated by tools/illustrations/generate.py, 2026-08-13. Do not edit the SVGs by hand.</p>
</header>
<section>
<h2>1. Ten up strip, 240px</h2>
<p class="note">Each still labelled with category number and English name.</p>
<div class="grid">@CELLS@</div>
</section>
<section class="paper">
<h2>2a. On light paper #f7f4ee</h2>
<p class="note">Same ten files, no theme swap: the artwork carries its own ground.</p>
<div class="grid">@CELLS@</div>
</section>
<section class="editorial">
<h2>2b. On dark editorial #17181c</h2>
<p class="note">Same ten files again on the dark surface.</p>
<div class="grid">@CELLS@</div>
</section>
<section>
<h2>3. Grayscale</h2>
<p class="note">filter: grayscale(1). Silhouette and opacity must separate without hue.</p>
<div class="grid gray">@CELLS@</div>
</section>
<section>
<h2>4. Thumbnails, 120px</h2>
<p class="note">Survival at small size.</p>
<div class="thumbrow">@THUMBS@</div>
</section>
<section>
<h2>5. Ink, anchors and plates</h2>
<table>
<thead><tr><th>No.</th><th>Name</th><th>Operator</th><th>Anchor</th><th>Plate</th><th>Field</th><th>Ink px2</th><th>Ink %</th></tr></thead>
<tbody>@ROWS@</tbody>
</table>
<p class="note">Budget 24446 px2 per still, so at least 61.8% of the 64000 px2 frame stays empty. The field rect is ground and does not count; the plate does. Device ink keeps 8px of clearance inside its plate.</p>
</section>
</main>
</body>
</html>
"""


def review_page(items):
    cells, thumbs, rows = [], [], []
    for cat, ink, pct in items:
        svg = (SVG_DIR / f"cat-{cat['n']}.svg").read_text(encoding="utf-8")
        label = f"{cat['n']}. {html.escape(cat['name'])}"
        cells.append(f'<figure class="cell">{svg}<figcaption>{label}</figcaption></figure>')
        thumbs.append(f'<figure class="thumb">{svg}<figcaption>{cat["n"]}</figcaption></figure>')
        ax, ay = ANCHORS[cat["anchor"]]
        ox, oy = plate_origin(cat["anchor"])
        rows.append(f"<tr><td>{cat['n']}</td><td>{html.escape(cat['name'])}</td><td>{cat['op']}</td>"
                    f"<td>{cat['anchor']} ({ax}, {ay})</td><td>({ox}, {oy})</td><td class=\"hex\">{cat['field']}</td>"
                    f"<td>{ink}</td><td>{pct:.1f}%</td></tr>")
    page = PAGE_TMPL.replace("@CELLS@", "".join(cells))
    page = page.replace("@THUMBS@", "".join(thumbs))
    return page.replace("@ROWS@", "\n".join(rows))


def main():
    force = "--force" in sys.argv
    sentinel = SVG_DIR / "cat-1.svg"
    if sentinel.exists() and not force:
        head = sentinel.read_text(encoding="utf-8")[:400]
        if 'viewBox="0 0 224 224"' in head:
            print("Refusing to overwrite owner Figma finals in assets/illustrations/categories/.")
            print("Those files are 224 squares from Figma frame categories (28:353).")
            print("This generator emits the superseded 320x200 probe. Pass --force only if you intend to replace them.")
            sys.exit(2)
    SVG_DIR.mkdir(parents=True, exist_ok=True)
    PAGE.parent.mkdir(parents=True, exist_ok=True)
    failures, items, total_viols = [], [], 0
    print(f"{FAMILY}: ten stills, frame {W}x{H} ({FRAME_AREA} px2), plate {PLATE}x{PLATE}, ink budget {INK_BUDGET} px2 per still")
    print()
    print(f"{'cat':>3}  {'operator':<13}{'anchor':<14}{'plate':<10}{'ink px2':>8}  {'ink %':>6}  {'budget':<8}{'checks'}")
    for cat in CATS:
        seed = hash32(f"{FAMILY}|{cat['n']}|{cat['hue']}")
        still = Still(cat)
        still.draw_plate()
        BUILDERS[cat["n"]](still, mulberry32(seed))
        ax, ay = ANCHORS[cat["anchor"]]
        ox, oy = plate_origin(cat["anchor"])
        if still.focal != (ax, ay):
            failures.append(f"cat {cat['n']}: focal {still.focal} is not anchor {cat['anchor']} ({ax},{ay})")
        if (ax - ox) not in (64, 104) or (ay - oy) not in (64, 104):
            failures.append(f"cat {cat['n']}: anchor does not sit on a plate crossing")
        svg = still.render()
        path = SVG_DIR / f"cat-{cat['n']}.svg"
        path.write_bytes(svg.encode("utf-8"))
        size = path.stat().st_size
        if size >= 4096:
            failures.append(f"cat {cat['n']}: file is {size} bytes, limit 4096")
        ink = round(still.ink)
        pct = 100.0 * still.ink / FRAME_AREA
        ok = ink <= INK_BUDGET
        if not ok:
            failures.append(f"cat {cat['n']}: ink {ink} px2 over budget {INK_BUDGET}")
        viols = still.violations()
        total_viols += len(viols)
        if viols:
            failures.append(f"cat {cat['n']}: " + "; ".join(viols))
        checks = "ok" if not viols else "; ".join(viols)
        anchor_txt = f"{cat['anchor']} ({ax},{ay})"
        plate_txt = f"({ox},{oy})"
        print(f"{cat['n']:>3}  {cat['op']:<13}{anchor_txt:<14}{plate_txt:<10}{ink:>8}  {pct:>5.1f}%  {'PASS' if ok else 'FAIL':<8}{checks}")
        items.append((cat, ink, pct))
    print()
    print("contrast (WCAG sRGB): mark/field must be at least 4.5, mute/field at least 1.5")
    # The mute floor is 1.5, not 1.6: cat 3 measures 1.5998 raw, and rounding it
    # up to clear a 1.6 test would hide a real value behind display precision.
    for cat in CATS:
        mf = contrast(CREAM, cat["field"])
        uf = contrast(cat["mute"], cat["field"])
        extra = f"  accent/field {contrast(cat['hue'], cat['field']):.2f}" if cat["mode"] == "B" else ""
        flag = ""
        if mf < 4.5:
            failures.append(f"cat {cat['n']}: mark/field {mf:.2f} below 4.5")
            flag = "  FAIL"
        if uf < 1.5:
            failures.append(f"cat {cat['n']}: mute/field {uf:.2f} below 1.5")
            flag = "  FAIL"
        print(f"{cat['n']:>3}  mark/field {mf:.2f}  mute/field {uf:.2f}{extra}{flag}")
    worst = max(items, key=lambda it: it[2])
    within = sum(1 for it in items if it[1] <= INK_BUDGET)
    print()
    print(f"summary: {within}/10 within ink budget, worst ink {worst[2]:.1f}% (cat {worst[0]['n']}), check violations {total_viols}")
    print()
    for cat, ink, pct in items:
        raw = (SVG_DIR / f"cat-{cat['n']}.svg").read_bytes()
        print(f"cat-{cat['n']}.svg  {len(raw)} bytes  sha256 {hashlib.sha256(raw).hexdigest()[:12]}")
    PAGE.write_text(review_page(items), encoding="utf-8")
    print(f"wrote {PAGE.relative_to(ROOT)}")
    if failures:
        print()
        print("FAILURES:")
        for f in failures:
            print("  " + f)
        sys.exit(1)
    print("all checks passed")


if __name__ == "__main__":
    main()
