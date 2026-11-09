"""Textos en local (con la letra de Lunerie) sobre las fotos de collar_cada_una.py (9-nov). La IA deja los papeles y la
caja en blanco; aquí se escribe encima, siguiendo el giro del papel o de la franja, así no hay faltas.
    python marca/textos_cada_una.py   → marca/fotos-ia/cada-una/post-*.jpg (4:5, 1080×1350)
"""
import math, pathlib
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont

RAIZ = pathlib.Path(__file__).resolve().parent.parent
D = RAIZ / "marca" / "fotos-ia" / "cada-una"
F = RAIZ / "marca" / "fuentes"
TINTA, GRIS, ORO, ROJO, BLANCO = (22, 32, 27), (52, 62, 57), (166, 131, 74), (202, 56, 1), (255, 255, 255)
CARRUSEL = [("circulo-marta-azul-2", "para mamá", None), ("editar-elena-rojo-1", "para tu hermana", None),
            ("circulo-sara-verde-1", "para tu mejor amiga", None),
            ("circulo-laura-rosa-1", "para ti", "La 2.ª, a mitad de precio")]


def fuente(nombre, tam, peso=None):
    f = ImageFont.truetype(str(F / nombre), tam)
    if peso:
        try:
            f.set_variation_by_axes([peso])
        except Exception:
            pass
    return f


def a_45(im):
    """Recorte central a 4:5 y a 1080×1350."""
    w, h = im.size
    if h / w > 1.25:
        alto = round(w * 1.25); y = (h - alto) // 2; im = im.crop((0, y, w, y + alto))
    else:
        ancho = round(h / 1.25); x = (w - ancho) // 2; im = im.crop((x, 0, x + ancho, h))
    return im.resize((1080, 1350), Image.LANCZOS)


def rectangulo(mascara):
    """Centro, tamaño y giro (grados, sentido de PIL) de la mancha más grande de la máscara."""
    n, et, st, _ = cv2.connectedComponentsWithStats(mascara.astype(np.uint8))
    k = 1 + int(np.argmax(st[1:, cv2.CC_STAT_AREA]))
    ys, xs = np.nonzero(et == k)
    (cx, cy), (w, h), ang = cv2.minAreaRect(np.column_stack([xs, ys]).astype(np.float32))
    if w < h:
        w, h, ang = h, w, ang - 90
    while ang > 45: ang -= 90
    while ang < -45: ang += 90
    if abs(ang) > 30 and w / h < 1.3:   # casi cuadrado: el giro pequeño es el bueno
        ang = ang - 90 if ang > 0 else ang + 90
    return (cx, cy), (w, h), -ang


