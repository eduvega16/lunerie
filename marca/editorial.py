"""Piezas «limpias y elegantes» para Instagram y anuncios (referencia de Edu del 19-nov: plantillas de Able,
Monica Vinader, Atolea, Brilliant Earth, Kendra Scott). Sin IA: foto ya revisada + letra de Lunerie.

Reglas de la estética (oficina/referencias/estetica-2026-11-19/README.md):
- foto a sangre que manda; texto corto y centrado en el tercio de arriba (o abajo si arriba está la pieza);
- LUNERIE pequeño en mayúsculas espaciadas · titular en Cormorant fina, la 2.ª línea en cursiva · línea pequeña en
  Jost con mayúsculas espaciadas;
- la oferta, si va, en píldoras de borde fino; nada de bloques de color, emojis ni rojo chillón.

    python marca/editorial.py            # las 4 de muestra en 4:5 y 9:16
"""
import pathlib
from PIL import Image, ImageDraw, ImageFont, ImageFilter

RAIZ = pathlib.Path(__file__).resolve().parent.parent
F = RAIZ / "marca" / "fuentes"
SALIDA = RAIZ / "marca" / "fotos-ia" / "editorial-limpio"
TINTA, BLANCO = (22, 32, 27), (255, 255, 255)


def fuente(nombre, tam, peso=None):
    f = ImageFont.truetype(str(F / nombre), tam)
    if peso:
        f.set_variation_by_name(peso)
    return f


def ancho(txt, f, esp):
    return sum(f.getlength(c) for c in txt) + esp * (len(txt) - 1)


def texto(d, cx, y, txt, f, color, esp=0.0):
    """Texto centrado en cx con espacio entre letras (esp en px). Devuelve la altura de la línea."""
    x = cx - ancho(txt, f, esp) / 2
    for c in txt:
        d.text((x, y), c, font=f, fill=color)
        x += f.getlength(c) + esp
    asc, desc = f.getmetrics()
    return asc + desc


def recorte(im, W, H, foco_y=0.5):
    """Recorta a W×H llenando el lienzo; foco_y = qué altura de la foto se conserva (0 arriba, 1 abajo)."""
    r = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
    x = (im.width - W) // 2
    y = round((im.height - H) * foco_y)
    return im.crop((x, y, x + W, y + H))


def velo(im, arriba=True, fuerza=0.38, alto=0.5, color=(0, 0, 0)):
    """Degradado suave para que el texto se lea (arriba o abajo)."""
    W, H = im.size
    m = Image.new("L", (1, H))
    for y in range(H):
        t = y / (H * alto) if arriba else (H - y) / (H * alto)
        m.putpixel((0, y), round(255 * fuerza * max(0.0, 1 - t) ** 1.6))
    capa = Image.new("RGB", (W, H), color)
    return Image.composite(capa, im, m.resize((W, H)))


def bloque(im, lineas, y0, color, pildoras=None):
    """lineas: [(tipo, texto)] con tipo marca | titulo | cursiva | linea. y0 en fracción del alto."""
    W, H = im.size
    k = W / 1080
    d = ImageDraw.Draw(im)
    estilos = {
        "marca": (fuente("Cormorant.ttf", round(30 * k), b"Medium"), 11 * k, 34 * k),
        "titulo": (fuente("Cormorant.ttf", round(78 * k), b"Light"), 0, -4 * k),
        "cursiva": (fuente("Cormorant-Italic.ttf", round(78 * k), b"Light Italic"), 0, 26 * k),
        "linea": (fuente("Jost.ttf", round(21 * k), b"Regular"), 5.5 * k, 14 * k),
    }
    y = H * y0
    for tipo, txt in lineas:
        f, esp, despues = estilos[tipo]
        y += texto(d, W / 2, y, txt, f, color, esp) + despues
    if pildoras:
        f = fuente("Jost.ttf", round(19 * k), b"Regular")
        esp, alto, sep = 3.5 * k, 46 * k, 14 * k
        anchos = [ancho(p, f, esp) + 44 * k for p in pildoras]
        x = W / 2 - (sum(anchos) + sep * (len(anchos) - 1)) / 2
        y += 10 * k
        for p, a in zip(pildoras, anchos):
            d.rounded_rectangle((x, y, x + a, y + alto), radius=alto / 2, outline=color, width=max(1, round(1.4 * k)))
            asc, desc = f.getmetrics()
            texto(d, x + a / 2, y + (alto - asc - desc) / 2 - 1 * k, p, f, color, esp)
            x += a + sep
    return im


