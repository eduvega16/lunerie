"""Carrusel «It's timeeee» (trend de noviembre visto en @embroidera.us, 18-nov): 5 fotos que juntas son una sola
imagen. En la 1.ª, «It's tim» y una cadena de «e» que ondula y hace un bucle de foto en foto; en la 5.ª, la frase
final con el Collar Signé (en un óvalo con filo dorado, la firma de Lunerie) y recortes del Reloj Lune y el Anillo Nuit.
Sin IA: Pillow con fotos ya revisadas.

    python marca/its_time.py            → versión A («It's timeeee… de encontrar su regalo.»)
    python marca/its_time.py es         → versión B («Ya es horaaaa… de buscar su regalo.»)

Salida: marca/fotos-ia/its-time/<versión>/its-time-1.jpg … its-time-5.jpg (4:5, 1080×1350) + hoja.jpg para revisar.
La música (el audio del trend) no se puede poner por la API: se sube desde la app.
"""
import math
import random
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

RAIZ = Path(__file__).resolve().parent
FUENTE = RAIZ / "fuentes" / "Jost.ttf"
W, H, N = 1080, 1350, 5
FONDO = (88, 10, 13)          # vino, como el terciopelo de Navidad
CREMA = (247, 239, 228)
ORO = (166, 131, 74)          # #A6834A
ORO_CLARO = (214, 184, 128)

VERSIONES = {
    "en": {"inicio": "It's tim", "letra": "e", "final": ["de encontrar", "su regalo."]},
    "es": {"inicio": "Ya es hor", "letra": "a", "final": ["de buscar", "su regalo."]},
}

# Recorrido de la cadena (x en «fotos», 0-5; y en fracción del alto). Hace una ola en la 2.ª, un bucle en la 3.ª,
# baja y sube en la 4.ª y acaba arriba en la 5.ª.
PUNTOS = [
    (0.84, None), (0.98, None), (1.12, 0.37), (1.24, 0.33), (1.36, 0.41), (1.50, 0.59), (1.68, 0.72), (1.90, 0.74),
    (2.15, 0.66), (2.38, 0.53), (2.55, 0.40), (2.64, 0.26), (2.58, 0.14), (2.45, 0.13), (2.37, 0.25), (2.42, 0.41),
    (2.58, 0.53), (2.82, 0.63), (3.10, 0.70), (3.38, 0.69), (3.55, 0.56), (3.58, 0.38), (3.62, 0.24), (3.78, 0.16),
    (4.05, 0.135), (4.33, 0.135),
]


def fuente(tam, peso="SemiBold"):
    f = ImageFont.truetype(str(FUENTE), tam)
    f.set_variation_by_name(peso)
    return f


def catmull_rom(p, pasos=60, alfa=0.5):
    """Curva centrípeta que pasa por todos los puntos (sin picos raros en el bucle)."""
    p = [p[0]] + p + [p[-1]]
    sal = []
    for i in range(1, len(p) - 2):
        p0, p1, p2, p3 = p[i - 1], p[i], p[i + 1], p[i + 2]

        def tj(ti, a, b):
            return ti + max(math.dist(a, b), 1e-6) ** alfa

        t0 = 0.0
        t1 = tj(t0, p0, p1)
        t2 = tj(t1, p1, p2)
        t3 = tj(t2, p2, p3)
        for k in range(pasos):
            t = t1 + (t2 - t1) * k / pasos

            def lerp(a, b, ta, tb):
                return tuple(((tb - t) * a[j] + (t - ta) * b[j]) / (tb - ta) for j in range(2))

            a1, a2, a3 = lerp(p0, p1, t0, t1), lerp(p1, p2, t1, t2), lerp(p2, p3, t2, t3)
            b1, b2 = lerp(a1, a2, t0, t2), lerp(a2, a3, t1, t3)
            sal.append(lerp(b1, b2, t1, t2))
    sal.append(p[-2])
    return sal


