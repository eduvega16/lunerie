"""Genera los logos de Lunerie en marca/logos/ (SVG + PNG) y una hoja para compararlos (marca/logos/hoja.png).

Logo: LUNERIE en Cormorant (fuentes/Cormorant.ttf, licencia OFL), mayúsculas muy espaciadas, como en la tienda.
Monograma «L» para avatar de redes y favicon. Colores de la página de marca (CLAUDE.md, apartado 3).
    python marca/logos.py
"""
import functools, io, pathlib
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
from PIL import Image, ImageDraw, ImageFont

DIR = pathlib.Path(__file__).parent
OUT = DIR / "logos"
OUT.mkdir(exist_ok=True)
TINTA, VERDE, ORO, NIEBLA, BLANCO = "#16201B", "#006039", "#A6834A", "#F2F4F2", "#FFFFFF"
TRACKING = 0.42  # espacio entre letras, en «em» (en la tienda 0.38-0.42)


@functools.lru_cache(None)
def fuente(peso):
    f = TTFont(DIR / "fuentes" / "Cormorant.ttf")
    return instancer.instantiateVariableFont(f, {"wght": peso})


@functools.lru_cache(None)
def fuente_bytes(peso):
    buf = io.BytesIO(); fuente(peso).save(buf)
    return buf.getvalue()


def svg_texto(texto, color, peso=500, tracking=TRACKING):
    """SVG con las letras convertidas a trazos (no depende de tener la fuente instalada)."""
    f = fuente(peso)
    gs, cmap, upm = f.getGlyphSet(), f.getBestCmap(), f["head"].unitsPerEm
    trazos, x, xmin, xmax, ymin, ymax = [], 0, None, 0, 0, 0
    for i, ch in enumerate(texto):
        g = gs[cmap[ord(ch)]]
        pen, bp = SVGPathPen(gs), BoundsPen(gs)
        g.draw(pen); g.draw(bp)
        if bp.bounds:
            b = bp.bounds
            xmin = x + b[0] if xmin is None else xmin
            xmax, ymin, ymax = x + b[2], min(ymin, b[1]), max(ymax, b[3])
        trazos.append(f'<path transform="translate({x} 0)" d="{pen.getCommands()}"/>')
        x += g.width + (tracking * upm if i < len(texto) - 1 else 0)
    m = upm * 0.06
    vb = (xmin - m, -ymax - m, xmax - xmin + 2 * m, ymax - ymin + 2 * m)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{" ".join(f"{v:.0f}" for v in vb)}">'
            f'<g fill="{color}" transform="scale(1 -1)">{"".join(trazos)}</g></svg>')


@functools.lru_cache(None)
def pil_fuente(peso, tam):
    return ImageFont.truetype(io.BytesIO(fuente_bytes(peso)), tam)


def dibujar_texto(d, texto, centro, tam, color, peso=500, tracking=TRACKING):
    """Texto espaciado centrado en `centro` (PIL no tiene letter-spacing: se coloca letra a letra)."""
    f = pil_fuente(peso, tam)
    anchos = [f.getlength(c) for c in texto]
    total = sum(anchos) + tracking * tam * (len(texto) - 1)
    x = centro[0] - total / 2
    for c, a in zip(texto, anchos):
        d.text((x, centro[1]), c, font=f, fill=color, anchor="lm")
        x += a + tracking * tam


def logo_png(color, fondo=None, ancho=2400, peso=500):
    S = 2  # se dibuja al doble y se reduce: bordes finos
    alto = int(ancho * 0.22)
    img = Image.new("RGBA", (ancho * S, alto * S), fondo or (0, 0, 0, 0))
    dibujar_texto(ImageDraw.Draw(img), "LUNERIE", (ancho * S / 2, alto * S / 2), int(ancho * S * 0.105), color, peso)
    return img.resize((ancho, alto), Image.LANCZOS)


def luna(d, cx, cy, r, color, fondo):
    """Luna creciente: un círculo tapado por otro desplazado del color del fondo."""
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)
    o = r * 0.42
    d.ellipse([cx - r + o, cy - r - o * 0.35, cx + r + o, cy + r - o * 0.35], fill=fondo)


