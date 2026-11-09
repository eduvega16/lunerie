"""Reel «¿Qué nombre pone?» (idea «mensaje tapado» de biblioteca/ideas-reels.json, opción B; OK de Edu, 9-nov):
hueco de curiosidad con el nombre. El Collar Signé baja con el nombre borroso y la pregunta debajo; rebota, la lágrima se
balancea, el nombre se enfoca («Carmen») y entra el texto del cierre. Foto real animada por partes, sin IA (como
marca/cierre_animado.py, del que usa el recorte de la lágrima y el texto).
    python marca/reel_nombre_tapado.py  → marca/fotos-ia/campana-bf/26-nombre-tapado-9x16.mp4 y -4x5.mp4
Sin sonido: la música se pone en Instagram o la pone Meta. En 9:16 todo dentro de la zona libre (y 270-1248).
"""
import math, subprocess
from PIL import Image, ImageDraw, ImageFilter
import imageio_ffmpeg
from mofu_bofu import SALIDA, FONDO, TINTA, corm, cormi, centro, jost, GRIS
from cierre_animado import preparar, texto, ESCALA, COLG, PIVOTE

FPS, DURACION = 30, 8.5
INICIO, BAJADA, RECORRIDO = 0.5, 1.6, 1150      # empieza a bajar a los 0,5 s y tarda 1,6 s
ENFOQUE = (3.6, 4.5)                             # el nombre pasa de borroso a nítido
SALE_PREG, ENTRA_CIERRE = (4.7, 5.1), (5.15, 5.7)   # primero se va la pregunta y luego entra el cierre
NOMBRE = (690, 1060, 1340, 1800)                 # caja del nombre «Carmen» en la foto original
BORROSO = 16                                     # radio del desenfoque (px a escala)


def movimiento(t):
    if t < INICIO:
        return -RECORRIDO, 0.0
    if t < INICIO + BAJADA:
        u = (t - INICIO) / BAJADA
        return -RECORRIDO * (1 - u ** 1.25), 0.0
    s = t - INICIO - BAJADA
    rebote = 20 * math.exp(-s / 0.22) * math.sin(2 * math.pi * 2.6 * s)
    angulo = 8 * math.exp(-s / 0.9) * math.sin(2 * math.pi * 1.3 * s) \
        + 2.0 * math.exp(-s / 0.18) * math.sin(2 * math.pi * 4.0 * s)
    return rebote, angulo


def suave(t, a, b):
    u = min(max((t - a) / (b - a), 0), 1)
    return u * u * (3 - 2 * u)


def pregunta(w):
    capa = Image.new("RGBA", (w, 1350), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    centro(d, 960, "¿Qué nombre pone?", cormi(104), TINTA, w)
    centro(d, 1100, "Mira bien el collar", jost(36, "Regular"), GRIS, w)
    return capa


def con_alfa(capa, a):
    c = capa.copy()
    c.putalpha(c.getchannel("A").point(lambda v: round(v * a)))
    return c


def fotograma(t, w, h, base, colg, mascara, caja, capa_preg, capa_cierre):
    lienzo = Image.new("RGB", (w, h), FONDO)
    dy, ang = movimiento(t)
    bx = round(540 - PIVOTE[0] * ESCALA)
    by = round(880 - 2434 * ESCALA + dy)
    b = base
    r = BORROSO * (1 - suave(t, *ENFOQUE))
    if r > 0.3:   # desenfoque solo en el nombre, con borde suave
        b = base.copy()
        trozo = base.crop(caja).filter(ImageFilter.GaussianBlur(r))
        b.paste(trozo, caja[:2], mascara)
    lienzo.paste(b, (bx, by))
    px, py = (PIVOTE[0] - COLG[0]) * ESCALA, (PIVOTE[1] - COLG[1]) * ESCALA
    m = 80
    capa = Image.new("RGBA", (colg.width + 2 * m, colg.height + 2 * m), (0, 0, 0, 0))
    capa.paste(colg, (m, m))
    capa = capa.rotate(ang, resample=Image.Resampling.BICUBIC, center=(px + m, py + m))
    lienzo.paste(capa, (round(bx + COLG[0] * ESCALA - m), round(by + COLG[1] * ESCALA - m)), capa)
    sale, entra = suave(t, *SALE_PREG), suave(t, *ENTRA_CIERRE)
    if sale < 1:
        c = con_alfa(capa_preg, 1 - sale)
        lienzo.paste(c, (0, 0), c)
    if entra > 0:
        c = con_alfa(capa_cierre, entra)
        lienzo.paste(c, (0, round(18 * (1 - entra))), c)
    return lienzo


def video(w, h, salida):
    base, colg = preparar()
    caja = tuple(round(v * ESCALA) for v in NOMBRE)
    ancho, alto = caja[2] - caja[0], caja[3] - caja[1]
    mascara = Image.new("L", (ancho, alto), 0)
    ImageDraw.Draw(mascara).rounded_rectangle((18, 18, ancho - 18, alto - 18), 60, fill=255)
    mascara = mascara.filter(ImageFilter.GaussianBlur(12))
    capa_preg, capa_cierre = pregunta(w), texto(w)
    proc = subprocess.Popen([imageio_ffmpeg.get_ffmpeg_exe(), "-y", "-loglevel", "error", "-f", "rawvideo",
                             "-pix_fmt", "rgb24", "-s", f"{w}x{h}", "-r", str(FPS), "-i", "-", "-c:v", "libx264",
                             "-crf", "16", "-preset", "slow", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
                             str(SALIDA / salida)], stdin=subprocess.PIPE)
    for i in range(round(DURACION * FPS)):
        proc.stdin.write(fotograma(i / FPS, w, h, base, colg, mascara, caja, capa_preg, capa_cierre).tobytes())
    proc.stdin.close()
    proc.wait()
    print(SALIDA / salida)


if __name__ == "__main__":
    video(1080, 1920, "26-nombre-tapado-9x16.mp4")
    video(1080, 1350, "26-nombre-tapado-4x5.mp4")
