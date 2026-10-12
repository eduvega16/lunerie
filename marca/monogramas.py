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
    fondo, tinta = {"V": (VERDE, BLANCO), "N": (NIEBLA, TINTA), "T": (TINTA, NIEBLA), "B": (BLANCO, TINTA)}[clave[-1]]
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


# ---------- tercera ronda (12-oct): L gruesa, inclinada y con la base ancha (inspirada en el estilo de LV, ----------
# ---------- sin copiar su monograma: nada de letras entrelazadas) ----------
@functools.lru_cache(None)
def fuente_ejes(nombre, ejes):
    buf = io.BytesIO()
    instancer.instantiateVariableFont(TTFont(DIR / "fuentes" / nombre), dict(ejes)).save(buf)
    return buf.getvalue()


def letra_forma(img, ch, nombre, ejes, cx, cy, alto, color, inclinar=0.0, ancho=1.0):
    """Letra con inclinación (`inclinar` = desplazamiento horizontal por unidad de alto) y estirada en horizontal
    (`ancho`), centrada en (cx, cy) con `alto` px. Devuelve la caja de tinta."""
    f = ImageFont.truetype(io.BytesIO(fuente_ejes(nombre, tuple(sorted(ejes.items())))), 1600)
    b = f.getbbox(ch, anchor="ls")
    w, h = b[2] - b[0] + 40, b[3] - b[1] + 40
    m = Image.new("L", (w, h), 0)
    ImageDraw.Draw(m).text((20 - b[0], 20 - b[1]), ch, font=f, fill=255, anchor="ls")
    W = int(w * ancho + inclinar * h) + 2
    m = m.transform((W, h), Image.AFFINE, (1 / ancho, inclinar / ancho, -inclinar * h / ancho, 0, 1, 0), Image.BICUBIC)
    m = m.crop(m.getbbox())
    m = m.resize((int(m.width * alto / m.height), int(alto)), RES)
    x, y = int(cx - m.width / 2), int(cy - m.height / 2)
    img.paste(Image.new("RGB", m.size, color), (x, y), m)
    return (x, y, x + m.width, y + m.height)


R3 = {  # clave: (título, fuente, ejes, inclinar, ancho, fondo)
    "corm-cursiva": ("Cormorant cursiva negrita", "Cormorant-Italic.ttf", {"wght": 700}, 0, 1.15, "V"),
    "corm-inclinada": ("Cormorant inclinada ancha", "Cormorant.ttf", {"wght": 700}, 0.2, 1.3, "V"),
    "bodoni-cursiva": ("Bodoni cursiva", "BodoniModa-Italic.ttf", {"wght": 900, "opsz": 96}, 0, 1.0, "V"),
    "bodoni-inclinada": ("Bodoni inclinada ancha", "BodoniModa.ttf", {"wght": 900, "opsz": 96}, 0.22, 1.25, "V"),
    "playfair": ("Playfair cursiva", "PlayfairDisplay-Italic.ttf", {"wght": 900}, 0, 1.1, "V"),
    "bodoni-inclinada-clara": ("Bodoni inclinada ancha (claro)", "BodoniModa.ttf", {"wght": 900, "opsz": 96}, 0.22,
                               1.25, "N"),
    "bodoni-inclinada-oscura": ("Bodoni inclinada ancha (oscuro)", "BodoniModa.ttf", {"wght": 900, "opsz": 96}, 0.22,
                                1.25, "T"),
    "corm-inclinada-sin": ("Cormorant inclinada, sin estrella", "Cormorant.ttf", {"wght": 700}, 0.2, 1.3, "V"),
}


def ronda3(clave, L):
    _, nombre, ejes, inc, anc, fnd = R3[clave]
    fondo, tinta = {"V": (VERDE, BLANCO), "N": (NIEBLA, TINTA), "T": (TINTA, NIEBLA)}[fnd]
    img = Image.new("RGB", (L, L), fondo)
    x0, y0, x1, y1 = letra_forma(img, "L", nombre, ejes, L / 2 - L * 0.03, L / 2 + L * 0.01, L * 0.42, tinta, inc, anc)
    if not clave.endswith("-sin"):
        destello(img, x1 - L * 0.02, y0 + L * 0.06, L * 0.07, ORO)
    return img


for clave in R3:
    ronda3(clave, 1080 * S).resize((1080, 1080), RES).save(OUT / f"{clave}-avatar.png")
