"""Carrusel «Tomando decisiones más saludables» (formato 29, como el de @laguacajoyeros; 10-nov, Edu: «como el original,
croissant, chocolate y eso»). A la izquierda un dulce (IA, sobre fondo beige liso) con sus kcal aproximadas de etiqueta;
a la derecha un Collar Signé (fotos ya revisadas, pegadas en local: el nombre no lo toca la IA) con «0 kcal».
    python marca/kcal.py comida [croissant chocolate polvoron donut] [--n 1]   → marca/fotos-ia/kcal/<dulce>-<n>.png
    python marca/kcal.py montar                                                → marca/fotos-ia/kcal/kcal-1..5.jpg (4:5)
"""
import concurrent.futures, pathlib, sys, urllib.request
import numpy as np
from dotenv import load_dotenv
from PIL import Image, ImageDraw, ImageFont

RAIZ = pathlib.Path(__file__).resolve().parent.parent
load_dotenv(RAIZ / ".env.local")
import higgsfield_client  # noqa: E402

SALIDA = RAIZ / "marca" / "fotos-ia" / "kcal"
F = RAIZ / "marca" / "fuentes"
BEIGE = (238, 227, 213)
TINTA, GRIS, ORO = (22, 32, 27), (60, 58, 52), (166, 131, 74)
FONDO = ("Minimal studio product photograph on a seamless, perfectly plain warm beige paper backdrop (colour #EEE3D5), "
         "soft diffused light from the left, a soft natural shadow on the floor. {cosa} sits alone in the centre of the "
         "frame, seen from a slightly low front angle, sharp, appetising and real, filling about half of the frame "
         "width. Leave generous empty beige space around it. No text, no logo, no brand, no plate, no props.")
COMIDA = {
    "croissant": "A single golden, flaky all-butter croissant",
    "chocolate": "A milk chocolate bar, partly unwrapped from plain gold foil, with two squares broken off next to it",
    "polvoron": "A single traditional Spanish polvoron (round, crumbly, pale golden shortbread dusted with powdered "
                "sugar) half unwrapped from its thin white tissue paper with twisted ends",
    "donut": "A single glazed ring doughnut with a shiny sugar glaze",
}
# (dulce, kcal aproximadas por pieza según etiquetas típicas, nota, joya)
COLLAR = RAIZ / "marca" / "fotos-ia" / "collar"
SLIDES = [
    ("croissant", "unas 240 kcal", "un croissant de mantequilla, 60 g", COLLAR / "producto-verde-3.jpg"),
    ("chocolate", "unas 530 kcal", "una tableta de chocolate con leche, 100 g", COLLAR / "post-nombre-laura-azul-2.jpg"),
    ("polvoron", "unas 130 kcal", "un polvorón, 25 g", RAIZ / "marca" / "fotos-ia" / "cada-una" / "plateado-elena-1.png"),
    ("donut", "unas 250 kcal", "un donut glaseado, 60 g", COLLAR / "post-nombre-alba-rojo-1.jpg"),
]


def generar(dulce, n):
    try:
        r = higgsfield_client.subscribe("marketing-studio/image/flare", arguments={
            "prompt": FONDO.format(cosa=COMIDA[dulce]), "image_urls": [], "aspect_ratio": "3:4", "resolution": "2k",
            "quality": "high", "enhance_prompt": False})
        url = ((r or {}).get("images") or [{}])[0].get("url")
        if not url:
            return dulce, f"SIN IMAGEN {r}"
        destino = SALIDA / f"{dulce}-{n}.png"
        urllib.request.urlretrieve(url, destino)
        return dulce, str(destino)
    except Exception as e:
        return dulce, f"ERROR {e}"


def fuente(nombre, tam, peso=None):
    f = ImageFont.truetype(str(F / nombre), tam)
    if peso:
        try:
            f.set_variation_by_axes([peso])
        except Exception:
            pass
    return f


def espaciado(d, xy_centro, texto, f, color, sep):
    ancho = sum(d.textlength(c, font=f) for c in texto) + sep * (len(texto) - 1)
    x, y = xy_centro[0] - ancho / 2, xy_centro[1]
    for c in texto:
        d.text((x, y), c, font=f, fill=color); x += d.textlength(c, font=f) + sep


def joya(ruta, alto):
    """La foto del collar (fondo blanco o niebla) pasada al beige multiplicando: el fondo desaparece."""
    im = Image.open(ruta).convert("RGB")
    w, h = im.size
    if "post-" in ruta.name:                       # los posts llevan texto abajo: fuera
        im = im.crop((0, 0, w, round(h * 0.80)))
    elif ruta.name == "producto-verde-3.jpg":      # sin el reflejo de debajo de la lágrima
        im = im.crop((0, 0, w, round(h * 0.787)))
    a = np.asarray(im).astype(float)
    fondo = np.median(np.concatenate([a[:20, :20].reshape(-1, 3), a[:20, -20:].reshape(-1, 3)]), axis=0)
    a = np.clip(a / np.maximum(fondo, 1) * np.array(BEIGE), 0, 255).astype(np.uint8)
    im = Image.fromarray(a)
    return im.resize((round(im.width * alto / im.height), alto), Image.LANCZOS)


