"""Grabación de pantalla de la ficha del Collar Signé (MOFU, biblioteca/funnel-meta.json): en el móvil se elige la
piedra y se escribe un nombre en la vista previa. Hace capturas a 3x (nítidas) con Playwright y las guarda numeradas
con su duración; el montaje lo hace marca/anuncio_vista_previa.py. Sin créditos de IA.
    python marca/grabar_vista_previa.py [Nombre] [Mes]   → marca/fotos-ia/campana-bf/pantalla/NNN.png + tiempos.json
Oculta el banner de cookies y el chat solo en la captura (no se acepta el banner: el píxel no se dispara).
"""
import json, pathlib, sys
from playwright.sync_api import sync_playwright

RAIZ = pathlib.Path(__file__).resolve().parent.parent
SAL = RAIZ / "marca" / "fotos-ia" / "campana-bf" / "pantalla"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
NOMBRE = sys.argv[1] if len(sys.argv) > 1 else "Carmen"
MES = sys.argv[2] if len(sys.argv) > 2 else "Mayo"
OCULTAR = "#shopify-pc__banner,#ShopifyChat,inbox-online-store-chat,shopify-chat{display:none!important}"

with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CHROME)
    c = b.new_context(viewport={"width": 390, "height": 844}, device_scale_factor=3, is_mobile=True,
                      has_touch=True, locale="es-ES")
    pg = c.new_page()
    pg.goto("https://lunerie.es/products/collar-signe", wait_until="domcontentloaded")
    pg.add_style_tag(content=OCULTAR)
    pg.wait_for_timeout(4500)
    pg.add_style_tag(content=OCULTAR)
    raiz = pg.locator("[data-lu-collar]").first
    raiz.scroll_into_view_if_needed()
    # «Piedra del mes» cerca de arriba, con el color encima
    y = pg.evaluate("document.querySelector('[data-lu-collar]').getBoundingClientRect().top")
    pg.evaluate(f"window.scrollBy(0,{y - 250})")
    pg.wait_for_timeout(800)
    SAL.mkdir(parents=True, exist_ok=True)
    for f in SAL.glob("*.png"):
        f.unlink()
    tiempos, n = [], 0

    def foto(seg, fase):
        global n
        n += 1
        pg.screenshot(path=str(SAL / f"{n:03d}.png"))
        tiempos.append({"f": f"{n:03d}.png", "seg": seg, "fase": fase})

    foto(1.2, "piedra")
    pg.locator("[data-lu-abrir]").first.tap()
    pg.wait_for_timeout(700)
    foto(1.4, "panel")
    pg.locator(f'[data-lu-mes="{MES}"]').first.tap()
    pg.wait_for_timeout(900)
    foto(1.0, "piedra")
    pg.locator("[data-lu-nombre]").first.tap()
    pg.wait_for_timeout(300)
    foto(0.5, "nombre")
    for letra in NOMBRE:
        pg.keyboard.type(letra)
        pg.wait_for_timeout(150)
        foto(0.28, "nombre")
    pg.locator("[data-lu-nombre]").first.blur()
    pg.wait_for_timeout(300)
    foto(2.6, "revisar")
    (SAL / "tiempos.json").write_text(json.dumps(tiempos, ensure_ascii=False, indent=1), encoding="utf-8")
    print(n, "capturas en", SAL)
    b.close()
