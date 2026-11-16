"""Leer las grabaciones de Propel Replays (la app de Shopify que graba las visitas) sin abrir ventanas. SOLO LECTURA.

Sirve para saber qué hace de verdad la gente que añade al carrito y no paga: lista de sesiones con carrito, la lista de
acciones de cada una (añadió a los X s, se fue a los Y s, llegó al pago o no…) y fotogramas de un momento concreto.

Cómo se usa (todo desde VS Code, en segundo plano; nada de ventanas):
1. Chrome sin ventana con la sesión del admin que quedó guardada en .claude/shopify-perfil (la abre Edu una vez con
   oficina/admin_shopify.py; dura días):
     "/c/Program Files/Google/Chrome/Application/chrome.exe" --headless=new --remote-debugging-port=9222 \
       --user-data-dir="D:/LUNERIE/.claude/shopify-perfil" --no-first-run --no-default-browser-check \
       --window-size=1500,1000 "https://admin.shopify.com/store/qjxvnn-xq/settings/apps"
   (si la sesión ha caducado, saldrá la página de entrar: entonces hay que abrirlo CON ventana y que entre Edu).
2. python oficina/propel_replays.py lista            → sesiones con «Added to cart» (.claude/propel/sesiones-carrito.json)
3. python oficina/propel_replays.py acciones         → lista de acciones de cada una (.claude/propel/acciones.json; ~12 s por sesión)
4. python oficina/propel_replays.py analiza          → tabla y resumen (sin datos personales)
5. python oficina/propel_replays.py evento <id> [segundos=24] [paso=1.5] ["Added product to cart"]
                                                     → hoja de fotogramas desde ese evento (.claude/propel/evento-<id>.jpg)
6. Al acabar: python oficina/propel_replays.py cerrar  (cierra el Chrome sin ventana).

Cosas aprendidas (16-nov-2026):
- La app va en un iframe (srn.propelcommerce.io) dentro de admin.shopify.com/store/qjxvnn-xq/apps/session-recording-now.
- El reproductor es rrweb: fija su tamaño al cargar (poner el tamaño de ventana ANTES de abrir la grabación) y la barra no
  es lineal con «skip inactive». Para ir a un momento, lo fiable es pulsar la fila del evento en «Shopper actions».
- Propel no graba la página de pago ni los botones exprés (Shop, PayPal, Google Pay): van en otro marco.
- No usar una segunda pestaña mientras corre «acciones»: el iframe deja de cargar.
- Los datos de las visitas (IP, nombres, emails de clientas identificadas) se quedan en .claude/propel/, fuera de git.
"""
import json
import re
import statistics as st
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from admin_shopify import CDP, TIENDA  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / ".claude" / "propel"
APP = TIENDA + "/apps/session-recording-now"
LISTA = OUT / "sesiones-carrito.json"
ACC = OUT / "acciones.json"
IP = re.compile(r"\b\d{1,3}(\.\d{1,3}){3}\b")
TIPOS = ("Focus lost", "Focus gained", "Added product to cart", "Removed product from cart", "Viewed checkout",
         "Javascript error", "Viewed product", "New shopper", "Returning shopper")


def marco(pg, intentos=40):
    """El iframe de Propel (o None si no aparece)."""
    for _ in range(intentos):
        fs = [x for x in pg.frames if x != pg.main_frame]
        if fs:
            try:
                if "propelcommerce" in fs[0].evaluate("() => location.host"):
                    return fs[0]
            except Exception:  # noqa: BLE001
                pass
        pg.wait_for_timeout(1000)
    return None


def conectar(pw, ancho=1900, alto=1200):
    br = pw.chromium.connect_over_cdp(CDP)
    ctx = br.contexts[0]
    for extra in ctx.pages[1:]:
        extra.close()
    pg = ctx.pages[0] if ctx.pages else ctx.new_page()
    pg.set_viewport_size({"width": ancho, "height": alto})
    return br, pg


def abrir_grabacion(pg, sid):
    pg.goto(f"{APP}/replays/{sid}", wait_until="domcontentloaded", timeout=60000)
    f = None
    for _ in range(25):
        pg.wait_for_timeout(1000)
        f = marco(pg, 1)
        try:
            if f and "Shopper actions" in f.evaluate("() => document.body.innerText"):
                break
        except Exception:  # noqa: BLE001
            continue
    pg.wait_for_timeout(1500)
    return f