def cabecera(d, W):
    espaciado(d, (W / 2, 120), "TOMANDO DECISIONES", fuente("Jost.ttf", 40, 400), TINTA, 9)
    t = "más saludables"
    f = fuente("Cormorant-Italic.ttf", 92)
    d.text(((W - d.textlength(t, font=f)) / 2, 170), t, font=f, fill=TINTA)


def montar():
    W, H = 1080, 1350
    for i, (dulce, kcal, nota, ruta_joya) in enumerate(SLIDES, 1):
        im = Image.new("RGB", (W, H), BEIGE)
        d = ImageDraw.Draw(im)
        cabecera(d, W)
        comida = Image.open(SALIDA / f"{dulce}-1.png").convert("RGB")
        a = np.asarray(comida).astype(float)                       # el beige de la IA, igualado al de la página
        fondo = np.median(a[:40].reshape(-1, 3), axis=0)
        comida = Image.fromarray(np.clip(a / np.maximum(fondo, 1) * np.array(BEIGE), 0, 255).astype(np.uint8))
        cw = 500; comida = comida.resize((cw, round(comida.height * cw / comida.width)), Image.LANCZOS)
        y0 = 330
        borde = 70                                                  # bordes fundidos: no se nota el recuadro
        m = np.ones((comida.height, cw))
        for k in range(borde):
            v = (k + 1) / borde
            m[k, :] = np.minimum(m[k, :], v); m[-k - 1, :] = np.minimum(m[-k - 1, :], v)
            m[:, k] = np.minimum(m[:, k], v); m[:, -k - 1] = np.minimum(m[:, -k - 1], v)
        mascara = Image.fromarray((m * 255).astype(np.uint8))
        im.paste(comida, (20, y0 + (700 - comida.height) // 2), mascara)
        j = joya(ruta_joya, 640)
        if j.width > 470:
            j = j.resize((470, round(j.height * 470 / j.width)), Image.LANCZOS)
        im.paste(j, (round(W * 0.75 - j.width / 2), y0 + 30))
        d.line((W / 2, y0 + 20, W / 2, y0 + 700), fill=ORO, width=2)
        fk = fuente("Jost.ttf", 46, 300)
        espaciado(d, (W * 0.25, 1085), kcal, fk, TINTA, 3)
        espaciado(d, (W * 0.75, 1085), "0 kcal", fk, TINTA, 3)
        fn = fuente("Jost.ttf", 24, 400)
        for x, t in ((W * 0.25, nota), (W * 0.75, "Collar Signé")):
            d.text((x - d.textlength(t, font=fn) / 2, 1160), t, font=fn, fill=GRIS)
        d.text((W - 60 - d.textlength(f"{i}/5", font=fn), 1270), f"{i}/5", font=fn, fill=GRIS)
        im.save(SALIDA / f"kcal-{i}.jpg", quality=97, subsampling=0); print("kcal", i)
    # 5 · cierre
    im = Image.new("RGB", (W, H), BEIGE)
    d = ImageDraw.Draw(im)
    j = joya(COLLAR / "producto-verde-3.jpg", 620)
    im.paste(j, (round((W - j.width) / 2), 150))
    f1 = fuente("Cormorant-Italic.ttf", 74)
    for k, t in enumerate(("Si vas a darte un capricho,", "que dure.")):
        d.text(((W - d.textlength(t, font=f1)) / 2, 830 + k * 90), t, font=f1, fill=TINTA)
    espaciado(d, (W / 2, 1050), "COLLAR SIGNÉ · 49,95 €", fuente("Jost.ttf", 32, 400), TINTA, 5)
    f3 = fuente("Jost.ttf", 28, 400)
    for k, t in enumerate(("Black Friday: la 2.ª pieza al 50 % y la 3.ª, gratis.", "Hasta el 5 de diciembre.")):
        d.text(((W - d.textlength(t, font=f3)) / 2, 1115 + k * 44), t, font=f3, fill=GRIS)
    fn = fuente("Jost.ttf", 22, 400)
    t = "Kcal aproximadas por pieza, según etiquetas habituales."
    d.text(((W - d.textlength(t, font=fn)) / 2, 1260), t, font=fn, fill=GRIS)
    im.save(SALIDA / "kcal-5.jpg", quality=97, subsampling=0); print("kcal 5")


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "comida":
        veces = 1
        if "--n" in a:
            i = a.index("--n"); veces = int(a[i + 1]); del a[i:i + 2]
        SALIDA.mkdir(parents=True, exist_ok=True)
        trabajos = [(c, n) for c in (a[1:] or list(COMIDA)) for n in range(1, veces + 1)]
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
            for dulce, r in ex.map(lambda t: generar(*t), trabajos):
                print(dulce, "->", r, flush=True)
    elif a and a[0] == "montar":
        montar()
    else:
        print(__doc__)
