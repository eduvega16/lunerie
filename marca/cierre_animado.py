"""Anuncio 23 animado (idea de Edu, 9-nov): el Collar Signé baja desde arriba como si alguien lo fuera bajando con la mano,
se para con un pequeño rebote, la lágrima se balancea hasta quedarse quieta y aparece el texto del cierre.
Es la foto REAL de la ficha (producto-verde-3) animada por partes, sin IA (Kling deforma el nombre): la lágrima con su
anilla se recorta por el fondo claro y gira desde donde cuelga de la cadena.
    python marca/cierre_animado.py  → marca/fotos-ia/campana-bf/23-cierre-anim-9x16.mp4 y -4x5.mp4
La cadena sale siempre por arriba del encuadre (como si hubiera una mano). En 9:16, nombre, lágrima y texto quedan
dentro de la zona libre de Meta (y 270-1248).
"""
import math, pathlib, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import imageio_ffmpeg
from mofu_bofu import FOTO, SALIDA, FONDO, TINTA, GRIS, ROJO, jost, corm, cormi, centro, mixto

ESCALA = 0.42
CORTE_Y = 2438            # debajo empieza el reflejo de la foto
COLG = (1060, 1925, 1440, 2438)   # caja de la lágrima con la parte baja de la anilla (por debajo de la cadena)
PIVOTE = (1257, 1900)     # donde la anilla cuelga de la cadena
FPS, DURACION = 30, 6.5
BAJADA = 1.15             # segundos bajando
RECORRIDO = 1150          # px que baja


def preparar():
    """Devuelve la cadena con el nombre (sin la lágrima) y la lágrima en RGBA, ya a escala."""
    im = Image.open(FOTO).convert("RGB").crop((0, 0, 2480, CORTE_Y))
    a = np.asarray(im).astype(np.int16)
    fondo = np.array(FONDO, dtype=np.int16)
    x0, y0, x1, y1 = COLG
    zona = a[y0:y1, x0:x1]
    dif = np.abs(zona - fondo).max(axis=2)
    alfa = np.clip((dif - 8) * 9, 0, 255).astype(np.uint8)
    colg = Image.fromarray(zona.astype(np.uint8)).convert("RGBA")
    colg.putalpha(Image.fromarray(alfa))
    # el hueco: color de fondo con un borde suave
    base = im.copy()
    hueco = Image.fromarray(alfa).filter(ImageFilter.MaxFilter(9)).filter(ImageFilter.GaussianBlur(4))
    base.paste(Image.new("RGB", colg.size, FONDO), (x0, y0), hueco)
    # arriba de la caja, la anilla sigue unida a la cadena en la base: no se toca
    w, h = round(base.width * ESCALA), round(base.height * ESCALA)
    base = base.resize((w, h), Image.Resampling.LANCZOS)
    colg = colg.resize((round(colg.width * ESCALA), round(colg.height * ESCALA)), Image.Resampling.LANCZOS)
    return base, colg


def texto(w):
    """Capa RGBA con el texto del cierre, entre y=915 y y≈1228."""
    capa = Image.new("RGBA", (w, 1350), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    y = 915
    centro(d, y, "BLACK FRIDAY", jost(32, "Medium"), ROJO, w, espaciado=7)
    y += 50
    mixto(d, y, [("Su nombre, ", corm(96), TINTA), ("su piedra.", cormi(96), TINTA)], w)
    y += 113
    centro(d, y, "La 2.ª pieza al 50 % y la 3.ª, gratis.", jost(44, "Regular"), TINTA, w)
    y += 64
    centro(d, y, "Collar Signé · 49,95 € · Hasta el 5 de diciembre", jost(34, "Regular"), GRIS, w)
    y += 48
    centro(d, y, "Garantía de 3 años · Envío gratis a península", jost(34, "Regular"), GRIS, w)
    return capa


def movimiento(t):
    """(desplazamiento vertical del collar en px, ángulo de la lágrima en grados)."""
    if t < BAJADA:   # la mano baja la cadena, cada vez algo más rápido, y para en seco
        u = t / BAJADA
        return -RECORRIDO * (1 - u ** 1.25), 0.0
    s = t - BAJADA   # el golpe: la cadena estira un poco y vuelve; la lágrima sigue balanceándose
    rebote = 20 * math.exp(-s / 0.22) * math.sin(2 * math.pi * 2.6 * s)
    angulo = 7.5 * math.exp(-s / 0.75) * math.sin(2 * math.pi * 1.35 * s) \
        + 2.0 * math.exp(-s / 0.18) * math.sin(2 * math.pi * 4.0 * s)
    return rebote, angulo


def fotograma(t, w, h, base, colg, capa_texto):
    lienzo = Image.new("RGB", (w, h), FONDO)
    dy, ang = movimiento(t)
    bx = round(540 - PIVOTE[0] * ESCALA)                 # la lágrima en el centro
    by = round(880 - 2434 * ESCALA + dy)                 # punta de la lágrima en y=880 en reposo
    lienzo.paste(base, (bx, by))
    # la lágrima gira alrededor del pivote (en coordenadas de la capa)
    px, py = (PIVOTE[0] - COLG[0]) * ESCALA, (PIVOTE[1] - COLG[1]) * ESCALA
    margen = 80
    capa = Image.new("RGBA", (colg.width + 2 * margen, colg.height + 2 * margen), (0, 0, 0, 0))
    capa.paste(colg, (margen, margen))
    capa = capa.rotate(ang, resample=Image.Resampling.BICUBIC, center=(px + margen, py + margen))
    lienzo.paste(capa, (round(bx + COLG[0] * ESCALA - margen), round(by + COLG[1] * ESCALA - margen)), capa)
    # el texto entra cuando el collar ya ha parado
    a = min(max((t - BAJADA - 0.35) / 0.6, 0), 1)
    if a > 0:
        a = a * a * (3 - 2 * a)
        capa_t = capa_texto.copy()
        capa_t.putalpha(capa_t.getchannel("A").point(lambda v: round(v * a)))
        lienzo.paste(capa_t, (0, round(18 * (1 - a))), capa_t)
    return lienzo


def video(w, h, salida):
    base, colg = preparar()
    capa_texto = texto(w)
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    proc = subprocess.Popen([ff, "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w}x{h}",
                             "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-crf", "16", "-preset", "slow",
                             "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(SALIDA / salida)],
                            stdin=subprocess.PIPE)
    for i in range(round(DURACION * FPS)):
        proc.stdin.write(fotograma(i / FPS, w, h, base, colg, capa_texto).tobytes())
    proc.stdin.close()
    proc.wait()
    print(SALIDA / salida)


if __name__ == "__main__":
    video(1080, 1920, "23-cierre-anim-9x16.mp4")
    video(1080, 1350, "23-cierre-anim-4x5.mp4")
