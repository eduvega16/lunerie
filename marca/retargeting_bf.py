"""Anuncio de retargeting del Black Friday (12-nov, idea de Edu): para quien añadió el Collar Signé al carrito y no
compró. Es la animación del anuncio 23 (el collar baja, rebota y la lágrima se balancea; foto real, sin IA) con un
texto que responde a «¿espero al Black Friday?» y, abajo, dos piezas más de la tienda en foto de producto QUIETA
(Reloj Lune y anillo Nuit) para que se vea que hay más cosas en la web.
    python marca/retargeting_bf.py  → marca/fotos-ia/campana-bf/30-retargeting-9x16.mp4 y -4x5.mp4 (+ portada .jpg)
Precios leídos de la tienda el 12-nov (/products/<handle>.js): Lune 39,95 € · Nuit 19,95 € · Signé 49,95 €.
En 9:16 todo queda dentro de la zona libre de Meta (y 270-1248 y 6 % a cada lado).
Solo cosas verdaderas: la promo ya está activa hasta el 5-dic; el plazo es solo lo que tarda en salir.
"""
import pathlib, subprocess, sys
from PIL import Image, ImageDraw, ImageFilter
import imageio_ffmpeg

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import cierre_animado as ca
from mofu_bofu import SALIDA, FONDO, TINTA, GRIS, ORO, ROJO, jost, corm, cormi, centro, mixto

FOTOS = pathlib.Path(__file__).resolve().parent / "fotos-ia" / "retargeting"
PIEZAS = [  # (foto, recorte 4:5 en la foto original, nombre, precio)
    ("lune.jpg", (562, 680, 1322, 1630), "Reloj Lune", "39,95 €"),
    ("nuit.jpg", (100, 125, 1500, 1875), "Anillo Nuit", "19,95 €"),
]
FPS, DURACION = 30, 7.5
T_TEXTO, T_PIEZAS = ca.BAJADA + 0.35, ca.BAJADA + 1.25

FORMATOS = {
    # escala del collar, y de la punta de la lágrima, y del texto, y de la fila de piezas, alto de la foto de cada pieza
    "9x16": dict(w=1080, h=1920, escala=0.30, punta=664, y_texto=694, y_piezas=962, foto_h=196),
    "4x5": dict(w=1080, h=1350, escala=0.36, punta=640, y_texto=672, y_piezas=1010, foto_h=230),
}


def capa_texto(w, h, y):
    capa = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    centro(d, y, "EL BLACK FRIDAY YA HA EMPEZADO", jost(28, "Medium"), ROJO, w, espaciado=5)
    y += 44
    mixto(d, y, [("Su nombre, ", corm(84), TINTA), ("su piedra.", cormi(84), TINTA)], w)
    y += 102
    centro(d, y, "La 2.ª pieza al 50 % y la 3.ª, gratis.", jost(40, "Regular"), TINTA, w)
    y += 56
    centro(d, y, "Hasta el 5 de diciembre · Sale en 3-5 días laborables", jost(30, "Regular"), GRIS, w)
    return capa


def redondear(im, radio):
    m = Image.new("L", im.size, 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, im.width - 1, im.height - 1), radio, fill=255)
    out = im.convert("RGBA")
    out.putalpha(m)
    return out


def capa_piezas(w, h, y, foto_h):
    """Etiqueta «También en lunerie.es» y dos tarjetas: foto de producto a la izquierda, nombre y precio a la derecha."""
    capa = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    centro(d, y, "TAMBIÉN EN LUNERIE.ES", jost(24, "Medium"), ORO, w, espaciado=6)
    y += 46
    foto_w = round(foto_h * 4 / 5)
    tarjeta_w, sep = 430, 40
    x = (w - (2 * tarjeta_w + sep)) // 2
    for archivo, caja, nombre, precio in PIEZAS:
        # fondo de la tarjeta (blanco, recto con esquinas suaves) y sombra muy ligera
        sombra = Image.new("RGBA", (tarjeta_w + 60, foto_h + 60), (0, 0, 0, 0))
        ImageDraw.Draw(sombra).rounded_rectangle((30, 36, tarjeta_w + 30, foto_h + 36), 18, fill=(22, 32, 27, 30))
        sombra = sombra.filter(ImageFilter.GaussianBlur(12))
        capa.alpha_composite(sombra, (x - 30, y - 30))
        ImageDraw.Draw(capa).rounded_rectangle((x, y, x + tarjeta_w, y + foto_h), 18, fill=(255, 255, 255, 255))
        foto = Image.open(FOTOS / archivo).convert("RGB").crop(caja).resize((foto_w, foto_h), Image.Resampling.LANCZOS)
        capa.alpha_composite(redondear(foto, 18), (x, y))
        d = ImageDraw.Draw(capa)
        tx = x + foto_w + 26
        d.text((tx, y + foto_h / 2 - 50), nombre, font=corm(40), fill=TINTA)
        d.text((tx, y + foto_h / 2 + 8), precio, font=jost(30, "Regular"), fill=GRIS)
        x += tarjeta_w + sep
    return capa