def glifo(letra, f):
    caja = f.getbbox(letra)
    im = Image.new("RGBA", (caja[2] + 20, caja[3] + 20), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((10, 10), letra, font=f, fill=CREMA)
    return im.crop(im.getbbox())


def destello(d, cx, cy, r, color):
    """Destello de 4 puntas (el del monograma)."""
    k = r * 0.22
    d.polygon([(cx, cy - r), (cx + k, cy - k), (cx + r, cy), (cx + k, cy + k), (cx, cy + r), (cx - k, cy + k),
               (cx - r, cy), (cx - k, cy - k)], fill=color)


def ovalo(foto, ancho, alto, borde=4):
    im = Image.open(foto).convert("RGB")
    esc = max(ancho / im.width, alto / im.height)
    im = im.resize((round(im.width * esc), round(im.height * esc)), Image.LANCZOS)
    x0, y0 = (im.width - ancho) // 2, int((im.height - alto) * 0.42)
    im = im.crop((x0, y0, x0 + ancho, y0 + alto))
    s = 4
    m = Image.new("L", (ancho * s, alto * s), 0)
    ImageDraw.Draw(m).ellipse((0, 0, ancho * s - 1, alto * s - 1), fill=255)
    m = m.resize((ancho, alto), Image.LANCZOS)
    sal = Image.new("RGBA", (ancho + 2 * borde + 40, alto + 2 * borde + 40), (0, 0, 0, 0))
    a = Image.new("L", (sal.width * s, sal.height * s), 0)
    ImageDraw.Draw(a).ellipse((20 * s, 20 * s, (20 + ancho + 2 * borde) * s - 1, (20 + alto + 2 * borde) * s - 1),
                              outline=255, width=borde * s // 2 * 2)
    a = a.resize(sal.size, Image.LANCZOS)
    sal.paste(Image.new("RGBA", sal.size, ORO + (255,)), (0, 0), a)
    sal.paste(im, (20 + borde, 20 + borde), m)
    return sal


def recorte(ruta, alto=None, ancho=None, giro=0, sombra=True):
    im = Image.open(ruta).convert("RGBA")
    im.putalpha(im.split()[3].filter(ImageFilter.MinFilter(3)))   # fuera el filo blanco del recorte
    im = im.crop(im.getbbox())
    esc = (alto / im.height) if alto else (ancho / im.width)
    im = im.resize((round(im.width * esc), round(im.height * esc)), Image.LANCZOS)
    if giro:
        im = im.rotate(giro, resample=Image.BICUBIC, expand=True)
    if not sombra:
        return im
    pad = 40
    s = Image.new("RGBA", (im.width + 2 * pad, im.height + 2 * pad), (0, 0, 0, 0))
    a = im.split()[3].point(lambda v: v * 0.55)
    s.paste((20, 0, 0, 255), (pad + 10, pad + 16), a)
    s = s.filter(ImageFilter.GaussianBlur(14))
    s.alpha_composite(im, (pad, pad))
    return s


def montar(clave):
    v = VERSIONES[clave]
    lienzo = Image.new("RGB", (W * N, H), FONDO)
    # luz suave: un poco más claro en el centro vertical, sin cortes entre fotos
    luz = Image.new("L", (1, H))
    for y in range(H):
        luz.putpixel((0, y), int(28 * math.exp(-((y / H - 0.48) ** 2) / 0.09)))
    lienzo = Image.composite(Image.new("RGB", lienzo.size, (122, 22, 24)), lienzo, luz.resize(lienzo.size))
    d = ImageDraw.Draw(lienzo)

    # 1.ª foto: «It's tim» y la cadena de letras
    f = fuente(132)
    x0, base = 92, 700
    d.text((x0, base), v["inicio"], font=f, fill=CREMA, anchor="ls")
    fin = x0 + d.textlength(v["inicio"], font=f)
    g = glifo(v["letra"], f)
    xh = f.getbbox("x", anchor="ls")
    yc = (base + (xh[1] + xh[3]) / 2) / H
    avance = d.textlength(v["letra"], font=f) * 0.98
    pts = [((fin + avance / 2) / W, yc)] + [(x, y if y is not None else yc) for x, y in PUNTOS]
    curva = [(x * W, y * H) for x, y in catmull_rom(pts)]
    dist = 0.0
    sig = 0.0
    for (ax, ay), (bx, by) in zip(curva, curva[1:]):
        seg = math.dist((ax, ay), (bx, by))
        while sig <= dist + seg:
            t = (sig - dist) / seg if seg else 0
            px, py = ax + (bx - ax) * t, ay + (by - ay) * t
            ang = math.degrees(math.atan2(by - ay, bx - ax))
            r = g.rotate(-ang, resample=Image.BICUBIC, expand=True)
            lienzo.paste(r, (round(px - r.width / 2), round(py - r.height / 2)), r)
            sig += avance
        dist += seg

    # 5.ª foto: frase final, el collar en el óvalo dorado y dos piezas recortadas
    o = 4 * W
    random.seed(7)
    libres = 0
    while libres < 22:                       # puntitos de nieve, solo en la última y lejos de texto y piezas
        cx, cy = random.randint(30, W - 30), random.randint(470, H - 30)
        if (200 < cx < 880 and cy < 560) or (280 < cx < 800 and 540 < cy < 1210) or (cx < 300 and cy > 680) \
                or (cx > 780 and 940 < cy < 1300) or (400 < cx < 680 and cy > 1250):
            continue
        rr = random.choice([3, 4, 5])
        d.ellipse((o + cx - rr, cy - rr, o + cx + rr, cy + rr), fill=(240, 220, 215))
        libres += 1
    f2 = fuente(104)
    for i, linea in enumerate(v["final"]):
        d.text((o + W / 2, 395 + i * 122), linea, font=f2, fill=CREMA, anchor="ms")
    ov = ovalo(RAIZ / "fotos-ia" / "terciopelo" / "cajita-carmen-1.jpg", 470, 600)
    lienzo.paste(ov, (o + (W - ov.width) // 2, 560), ov)
    img = RAIZ / "anuncios-hf" / "assets" / "img"
    reloj = recorte(img / "reloj-lune-recorte.png", alto=560, giro=-14)
    lienzo.paste(reloj, (o + 40, 690), reloj)
    anillo = recorte(img / "anillo-nuit-recorte.png", ancho=210, giro=12)
    lienzo.paste(anillo, (o + W - anillo.width - 10, 930), anillo)
    d = ImageDraw.Draw(lienzo)
    for cx, cy, r in [(o + 150, 560, 22), (o + 930, 600, 30), (o + 975, 470, 14), (o + 70, 470, 12),
                      (o + 330, 1270, 16), (o + 760, 1250, 20)]:
        destello(d, cx, cy, r, ORO_CLARO)
    fl = fuente(30, "Regular")
    marca = "L U N E R I E"
    d.text((o + W / 2, H - 34), marca, font=fl, fill=CREMA, anchor="ms")

    sal = RAIZ / "fotos-ia" / "its-time" / clave
    sal.mkdir(parents=True, exist_ok=True)
    for i in range(N):
        lienzo.crop((i * W, 0, (i + 1) * W, H)).save(sal / f"its-time-{i + 1}.jpg", quality=97, subsampling=0)
    hoja = lienzo.resize((W * N // 4, H // 4), Image.LANCZOS)
    hoja.save(sal / "hoja.jpg", quality=92)
    print("hecho:", sal)


if __name__ == "__main__":
    montar(sys.argv[1] if len(sys.argv) > 1 else "en")
