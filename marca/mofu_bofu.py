"""Anuncios MOFU y BOFU del Collar Signé (biblioteca/funnel-meta.json, 9-nov). Sin créditos de IA: foto 1 de la ficha
(producto-verde-3, «Carmen» verde), las 12 gotas y la grabación de la ficha (marca/grabar_vista_previa.py).
    python marca/mofu_bofu.py  → marca/fotos-ia/campana-bf/
      23-cierre-9x16.jpg / -4x5.jpg        BOFU: estático de cierre con la oferta real (fin 5-dic)
      24-dudas-1..6.jpg (4:5)              MOFU: carrusel de dudas
      25-vista-previa-9x16.mp4 / -4x5.mp4  MOFU: grabación de pantalla (elegir piedra → escribir el nombre)
Precios comprobados en Shopify: 1 Signé 49,95 € · 2 = 74,93 € (el 2.º al 50 %, en céntimos hacia abajo) · 3 = 99,90 €.
Solo cosas verdaderas: el plazo es solo lo que tarda en salir (nunca la suma con el envío), la vista previa es
«orientativa» y la garantía es la legal de 3 años (si llega mal hecho, se rehace).
"""
import json, pathlib, subprocess, tempfile
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import imageio_ffmpeg

RAIZ = pathlib.Path(__file__).resolve().parent.parent
FUENTES = RAIZ / "marca" / "fuentes"
SALIDA = RAIZ / "marca" / "fotos-ia" / "campana-bf"
PANTALLA = SALIDA / "pantalla"
FOTO = RAIZ / "marca" / "fotos-ia" / "collar" / "producto-verde-3.jpg"
GOTAS = RAIZ / "marca" / "fotos-ia" / "lagrimas"
FONDO, TINTA, GRIS, ORO, ROJO = (244, 246, 243), (22, 32, 27), (52, 62, 57), (166, 131, 74), (202, 56, 1)
MESES = "Enero Febrero Marzo Abril Mayo Junio Julio Agosto Septiembre Octubre Noviembre Diciembre".split()


def f(nombre, tam, peso="Regular"):
    x = ImageFont.truetype(str(FUENTES / nombre), tam)
    try:
        x.set_variation_by_name(peso)
    except Exception:
        pass
    return x


def jost(t, p="Light"): return f("Jost.ttf", t, p)
def corm(t): return f("Cormorant.ttf", t, "Medium")
def cormi(t): return f("Cormorant-Italic.ttf", t, "Medium")


def centro(d, y, texto, fuente, color, w, espaciado=0):
    if espaciado:
        ancho = sum(d.textlength(c, font=fuente) for c in texto) + espaciado * (len(texto) - 1)
        x = (w - ancho) / 2
        for c in texto:
            d.text((x, y), c, font=fuente, fill=color)
            x += d.textlength(c, font=fuente) + espaciado
        return
    d.text(((w - d.textlength(texto, font=fuente)) / 2, y), texto, font=fuente, fill=color)


def mixto(d, y, partes, w):
    """Una línea centrada con trozos de distinta letra: [(texto, fuente, color), …]."""
    ancho = sum(d.textlength(t, font=fu) for t, fu, _ in partes)
    x = (w - ancho) / 2
    for t, fu, c in partes:
        d.text((x, y), t, font=fu, fill=c)
        x += d.textlength(t, font=fu)


def parrafo(d, y, texto, fuente, color, w, ancho_max, interlinea=1.35):
    palabras, lineas, l = texto.split(), [], ""
    for p in palabras:
        prueba = (l + " " + p).strip()
        if d.textlength(prueba, font=fuente) > ancho_max and l:
            lineas.append(l)
            l = p
        else:
            l = prueba
    lineas.append(l)
    alto = int(fuente.size * interlinea)
    for i, li in enumerate(lineas):
        centro(d, y + i * alto, li, fuente, color, w)
    return y + len(lineas) * alto


def foto_collar(caja, ancho=None, alto=None):
    im = Image.open(FOTO).convert("RGB").crop(caja)
    if ancho:
        return im.resize((ancho, round(im.height * ancho / im.width)), Image.Resampling.LANCZOS)
    return im.resize((round(im.width * alto / im.height), alto), Image.Resampling.LANCZOS)


def tarjeta(im, lienzo, x, y, radio=26):
    """Pega una captura con esquinas redondeadas y una sombra suave."""
    m = Image.new("L", im.size, 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, im.width - 1, im.height - 1), radio, fill=255)
    sombra = Image.new("RGBA", (im.width + 80, im.height + 80), (0, 0, 0, 0))
    ImageDraw.Draw(sombra).rounded_rectangle((40, 48, im.width + 40, im.height + 48), radio, fill=(22, 32, 27, 46))
    sombra = sombra.filter(ImageFilter.GaussianBlur(18))
    lienzo.paste(sombra, (x - 40, y - 40), sombra)
    lienzo.paste(im, (x, y), m)


def guardar(im, nombre):
    im.save(SALIDA / nombre, quality=97, subsampling=0)
    print(SALIDA / nombre)


