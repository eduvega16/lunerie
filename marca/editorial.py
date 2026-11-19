"""Piezas de Instagram y anuncios con la estética de Olivia Jewelry (Edu, 19-nov: «a eso quiero que nos parezcamos,
lo máximo posible»). Sin IA: fotos ya revisadas + letra de Lunerie.

Lo que se copia de @oliviajewelryco (oficina/referencias/olivia-ig-2026-11-19/README.md):
- encuadres muy cerrados en la joya: cuello de la barbilla al pecho, sin brazo ni reloj de relleno;
- texto blanco, pequeño, directamente sobre la piel (sin franjas ni degradados), con una sombra casi invisible;
- anotaciones con flechas finas que señalan la pieza («tu nombre, en letra de firma» → el nombre);
- promos en un bloque de color de marca con textura, partido con una foto de cerca (borde limpio, sin fundidos);
- revelado de película solo en la piel y el fondo: la joya conserva su brillo y su color.

    python marca/editorial.py                 # todas, en 4:5 y 9:16
    python marca/editorial.py --sin-revelar   # sin el acabado de película (para comparar)
    python marca/editorial.py --color naranja # solo los bloques de color (promo, regalo, marca) en ese color, 4:5
"""
import math
import pathlib
import sys

import numpy as np
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

RAIZ = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "marca"))
from revelar import pelicula  # noqa: E402

F = RAIZ / "marca" / "fuentes"
FOTOS = RAIZ / "marca" / "fotos-ia"
SALIDA = FOTOS / "editorial-limpio"
TINTA, BLANCO = (22, 32, 27), (255, 255, 255)
VERDE, BURDEOS = (0, 96, 57), (74, 10, 16)
REVELAR = "--sin-revelar" not in sys.argv
# Prueba de color de marca para los bloques (Edu, 19-nov: «me gusta el naranja y el azul… podríamos probar»).
# El naranja es un punto más ámbar que el de Olivia (#C84011) para no ser idéntico; el azul es azul noche, por la luna.
NARANJA, AZUL, NARANJA_VIVO = (194, 83, 27), (27, 42, 78), (234, 114, 46)
# combinación → (fondo del bloque, texto, acento). Edu (19-nov): «es la combinación de ambos».
COMBOS = {"verde": (VERDE, BLANCO, BLANCO), "naranja": (NARANJA, BLANCO, BLANCO), "azul": (AZUL, BLANCO, BLANCO),
          "azul-naranja": (AZUL, BLANCO, NARANJA_VIVO), "naranja-azul": (NARANJA, AZUL, BLANCO)}
COLOR = sys.argv[sys.argv.index("--color") + 1] if "--color" in sys.argv else None
MARCA, TXT, ACC = COMBOS[COLOR] if COLOR else (VERDE, BLANCO, BLANCO)
CINTA = {"azul-naranja": NARANJA_VIVO, "naranja-azul": AZUL}.get(COLOR)  # la cinta del otro color entre bloque y foto


# ───────────────────────── letra ─────────────────────────
def fuente(nombre, tam, peso=None):
    f = ImageFont.truetype(str(F / nombre), max(8, round(tam)))
    if peso:
        f.set_variation_by_name(peso)
    return f


def ancho(txt, f, esp):
    return sum(f.getlength(c) for c in txt) + esp * (len(txt) - 1)


def texto(d, x, y, txt, f, color, esp=0.0, alinear="centro"):
    """Escribe con espacio entre letras. x es el centro, el borde izquierdo o el derecho según `alinear`."""
    w = ancho(txt, f, esp)
    x = x - w / 2 if alinear == "centro" else (x - w if alinear == "derecha" else x)
    for c in txt:
        d.text((x, y), c, font=f, fill=color)
        x += f.getlength(c) + esp
    asc, desc = f.getmetrics()
    return asc + desc


def estilos(k):
    return {
        "marca": (fuente("Cormorant.ttf", 30 * k, b"Medium"), 11 * k, 30 * k),
        "grande": (fuente("Cormorant.ttf", 120 * k, b"Light"), 6 * k, 8 * k),
        "titulo": (fuente("Cormorant.ttf", 78 * k, b"Light"), 0, -4 * k),
        "cursiva": (fuente("Cormorant-Italic.ttf", 78 * k, b"Light Italic"), 0, 24 * k),
        "linea": (fuente("Jost.ttf", 21 * k, b"Regular"), 5.5 * k, 14 * k),
        "nota": (fuente("Jost.ttf", 19 * k, b"Regular"), 4.5 * k, 6 * k),
        "cifra": (fuente("Cormorant-Italic.ttf", 230 * k, b"Light Italic"), 0, 6 * k),
    }


