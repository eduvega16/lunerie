"""Serie de Navidad en terciopelo rojo para Instagram (13-nov, Edu: «quiero que subamos mucho contenido, las fotos en un
fondo rojo terciopelado rollo navidad» → «sí dale y programa la subida»). Parte de las fotos de marca/terciopelo.py
(revisadas a tamaño real) y monta, sin IA ni créditos:
    posts 4:5 con una línea de texto · carrusel «Ideas de regalo para Navidad» · historias 9:16 (foto + ficha) · 2 reels
    python marca/navidad_terciopelo.py [posts|carrusel|historias|reels]   → marca/fotos-ia/terciopelo/navidad/
En 9:16 el texto queda fuera de las zonas que tapan los botones de Instagram (arriba ~200 px, abajo ~250 px).
Precios leídos de la tienda el 13-nov (si cambian, cambiarlos aquí y volver a montar).
"""
import pathlib, shutil, subprocess, sys, tempfile
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
from mofu_bofu import jost, cormi

RAIZ = pathlib.Path(__file__).resolve().parent.parent
T = RAIZ / "marca" / "fotos-ia" / "terciopelo"
SAL = T / "navidad"
MUSICA = RAIZ / "marca" / "musica" / "holiday-bells.m4a"
FF = shutil.which("ffmpeg") or __import__("imageio_ffmpeg").get_ffmpeg_exe()
CREMA, ORO_CLARO, GRANATE = (246, 239, 228), (224, 193, 132), (58, 9, 14)

PRODUCTOS = {   # foto: (nombre, precio, una línea verdadera)
    "plano-sara-1": ("Collar Signé", "49,95 €", "Su nombre y la piedra de su mes"),
    "lazo-laura-1": ("Collar Signé", "49,95 €", "Su nombre en letra de firma"),
    "regalo-carmen-1": ("Collar Signé", "49,95 €", "Su nombre y la piedra de su mes"),
    "cajita-carmen-1": ("Collar Signé", "49,95 €", "Llega en su cajita de terciopelo"),
    "plata-elena-1": ("Collar Signé", "49,95 €", "También en plateado"),
    "nombre-ana-1": ("Collar Signé", "49,95 €", "Marzo, azul agua"),
    "nombre-paula-1": ("Collar Signé", "49,95 €", "Abril, blanco"),
    "nombre-eva-1": ("Collar Signé", "49,95 €", "Febrero, morado"),
    "reloj-lune-1": ("Reloj Lune", "39,95 €", "Pequeño, ovalado y con piedras"),
    "reloj-maille-1": ("Reloj Maille", "39,95 €", "Esfera ovalada y malla dorada"),
    "anillo-nuit-1": ("Anillo Nuit", "19,95 €", "Sello con circonita"),
    "aros-boucle-1": ("Aros Boucle", "19,95 €", "Aros dorados en U"),
}
PROMO = ["Black Friday: la 2.ª pieza al 50 %", "y la 3.ª, gratis. Hasta el 5 de diciembre."]

# posts del feed con una línea encima (solo collares: en los relojes la correa llega abajo y el texto la taparía)
POSTS = {"cajita-carmen-1": None,   # la caja llega abajo: el texto la tapaba (va en el pie)
         "plata-elena-1": "Su nombre, en plata.",
         "lazo-laura-1": "Su nombre, bajo el árbol.", "plano-sara-1": "Un regalo que lleva su nombre.",
         "reloj-lune-1": None}