def cmd_lista():
    from playwright.sync_api import sync_playwright
    OUT.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as pw:
        _, pg = conectar(pw, 2100, 1300)
        pg.goto(APP + "/replays", wait_until="domcontentloaded", timeout=60000)
        f = marco(pg)
        pg.wait_for_timeout(8000)
        f = marco(pg)
        f.locator('button:has-text("Added to cart") >> visible=true').first.click()
        pg.wait_for_timeout(6000)
        todas = []
        for pagina in range(1, 15):
            filas = f.evaluate("""() => [...document.querySelectorAll('a[href^="/replays/"]')].map(a => {
                const tr = a.closest('tr') || a.closest('[role=row]') || a.parentElement.parentElement;
                return {id: a.getAttribute('href').split('/').pop(), texto: (tr.innerText || '').replace(/\\s+/g, ' ').trim()}; })
                .filter((v, i, arr) => arr.findIndex(x => x.id === v.id) === i)""")
            nuevas = [x for x in filas if x["id"] not in {t["id"] for t in todas}]
            print("página", pagina, "· filas", len(filas), "· nuevas", len(nuevas))
            todas += nuevas
            sig = f.locator('button[aria-label="Next"], nav button:has(svg)').last
            try:
                if not nuevas or sig.is_disabled():
                    break
                sig.click()
                pg.wait_for_timeout(5000)
            except Exception:  # noqa: BLE001
                break
        LISTA.write_text(json.dumps(todas, ensure_ascii=False, indent=1), encoding="utf8")
        for t in todas:
            print(t["id"], "|", IP.sub("", t["texto"])[:150])


def cmd_acciones():
    from playwright.sync_api import sync_playwright
    ids = [x["id"] for x in json.loads(LISTA.read_text(encoding="utf8"))]
    hecho = json.loads(ACC.read_text(encoding="utf8")) if ACC.exists() else {}
    with sync_playwright() as pw:
        _, pg = conectar(pw)
        for sid in ids:
            if sid in hecho:
                continue
            f = abrir_grabacion(pg, sid)
            if not f:
                print(sid, "sin iframe (se puede volver a lanzar: sigue donde lo dejó)")
                continue
            t = f.evaluate("() => document.body.innerText")
            i = t.find("Shopper actions")
            j = t.find("AI summary", i)
            hecho[sid] = {"acciones": " ".join(t[i:j].split())}
            ACC.write_text(json.dumps(hecho, ensure_ascii=False, indent=1), encoding="utf8")
            print(sid, "|", hecho[sid]["acciones"][:200])


def eventos(texto):
    """[(segundo, tipo)] a partir del texto de «Shopper actions»."""
    evs = []
    for m in re.finditer(r"(?:^|(?<= [AP]M ))(?:Shopper actions [A-Z]+ \d+, \d+ )?(.*?) \+(\d\d):(\d\d) · \d+:\d\d:\d\d [AP]M", texto):
        nombre = re.sub(r"^[A-Z]+ \d+, \d+ ", "", m.group(1).strip())
        tipo = next((k for k in TIPOS if nombre.startswith(k)), "OTRO:" + nombre[:30])
        evs.append((int(m.group(2)) * 60 + int(m.group(3)), tipo))
    return evs


