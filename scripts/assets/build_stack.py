"""Gera assets/stack-{light,dark}.svg: a stack como a legenda de uma planta."""
import re
import sys
from textpath import text_path

FONT, ICONS, OUT = sys.argv[1], sys.argv[2], sys.argv[3]

THEMES = {
    "light": dict(bg="#F4F7FB", line="#C9D5E6", ink="#14294D", sub="#5B6F90"),
    "dark": dict(bg="#0D1D36", line="#22406B", ink="#EEF3FB", sub="#A9BCDB"),
}

ITEMS = [
    ("nextdotjs", "Next.js"), ("react", "React"), ("typescript", "TypeScript"),
    ("javascript", "JavaScript"), ("html5", "HTML"), ("css", "CSS"),
    ("supabase", "Supabase"), ("postgresql", "PostgreSQL"), ("claude", "Claude API"),
    ("vercel", "Vercel"), ("git", "Git"), ("c", "C"),
]

COLS, ROWS = 6, 2
CW, CH = 200, 118
W, H = COLS * CW, ROWS * CH
ICON = 36


def icon_path(slug):
    svg = open(f"{ICONS}/{slug}.svg").read()
    return re.search(r'<path d="([^"]+)"', svg).group(1)


def build(theme):
    t = THEMES[theme]
    cells = []
    for i, (slug, label) in enumerate(ITEMS):
        c, r = i % COLS, i // COLS
        x, y = c * CW, r * CH
        s = ICON / 24
        ix, iy = x + (CW - ICON) / 2, y + 26
        cells.append(f'<path transform="translate({ix:.1f} {iy:.1f}) scale({s:.4f})" d="{icon_path(slug)}" fill="{t["ink"]}"/>')
        d, _ = text_path(label, x + CW / 2, y + 92, 17, 560, 100, 0.0, "middle", FONT)
        cells.append(f'<path d="{d}" fill="{t["sub"]}"/>')
    grid = []
    for c in range(1, COLS):
        grid.append(f'<path d="M{c * CW} 0V{H}"/>')
    for r in range(1, ROWS):
        grid.append(f'<path d="M0 {r * CH}H{W}"/>')
    alt = "Stack: " + ", ".join(lbl for _, lbl in ITEMS)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="-1 -1 {W + 2} {H + 2}" width="{W + 2}" height="{H + 2}" role="img" aria-label="{alt}">
  <title>{alt}</title>
  <rect width="{W}" height="{H}" rx="14" fill="{t["bg"]}" stroke="{t["line"]}" stroke-width="1.2"/>
  <g stroke="{t["line"]}" stroke-width="1.2">{"".join(grid)}</g>
  {"".join(cells)}
</svg>
'''
    with open(f"{OUT}/stack-{theme}.svg", "w") as f:
        f.write(svg)


for th in THEMES:
    build(th)
