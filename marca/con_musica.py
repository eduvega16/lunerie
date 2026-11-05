"""Pone música por debajo de la voz de un vídeo (5-nov, Edu: «Holiday Bells» para el vídeo UGC del collar).
La música baja sola cuando habla la voz (sidechain), entra con fundido y sale con fundido al final; el total se
normaliza a -14 LUFS (lo que usa Instagram). Sin créditos.
    python marca/con_musica.py <video.mp4> <musica> [--inicio 0.5] [--bajo 18]   → <video>-musica.mp4
--bajo: cuántos dB queda la música por debajo de la voz (media medida con volumedetect). 5-nov: con un volumen fijo
(0,30) la música quedó POR ENCIMA de la voz de Silvia (Edu: «va súper fuerte la música»); por eso ahora se mide.
La música tiene que tener licencia para anuncios (la de la biblioteca de sonidos de Meta vale en Facebook e Instagram).
"""
import pathlib, re, subprocess, sys


def duracion(f):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)],
                                capture_output=True, text=True).stdout)


def media_db(f, filtro="anull"):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(f), "-vn", "-af", filtro + ",volumedetect", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    return float(re.search(r"mean_volume: (-?[\d.]+) dB", r).group(1))


def mezclar(video, musica, inicio=0.5, bajo=18):
    video, musica = pathlib.Path(video), pathlib.Path(musica)
    salida = video.with_name(video.stem + "-musica.mp4")
    d = duracion(video)
    voz_db = media_db(video)
    mus_db = media_db(musica, f"atrim=start={inicio}:duration={d:.2f}")
    vol = 10 ** ((voz_db - bajo - mus_db) / 20)
    print(f"voz {voz_db} dB · música {mus_db} dB → volumen de la música {vol:.3f} ({bajo} dB por debajo)")
    filtro = (f"[1:a]atrim=start={inicio}:duration={d:.2f},asetpts=PTS-STARTPTS,volume={vol},"
              f"afade=t=in:st=0:d=0.4,afade=t=out:st={d - 1.6:.2f}:d=1.6[m];"
              "[0:a]asplit=2[voz][llave];"
              "[m][llave]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=350[mb];"
              "[voz][mb]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(video), "-i", str(musica), "-filter_complex", filtro,
                    "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                    "-movflags", "+faststart", str(salida)], check=True)
    print(salida)
    return salida


if __name__ == "__main__":
    a = sys.argv[1:]
    ini = float(a[a.index("--inicio") + 1]) if "--inicio" in a else 0.5
    bajo = float(a[a.index("--bajo") + 1]) if "--bajo" in a else 18
    mezclar(a[0], a[1], ini, bajo)
