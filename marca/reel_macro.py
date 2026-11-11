"""Reel «de cerca» del Collar Signé (11-nov-2026), con la estructura del anuncio de Lucce Jewelry que describió Edu:
la chica poniéndose el collar → planos muy cerca del nombre y de la lágrima → transiciones de zoom y destello → oferta.

Sin IA nueva (0 €): clip de Kling ya hecho (la chica abrochándolo; solo los primeros 2,4 s, luego cambia la cara),
la foto de producto en 4K (el nombre siempre sale nítido), el vídeo de la mano y la lámina de las 12 lágrimas.

    python marca/reel_macro.py [--pvd | --oro18]   →  marca/fotos-ia/campana-bf/28-de-cerca-9x16.mp4 y -4x5.mp4

--oro18 solo cuando QIUHAN confirme por escrito el baño de oro de 18 quilates. Nunca «waterproof».
Texto dentro de la zona libre de Meta en 9:16 (y 270-1248, 6 % a los lados).
"""
import argparse
import subprocess
import sys
from pathlib import Path

import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFilter, ImageFont

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "marca"))   # cierre_animado y mofu_bofu
FOTOS = RAIZ / "marca" / "fotos-ia"
SALIDA = FOTOS / "campana-bf"
FUENTES = RAIZ / "marca" / "fuentes"
W, H, FPS = 1080, 1920, 30
TINTA, BLANCO = (22, 32, 27), (255, 255, 255)
FONDO_FOTO = (246, 248, 245)   # fondo de producto-verde-carmen-v2.jpg (medido)

PRODUCTO = FOTOS / "collar" / "producto-verde-carmen-v2.jpg"       # 2480 × 3100
CIERRE = FOTOS / "ugc-collar-carmen-2" / "clips" / "cierre-1.mp4"   # la chica abrochándolo
MANO = FOTOS / "mano" / "mano-marta-tcorta-1.mp4"                   # el de la ficha
LAGRIMAS = FOTOS / "lagrimas" / "lagrimas-12.jpg"
LOGO = RAIZ / "marca" / "logos" / "logo-tinta.png"


def fuente(nombre, tam):
    return ImageFont.truetype(str(FUENTES / nombre), tam)


def suave(x):
    x = max(0.0, min(1.0, x))
    return x * x * (3 - 2 * x)


# ---------- fuentes de imagen ----------
class Foto:
    """Encuadre que se mueve dentro de una foto grande: (cx, cy, ancho del recorte) al principio y al final."""
    def __init__(self, ruta, a, b):
        self.img = Image.open(ruta).convert("RGB")
        self.a, self.b = a, b

    def cuadro(self, p):
        p = suave(p)
        cx, cy, ancho = (self.a[i] + (self.b[i] - self.a[i]) * p for i in range(3))
        alto = ancho * H / W
        cx = min(max(cx, ancho / 2), self.img.width - ancho / 2)   # que el recorte no se salga de la foto
        cy = min(max(cy, alto / 2), self.img.height - alto / 2)
        caja =(cx - ancho / 2, cy - alto / 2, cx + ancho / 2, cy + alto / 2)
        return self.img.resize((W, H), Image.LANCZOS, box=caja)


class Video:
    def __init__(self, ruta, desde=0.0):
        r = imageio_ffmpeg.read_frames(str(ruta))
        meta = next(r)
        self.fps, tam = meta["fps"], meta["size"]
        self.cuadros = [Image.frombytes("RGB", tam, c) for c in r]
        self.desde = desde

    def en(self, t):
        i = min(int((self.desde + t) * self.fps), len(self.cuadros) - 1)
        c = self.cuadros[i]
        if c.size != (W, H):
            c = c.resize((W, H), Image.LANCZOS)
        return c


# ---------- texto ----------
def rotulo(img, lineas, y, color, sombra=False):
    """lineas: [(texto, fuente)], centradas desde y."""
    d = ImageDraw.Draw(img)
    for texto, f in lineas:
        ancho = d.textlength(texto, font=f)
        x = (W - ancho) / 2
        if sombra:
            capa = Image.new("RGBA", img.size, (0, 0, 0, 0))
            ImageDraw.Draw(capa).text((x, y + 3), texto, font=f, fill=(0, 0, 0, 120))
            img.paste(capa.filter(ImageFilter.GaussianBlur(6)), (0, 0), capa.filter(ImageFilter.GaussianBlur(6)))
            d = ImageDraw.Draw(img)
        d.text((x, y), texto, font=f, fill=color)
        y += f.size * 1.18
    return img


def aparece(t, entra=0.15):
    return suave(t / entra)


def con_texto(img, lineas, y, color, t, sombra=False):
    alfa = aparece(t)
    if alfa <= 0:
        return img
    capa = rotulo(img.copy(), lineas, y, color, sombra)
    return Image.blend(img, capa, alfa)


# ---------- transiciones ----------
def zoom(img, escala, desenfoque):
    if escala != 1:
        a, b = W / escala, H / escala
        img = img.resize((W, H), Image.LANCZOS, box=((W - a) / 2, (H - b) / 2, (W + a) / 2, (H + b) / 2))
    if desenfoque > 0.3:
        img = img.filter(ImageFilter.GaussianBlur(desenfoque))
    return img


def destello(img, x):
    return Image.blend(img, Image.new("RGB", img.size, BLANCO), max(0.0, min(1.0, x)))