hoja = Image.new("RGB", (2400, 1780), BLANCO)
d = ImageDraw.Draw(hoja)
for i, clave in enumerate(R3):
    col, fila = i % 4, i // 4
    x, y = 90 + col * 570, 60 + fila * 860
    av = Image.open(OUT / f"{clave}-avatar.png")
    hoja.paste(av.resize((480, 480), RES), (x, y), mask)
    d.text((x + 240, y + 520), R3[clave][0], font=rot, fill=TINTA, anchor="mm")
    hoja.paste(av.resize((32, 32), RES), (x + 120, y + 590))
    hoja.paste(av.resize((128, 128), RES), (x + 190, y + 590))
hoja.save(OUT / "hoja-l-gruesa.png")


# ---------- cuarta ronda (12-oct): L dibujada a medida (no es una tipografía) ----------
# Palo y base visibles, remate en cuña al final de la base, remate fino arriba, todo inclinado.
def l_propia(img, cx, cy, alto, color, inclinacion=20, palo=0.13, base=0.095, largo=0.62, cuna=0.17):
    """Unidades: alto de la L = 1. inclinacion en grados; palo/base = grosores; largo = base desde el palo."""
    import math
    s = math.tan(math.radians(inclinacion))
    t, f, F = palo, base, palo + largo
    piezas = [
        [(0, 0), (t, 0), (t, 1), (0, 1)],                       # palo
        [(-0.05, 0), (F, 0), (F, f), (-0.05, f)],              # base (sale un poco a la izquierda)
        [(-0.075, 1 - 0.03), (t + 0.05, 1 - 0.03), (t + 0.05, 1), (-0.075, 1)],  # remate de arriba, fino
    ]
    # cuña al final de la base: curva cóncava de (F - ancho, f) a (F, f + cuna)
    an = cuna * 0.85
    curva = [((1 - u) ** 2 * (F - an) + 2 * (1 - u) * u * (F - 0.01) + u ** 2 * F,
              (1 - u) ** 2 * f + 2 * (1 - u) * u * (f + 0.01) + u ** 2 * (f + cuna)) for u in [i / 30 for i in range(31)]]
    piezas.append([(F - an, f - 0.001)] + curva + [(F, f - 0.001)])
    # a coordenadas de imagen: inclinar (x + s·y), escalar y centrar la caja
    pts = [[(x + s * y, y) for x, y in p] for p in piezas]
    xs = [x for p in pts for x, _ in p]
    x0, x1 = min(xs), max(xs)
    k = alto
    ox, oy = cx - (x0 + x1) / 2 * k, cy + 0.5 * k
    d = ImageDraw.Draw(img)
    for p in pts:
        d.polygon([(ox + x * k, oy - y * k) for x, y in p], fill=color)
    return (ox + x0 * k, oy - k, ox + x1 * k, oy)


R4 = {  # clave: (título, fondo, color L, estrella, parámetros)
    "propia-equilibrada": ("Equilibrada", "V", BLANCO, False, {}),
    "propia-fina": ("Fina y más inclinada", "V", BLANCO, False, {"inclinacion": 24, "palo": 0.105, "base": 0.08}),
    "propia-remate": ("Con más remate", "V", BLANCO, False, {"palo": 0.14, "base": 0.105, "cuna": 0.22}),
    "propia-fina-estrella": ("Fina + destello", "V", BLANCO, True, {"inclinacion": 24, "palo": 0.105, "base": 0.08}),
    "propia-fina-oro": ("Fina, oro sobre tinta", "T", ORO, False, {"inclinacion": 24, "palo": 0.105, "base": 0.08}),
    "propia-fina-clara": ("Fina, sobre claro", "N", TINTA, False, {"inclinacion": 24, "palo": 0.105, "base": 0.08}),
    "propia-muy-inclinada": ("Muy inclinada", "V", BLANCO, False, {"inclinacion": 28, "palo": 0.1, "base": 0.075,
                                                                    "largo": 0.66}),
    "propia-equilibrada-estrella": ("Equilibrada + destello", "V", BLANCO, True, {}),
}