CARRUSEL = ["regalo-carmen-1", "plano-sara-1", "reloj-lune-1", "reloj-maille-1", "anillo-nuit-1", "aros-boucle-1"]
HISTORIAS = {   # foto: gancho (una historia por día: la foto con el gancho + la ficha con precio y promo)
    "cajita-carmen-1": "Así llega: en su cajita de terciopelo.",
    "plano-sara-1": "¿Y si este año le regalas su nombre?",
    "reloj-lune-1": "Un reloj que solo da la hora.",
    "lazo-laura-1": "Su nombre, bajo el árbol.",
    "nombre-ana-1": "¿En qué mes nació? Marzo es azul agua.",
    "plata-elena-1": "¿Dorado o plateado?",
    "aros-boucle-1": "Para llevar cada día.",
    "nombre-paula-1": "¿En qué mes nació? Abril es blanco.",
    "regalo-carmen-1": "Un regalo que lleva su nombre.",
    "nombre-eva-1": "¿En qué mes nació? Febrero es morado.",
    "anillo-nuit-1": "El detalle que suma al regalo.",
}
REELS = {
    "reel-nombre-arbol": [("lazo-laura-1", 2.2, "Su nombre, bajo el árbol."), ("plano-sara-1", 1.3, None),
                          ("nombre-ana-1", 1.3, None), ("nombre-paula-1", 1.3, None), ("nombre-eva-1", 1.3, None),
                          ("plata-elena-1", 1.3, None), ("cajita-carmen-1", 2.0, "En su cajita de terciopelo."),
                          ("ficha:cajita-carmen-1", 2.8, None)],
    "reel-ideas-regalo": [("regalo-carmen-1", 2.0, "Ideas de regalo para Navidad"),
                          ("plano-sara-1", 1.6, "Collar Signé · 49,95 €"), ("reloj-lune-1", 1.6, "Reloj Lune · 39,95 €"),
                          ("reloj-maille-1", 1.6, "Reloj Maille · 39,95 €"), ("anillo-nuit-1", 1.6, "Anillo Nuit · 19,95 €"),
                          ("aros-boucle-1", 1.6, "Aros Boucle · 19,95 €"), ("ficha:regalo-carmen-1", 2.8, None)],
}


def foto(n):
    """El .png original o, en el otro PC (los .png no van a git), el .jpg."""
    png = T / f"{n}.png"
    return Image.open(png if png.exists() else T / f"{n}.jpg").convert("RGB")


def a_45(im):
    w, h = im.size
    alto = round(w * 1.25)
    y = (h - alto) // 2
    return im.crop((0, y, w, y + alto)).resize((1080, 1350), Image.LANCZOS)


def ancho(d, texto, fuente, esp=0):
    return sum(d.textlength(c, font=fuente) for c in texto) + esp * (len(texto) - 1) if esp else d.textlength(texto, font=fuente)


def escribir(im, lineas, sombra=True):
    """lineas: [(y, texto, fuente, color, espaciado)] centradas. Sombra suave debajo para que se lea sobre el terciopelo."""
    capa = Image.new("RGBA", im.size, (0, 0, 0, 0))
    som = Image.new("RGBA", im.size, (0, 0, 0, 0))
    d, ds = ImageDraw.Draw(capa), ImageDraw.Draw(som)
    for y, texto, fuente, color, esp in lineas:
        x = (im.width - ancho(d, texto, fuente, esp)) / 2
        for c in (texto if esp else [texto]):
            ds.text((x + 2, y + 3), c, font=fuente, fill=(0, 0, 0, 170))
            d.text((x, y), c, font=fuente, fill=color + (255,))
            x += d.textlength(c, font=fuente) + esp if esp else 0
    base = im.convert("RGBA")
    if sombra:
        base = Image.alpha_composite(base, som.filter(ImageFilter.GaussianBlur(6)))
    return Image.alpha_composite(base, capa).convert("RGB")


def degradado_abajo(im, desde, fuerza=150):
    capa = Image.new("L", im.size, 0)
    d = ImageDraw.Draw(capa)
    for y in range(desde, im.height):
        d.line([(0, y), (im.width, y)], fill=int(fuerza * (y - desde) / (im.height - desde)))
    negro = Image.new("RGB", im.size, (20, 2, 5))
    return Image.composite(negro, im, capa)


def guardar(im, nombre):
    SAL.mkdir(parents=True, exist_ok=True)
    im.save(SAL / nombre, quality=96, subsampling=0)
    return SAL / nombre


