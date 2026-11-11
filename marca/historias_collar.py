"""Vídeos de la fila «Así se lleva» de la ficha del Collar Signé (11-nov-2026, idea de Edu: como el «As Seen On You»
de otras tiendas, con estética de historias de Instagram).

Título honesto: son vídeos nuestros hechos con IA, no de clientas (nada de «As seen on you» ni «nuestras clientas»).
Clips de Kling ya hechos (0 €), recortados donde Kling aún no deforma la cara ni el nombre, a 540 × 960, sin sonido.

    python marca/historias_collar.py   →  marca/videos-ficha/collar-*.mp4 + .jpg, subidos a Archivos de Shopify;
                                          las URL quedan en marca/videos-ficha/collar-urls.json (las lee el tema)
"""
import json
import subprocess
import sys
from pathlib import Path

import imageio_ffmpeg

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "anuncios"))
from subir_creatividades import subir  # noqa: E402

FF = imageio_ffmpeg.get_ffmpeg_exe()
FOTOS = RAIZ / "marca" / "fotos-ia"
DESTINO = RAIZ / "marca" / "videos-ficha"
URLS = DESTINO / "collar-urls.json"
CLIPS = [  # (nombre, clip, segundos útiles). 11-nov (Edu): variados, sin repetir chica (antes salían Sarah y Carmen ×3)
    ("collar-sarah-mirada", FOTOS / "ugc-collar" / "clips" / "mirada-1.mp4", 4.0),
    ("collar-mano-marta", FOTOS / "mano" / "mano-marta-tcorta-1.mp4", 3.0),          # al final deforma el nombre
    ("collar-madre-hija-cuellos", FOTOS / "ugc-madre-hija" / "clips" / "cuellos-1.mp4", 3.5),
    ("collar-carmen-espejo", FOTOS / "ugc-collar-carmen-2" / "clips" / "espejo-1.mp4", 4.0),
    ("collar-hermanas-mesa", FOTOS / "ugc-dos-hijas" / "clips" / "mesa-1.mp4", 3.5),
    ("collar-madre-hija-palmas", FOTOS / "ugc-madre-hija" / "clips" / "palmas-1.mp4", 3.5),
]


def main():
    DESTINO.mkdir(parents=True, exist_ok=True)
    urls = json.loads(URLS.read_text(encoding="utf8")) if URLS.exists() else {}
    for nombre, clip, seg in CLIPS:
        mp4, jpg = DESTINO / f"{nombre}.mp4", DESTINO / f"{nombre}.jpg"
        subprocess.run([FF, "-v", "error", "-y", "-i", str(clip), "-t", str(seg), "-an", "-vf", "scale=540:960",
                        "-c:v", "libx264", "-crf", "24", "-preset", "slow", "-pix_fmt", "yuv420p",
                        "-movflags", "+faststart", str(mp4)], check=True)
        subprocess.run([FF, "-v", "error", "-y", "-i", str(mp4), "-frames:v", "1", "-q:v", "3", str(jpg)], check=True)
        if nombre not in urls:
            urls[nombre] = {"mp4": subir(mp4), "jpg": subir(jpg)}
            URLS.write_text(json.dumps(urls, ensure_ascii=False, indent=1) + "\n", encoding="utf8")
        print(nombre, urls[nombre]["mp4"][:80])
    # Lista para pegar en lunerie-ficha.liquid (parte «historias»): «mp4|jpg» separados por comas
    print("\n" + ",".join(f"{urls[n]['mp4']}|{urls[n]['jpg']}" for n, _, _ in CLIPS))
    # El bloque del collar (parte «signe»): la piedra que cambia de color y la cajita con la pegatina
    for nombre, ruta in (("collar-piedra-mes", DESTINO / "collar-piedra-mes.mp4"),
                         ("collar-signe-cajita-pegatina", FOTOS / "cajita" / "collar-signe-cajita-pegatina.jpg")):
        if nombre not in urls:
            urls[nombre] = {"url": subir(ruta)}
            if ruta.suffix == ".mp4":
                urls[nombre]["jpg"] = subir(ruta.with_suffix(".jpg"))
            URLS.write_text(json.dumps(urls, ensure_ascii=False, indent=1) + "\n", encoding="utf8")
        print(nombre, urls[nombre])


if __name__ == "__main__":
    main()
