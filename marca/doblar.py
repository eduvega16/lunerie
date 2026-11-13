"""Voz en off de Silvia (ElevenLabs) para los reels «de cerca» (28) y «Sarah» (29), 11-nov-2026.

Cada frase se genera por separado y se coloca en el segundo en que sale su plano; si una frase es más larga que su
plano, la siguiente espera a que acabe. La voz se pasa por el filtro «móvil» (sin graves ni brillo de estudio, un poco
de eco de habitación): Edu no quiere voces de «doblaje». Siempre en segunda persona («Te van a preguntar…»): nada de
testimonios inventados.

    python marca/doblar.py [28|29|31|todos] [--voz <voice_id>]   →  <vídeo>-voz-9x16.mp4 y -voz-4x5.mp4
    python marca/doblar.py 31 --muestras <id1,id2,…>   →  voz/muestras-31/<voz>.mp3 (primeras frases, para elegir voz)
13-nov: el 31 (UGC «abrir la cajita», marca/fotos-ia/ugc-lucce/) con otra voz (Edu); la caché de frases lleva la voz en
el nombre para no mezclar voces. Después, el 31 va en una sola toma (TOMAS, más natural):
    python marca/doblar.py 31   →  ugc-lucce/31-ugc-cajita-voz-9x16-musica.mp4 y -4x5-musica.mp4 (voz + Holiday Bells)

Necesita ELEVENLABS_KEY en .env.local (la pone Edu; nunca en el chat ni en git). Gasta ~1 crédito por carácter
(~200 por vídeo). La música va aparte: python marca/con_musica.py <vídeo-voz> <música> (baja cuando habla).
"""
import base64
import subprocess
import sys
from pathlib import Path

import shutil

sys.path.insert(0, str(Path(__file__).resolve().parent))
import voz_elevenlabs as el  # noqa: E402

SILVIA = "DNtbMnLZ43q8pReedyYw"   # «Silvia - Expressive», biblioteca de ElevenLabs (la de los vídeos UGC del 5-7 nov)
CAMPANA = el.RAIZ / "marca" / "fotos-ia" / "campana-bf"
DESTINO = CAMPANA / "voz"
FF = shutil.which("ffmpeg") or __import__("imageio_ffmpeg").get_ffmpeg_exe()
VOZ_ID = SILVIA

PROMO = "Y hasta el cinco de diciembre, el tercero es gratis."
GUIONES = {   # (segundo en que empieza su plano, frase)
    "28-de-cerca": [(0.2, "Te van a preguntar de dónde es."), (2.5, "Lleva su nombre…"),
                    (4.2, "…y la piedra de su mes."), (6.0, "Con baño de oro de dieciocho quilates."),
                    (8.65, "Hay una lágrima para cada mes."), (11.3, PROMO)],
    "29-ugc-sarah": [(0.2, "Te van a preguntar de dónde es."), (2.4, "Lleva su nombre…"),
                     (4.4, "…y la piedra de su mes."), (6.4, "Con baño de oro de dieciocho quilates."),
                     (8.7, PROMO)],
    # 13-nov: planos de ugc_lucce_montaje.py → caja-cara 0 · caja-mano 1,6 · delante 4,6 · colgando 6,7 · abrochar 9,2 ·
    # pellizco 10,9 · pecho 12,5 · ancla 13,9 · cierre 15,5 (el texto entra hacia 16,8)
    "31-ugc-cajita": [(0.2, "Así llega su collar…"), (1.8, "…en su cajita de terciopelo, lista para regalar."),
                      (4.8, "Lleva su nombre, escrito como una firma…"),
                      (7.0, "…y la piedra de su mes. O la que más te guste."),
                      (9.6, "Con baño de oro de dieciocho quilates."),
                      (15.8, "Y por Black Friday, la cajita te la regalamos."),
                      (18.6, "La segunda pieza, a mitad de precio.")],
}
CARPETA_VIDEO = {"31-ugc-cajita": el.RAIZ / "marca" / "fotos-ia" / "ugc-lucce"}   # el resto, en campana-bf
# 13-nov (Edu: las voces frase a frase «suenan poco naturales»): el 31 va en UNA toma seguida (Jenni, eleven_v4, texto
# más hablado; elegida la «A» de voz/muestras-31/jenni/) y se corta en trozos con los tiempos de cada palabra (sacados
# con el speech-to-text de ElevenLabs): el cuerpo sobre los planos y la promo cuando sale la tarjeta. Filtro sin eco.
#   «Mira cómo llega su collar… en una cajita de terciopelo, ya lista para regalar. Lleva su nombre, como si lo hubiera
#    firmado ella… y la piedra de su mes, o la que tú quieras. Con baño de oro de dieciocho quilates. | Y por Black
#    Friday, la cajita te la regalamos. Y la segunda pieza, a mitad de precio.»
TOMAS = {"31-ugc-cajita": {"archivo": DESTINO / "muestras-31" / "jenni" / "A-v4-una-toma-crudo.mp3",
                           "trozos": [(0.0, 13.6, 0.2), (13.6, None, 15.6)]}}   # (desde, hasta, segundo del vídeo)
