"""Anuncios de la campaña de Black Friday (2-nov) a partir de fotos que ya tenemos, sin gastar créditos de IA.

Salen en marca/fotos-ia/campana-bf/: cada anuncio en 4:5 (feed) y 9:16 (Reels/Stories; el texto queda entre el
14 % de arriba y el 35 % de abajo, que Instagram tapa). Precios leídos de la tienda al ejecutar. Uso:
    python marca/campana_bf.py
Reglas: nada de escasez inventada, ni «waterproof», ni precios tachados; la oferta acaba de verdad el 5-dic.
"""
import io, json, pathlib, subprocess, urllib.request
from PIL import Image, ImageDraw, ImageFont

RAIZ = pathlib.Path(__file__).resolve().parent
FOTOS = RAIZ / "fotos-ia"
SALIDA = FOTOS / "campana-bf"
FUENTES = RAIZ / "fuentes"
TINTA, ORO_CLARO, ORO, CREMA, NIEBLA = (22, 32, 27), (201, 166, 107), (166, 131, 74), (231, 225, 214), (242, 244, 242)
FORMATOS = {"4x5": (1080, 1350), "9x16": (1080, 1920)}
OFERTA = "La 2.ª pieza al 50 % y la 3.ª, gratis"


def fuente(nombre, tam, peso):
    f = ImageFont.truetype(str(FUENTES / nombre), tam)
    f.set_variation_by_axes([peso])
    return f


ESTILOS = {  # fuente, tamaño, peso, color, espaciado entre letras (px), mayúsculas
    "ceja": ("Jost.ttf", 30, 450, ORO_CLARO, 7, True),
    "grande": ("Cormorant.ttf", 118, 500, (255, 255, 255), 9, True),
    "titulo": ("Cormorant.ttf", 76, 450, (255, 255, 255), 0, False),
    "cursiva": ("Cormorant-Italic.ttf", 60, 450, CREMA, 0, False),
    "gancho": ("Cormorant-Italic.ttf", 96, 450, (255, 255, 255), 0, False),
    "pie": ("Jost.ttf", 30, 400, CREMA, 1, False),
    "marca": ("Cormorant.ttf", 34, 500, (255, 255, 255), 12, True),
}


def texto_ancho(draw, t, f, esp):
    return sum(draw.textlength(c, font=f) for c in t) + esp * max(len(t) - 1, 0)


def linea(draw, t, estilo, cx, y, ancho_max, color=None, izquierda=None):
    """Pinta una línea centrada en cx (o alineada a la izquierda) y devuelve su alto. Se encoge si no cabe."""
    nombre, tam, peso, col, esp, mayus = ESTILOS[estilo]
    t = t.upper() if mayus else t
    while True:
        f = fuente(nombre, tam, peso)
        w = texto_ancho(draw, t, f, esp)
        if w <= ancho_max or tam < 20:
            break
        tam -= 2
    x = izquierda if izquierda is not None else cx - w / 2
    for c in t:
        draw.text((x, y), c, font=f, fill=color or col)
        x += draw.textlength(c, font=f) + esp
    asc, desc = f.getmetrics()
    return asc + desc


def recorte(img, w, h, fx=0.5, fy=0.5):
    """Recorta a la proporción w:h alrededor del punto (fx, fy) y escala."""
    iw, ih = img.size
    if iw / ih > w / h:
        cw, ch = int(ih * w / h), ih
    else:
        cw, ch = iw, int(iw * h / w)
    x = min(max(int(fx * iw - cw / 2), 0), iw - cw)
    y = min(max(int(fy * ih - ch / 2), 0), ih - ch)
    return img.crop((x, y, x + cw, y + ch)).resize((w, h), Image.LANCZOS)


def degradado(img, y0, y1, alfa=0.9):
    """Oscurece hacia abajo (tinta) entre y0 y y1; por debajo de y1, del todo."""
    w, h = img.size
    capa = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    for y in range(max(y0, 0), h):
        a = alfa * min(max((y - y0) / max(y1 - y0, 1), 0), 1)
        d.line([(0, y), (w, y)], fill=TINTA + (int(255 * a ** 1.3),))
    return Image.alpha_composite(img.convert("RGBA"), capa).convert("RGB")


