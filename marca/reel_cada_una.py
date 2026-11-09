"""Reel «Un collar para cada una» (9-nov): las 4 fotos del carrusel (post-cada-una-1..4.jpg, con el texto del papel ya
escrito) en 9:16, con un acercamiento lento y cortes secos; arriba y abajo, la misma foto desenfocada. Sin IA ni sonido.
    python marca/reel_cada_una.py   → marca/fotos-ia/campana-bf/28-cada-una-9x16.mp4
"""
import pathlib, subprocess
import imageio_ffmpeg
from PIL import Image, ImageFilter

RAIZ = pathlib.Path(__file__).resolve().parent.parent
D = RAIZ / "marca" / "fotos-ia" / "cada-una"
DESTINO = RAIZ / "marca" / "fotos-ia" / "campana-bf" / "28-cada-una-9x16.mp4"
W, H, FPS, SEG = 1080, 1920, 30, 1.9


def fondo(foto):
    f = foto.resize((round(H * foto.width / foto.height), H), Image.LANCZOS)
    x = (f.width - W) // 2
    return f.crop((x, 0, x + W, H)).filter(ImageFilter.GaussianBlur(40)).point(lambda v: int(v * 0.8))


def main():
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    p = subprocess.Popen([ff, "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                          "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-crf", "16", "-preset", "slow",
                          "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(DESTINO)], stdin=subprocess.PIPE)
    for i in range(1, 5):
        foto = Image.open(D / f"post-cada-una-{i}.jpg").convert("RGB")
        base = fondo(foto)
        n = round(SEG * FPS)
        for k in range(n):
            z = 1.0 + 0.06 * k / n                              # acercamiento lento
            ancho = round(W * z); alto = round(ancho * 1.25)
            f = foto.resize((ancho, alto), Image.LANCZOS)
            cuadro = base.copy()
            visible = f.crop(((ancho - W) // 2, (alto - 1350) // 2, (ancho - W) // 2 + W, (alto - 1350) // 2 + 1350))
            cuadro.paste(visible, (0, (H - 1350) // 2))
            p.stdin.write(cuadro.tobytes())
    p.stdin.close(); p.wait()
    print(DESTINO)


if __name__ == "__main__":
    main()