def giro_papel(mascara):
    """Giro del papel por sus bordes de arriba y de abajo (el de minAreaRect sale de más con los bordes rotos)."""
    m = mascara.astype(np.uint8)
    n, et, st, _ = cv2.connectedComponentsWithStats(m)
    k = 1 + int(np.argmax(st[1:, cv2.CC_STAT_AREA]))
    cs, _ = cv2.findContours((et == k).astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    c = max(cs, key=cv2.contourArea)
    q = cv2.approxPolyDP(c, 0.04 * cv2.arcLength(c, True), True).reshape(-1, 2).astype(float)
    if len(q) != 4:
        return None
    q = q[np.argsort(q[:, 1])]
    angulos = []
    for a, b in (q[:2], q[2:]):
        a, b = sorted((a, b), key=lambda v: v[0])
        angulos.append(np.degrees(np.arctan2(-(b[1] - a[1]), b[0] - a[0])))
    return float(np.mean(angulos))


def texto_girado(im, centro, giro, lineas):
    """lineas: [(texto, fuente, color, sep_despues)] centradas en `centro` y giradas `giro` grados."""
    capa = Image.new("RGBA", (im.width, im.height), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    alturas = [d.textbbox((0, 0), t, font=f)[3] for t, f, _, _ in lineas]
    total = sum(alturas) + sum(s for *_, s in lineas[:-1])
    y = im.height / 2 - total / 2
    for (t, f, c, s), a in zip(lineas, alturas):
        d.text((im.width / 2 - d.textlength(t, font=f) / 2, y), t, font=f, fill=c); y += a + s
    capa = capa.rotate(giro, resample=Image.BICUBIC, center=(im.width / 2, im.height / 2),
                       translate=(centro[0] - im.width / 2, centro[1] - im.height / 2))
    im.paste(capa, (0, 0), capa)


def carrusel():
    for i, (n, para, extra) in enumerate(CARRUSEL, 1):
        im = Image.open(D / f"{n}.png").convert("RGB")
        a = np.asarray(im).astype(int)
        papel = (a.min(axis=2) > 170) & (a.max(axis=2) - a.min(axis=2) < 45)
        centro, (w, h), giro = rectangulo(papel)
        g2 = giro_papel(papel)
        giro = g2 if g2 is not None else giro
        lado = min(w, h)
        f = fuente("Cormorant-Italic.ttf", round(lado * 0.17))
        while ImageDraw.Draw(im).textlength(para, font=f) > lado * 0.74:
            f = fuente("Cormorant-Italic.ttf", f.size - 2)
        lineas = [(para, f, TINTA, round(h * 0.06))]
        if extra:
            lineas.append((extra, fuente("Jost.ttf", round(lado * 0.075), 400), GRIS, 0))
        texto_girado(im, centro, giro, lineas)
        a_45(im).save(D / f"post-cada-una-{i}.jpg", quality=97, subsampling=0)
        print("post-cada-una", i, f"giro {giro:.1f}")


def pie(im, linea1, cursiva, linea2):
    """Dos líneas al pie, como los otros posts del collar."""
    d = ImageDraw.Draw(im)
    f1, f2, f3 = fuente("Jost.ttf", 38, 300), fuente("Cormorant-Italic.ttf", 50), fuente("Jost.ttf", 38, 600)
    a = d.textlength(linea1 + " ", font=f1); b = d.textlength(cursiva, font=f2)
    x = (im.width - a - b) / 2
    d.text((x, 1165), linea1 + " ", font=f1, fill=GRIS); d.text((x + a, 1153), cursiva, font=f2, fill=GRIS)
    d.text(((im.width - d.textlength(linea2, font=f3)) / 2, 1232), linea2, font=f3, fill=TINTA)


def plateado():
    im = Image.open(D / "plateado-elena-1.png").convert("RGB")
    w, h = im.size
    im = im.crop((0, 0, w, round(w * 1.25))).resize((1080, 1350), Image.LANCZOS)
    pie(im, "TAMBIÉN EN", "plateado", "COLLAR CON SU NOMBRE Y SU PIEDRA")
    im.save(D / "post-plateado-elena.jpg", quality=97, subsampling=0); print("post-plateado-elena")


def prospecto():
    im = a_45(Image.open(D / "prospecto-1.png").convert("RGB"))
    a = np.asarray(im).astype(int)
    verde = (a[..., 1] > a[..., 0] + 40) & (a[..., 1] > a[..., 2] + 10) & (a[..., 0] < 90)
    centro, (w, h), giro = rectangulo(verde)
    texto_girado(im, centro, giro, [("Signé", fuente("Cormorant-Italic.ttf", round(h * 0.62)), BLANCO, 0)])
    rad = math.radians(giro)
    debajo = (centro[0] + math.sin(rad) * h * 0.95, centro[1] + math.cos(rad) * h * 0.95)
    texto_girado(im, debajo, giro, [("1 collar · vía: cuello", fuente("Jost.ttf", round(h * 0.2), 400), GRIS, 0)])
    d = ImageDraw.Draw(im)
    for t, f, y, c in (("Posología: llevar a diario.", fuente("Cormorant-Italic.ttf", 58), 70, TINTA),
                       ("Efectos secundarios: que te pregunten", fuente("Jost.ttf", 32, 400), 160, GRIS),
                       ("dónde lo has comprado.", fuente("Jost.ttf", 32, 400), 204, GRIS)):
        d.text(((im.width - d.textlength(t, font=f)) / 2, y), t, font=f, fill=c)
    im.save(D / "post-prospecto.jpg", quality=97, subsampling=0); print("post-prospecto", f"franja giro {giro:.1f}")


def kcal():
    W, H = 1080, 1350
    fondo = (244, 246, 243)
    im = Image.new("RGB", (W, H), fondo)
    d = ImageDraw.Draw(im)
    titulo = fuente("Cormorant-Italic.ttf", 66)
    t = "Decisiones más saludables"
    d.text(((W - d.textlength(t, font=titulo)) / 2, 62), t, font=titulo, fill=TINTA)
    sub = fuente("Jost.ttf", 26, 400); s = "PARA ESTAS FIESTAS"
    d.text(((W - d.textlength(s, font=sub)) / 2, 160), s, font=sub, fill=GRIS)

    def foto(ruta, caja, recorte):
        f = Image.open(ruta).convert("RGB"); w, h = f.size
        f = f.crop(tuple(round(v * (w if i % 2 == 0 else h)) for i, v in enumerate(recorte)))
        f = f.resize((caja[2] - caja[0], caja[3] - caja[1]), Image.LANCZOS)
        a = np.asarray(f).astype(float) * (np.array(fondo) / 255.0)   # el blanco de la foto pasa al fondo de la página
        im.paste(Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)) if "polvoron" in str(ruta) else f, caja[:2])

    foto(D / "polvoron-1.png", (60, 230, 560, 730), (0.0, 0.12, 1.0, 0.87))
    foto(RAIZ / "marca" / "fotos-ia" / "collar" / "producto-verde-3.jpg", (60, 770, 560, 1270), (0.05, 0.18, 0.95, 0.9))
    for y, a, b, c in ((400, "Un polvorón", "unas 130 kcal", "(una pieza de 25 g)"),
                       (940, "Collar Signé", "0 kcal", "y dura más que la Navidad")):
        d.text((610, y), a, font=fuente("Jost.ttf", 30, 400), fill=GRIS)
        d.text((606, y + 44), b, font=fuente("Cormorant.ttf", 86), fill=TINTA)
        d.text((610, y + 150), c, font=fuente("Cormorant-Italic.ttf", 38), fill=GRIS)
    d.line((60, 750, W - 60, 750), fill=ORO, width=2)
    im.save(D / "post-kcal.jpg", quality=97, subsampling=0); print("post-kcal")


if __name__ == "__main__":
    carrusel(); plateado(); prospecto(); kcal()
