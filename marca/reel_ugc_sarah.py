"""Reel UGC «Te van a preguntar de dónde es» con Sarah (la influencer morena, collar «Marta» con lágrima azul), 11-nov-2026.

Misma estructura que reel_macro.py (anuncio de Lucce), pero más UGC: los clips de Sarah grabados como con el móvil y
cortes rápidos con un pequeño zoom. Textos con el estilo del de cerca (Cormorant cursiva blanca con sombra suave) y, al
final, el collar real cayendo con la lágrima balanceándose (cierre_animado.py) con la promo debajo. 0 €: todo
postproducción con clips y fotos que ya teníamos.

    python marca/reel_ugc_sarah.py   →  marca/fotos-ia/campana-bf/29-ugc-sarah-9x16.mp4 y -4x5.mp4

«Baño de oro de 18K»: confirmado por QIUHAN por escrito (11-nov). Nunca «waterproof».
"""
import subprocess
import sys
from pathlib import Path

import imageio_ffmpeg
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from reel_macro import BLANCO, FOTOS, cierre_promo, FPS, H, SALIDA, W, Video, con_texto, destello, fuente, zoom  # noqa: E402
import cierre_animado as caida  # noqa: E402

CLIPS = FOTOS / "ugc-collar" / "clips"


def movil(img, t):
    """Un poco de vida de cámara en mano: zoom lento hacia dentro."""
    return zoom(img, 1.0 + 0.04 * t, 0)


def main():
    mirada, nombre, cuello, ancla = (Video(CLIPS / f"{n}-1.mp4") for n in ("mirada", "nombre", "cuello", "ancla"))
    titular = fuente("Cormorant-Italic.ttf", 104)

    # Degradado oscuro suave arriba para que el texto blanco se lea sobre el pelo y la ventana (como en el de cerca)
    mascara = Image.new("L", (1, H))
    for y in range(H):
        mascara.putpixel((0, y), int(120 * max(0.0, 1 - y / 950)))
    mascara = mascara.resize((W, H))
    negro = Image.new("RGB", (W, H), (0, 0, 0))

    def sarah(clip, desde, lineas):
        def f(t):
            img = Image.composite(negro, movil(clip.en(t + desde), t), mascara)
            return con_texto(img, [(l, titular) for l in lineas], 330, BLANCO, t - .1, sombra=True)
        return f

    base, colg = caida.preparar()
    capa_fin = cierre_promo("Baño de oro de 18K")   # el mismo final que el de cerca

    planos = [  # (duración, imagen(t), entrada)
        (2.3, sarah(mirada, 0, ["Te van a preguntar", "de dónde es."]), None),
        (2.0, sarah(nombre, .3, ["Lleva su nombre…"]), "zoom"),
        (2.0, sarah(cuello, .2, ["…y la piedra de su mes."]), "destello"),
        (2.0, sarah(ancla, 0, ["Baño de oro de 18K."]), "zoom"),
        (4.6, lambda t: caida.fotograma(t, W, H, base, colg, capa_fin), "destello"),
    ]

    s916 = SALIDA / "29-ugc-sarah-9x16.mp4"
    esc = imageio_ffmpeg.write_frames(str(s916), (W, H), fps=FPS, quality=9, macro_block_size=8,
                                      output_params=["-preset", "slow"])
    esc.send(None)
    TR = 0.15
    for i, (dur, f, entrada) in enumerate(planos):
        sig = planos[i + 1][2] if i + 1 < len(planos) else None
        for n in range(int(dur * FPS)):
            t = n / FPS
            img = f(t)
            if entrada == "zoom" and t < TR:
                x = 1 - t / TR
                img = zoom(img, 1 + .3 * x, 14 * x)
            if entrada == "destello" and t < TR:
                img = destello(img, 1 - t / TR)
            falta = dur - t
            if sig == "zoom" and falta < TR:
                x = 1 - falta / TR
                img = zoom(img, 1 + .3 * x, 14 * x)
            if sig == "destello" and falta < TR:
                img = destello(img, 1 - falta / TR)
            esc.send(img.tobytes())
    esc.close()

    s45 = SALIDA / "29-ugc-sarah-4x5.mp4"
    subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), "-v", "error", "-y", "-i", str(s916), "-vf", "crop=1080:1350:0:285",
                    "-c:v", "libx264", "-crf", "18", "-preset", "slow", "-pix_fmt", "yuv420p", str(s45)], check=True)
    print(s916, s45, sep="\n")


if __name__ == "__main__":
    sys.exit(main())
