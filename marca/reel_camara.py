"""Reel «cámara digital» (6-nov, idea de Edu: reel de @mybirdyboutique): una cámara compacta antigua vista por detrás
y en su pantalla van pasando las fotos de las piezas, con cortes secos y un destello en cada cambio. Sin música (se pone
en Instagram).
    python marca/reel_camara.py camara [--n 2]   → marca/fotos-ia/reel-camara/camara-<n>.png  (IA, ~0,13 $ cada una)
    python marca/reel_camara.py montar <camara.png> → marca/fotos-ia/reel-camara/reel-camara-9x16.mp4  (gratis)
La pantalla se detecta sola (la zona blanca más grande dentro de la cámara); FOTOS = las que pasan, en orden.
"""
import pathlib, subprocess, sys, tempfile, urllib.request
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

RAIZ = pathlib.Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "marca" / "fotos-ia" / "reel-camara"
COLLAR = RAIZ / "marca" / "fotos-ia" / "collar"
W, H, FPS = 1080, 1920, 30
ESTUDIO = (0.02, 0.07, 0.80)   # recorte (x, y, ancho) en fracciones de la foto: acerca el collar en las de estudio
FOTOS = [  # (foto, segundos en pantalla, recorte o None = centro)
    (COLLAR / "nombre-laura-azul-2.png", 0.9, ESTUDIO),
    (COLLAR / "nombre-alba-rojo-1.png", 0.9, ESTUDIO),
    (COLLAR / "nombre-sara-verde-1.png", 0.9, ESTUDIO),
    (COLLAR / "dedos-1.png", 0.9, None),
    (COLLAR / "estudio-rojo-v2-1.png", 0.9, ESTUDIO),
    (COLLAR / "dedos-2.png", 0.9, None),
    ("FINAL", 2.2, None),
]
ZOOM = 0.06    # acercamiento lento de toda la imagen a lo largo del vídeo
PROMPT = (
    "Top-down product photograph on a seamless pure white background with soft natural daylight and a gentle soft "
    "shadow. A compact silver digital camera from the early 2000s, seen from the back, standing vertically (rotated 90 "
    "degrees) so that its large LCD screen is in portrait orientation, 3:4, in the upper part of the camera body; below "
    "the screen a round silver control dial and a few small buttons; a thin grey wrist strap cord comes out of the "
    "bottom right corner and runs out of the frame. The LCD screen is completely blank, flat, evenly lit pure white "
    "with a thin black inner border, perfectly rectangular and facing the camera straight on. The camera is centred and "
    "fills about 65% of the frame width, in the upper two thirds of the frame. Absolutely no logos, no brand names, no "
    "text, no numbers and no icons anywhere on the camera or the screen. Clean, minimal, high-end look.")


def camara(n):
    from dotenv import load_dotenv
    import higgsfield_client
    load_dotenv(RAIZ / ".env.local")
    SALIDA.mkdir(parents=True, exist_ok=True)
    for i in range(1, n + 1):
        res = higgsfield_client.subscribe("marketing-studio/image/flare", arguments={
            "prompt": PROMPT, "aspect_ratio": "9:16", "resolution": "2k", "quality": "high", "enhance_prompt": False})
        imgs = (res or {}).get("images") or []
        if not imgs:
            print(f"camara-{i}: SIN IMAGEN {res}"); continue
        destino = SALIDA / f"camara-{i}.png"
        urllib.request.urlretrieve(imgs[0]["url"], destino)
        print(destino)