# ---------- feed ----------
def posts():
    for n, frase in POSTS.items():
        im = a_45(foto(n))
        if frase:
            im = degradado_abajo(im, 1000)
            nombre, precio, _ = PRODUCTOS[n]
            im = escribir(im, [(1158, frase, cormi(60), CREMA, 0),
                               (1248, f"{nombre.upper()} · {precio}", jost(27, "Regular"), ORO_CLARO, 3)])
        print(guardar(im, f"post-{n}.jpg"))


def diapositiva(n):
    """Foto arriba (1080×1110) y franja granate abajo con nombre, precio y una línea."""
    im = Image.new("RGB", (1080, 1350), GRANATE)
    f = foto(n).resize((1080, 1446), Image.LANCZOS)
    y0 = (1446 - 1110) // 2
    im.paste(f.crop((0, y0, 1080, y0 + 1110)), (0, 0))
    nombre, precio, linea = PRODUCTOS[n]
    return escribir(im, [(1140, f"{nombre} · {precio}", cormi(58), CREMA, 0),
                         (1228, linea.upper(), jost(24, "Regular"), ORO_CLARO, 3)], sombra=False)


def carrusel():
    portada = degradado_abajo(a_45(foto(CARRUSEL[0])), 820, 175)
    portada = escribir(portada, [(1068, "Ideas de regalo", cormi(84), CREMA, 0),
                                 (1158, "para Navidad", cormi(84), CREMA, 0),
                                 (1268, "DE 19,95 € A 49,95 €", jost(26, "Regular"), ORO_CLARO, 4)])
    print(guardar(portada, "car-1.jpg"))
    for i, n in enumerate(CARRUSEL[1:], 2):
        print(guardar(diapositiva(n), f"car-{i}.jpg"))
    fin = ImageEnhance.Brightness(a_45(foto("cajita-carmen-1")).filter(ImageFilter.GaussianBlur(14))).enhance(0.45)
    fin = escribir(fin, [(470, "BLACK FRIDAY", jost(34, "Regular"), ORO_CLARO, 6),
                         (540, "La 2.ª pieza al 50 %", cormi(76), CREMA, 0),
                         (630, "y la 3.ª, gratis.", cormi(76), CREMA, 0),
                         (770, "Mezcla relojes y joyas · Hasta el 5 de diciembre", jost(28), CREMA, 0),
                         (830, "Envío gratis a península", jost(28), CREMA, 0),
                         (960, "LUNERIE.ES", jost(26, "Regular"), ORO_CLARO, 6)])
    print(guardar(fin, f"car-{len(CARRUSEL) + 1}.jpg"))


# ---------- 9:16 ----------
def fondo_916(f):
    """La misma foto, ampliada para cubrir 9:16, borrosa y oscurecida."""
    alto = 1920
    g = f.resize((round(f.width * alto / f.height), alto), Image.LANCZOS)
    x = (g.width - 1080) // 2
    g = g.crop((x, 0, x + 1080, alto)).filter(ImageFilter.GaussianBlur(28))
    return ImageEnhance.Brightness(g).enhance(0.5)


def partir(texto, fuente, maximo, d):
    palabras, lineas, actual = texto.split(), [], ""
    for p in palabras:
        prueba = (actual + " " + p).strip()
        if d.textlength(prueba, font=fuente) > maximo and actual:
            lineas.append(actual); actual = p
        else:
            actual = prueba
    return lineas + [actual]


def historia_foto(n, gancho, y_foto=400):
    f = foto(n)
    im = fondo_916(f)
    im.paste(f.resize((1080, 1446), Image.LANCZOS), (0, y_foto))
    if gancho:
        fu = cormi(64)
        lineas = partir(gancho, fu, 940, ImageDraw.Draw(im))
        y = y_foto - 40 - 74 * len(lineas)
        im = escribir(im, [(y + 74 * i, l, fu, CREMA, 0) for i, l in enumerate(lineas)])
    return im


