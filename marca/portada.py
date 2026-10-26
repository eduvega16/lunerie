"""Vídeos de la portada (fondo del óvalo) a partir de los clips de Kling del Lune verde, en bucle sin salto.

    python marca/portada.py            → marca/portada/portada-movil.mp4 / portada-pc.mp4 + sus .jpg (primer fotograma)

· Móvil (720x1280): los planos uno detrás de otro con fundidos; el último funde al primero, así el bucle no se nota.
· PC (1920x1080): tres planos verticales en fila, cada uno ida y vuelta (el bucle cierra solo).
Solo se usan los primeros ~2,6 s de cada clip: al final Kling deforma la esfera. Sin audio. El oscurecido y el grano
los pone el CSS de la portada (lunerie-inicio.liquid), no el vídeo.
"""
import pathlib, subprocess

RAIZ = pathlib.Path(__file__).resolve().parent
CLIPS = RAIZ / "fotos-ia" / "anuncios"
SALIDA = RAIZ / "portada"
FPS, TRAMO, FUNDIDO = 24, 2.6, 0.6
MOVIL = ["planos/5-cielo.mp4", "lune-verde-toalla-b.mp4", "planos/2-perfil.mp4", "planos/4-pelo.mp4"]
PC = ["lune-verde-toalla-b.mp4", "planos/5-cielo.mp4", "planos/4-pelo.mp4"]   # el del centro queda tras el texto
COMUN = ["-an", "-c:v", "libx264", "-crf", "23", "-preset", "slow", "-pix_fmt", "yuv420p", "-movflags", "+faststart"]


def encuadre(i, w, h):
    return f"[{i}:v]fps={FPS},scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h},setsar=1,setpts=PTS-STARTPTS"


def movil(salida, w=720, h=1280):
    # A empieza en FUNDIDO y el A' del final acaba en FUNDIDO: el último fotograma enlaza con el primero
    tramos = [(MOVIL[0], FUNDIDO, TRAMO - FUNDIDO)] + [(c, 0, TRAMO) for c in MOVIL[1:]] + [(MOVIL[0], 0, FUNDIDO)]
    entradas, filtros = [], []
    for i, (c, ini, dur) in enumerate(tramos):
        entradas += ["-ss", str(ini), "-t", str(dur), "-i", str(CLIPS / c)]
        filtros.append(encuadre(i, w, h) + f"[v{i}]")
    previo, largo = "[v0]", tramos[0][2]
    for i in range(1, len(tramos)):
        largo -= FUNDIDO
        filtros.append(f"{previo}[v{i}]xfade=transition=fade:duration={FUNDIDO}:offset={largo:.3f}[x{i}]")
        previo, largo = f"[x{i}]", largo + tramos[i][2]
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *entradas, "-filter_complex", ";".join(filtros),
                    "-map", previo, *COMUN, str(salida)], check=True)
    return largo


def pc(salida, w=640, h=1080):
    entradas, filtros = [], []
    for i, c in enumerate(PC):
        entradas += ["-t", str(TRAMO), "-i", str(CLIPS / c)]
        filtros.append(encuadre(i, w, h) + f",split[a{i}][b{i}];[b{i}]reverse[r{i}];[a{i}][r{i}]concat=n=2:v=1:a=0[p{i}]")
    filtros.append("".join(f"[p{i}]" for i in range(len(PC))) + f"hstack=inputs={len(PC)}[out]")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *entradas, "-filter_complex", ";".join(filtros),
                    "-map", "[out]", *COMUN, str(salida)], check=True)
    return 2 * TRAMO


def primer_fotograma(video, jpg):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(video), "-frames:v", "1", "-q:v", "3", str(jpg)],
                   check=True)


if __name__ == "__main__":
    SALIDA.mkdir(exist_ok=True)
    for nombre, hacer in (("portada-movil", movil), ("portada-pc", pc)):
        mp4 = SALIDA / f"{nombre}.mp4"
        dur = hacer(mp4)
        primer_fotograma(mp4, SALIDA / f"{nombre}.jpg")
        print(f"{nombre}: {dur:.1f} s, {mp4.stat().st_size / 1e6:.1f} MB")
