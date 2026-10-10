"""Fotos provisionales del reloj Lune (dibujo como la maqueta de la página de marca), 4:5 con fondo niebla.
Solo para probar la ficha mientras no lleguen las muestras: llevan «Foto provisional» abajo a la izquierda."""
import pathlib
from PIL import Image, ImageDraw, ImageFont

OUT = pathlib.Path(__file__).parent / "fotos_prueba"
OUT.mkdir(exist_ok=True)
W, H, S = 1600, 2000, 4  # se dibuja a 4× y se reduce (bordes suaves)
MIST, GREY, INK = "#F2F4F2", "#6F7873", "#16201B"
GOLD, SILVER = "#A6834A", "#B9BEC0"
VARIANTES = {
    "dorado-verde": ("#1F6B4E", GOLD),
    "dorado-azul": ("#2C4F86", GOLD),
    "plateado-verde": ("#1F6B4E", SILVER),
}


def oval(d, cx, cy, w, h, fill, border, bw):
    d.ellipse([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], fill=border)
    d.ellipse([cx - w / 2 + bw, cy - h / 2 + bw, cx + w / 2 - bw, cy + h / 2 - bw], fill=fill)


def foto(piedra, metal, nombre):
    img = Image.new("RGB", (W * S, H * S), MIST)
    d = ImageDraw.Draw(img)
    cx, cy = W * S / 2, H * S / 2
    k = 5.2 * S  # escala respecto a la maqueta (piedra 26×38, esfera 68×86)
    piedra_h, esfera_h, gap = 38 * k, 86 * k, 4 * k
    alto = 4 * piedra_h + esfera_h + 4 * gap
    y = cy - alto / 2
    piezas = ["p", "p", "e", "p", "p"]
    for p in piezas:
        if p == "p":
            oval(d, cx, y + piedra_h / 2, 26 * k, piedra_h, piedra, metal, 4 * k)
            # brillo de la piedra
            d.ellipse([cx - 6 * k, y + 7 * k, cx - 1 * k, y + 15 * k], fill=_mezcla(piedra, "#FFFFFF", .3))
            y += piedra_h + gap
        else:
            oval(d, cx, y + esfera_h / 2, 68 * k, esfera_h, "#FBFAF6", metal, 7 * k)
            ccx, ccy = cx, y + esfera_h / 2
            _aguja(d, ccx, ccy, 24 * k, -35, 2 * k)
            _aguja(d, ccx, ccy, 17 * k, 70, 2 * k)
            r = 2.2 * k
            d.ellipse([ccx - r, ccy - r, ccx + r, ccy + r], fill=INK)
            y += esfera_h + gap
    img = img.resize((W, H), Image.LANCZOS)
    d = ImageDraw.Draw(img)
    try:
        f = ImageFont.truetype("arial.ttf", 30)
    except OSError:
        f = ImageFont.load_default()
    d.text((56, H - 80), "Foto provisional", fill=GREY, font=f)
    img.save(OUT / f"lune-{nombre}.jpg", quality=90)


def _aguja(d, cx, cy, largo, grados, ancho):
    import math
    a = math.radians(grados - 90)
    d.line([cx, cy, cx + largo * math.cos(a), cy + largo * math.sin(a)], fill=INK, width=int(ancho))


def _mezcla(c1, c2, t):
    a = [int(c1[i:i + 2], 16) for i in (1, 3, 5)]
    b = [int(c2[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(x + (y - x) * t):02x}" for x, y in zip(a, b))


for nombre, (piedra, metal) in VARIANTES.items():
    foto(piedra, metal, nombre)
print("ok", sorted(p.name for p in OUT.iterdir()))
