"""Lámina de las 12 lágrimas del Collar Signé en español (5-nov, Edu: «una foto de todas las lágrimas» en la ficha).

Parte de la tabla en inglés que bajó Edu («BIRTHSTONE CHART», Downloads/LUNERIE/collar personalizable/7.webp, de la web
de Olivia Jewelry, como las otras fotos del collar; Edu asume el riesgo): recorta las 12 gotas tal cual y monta una lámina
4:5 con la letra de Lunerie, el mes y el NOMBRE DEL COLOR (sin nombres de gemas: son circonitas, CLAUDE.md 5.4), los
mismos colores que el selector de la ficha (tema/codigo/snippets/lunerie-collar.liquid).
    python marca/lagrimas.py <tabla.webp>      → marca/fotos-ia/lagrimas/lagrimas-12.jpg
    python marca/lagrimas.py --recortes [<tabla.webp>] [--subir]
        → marca/fotos-ia/lagrimas/lagrima-01..12.png (cada gota sola, con fondo transparente) para el panel «Elige la
          piedra» de la ficha (6-nov, Edu: en Olivia las piedras se ven reales). Con --subir, a Archivos de Shopify con
          ese mismo nombre (el snippet lunerie-collar.liquid las lee con images['lagrima-01.png']).
"""
import pathlib, sys
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont

RAIZ = pathlib.Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "marca" / "fotos-ia" / "lagrimas"
FUENTES = RAIZ / "marca" / "fuentes"
TINTA, GRIS = (22, 32, 27), (107, 116, 111)
MESES = [("Enero", "rojo oscuro"), ("Febrero", "morado"), ("Marzo", "azul agua"), ("Abril", "blanco"),
         ("Mayo", "verde"), ("Junio", "violeta"), ("Julio", "rojo"), ("Agosto", "verde oliva"),
         ("Septiembre", "azul oscuro"), ("Octubre", "rosa"), ("Noviembre", "amarillo"), ("Diciembre", "azul")]


def gotas(ruta):
    """Las 12 gotas de la tabla, en orden de lectura (filas de 4), recortadas con su fondo."""
    im = Image.open(ruta).convert("RGB")
    a = np.asarray(im).astype(np.int16)
    fondo = a[5, 5]
    m = (np.abs(a - fondo).sum(2) > 18).astype(np.uint8)
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((15, 15), np.uint8))
    n, et, st, _ = cv2.connectedComponentsWithStats(m, 8)
    # las gotas son las manchas grandes y más altas que anchas (el texto son manchas bajas y anchas)
    cajas = [tuple(st[i, :4]) for i in range(1, n) if st[i, 3] > 150 and st[i, 2] > 100]
    assert len(cajas) == 12, f"esperaba 12 gotas y salen {len(cajas)}"
    cajas.sort(key=lambda c: (round(c[1] / 200), c[0]))
    return im, tuple(int(v) for v in fondo), cajas


def montar(ruta):
    im, fondo, cajas = gotas(ruta)
    W, H = 1400, 1750
    lam = Image.new("RGB", (W, H), fondo)
    d = ImageDraw.Draw(lam)
    serif = lambda s: ImageFont.truetype(str(FUENTES / "Cormorant.ttf"), s)
    sans = lambda s: ImageFont.truetype(str(FUENTES / "Jost.ttf"), s)

    def centrado(texto, fuente, y, color):
        d.text(((W - d.textlength(texto, font=fuente)) / 2, y), texto, font=fuente, fill=color)

    centrado("Una lágrima para cada mes", serif(84), 110, TINTA)
    centrado("Elige el color de su mes de nacimiento", sans(34), 225, GRIS)
    alto = max(c[3] for c in cajas)
    x_cols = [210, 530, 855, 1180]                     # centros de columna, como en la tabla original
    y_ini, paso = 330, 455
    for k, (x, y, w, h) in enumerate(cajas):
        gota = im.crop((x - 6, y - 6, x + w + 6, y + h + 6))
        cx, top = x_cols[k % 4], y_ini + (k // 4) * paso
        lam.paste(gota, (cx - gota.width // 2, top + (alto - h) // 2))
        mes, color = MESES[k]
        f1, f2 = serif(46), sans(30)
        d.text((cx - d.textlength(mes, font=f1) / 2, top + alto + 26), mes, font=f1, fill=TINTA)
        d.text((cx - d.textlength(color, font=f2) / 2, top + alto + 84), color, font=f2, fill=GRIS)
    centrado("Circonita en forma de lágrima. Los colores en pantalla son orientativos.", sans(28), H - 105, GRIS)
    SALIDA.mkdir(parents=True, exist_ok=True)
    destino = SALIDA / "lagrimas-12.jpg"
    lam.save(destino, quality=97, subsampling=0)
    print(destino, lam.size)


def recortes(ruta, alto=150):
    """Cada gota sola en PNG con transparencia: máscara de la silueta (rellena por dentro, para que el blanco del mes de
    abril no se vuelva transparente) con el borde suavizado."""
    im, fondo, cajas = gotas(ruta)
    a = np.asarray(im).astype(np.int16)
    rutas = []
    for k, (x, y, w, h) in enumerate(cajas):
        p = 10
        x0, y0, x1, y1 = max(x - p, 0), max(y - p, 0), x + w + p, y + h + p
        trozo = a[y0:y1, x0:x1]
        m = (np.abs(trozo - np.array(fondo)).sum(2) > 10).astype(np.uint8) * 255
        m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9)))
        n, et, st, _ = cv2.connectedComponentsWithStats(m, 8)
        m = np.where(et == 1 + int(np.argmax(st[1:, cv2.CC_STAT_AREA])), 255, 0).astype(np.uint8)
        relleno = m.copy()                                   # rellenar huecos: todo lo que no se alcanza desde fuera
        cv2.floodFill(relleno, np.zeros((m.shape[0] + 2, m.shape[1] + 2), np.uint8), (0, 0), 255)
        m = m | cv2.bitwise_not(relleno)
        m = cv2.erode(m, np.ones((2, 2), np.uint8))
        alfa = cv2.GaussianBlur(m, (0, 0), 1.2)
        rgba = np.dstack([trozo.astype(np.uint8), alfa])
        ys, xs = np.nonzero(alfa > 8)
        rgba = rgba[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
        gota = Image.fromarray(rgba, "RGBA")
        gota = gota.resize((round(gota.width * alto / gota.height), alto), Image.LANCZOS)
        SALIDA.mkdir(parents=True, exist_ok=True)
        destino = SALIDA / f"lagrima-{k + 1:02d}.png"
        gota.save(destino, optimize=True)
        rutas.append(destino)
        print(destino.name, gota.size, MESES[k][0])
    return rutas


if __name__ == "__main__":
    args = sys.argv[1:]
    tabla = str(pathlib.Path.home() / "Downloads" / "LUNERIE" / "collar personalizable" / "7.webp")
    if "--recortes" in args:
        args.remove("--recortes")
        subir = "--subir" in args
        if subir:
            args.remove("--subir")
        rutas = recortes(args[0] if args else tabla)
        if subir:
            sys.path.insert(0, str(RAIZ / "anuncios"))
            from subir_creatividades import subir as subir_archivo
            for r in rutas:
                print(r.name, "->", subir_archivo(r)[:90], flush=True)
    else:
        montar(args[0] if args else tabla)
