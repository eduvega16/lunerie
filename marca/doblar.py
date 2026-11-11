"""Voz en off de Silvia (ElevenLabs) para los reels «de cerca» (28) y «Sarah» (29), 11-nov-2026.

Cada frase se genera por separado y se coloca en el segundo en que sale su plano; si una frase es más larga que su
plano, la siguiente espera a que acabe. La voz se pasa por el filtro «móvil» (sin graves ni brillo de estudio, un poco
de eco de habitación): Edu no quiere voces de «doblaje». Siempre en segunda persona («Te van a preguntar…»): nada de
testimonios inventados.

    python marca/doblar.py [28|29|todos]   →  campana-bf/<vídeo>-voz-9x16.mp4 y -voz-4x5.mp4

Necesita ELEVENLABS_KEY en .env.local (la pone Edu; nunca en el chat ni en git). Gasta ~1 crédito por carácter
(~200 por vídeo). La música va aparte: python marca/con_musica.py <vídeo-voz> <música> (baja cuando habla).
"""
import base64
import subprocess
import sys
from pathlib import Path

import imageio_ffmpeg

sys.path.insert(0, str(Path(__file__).resolve().parent))
import voz_elevenlabs as el  # noqa: E402

SILVIA = "DNtbMnLZ43q8pReedyYw"   # «Silvia - Expressive», biblioteca de ElevenLabs (la de los vídeos UGC del 5-7 nov)
CAMPANA = el.RAIZ / "marca" / "fotos-ia" / "campana-bf"
DESTINO = CAMPANA / "voz"
FF = imageio_ffmpeg.get_ffmpeg_exe()

PROMO = "Y hasta el cinco de diciembre, el tercero es gratis."
GUIONES = {   # (segundo en que empieza su plano, frase)
    "28-de-cerca": [(0.2, "Te van a preguntar de dónde es."), (2.5, "Lleva su nombre…"),
                    (4.2, "…y la piedra de su mes."), (6.0, "Con baño de oro de dieciocho quilates."),
                    (8.65, "Hay una lágrima para cada mes."), (11.3, PROMO)],
    "29-ugc-sarah": [(0.2, "Te van a preguntar de dónde es."), (2.4, "Lleva su nombre…"),
                     (4.4, "…y la piedra de su mes."), (6.4, "Con baño de oro de dieciocho quilates."),
                     (8.7, PROMO)],
}
MOVIL = ("highpass=f=160,lowpass=f=7200,equalizer=f=2800:t=q:w=1.2:g=2,"
         "aecho=0.85:0.5:22|41:0.12|0.07,volume=1.1")


def duracion(ruta):
    r = subprocess.run([FF, "-i", str(ruta)], capture_output=True, text=True)
    linea = next(l for l in r.stderr.splitlines() if "Duration" in l)
    h, m, s = linea.split("Duration:")[1].split(",")[0].strip().split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)


def frase(texto, n, modelo):
    ruta = DESTINO / f"frase-{n}-{el.limpio(texto)}.mp3"
    if not ruta.exists():   # no se paga dos veces la misma frase
        # el endpoint con tiempos devuelve JSON con el audio en base64 (el simple devuelve el mp3 y pedir() espera JSON)
        r = el.pedir(f"/v1/text-to-speech/{SILVIA}/with-timestamps?output_format=mp3_44100_128",
                     {"text": texto, "model_id": modelo, "language_code": "es",
                      "voice_settings": {"stability": 0.32, "similarity_boost": 0.75, "style": 0.0,
                                         "use_speaker_boost": False}})
        ruta.write_bytes(base64.b64decode(r["audio_base64"]))
        print(f"  generada: {texto} ({len(texto)} caracteres)")
    return ruta


def doblar(nombre, modelo):
    print(nombre)
    frases, t_libre = [], 0.0
    for n, (inicio, texto) in enumerate(GUIONES[nombre], 1):
        ruta = frase(texto, n, modelo)
        t = max(inicio, t_libre)
        frases.append((ruta, t))
        t_libre = t + duracion(ruta) + 0.08
    for formato in ("9x16", "4x5"):
        video = CAMPANA / f"{nombre}-{formato}.mp4"
        salida = CAMPANA / f"{nombre}-voz-{formato}.mp4"
        entradas, filtros = ["-i", str(video)], []
        for i, (ruta, t) in enumerate(frases, 1):
            entradas += ["-i", str(ruta)]
            ms = int(t * 1000)
            filtros.append(f"[{i}:a]{MOVIL},adelay={ms}|{ms}[f{i}]")
        mezcla = "".join(f"[f{i}]" for i in range(1, len(frases) + 1))
        # 11-nov (Edu: «suena muy bajita»): volumen normalizado a -14 LUFS, lo que piden Instagram y TikTok
        filtros.append(f"{mezcla}amix=inputs={len(frases)}:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11,apad[a]")
        subprocess.run([FF, "-v", "error", "-y", *entradas, "-filter_complex", ";".join(filtros),
                        "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest",
                        str(salida)], check=True)
        print(" ", salida)
    fin = t_libre - 0.08
    if fin > duracion(CAMPANA / f"{nombre}-9x16.mp4"):
        print(f"  OJO: la voz acaba en {fin:.1f} s y el vídeo es más corto: se corta la última frase")


def main():
    if not el.CLAVE:
        sys.exit("Falta ELEVENLABS_KEY en .env.local (la pone Edu en este PC; nunca en el chat).")
    DESTINO.mkdir(parents=True, exist_ok=True)
    el.asegurar_voz(SILVIA)
    modelo = el.modelo()
    cual = sys.argv[1] if len(sys.argv) > 1 else "todos"
    for nombre in GUIONES:
        if cual in ("todos", nombre[:2]):
            doblar(nombre, modelo)


if __name__ == "__main__":
    main()