def bloque(img, lineas, abajo, separacion=14, ancho_max=940, izquierda=None):
    """Pinta las líneas (estilo, texto) de forma que la última acabe en `abajo`."""
    d = ImageDraw.Draw(img)
    altos = []
    for estilo, t in lineas:   # medir
        nombre, tam, peso, *_ = ESTILOS[estilo]
        a, b = fuente(nombre, tam, peso).getmetrics()
        altos.append(a + b)
    y = abajo - sum(altos) - separacion * (len(lineas) - 1)
    for (estilo, t), alto in zip(lineas, altos):
        linea(d, t, estilo, img.width / 2, y, ancho_max, izquierda=izquierda)
        y += alto + separacion
    return img


def foto_con_texto(foto, lineas, formato, fx=0.5, fy=0.5, alto_degradado=None, arriba=False):
    w, h = FORMATOS[formato]
    img = recorte(Image.open(foto).convert("RGB"), w, h, fx, fy)
    if arriba:   # texto arriba (bajo el 14 % que tapa Instagram), cuando la pieza queda a media altura
        img = degradado(img.transpose(Image.FLIP_TOP_BOTTOM), h - int(h * 0.42), h - int(h * 0.12)).transpose(Image.FLIP_TOP_BOTTOM)
        return bloque(img, lineas, int(h * 0.36))
    abajo = h - 80 if formato == "4x5" else int(h * 0.64)
    # en 9:16 el texto queda a media altura: oscurecer menos para no apagar la pieza que suele estar justo encima
    alto_degradado = alto_degradado or (620 if formato == "4x5" else 480)
    img = degradado(img, abajo - alto_degradado, abajo - 80)
    return bloque(img, lineas, abajo)


def tarjeta_oferta(formato, lineas=None):
    w, h = FORMATOS[formato]
    img = Image.new("RGB", (w, h), TINTA)
    lineas = lineas or [("ceja", "Black Friday"), ("grande", "2.ª pieza"), ("grande", "al 50 %"),
                        ("cursiva", "y la 3.ª, gratis"), ("pie", "Mezcla relojes y joyas · hasta el 5 de diciembre"),
                        ("marca", "Lunerie")]
    centro = h / 2 if formato == "4x5" else h * 0.42
    return bloque(img, lineas, int(centro + 260), separacion=18)


def productos():
    datos = json.load(urllib.request.urlopen("https://lunerie.es/products.json?limit=50"))
    return {p["handle"]: p for p in datos["products"]}


def euros(p):
    return p["variants"][0]["price"].replace(".", ",") + " €"


def foto_producto(p, ancho=900):
    url = p["images"][0]["src"] + f"&width={ancho}"
    return Image.open(io.BytesIO(urllib.request.urlopen(url).read())).convert("RGB")


def cuadricula(formato, piezas, prods):
    """«Regalos de menos de 40 €»: fotos reales de producto en niebla, con nombre y precio."""
    w, h = FORMATOS[formato]
    img = Image.new("RGB", (w, h), NIEBLA)
    d = ImageDraw.Draw(img)
    cols = 3
    y = 110 if formato == "4x5" else 250   # en 9:16 todo cabe entre el 13 % y el 65 % (lo que no tapa Instagram)
    y += linea(d, "Black Friday", "ceja", w / 2, y, 940, color=ORO) + 10
    y += linea(d, "Regalos de menos de 40 €", "titulo", w / 2, y, 940, color=TINTA) + 6
    y += linea(d, OFERTA, "pie", w / 2, y, 940, color=TINTA) + 36
    margen, hueco = (60, 22) if formato == "4x5" else (90, 22)
    cw = (w - 2 * margen - hueco * (cols - 1)) // cols
    for i, handle in enumerate(piezas):
        p = prods[handle]
        c, f = i % cols, i // cols
        x0, y0 = margen + c * (cw + hueco), y + f * (cw + 108)
        img.paste(recorte(foto_producto(p), cw, cw), (x0, y0))
        linea(d, p["title"], "pie", x0 + cw / 2, y0 + cw + 12, cw, color=TINTA)
        linea(d, euros(p), "pie", x0 + cw / 2, y0 + cw + 50, cw, color=ORO)
    return img