class Capa:
    """Texto y trazos en una capa aparte: así se les pone una sombra suave sin manchar la foto."""

    def __init__(self, im):
        self.im = im
        self.k = im.width / 1080
        self.capa = Image.new("RGBA", im.size, (0, 0, 0, 0))
        self.d = ImageDraw.Draw(self.capa)

    def bloque(self, lineas, y0, color, cx=None, alinear="centro"):
        """lineas: [(estilo, texto)]; y0 en fracción del alto. Devuelve la y (px) donde acaba."""
        W, H = self.im.size
        cx = W / 2 if cx is None else cx
        y = H * y0
        est = estilos(self.k)
        for tipo, txt in lineas:
            f, esp, despues = est[tipo]
            y += texto(self.d, cx, y, txt, f, color, esp, alinear) + despues
        return y

    def pildoras(self, textos, y, color):
        k = self.k
        f = fuente("Jost.ttf", 19 * k, b"Regular")
        esp, alto, sep = 3.5 * k, 46 * k, 14 * k
        anchos = [ancho(p, f, esp) + 44 * k for p in textos]
        x = self.im.width / 2 - (sum(anchos) + sep * (len(anchos) - 1)) / 2
        for p, a in zip(textos, anchos):
            self.d.rounded_rectangle((x, y, x + a, y + alto), radius=alto / 2, outline=color, width=max(1, round(1.4 * k)))
            asc, desc = f.getmetrics()
            texto(self.d, x + a / 2, y + (alto - asc - desc) / 2 - k, p, f, color, esp)
            x += a + sep

    def flecha(self, desde, hasta, color, curva=0.25):
        """Trazo fino y algo curvo, como dibujado a mano, con la punta en `hasta`."""
        (x0, y0), (x1, y1) = desde, hasta
        mx, my = (x0 + x1) / 2, (y0 + y1) / 2
        cx, cy = mx - (y1 - y0) * curva, my + (x1 - x0) * curva
        pts = [((1 - t) ** 2 * x0 + 2 * (1 - t) * t * cx + t ** 2 * x1,
                (1 - t) ** 2 * y0 + 2 * (1 - t) * t * cy + t ** 2 * y1) for t in np.linspace(0, 1, 40)]
        w = max(1, round(2 * self.k))
        self.d.line(pts, fill=color, width=w, joint="curve")
        ang = math.atan2(y1 - pts[-4][1], x1 - pts[-4][0])
        L = 16 * self.k
        for s in (-1, 1):
            a = ang + math.pi - s * 0.45
            self.d.line([(x1, y1), (x1 + L * math.cos(a), y1 + L * math.sin(a))], fill=color, width=w)

    def pegar(self, sombra=0.0):
        """sombra = opacidad de un halo muy difuso bajo el texto blanco (0 = sin sombra)."""
        base = self.im.convert("RGBA")
        if sombra:
            a = self.capa.getchannel("A").filter(ImageFilter.GaussianBlur(9 * self.k))
            negro = Image.new("RGBA", base.size, (0, 0, 0, 0))
            negro.putalpha(a.point(lambda v: round(v * sombra)))
            base = Image.alpha_composite(base, negro)
        return Image.alpha_composite(base, self.capa).convert("RGB")


# ───────────────────────── foto ─────────────────────────
def caja(im, W, H, cx, cy, alto):
    """Recorta de la foto una caja con la proporción W:H, centrada en (cx, cy) y de `alto` (fracción del alto)."""
    h = im.height * alto
    w = h * W / H
    if w > im.width:
        w, h = im.width, im.width * H / W
    x = min(max(cx * im.width - w / 2, 0), im.width - w)
    y = min(max(cy * im.height - h / 2, 0), im.height - h)
    rec = (x, y, x + w, y + h)
    return im.crop(tuple(round(v) for v in rec)).resize((W, H), Image.LANCZOS), rec


def a_lienzo(pt, rec, W, H, im):
    """Pasa un punto de la foto original (fracciones) a píxeles del lienzo recortado."""
    x0, y0, x1, y1 = rec
    return ((pt[0] * im.width - x0) / (x1 - x0) * W, (pt[1] * im.height - y0) / (y1 - y0) * H)


