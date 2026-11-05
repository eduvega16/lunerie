"""Prepara los materiales del vídeo del Collar Signé (5-nov): las 12 gotas de la lámina y las fotos del collar,
en assets/img/ (fuera de git). No usa créditos de IA.
    python marca/anuncios-hf/preparar_collar.py
"""
import pathlib, sys
from PIL import Image

AQUI = pathlib.Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
sys.path.insert(0, str(RAIZ / "marca"))
import lagrimas

IMG = AQUI / "assets" / "img"
IMG.mkdir(parents=True, exist_ok=True)

TABLA = pathlib.Path.home() / "Downloads" / "LUNERIE" / "collar personalizable" / "7.webp"
im, fondo, cajas = lagrimas.gotas(str(TABLA))
print("fondo de la tabla:", fondo)
import numpy as np, cv2
for k, (x, y, w, h) in enumerate(cajas, 1):
    g = im.crop((x - 6, y - 6, x + w + 6, y + h + 6))
    a = np.asarray(g).astype(np.int16)
    m = (np.abs(a - np.array(fondo)).sum(2) > 12).astype(np.uint8)
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
    n, et, st, _ = cv2.connectedComponentsWithStats(m, 8)
    big = 1 + int(np.argmax(st[1:, 4]))
    m = (et == big).astype(np.uint8) * 255
    ff = m.copy(); cv2.floodFill(ff, None, (0, 0), 128)      # rellena huecos (gotas casi blancas)
    m[ff != 128] = 255
    m = cv2.erode(m, np.ones((3, 3), np.uint8))
    m = cv2.GaussianBlur(m, (0, 0), 1.2)
    rgba = Image.fromarray(np.dstack([np.asarray(g), m]), "RGBA")
    rgba = rgba.resize((rgba.width * 2, rgba.height * 2), Image.LANCZOS)
    rgba.save(IMG / f"lagrima-{k:02d}.png")
print("gotas:", len(cajas))

FOTOS = {
    "collar-marta": "marca/fotos-ia/collar/producto-dorado-1.png",
    "collar-carmen": "marca/fotos-ia/collar/editar-hombro-2-reloj.png",
    "collar-elena": "marca/fotos-ia/collar/editar-tirantes-1.png",
    "collar-paula": "marca/fotos-ia/collar/producto-plateado-1.png",
}
for nombre, ruta in FOTOS.items():
    f = Image.open(RAIZ / ruta).convert("RGB")
    f = f.resize((1500, round(f.height * 1500 / f.width)), Image.LANCZOS)
    f.save(IMG / f"{nombre}.jpg", quality=93, subsampling=0)
    print(nombre, f.size)
