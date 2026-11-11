"""Pegatina redonda «Cajita de regalo incluida» sobre la foto de la cajita del Collar Signé (11-nov-2026, idea de Edu
vista en otra tienda; diseño propio con los colores de Lunerie: verde Rolex, oro y Jost).

    python marca/pegatina_cajita.py  →  marca/fotos-ia/cajita/collar-signe-cajita-pegatina.jpg (1744 × 2180, 4:5)
"""
import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

RAIZ = Path(__file__).resolve().parent.parent
FOTO = RAIZ / "marca" / "fotos-ia" / "cajita" / "collar-signe-cajita.jpg"
SALIDA = FOTO.with_name("collar-signe-cajita-pegatina.jpg")
VERDE, ORO, BLANCO = (0, 96, 57), (214, 184, 128), (255, 255, 255)


def jost(tam, peso):
    f = ImageFont.truetype(str(RAIZ / "marca" / "fuentes" / "Jost.ttf"), tam)
    f.set_variation_by_name(peso)
    return f


def pegatina(d=520):
    esc = 3   # se dibuja grande y se reduce: bordes limpios
    D = d * esc
    im = Image.new("RGBA", (D, D), (0, 0, 0, 0))
    dr = ImageDraw.Draw(im)
    dr.ellipse((0, 0, D - 1, D - 1), fill=VERDE)
    dr.ellipse((D * .15, D * .15, D * .85, D * .85), outline=ORO, width=int(2.2 * esc))
    # texto en círculo alrededor
    f = jost(int(34 * esc), "Medium")
    r = D * .4
    unidad = "LUNERIE  ·  "
    veces = max(1, round(2 * math.pi * r / sum(dr.textlength(c, font=f) for c in unidad)))
    frase = unidad * veces   # da la vuelta entera: el espaciado se estira para cerrar el círculo
    estira = 2 * math.pi * r / sum(dr.textlength(c, font=f) for c in frase)
    ang = -90
    for c in frase:
        w = dr.textlength(c, font=f)
        a = ang + math.degrees(w * estira / 2 / r)
        letra = Image.new("RGBA", (int(w * 2 + 10), int(f.size * 1.6)), (0, 0, 0, 0))
        ImageDraw.Draw(letra).text((letra.width / 2, letra.height / 2), c, font=f, fill=ORO, anchor="mm")
        letra = letra.rotate(-a - 90, resample=Image.BICUBIC, expand=True)
        x = D / 2 + r * math.cos(math.radians(a)) - letra.width / 2
        y = D / 2 + r * math.sin(math.radians(a)) - letra.height / 2
        im.alpha_composite(letra, (int(x), int(y)))
        ang += math.degrees(w * estira / r)
    # centro
    g = jost(int(46 * esc), "SemiBold")
    for i, linea in enumerate(["CAJITA", "DE REGALO", "INCLUIDA"]):
        dr.text((D / 2, D / 2 + (i - 1) * 54 * esc), linea, font=g, fill=BLANCO, anchor="mm")
    return im.resize((d, d), Image.LANCZOS)


def main():
    foto = Image.open(FOTO).convert("RGBA")
    p = pegatina(int(foto.width * .3))
    sombra = Image.new("RGBA", foto.size, (0, 0, 0, 0))
    x, y = foto.width - p.width - int(foto.width * .05), int(foto.width * .05)
    foto.alpha_composite(p.rotate(-12, resample=Image.BICUBIC), (x, y))
    foto.convert("RGB").save(SALIDA, quality=95, subsampling=0)
    print(SALIDA)


if __name__ == "__main__":
    sys.exit(main())
