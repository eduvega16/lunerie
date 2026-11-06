"""Reel con material REAL (fotos y vídeos del móvil de Edu, 6-nov): la muestra «Marta» del Collar Signé.
Cortes secos, texto corto en Jost y tarjeta final (la de ugc_montaje.py). Sin música (se pone en Instagram) y sin
metadatos del iPhone. Sin créditos de IA.
    python marca/reel_muestra.py            → marca/fotos-ia/reel-muestra/reel-muestra-9x16.mp4
Material en marca/referencias-reales/muestra-marta/ (fotos 1-12 y vídeos IMG_8671/8672, en el orden que mandó Edu).
"""
import pathlib, subprocess, sys, tempfile
from PIL import Image, ImageEnhance

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from ugc_montaje import tarjeta, W, H   # misma tarjeta final que los UGC

RAIZ = pathlib.Path(__file__).resolve().parent.parent
MAT = RAIZ / "marca" / "referencias-reales" / "muestra-marta"
SALIDA = RAIZ / "marca" / "fotos-ia" / "reel-muestra"
FPS = 30

# (tipo, fuente, duración, recorte, texto, y del texto)
#  foto: recorte (x0, y0, ancho) en la foto original, en 9:16; zoom lento hacia dentro
#  video: recorte (x0, y0, ancho) en el vídeo ya girado (1080x1920), inicio en s
#  texto: líneas separadas por «|»; y entre 270 y 1248 (zona que no tapan los botones de Instagram)
PLANOS = [
    ("foto", "foto-10.jpg", 2.3, (300, 700, 740), "Antes de venderlo,|pedimos uno.", 1040),
    ("video", ("IMG_8672.mov", 1.4), 2.5, (150, 420, 675), "Su nombre,|en chapa pulida.", 1040),
    ("foto", "foto-06.jpg", 2.5, (150, 0, 1134), "Y la piedra de su mes.", 330),
    ("video", ("IMG_8671.mov", 6.0), 2.2, (120, 410, 720), "Sin filtros.", 330),
    ("final", "foto-04.jpg", 2.8, (150, 0, 1134), None, 0),
]


def rotulo(texto, destino):
    """Como subtitulo() de ugc_montaje.py (Jost SemiBold blanco con sombra), pero con los cortes de línea a mano."""
    from PIL import ImageDraw, ImageFilter
    from ugc_montaje import jost
    f, lineas = jost(66, "SemiBold"), texto.split("|")
    im = Image.new("RGBA", (W, 96 * len(lineas) + 40), (0, 0, 0, 0))
    sombra = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ds, d = ImageDraw.Draw(sombra), ImageDraw.Draw(im)
    for i, l in enumerate(lineas):
        x = (W - d.textlength(l, font=f)) / 2
        ds.text((x, 20 + i * 96), l, font=f, fill=(0, 0, 0, 190))
        d.text((x, 20 + i * 96), l, font=f, fill=(255, 255, 255, 255))
    Image.alpha_composite(sombra.filter(ImageFilter.GaussianBlur(7)), im).save(destino)


def recorte_foto(ruta, caja, oscurecer=False):
    x0, y0, ancho = caja
    alto = round(ancho * 16 / 9)
    im = Image.open(ruta).convert("RGB").crop((x0, y0, x0 + ancho, y0 + alto))
    im = im.resize((W * 2, H * 2), Image.LANCZOS)          # el doble, para que el zoom no tiemble
    if oscurecer:
        im = ImageEnhance.Brightness(im).enhance(0.62)
    return im


def plano(tmp, i, p):
    tipo, fuente, dur, caja, texto, ytexto = p
    out = tmp / f"p{i}.mp4"
    frames = round(dur * FPS)
    if tipo in ("foto", "final"):
        png = tmp / f"p{i}.png"
        recorte_foto(MAT / fuente, caja, oscurecer=(tipo == "final")).save(png)
        vf = (f"zoompan=z='1+0.07*on/{frames}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s={W}x{H}:fps={FPS}")
        ent = ["-loop", "1", "-t", f"{dur}", "-i", str(png)]
    else:
        nombre, inicio = fuente
        x0, y0, ancho = caja
        alto = round(ancho * 16 / 9)
        vf = f"crop={ancho}:{alto}:{x0}:{y0},scale={W}:{H}:flags=lanczos,fps={FPS}"
        ent = ["-ss", f"{inicio}", "-t", f"{dur}", "-i", str(MAT / nombre)]
    capas, filtro = [], f"[0:v]{vf},setsar=1,format=yuv420p[base]"
    if texto or tipo == "final":
        capa = tmp / f"t{i}.png"
        if tipo == "final":
            tarjeta(capa); y = 0
        else:
            rotulo(texto, capa); y = ytexto
        capas = ["-loop", "1", "-t", f"{dur}", "-i", str(capa)]
        filtro = (f"[0:v]{vf},setsar=1[b];[1:v]format=rgba,fade=in:st=0.12:d=0.25:alpha=1[t];"
                  f"[b][t]overlay=0:{y}:format=auto,format=yuv420p[base]")
    subprocess.run(["ffmpeg", "-v", "error", "-y", *ent, *capas, "-filter_complex", filtro, "-map", "[base]",
                    "-frames:v", str(frames), "-an", "-c:v", "libx264", "-crf", "16", "-preset", "slow",
                    "-r", str(FPS), str(out)], check=True)
    return out


def main():
    SALIDA.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as t:
        tmp = pathlib.Path(t)
        partes = [plano(tmp, i, p) for i, p in enumerate(PLANOS)]
        lista = tmp / "lista.txt"
        lista.write_text("".join(f"file '{p.as_posix()}'\n" for p in partes), encoding="utf-8")
        destino = SALIDA / "reel-muestra-9x16.mp4"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lista),
                        "-map_metadata", "-1", "-c:v", "libx264", "-crf", "17", "-preset", "slow",
                        "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(destino)], check=True)
        print(destino)


if __name__ == "__main__":
    main()