def guardar(img, nombre):
    SALIDA.mkdir(parents=True, exist_ok=True)
    img.save(SALIDA / f"{nombre}.jpg", quality=92)
    return SALIDA / f"{nombre}.jpg"


def video(nombre, fotogramas, segundos=2.6):
    """Vídeo 9:16 con zoom lento en cada imagen y cortes secos, sin audio (la música se pone en Meta)."""
    entradas, filtros = [], []
    for i, f in enumerate(fotogramas):
        entradas += ["-i", str(f)]   # una sola imagen: zoompan saca de ella los n fotogramas (con -loop saldrían n por cada una)
        n = int(segundos * 30)
        filtros.append(f"[{i}:v]scale=2160:-1,zoompan=z='min(zoom+0.0007,1.05)':d={n}:x='iw/2-(iw/zoom/2)':"
                       f"y='ih/2-(ih/zoom/2)':s=1080x1920:fps=30,setsar=1[v{i}]")
    filtros.append("".join(f"[v{i}]" for i in range(len(fotogramas))) + f"concat=n={len(fotogramas)}:v=1:a=0[out]")
    salida = SALIDA / f"{nombre}.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *entradas, "-filter_complex", ";".join(filtros),
                    "-map", "[out]", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "19", str(salida)], check=True)
    return salida


