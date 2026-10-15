"""Diseño de la caja de regalo (tipo cajón, blanca, impresión en tinta) para pedir presupuesto e imprimir.

Composición como la caja «VOGUE» de Nihao / Yiwu Chunshen: palabra grande en vertical a la derecha, texto pequeño
arriba a la izquierda y una línea en la banda del cajón (abajo). Cara de 100 × 100 mm (ajustar a la plantilla del
proveedor). Letras convertidas a trazos: el archivo no depende de tener las fuentes.
Salida en marca/caja/: tapa-<frase>.svg / .pdf (para imprimir, con y sin destello dorado), maqueta.png y, para la
elegida (ELEGIDA), una capa por acabado: -capa-tinta (impresión negra) y -capa-oro (cliché del estampado en oro).
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
ARRIBA = "JOYAS Y RELOJES"
FRASES = {"para-ti": ["PARA TI"], "regalar": ["HECHO PARA", "REGALAR"],
          "joya": ["UN RELOJ QUE SE LLEVA", "COMO UNA JOYA"]}
ELEGIDA = "para-ti"  # 15-oct: «PARA TI» + destello dorado


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


def tapa(frase, con_oro, guias=False, capa=None):
    """SVG de la cara de la caja en mm. capa = "tinta" u "oro" deja solo ese acabado."""
    partes, tinta = [], capa != "oro"
    if guias:  # solo para la maqueta: borde de la banda del cajón
        partes.append(f'<line x1="0" y1="{BANDA}" x2="{LADO}" y2="{BANDA}" stroke="#d9d9d9" stroke-width="0.35"/>')
    g, _, alto = texto(ARRIBA, "Jost.ttf", 400, 3.2, 0.32, TINTA)
    if tinta:
        partes.append(f'<g transform="translate(9 {9 + alto})">{g}</g>')
    # LUNERIE en vertical, leyendo de abajo arriba, pegado al borde derecho y sin pasar a la banda
    g, ancho, alto = texto("LUNERIE", "Cormorant.ttf", 500, 10.5, 0.24, TINTA)
    x_base, y_ini = LADO - 9, BANDA - 6
    if tinta:
        partes.append(f'<g transform="translate({x_base} {y_ini}) rotate(-90)">{g}</g>')
    if con_oro and capa != "tinta":
        partes.append(destello(x_base - alto / 2, y_ini - ancho - 5.5, 2.3, ORO))
    for i, linea in enumerate(FRASES[frase]):
        g, _, alto = texto(linea, "Jost.ttf", 400, 2.9, 0.22, TINTA)
        if tinta:
            partes.append(f'<g transform="translate(9 {BANDA + 9 + i * 4.6})">{g}</g>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{LADO}mm" height="{LADO}mm" '
            f'viewBox="0 0 {LADO} {LADO}">{"".join(partes)}</svg>')


def main():
    with sync_playwright() as p:
        nav = p.chromium.launch(channel="chrome", headless=True)
        pag = nav.new_page()
        trabajos = [(f"tapa-{f}{'-oro' if o else ''}", f, o, None) for f in FRASES for o in (False, True)]
        trabajos += [(f"tapa-{ELEGIDA}-oro-capa-{c}", ELEGIDA, True, c) for c in ("tinta", "oro")]
        for nombre, frase, con_oro, capa in trabajos:
            svg = tapa(frase, con_oro, capa=capa)
            (OUT / f"{nombre}.svg").write_text(svg, encoding="utf8")
            pag.set_content(f"<html><body style='margin:0'>{svg}</body></html>")
            pag.pdf(path=str(OUT / f"{nombre}.pdf"), width=f"{LADO}mm", height=f"{LADO}mm",
                    print_background=True, page_ranges="1")
        cajas = "".join(
            f"<figure><div class='caja'>{tapa(f, o, guias=True)}</div>"
            f"<figcaption>{' / '.join(FRASES[f])}{' · con destello dorado' if o else ''}</figcaption></figure>"
            for f in FRASES for o in (False, True))
        html = f"""<html><head><style>
            body {{ margin:0; padding:48px; background:#ecebe8; font:15px system-ui; color:#444;
                   display:grid; grid-template-columns:repeat(2, 380px); gap:40px 56px; }}
            .caja {{ width:340px; height:340px; background:#fff; box-shadow: 0 18px 30px -12px #0004, 0 2px 4px #0002; }}
            .caja svg {{ width:100%; height:100%; display:block; }}
            figure {{ margin:0; }} figcaption {{ margin-top:14px; }}
        </style></head><body>{cajas}</body></html>"""
        pag.set_viewport_size({"width": 960, "height": 1400})
        pag.set_content(html)
        pag.screenshot(path=str(OUT / "maqueta.png"), full_page=True)
        nav.close()
    print("Hecho:", *sorted(x.name for x in OUT.iterdir()), sep="\n  ")


if __name__ == "__main__":
    main()