def ronda4(clave, L):
    _, fnd, color, estrella, p = R4[clave]
    fondo = {"V": VERDE, "N": NIEBLA, "T": TINTA}[fnd]
    img = Image.new("RGB", (L, L), fondo)
    x0, y0, x1, y1 = l_propia(img, L / 2 - (L * 0.03 if estrella else 0), L / 2, L * 0.44, color, **p)
    if estrella:
        destello(img, x1 + L * 0.02, y0 + L * 0.07, L * 0.065, ORO)
    return img


for clave in R4:
    ronda4(clave, 1080 * S).resize((1080, 1080), RES).save(OUT / f"{clave}-avatar.png")
hoja = Image.new("RGB", (2400, 1780), BLANCO)
d = ImageDraw.Draw(hoja)
for i, clave in enumerate(R4):
    col, fila = i % 4, i // 4
    x, y = 90 + col * 570, 60 + fila * 860
    av = Image.open(OUT / f"{clave}-avatar.png")
    hoja.paste(av.resize((480, 480), RES), (x, y), mask)
    d.text((x + 240, y + 520), R4[clave][0], font=rot, fill=TINTA, anchor="mm")
    hoja.paste(av.resize((32, 32), RES), (x + 120, y + 590))
    hoja.paste(av.resize((128, 128), RES), (x + 190, y + 590))
hoja.save(OUT / "hoja-l-propia.png")
print("ok →", OUT)


# ---------- elegida (13-oct): «Cursiva» con destello. Verde o blanco, vistos donde se usan ----------
for clave in ("cursivaV", "cursivaB"):
    ronda2(clave, 1080 * S).resize((1080, 1080), RES).save(OUT / f"{clave}-avatar.png")


def perfil_instagram(av, oscuro):
    """Cabecera de perfil de Instagram simplificada (foto en círculo + nombre + cifras)."""
    fondo, texto, gris = ((0, 0, 0), (245, 245, 245), (150, 150, 150)) if oscuro else (BLANCO, (20, 20, 20), (115, 115, 115))
    W, H = 1080, 520
    img = Image.new("RGB", (W, H), fondo)
    d = ImageDraw.Draw(img)
    sans = ImageFont.truetype("arial.ttf", 34)
    sans_b = ImageFont.truetype("arialbd.ttf", 38)
    m = Image.new("L", (300, 300), 0); ImageDraw.Draw(m).ellipse([0, 0, 299, 299], fill=255)
    img.paste(av.resize((300, 300), RES), (60, 110), m)
    d.text((60, 40), "lunerie", font=sans_b, fill=texto)
    for i, (n, t) in enumerate([("12", "publicaciones"), ("1.204", "seguidores"), ("85", "seguidos")]):
        d.text((470 + i * 200, 210), n, font=sans_b, fill=texto, anchor="mm")
        d.text((470 + i * 200, 260), t, font=ImageFont.truetype("arial.ttf", 26), fill=gris, anchor="mm")
    d.text((60, 440), "Joyas y relojes para regalar · Envío gratis a península", font=sans, fill=texto)
    return img


def pestana(av, oscuro):
    """Pestaña del navegador con el favicon a tamaño real (32 px dibujado a 16 px de pestaña ×2)."""
    barra, tab, texto = ((32, 33, 36), (53, 54, 58), (232, 234, 237)) if oscuro else ((222, 225, 230), BLANCO, (32, 33, 36))
    img = Image.new("RGB", (1080, 120), barra)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([20, 24, 520, 140], radius=18, fill=tab)
    img.paste(av.resize((32, 32), RES), (50, 56))
    d.text((100, 72), "Lunerie · Joyas y relojes", font=ImageFont.truetype("arial.ttf", 26), fill=texto, anchor="lm")
    return img


hoja = Image.new("RGB", (2400, 1600), (236, 236, 236))
d = ImageDraw.Draw(hoja)
for col, clave in enumerate(("cursivaV", "cursivaB")):
    av = Image.open(OUT / f"{clave}-avatar.png")
    x = 80 + col * 1180
    d.text((x, 40), "Fondo verde" if col == 0 else "Fondo blanco", font=rot, fill=TINTA)
    hoja.paste(perfil_instagram(av, False), (x, 100))
    hoja.paste(perfil_instagram(av, True), (x, 640))
    hoja.paste(pestana(av, False), (x, 1190))
    hoja.paste(pestana(av, True), (x, 1330))
hoja.save(OUT / "hoja-cursiva-verde-o-blanco.png")
print("ok →", OUT)