if __name__ == "__main__":
    prods = productos()
    navidad = FOTOS / "portada-navidad"
    hora = FOTOS / "campana-hora"
    para_ti = FOTOS / "anuncios" / "test-lune" / "para-ti-foto.jpg"
    lune = euros(prods["reloj-lune"])
    hechos = []
    for fmt in FORMATOS:
        # 1 · Oferta con la foto del teléfono
        hechos.append(guardar(foto_con_texto(navidad / "portada-navidad-izquierda.jpg", [
            ("ceja", "Relojes y joyas para regalar"), ("grande", "Black Friday"), ("cursiva", OFERTA),
            ("pie", "Hasta el 5 de diciembre · lunerie.es")], fmt, fy=0.4), f"1-oferta-telefono-{fmt}"))
        # 2 · Pack a juego (Lune + collar Lune), con el precio que sale en la cesta
        total = round(float(prods["reloj-lune"]["variants"][0]["price"]) + float(prods["collar-lune"]["variants"][0]["price"]), 2)
        mitad = int(min(float(prods["reloj-lune"]["variants"][0]["price"]), float(prods["collar-lune"]["variants"][0]["price"])) * 100) // 2
        pack = f"{(int(round(total * 100)) - mitad) / 100:.2f}".replace(".", ",") + " €"
        hechos.append(guardar(foto_con_texto(navidad / "portada-navidad-centro.jpg", [
            ("ceja", "Black Friday · Pack a juego"), ("titulo", "Reloj Lune y collar Lune"),
            ("cursiva", f"{pack} los dos"), ("pie", f"{total:.2f}".replace(".", ",") + " € por separado · lunerie.es")],
            fmt, fx=0.5, fy=0.45), f"2-pack-a-juego-{fmt}"))
        # 6 · Regalos de menos de 40 €
        hechos.append(guardar(cuadricula(fmt, ["reloj-lune", "reloj-sepia", "reloj-galet", "collar-lune",
                                               "pendientes-larme", "aros-boucle"], prods), f"6-menos-de-40-{fmt}"))
        # 7 · Por destinataria (manos con café: valen para cualquier edad)
        for quien in ("madre", "hermana", "pareja"):
            hechos.append(guardar(foto_con_texto(hora / "smartwatch-calma.jpg", [
                ("gancho", f"Para tu {quien}."), ("pie", f"Reloj Lune · {lune}"),
                ("pie", "Black Friday: " + OFERTA.lower().replace("la 2.ª", "2.ª") + " · lunerie.es")], fmt, fy=0.45,
                arriba=fmt == "9x16"),
                f"7-para-tu-{quien}-{fmt}"))
        # 5 · «Para ti» (el que más clics trajo en el test) con el precio nuevo
        hechos.append(guardar(foto_con_texto(para_ti, [
            ("gancho", "Para ti."), ("pie", f"Reloj Lune · {lune}"), ("pie", "No hace falta esperar a que te lo regalen.")],
            fmt, fy=0.5), f"5-para-ti-{fmt}"))
        hechos.append(guardar(tarjeta_oferta(fmt), f"0-tarjeta-oferta-{fmt}"))
    # 3 · Carrusel de Navidad (4:5): las tres fotos con sus piezas y la tarjeta de la oferta
    piezas = {"izquierda": ["reloj-galet", "anillo-nuit", "aros-boucle"],
              "centro": ["reloj-lune", "collar-lune", "reloj-maille"],
              "derecha": ["reloj-sepia", "pendientes-larme"]}
    for n, (lado, hs) in enumerate(piezas.items(), 1):
        w, h = FORMATOS["4x5"]
        img = degradado(recorte(Image.open(navidad / f"portada-navidad-{lado}.jpg").convert("RGB"), w, h, 0.5, 0.42),
                        h - 420, h - 60)
        lineas = [("pie", f"{prods[x]['title']} · {euros(prods[x])}") for x in hs]
        hechos.append(guardar(bloque(img, lineas, h - 70, separacion=8, izquierda=70), f"3-carrusel-{n}-{lado}"))
    hechos.append(guardar(tarjeta_oferta("4x5"), "3-carrusel-4-oferta"))
    # 4 · Vídeo «Un reloj que solo da la hora» (9:16) y su foto para el feed
    f1 = foto_con_texto(hora / "smartwatch-antes.jpg", [("gancho", "Mensajes. Avisos. Pasos.")], "9x16")
    f2 = foto_con_texto(hora / "smartwatch-despues.jpg", [("gancho", "Un reloj que"), ("gancho", "solo da la hora.")], "9x16")
    f3 = foto_con_texto(hora / "smartwatch-calma.jpg", [("ceja", "Reloj Lune"), ("titulo", lune),
                                                        ("pie", "Esfera de 12 mm · piedras verdes · eslabones finos")], "9x16",
                        arriba=True)
    tmp = [guardar(x, f"4-hora-plano-{i}") for i, x in enumerate((f1, f2, f3, tarjeta_oferta("9x16")), 1)]
    hechos.append(video("4-solo-da-la-hora-9x16", tmp))
    hechos.append(guardar(foto_con_texto(hora / "smartwatch-despues.jpg", [
        ("gancho", "Un reloj que solo da la hora."), ("pie", f"Reloj Lune · {lune} · Black Friday: 2.ª pieza al 50 %")],
        "4x5", fy=0.5), "4-solo-da-la-hora-4x5"))
    # 8 · Vídeo de la oferta (9:16): las tres fotos de Navidad y la tarjeta
    planos = []
    for lado in ("izquierda", "centro", "derecha"):
        planos.append(guardar(foto_con_texto(navidad / f"portada-navidad-{lado}.jpg", [
            ("ceja", "Black Friday"), ("pie", " · ".join(f"{prods[x]['title']} {euros(prods[x])}" for x in piezas[lado][:2]))],
            "9x16", fx=0.5, fy=0.4, alto_degradado=420), f"8-oferta-plano-{lado}"))
    planos.append(SALIDA / "0-tarjeta-oferta-9x16.jpg")
    hechos.append(video("8-oferta-navidad-9x16", planos, segundos=2.2))
    print("\n".join(str(x.relative_to(RAIZ.parent)) for x in hechos))
