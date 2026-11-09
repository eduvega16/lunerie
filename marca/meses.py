"""Posts «Las lágrimas del invierno / de la primavera» (plan de 2 al día, 9-nov, OK de Edu): las 3 gotas reales de la
tabla (lagrima-NN.png, las mismas del panel «Elige la piedra» de la ficha) con el mes y el nombre del color, sin
nombres de gemas. Sin IA.
    python marca/meses.py   → marca/fotos-ia/meses/invierno.jpg, primavera.jpg (4:5, 1080×1350)
"""
import pathlib
from PIL import Image, ImageDraw, ImageFont

RAIZ = pathlib.Path(__file__).resolve().parent.parent
GOTAS = RAIZ / "marca" / "fotos-ia" / "lagrimas"
SALIDA = RAIZ / "marca" / "fotos-ia" / "meses"
F = RAIZ / "marca" / "fuentes"
NIEBLA, TINTA, GRIS, ORO = (242, 244, 242), (22, 32, 27), (52, 62, 57), (166, 131, 74)
ESTACIONES = {
    "invierno": ("del invierno", [(12, "Diciembre", "azul"), (1, "Enero", "rojo oscuro"), (2, "Febrero", "morado")]),
    "primavera": ("de la primavera", [(3, "Marzo", "azul agua"), (4, "Abril", "blanco"), (5, "Mayo", "verde")]),
}


def fuente(nombre, tam):
    return ImageFont.truetype(str(F / nombre), tam)


def montar(clave):
    titulo, meses = ESTACIONES[clave]
    W, H = 1080, 1350
    im = Image.new("RGB", (W, H), NIEBLA)
    d = ImageDraw.Draw(im)

    def centrado(texto, f, y, color, x=W / 2, espacio=0):
        if espacio:
            ancho = sum(d.textlength(c, font=f) for c in texto) + espacio * (len(texto) - 1)
            xx = x - ancho / 2
            for c in texto:
                d.text((xx, y), c, font=f, fill=color); xx += d.textlength(c, font=f) + espacio
        else:
            d.text((x - d.textlength(texto, font=f) / 2, y), texto, font=f, fill=color)

    centrado("LAS LÁGRIMAS", fuente("Jost.ttf", 30), 150, GRIS, espacio=7)
    centrado(titulo, fuente("Cormorant-Italic.ttf", 104), 196, TINTA)
    d.line((W / 2 - 40, 352, W / 2 + 40, 352), fill=ORO, width=2)
    alto = 240
    for k, (n, mes, color) in enumerate(meses):
        cx = W * (k + 1) / 4
        g = Image.open(GOTAS / f"lagrima-{n:02d}.png").convert("RGBA")
        g = g.resize((round(g.width * alto / g.height), alto), Image.LANCZOS)
        sombra = Image.new("RGBA", g.size, (0, 0, 0, 0))
        im.paste(g, (round(cx - g.width / 2), 470), g)
        centrado(mes, fuente("Cormorant.ttf", 50), 470 + alto + 40, TINTA, x=cx)
        centrado(color, fuente("Jost.ttf", 28), 470 + alto + 108, GRIS, x=cx)
    centrado("¿Cuál es la suya?", fuente("Cormorant-Italic.ttf", 62), 1040, TINTA)
    centrado("COLLAR SIGNÉ · SU NOMBRE Y LA LÁGRIMA DE SU MES", fuente("Jost.ttf", 24), 1140, GRIS, espacio=3)
    SALIDA.mkdir(parents=True, exist_ok=True)
    destino = SALIDA / f"{clave}.jpg"
    im.save(destino, quality=97, subsampling=0)
    print(destino)


if __name__ == "__main__":
    for c in ESTACIONES:
        montar(c)
