"""«Revelado» de las fotos de IA para que no parezcan de IA (3-nov, Edu: «se ven muy IA» y «los relojes salen algo
pequeños»): encuadre más cerca de las joyas (el reloj ocupa más foto sin agrandarlo respecto a la muñeca: la esfera
mide 12 mm) y acabado de película (algo más cálido y menos saturado, negros levantados, luces suaves, viñeta ligera
y grano). No cambia ninguna pieza.
    python marca/revelar.py [nombre ...]   →   marca/fotos-ia/portada-dia/revelado/<nombre>.jpg
"""
import pathlib, sys
import numpy as np
from PIL import Image, ImageFilter

DIA = pathlib.Path(__file__).resolve().parent / "fotos-ia" / "portada-dia"
SALIDA = DIA / "revelado"
# salida: (foto original, zoom, centro x, centro y) — el centro, donde están el reloj y las joyas
ENCUADRE = {
    "izquierda-1": ("izquierda-1", 1.15, 0.40, 0.46), "centro-2": ("centro-2", 1.12, 0.52, 0.45),
    "derecha-2": ("derecha-2", 1.10, 0.50, 0.45), "metro-1": ("metro-1", 1.12, 0.40, 0.45),
    "trabajo-1": ("trabajo-1", 1.15, 0.60, 0.40), "mercado-1": ("mercado-1", 1.12, 0.55, 0.45),
    # para el carrusel (4:5): la apaisada sin acercar, o el reloj queda pegado al borde de abajo
    "centro-2-entera": ("centro-2", 1.0, 0.5, 0.5),
}


def acercar(im, zoom, cx, cy):
    w, h = im.size
    cw, ch = w / zoom, h / zoom
    x = min(max(cx * w - cw / 2, 0), w - cw)
    y = min(max(cy * h - ch / 2, 0), h - ch)
    return im.crop((round(x), round(y), round(x + cw), round(y + ch))).resize((w, h), Image.LANCZOS)


def pelicula(im, semilla=7):
    a = np.asarray(im.convert("RGB"), dtype=np.float32) / 255
    # color: un poco menos saturado y más cálido
    gris = a @ np.array([0.299, 0.587, 0.114], dtype=np.float32)
    a = gris[..., None] + (a - gris[..., None]) * 0.88
    a *= np.array([1.025, 1.0, 0.965], dtype=np.float32)
    # curva: negros levantados y luces que no llegan al blanco puro
    a = 0.035 + a * 0.93
    a = a + 0.04 * np.sin(np.pi * a) * (0.5 - a)        # contraste suave en S, invertido en los extremos
    # viñeta ligera
    h, w = gris.shape
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    r = np.sqrt(((xx - w / 2) / (w / 2)) ** 2 + ((yy - h / 2) / (h / 2)) ** 2)
    a *= (1 - 0.10 * np.clip(r - 0.55, 0, None) ** 1.6)[..., None]
    # grano: ruido de luminancia, algo más visible en los medios tonos, con tamaño de ~1,5 px
    rng = np.random.default_rng(semilla)
    ruido = Image.fromarray(((rng.standard_normal((h, w)) * 0.5 + 0.5).clip(0, 1) * 255).astype(np.uint8))
    ruido = np.asarray(ruido.filter(ImageFilter.GaussianBlur(0.8)), dtype=np.float32) / 255 - 0.5
    lum = a.mean(axis=2, keepdims=True)
    a += ruido[..., None] * 0.09 * (0.4 + 0.6 * (1 - np.abs(lum - 0.5) * 2))
    return Image.fromarray((a.clip(0, 1) * 255).astype(np.uint8))


if __name__ == "__main__":
    SALIDA.mkdir(parents=True, exist_ok=True)
    for i, n in enumerate(sys.argv[1:] or ENCUADRE):
        fuente, *encuadre = ENCUADRE[n]
        im = acercar(Image.open(DIA / f"{fuente}.png").convert("RGB"), *encuadre)
        pelicula(im, semilla=i + 7).save(SALIDA / f"{n}.jpg", quality=90, optimize=True, progressive=True)
        print("ok", n)
