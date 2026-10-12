"""Variantes del monograma «L + luna» (a partir de la opción C de logos.py). Salida: marca/logos/monogramas/.
    python marca/monogramas.py
"""
import functools, io, pathlib
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from PIL import Image, ImageChops, ImageDraw, ImageFont

DIR = pathlib.Path(__file__).parent
OUT = DIR / "logos" / "monogramas"
OUT.mkdir(parents=True, exist_ok=True)
TINTA, VERDE, ORO, NIEBLA, BLANCO = "#16201B", "#006039", "#A6834A", "#F2F4F2", "#FFFFFF"
RES = Image.Resampling.LANCZOS if hasattr(Image, "Resampling") else Image.LANCZOS


@functools.lru_cache(None)
def fuente(peso, cursiva=False, tam=100):
    nombre = "Cormorant-Italic.ttf" if cursiva else "Cormorant.ttf"
    buf = io.BytesIO()
    instancer.instantiateVariableFont(TTFont(DIR / "fuentes" / nombre), {"wght": peso}).save(buf)
    return buf.getvalue()


def letra(img, ch, cx, cy, alto, color, peso=500, cursiva=False):
    """Dibuja `ch` con la caja de tinta centrada en (cx, cy) y `alto` px de alto (centrado óptico, no por avance)."""
    f = ImageFont.truetype(io.BytesIO(fuente(peso, cursiva)), 100)
    b = f.getbbox(ch, anchor="ls")
    f = ImageFont.truetype(io.BytesIO(fuente(peso, cursiva)), int(100 * alto / (b[3] - b[1])))
    b = f.getbbox(ch, anchor="ls")
    x, y = cx - (b[0] + b[2]) / 2, cy - (b[1] + b[3]) / 2
    ImageDraw.Draw(img).text((x, y), ch, font=f, fill=color, anchor="ls")
    return (x + b[0], y + b[1], x + b[2], y + b[3])  # caja de tinta en la imagen


def luna(img, cx, cy, r, grosor, angulo, color):
    """Luna creciente: círculo menos el mismo círculo desplazado `grosor`·r hacia `angulo` (0 = abre a la derecha)."""
    import math
    m1 = Image.new("L", img.size, 0); ImageDraw.Draw(m1).ellipse([cx - r, cy - r, cx + r, cy + r], fill=255)
    dx, dy = math.cos(math.radians(angulo)) * grosor * r, -math.sin(math.radians(angulo)) * grosor * r
    m2 = Image.new("L", img.size, 0)
    ImageDraw.Draw(m2).ellipse([cx - r + dx, cy - r + dy, cx + r + dx, cy + r + dy], fill=255)
    img.paste(Image.new("RGB", img.size, color), (0, 0), ImageChops.subtract(m1, m2))


def destello(img, cx, cy, R, color, puntas=4, finura=3.0):
    """Estrella de destello: astroide (lados curvos hacia dentro). finura 3 = clásica; más alto = más fina.
    puntas=8 añade un segundo destello girado 45° y más corto (estrella polar)."""
    import math
    d = ImageDraw.Draw(img)
    def astroide(r, giro):
        pts = []
        for i in range(720):
            t = 2 * math.pi * i / 720
            x = math.copysign(abs(math.cos(t)) ** finura, math.cos(t)) * r
            y = math.copysign(abs(math.sin(t)) ** finura, math.sin(t)) * r
            g = math.radians(giro)
            pts.append((cx + x * math.cos(g) - y * math.sin(g), cy + x * math.sin(g) + y * math.cos(g)))
        d.polygon(pts, fill=color)
    astroide(R, 0)
    if puntas == 8:  # puntas cortas en diagonal (a 0,5·R quedarían tapadas por la estrella grande)
        astroide(R * 0.75, 45)


def anillo(img, cx, cy, r, ancho, color):
    ImageDraw.Draw(img).ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=int(ancho))


def opcion(n, L):
    """Dibuja la variante n en un lienzo L×L. Devuelve la imagen."""
    fondo = {7: TINTA}.get(n, NIEBLA)
    tinta = {7: NIEBLA}.get(n, TINTA)
    img = Image.new("RGB", (L, L), fondo)
    c = L / 2
    if n == 1:  # luna dorada apoyada en el pie de la L, abierta hacia arriba (una cuna)
        x0, y0, x1, y1 = letra(img, "L", c, c, L * 0.42, tinta)
        luna(img, x0 + (x1 - x0) * 0.62, y1 - L * 0.115, L * 0.06, 0.32, 90, ORO)
    elif n == 2:  # una luna fina y grande abraza la L
        luna(img, c, c, L * 0.34, 0.16, 0, ORO)
        letra(img, "L", c + L * 0.035, c, L * 0.36, tinta)
    elif n == 3:  # punto de luna llena: L·
        x0, y0, x1, y1 = letra(img, "L", c - L * 0.04, c, L * 0.42, tinta)
        r = L * 0.028
        ImageDraw.Draw(img).ellipse([x1 + L * 0.03, y1 - 2 * r, x1 + L * 0.03 + 2 * r, y1], fill=ORO)
    elif n == 4:  # L cursiva + luna fina arriba
        x0, y0, x1, y1 = letra(img, "L", c - L * 0.03, c + L * 0.01, L * 0.44, tinta, 500, True)
        luna(img, x1 - L * 0.02, y0 + L * 0.06, L * 0.065, 0.3, 200, ORO)
    elif n == 5:  # trazo fino (Cormorant Light), alta y con mucho aire
        x0, y0, x1, y1 = letra(img, "L", c - L * 0.02, c, L * 0.5, tinta, 300)
        luna(img, x1 - L * 0.01, y0 + L * 0.05, L * 0.05, 0.28, 200, ORO)
    elif n == 6:  # sello: anillo dorado fino con la L y una luna pequeña en lo alto
        anillo(img, c, c, L * 0.36, L * 0.006, ORO)
        letra(img, "L", c, c + L * 0.02, L * 0.3, tinta)
        luna(img, c, c - L * 0.25, L * 0.04, 0.3, 270, ORO)
    elif n == 7:  # la 2 en oscuro: fondo tinta, L clara, luna dorada
        luna(img, c, c, L * 0.34, 0.16, 0, ORO)
        letra(img, "L", c + L * 0.035, c, L * 0.36, tinta)
    return img


