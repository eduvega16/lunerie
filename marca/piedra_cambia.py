"""Collar en la mano con la lágrima cambiando de color mes a mes (11-nov-2026, idea de Edu visto en Lucce Jewelry).

Sin IA: la foto «Marta» en la mano (mano-marta-tcorta-1.png, lágrima verde) y la lágrima se tiñe con el color de cada
mes conservando sus facetas y brillos (se pasa a luminancia y se pinta con un degradado oscuro → claro del color, sacado
de las gotas reales de marca/fotos-ia/lagrimas/lagrima-NN.png). El nombre, la cadena y las garras no se tocan.

    python marca/piedra_cambia.py   →  marca/videos-ficha/collar-piedra-mes.mp4 (4:5, 1080 × 1350, en bucle) + .jpg
"""
import subprocess
import sys
from pathlib import Path

import imageio_ffmpeg
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

RAIZ = Path(__file__).resolve().parent.parent
FOTO = RAIZ / "marca" / "fotos-ia" / "cada-una" / "mano-marta-tcorta-1.png"   # 1520 × 2688
GOTAS = RAIZ / "marca" / "fotos-ia" / "lagrimas"
SALIDA = RAIZ / "marca" / "videos-ficha" / "collar-piedra-mes.mp4"
CAJA = (870, 1580, 1070, 1840)          # alrededor de la lágrima verde (medida por color: x 892-1044, y 1600-1818)
RECORTE = (150, 880, 1250, 2255)        # 4:5 más cerca: el nombre y la lágrima
MESES = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
         "Noviembre", "Diciembre"]
FPS, POR_MES, FUNDIDO = 30, 1.0, 0.25


def color_mes(n):
    g = np.asarray(Image.open(GOTAS / f"lagrima-{n:02d}.png").convert("RGBA")).astype(float)
    a = g[..., 3] > 200
    rgb = g[..., :3][a]
    # el color de la piedra sin los brillos blancos ni las sombras: los píxeles más saturados (mediana)
    sat = rgb.max(axis=1) - rgb.min(axis=1)
    return np.median(rgb[sat >= np.percentile(sat, 60)], axis=0)


def main():
    im = np.asarray(Image.open(FOTO).convert("RGB")).astype(float)
    x0, y0, x1, y1 = CAJA
    zona = im[y0:y1, x0:x1]
    r, g, b = zona[..., 0], zona[..., 1], zona[..., 2]
    # máscara suave de la piedra: lo verde (las garras doradas tienen r > g y no entran)
    verde = np.clip((g - np.maximum(r, b) - 12) / 25, 0, 1)
    mascara = np.asarray(Image.fromarray((verde * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(3))
                         .filter(ImageFilter.GaussianBlur(1.2))).astype(float) / 255
    lum = (0.30 * r + 0.59 * g + 0.11 * b)
    piedra = lum[verde > .5]
    lo, hi = np.percentile(piedra, 3), np.percentile(piedra, 99)
    t = np.clip((lum - lo) / (hi - lo), 0, 1)[..., None]

    def tenida(color):
        oscuro, claro = color * 0.45, color + (255 - color) * 0.5
        nueva = oscuro + (claro - oscuro) * t ** 0.6   # la piedra verde es oscura: se aclara un poco el reparto
        nueva = nueva + (255 - nueva) * np.clip((t - .88) / .12, 0, 1) ** 2   # los destellos, casi blancos
        out = im.copy()
        out[y0:y1, x0:x1] = zona * (1 - mascara[..., None]) + nueva * mascara[..., None]
        return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)).crop(RECORTE).resize((1080, 1350), Image.LANCZOS)

    fuente = ImageFont.truetype(str(RAIZ / "marca" / "fuentes" / "Cormorant-Italic.ttf"), 76)
    cuadros = []
    for n in range(1, 13):
        c = tenida(color_mes(n))
        d = ImageDraw.Draw(c)
        texto = MESES[n - 1]
        w = d.textlength(texto, font=fuente)
        sombra = Image.new("RGBA", c.size, (0, 0, 0, 0))
        ImageDraw.Draw(sombra).text(((1080 - w) / 2, 1215), texto, font=fuente, fill=(0, 0, 0, 170))
        sombra = sombra.filter(ImageFilter.GaussianBlur(7))
        c.paste(sombra, (0, 0), sombra)
        d = ImageDraw.Draw(c)
        d.text(((1080 - w) / 2, 1215), texto, font=fuente, fill=(255, 255, 255))
        cuadros.append(c)

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    esc = imageio_ffmpeg.write_frames(str(SALIDA), (1080, 1350), fps=FPS, quality=8, macro_block_size=2,
                                      output_params=["-movflags", "+faststart"])
    esc.send(None)
    quieto, fundido = int((POR_MES - FUNDIDO) * FPS), int(FUNDIDO * FPS)
    for i, c in enumerate(cuadros):
        sig = cuadros[(i + 1) % 12]
        for _ in range(quieto):
            esc.send(c.tobytes())
        for k in range(fundido):
            esc.send(Image.blend(c, sig, (k + 1) / (fundido + 1)).tobytes())
    esc.close()
    cuadros[4].save(SALIDA.with_suffix(".jpg"), quality=90)   # mayo (verde): la foto mientras carga
    hoja = Image.new("RGB", (6 * 270, 2 * 338))
    for i, c in enumerate(cuadros):
        hoja.paste(c.resize((270, 338)), ((i % 6) * 270, (i // 6) * 338))
    hoja.save(SALIDA.with_name("collar-piedra-mes-hoja.jpg"), quality=85)
    print(SALIDA)


if __name__ == "__main__":
    sys.exit(main())
