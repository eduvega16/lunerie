"""Anuncio «Nota del equipo» (formato 26 de biblioteca/formatos-anuncio.json, visto en Olivia Jewelry el 5-nov): solo
texto sobre fondo tinta, como un aviso escrito por Lunerie. Sin créditos de IA.
    python marca/nota_equipo.py   → marca/fotos-ia/campana-bf/17-nota-equipo-9x16.jpg y -4x5.jpg
El ejemplo de precios tiene que ser una cesta real: Collar Signé 49,95 + Reloj Lune 39,95 + aros Boucle 19,95 =
109,85 €; con el 3x2 la más barata sale gratis → 89,90 € (comprobado el 5-nov). Si cambia un precio, cambiar LINEAS.
"""
import pathlib
from PIL import Image, ImageDraw, ImageFont

RAIZ = pathlib.Path(__file__).resolve().parent.parent
FUENTES = RAIZ / "marca" / "fuentes"
SALIDA = RAIZ / "marca" / "fotos-ia" / "campana-bf"
TINTA, BLANCO, NIEBLA, ORO = (22, 32, 27), (255, 255, 255), (214, 220, 216), (196, 162, 106)


def fuente(nombre, tam, peso=None):
    f = ImageFont.truetype(str(FUENTES / nombre), tam)
    if peso:
        try:
            f.set_variation_by_name(peso)
        except Exception:
            pass
    return f


# (texto, estilo, espacio antes)
LINEAS = [
    ("Hola,", "titulo", 0),
    ("Un aviso rápido:", "texto", 26),
    ("el Black Friday de Lunerie ya está aquí.", "texto", 10),
    ("La 2.ª pieza al 50 % y la 3.ª, gratis.", "destacado", 30),
    ("Y sí: el collar con nombre también entra.", "texto", 30),
    ("Por ejemplo, Collar Signé + Reloj Lune", "texto", 30),
    ("+ aros Boucle: 109,85 € por separado.", "texto", 10),
    ("Con la oferta, 89,90 €.", "destacado", 10),
    ("Mezcla lo que quieras. Hasta el 5 de diciembre.", "texto", 30),
    ("El equipo de Lunerie", "firma", 40),
]
ESTILOS = {
    "titulo": (lambda: fuente("Cormorant-Italic.ttf", 110, "Regular"), BLANCO),
    "texto": (lambda: fuente("Jost.ttf", 44, "Light"), NIEBLA),
    "destacado": (lambda: fuente("Jost.ttf", 46, "Medium"), BLANCO),
    "firma": (lambda: fuente("Cormorant-Italic.ttf", 58, "Regular"), ORO),
}


def bloque():
    """Calcula alto total y posiciones relativas."""
    d = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    y, items = 0, []
    for texto, estilo, antes in LINEAS:
        f, color = ESTILOS[estilo][0](), ESTILOS[estilo][1]
        y += antes
        caja = d.textbbox((0, 0), texto, font=f)
        items.append((texto, f, color, y))
        y += (caja[3] - caja[1]) + 16
    return y, items


def lamina(w, h, y0, destino):
    im = Image.new("RGB", (w, h), TINTA)
    d = ImageDraw.Draw(im)
    alto, items = bloque()
    y0 = y0 if y0 is not None else (h - alto) // 2
    for texto, f, color, y in items:
        x = (w - d.textlength(texto, font=f)) / 2
        d.text((x, y0 + y), texto, font=f, fill=color)
    im.save(destino, quality=97, subsampling=0)
    print(destino, "texto de", y0, "a", y0 + alto)


if __name__ == "__main__":
    SALIDA.mkdir(parents=True, exist_ok=True)
    lamina(1080, 1920, 290, SALIDA / "17-nota-equipo-9x16.jpg")     # 9:16: texto entre y=270 y y=1248
    lamina(1080, 1350, None, SALIDA / "17-nota-equipo-4x5.jpg")
