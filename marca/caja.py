"""Diseño de la caja de regalo de Lunerie (tipo cajón, blanca): «PARA TI» + destello dorado (elegido el 15-oct).

Composición como la caja «VOGUE» de Nihao / Yiwu Chunshen: LUNERIE grande en vertical a la derecha con el destello
encima, «JOYAS Y RELOJES» pequeño arriba a la izquierda y «PARA TI» en la banda del cajón. Cara de 100 × 100 mm
(ajustar LADO / BANDA a la plantilla del proveedor). Letras convertidas a trazos: no depende de tener las fuentes.
Salida en marca/caja/:
    tapa.pdf / .svg         diseño completo (tinta + oro)
    capa-tinta.pdf / .svg   solo la impresión en negro
    capa-oro.pdf / .svg     solo el destello (cliché del estampado en oro)
    maqueta.png             cómo queda
    python marca/caja.py
"""
import functools, math, pathlib
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
from playwright.sync_api import sync_playwright

DIR = pathlib.Path(__file__).parent
OUT = DIR / "caja"
OUT.mkdir(exist_ok=True)
TINTA, ORO = "#16201B", "#A6834A"
LADO, BANDA = 100, 76  # mm: cara cuadrada; la banda del cajón empieza en y = 76
ARRIBA, FRASE = "JOYAS Y RELOJES", "PARA TI"


@functools.lru_cache(None)
def fuente(nombre, peso):
    return instancer.instantiateVariableFont(TTFont(DIR / "fuentes" / nombre), {"wght": peso})


def texto(cadena, nombre, peso, em_mm, tracking, color):
    """Devuelve (<g> con el texto en trazos, ancho en mm, alto de mayúscula en mm). Origen: línea base, izquierda."""
    f = fuente(nombre, peso)
    gs, cmap, upm = f.getGlyphSet(), f.getBestCmap(), f["head"].unitsPerEm
    trazos, x = [], 0
    for i, ch in enumerate(cadena):
        g = gs[cmap[ord(ch)]]
        pen = SVGPathPen(gs)
        g.draw(pen)
        trazos.append(f'<path transform="translate({x} 0)" d="{pen.getCommands()}"/>')
        x += g.width + (tracking * upm if i < len(cadena) - 1 else 0)
    bp = BoundsPen(gs)
    gs[cmap[ord("H")]].draw(bp)
    s = em_mm / upm
    grupo = f'<g fill="{color}" transform="scale({s} {-s})">{"".join(trazos)}</g>'
    return grupo, x * s, bp.bounds[3] * s


def destello(cx, cy, r, color, finura=3.0):
    pts = []
    for i in range(240):
        t = 2 * math.pi * i / 240
        pts.append((cx + math.copysign(abs(math.cos(t)) ** finura, math.cos(t)) * r,
                    cy + math.copysign(abs(math.sin(t)) ** finura, math.sin(t)) * r))
    return f'<polygon fill="{color}" points="{" ".join(f"{x:.3f},{y:.3f}" for x, y in pts)}"/>'


def tapa(capa=None, guias=False):
    """SVG de la cara de la caja en mm. capa = "tinta" u "oro" deja solo ese acabado."""
    partes = []
    if guias:  # solo para la maqueta: borde de la banda del cajón
        partes.append(f'<line x1="0" y1="{BANDA}" x2="{LADO}" y2="{BANDA}" stroke="#d9d9d9" stroke-width="0.35"/>')
    g_arriba, _, alto_arriba = texto(ARRIBA, "Jost.ttf", 400, 3.2, 0.32, TINTA)
    g_marca, ancho, alto = texto("LUNERIE", "Cormorant.ttf", 500, 10.5, 0.24, TINTA)
    g_frase, _, _ = texto(FRASE, "Jost.ttf", 400, 2.9, 0.22, TINTA)
    x_base, y_ini = LADO - 9, BANDA - 6  # LUNERIE lee de abajo arriba, pegado al borde derecho
    if capa != "oro":
        partes += [f'<g transform="translate(9 {9 + alto_arriba})">{g_arriba}</g>',
                   f'<g transform="translate({x_base} {y_ini}) rotate(-90)">{g_marca}</g>',
                   f'<g transform="translate(9 {BANDA + 9})">{g_frase}</g>']
    if capa != "tinta":
        partes.append(destello(x_base - alto / 2, y_ini - ancho - 5.5, 2.3, ORO))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{LADO}mm" height="{LADO}mm" '
            f'viewBox="0 0 {LADO} {LADO}">{"".join(partes)}</svg>')


def main():
    with sync_playwright() as p:
        nav = p.chromium.launch(channel="chrome", headless=True)
        pag = nav.new_page()
        for nombre, capa in (("tapa", None), ("capa-tinta", "tinta"), ("capa-oro", "oro")):
            svg = tapa(capa)
            (OUT / f"{nombre}.svg").write_text(svg, encoding="utf8")
            pag.set_content(f"<html><body style='margin:0'>{svg}</body></html>")
            pag.pdf(path=str(OUT / f"{nombre}.pdf"), width=f"{LADO}mm", height=f"{LADO}mm",
                    print_background=True, page_ranges="1")
        pag.set_viewport_size({"width": 520, "height": 520})
        pag.set_content(f"""<html><body style="margin:0;padding:70px;background:#ecebe8">
            <div style="width:380px;height:380px;background:#fff;box-shadow:0 18px 30px -12px #0004,0 2px 4px #0002">
            {tapa(guias=True).replace('width="100mm" height="100mm"', 'width="380" height="380"')}</div></body></html>""")
        pag.screenshot(path=str(OUT / "maqueta.png"))
        nav.close()
    print("Hecho:", *sorted(x.name for x in OUT.iterdir()), sep="\n  ")


if __name__ == "__main__":
    main()
