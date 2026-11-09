"""Reel «pellizco» (gancho de un reel que pasó Edu, 9-nov): una chica NÍTIDA mira a cámara y hace el gesto de agrandar
la pantalla con dos dedos; en el centro, el Collar Signé (foto REAL de la ficha, recortada) empieza diminuto y crece a
saltos con cada gesto hasta que se lee «Carmen» y se ve la lágrima. Luego, el texto del cierre.
La chica es IA (Higgsfield flare + Kling 3.0 pro, sin collar puesto); el collar NO es IA (se pega encima, nombre exacto).
    python marca/reel_pellizco.py foto --n 2                 → marca/fotos-ia/reel-pellizco/chica-1.png …
    python marca/reel_pellizco.py animar chica-1 [--seg 6]   → marca/fotos-ia/reel-pellizco/chica-1.mp4
    python marca/reel_pellizco.py montar chica-1 --gestos 1.2,2.6,4.0  → 27-pellizco-9x16.mp4 / -4x5.mp4
`--gestos`: segundos del clip en que los dedos se abren (mirarlo en los fotogramas). En 9:16 todo dentro de y 270-1248.
"""
import math, pathlib, subprocess, sys, urllib.request
import numpy as np
from dotenv import load_dotenv
from PIL import Image, ImageFilter
import imageio_ffmpeg
import higgsfield_client

RAIZ = pathlib.Path(__file__).resolve().parent.parent
load_dotenv(RAIZ / ".env.local")
sys.path.insert(0, str(RAIZ / "marca"))
from mofu_bofu import FOTO, SALIDA, FONDO   # noqa: E402
from cierre_animado import texto, CORTE_Y    # noqa: E402

CARPETA = RAIZ / "marca" / "fotos-ia" / "reel-pellizco"
CHICA = ("A young Spanish woman of about 25 with straight light-brown hair with soft honey highlights tucked behind one "
         "ear, fair warm skin with real texture, natural minimal makeup, green-hazel eyes, small gold hoop earrings, "
         "wearing a plain white ribbed tank top. Her neck is bare: NO necklace at all.")
FOTO_PROMPT = (CHICA + " Vertical smartphone selfie-style video frame: she faces the camera at eye level, seen from the "
               "waist up, centred, sharp and in focus. Both of her hands are raised in front of her chest towards the "
               "camera, the thumb and index finger of each hand pinched together, as if she were about to zoom into a "
               "touchscreen between her and the viewer. Curious, playful expression, slight smile. Bright bedroom with "
               "white walls and linen curtains behind her (the room slightly soft, she is sharp), soft natural daylight, "
               "slight phone-camera grain, candid UGC look, not a studio photo. No text, no logo, no watermark.")
ANIM_PROMPT = ("She looks straight at the camera and makes the pinch-to-zoom gesture three times in a steady rhythm, as if "
               "enlarging something on a touchscreen in front of her: she brings thumb and index finger together, then "
               "spreads them apart quickly towards the camera; after each spread she returns to the pinch and repeats. "
               "Each gesture is clear and about one second long. Curious expression, a small smile at the end. Same face, "
               "natural skin, no necklace appears. Static phone on a tripod, very subtle natural shake, soft daylight.")
FPS = 30
MODO = "pro"
CAJA = (520, 980, 1990, 2438)       # zona del collar en la foto real: nombre + lágrima (sin el reflejo)
ALTO_FINAL = {1920: 860, 1350: 700}       # alto del collar cuando ya se lee (9:16 / 4:5)
CY = {1920: ((1060, 760), 520), 1350: ((760, 520), 330)}   # centro: (pequeño, grande) y en el cierre
ESCALAS = [0.07, 0.16, 0.38, 1.0]   # tamaño relativo antes del 1.er gesto y tras cada uno


def foto(n):
    CARPETA.mkdir(parents=True, exist_ok=True)
    for k in range(n):
        r = higgsfield_client.subscribe("marketing-studio/image/flare", arguments={
            "prompt": FOTO_PROMPT, "image_urls": [], "aspect_ratio": "9:16", "resolution": "2k",
            "quality": "high", "enhance_prompt": False})
        imgs = (r or {}).get("images") or []
        if not imgs:
            print("SIN IMAGEN", r)
            continue
        destino = CARPETA / f"chica-{k + 1}.png"
        urllib.request.urlretrieve(imgs[0]["url"], destino)
        print(destino, Image.open(destino).size, flush=True)


def animar(nombre, seg):
    im = Image.open(CARPETA / f"{nombre}.png").convert("RGB")
    w = round(im.height * 9 / 16)
    if im.width > w:
        x0 = (im.width - w) // 2
        im = im.crop((x0, 0, x0 + w, im.height))
    jpg = CARPETA / f"{nombre}-916.jpg"
    im.save(jpg, quality=95, subsampling=0)
    r = higgsfield_client.subscribe("kling-video/v3.0/" + MODO + "/image-to-video", arguments={
        "image_url": higgsfield_client.upload_file(jpg), "prompt": ANIM_PROMPT, "duration": seg,
        "sound": "off", "aspect_ratio": "9:16"})
    v = (r or {}).get("video") or ((r or {}).get("videos") or [None])[0]
    if not v:
        sys.exit(f"SIN VÍDEO {r}")
    destino = CARPETA / f"{nombre}.mp4"
    urllib.request.urlretrieve(v["url"], destino)
    print(destino)


