"""Monta el UGC «abrir la cajita» del Collar Signé (anuncio 31, 13-nov): los 8 clips de Kling (ugc_animar.py --carpeta
ugc-lucce) con el ritmo del anuncio de Lucce Jewelry (oficina/referencias/lucce-2026-11-12/planos.jpg), un texto de
gancho al principio y el cierre animado con la cajita (cierre_animado.py --cajita). Sin voz; música baja.
    python marca/ugc_lucce_montaje.py [--sin-texto] [--sin-musica]
        → marca/fotos-ia/ugc-lucce/31-ugc-cajita-9x16.mp4 y -4x5.mp4
De cada clip se usa solo el principio (Kling deforma el nombre a partir de ~2,5-3 s).
En 9:16, el texto va dentro de la zona libre de Meta (y 270-1248).
"""
import pathlib, shutil, subprocess, sys, tempfile
from PIL import Image, ImageDraw, ImageFilter
from mofu_bofu import jost

RAIZ = pathlib.Path(__file__).resolve().parent.parent
CARPETA = RAIZ / "marca" / "fotos-ia" / "ugc-lucce"
CLIPS = CARPETA / "clips"
CIERRE = RAIZ / "marca" / "fotos-ia" / "campana-bf" / "31-cierre-cajita-{}.mp4"
MUSICA = RAIZ / "marca" / "musica" / "holiday-bells.m4a"
FF = shutil.which("ffmpeg") or __import__("imageio_ffmpeg").get_ffmpeg_exe()
FPS = 30

# (clip, inicio, duración, desplazamiento del recorte 4:5: 0 = arriba, 1 = abajo)
PLANOS = [
    ("caja-cara-2", 0.0, 1.6, 0.55),
    ("caja-mano-2", 0.0, 3.0, 0.45),
    ("delante-4", 0.0, 2.1, 0.40),
    ("colgando-1", 0.0, 2.5, 0.30),
    ("abrochar-2", 0.0, 1.7, 0.55),    # a partir de ~1,8 s Kling le cambia la cara
    ("pellizco-2", 0.0, 1.6, 0.45),    # después la lágrima se va hacia los dedos
    ("pecho-1", 0.0, 1.4, 0.45),
    ("ancla-2", 2.3, 1.6, 0.60),       # el final: manos enmarcando el collar y sonrisa (al principio cruza una mano borrosa)
]
# texto de gancho: (desde, hasta, texto, y en 9:16). Nada en primera persona de la chica (no es una clienta real).
TEXTOS = [(0.0, 4.6, "Así llega su collar", 300)]


def capa_texto(texto, w, h, y):
    """Texto blanco con sombra suave, centrado, en una capa RGBA del tamaño del vídeo."""
    f = jost(66, "Medium")
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    sombra = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    x = (w - ImageDraw.Draw(im).textlength(texto, font=f)) / 2
    ImageDraw.Draw(sombra).text((x, y), texto, font=f, fill=(0, 0, 0, 150))
    ImageDraw.Draw(im).text((x, y), texto, font=f, fill=(255, 255, 255, 255))
    return Image.alpha_composite(sombra.filter(ImageFilter.GaussianBlur(7)), im)


def montar(formato, con_texto=True, con_musica=True):
    w, h = 1080, 1920 if formato == "9x16" else 1350
    tmp = pathlib.Path(tempfile.mkdtemp())
    entradas, filtros, nombres = [], [], []
    for i, (clip, ini, dur, desp) in enumerate(PLANOS):
        entradas += ["-ss", str(ini), "-t", str(dur), "-i", str(CLIPS / f"{clip}.mp4")]
        f = f"[{i}:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps={FPS},setsar=1"
        if formato == "4x5":
            f += f",crop=1080:1350:0:{round((1920 - 1350) * desp)}"
        filtros.append(f + ",setpts=PTS-STARTPTS" + f"[v{i}]")
        nombres.append(f"[v{i}]")
    n = len(PLANOS)
    entradas += ["-i", str(CIERRE).format(formato)]
    filtros.append(f"[{n}:v]fps={FPS},setsar=1,setpts=PTS-STARTPTS[v{n}]")
    nombres.append(f"[v{n}]")
    filtros.append("".join(nombres) + f"concat=n={n + 1}:v=1:a=0[base]")
    actual, k = "[base]", n + 1
    if con_texto:
        for j, (desde, hasta, texto, y) in enumerate(TEXTOS):
            png = tmp / f"texto-{j}.png"
            capa_texto(texto, w, h, y if formato == "9x16" else 90).save(png)
            entradas += ["-loop", "1", "-i", str(png)]
            filtros.append(f"{actual}[{k}:v]overlay=0:0:shortest=1:enable='between(t,{desde},{hasta})'[t{j}]")
            actual, k = f"[t{j}]", k + 1
    total = sum(p[2] for p in PLANOS) + 6.5
    filtros.append(f"{actual}fade=t=out:st={total - 0.3}:d=0.3[out]")
    audio = ["-an"]
    if con_musica:
        entradas += ["-i", str(MUSICA)]
        filtros.append(f"[{k}:a]volume=0.55,afade=t=in:st=0:d=0.4,afade=t=out:st={total - 1.2}:d=1.2[aud]")
        audio = ["-map", "[aud]", "-c:a", "aac", "-b:a", "192k"]
    salida = CARPETA / f"31-ugc-cajita-{formato}.mp4"
    subprocess.run([FF, "-y", "-loglevel", "error", *entradas, "-filter_complex", ";".join(filtros), "-map", "[out]",
                    *audio, "-t", str(total), "-c:v", "libx264", "-crf", "18", "-preset", "slow", "-pix_fmt", "yuv420p",
                    "-movflags", "+faststart", str(salida)], check=True)
    print(f"{salida} ({total:.1f} s)")


if __name__ == "__main__":
    a = sys.argv[1:]
    for formato in ("9x16", "4x5"):
        montar(formato, "--sin-texto" not in a, "--sin-musica" not in a)
