"""Converte texto em caminhos SVG (Archivo variável, shaping com HarfBuzz)."""
import uharfbuzz as hb
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

_blob_cache = {}


def _font(path, wght, wdth):
    key = (path, wght, wdth)
    if key not in _blob_cache:
        from fontTools.ttLib import TTFont
        import io
        tt = TTFont(path)  # woff2 -> sfnt em memória
        tt.flavor = None
        buf = io.BytesIO()
        tt.save(buf)
        face = hb.Face(buf.getvalue())
        font = hb.Font(face)
        font.set_variations({"wght": wght, "wdth": wdth})
        _blob_cache[key] = (font, face.upem)
    return _blob_cache[key]


def measure(text, size, wght=400, wdth=100, tracking=0.0, font_path=None):
    return layout(text, size, wght, wdth, tracking, font_path)[1]


def layout(text, size, wght=400, wdth=100, tracking=0.0, font_path=None):
    font, upem = _font(font_path, wght, wdth)
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(font, buf, {"kern": True, "liga": True})
    scale = size / upem
    glyphs = []
    x = 0.0
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        glyphs.append((info.codepoint, x + pos.x_offset * scale, pos.y_offset * scale))
        x += pos.x_advance * scale + tracking * size
    width = x - (tracking * size if text else 0)
    return glyphs, width, scale, font


def text_path(text, x, y, size, wght=400, wdth=100, tracking=0.0, anchor="start", font_path=None):
    """Retorna (d, largura). y é a linha de base."""
    glyphs, width, scale, font = layout(text, size, wght, wdth, tracking, font_path)
    if anchor == "middle":
        x -= width / 2
    elif anchor == "end":
        x -= width
    parts = []
    for gid, gx, gy in glyphs:
        pen = SVGPathPen(None, ntos=lambda v: f"{v:.2f}".rstrip("0").rstrip("."))
        tpen = TransformPen(pen, (scale, 0, 0, -scale, x + gx, y - gy))
        font.draw_glyph_with_pen(gid, tpen)
        d = pen.getCommands()
        if d:
            parts.append(d)
    return "".join(parts), width