def mascara_joya(im):
    """Dónde está la joya: oro (amarillo saturado y luminoso) y piedras (colores muy saturados que no son piel)."""
    hsv = np.asarray(im.convert("HSV"), dtype=np.float32)
    h, s, v = hsv[..., 0] * 360 / 255, hsv[..., 1] / 255, hsv[..., 2] / 255
    oro = (h > 28) & (h < 58) & (s > 0.42) & (v > 0.45)
    piedra = (s > 0.38) & (v > 0.12) & ((h > 70) & (h < 330))
    m = Image.fromarray(((oro | piedra) * 255).astype(np.uint8))
    return m.filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(3))


def revelar(im):
    """Acabado de película en la piel y el fondo; la joya, casi intacta (Edu: «sin afectar tanto a la joya»)."""
    if not REVELAR:
        return im
    pel = pelicula(im)
    m = mascara_joya(im).point(lambda v: round(v * 0.85))
    return Image.composite(im, pel, m)


def textura(W, H, color, semilla=3):
    """Bloque de color con relieve de papel (como el naranja de Olivia), no un color plano de ordenador."""
    rng = np.random.default_rng(semilla)
    ruido = Image.fromarray(((rng.standard_normal((H // 2, W // 2)) * 0.5 + 0.5).clip(0, 1) * 255).astype(np.uint8))
    ruido = ruido.resize((W, H), Image.BICUBIC).filter(ImageFilter.GaussianBlur(1.2)).filter(ImageFilter.EMBOSS)
    r = (np.asarray(ruido, dtype=np.float32) - 128) / 128
    base = np.ones((H, W, 3), dtype=np.float32) * np.array(color, dtype=np.float32)
    base += r[..., None] * 9
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    base *= (1 - 0.06 * (((xx - W / 2) / W) ** 2 + ((yy - H / 2) / H) ** 2))[..., None]  # luz algo más viva en el centro
    return Image.fromarray(base.clip(0, 255).astype(np.uint8))


def cinta(im, rec, color):
    """Franja de raso: el color con un brillo suave en el centro, como una cinta de regalo."""
    x0, y0, x1, y1 = rec
    w, h = x1 - x0, y1 - y0
    vertical = h > w
    n = w if vertical else h
    perfil = np.array([1 + 0.16 * math.sin(math.pi * i / max(1, n - 1)) ** 2 - 0.06 for i in range(n)], dtype=np.float32)
    base = np.array(color, dtype=np.float32)
    fila = (base[None, :] * perfil[:, None]).clip(0, 255).astype(np.uint8)
    arr = np.repeat(fila[None, :, :], h, axis=0) if vertical else np.repeat(fila[:, None, :], w, axis=1)
    im.paste(Image.fromarray(arr), (x0, y0))


def guardar(im, nombre):
    if COLOR:
        nombre = f"{nombre}-{COLOR}"
    SALIDA.mkdir(parents=True, exist_ok=True)
    ruta = SALIDA / f"{nombre}.jpg"
    im.save(ruta, quality=95, subsampling=0)
    return ruta


# ───────────────────────── plantillas ─────────────────────────
def piezas(W, H, suf):
    vertical = H / W > 1.5
    y_arriba = 0.165 if vertical else 0.075  # en 9:16, por debajo de lo que tapa Instagram arriba
    hechas = []

    # 1 · De cerca: el cuello de Carmen, sin brazo ni reloj; texto blanco sobre la piel
    src = Image.open(FOTOS / "collar/editar-hombro-2.png").convert("RGB")
    im, _ = caja(src, W, H, 0.33, 0.36 if not vertical else 0.40, 0.50 if not vertical else 0.62)
    im = revelar(im)
    c = Capa(im)
    c.bloque([("marca", "LUNERIE"), ("titulo", "Tu nombre,"), ("cursiva", "tu piedra."),
              ("linea", "COLLAR SIGNÉ · 39,90 €")], y_arriba, BLANCO)
    hechas.append(guardar(c.pegar(0.35), f"1-de-cerca-{suf}"))

    # 2 · Anotada (como «NEW IN» de Olivia): el cuello de Elena con flechas al nombre y a la piedra
    src = Image.open(FOTOS / "collar/editar-tirantes-1.png").convert("RGB")
    im, rec = caja(src, W, H, 0.47, 0.50 if not vertical else 0.57, 0.56 if not vertical else 0.62)
    im = revelar(im)
    c = Capa(im)
    k = c.k
    c.bloque([("grande", "SIGNÉ"), ("linea", "EL COLLAR CON TU NOMBRE")], y_arriba + (0.0 if vertical else 0.01), BLANCO)
    nombre = a_lienzo((0.34, 0.545), rec, W, H, src)
    piedra = a_lienzo((0.555, 0.70), rec, W, H, src)
    est = estilos(k)["nota"][0]
    # nota del nombre: a la izquierda y por debajo, la flecha sube hacia el nombre
    nx, ny = nombre[0] - 40 * k, nombre[1] + 150 * k
    texto(c.d, nx, ny, "TU NOMBRE,", est, BLANCO, 4.5 * k)
    texto(c.d, nx, ny + 28 * k, "EN LETRA DE FIRMA", est, BLANCO, 4.5 * k)
    c.flecha((nx + 10 * k, ny - 12 * k), (nombre[0] - 6 * k, nombre[1] + 42 * k), BLANCO, 0.22)
    # nota de la piedra: a la derecha y por encima, la flecha baja hacia la piedra
    px, py = piedra[0] + 150 * k, piedra[1] - 150 * k
    texto(c.d, px, py, "EL COLOR", est, BLANCO, 4.5 * k)
    texto(c.d, px, py + 28 * k, "DE TU MES", est, BLANCO, 4.5 * k)
    c.flecha((px - 30 * k, py + 66 * k), (piedra[0] + 30 * k, piedra[1] - 6 * k), BLANCO, -0.25)
    hechas.append(guardar(c.pegar(0.38), f"2-anotada-{suf}"))

    # 3 · Producto: la pieza sola sobre su fondo y el nombre debajo
    foto = Image.open(FOTOS / "collar/producto-verde-carmen-v2.jpg").convert("RGB")
    fondo = foto.getpixel((10, 10))
    foto = foto.crop((0, 0, foto.width, round(foto.height * 0.789)))
    lienzo = Image.new("RGB", (W, H), fondo)
    h_foto = round(H * (0.74 if not vertical else 0.60))
    ph = foto.resize((round(foto.width * h_foto / foto.height), h_foto), Image.LANCZOS)
    m = Image.new("L", ph.size, 255)  # funde solo el último 1 % con el fondo (debajo había un reflejo)
    dm = ImageDraw.Draw(m)
    for i in range(round(h_foto * 0.012)):
        dm.line((0, h_foto - 1 - i, ph.width, h_foto - 1 - i), fill=round(255 * i / (h_foto * 0.012)))
    if vertical:  # la cadena entra fundida desde arriba
        for i in range(round(h_foto * 0.16)):
            dm.line((0, i, ph.width, i), fill=round(255 * i / (h_foto * 0.16)))
    lienzo.paste(ph, ((W - ph.width) // 2, 0 if not vertical else round(H * 0.33)), m)
    lienzo = revelar(lienzo)
    c = Capa(lienzo)
    c.bloque([("marca", "LUNERIE"), ("titulo", "Collar Signé"), ("linea", "TU NOMBRE EN LETRA DE FIRMA")],
             0.775 if not vertical else y_arriba, TINTA)
    hechas.append(guardar(c.pegar(), f"3-producto-{suf}"))

    # 4 · Promo partida (como el Black Friday de Olivia): bloque verde Lunerie con relieve + foto de cerca
    src = Image.open(FOTOS / "ugc-lucce/pecho-1.jpg").convert("RGB")
    if not vertical:  # mitad y mitad, en vertical
        mitad = W // 2
        lienzo = Image.new("RGB", (W, H))
        lienzo.paste(textura(mitad, H, MARCA), (0, 0))
        ph, _ = caja(src, W - mitad, H, 0.47, 0.50, 0.50)
        lienzo.paste(revelar(ph), (mitad, 0))
        c = Capa(lienzo)
        cx = mitad / 2
        if CINTA:
            cinta(lienzo, (mitad - round(7 * lienzo.width / 1080), 0, mitad + round(7 * lienzo.width / 1080), H), CINTA)
        c.bloque([("marca", "LUNERIE")], 0.075, ACC, cx)
        c.bloque([("titulo", "Black Friday")], 0.25, TXT, cx)
        y = c.bloque([("cifra", "3x2")], 0.33, ACC, cx)
        c.bloque([("linea", "LA 2.ª AL 50 %"), ("linea", "Y LA 3.ª, GRATIS")], (y + 10 * c.k) / H, TXT, cx)
        c.bloque([("nota", "HASTA EL 5 DE DICIEMBRE")], 0.86, TXT, cx)
    else:  # arriba el bloque, abajo la foto
        alto = round(H * 0.47)
        lienzo = Image.new("RGB", (W, H))
        lienzo.paste(textura(W, alto, MARCA), (0, 0))
        ph, _ = caja(src, W, H - alto, 0.42, 0.50, 0.40)
        lienzo.paste(revelar(ph), (0, alto))
        c = Capa(lienzo)
        c.bloque([("marca", "LUNERIE"), ("titulo", "Black Friday")], 0.15, BLANCO)
        y = c.bloque([("cifra", "3x2")], 0.225, BLANCO)
        c.bloque([("linea", "LA 2.ª AL 50 % Y LA 3.ª, GRATIS")], (y + 6 * c.k) / H, BLANCO)
    hechas.append(guardar(c.pegar(), f"4-promo-{suf}"))

    # 5 · Regalo partido: bloque burdeos con relieve arriba y la cajita abajo, borde limpio
    src = Image.open(FOTOS / "terciopelo/cajita-carmen-1.jpg").convert("RGB")
    alto = round(H * (0.36 if not vertical else 0.42))
    lienzo = Image.new("RGB", (W, H))
    lienzo.paste(textura(W, alto, MARCA if COLOR else BURDEOS, 5), (0, 0))
    ph, _ = caja(src, W, H - alto, 0.5, 0.58, 0.78 if not vertical else 0.80)
    lienzo.paste(revelar(ph), (0, alto))
    if CINTA:
        cinta(lienzo, (0, alto - round(7 * W / 1080), W, alto + round(7 * W / 1080)), CINTA)
    c = Capa(lienzo)
    y0 = 0.06 if not vertical else 0.15
    y = c.bloque([("marca", "LUNERIE")], y0, ACC)
    c.bloque([("titulo", "El regalo que"), ("cursiva", "lleva su nombre."),
              ("linea", "LLEGA EN SU CAJITA DE TERCIOPELO")], y / H, TXT)
    hechas.append(guardar(c.pegar(), f"5-regalo-{suf}"))

    # 6 · En la mano: sin texto, como los reels de Olivia (la foto se basta sola)
    src = Image.open(FOTOS / "collar/dedos-1.png").convert("RGB")
    im, _ = caja(src, W, H, 0.5, 0.5, 1.0)
    hechas.append(guardar(revelar(im), f"6-en-la-mano-{suf}"))
    return hechas


def bloque_marca(W, H, suf):
    """7 · La marca sola en su color (como la portada naranja de Olivia), para anuncios de novedad o temporada."""
    lienzo = textura(W, H, MARCA, 9)
    c = Capa(lienzo)
    k = c.k
    f = fuente("Cormorant.ttf", 64 * k, b"Medium")
    asc, desc = f.getmetrics()
    if CINTA:  # una cinta del otro color cruzando el bloque, como un lazo de regalo
        cinta(lienzo, (0, round(H * 0.72), W, round(H * 0.72 + 30 * k)), CINTA)
        c = Capa(lienzo)
    texto(c.d, W / 2, H * 0.40, "LUNERIE", f, TXT, 26 * k)
    c.bloque([("cursiva", "Con tu nombre.")], 0.40 + (asc + desc + 30 * k) / H, ACC)
    c.bloque([("nota", "TU NOMBRE  ·  TU INICIAL  ·  TU PIEDRA")], 0.90, TXT)
    return guardar(c.pegar(), f"7-marca-{suf}")


if __name__ == "__main__":
    if COLOR:  # prueba de color: solo lo que lleva el bloque de color
        hechas = [r for r in piezas(1080, 1350, "4x5") if any(n in r.name for n in ("4-promo", "5-regalo"))]
        hechas.append(bloque_marca(1080, 1350, "4x5"))
        for r in hechas:
            print(r)
    else:
        for W, H, s in ((1080, 1350, "4x5"), (1080, 1920, "9x16")):
            for r in piezas(W, H, s if REVELAR else s + "-sin-revelar"):
                print(r)
