#!/usr/bin/env python3
"""Bake 49 Phase B pattern stills from the Figma category alphabet. Dev-only."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "assets" / "illustrations" / "patterns"
PROBE = ROOT / "docs" / "designpowers" / "probes" / "2026-08-14-pattern-stills-strip.html"
CREAM = "#F2EEE2"
FIELDS = {
    1: "#326E36", 2: "#E95444", 3: "#B15556", 4: "#AF5586", 5: "#2A7EA4",
    6: "#5D8028", 7: "#A6307F", 8: "#1C8293", 9: "#A86530", 10: "#297AA3",
}
CELL, GAP, PAD = 42.5, 10.0, 12.0

NAMES = {
    "1.1": "Agent identity & role contract", "1.2": "Delegation modes",
    "2.1": "Sandboxed playgrounds", "2.2": "Wayfinders",
    "2.3": "Progressive disclosure modes", "2.4": "Teach-me interfaces",
    "2.5": "Scenario templates & recipes", "2.6": "Feedback & rating controls",
    "3.1": "Kill switch, pause & resume", "3.2": "Human-in-the-loop gates",
    "3.3": "Plan-then-execute workflow", "3.4": "Steerability & polite interruption",
    "3.5": "Scoped permissions & tool consent", "3.6": "Rollback & version history",
    "3.7": "User-directed tool use",
    "4.1": "Structured clarification prompts", "4.2": "Edit request",
    "4.3": "Confirmed assumptions",
    "5.1": "Reasoning glimpse", "5.2": "Streaming results visualizations",
    "5.3": "Tool usage indicators", "5.4": "Activity timeline & audit log",
    "5.5": "Execution progress view", "5.6": "Confessions view",
    "6.1": "Source anchoring & grounding", "6.2": "Confidence thermometer",
    "6.3": "Semantic highlighting of uncertainty", "6.4": "Multiple presented options",
    "6.5": "Explanation on demand", "6.6": "Counter-evidence",
    "7.1": "Orchestration graph", "7.2": "Agent registry & profiles",
    "7.3": "Supervisor agent", "7.4": "Agent handover briefs",
    "7.5": "Assignment boards & work queues", "7.6": "Escalation & fallback routing",
    "8.1": "Memory inspector & editor", "8.2": "Preference persona settings",
    "8.3": "Privacy & data usage controls", "8.4": "Context repository & workspace profiles",
    "8.5": "Personal context profiles",
    "9.1": "Safe failure states", "9.2": "Guided repair flows",
    "9.3": "Sentiment-aware response styles", "9.4": "Apology & remedy bundle",
    "10.1": "Fleet health dashboard", "10.2": "Risk & policy heatmaps",
    "10.3": "Access & permission tiers for agents",
    "10.4": "Workflow & policy template library",
}


def box(c, r):
    x = PAD + c * (CELL + GAP)
    y = PAD + r * (CELL + GAP)
    return x, y, x + CELL, y + CELL


def fill_cell(c, r, op=1.0):
    x0, y0, x1, y1 = box(c, r)
    op_attr = "" if op >= 0.999 else f' fill-opacity="{op:g}"'
    return f'<path d="M{x1:g} {y0:g}H{x0:g}V{y1:g}H{x1:g}V{y0:g}Z" fill="{CREAM}"{op_attr}/>'


def stroke_cell(c, r):
    x0, y0, x1, y1 = box(c, r)
    return (
        f'<path d="M{x1-2:g} {y0+2:g}V{y1-2:g}H{x0+2:g}V{y0+2:g}H{x1-2:g}Z" '
        f'stroke="black" stroke-opacity="0.2" stroke-width="4"/>'
    )


def wrap(n, field, inner, clip=False):
    cid = "clip-pat-" + n.replace(".", "-")
    body = f'<rect width="224" height="224" fill="{field}"/>\n{inner}'
    if clip:
        body = (
            f'<g clip-path="url(#{cid})">\n{body}\n</g>\n'
            f'<defs><clipPath id="{cid}"><rect width="224" height="224" fill="white"/></clipPath></defs>'
        )
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 224 224" fill="none" aria-hidden="true">\n'
        f"{body}\n</svg>\n"
    )


def grid(cells):
    parts = []
    for r in range(4):
        for c in range(4):
            v = cells.get((c, r), "stroke")
            if v == "stroke" or v is None:
                parts.append(stroke_cell(c, r))
            elif v == "empty":
                continue
            else:
                parts.append(fill_cell(c, r, float(v)))
    return "\n".join(parts)


def from_set(n, field, filled):
    cells = {(c, r): "stroke" for c in range(4) for r in range(4)}
    cells.update(filled)
    return wrap(n, field, grid(cells))


def all_stills():
    f1, f2, f3, f4 = FIELDS[1], FIELDS[2], FIELDS[3], FIELDS[4]
    f5, f6, f7, f8, f9, f10 = FIELDS[5], FIELDS[6], FIELDS[7], FIELDS[8], FIELDS[9], FIELDS[10]
    firm = (
        '<path d="M163.026 16.6667H27.6409C20.8436 16.6667 15.3333 22.1771 15.3333 28.9744V164.359'
        'C15.3333 171.156 20.8436 176.667 27.6409 176.667H163.026C169.823 176.667 175.333 171.156 '
        '175.333 164.359V28.9744C175.333 22.1771 169.823 16.6667 163.026 16.6667Z" '
        'stroke="#0D0D0D" stroke-opacity="0.2" stroke-width="4"/>'
    )
    loose = (
        '<path d="M195.026 48.6667H59.6409C52.8436 48.6667 47.3333 54.1771 47.3333 60.9744V196.359'
        'C47.3333 203.156 52.8436 208.667 59.6409 208.667H195.026C201.823 208.667 207.333 203.156 '
        '207.333 196.359V60.9744C207.333 54.1771 201.823 48.6667 195.026 48.6667Z" '
        'stroke="#0D0D0D" stroke-opacity="0.2" stroke-width="3"/>'
    )
    circ_in = (
        f'<path d="M95.333 112.333C108.588 112.333 119.333 101.588 119.333 88.333C119.333 75.078 '
        f'108.588 64.333 95.333 64.333C82.078 64.333 71.333 75.078 71.333 88.333C71.333 101.588 '
        f'82.078 112.333 95.333 112.333Z" fill="{CREAM}"/>'
    )
    circ_edge = (
        f'<path d="M151.333 179.333C164.588 179.333 175.333 168.588 175.333 155.333C175.333 142.078 '
        f'164.588 131.333 151.333 131.333C138.078 131.333 127.333 142.078 127.333 155.333C127.333 168.588 '
        f'138.078 179.333 151.333 179.333Z" fill="{CREAM}"/>'
    )
    outer = '<path d="M191.25 65V159H97.25V65H191.25Z" stroke="black" stroke-opacity="0.15" stroke-width="2"/>'
    inner = '<path d="M182.25 74V150H106.25V74H182.25Z" stroke="black" stroke-opacity="0.3" stroke-width="4"/>'
    square = f'<path d="M165.5 90.75H123V133.25H165.5V90.75Z" fill="{CREAM}"/>'
    extra = '<path d="M173.25 83V141H115.25V83H173.25Z" stroke="black" stroke-opacity="0.2" stroke-width="4"/>'
    left9 = '<rect x="14" y="94" width="60" height="36" stroke="black" stroke-opacity="0.2" stroke-width="4"/>'
    right9 = '<rect x="150" y="94" width="60" height="36" stroke="black" stroke-opacity="0.2" stroke-width="4"/>'
    mend = f'<rect x="92" y="92" width="40" height="40" fill="{CREAM}"/>'

    def bars8(xs, missing=None):
        parts = []
        for i, y in enumerate((42, 82, 122, 162)):
            if missing is not None and i == missing:
                continue
            for x in xs:
                parts.append(
                    f'<rect x="{x}" y="{y}" width="100" height="20" rx="2" '
                    f'stroke="black" stroke-opacity="0.2" stroke-width="4"/>'
                )
        return "\n".join(parts)

    def c2(n, filled):
        cells = {(c, r): "stroke" for c in range(4) for r in range(4)}
        cells.update(filled)
        return wrap(n, f2, grid(cells))

    x0, y0, x1, y1 = box(1, 1)
    ring51 = (
        f'<path d="M{x1+4:g} {y0-4:g}V{y1+4:g}H{x0-4:g}V{y0-4:g}H{x1+4:g}Z" '
        f'stroke="{CREAM}" stroke-width="3" fill="none"/>'
    )
    gx0, gy0, gx1, gy1 = box(2, 2)
    ghost10 = (
        f'<path d="M{gx1-2:g} {gy0+2:g}V{gy1-2:g}H{gx0+2:g}V{gy0+2:g}H{gx1-2:g}Z" '
        f'stroke="{CREAM}" stroke-opacity="0.45" stroke-width="4"/>'
    )

    cells23 = {}
    ramp = [[0.15, 0.35, 0.55, 0.7], [0.12, 0.3, 0.5, 0.65], [0.1, 0.25, 0.45, 0.55], [0.08, 0.2, 0.35, 0.45]]
    for r in range(4):
        for c in range(4):
            cells23[(c, r)] = ramp[r][c]
    cells23[(2, 0)] = 1
    cells24 = {(c, r): 0.12 for c in range(4) for r in range(4)}
    cells24[(2, 1)] = 1
    for dc, dr in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        cells24[(2 + dc, 1 + dr)] = 0.5

    cells61 = {}
    for r in range(4):
        cells61[(0, r)] = 1
        cells61[(1, r)] = 0.75
        cells61[(2, r)] = 0.25
        cells61[(3, r)] = "stroke"
    cells63 = dict(cells61)
    cells63[(1, 2)] = 0.12
    cells103 = {}
    for c in range(4):
        cells103[(c, 0)] = 1
        cells103[(c, 1)] = 0.55
        cells103[(c, 2)] = 0.25
        cells103[(c, 3)] = "stroke"

    dashes = "".join(f'<rect x="{x}" y="108" width="10" height="8" fill="{CREAM}"/>' for x in (8, 26, 44, 62))
    stills = {
        "1.1": wrap("1.1", f1, firm + "\n" + circ_in),
        "1.2": wrap("1.2", f1, firm + "\n" + loose + "\n" + circ_edge),
        "2.1": c2("2.1", {(1, 1): 1, (2, 1): 0.75, (1, 2): 0.75, (2, 2): 0.5}),
        "2.2": c2("2.2", {(0, 1): 0.35, (1, 1): 0.6, (2, 1): 1, (3, 1): 0.25}),
        "2.3": wrap("2.3", f2, grid(cells23)),
        "2.4": wrap("2.4", f2, grid(cells24)),
        "2.5": c2("2.5", {(0, 0): 1, (2, 1): 1, (3, 3): 1}),
        "2.6": c2("2.6", {(3, 0): 1, (0, 3): 0.7, (1, 1): 0.2}),
        "3.1": wrap("3.1", f3, f"{outer}\n{inner}\n<rect y=\"108\" width=\"100\" height=\"8\" fill=\"{CREAM}\"/>\n{square}"),
        "3.2": wrap("3.2", f3, f"{outer}\n{inner}\n<rect y=\"108\" width=\"144\" height=\"8\" fill=\"{CREAM}\"/>\n<rect x=\"108\" y=\"70\" width=\"8\" height=\"84\" fill=\"{CREAM}\"/>\n{square}"),
        "3.3": wrap("3.3", f3, f"{outer}\n{inner}\n{dashes}\n<rect x=\"80\" y=\"108\" width=\"64\" height=\"8\" fill=\"{CREAM}\"/>\n{square}"),
        "3.4": wrap("3.4", f3, f"{outer}\n{inner}\n<rect y=\"96\" width=\"144\" height=\"8\" fill=\"{CREAM}\"/>\n{square}"),
        "3.5": wrap("3.5", f3, f"{outer}\n{inner}\n{extra}\n<rect y=\"108\" width=\"144\" height=\"8\" fill=\"{CREAM}\"/>\n{square}"),
        "3.6": wrap("3.6", f3, f"{outer}\n{inner}\n<rect y=\"108\" width=\"144\" height=\"8\" fill=\"{CREAM}\"/>\n<rect x=\"165.5\" y=\"128\" width=\"50\" height=\"4\" fill=\"{CREAM}\" fill-opacity=\"0.4\"/>\n{square}"),
        "3.7": wrap("3.7", f3, f"{outer}\n{inner}\n<rect y=\"108\" width=\"123\" height=\"8\" fill=\"{CREAM}\"/>\n<path d=\"M123 90.75H80.5V133.25H123V90.75Z\" fill=\"{CREAM}\"/>"),
        "4.1": wrap("4.1", f4, "\n".join([
            f'<path d="M58 40.24H22V183.76H58V40.24Z" fill="{CREAM}" fill-opacity="0.3"/>',
            f'<path d="M104 40.24H68V183.76H104V40.24Z" fill="{CREAM}" fill-opacity="0.5"/>',
            f'<path d="M150 40.24H114V183.76H150V40.24Z" fill="{CREAM}" fill-opacity="0.8"/>',
            f'<path d="M196 40.24H160V183.76H196V40.24Z" fill="{CREAM}"/>',
        ]), clip=True),
        "4.2": wrap("4.2", f4, "\n".join([
            f'<path d="M58 40.24H22V183.76H58V40.24Z" fill="{CREAM}" fill-opacity="0.3"/>',
            f'<path d="M104 40.24H68V183.76H104V40.24Z" fill="{CREAM}" fill-opacity="0.55"/>',
            f'<path d="M150 72H114V160H150V72Z" fill="{CREAM}" fill-opacity="0.8"/>',
            f'<path d="M196 40.24H160V183.76H196V40.24Z" fill="{CREAM}"/>',
        ]), clip=True),
        "4.3": wrap("4.3", f4, "\n".join([
            f'<path d="M58 40.24H22V183.76H58V40.24Z" fill="{CREAM}" fill-opacity="0.3"/>',
            f'<path d="M104 40.24H68V183.76H104V40.24Z" fill="{CREAM}" fill-opacity="0.55"/>',
            f'<path d="M150 40.24H114V183.76H150V40.24Z" fill="{CREAM}" fill-opacity="0.8"/>',
            f'<path d="M196 40.24H160V183.76H196V40.24Z" fill="{CREAM}"/>',
            '<path d="M200 36.24V187.76H156V36.24H200Z" stroke="#F2EEE2" stroke-width="3"/>',
        ]), clip=True),
        "5.1": wrap("5.1", f5, grid({(c, r): "stroke" for c in range(4) for r in range(4)} | {(0, 1): 0.5, (1, 1): 1}) + "\n" + ring51),
        "5.2": from_set("5.2", f5, {(1, 1): 1, (2, 1): 0.45, (3, 1): 0.2}),
        "5.3": from_set("5.3", f5, {(0, 1): 0.5, (1, 1): 1, (3, 0): 0.85}),
        "5.4": from_set("5.4", f5, {(0, 1): 0.5, (1, 1): 1, (0, 2): 0.35, (1, 2): 0.6, (2, 2): 0.25}),
        "5.5": from_set("5.5", f5, {(0, 1): 0.35, (1, 1): 0.5, (2, 1): 1}),
        "5.6": from_set("5.6", f5, {(0, 2): 0.5, (1, 1): 1}),
        "6.1": wrap("6.1", f6, grid(cells61) + f'\n<rect x="12" y="214" width="95" height="6" fill="{CREAM}"/>'),
        "6.2": from_set("6.2", f6, {(0, r): 1 for r in range(4)} | {(1, r): 0.4 for r in range(4)}),
        "6.3": wrap("6.3", f6, grid(cells63)),
        "6.4": from_set("6.4", f6, {(2, 1): 1, (3, 1): 1}),
        "6.5": from_set("6.5", f6, {(1, 1): 1}),
        "6.6": from_set("6.6", f6, {(0, r): 1 for r in range(4)} | {(3, 3): 0.35}),
        "7.1": from_set("7.1", f7, {(0, 0): 1, (1, 1): 1, (2, 1): 1, (0, 2): 1, (3, 2): 1, (2, 3): 1, (3, 0): 1}),
        "7.2": from_set("7.2", f7, {(0, 0): 1, (1, 0): 1, (0, 1): 1, (2, 2): 1, (3, 2): 1, (2, 3): 1}),
        "7.3": from_set("7.3", f7, {(0, 0): 1, (1, 1): 0.5, (2, 1): 0.5, (0, 2): 0.5, (3, 2): 0.5, (2, 3): 0.5}),
        "7.4": from_set("7.4", f7, {(1, 1): 1, (2, 1): 1}),
        "7.5": from_set("7.5", f7, {(0, 2): 1, (1, 2): 1, (2, 2): 1, (3, 2): 1}),
        "7.6": from_set("7.6", f7, {(0, 3): 1, (1, 2): 1, (2, 1): 1, (3, 0): 1}),
        "8.1": wrap("8.1", f8, bars8([26]) + f'\n<rect x="148" y="104" width="48" height="48" fill="{CREAM}"/>\n<rect x="142" y="98" width="60" height="60" fill="none" stroke="{CREAM}" stroke-width="3"/>'),
        "8.2": wrap("8.2", f8, bars8([26]) + f'\n<rect x="132" y="88" width="48" height="48" fill="{CREAM}"/>'),
        "8.3": wrap("8.3", f8, bars8([26], missing=2) + f'\n<rect x="148" y="104" width="48" height="48" fill="{CREAM}"/>'),
        "8.4": wrap("8.4", f8, bars8([18, 80]) + f'\n<rect x="168" y="88" width="40" height="40" fill="{CREAM}"/>'),
        "8.5": wrap("8.5", f8, bars8([26]) + f'\n<rect x="148" y="78" width="64" height="64" fill="{CREAM}"/>'),
        "9.1": wrap("9.1", f9, left9 + "\n" + right9),
        "9.2": wrap("9.2", f9, left9 + "\n" + right9 + "\n" + mend),
        "9.3": wrap("9.3", f9, '<rect x="8" y="94" width="52" height="36" stroke="black" stroke-opacity="0.2" stroke-width="4"/>\n<rect x="164" y="94" width="52" height="36" stroke="black" stroke-opacity="0.2" stroke-width="4"/>\n' + mend),
        "9.4": wrap("9.4", f9, left9 + "\n" + right9 + "\n" + mend + f'\n<rect x="138" y="102" width="16" height="16" fill="{CREAM}"/>'),
        "10.1": from_set("10.1", f10, {(3, 0): 1}),
        "10.2": from_set("10.2", f10, {(1, 1): 1, (2, 1): 0.5, (3, 1): 0.25}),
        "10.3": wrap("10.3", f10, grid(cells103)),
        "10.4": wrap("10.4", f10, grid({(c, r): "stroke" for c in range(4) for r in range(4)} | {(1, 1): 1}) + "\n" + ghost10),
    }
    return stills


def minify(svg):
    return "".join(line.strip() for line in svg.splitlines() if line.strip())


def write_strip(stills):
    figures, thumbs = [], []
    for n, svg in stills.items():
        cap = f"{n} {NAMES[n]}"
        figures.append(f'<figure class="cell">{svg}<figcaption>{cap}</figcaption></figure>')
        thumbs.append(f'<figure class="thumb">{svg}<figcaption>{n}</figcaption></figure>')
    joined = "".join(figures)
    html = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Pattern stills: Phase B</title>
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background: #101114; color: #e8e6df; padding: 40px 32px 80px; }
main { max-width: 1360px; margin: 0 auto; }
h1 { font-size: 22px; font-weight: 650; }
.lede { color: #9a978e; font-size: 13px; margin-top: 8px; max-width: 78ch; line-height: 1.5; }
section { margin-top: 48px; }
h2 { font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.09em; color: #9a978e; margin-bottom: 6px; }
.note { font-size: 12px; color: #7c7a72; margin-bottom: 14px; }
.grid { display: grid; grid-template-columns: repeat(auto-fill, 224px); gap: 24px 16px; }
figure.cell svg { width: 224px; height: 224px; display: block; }
figure.cell figcaption { font-size: 12px; margin-top: 7px; }
section.paper { background: #f7f4ee; color: #26241f; padding: 28px; border-radius: 6px; }
section.paper h2 { color: #6c675a; }
section.editorial { background: #17181c; color: #e8e6df; padding: 28px; border-radius: 6px; border: 1px solid #26282f; }
.gray svg { filter: grayscale(1); }
.thumbrow { display: flex; flex-wrap: wrap; gap: 14px; }
figure.thumb svg { width: 48px; height: 48px; display: block; }
figure.thumb figcaption { font-size: 11px; color: #9a978e; margin-top: 5px; }
</style>
</head>
<body>
<main>
<header>
<h1>Pattern stills: Phase B</h1>
<p class="lede">49 knob variants of the Figma category squares. Frame 224. Cream on-state. Do not run generate.py against category files. Parent category art stays on the chip hero.</p>
</header>
<section>
<h2>1. Forty-nine up, 224px</h2>
<p class="note">Grouped in file order 1.1 through 10.4.</p>
<div class="grid">@F@</div>
</section>
<section class="paper">
<h2>2. Light paper</h2>
<div class="grid">@F@</div>
</section>
<section class="editorial">
<h2>3. Dark editorial</h2>
<div class="grid">@F@</div>
</section>
<section>
<h2>4. Grayscale</h2>
<p class="note">Siblings in one category must separate by silhouette.</p>
<div class="grid gray">@F@</div>
</section>
<section>
<h2>5. 48px thumbs</h2>
<div class="thumbrow">@T@</div>
</section>
</main>
</body>
</html>
"""
    PROBE.write_text(html.replace("@F@", joined).replace("@T@", "".join(thumbs)), encoding="utf-8")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    stills = all_stills()
    expected = set(NAMES)
    got = set(stills)
    if expected != got:
        raise SystemExit(f"key mismatch missing={expected-got} extra={got-expected}")
    for n, svg in stills.items():
        (OUT / f"{n}.svg").write_text(svg, encoding="utf-8")
    write_strip(stills)
    pat = {n: minify(svg) for n, svg in stills.items()}
    (OUT / "_pat.json").write_text(json.dumps(pat, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {len(stills)} svgs")


if __name__ == "__main__":
    main()