SUAVE = "highpass=f=120,lowpass=f=8500,equalizer=f=3000:t=q:w=1.2:g=1.5"
MOVIL = ("highpass=f=160,lowpass=f=7200,equalizer=f=2800:t=q:w=1.2:g=2,"
         "aecho=0.85:0.5:22|41:0.12|0.07,volume=1.1")


def duracion(ruta):
    r = subprocess.run([FF, "-i", str(ruta)], capture_output=True, text=True)
    linea = next(l for l in r.stderr.splitlines() if "Duration" in l)
    h, m, s = linea.split("Duration:")[1].split(",")[0].strip().split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)


def frase(texto, n, modelo):
    pre = "" if VOZ_ID == SILVIA else f"{VOZ_ID[:6]}-"
    ruta = DESTINO / f"{pre}frase-{n}-{el.limpio(texto)}.mp3"
    if not ruta.exists():   # no se paga dos veces la misma frase
        # el endpoint con tiempos devuelve JSON con el audio en base64 (el simple devuelve el mp3 y pedir() espera JSON)
        r = el.pedir(f"/v1/text-to-speech/{VOZ_ID}/with-timestamps?output_format=mp3_44100_128",
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
        carpeta = CARPETA_VIDEO.get(nombre, CAMPANA)
        video = carpeta / f"{nombre}-{formato}.mp4"
        salida = carpeta / f"{nombre}-voz-{formato}.mp4"
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
    if fin > duracion(CARPETA_VIDEO.get(nombre, CAMPANA) / f"{nombre}-9x16.mp4"):
        print(f"  OJO: la voz acaba en {fin:.1f} s y el vídeo es más corto: se corta la última frase")


def doblar_toma(nombre, toma):
    """Voz de una sola toma, cortada en trozos y colocada en su segundo; luego la música por debajo (con_musica)."""
    import con_musica
    print(nombre, "(una toma)")
    carpeta = CARPETA_VIDEO.get(nombre, CAMPANA)
    for formato in ("9x16", "4x5"):
        video = carpeta / f"{nombre}-{formato}.mp4"
        salida = carpeta / f"{nombre}-voz-{formato}.mp4"
        entradas, filtros = ["-i", str(video)], []
        for i, (desde, hasta, t) in enumerate(toma["trozos"], 1):
            entradas += ["-i", str(toma["archivo"])]
            corte = f"atrim=start={desde}" + (f":end={hasta}" if hasta else "")
            ms = int(t * 1000)
            filtros.append(f"[{i}:a]{corte},asetpts=PTS-STARTPTS,afade=t=in:d=0.03,areverse,afade=t=in:d=0.05,"
                           f"areverse,{SUAVE},adelay={ms}|{ms}[f{i}]")
        n = len(toma["trozos"])
        filtros.append("".join(f"[f{i}]" for i in range(1, n + 1)) +
                       f"amix=inputs={n}:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11,apad[a]")
        subprocess.run([FF, "-v", "error", "-y", *entradas, "-filter_complex", ";".join(filtros),
                        "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest",
                        str(salida)], check=True)
        print(" ", salida)
        con_musica.mezclar(salida, el.RAIZ / "marca" / "musica" / "holiday-bells.m4a")


def muestras(nombre, voces, modelo, n_frases=3):
    """Las primeras frases del guion con cada voz, en un mp3 por voz (con el filtro «móvil»), para elegir."""
    global VOZ_ID
    carpeta = DESTINO / f"muestras-{nombre[:2]}"
    carpeta.mkdir(parents=True, exist_ok=True)
    for voz in voces:
        VOZ_ID = voz
        el.asegurar_voz(voz)
        rutas = [frase(texto, i, modelo) for i, (_, texto) in enumerate(GUIONES[nombre][:n_frases], 1)]
        entradas = sum((["-i", str(r)] for r in rutas), [])
        filtro = "".join(f"[{i}:a]{MOVIL},apad=pad_dur=0.25[f{i}];" for i in range(len(rutas)))
        filtro += "".join(f"[f{i}]" for i in range(len(rutas))) + f"concat=n={len(rutas)}:v=0:a=1,loudnorm=I=-14:TP=-1.5[a]"
        salida = carpeta / f"{voz[:6]}.mp3"
        subprocess.run([FF, "-v", "error", "-y", *entradas, "-filter_complex", filtro, "-map", "[a]", str(salida)],
                       check=True)
        print(" ", voz, "→", salida)


def main():
    global VOZ_ID
    if not el.CLAVE:
        sys.exit("Falta ELEVENLABS_KEY en .env.local (la pone Edu en este PC; nunca en el chat).")
    DESTINO.mkdir(parents=True, exist_ok=True)
    modelo = el.modelo()
    a = sys.argv[1:]
    cual = a[0] if a and not a[0].startswith("--") else "todos"
    if "--muestras" in a:
        nombre = next(n for n in GUIONES if n.startswith(cual))
        return muestras(nombre, a[a.index("--muestras") + 1].split(","), modelo)
    if "--voz" in a:
        VOZ_ID = a[a.index("--voz") + 1]
    el.asegurar_voz(VOZ_ID)
    for nombre in GUIONES:
        if cual in ("todos", nombre[:2]):
            if nombre in TOMAS and "--voz" not in a:
                doblar_toma(nombre, TOMAS[nombre])
            else:
                doblar(nombre, modelo)


if __name__ == "__main__":
    main()