NOMBRES = {1: "Cuna", 2: "Abrazo", 3: "Punto", 4: "Cursiva", 5: "Fino", 6: "Sello", 7: "Abrazo oscuro"}
S = 3
for n in NOMBRES:
    opcion(n, 1080 * S).resize((1080, 1080), RES).save(OUT / f"C{n}-avatar.png")

# hoja: avatar en círculo (como Instagram) + favicon a 32 px y 128 px
hoja = Image.new("RGB", (2400, 1780), BLANCO)
d = ImageDraw.Draw(hoja)
rot = ImageFont.truetype(io.BytesIO(fuente(500)), 34)
mask = Image.new("L", (480, 480), 0); ImageDraw.Draw(mask).ellipse([0, 0, 479, 479], fill=255)
for i, n in enumerate(NOMBRES):
    col, fila = i % 4, i // 4
    x, y = 90 + col * 570, 60 + fila * 860
    av = Image.open(OUT / f"C{n}-avatar.png")
    hoja.paste(av.resize((480, 480), RES), (x, y), mask)
    d.text((x + 240, y + 520), f"C{n} · {NOMBRES[n]}", font=rot, fill=TINTA, anchor="mm")
    hoja.paste(av.resize((32, 32), RES), (x + 120, y + 590))
    hoja.paste(av.resize((128, 128), RES), (x + 190, y + 590))
hoja.save(OUT / "hoja-monogramas.png")


# ---------- segunda ronda (12-oct): C7 en verde y versiones con estrella (destello de 4 puntas) ----------
def ronda2(clave, L):
    fondo, tinta = {"V": (VERDE, BLANCO), "N": (NIEBLA, TINTA), "T": (TINTA, NIEBLA)}[clave[-1]]
    img = Image.new("RGB", (L, L), fondo)
    c = L / 2
    tipo = clave[:-1]
    if tipo == "abrazo":
        luna(img, c, c, L * 0.34, 0.16, 0, ORO)
        letra(img, "L", c + L * 0.035, c, L * 0.36, tinta)
    elif tipo == "destello":  # L + destello dorado arriba a la derecha
        x0, y0, x1, y1 = letra(img, "L", c - L * 0.03, c + L * 0.02, L * 0.42, tinta)
        destello(img, x1 - L * 0.01, y0 + L * 0.05, L * 0.075, ORO)
    elif tipo == "polar":  # destello de 8 puntas
        x0, y0, x1, y1 = letra(img, "L", c - L * 0.03, c + L * 0.02, L * 0.42, tinta)
        destello(img, x1 - L * 0.01, y0 + L * 0.06, L * 0.085, ORO, puntas=8)
    elif tipo == "cursiva":
        x0, y0, x1, y1 = letra(img, "L", c - L * 0.03, c + L * 0.02, L * 0.44, tinta, 500, True)
        destello(img, x1 + L * 0.01, y0 + L * 0.04, L * 0.07, ORO)
    elif tipo == "pie":  # el destello hace de punto final: L✦
        x0, y0, x1, y1 = letra(img, "L", c - L * 0.05, c, L * 0.42, tinta)
        destello(img, x1 + L * 0.065, y1 - L * 0.045, L * 0.05, ORO)
    elif tipo == "grande":  # destello grande y fino detrás, la L delante
        destello(img, c, c, L * 0.36, ORO, finura=4.2)
        letra(img, "L", c, c, L * 0.3, tinta)
    return img


R2 = {"abrazoV": "Abrazo verde", "destelloN": "Destello", "destelloV": "Destello verde",
      "destelloT": "Destello oscuro", "polarV": "Polar verde", "cursivaV": "Cursiva verde",
      "pieV": "Punto estrella verde", "grandeV": "Estrella grande verde"}
for clave in R2:
    ronda2(clave, 1080 * S).resize((1080, 1080), RES).save(OUT / f"{clave}-avatar.png")
hoja = Image.new("RGB", (2400, 1780), BLANCO)
d = ImageDraw.Draw(hoja)
for i, clave in enumerate(R2):
    col, fila = i % 4, i // 4
    x, y = 90 + col * 570, 60 + fila * 860
    av = Image.open(OUT / f"{clave}-avatar.png")
    hoja.paste(av.resize((480, 480), RES), (x, y), mask)
    d.text((x + 240, y + 520), R2[clave], font=rot, fill=TINTA, anchor="mm")
    hoja.paste(av.resize((32, 32), RES), (x + 120, y + 590))
    hoja.paste(av.resize((128, 128), RES), (x + 190, y + 590))
hoja.save(OUT / "hoja-estrellas.png")
print("ok →", OUT)