def avatar(opcion, lado=1080, peso=500):
    S = 2
    L = lado * S
    fondo, tinta = {"A": (NIEBLA, TINTA), "B": (VERDE, BLANCO), "C": (NIEBLA, TINTA), "D": (NIEBLA, TINTA)}[opcion]
    img = Image.new("RGB", (L, L), fondo)
    d = ImageDraw.Draw(img)
    if opcion == "D":
        dibujar_texto(d, "LUNERIE", (L / 2, L / 2), int(L * 0.085), tinta, peso)
    else:
        f = pil_fuente(peso, int(L * 0.56))
        dx = -L * 0.03 if opcion == "C" else 0
        d.text((L / 2 + dx, L / 2 + L * 0.02), "L", font=f, fill=tinta, anchor="mm")
        if opcion == "C":
            luna(d, L * 0.64, L * 0.33, L * 0.075, ORO, fondo)
    return img.resize((lado, lado), Image.LANCZOS)


# ---------- logo (SVG para la web/imprenta, PNG transparente para todo lo demás) ----------
for nombre, color in {"tinta": TINTA, "blanco": BLANCO, "oro": ORO}.items():
    (OUT / f"logo-{nombre}.svg").write_text(svg_texto("LUNERIE", color), encoding="utf8")
    logo_png(color).save(OUT / f"logo-{nombre}.png")

# ---------- avatares de redes (1080×1080; Instagram los recorta en círculo) y favicons ----------
for op in "ABCD":
    avatar(op).save(OUT / f"avatar-{op}.png")
    # favicon: más grueso (a 32 px los trazos finos de Cormorant desaparecen)
    avatar(op, 512, peso=700).save(OUT / f"favicon-{op}.png")

# ---------- hoja para comparar ----------
W = 2400
hoja = Image.new("RGB", (W, 2350), BLANCO)
d = ImageDraw.Draw(hoja)
rot = pil_fuente(500, 34)
d.text((80, 60), "Logo", font=rot, fill=TINTA)
hoja.paste(logo_png(TINTA, ancho=1000), (80, 120), logo_png(TINTA, ancho=1000))
verde = Image.new("RGB", (1100, 260), VERDE)
verde.paste(logo_png(BLANCO, ancho=1000), (50, 20), logo_png(BLANCO, ancho=1000))
hoja.paste(verde, (1220, 100))
oro = logo_png(ORO, ancho=1000)
hoja.paste(oro, (80, 380), oro)
d.text((80, 700), "Avatar redes (A · B · C · D) — Instagram lo recorta en círculo", font=rot, fill=TINTA)
mask = Image.new("L", (520, 520), 0); ImageDraw.Draw(mask).ellipse([0, 0, 519, 519], fill=255)
for i, op in enumerate("ABCD"):
    a = avatar(op).resize((520, 520), Image.LANCZOS)
    hoja.paste(a, (80 + i * 580, 770), mask)
    d.text((80 + i * 580 + 250, 1320), op, font=rot, fill=TINTA)
d.text((80, 1420), "Favicon a tamaño real de pestaña (32 px) y ampliado (128 px)", font=rot, fill=TINTA)
for i, op in enumerate("ABCD"):
    fav = Image.open(OUT / f"favicon-{op}.png")
    hoja.paste(fav.resize((32, 32), Image.LANCZOS), (80 + i * 580, 1500))
    hoja.paste(fav.resize((128, 128), Image.LANCZOS), (140 + i * 580, 1500))
    d.text((80 + i * 580 + 300, 1550), op, font=rot, fill=TINTA)
# cómo queda en la cabecera de la tienda (logo pequeño, ~120 px de ancho a tamaño real ×2)
d.text((80, 1720), "En la cabecera de la tienda", font=rot, fill=TINTA)
cab = Image.new("RGB", (2240, 420), BLANCO)
dc = ImageDraw.Draw(cab)
dc.rectangle([0, 0, 2240, 60], fill=VERDE)
dibujar_texto(dc, "ENVÍO GRATIS A PENÍNSULA · DEVOLUCIÓN EN 14 DÍAS", (1120, 30), 22, BLANCO, 500, 0.14)
lp = logo_png(TINTA, ancho=420)
cab.paste(lp, (910, 150), lp)
dc.line([0, 419, 2240, 419], fill="#E2E6E3", width=2)
hoja.paste(cab, (80, 1790))
hoja.save(OUT / "hoja.png")
print("ok →", OUT)
