"""Gera assets/banner-{pt,en}-{light,dark}.svg.

Conceito: uma planta de loteamento desenhada como planta técnica. Ao abrir,
alguns lotes são "registrados" um a um: o único movimento da página.
O texto vira contorno (path), então o banner fica igual em qualquer tela.

Para regenerar (ex.: mudar o texto em COPY):
    pip install fonttools brotli uharfbuzz
    npm pack @fontsource-variable/archivo simple-icons   # e extraia os .tgz
    python scripts/assets/build_banner.py <archivo-latin-wdth-normal.woff2> assets
    python scripts/assets/build_stack.py <archivo-latin-wdth-normal.woff2> <simple-icons/icons> assets
"""
import math
import random
import sys
from textpath import text_path, measure

FONT = sys.argv[1]
OUT = sys.argv[2]

W, H = 1200, 340

THEMES = {
    "light": dict(bg="#F4F7FB", grid="#DCE4F0", line="#9DB0CC", street="#C9D5E6",
                  ink="#14294D", sub="#4D6182", lot_on="#2E5AD6", lot_on2="#7D9AE8",
                  label="#7C8FAE", stroke_on="#1F46B8"),
    "dark": dict(bg="#0D1D36", grid="#15294A", line="#3A5684", street="#1B3157",
                 ink="#EEF3FB", sub="#A9BCDB", lot_on="#6F95FF", lot_on2="#3A5CB8",
                 label="#6D86AE", stroke_on="#9DB7FF"),
}

COPY = {
    "pt": ("Lucas Matias", "Estudante de Engenharia de Software no IFG", "e escrevente de cartório em Goiás"),
    "en": ("Lucas Matias", "Software Engineering student at IFG", "and notary clerk in Goiás, Brazil"),
}


def clip_poly(poly, a, b, c):
    """Mantém a parte do polígono com a*x + b*y <= c (Sutherland–Hodgman)."""
    out = []
    n = len(poly)
    for i in range(n):
        p, q = poly[i], poly[(i + 1) % n]
        fp = a * p[0] + b * p[1] - c
        fq = a * q[0] + b * q[1] - c
        if fp <= 0:
            out.append(p)
        if (fp <= 0) != (fq <= 0):
            t = fp / (fp - fq)
            out.append((p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1])))
    return out


def area(poly):
    return abs(sum(poly[i][0] * poly[(i + 1) % len(poly)][1] - poly[(i + 1) % len(poly)][0] * poly[i][1]
                   for i in range(len(poly)))) / 2


def fmt(poly):
    return "M" + "L".join(f"{x:.1f} {y:.1f}" for x, y in poly) + "Z"


def plan():
    """Quadras em grade, cortadas por uma avenida diagonal. Coordenadas do plano."""
    lots, blocks = [], []
    qw, qh = 300, 112          # quadra
    sw = 30                    # rua
    cols, rows = 3, 5
    x0, y0 = 520, -230
    # avenida diagonal: faixa entre duas retas paralelas (a*x + b*y = c)
    ax, ay = 1.0, 0.45
    c1, c2 = 1112, 1146
    qd = 1
    for r in range(rows):
        for cidx in range(cols):
            bx, by = x0 + cidx * (qw + sw), y0 + r * (qh + sw)
            rect = [(bx, by), (bx + qw, by), (bx + qw, by + qh), (bx, by + qh)]
            for side in (0, 1):
                part = clip_poly(rect, ax, ay, c1) if side == 0 else clip_poly(rect, -ax, -ay, -c2)
                if len(part) < 3 or area(part) < 400:
                    continue
                blocks.append((qd, part))
                n = 10
                lw = qw / n
                for row in range(2):
                    for k in range(n):
                        lx, ly = bx + k * lw, by + row * qh / 2
                        lr = [(lx, ly), (lx + lw, ly), (lx + lw, ly + qh / 2), (lx, ly + qh / 2)]
                        lp = clip_poly(lr, ax, ay, c1) if side == 0 else clip_poly(lr, -ax, -ay, -c2)
                        if len(lp) >= 3 and area(lp) > 180:
                            lots.append((qd, lp))
                qd += 1
    return lots, blocks, (ax, ay, c1, c2)


