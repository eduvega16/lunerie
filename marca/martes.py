"""Carrusel «Un martes cualquiera» (3-nov; idea 1 de oficina/ideas/2026-11-03-cada-dia.md): las piezas a lo largo de un
día normal, con la hora en pequeño y el nombre de lo que se ve, en el estilo sobrio de la portada (fotos de
marca/portada_dia.py). Sin precios en las fotos salvo la última; sin oferta, para que sirva también después del 5-dic.
    python marca/martes.py   →   marca/fotos-ia/martes/1.jpg … 7.jpg (4:5, 1080×1350)
Las horas son un rótulo, no lo que marcan las agujas.
"""
import pathlib
from PIL import Image, ImageDraw
from campana_bf import ESTILOS, FOTOS, NIEBLA, TINTA, ORO, degradado, linea, recorte

SALIDA = FOTOS / "martes"
DIA = FOTOS / "portada-dia"
W, H, M = 1080, 1350, 72
ESTILOS.update({
    "hora": ("Jost.ttf", 30, 500, (255, 255, 255), 6, True),
    "piezas": ("Jost.ttf", 29, 400, (231, 225, 214), 1, False),
    "fin-titulo": ("Cormorant-Italic.ttf", 92, 450, TINTA, 0, False),
    "fin-texto": ("Jost.ttf", 32, 400, (61, 72, 66), 1, False),
    "fin-marca": ("Cormorant.ttf", 40, 500, TINTA, 14, True),
    "fin-ceja": ("Jost.ttf", 26, 450, ORO, 6, True),
})
# foto, punto del recorte (x, y), hora, piezas que se ven; la primera lleva además el gancho
DIAPOSITIVAS = [
    ("izquierda-1.png", (0.45, 0.5), "8:00 · café", "Reloj Lune · Anillo Nuit · Collar Lune"),
    ("metro-1.png", (0.5, 0.5), "8:40 · metro", "Reloj Galet · Anillo Nuit"),
    ("trabajo-1.png", (0.5, 0.5), "11:00 · trabajo", "Reloj Perle · Anillo Duo"),
    ("mercado-1.png", (0.5, 0.5), "13:30 · mercado", "Reloj Lune · Anillo Étoile"),
    ("centro-2.png", (0.53, 0.5), "17:00 · una pausa", "Reloj Maille · Aros Boucle · Anillo Duo"),
    ("derecha-2.png", (0.5, 0.5), "20:30 · una copa", "Reloj Sépia · Anillo Étoile · Pendientes Larme"),
]


def foto(i, nombre, punto, hora, piezas):
    img = recorte(Image.open(DIA / nombre).convert("RGB"), W, H, *punto)
    img = degradado(img, int(H * (0.52 if i == 0 else 0.7)), H, alfa=0.72)
    d = ImageDraw.Draw(img)
    y = H - M - 34 - 38
    if i == 0:
        y -= 128
        linea(d, "Un martes cualquiera.", "gancho", 0, y, W - 2 * M, izquierda=M)
        y += 128
    linea(d, hora, "hora", 0, y, W - 2 * M, izquierda=M)
    linea(d, piezas, "piezas", 0, y + 46, W - 2 * M, izquierda=M)
    return img


def final():
    img = Image.new("RGB", (W, H), NIEBLA)
    d = ImageDraw.Draw(img)
    y = 430
    for texto, estilo, salto in [("Para cada día", "fin-ceja", 70), ("Un reloj que solo", "fin-titulo", 104),
                                 ("da la hora.", "fin-titulo", 150),
                                 ("Relojes desde 34,95 € · joyas desde 19,95 €", "fin-texto", 52),
                                 ("Envío gratis a península · lunerie.es", "fin-texto", 200),
                                 ("Lunerie", "fin-marca", 0)]:
        linea(d, texto, estilo, W / 2, y, W - 2 * M)
        y += salto
    return img


if __name__ == "__main__":
    SALIDA.mkdir(parents=True, exist_ok=True)
    for i, (nombre, punto, hora, piezas) in enumerate(DIAPOSITIVAS):
        foto(i, nombre, punto, hora, piezas).save(SALIDA / f"{i + 1}.jpg", quality=90)
    final().save(SALIDA / f"{len(DIAPOSITIVAS) + 1}.jpg", quality=90)
    print("ok:", SALIDA)