def aparecer(capa, t, t0, dur=0.6, sube=18):
    a = min(max((t - t0) / dur, 0), 1)
    if a <= 0:
        return None, 0
    a = a * a * (3 - 2 * a)
    c = capa.copy()
    c.putalpha(c.getchannel("A").point(lambda v: round(v * a)))
    return c, round(sube * (1 - a))


def mascara_bordes(im, borde=90):
    """Alfa que funde los lados y el borde de abajo de la foto con el fondo (a esta escala la foto no llena el ancho)."""
    import numpy as np
    w, h = im.size
    x = np.minimum(np.arange(w), np.arange(w)[::-1]) / borde
    y = (h - 1 - np.arange(h)) / (borde / 3)
    a = np.clip(np.minimum(x[None, :], y[:, None]), 0, 1)
    a = a * a * (3 - 2 * a)
    return Image.fromarray((a * 255).astype("uint8"))


def fotograma(t, f, base, colg, texto, piezas, alfa_base):
    w, h, esc = f["w"], f["h"], f["escala"]
    lienzo = Image.new("RGB", (w, h), FONDO)
    dy, ang = ca.movimiento(t)
    bx = round(w / 2 - ca.PIVOTE[0] * esc)
    by = round(f["punta"] - 2434 * esc + dy)
    lienzo.paste(base, (bx, by), alfa_base)
    px, py = (ca.PIVOTE[0] - ca.COLG[0]) * esc, (ca.PIVOTE[1] - ca.COLG[1]) * esc
    margen = 80
    capa = Image.new("RGBA", (colg.width + 2 * margen, colg.height + 2 * margen), (0, 0, 0, 0))
    capa.paste(colg, (margen, margen))
    capa = capa.rotate(ang, resample=Image.Resampling.BICUBIC, center=(px + margen, py + margen))
    lienzo.paste(capa, (round(bx + ca.COLG[0] * esc - margen), round(by + ca.COLG[1] * esc - margen)), capa)
    for c, t0 in ((texto, T_TEXTO), (piezas, T_PIEZAS)):
        capa_t, sube = aparecer(c, t, t0)
        if capa_t is not None:
            lienzo.paste(capa_t, (0, sube), capa_t)
    return lienzo


def video(nombre, f, zona=False):
    ca.ESCALA = f["escala"]
    base, colg = ca.preparar()
    texto = capa_texto(f["w"], f["h"], f["y_texto"])
    piezas = capa_piezas(f["w"], f["h"], f["y_piezas"], f["foto_h"])
    alfa_base = mascara_bordes(base)
    salida = SALIDA / f"30-retargeting-{nombre}.mp4"
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    proc = subprocess.Popen([ff, "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
                             "-s", f"{f['w']}x{f['h']}", "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-crf", "16",
                             "-preset", "slow", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(salida)],
                            stdin=subprocess.PIPE)
    for i in range(round(DURACION * FPS)):
        proc.stdin.write(fotograma(i / FPS, f, base, colg, texto, piezas, alfa_base).tobytes())
    proc.stdin.close()
    proc.wait()
    final = fotograma(DURACION, f, base, colg, texto, piezas, alfa_base)
    final.save(SALIDA / f"30-retargeting-{nombre}.jpg", quality=97, subsampling=0)
    if zona and f["h"] > 1500:   # comprobación: la zona libre de Meta pintada encima
        z = final.copy()
        d = ImageDraw.Draw(z)
        d.rectangle((round(f["w"] * 0.06), 270, round(f["w"] * 0.94), 1248), outline=(255, 0, 0), width=3)
        z.save(FOTOS / f"zona-{nombre}.jpg", quality=90)
    print(salida)


if __name__ == "__main__":
    for nombre, f in FORMATOS.items():
        video(nombre, f, zona=True)