# ---------- BOFU: estático de cierre ----------
def cierre(w, h):
    im = Image.new("RGB", (w, h), FONDO)
    d = ImageDraw.Draw(im)
    if h > 1500:   # 9:16: zona libre de Meta = y 270-1248 y 6 % a cada lado; nombre y lágrima dentro
        y = 285
        foto = foto_collar((560, 900, 1960, 2438), alto=600)
        im.paste(foto, ((w - foto.width) // 2, 1240 - foto.height))
        tam_t = 100
    else:          # 4:5: foto arriba y texto abajo
        foto = foto_collar((330, 520, 2150, 2438), alto=880)
        im.paste(foto, ((w - foto.width) // 2, 20))
        y = 930
        tam_t = 96
    d = ImageDraw.Draw(im)
    centro(d, y, "BLACK FRIDAY", jost(32, "Medium"), ROJO, w, espaciado=7)
    y += 58
    mixto(d, y, [("Su nombre, ", corm(tam_t), TINTA), ("su piedra.", cormi(tam_t), TINTA)], w)
    y += int(tam_t * 1.2)
    centro(d, y, "La 2.ª pieza al 50 % y la 3.ª, gratis.", jost(44, "Regular"), TINTA, w)
    y += 70
    centro(d, y, "Collar Signé · 49,95 € · Hasta el 5 de diciembre", jost(34, "Regular"), GRIS, w)
    y += 52
    centro(d, y, "Garantía de 3 años · Envío gratis a península", jost(34, "Regular"), GRIS, w)
    return im


# ---------- MOFU: carrusel de dudas ----------
W, H = 1080, 1350


def base(pregunta):
    im = Image.new("RGB", (W, H), FONDO)
    d = ImageDraw.Draw(im)
    centro(d, 110, "COLLAR SIGNÉ", jost(28, "Medium"), ORO, W, espaciado=7)
    parrafo(d, 165, pregunta, cormi(92), TINTA, W, 900, 1.1)
    return im, d


def respuesta(d, texto, nota=None, y=1045):
    y = parrafo(d, y, texto, jost(40), TINTA, W, 880)
    if nota:
        centro(d, y + 14, nota, jost(28, "Regular"), GRIS, W)


def dudas():
    # 1 · portada
    im = Image.new("RGB", (W, H), FONDO)
    foto = foto_collar((380, 560, 2100, 2438), alto=990)
    im.paste(foto, ((W - foto.width) // 2, 30))
    d = ImageDraw.Draw(im)
    mixto(d, 1060, [("Antes de regalarlo, ", corm(84), TINTA), ("tus dudas.", cormi(84), TINTA)], W)
    centro(d, 1185, "Lo que más nos preguntáis del collar con nombre  →", jost(34, "Regular"), GRIS, W)
    guardar(im, "24-dudas-1.jpg")

    # 2 · el nombre (captura real de la ficha: piedra elegida + nombre escrito + «Se hará así»)
    im, d = base("¿Y si me equivoco con el nombre?")
    cap = Image.open(PANTALLA / "011.png").convert("RGB").crop((0, 735, 1170, 1530))
    cap = cap.resize((900, round(cap.height * 900 / 1170)), Image.Resampling.LANCZOS)
    tarjeta(cap, im, 90, 395)
    d = ImageDraw.Draw(im)
    respuesta(d, "Lo ves escrito mientras lo tecleas y, debajo, cómo se hará. Se hace tal cual lo escribes, "
                 "mayúsculas y tildes incluidas.", "Vista previa orientativa de la letra.", y=1060)
    guardar(im, "24-dudas-2.jpg")

    # 3 · la piedra
    im, d = base("¿Qué piedra le pongo?")
    lado, sep_x, sep_y, x0, y0 = 120, 160, 190, 0, 400
    x0 = (W - (5 * sep_x + lado)) // 2
    for i, mes in enumerate(MESES):
        fila, col = divmod(i, 6)
        g = Image.open(GOTAS / f"lagrima-{i + 1:02d}.png").convert("RGBA")
        g.thumbnail((lado, lado), Image.Resampling.LANCZOS)
        gx = x0 + col * sep_x + (lado - g.width) // 2
        gy = y0 + fila * (sep_y + 110) + (lado - g.height) // 2
        im.paste(g, (gx, gy), g)
        etiqueta = mes[:3] + "."
        fu = jost(28)
        d.text((x0 + col * sep_x + (lado - d.textlength(etiqueta, font=fu)) / 2, y0 + fila * (sep_y + 110) + lado + 18),
               etiqueta, font=fu, fill=GRIS)
    respuesta(d, "Una lágrima para cada mes: la de su mes de nacimiento. Y el collar, en dorado o plateado.",
              "Circonita · colores orientativos", y=1000)
    guardar(im, "24-dudas-3.jpg")

    # 4 · el plazo (solo lo que tarda en salir)
    im, d = base("¿Cuánto tarda?")
    centro(d, 390, "3-5", cormi(330), ORO, W)
    centro(d, 790, "DÍAS LABORABLES", jost(34, "Medium"), TINTA, W, espaciado=7)
    respuesta(d, "Se hace para ti y sale en 3-5 días laborables. Envío gratis a península, con seguimiento.", y=930)
    guardar(im, "24-dudas-4.jpg")

    # 5 · la garantía
    im, d = base("¿Y si algo no está bien?")
    centro(d, 390, "3 años", cormi(300), ORO, W)
    centro(d, 790, "DE GARANTÍA", jost(34, "Medium"), TINTA, W, espaciado=7)
    respuesta(d, "Si llega mal hecho o con algún fallo, escríbenos y lo rehacemos.", y=930)
    guardar(im, "24-dudas-5.jpg")

    # 6 · la oferta
    im = Image.new("RGB", (W, H), FONDO)
    d = ImageDraw.Draw(im)
    centro(d, 200, "BLACK FRIDAY", jost(34, "Medium"), ROJO, W, espaciado=8)
    parrafo(d, 275, "La segunda pieza al 50 % y la tercera, gratis.", cormi(96), TINTA, W, 860, 1.08)
    y = 600
    for izq, der in [("1 collar", "49,95 €"), ("2 collares", "74,93 €"), ("3 collares", "99,90 €")]:
        d.line((190, y + 78, 890, y + 78), fill=(214, 220, 216), width=2)
        d.text((190, y), izq, font=jost(46), fill=TINTA)
        fu = jost(46, "Regular")
        d.text((890 - d.textlength(der, font=fu), y), der, font=fu, fill=TINTA)
        y += 120
    centro(d, 1010, "Mezcla relojes y joyas: se descuenta solo en la cesta.", jost(34, "Regular"), GRIS, W)
    centro(d, 1062, "Hasta el 5 de diciembre.", jost(34, "Regular"), GRIS, W)
    centro(d, 1180, "Personaliza el tuyo en lunerie.es", jost(36, "Regular"), TINTA, W)
    guardar(im, "24-dudas-6.jpg")


# ---------- MOFU: grabación de pantalla ----------
TEXTOS = {"piedra": ("Elige su piedra.", "Una lágrima para cada mes"),
          "panel": ("Elige su piedra.", "Una lágrima para cada mes"),
          "nombre": ("Escribe su nombre.", "Lo ves en letra de firma"),
          "revisar": ("Revísalo antes de pagar.", "Se hace tal cual lo escribes")}


def fotograma(png, fase, w, h):
    im = Image.new("RGB", (w, h), FONDO)
    d = ImageDraw.Draw(im)
    titulo, sub = TEXTOS[fase]
    if h > 1500:
        yt, ys, ancho, yc = 290, 412, 920, 500
    else:
        yt, ys, ancho, yc = 40, 150, 820, 230
    centro(d, yt, titulo, cormi(96), TINTA, w)
    centro(d, ys, sub, jost(36, "Regular"), GRIS, w)
    if h > 1500:   # 9:16: css y 228-520 (piedra, nombre y «Se hará así»), para que acabe antes de y=1248
        y0 = 960 if fase == "panel" else 684   # con el panel abierto, la fila de mayo entera
        cap = Image.open(png).convert("RGB").crop((0, y0, 1170, y0 + 876))
    else:          # 4:5 (feed, sin botones encima): css y 140-640, con el color y el botón
        cap = Image.open(png).convert("RGB").crop((0, 420, 1170, 1920))
    cap = cap.resize((ancho, round(cap.height * ancho / 1170)), Image.Resampling.LANCZOS)
    if yc + cap.height > h - 20:
        cap = cap.crop((0, 0, cap.width, h - 20 - yc))
    tarjeta(cap, im, (w - ancho) // 2, yc)
    return im


def video(w, h, final, salida):
    tiempos = json.loads((PANTALLA / "tiempos.json").read_text(encoding="utf-8"))
    with tempfile.TemporaryDirectory() as tmp:
        tmp = pathlib.Path(tmp)
        lista = []
        for i, t in enumerate(tiempos):
            p = tmp / f"{i:03d}.png"
            fotograma(PANTALLA / t["f"], t["fase"], w, h).save(p)
            lista.append((p, t["seg"]))
        p = tmp / "final.png"
        final.save(p)
        lista.append((p, 2.8))
        txt = tmp / "lista.txt"
        txt.write_text("".join(f"file '{a.as_posix()}'\nduration {s}\n" for a, s in lista)
                       + f"file '{lista[-1][0].as_posix()}'\n", encoding="utf-8")
        subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
                        "-i", str(txt), "-vf", "fps=30,format=yuv420p", "-c:v", "libx264", "-crf", "16",
                        "-preset", "slow", "-movflags", "+faststart", str(SALIDA / salida)], check=True)
    print(SALIDA / salida, round(sum(s for _, s in lista), 1), "s")


if __name__ == "__main__":
    c916, c45 = cierre(1080, 1920), cierre(1080, 1350)
    guardar(c916, "23-cierre-9x16.jpg")
    guardar(c45, "23-cierre-4x5.jpg")
    dudas()
    video(1080, 1920, c916, "25-vista-previa-9x16.mp4")
    video(1080, 1350, c45, "25-vista-previa-4x5.mp4")
