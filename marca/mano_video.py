"""Vídeo corto del Collar Signé colgando de los dedos con un balanceo suave (10-nov, Edu: «un vídeo del collar en la mano
moviéndose», con Carmen o Marta), para la ficha (4:5) y para reels (9:16). Foto: marca/fotos-ia/cada-una/
mano-carmen-verde-2.png (IA, nombre revisado a tamaño real; de reserva mano-marta-verde-1.png). Kling 3.0 pro por la API
de Higgsfield; mirar los fotogramas: si el nombre se deforma, usar solo el tramo bueno.
    python marca/mano_video.py animar [--seg 5] [--foto <png>]   → marca/fotos-ia/mano/<foto>.mp4
    python marca/mano_video.py montar <ini> <dur> [--foto <png>]  → mano-ficha-4x5.mp4 y mano-9x16.mp4 (ida y vuelta)
"""
import pathlib, subprocess, sys, urllib.request
import imageio_ffmpeg
from dotenv import load_dotenv
from PIL import Image

RAIZ = pathlib.Path(__file__).resolve().parent.parent
load_dotenv(RAIZ / ".env.local")
import higgsfield_client  # noqa: E402

FOTOS = RAIZ / "marca" / "fotos-ia" / "cada-una"
SALIDA = RAIZ / "marca" / "fotos-ia" / "mano"
PROMPT = ("A very gentle, slow sway: the necklace hanging from her fingers swings slightly left and right like a soft "
          "pendulum, the green crystal catching small sparkles of sunlight, the dappled light on the wall moving softly. "
          "The hand stays almost still. The necklace keeps exactly its shape: the gold name stays rigid, flat and "
          "perfectly readable the whole time, the crystal keeps its size. Static camera, real footage, no zoom.")


def animar(foto, seg):
    SALIDA.mkdir(parents=True, exist_ok=True)
    jpg = SALIDA / f"{foto}-916.jpg"
    im = Image.open(FOTOS / f"{foto}.png").convert("RGB")
    w, h = im.size
    ancho = round(h * 9 / 16)
    im.crop(((w - ancho) // 2, 0, (w - ancho) // 2 + ancho, h)).save(jpg, quality=95)
    r = higgsfield_client.subscribe("kling-video/v3.0/pro/image-to-video", arguments={
        "image_url": higgsfield_client.upload_file(jpg), "prompt": PROMPT, "duration": seg, "sound": "off",
        "aspect_ratio": "9:16"})
    v = (r or {}).get("video") or ((r or {}).get("videos") or [None])[0]
    url = v.get("url") if isinstance(v, dict) else v
    if not url:
        sys.exit(f"SIN VÍDEO {r}")
    destino = SALIDA / f"{foto}.mp4"
    urllib.request.urlretrieve(url, destino)
    print(destino)


def montar(foto, ini, dur):
    """Tramo bueno [ini, ini+dur] en ida y vuelta (bucle sin salto); 4:5 para la ficha y 9:16 para reels."""
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    src = SALIDA / f"{foto}.mp4"
    for nombre, filtro in (("mano-9x16.mp4", "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920"),
                           ("mano-ficha-4x5.mp4", "scale=1080:1920:force_original_aspect_ratio=increase,"
                                                  "crop=1080:1350:0:60")):
        g = (f"[0:v]trim={ini}:{ini + dur},setpts=PTS-STARTPTS,fps=30,{filtro},split[a][b];[b]reverse[r];"
             f"[a][r]concat=n=2:v=1:a=0,format=yuv420p[v]")
        subprocess.run([ff, "-loglevel", "error", "-y", "-i", str(src), "-filter_complex", g, "-map", "[v]",
                        "-c:v", "libx264", "-crf", "17", "-preset", "slow", "-movflags", "+faststart", "-an",
                        str(SALIDA / nombre)], check=True)
        print(SALIDA / nombre)


if __name__ == "__main__":
    a = sys.argv[1:]
    foto = a[a.index("--foto") + 1] if "--foto" in a else "mano-carmen-verde-2"
    if a[:1] == ["animar"]:
        animar(foto, int(a[a.index("--seg") + 1]) if "--seg" in a else 5)
    elif a[:1] == ["montar"]:
        montar(foto, float(a[1]), float(a[2]))
    else:
        print(__doc__)
