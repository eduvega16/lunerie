"""Prepara los anuncios animados de HyperFrames (4-nov, formatos de biblioteca/formatos-anuncio.json).

- Baja de la tienda la 1.ª foto (producto en niebla) y la 2.ª (puesto) de cada pieza → assets/img/<handle>-niebla/puesto.jpg
- Hace una copia de la foto en niebla con el fondo pasado a blanco (<handle>-blanco.jpg): con `mix-blend-mode: multiply`
  sobre cualquier fondo claro, el fondo desaparece y la pieza queda con su sombra.
- Lee los precios reales de lunerie.es y los deja en assets/datos.js (los anuncios los pintan desde ahí: nunca un
  precio viejo). Calcula el pack «A juego» como Shopify (2.ª pieza, la más barata, al 50 %).
    python marca/anuncios-hf/preparar.py
Después: cd marca/anuncios-hf && npx hyperframes render -c <anuncio>.html -o salida/<anuncio>.mp4
"""
import io, json, pathlib, shutil, sys, urllib.request
import cv2
import numpy as np
from PIL import Image

AQUI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent.parent / "productos"))
from gql import gql  # noqa: E402

IMG = AQUI / "assets" / "img"
MARCA = AQUI.parent
# lo que se copia del repo (assets/ entera está fuera de git: se rehace con este script)
COPIAS = {MARCA / "fuentes" / f: AQUI / "assets" / "fonts" / f for f in ("Cormorant.ttf", "Cormorant-Italic.ttf", "Jost.ttf")}
COPIAS.update({MARCA / "logos" / f: IMG / f for f in ("logo-blanco.svg", "logo-tinta.svg", "oficial-avatar-redes.png")})
COPIAS.update({MARCA / "fotos-ia" / "portada-dia" / "revelado" / "izquierda-1.jpg": IMG / "ambiente-cafe.jpg",
               MARCA / "fotos-ia" / "portada-dia" / "revelado" / "derecha-2.jpg": IMG / "ambiente-copa.jpg",
               AQUI / "node_modules" / "hyperframes" / "dist" / "vendor" / "npm" / "gsap@3.15.0" / "dist" / "gsap.min.js":
                   AQUI / "assets" / "gsap.min.js"})
RECORTES = ["collar-lune", "reloj-lune", "anillo-nuit"]   # piezas que se mueven: PNG con fondo transparente
PIEZAS = ["reloj-lune", "collar-lune", "anillo-nuit", "aros-boucle", "reloj-perle", "reloj-galet", "pendientes-larme"]


def bajar(url, ancho=1400):
    req = urllib.request.Request(f"{url}&width={ancho}", headers={"Accept": "image/jpeg", "User-Agent": "Mozilla/5.0"})
    return Image.open(io.BytesIO(urllib.request.urlopen(req).read())).convert("RGB")


def a_blanco(im):
    """Fondo → blanco: divide cada canal por el color del fondo (mediana del borde)."""
    a = np.asarray(im).astype(np.float32)
    b = max(4, a.shape[0] // 60)
    borde = np.concatenate([a[:b].reshape(-1, 3), a[-b:].reshape(-1, 3), a[:, :b].reshape(-1, 3), a[:, -b:].reshape(-1, 3)])
    fondo = np.median(borde, axis=0)
    return Image.fromarray(np.clip(a * (255.0 / fondo), 0, 255).astype(np.uint8))


def recortar(h):
    """Pieza sola, sin fondo ni sombra: oro y piedras (con color) o muy oscuro; huecos cerrados (esfera) rellenos."""
    im = np.asarray(Image.open(IMG / f"{h}-blanco.jpg").convert("RGB"))
    v = cv2.cvtColor(im, cv2.COLOR_RGB2HSV)[..., 2].astype(np.float32) / 255
    lab = cv2.cvtColor(im, cv2.COLOR_RGB2LAB).astype(np.float32)
    croma = np.hypot(lab[..., 1] - 128, lab[..., 2] - 128)
    m = ((((croma > 9) & (v < 0.995)) | (v < 0.45)) * 255).astype(np.uint8)
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
    n, et, st, _ = cv2.connectedComponentsWithStats(255 - m, 8)
    borde = set(np.unique(np.concatenate([et[0], et[-1], et[:, 0], et[:, -1]])))
    for i in range(1, n):
        if i not in borde and st[i, cv2.CC_STAT_AREA] < 0.02 * m.size:
            m[et == i] = 255
    n, et, st, _ = cv2.connectedComponentsWithStats(m, 8)
    for i in range(1, n):
        if st[i, cv2.CC_STAT_AREA] < 60:
            m[et == i] = 0
    a = cv2.GaussianBlur(m, (3, 3), 0)
    ys, xs = np.where(a > 0)
    y0, y1, x0, x1 = max(ys.min() - 20, 0), ys.max() + 20, max(xs.min() - 20, 0), xs.max() + 20
    Image.fromarray(np.dstack([im, a])[y0:y1, x0:x1]).save(IMG / f"{h}-recorte.png")


def precio(handle):
    d = json.load(urllib.request.urlopen(urllib.request.Request(f"https://lunerie.es/products/{handle}.js",
                                                                headers={"User-Agent": "Mozilla/5.0"})))
    return min(v["price"] for v in d["variants"]) / 100


def euros(x):
    return f"{x:.2f}".replace(".", ",") + " €"


if __name__ == "__main__":
    IMG.mkdir(parents=True, exist_ok=True)
    for origen, destino in COPIAS.items():
        destino.parent.mkdir(parents=True, exist_ok=True); shutil.copyfile(origen, destino)
    precios = {}
    for h in PIEZAS:
        p = gql('query($h:String!){productByHandle(handle:$h){media(first:2){nodes{... on MediaImage{image{url}}}}}}',
                {"h": h})["productByHandle"]
        urls = [n["image"]["url"] for n in p["media"]["nodes"]]
        niebla = bajar(urls[0]); niebla.save(IMG / f"{h}-niebla.jpg", quality=95)
        a_blanco(niebla).save(IMG / f"{h}-blanco.jpg", quality=95)
        bajar(urls[1]).save(IMG / f"{h}-puesto.jpg", quality=95)
        if h in RECORTES:
            recortar(h)
        precios[h] = precio(h)
        print(h, euros(precios[h]))
    # pack «A juego» (reloj + collar Lune): la más barata al 50 %, en céntimos y hacia abajo, como el inicio (parte packs)
    a, b = sorted([precios["reloj-lune"], precios["collar-lune"]])
    pack = round(b * 100 + (a * 100 - int(a * 100 / 2))) / 100
    datos = {"precios": {h: euros(x) for h, x in precios.items()},
             "pack_a_juego": {"separado": euros(precios["reloj-lune"] + precios["collar-lune"]), "juntos": euros(pack)}}
    (AQUI / "assets" / "datos.js").write_text("window.LU = " + json.dumps(datos, ensure_ascii=False, indent=1) + ";\n",
                                              encoding="utf8")
    print(json.dumps(datos, ensure_ascii=False))