def cierre_promo(acabado):
    """Texto bajo el collar que cae (cierre_animado.py; la lágrima acaba en y≈880): de y 930 a y≈1215, zona libre."""
    from mofu_bofu import GRIS, centro, cormi, jost
    capa = Image.new("RGBA", (W, 1350), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    y = 930
    centro(d, y, "El 3.º, gratis", cormi(110), TINTA, W)
    y += 128
    centro(d, y, "hasta el 5 de diciembre", jost(44, "Regular"), TINTA, W)
    y += 66
    centro(d, y, "Collar Signé · 49,95 €", jost(38, "Regular"), GRIS, W)
    y += 50
    centro(d, y, f"{acabado} · Garantía de 3 años", jost(34, "Regular"), GRIS, W)
    return capa


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--oro18", action="store_true", help="solo con la confirmación escrita de QIUHAN")
    args = ap.parse_args()
    acabado = "Baño de oro de 18K" if args.oro18 else "Acero con baño PVD"

    titular = fuente("Cormorant-Italic.ttf", 104)
    titular_g = fuente("Cormorant-Italic.ttf", 112)
    texto = fuente("Jost.ttf", 44)
    texto_p = fuente("Jost.ttf", 38)

    cierre = Video(CIERRE)
    mano = Video(MANO)
    # La foto mide 2480 × 3100 (medido por color): nombre de (680, 1100) a (1250, 1760); lágrima de (1265, 2000)
    # a (1500, 2390); debajo, su reflejo hasta y 2750
    nombre = Foto(PRODUCTO, (980, 1430, 900), (1000, 1420, 640))
    gota = Foto(PRODUCTO, (1380, 1930, 800), (1380, 1910, 600))   # texto arriba, entre los dos lados de la cadena
    # 11-nov (Edu): todo con el MISMO fondo que la foto de producto; la lámina (fondo 249) se tiñe para que su fondo
    # quede igual y no se vea un rectángulo de otro color
    lam = Image.open(LAGRIMAS).convert("RGB")
    lam = Image.merge("RGB", [c.point(lambda v, k=k: round(v * k)) for c, k in zip(lam.split(), [x / 249 for x in FONDO_FOTO])])
    lam_fondo = Image.new("RGB", (W, H), FONDO_FOTO)

    def lamina(p):
        esc = 1.12 - 0.12 * suave(p)
        a = int(W * 0.92 * esc)
        im = lam.resize((a, int(a * lam.height / lam.width)), Image.LANCZOS)
        f = lam_fondo.copy()
        f.paste(im, ((W - im.width) // 2, (H - im.height) // 2 + 60))
        return f

    # (duración, función(t, d) → imagen, entrada) — entrada: «zoom» o «destello»
    planos = [
        (2.4, lambda t, d: con_texto(sombra_arriba(cierre.en(t)), [("Te van a preguntar", titular), ("de dónde es.", titular)],
                                     330, BLANCO, t, sombra=True), None),
        (1.7, lambda t, d: con_texto(nombre.cuadro(t / d), [("Su nombre,", titular_g)], 330, TINTA, t - .2), "zoom"),
        (1.7, lambda t, d: con_texto(gota.cuadro(t / d), [("su piedra.", titular_g)], 330, TINTA, t - .2), "destello"),
        (2.7, lambda t, d: mano.en(t), "zoom"),          # 11-nov: más largos para que quepa la voz (doblar.py)
        (2.6, lambda t, d: lamina(t / d), "destello"),
        (4.6, lambda t, d: final(t), "zoom"),
    ]

    # Final (11-nov, Edu): el mismo que el de Sarah, el collar real cayendo con la lágrima balanceándose y la promo debajo
    import cierre_animado as caida
    base_caida, colg_caida = caida.preparar()
    capa_fin = cierre_promo(acabado)

    def final(t):
        return caida.fotograma(t, W, H, base_caida, colg_caida, capa_fin)

    # Degradado oscuro suave arriba para que el titular blanco se lea sobre el pelo y la luz de la ventana
    mascara = Image.new("L", (1, H))
    for y in range(H):
        mascara.putpixel((0, y), int(110 * max(0.0, 1 - y / 900)))
    mascara = mascara.resize((W, H))
    negro = Image.new("RGB", (W, H), (0, 0, 0))

    def sombra_arriba(img):
        return Image.composite(negro, img, mascara)

    SALIDA.mkdir(parents=True, exist_ok=True)
    s916 = SALIDA / "28-de-cerca-9x16.mp4"
    escritor = imageio_ffmpeg.write_frames(str(s916), (W, H), fps=FPS, quality=9, macro_block_size=8,
                                           output_params=["-pix_fmt", "yuv420p", "-preset", "slow"])
    escritor.send(None)
    TR = 0.2  # segundos de transición a cada lado del corte
    for i, (dur, f, entrada) in enumerate(planos):
        salida_sig = planos[i + 1][2] if i + 1 < len(planos) else None
        for n in range(int(dur * FPS)):
            t = n / FPS
            img = f(t, dur)
            if entrada == "zoom" and t < TR:
                x = 1 - t / TR
                img = zoom(img, 1 + .35 * x, 18 * x)
            if entrada == "destello" and t < TR:
                img = destello(img, 1 - t / TR)
            falta = dur - t
            if salida_sig == "zoom" and falta < TR:
                x = 1 - falta / TR
                img = zoom(img, 1 + .35 * x, 18 * x)
            if salida_sig == "destello" and falta < TR:
                img = destello(img, 1 - falta / TR)
            escritor.send(img.tobytes())
    escritor.close()

    # 4:5 de reserva (feed): recorte del centro, 1080 × 1350 desde y = 285 (el texto va entre 300 y 1240)
    s45 = SALIDA / "28-de-cerca-4x5.mp4"
    subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), "-v", "error", "-y", "-i", str(s916), "-vf", "crop=1080:1350:0:285",
                    "-c:v", "libx264", "-crf", "18", "-preset", "slow", "-pix_fmt", "yuv420p", str(s45)], check=True)
    print(s916, s45, sep="\n")


if __name__ == "__main__":
    sys.exit(main())