def ficha(n):
    """Historia de cierre: la foto en pequeño con filo dorado, nombre, precio, la promo y «Enlace en el perfil»."""
    f = foto(n)
    im = fondo_916(f)
    mini = f.resize((600, 804), Image.LANCZOS)
    marco = Image.new("RGB", (606, 810), ORO_CLARO)
    marco.paste(mini, (3, 3))
    im.paste(marco, ((1080 - 606) // 2, 250))
    nombre, precio, linea = PRODUCTOS[n]
    return escribir(im, [(1105, nombre, cormi(88), CREMA, 0),
                         (1215, precio, jost(46, "Regular"), CREMA, 0),
                         (1290, linea, jost(32), CREMA, 0),
                         (1395, PROMO[0], jost(33, "Regular"), ORO_CLARO, 0),
                         (1442, PROMO[1], jost(33, "Regular"), ORO_CLARO, 0),
                         (1540, "ENLACE EN EL PERFIL", jost(26, "Regular"), CREMA, 5)])


def historias():
    for n, gancho in HISTORIAS.items():
        print(guardar(historia_foto(n, gancho), f"st-{n}-1.jpg"))
        print(guardar(ficha(n), f"st-{n}-2.jpg"))


# ---------- reels ----------
def fotograma_reel(paso, texto):
    if paso.startswith("ficha:"):
        return ficha(paso.split(":", 1)[1])
    im = historia_foto(paso, None, y_foto=237)
    if texto:
        im = escribir(im, [(300, texto, cormi(66), CREMA, 0)])
    return im


def reel(nombre, pasos):
    tmp = pathlib.Path(tempfile.mkdtemp())
    clips, fps, fundido = [], 30, 0.3
    for i, (paso, dur, texto) in enumerate(pasos):
        png = tmp / f"{i}.png"
        fotograma_reel(paso, texto).resize((2160, 3840), Image.LANCZOS).save(png)
        clip = tmp / f"{i}.mp4"
        n = round((dur + fundido) * fps)
        subprocess.run([FF, "-v", "error", "-y", "-loop", "1", "-i", str(png), "-vf",
                        f"zoompan=z='1+0.05*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1080x1920:fps={fps},"
                        "format=yuv420p", "-frames:v", str(n), "-c:v", "libx264", "-crf", "17", str(clip)], check=True)
        clips.append((clip, dur + fundido))
    entradas = sum((["-i", str(c)] for c, _ in clips), [])
    filtros, previo, t = [], "[0:v]", clips[0][1]
    for i in range(1, len(clips)):
        t -= fundido
        filtros.append(f"{previo}[{i}:v]xfade=transition=fade:duration={fundido}:offset={t:.2f}[x{i}]")
        previo, t = f"[x{i}]", t + clips[i][1]
    total = t
    filtros.append(f"[{len(clips)}:a]atrim=start=0.5:duration={total:.2f},asetpts=PTS-STARTPTS,"
                   f"afade=t=in:d=0.4,afade=t=out:st={total - 1.4:.2f}:d=1.4,loudnorm=I=-14:TP=-1.5[a]")
    salida = SAL / f"{nombre}.mp4"
    subprocess.run([FF, "-v", "error", "-y", *entradas, "-i", str(MUSICA), "-filter_complex", ";".join(filtros),
                    "-map", previo, "-map", "[a]", "-c:v", "libx264", "-crf", "18", "-preset", "slow", "-pix_fmt",
                    "yuv420p", "-c:a", "aac", "-b:a", "192k", "-t", f"{total:.2f}", "-movflags", "+faststart",
                    str(salida)], check=True)
    print(f"{salida} ({total:.1f} s)")


def reels():
    SAL.mkdir(parents=True, exist_ok=True)
    for nombre, pasos in REELS.items():
        reel(nombre, pasos)


if __name__ == "__main__":
    que = sys.argv[1:] or ["posts", "carrusel", "historias", "reels"]
    for q in que:
        {"posts": posts, "carrusel": carrusel, "historias": historias, "reels": reels}[q]()
