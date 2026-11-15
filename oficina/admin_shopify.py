"""Manejar el admin de Shopify desde aquí cuando la API no llega (Messaging/Shopify Email, ajustes sin permiso…).

Cómo se usa (sin ventanas de terminal; todo en segundo plano desde VS Code):
1. Abrir un Chrome aparte con depuración (Edu entra él con luneriecompany@gmail.com; el perfil queda guardado
   en .claude/shopify-perfil, fuera de git):
     "/c/Program Files/Google/Chrome/Application/chrome.exe" --remote-debugging-port=9222 \
       --user-data-dir="D:/LUNERIE/.claude/shopify-perfil" --no-first-run --no-default-browser-check \
       --window-size=1500,1000 "https://admin.shopify.com/store/qjxvnn-xq/marketing/automations"
2. python oficina/admin_shopify.py esperar      → avisa cuando Edu ya está dentro del admin (15 min máximo).
3. Desde un script:  from admin_shopify import *  ;  pw, br, pg = abrir()  ;  f = app(pg)

Trucos del editor de correos de Messaging (15-nov):
- Todo va en el iframe email.shopifyapps.com → app(pg) (frame 1), no en la página.
- Asunto y vista previa son cajas Slate: [role=textbox][aria-label="Asunto"] / "Texto de vista previa" → asunto().
- Las secciones se eligen con su radio oculto (id «gid://email-app/Section/<nombre>») → seccion().
  Botones: button[aria-label="Eliminar sección"] / "Ocultar sección" (la cabecera no se borra, solo se oculta).
- «Liquid personalizado» es CodeMirror sin cmView: se pega con el portapapeles → pegar_liquid().
- El editor se salta align="center" y <s>: centrar con text-align / margin:0 auto y tachar con
  text-decoration:line-through en el estilo.
- Captura del correo largo: la de un elemento sale en blanco por debajo; mejor rueda del ratón + recortes.
"""
import json
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

CDP = "http://127.0.0.1:9222"
TIENDA = "https://admin.shopify.com/store/qjxvnn-xq"
CAPTURAS = Path(__file__).resolve().parent.parent / ".claude" / "preview"


def esperar(minutos=15):
    """Espera a que haya una pestaña del admin de Lunerie abierta en el Chrome de depuración."""
    fin = time.time() + minutos * 60
    ultimo = ""
    while time.time() < fin:
        try:
            tabs = json.load(urllib.request.urlopen(CDP + "/json", timeout=3))
            urls = [t.get("url", "") for t in tabs if t.get("type") == "page"]
            ultimo = " | ".join(u[:90] for u in urls)
            if any(u.startswith(TIENDA) for u in urls):
                print("DENTRO:", ultimo)
                return True
        except Exception as e:  # Chrome aún sin abrir o cerrándose
            ultimo = f"sin conexión ({e.__class__.__name__})"
        time.sleep(3)
    print("TIEMPO AGOTADO; último:", ultimo)
    return False


def abrir():
    """Se conecta al Chrome de depuración y devuelve (playwright, navegador, pestaña del admin)."""
    from playwright.sync_api import sync_playwright
    pw = sync_playwright().start()
    br = pw.chromium.connect_over_cdp(CDP)
    ctx = br.contexts[0]
    pags = [p for p in ctx.pages if p.url.startswith("https://admin.shopify.com")]
    return pw, br, (pags[0] if pags else ctx.pages[0])


def app(pg):
    """El iframe de la app (Messaging, Flow…): ahí está el contenido de verdad."""
    return pg.frames[1] if len(pg.frames) > 1 else pg.main_frame


def foto(pg, nombre):
    CAPTURAS.mkdir(parents=True, exist_ok=True)
    ruta = CAPTURAS / f"{nombre}.png"
    pg.screenshot(path=str(ruta))
    print("captura:", ruta)
    return ruta


def asunto(pg, f, texto_asunto, vista_previa=None):
    """Escribe el asunto (y la vista previa) de un correo de Messaging."""
    pares = [("Asunto", texto_asunto)]
    if vista_previa is not None:
        pares.append(("Texto de vista previa", vista_previa))
    for etiqueta, texto in pares:
        caja = f.locator(f'[role=textbox][aria-label="{etiqueta}"]')
        caja.click()
        pg.keyboard.press("Control+A")
        pg.keyboard.insert_text(texto)
        pg.wait_for_timeout(500)


def seccion(pg, f, nombre):
    """Selecciona una sección del correo por su nombre (header, custom_liquid, footer…)."""
    r = f.locator(f"input[type=radio][id*='gid://email-app/Section/{nombre}']").first
    r.evaluate("e => { e.scrollIntoView({block:'center'}); e.click(); }")
    pg.wait_for_timeout(900)


def boton_visible(f, etiqueta):
    vis = [b for b in f.locator(f'button[aria-label="{etiqueta}"]').all() if b.is_visible()]
    return vis[0] if vis else None


def pegar_liquid(pg, f, fichero_html):
    """Copia el fichero al portapapeles y lo pega en el editor de «Liquid personalizado» ya seleccionado."""
    subprocess.run(["powershell", "-NoProfile", "-Command",
                    f"Get-Content -Raw -Encoding UTF8 '{Path(fichero_html).resolve()}' | Set-Clipboard"],
                   check=True)
    cm = f.locator(".cm-content").first
    cm.click()
    pg.keyboard.press("Control+A")
    pg.keyboard.press("Control+V")
    pg.wait_for_timeout(3000)
    print("líneas en el editor:", f.locator(".cm-line").count())


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "esperar":
        sys.exit(0 if esperar() else 1)
    print(__doc__)
