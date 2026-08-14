#!/usr/bin/env python3
"""Bake aup-mesh-v1 category motifs (dev-only). Embed via rebuild or copy from motifs.json."""
import hashlib, json, math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FAMILY = "aup-mesh-v1"

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

def motif_svg(hex_color: str, seed: int, w=320, h=180) -> str:
    rnd = mulberry32(seed)
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" fill="none" aria-hidden="true">']
    parts.append(f'<rect width="{w}" height="{h}" fill="{hex_color}" opacity="0.08"/>')
    for _ in range(5):
        cx, cy, r = rnd() * w, rnd() * h * 0.85, 28 + rnd() * 90
        sw, op = 0.8 + rnd() * 1.6, 0.18 + rnd() * 0.35
        dash = "" if rnd() > 0.45 else f' stroke-dasharray="{4 + rnd() * 10:.1f} {3 + rnd() * 8:.1f}"'
        parts.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" stroke="{hex_color}" stroke-width="{sw:.2f}" opacity="{op:.2f}"{dash}/>')
    pts, x0, y0 = [], -20, h * (0.25 + rnd() * 0.5)
    for _ in range(8):
        x0 += w / 7
        y0 += (rnd() - 0.5) * 48
        pts.append(f"{x0:.1f},{max(8, min(h - 8, y0)):.1f}")
    parts.append(f'<polyline points="{" ".join(pts)}" stroke="{hex_color}" stroke-width="1.2" opacity="0.45" stroke-linecap="round" stroke-linejoin="round"/>')
    for _ in range(14):
        x, y, r, op = rnd() * w, rnd() * h, 0.8 + rnd() * 2.4, 0.25 + rnd() * 0.5
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.2f}" fill="{hex_color}" opacity="{op:.2f}"/>')
    for _ in range(4):
        x1, y1, ang, ln = rnd() * w, rnd() * h, rnd() * math.tau, 20 + rnd() * 50
        x2, y2 = x1 + math.cos(ang) * ln, y1 + math.sin(ang) * ln
        parts.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{hex_color}" stroke-width="1" opacity="0.3" stroke-linecap="round"/>')
    parts.append("</svg>")
    return "".join(parts)

def main():
    cats = json.loads((ROOT / "data/en.json").read_text())["cats"]
    seeds, svg = {}, {}
    hex_l = "#7d7b75"
    seeds["landing"] = hash32(f"{FAMILY}|landing|{hex_l}")
    svg["landing"] = motif_svg(hex_l, seeds["landing"], 800, 280)
    for k, v in cats.items():
        seeds[k] = hash32(f"{FAMILY}|{k}|{v['hex']}")
        svg[k] = motif_svg(v["hex"], seeds[k])
    out = {"family": FAMILY, "seeds": seeds, "svg": svg}
    (Path(__file__).parent / "motifs.json").write_text(json.dumps(out, ensure_ascii=False))
    print(json.dumps(seeds, indent=2))

if __name__ == "__main__":
    main()
