"""Monta un anuncio vertical (1080x1920) a partir de varios clips: cortes secos y logo LUNERIE en el último plano.

    python marca/montaje.py salida.mp4 clip1.mp4,inicio,duración[,giro] clip2.mp4,... [--logo-y 0.62]
                            [--musica pista.mp3 [--vol 0.8] [--musica-inicio 12]]

`giro` = 180 pone ese plano al revés (como el cierre del anuncio de referencia). El logo blanco sale en el último
plano, centrado, con un fundido. Sin `--musica` el vídeo sale sin audio (la música se elige luego en TikTok / Meta).
Con `--musica` (29-oct, para el editor de vídeo de la oficina): se mezcla la pista con fundido de entrada y de
salida y se recorta al largo del vídeo. LA PISTA TIENE QUE TENER LICENCIA para anuncios y redes (ver oficina/README.md).
"""
import pathlib, subprocess, sys

RAIZ = pathlib.Path(__file__).resolve().parent
LOGO = RAIZ / "logos" / "logo-blanco.png"
W, H, FPS = 1080, 1920, 30


def montar(salida, planos, logo_y=0.62, logo_ancho=300, musica=None, vol=0.8, musica_inicio=0.0):
    entradas, filtros, nombres = [], [], []
    for i, (fich, ini, dur, giro) in enumerate(planos):
        entradas += ["-ss", str(ini), "-t", str(dur), "-i", fich]
        f = (f"[{i}:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},"
             f"setsar=1,setpts=PTS-STARTPTS")
        if giro == 180:
            f += ",hflip,vflip"
        filtros.append(f + f"[v{i}]")
        nombres.append(f"[v{i}]")
    n = len(planos)
    filtros.append("".join(nombres) + f"concat=n={n}:v=1:a=0[base]")
    total = sum(p[2] for p in planos)
    ini_ult = total - planos[-1][2]
    entradas += ["-loop", "1", "-i", str(LOGO)]
    filtros.append(f"[{n}:v]trim=0:{total},crop=1646:167:375:184,scale={logo_ancho}:-1,format=rgba,"
                   f"fade=t=in:st={ini_ult + 0.4}:d=0.6:alpha=1[logo]")
    filtros.append(f"[base][logo]overlay=(W-w)/2:H*{logo_y}-h/2:enable='gte(t,{ini_ult})',"
                   f"fade=t=out:st={total - 0.35}:d=0.35[out]")
    if musica:
        entradas += ["-ss", str(musica_inicio), "-i", str(musica)]
        fade = min(1.2, total / 3)
        filtros.append(f"[{n + 1}:a]volume={vol},afade=t=in:st=0:d=0.5,afade=t=out:st={total - fade}:d={fade}[aud]")
        audio = ["-map", "[aud]", "-c:a", "aac", "-b:a", "192k"]
    else:
        audio = ["-an"]
    cmd = ["ffmpeg", "-y", "-loglevel", "error", *entradas, "-filter_complex", ";".join(filtros),
           "-map", "[out]", *audio, "-t", str(total), "-c:v", "libx264", "-crf", "18", "-preset", "slow",
           "-pix_fmt", "yuv420p", "-movflags", "+faststart", salida]
    subprocess.run(cmd, check=True)
    return total


if __name__ == "__main__":
    args = sys.argv[1:]
    logo_y = 0.62
    if "--logo-y" in args:
        k = args.index("--logo-y"); logo_y = float(args[k + 1]); del args[k:k + 2]
    opciones = {}
    for flag, clave, tipo in (("--musica", "musica", str), ("--vol", "vol", float), ("--musica-inicio", "musica_inicio", float)):
        if flag in args:
            k = args.index(flag); opciones[clave] = tipo(args[k + 1]); del args[k:k + 2]
    salida, planos = args[0], []
    for a in args[1:]:
        fich, ini, dur, *g = a.split(",")
        planos.append((fich, float(ini), float(dur), int(g[0]) if g else 0))
    print("duracion:", montar(salida, planos, logo_y, **opciones), "s ->", salida)