def build(theme, lang):
    t = THEMES[theme]
    name, l1, l2 = COPY[lang]
    lots, blocks, (ax, ay, c1, c2) = plan()

    rot, cx, cy = -14, 960, 170
    rnd = random.Random(7)

    def visible(poly):
        # centro do lote depois da rotação, dentro do painel e longe do texto
        mx = sum(p[0] for p in poly) / len(poly)
        my = sum(p[1] for p in poly) / len(poly)
        a = math.radians(rot)
        x = cx + (mx - cx) * math.cos(a) - (my - cy) * math.sin(a)
        y = cy + (mx - cx) * math.sin(a) + (my - cy) * math.cos(a)
        return 790 < x < 1170 and 30 < y < 312 and not (x > 1100 and y < 100)

    cand = [i for i, (_, p) in enumerate(lots) if visible(p) and area(p) > 1300]
    on = sorted(rnd.sample(cand, 9), key=lambda i: (sum(p[0] for p in lots[i][1]) / len(lots[i][1])))

    g = []
    # papel milimetrado
    for x in range(0, W + 1, 24):
        g.append(f'<path d="M{x} 0V{H}" />')
    for y in range(0, H + 1, 24):
        g.append(f'<path d="M0 {y}H{W}" />')
    grid = f'<g stroke="{t["grid"]}" stroke-width="1" opacity=".55">{"".join(g)}</g>'

    # avenida: faixa entre c1 e c2 (desenha como polígono grande)
    big = [(-400, -600), (2000, -600), (2000, 1200), (-400, 1200)]
    avenue = clip_poly(clip_poly(big, -ax, -ay, -c1), ax, ay, c2)

    lot_paths = []
    for i, (_, poly) in enumerate(lots):
        lot_paths.append(f'<path d="{fmt(poly)}"/>')
    on_paths = []
    for k, i in enumerate(on):
        delay = 0.35 + k * 0.16
        fill = t["lot_on"] if k % 3 else "url(#hatch)"
        on_paths.append(f'<path class="r" style="animation-delay:{delay:.2f}s" d="{fmt(lots[i][1])}" fill="{fill}"/>')

    labels = []
    for qd, poly in blocks:
        xs = [p[0] for p in poly]
        ys = [p[1] for p in poly]
        mx, my = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
        if not visible(poly) or area(poly) < 20000:
            continue
        d, lw_ = text_path(f"QD {qd:02d}", mx, my + 4.6, 13, 650, 112, 0.05, "middle", FONT)
        labels.append(f'<rect x="{mx - lw_ / 2 - 7:.1f}" y="{my - 10:.1f}" width="{lw_ + 14:.1f}" height="20" rx="10" fill="{t["bg"]}" stroke="{t["line"]}" stroke-width="1"/><path d="{d}" fill="{t["label"]}"/>')

    plan_svg = f'''<g transform="rotate({rot} {cx} {cy})">
    <path d="{fmt(avenue)}" fill="{t["street"]}" opacity=".7"/>
    <g fill="{t["bg"]}" stroke="{t["line"]}" stroke-width="1.15" stroke-linejoin="round">{"".join(lot_paths)}</g>
    <g stroke="{t["stroke_on"]}" stroke-width="1.15" stroke-linejoin="round">{"".join(on_paths)}</g>
    <path d="M{(c1 + c2) / 2 - ay * -400:.1f} -400L{(c1 + c2) / 2 - ay * 800:.1f} 800" stroke="{t["line"]}" stroke-width="1" stroke-dasharray="10 8" opacity=".8"/>
    <g>{"".join(labels)}</g>
  </g>'''

    # rosa dos ventos mínima (norte) no canto
    nx, ny = 1148, 52
    north = text_path("N", nx, ny - 20, 13, 700, 100, 0, "middle", FONT)[0]
    compass = f'''<g transform="rotate({rot} {nx} {ny})">
    <circle cx="{nx}" cy="{ny}" r="15" fill="{t["bg"]}" stroke="{t["line"]}" stroke-width="1.2"/>
    <path d="M{nx} {ny - 11}L{nx + 5} {ny + 8}L{nx} {ny + 4}L{nx - 5} {ny + 8}Z" fill="{t["ink"]}"/>
    <path d="{north}" fill="{t["ink"]}"/>
  </g>'''

    # texto (contornado)
    size_name = 70
    nm, nw = text_path(name, 64, 168, size_name, 800, 125, -0.01, "start", FONT)
    s1, _ = text_path(l1, 66, 224, 27, 560, 100, 0, "start", FONT)
    s2, _ = text_path(l2, 66, 260, 27, 430, 100, 0, "start", FONT)

    alt = f"{name}: {l1} {l2}"
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{alt}">
  <title>{alt}</title>
  <style>
    .r{{opacity:0;animation:reg .55s cubic-bezier(.2,.7,.2,1) forwards}}
    @keyframes reg{{0%{{opacity:0}}60%{{opacity:1}}100%{{opacity:1}}}}
    @media (prefers-reduced-motion:reduce){{.r{{animation:none;opacity:1}}}}
  </style>
  <defs>
    <clipPath id="panel"><rect width="{W}" height="{H}" rx="18"/></clipPath>
    <linearGradient id="fade" x1="0" x2="1" y1="0" y2="0">
      <stop offset="0" stop-color="#fff" stop-opacity="0"/>
      <stop offset=".5" stop-color="#fff" stop-opacity="0"/>
      <stop offset=".66" stop-color="#fff" stop-opacity="1"/>
    </linearGradient>
    <pattern id="hatch" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
      <rect width="7" height="7" fill="{t["bg"]}"/><path d="M0 0V7" stroke="{t["lot_on"]}" stroke-width="2.2"/>
    </pattern>
    <mask id="m"><rect width="{W}" height="{H}" fill="url(#fade)"/></mask>
  </defs>
  <g clip-path="url(#panel)">
    <rect width="{W}" height="{H}" fill="{t["bg"]}"/>
    {grid}
    <g mask="url(#m)">
  {plan_svg}
    </g>
  </g>
  {compass}
  <path d="{nm}" fill="{t["ink"]}"/>
  <path d="{s1}" fill="{t["ink"]}"/>
  <path d="{s2}" fill="{t["sub"]}"/>
</svg>
'''
    with open(f"{OUT}/banner-{lang}-{theme}.svg", "w") as f:
        f.write(svg)
    return nw


for lang in ("pt", "en"):
    for theme in ("light", "dark"):
        w = build(theme, lang)
print("name width", round(w))