def collar_recortado():
    """El collar de la foto real con fondo transparente (recortado por la diferencia con el fondo claro)."""
    im = Image.open(FOTO).convert("RGB").crop((CAJA[0], CAJA[1], CAJA[2], min(CAJA[3], CORTE_Y)))
    a = np.asarray(im).astype(np.int16)
    dif = np.abs(a - np.array(FONDO, dtype=np.int16)).max(axis=2)
    alfa = np.clip((dif - 10) * 7, 0, 255).astype(np.uint8)
    c = im.convert("RGBA")
    c.putalpha(Image.fromarray(alfa))
    return c.crop(c.getbbox())


def leer_clip(mp4, w, h):
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    p = subprocess.run([ff, "-loglevel", "error", "-i", str(mp4), "-vf",
                        f"scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h},fps={FPS}",
                        "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True, check=True)
    datos = np.frombuffer(p.stdout, np.uint8)
    return datos.reshape(-1, h, w, 3)


def escala(t, gestos):
    """Tamaño relativo del collar: salta con cada gesto con un pequeño rebote (como un zoom con los dedos)."""
    e = ESCALAS[0]
    for k, g in enumerate(gestos):
        if t < g:
            break
        s = t - g
        de, a = ESCALAS[k], ESCALAS[k + 1]
        u = min(s / 0.35, 1)
        u = 1 - (1 - u) ** 3
        rebote = 0.06 * math.exp(-s / 0.18) * math.sin(2 * math.pi * 2.2 * s)
        e = de + (a - de) * u
        e *= 1 + rebote * min(s / 0.05, 1)
    return e


def con_sombra(c):
    """Sombra suave debajo del collar, como si estuviera encima de la pantalla."""
    m = 40
    lienzo = Image.new("RGBA", (c.width + 2 * m, c.height + 2 * m), (0, 0, 0, 0))
    a = Image.new("L", lienzo.size, 0)
    a.paste(c.getchannel("A"), (m + 6, m + 10))
    sombra = Image.new("RGBA", lienzo.size, (20, 25, 22, 0))
    sombra.putalpha(a.filter(ImageFilter.GaussianBlur(9)).point(lambda v: round(v * 0.45)))
    lienzo.alpha_composite(sombra)
    lienzo.alpha_composite(c, (m, m))
    return lienzo


def suave(u):
    u = min(max(u, 0), 1)
    return u * u * (3 - 2 * u)


def montar(nombre, gestos, w, h, salida):
    clip = leer_clip(CARPETA / f"{nombre}.mp4", w, h)
    col = con_sombra(collar_recortado())
    base = ALTO_FINAL[h] / col.height
    (cy_peq, cy_gran), cy_cierre = CY[h]
    final = gestos[-1] + 1.0            # se queda grande un momento sobre la chica
    total = final + 3.4                 # luego, fondo claro y el texto del cierre
    capa_txt = texto(w)
    dy_txt = 0 if h == 1920 else -190   # en 4:5 el texto del cierre sube
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    proc = subprocess.Popen([ff, "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w}x{h}",
                             "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-crf", "16", "-preset", "slow",
                             "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(SALIDA / salida)],
                            stdin=subprocess.PIPE)
    for i in range(round(total * FPS)):
        t = i / FPS
        fr = Image.fromarray(clip[min(i, len(clip) - 1)]).convert("RGBA")
        e = escala(t, gestos)
        p = (e - ESCALAS[0]) / (ESCALAS[-1] - ESCALAS[0])
        cy = cy_peq + (cy_gran - cy_peq) * min(max(p, 0), 1)
        u = suave((t - final) / 0.7)
        if u > 0:   # fundido a fondo claro: el collar encoge y sube y entra el texto
            fr.alpha_composite(Image.new("RGBA", (w, h), FONDO + (round(255 * u),)))
            e *= 1 - 0.42 * u
            cy += (cy_cierre - cy) * u
        k = e * base
        cw, ch = max(2, round(col.width * k)), max(2, round(col.height * k))
        c = col.resize((cw, ch), Image.Resampling.LANCZOS)
        fr.alpha_composite(c, (round(w / 2 - cw / 2), round(cy - ch / 2)))
        v = suave((t - final - 0.55) / 0.5)
        if v > 0:
            txt = capa_txt.copy()
            txt.putalpha(txt.getchannel("A").point(lambda q: round(q * v)))
            y = dy_txt + round(16 * (1 - v))
            fr.alpha_composite(txt.crop((0, -y, w, -y + h)) if y < 0 else txt.crop((0, 0, w, h - y)), (0, max(y, 0)))
        proc.stdin.write(fr.convert("RGB").tobytes())
    proc.stdin.close()
    proc.wait()
    print(SALIDA / salida)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "foto":
        foto(int(a[a.index("--n") + 1]) if "--n" in a else 1)
    elif a[0] == "animar":
        animar(a[1], int(a[a.index("--seg") + 1]) if "--seg" in a else 6)
    elif a[0] == "montar":
        g = [float(x) for x in a[a.index("--gestos") + 1].split(",")]
        montar(a[1], g, 1080, 1920, "27-pellizco-9x16.mp4")
        montar(a[1], g, 1080, 1350, "27-pellizco-4x5.mp4")