def pantalla(img):
    """Rectángulo de la pantalla: la mayor zona casi blanca rodeada de oscuro (el marco negro del LCD)."""
    a = np.asarray(img.convert("L").resize((W, H)), dtype=np.int16)
    oscuro = a < 70
    # columna central del marco: la mediana de las columnas con muchos píxeles oscuros (los lados del marco)
    cols = np.where(oscuro.sum(axis=0) > 150)[0]
    if not len(cols):
        raise SystemExit("No encuentro el marco negro de la pantalla")
    def tramos(v):
        """Tramos oscuros de al menos 6 px seguidos (el marco), ignorando huecos de 1-2 px del antialias."""
        idx, out = np.where(v)[0], []
        for i in idx:
            if out and i - out[-1][1] <= 3:
                out[-1][1] = i
            else:
                out.append([i, i])
        return [t for t in out if t[1] - t[0] >= 5]
    cx = int((cols.min() + cols.max()) / 2)
    t = tramos(oscuro[:, cx])                    # marco de arriba y de abajo
    y0, y1 = t[0][1] + 1, t[1][0] - 1
    t = tramos(oscuro[(y0 + y1) // 2, :])        # marco de la izquierda y de la derecha
    x0, x1 = t[0][1] + 1, t[1][0] - 1
    return (x0, y0, x1, y1)


def tarjeta(tam):
    """Última pantalla: fondo niebla con el nombre de la pieza (Cormorant + Jost, como la tarjeta de los UGC)."""
    from PIL import ImageFont
    w, h = tam
    im = Image.new("RGB", tam, (242, 244, 242))
    d = ImageDraw.Draw(im)
    fuentes = RAIZ / "marca" / "fuentes"
    serif = ImageFont.truetype(str(fuentes / "Cormorant.ttf"), round(w * 0.16))
    cursiva = ImageFont.truetype(str(fuentes / "Cormorant-Italic.ttf"), round(w * 0.10))
    jost = ImageFont.truetype(str(fuentes / "Jost.ttf"), round(w * 0.055))
    tinta, oro = (22, 32, 27), (166, 131, 74)
    def centro(t, f, y, c):
        d.text(((w - d.textlength(t, font=f)) / 2, y), t, font=f, fill=c)
    centro("Collar Signé", serif, h * 0.30, tinta)
    centro("con su nombre", cursiva, h * 0.47, tinta)
    centro("y su piedra", cursiva, h * 0.56, tinta)
    centro("lunerie.es", jost, h * 0.74, oro)
    return im


def montar(ruta_camara):
    base = Image.open(ruta_camara).convert("RGB").resize((W, H), Image.LANCZOS)
    x0, y0, x1, y1 = pantalla(base)
    x0, y0, x1, y1 = x0 + 2, y0 + 2, x1 - 1, y1 - 1          # sin pisar el filo del marco
    tam = (x1 - x0, y1 - y0)
    print("pantalla", (x0, y0, x1, y1), tam)
    SALIDA.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as t:
        tmp = pathlib.Path(t)
        total = sum(round(s * FPS) for _, s, _ in FOTOS)
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2 + 120     # el acercamiento va hacia la pantalla
        k = 0
        for foto, seg, rec in FOTOS:
            if foto == "FINAL":
                im = tarjeta(tam)
            else:
                im = Image.open(foto).convert("RGB")
                if rec:
                    fx, fy, fw = rec
                    w = im.width * fw
                    im = im.crop((round(im.width * fx), round(im.height * fy),
                                  round(im.width * fx + w), round(im.height * fy + w * tam[1] / tam[0])))
                r = max(tam[0] / im.width, tam[1] / im.height)    # llenar la pantalla, recortando al centro
                im = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
                cx, cy = (im.width - tam[0]) // 2, (im.height - tam[1]) // 2
                im = im.crop((cx, cy, cx + tam[0], cy + tam[1]))
            frames = round(seg * FPS)
            for f in range(frames):
                cuadro = base.copy()
                pant = im
                if f < 3:                                       # destello del cambio de foto
                    pant = Image.blend(im, Image.new("RGB", tam, "white"), (3 - f) / 3 * 0.85)
                cuadro.paste(pant, (x0, y0))
                s = 1 + ZOOM * k / total
                cw, ch = W / s, H / s
                bx = min(max(cx - cw / 2, 0), W - cw); by = min(max(cy - ch / 2, 0), H - ch)
                cuadro = cuadro.resize((W, H), Image.LANCZOS, box=(bx, by, bx + cw, by + ch))
                cuadro.save(tmp / f"f{k:05d}.jpg", quality=95)
                k += 1
        destino = SALIDA / "reel-camara-9x16.mp4"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", str(FPS), "-i", str(tmp / "f%05d.jpg"),
                        "-c:v", "libx264", "-crf", "17", "-preset", "slow", "-pix_fmt", "yuv420p",
                        "-movflags", "+faststart", str(destino)], check=True)
        print(destino)


if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "camara":
        n = int(args[args.index("--n") + 1]) if "--n" in args else 2
        camara(n)
    elif args and args[0] == "montar":
        montar(args[1])
    else:
        print(__doc__)