def sobre_color(foto, W, H, color, alto_foto=0.66):
    """La foto abajo y un color liso arriba que se funde con ella (como el anuncio de Monica Vinader)."""
    lienzo = Image.new("RGB", (W, H), color)
    h = round(H * alto_foto)
    ph = recorte(foto, W, h, 0.6)
    m = Image.new("L", (1, h))
    for y in range(h):
        m.putpixel((0, y), round(255 * min(1.0, y / (h * 0.30)) ** 1.3))
    lienzo.paste(ph, (0, H - h), m.resize((W, h)))
    return lienzo


def guardar(im, nombre):
    SALIDA.mkdir(parents=True, exist_ok=True)
    ruta = SALIDA / f"{nombre}.jpg"
    im.save(ruta, quality=95, subsampling=0)
    return ruta


def piezas(W, H, sufijo):
    fc = RAIZ / "marca" / "fotos-ia"
    hechas = []
    alto = H / W  # 1,25 en 4:5; 1,78 en 9:16
    y_arriba = 0.10 if alto < 1.5 else 0.17  # en 9:16, por debajo de la zona que tapa Instagram arriba

    # 1 · puesta, texto blanco sobre la piel (Able «Make it personal»)
    im = recorte(Image.open(fc / "collar/editar-hombro-2.png").convert("RGB"), W, H, 0.55)
    im = velo(im, True, 0.42, 0.55)
    bloque(im, [("marca", "LUNERIE"), ("titulo", "Su nombre,"), ("cursiva", "su piedra."),
                ("linea", "COLLAR SIGNÉ · 39,90 €")], y_arriba, BLANCO)
    hechas.append(guardar(im, f"1-puesta-{sufijo}"))

    # 2 · cajita sobre color liso (Monica Vinader «The gift she's guaranteed to love»)
    foto = Image.open(fc / "terciopelo/cajita-carmen-1.jpg").convert("RGB")
    im = sobre_color(foto, W, H, (74, 10, 16), 0.64 if alto < 1.5 else 0.60)
    bloque(im, [("marca", "LUNERIE"), ("titulo", "El regalo que"), ("cursiva", "lleva su nombre."),
                ("linea", "LLEGA EN SU CAJITA DE TERCIOPELO")], y_arriba, BLANCO)
    hechas.append(guardar(im, f"2-cajita-{sufijo}"))

    # 3 · producto solo sobre su fondo, texto abajo en tinta (Brilliant Earth). La foto se corta justo bajo la
    #     piedra (debajo tiene un reflejo) y se funde con un lienzo del mismo color.
    foto = Image.open(fc / "collar/producto-verde-carmen-v2.jpg").convert("RGB")
    fondo = foto.getpixel((10, 10))
    foto = foto.crop((0, 0, foto.width, round(foto.height * 0.789)))
    im = Image.new("RGB", (W, H), fondo)
    h_foto = round(H * (0.74 if alto < 1.5 else 0.60))
    r = h_foto / foto.height  # entera, sin recortar la piedra; a los lados queda el mismo fondo
    ph = foto.resize((round(foto.width * r), h_foto), Image.LANCZOS)
    ph = velo(ph, False, 1.0, 0.012, fondo)
    if alto < 1.5:  # 4:5: la pieza arriba y el texto abajo
        im.paste(ph, ((W - ph.width) // 2, 0))
        y_txt = 0.775
    else:  # 9:16: el texto arriba (zona libre de Meta: 14-65 % del alto) y la cadena entra fundida
        im.paste(velo(ph, True, 1.0, 0.18, fondo), ((W - ph.width) // 2, round(H * 0.33)))
        y_txt = y_arriba
    bloque(im, [("marca", "LUNERIE"), ("titulo", "Collar Signé"),
                ("linea", "SU NOMBRE EN LETRA DE FIRMA")], y_txt, TINTA)
    hechas.append(guardar(im, f"3-producto-{sufijo}"))

    # 4 · oferta discreta en píldoras (Atolea «Buy 2, get 2 free»), sobre crema y con la foto abajo
    foto = Image.open(fc / "collar/dedos-1.png").convert("RGB")
    im = sobre_color(foto, W, H, (244, 239, 231), 0.62 if alto < 1.5 else 0.58)
    bloque(im, [("marca", "LUNERIE"), ("titulo", "Black Friday"), ("cursiva", "con su nombre.")],
           y_arriba, TINTA, pildoras=["2.ª PIEZA AL 50 %", "3.ª GRATIS"])
    hechas.append(guardar(im, f"4-oferta-{sufijo}"))
    return hechas


if __name__ == "__main__":
    for W, H, s in ((1080, 1350, "4x5"), (1080, 1920, "9x16")):
        for r in piezas(W, H, s):
            print(r)