def cmd_analiza():
    acc = json.loads(ACC.read_text(encoding="utf8"))
    lista = {x["id"]: x["texto"] for x in json.loads(LISTA.read_text(encoding="utf8"))}
    filas = []
    for sid, v in acc.items():
        evs = eventos(v["acciones"])
        adds = [t for t, k in evs if k == "Added product to cart"]
        if not adds:
            continue
        m = re.search(r"(Nov|Dec|Oct|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep) \d+ \d{4}, \d+:\d\d [ap]m", lista.get(sid, ""))
        fecha = datetime.strptime(m.group(0), "%b %d %Y, %I:%M %p") if m else datetime.min
        tras = [(t, k) for t, k in evs if t >= adds[-1] and k != "Added product to cart"]
        foco = [(t, k) for t, k in tras if k in ("Focus lost", "Focus gained")]
        vuelve = any(k == "Focus lost" and i + 1 < len(foco) and foco[i + 1][1] == "Focus gained" and foco[i + 1][0] - t > 8
                     for i, (t, k) in enumerate(foco))
        filas.append(dict(sid=sid, fecha=fecha, t_add=adds[0], n_add=len(adds), pago=any(k == "Viewed checkout" for _, k in evs),
                          sig=(tras[0][1], tras[0][0] - adds[-1]) if tras else ("fin", 0), tras=evs[-1][0] - adds[-1], vuelve=vuelve,
                          quita=any(k == "Removed product from cart" for _, k in evs), js=any(k == "Javascript error" for _, k in evs)))
    filas.sort(key=lambda r: r["fecha"])
    print("fecha | añade a los | n.º añadidos | lo siguiente (s después) | s en la página tras añadir | pago | se va >8 s y vuelve | error JS")
    for r in filas:
        print(f"{r['fecha']:%d-%m %H:%M} | {r['t_add']}s | {r['n_add']} | {r['sig'][0]} (+{r['sig'][1]}s) | {r['tras']}s | "
              f"{'PAGO' if r['pago'] else '-'} | {'sí' if r['vuelve'] else '-'} | {'JS' if r['js'] else '-'}")
    no = [r for r in filas if not r["pago"]]
    print(f"\nsesiones con carrito: {len(filas)} · llegan al pago: {len(filas) - len(no)}")
    print("segundos desde que llegan hasta que añaden (mediana):", st.median([r["t_add"] for r in filas]))
    if no:
        print("las que no pagan siguen en la página tras añadir (mediana, s):", st.median([r["tras"] for r in no]))
        print("lo primero que hacen tras añadir:", {k: sum(1 for r in no if r["sig"][0] == k) for k in {r["sig"][0] for r in no}})
        print("se van más de 8 s y vuelven:", sum(1 for r in no if r["vuelve"]), "· añaden 2 o más:", sum(1 for r in filas if r["n_add"] > 1),
              "· quitan algo:", sum(1 for r in filas if r["quita"]))


def cmd_evento(sid, segundos=24.0, paso=1.5, evento="Added product to cart", cual=-1):
    from PIL import Image, ImageDraw
    from playwright.sync_api import sync_playwright
    OUT.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as pw:
        _, pg = conectar(pw)
        f = abrir_grabacion(pg, sid)   # siempre se recarga: el reproductor fija su tamaño al cargar
        try:
            f.locator("text=1x").first.click(timeout=3000)
        except Exception:  # noqa: BLE001
            pass
        filas = f.locator(f"text={evento}")
        n = filas.count()
        fila = filas.nth(cual if cual >= 0 else n + cual)
        fila.scroll_into_view_if_needed()
        fila.click()
        pg.wait_for_timeout(400)
        f.evaluate("() => scrollTo(0, 0)")
        reloj = lambda: f.evaluate("() => [...document.querySelectorAll('.rr-timeline__time')].map(e => e.innerText).join('/')")  # noqa: E731
        r0 = reloj()
        pg.wait_for_timeout(1200)
        if r0 == reloj():   # en pausa
            f.locator(".rr-controller__btns button").first.click()
        ims, t = [], 0.0
        tmp = OUT / "_fotograma.png"
        while t <= segundos:
            pg.screenshot(path=str(tmp), clip=f.locator(".replayer-wrapper").first.bounding_box())
            im = Image.open(tmp).convert("RGB")
            im.thumbnail((330, 660))
            d = ImageDraw.Draw(im)
            d.rectangle([0, 0, 120, 16], fill="black")
            d.text((3, 2), f"{len(ims):02d} {reloj()}", fill="white")
            ims.append(im)
            pg.wait_for_timeout(int(paso * 1000))
            t += paso
        tmp.unlink(missing_ok=True)
        w, h = max(i.width for i in ims), max(i.height for i in ims)
        cols = 6
        hoja = Image.new("RGB", (cols * w, ((len(ims) + cols - 1) // cols) * h), "white")
        for i, im in enumerate(ims):
            hoja.paste(im, ((i % cols) * w, (i // cols) * h))
        sal = OUT / f"evento-{sid}.jpg"
        hoja.save(sal, quality=84)
        print(sal, hoja.size)


def cmd_cerrar():
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        br = pw.chromium.connect_over_cdp(CDP)
        br.new_browser_cdp_session().send("Browser.close")
    print("Chrome sin ventana cerrado")


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        print(__doc__)
    elif a[0] == "lista":
        cmd_lista()
    elif a[0] == "acciones":
        cmd_acciones()
    elif a[0] == "analiza":
        cmd_analiza()
    elif a[0] == "evento":
        cmd_evento(a[1], *(float(x) for x in a[2:4]), *a[4:5])
    elif a[0] == "cerrar":
        cmd_cerrar()
    else:
        print(__doc__)
