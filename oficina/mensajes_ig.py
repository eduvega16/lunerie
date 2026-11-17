"""Mensajes de Instagram de Lunerie desde la bandeja de Meta Business Suite (17-nov).

Por qué así: la API de Meta devuelve 0 conversaciones de Instagram mientras la app «Lunerie Claude Publisher» esté
en modo desarrollo (solo enseña las de gente con papel en la app) y publicarla pide requisitos que no merece la pena
cumplir. La bandeja de Business Suite sí las ve todas.

Sesión: Chrome con el perfil D:/LUNERIE/.claude/meta-perfil (fuera de git), donde Edu entró el 17-nov con la cuenta
que administra Lunerie (OJO: la cuenta «Eduardo Vega» solo ve southshoes). Si la sesión caduca, abrir una ventana
(avisando a Edu antes) y que entre él:
    "/c/Program Files/Google/Chrome/Application/chrome.exe" --remote-debugging-port=9223 \
      --user-data-dir="D:/LUNERIE/.claude/meta-perfil" --no-first-run "<BANDEJA>"
Sin ventana (lo normal): este script arranca Chrome --headless=new con ese perfil si no hay ninguno en el puerto 9223.

Uso:
    python oficina/mensajes_ig.py lista                    → conversaciones (nombre, último mensaje, cuándo)
    python oficina/mensajes_ig.py hilo "<nombre>"          → la conversación entera
    python oficina/mensajes_ig.py responder "<nombre>" "<texto>"              → ENSAYO: enseña lo que mandaría
    python oficina/mensajes_ig.py responder "<nombre>" "<texto>" --confirmar  → lo manda (solo con el OK de Edu)
    python oficina/mensajes_ig.py cerrar                   → cierra el Chrome sin ventana
En el texto, «\\n» o un salto de línea = nueva línea en el mismo mensaje. Los datos de las clientas no van a git.
"""
import subprocess
import sys
import time
import urllib.request

from playwright.sync_api import sync_playwright

PUERTO = 9223
CDP = f"http://127.0.0.1:{PUERTO}"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PERFIL = r"D:\LUNERIE\.claude\meta-perfil"
BANDEJA = ("https://business.facebook.com/latest/inbox/instagram_direct"
           "?business_id=1639315480899561&asset_id=1376893392171782")


def chrome_vivo():
    try:
        urllib.request.urlopen(CDP + "/json/version", timeout=2)
        return True
    except Exception:  # noqa: BLE001
        return False


def arrancar():
    if chrome_vivo():
        return
    flags = getattr(subprocess, "CREATE_NO_WINDOW", 0)
    subprocess.Popen([CHROME, "--headless=new", f"--remote-debugging-port={PUERTO}", f"--user-data-dir={PERFIL}",
                      "--window-size=1500,1100", "--no-first-run", "about:blank"],
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, creationflags=flags)
    for _ in range(30):
        if chrome_vivo():
            return
        time.sleep(0.5)
    sys.exit("Chrome no arrancó en el puerto 9223")


def bandeja(pw):
    arrancar()
    br = pw.chromium.connect_over_cdp(CDP)
    ctx = br.contexts[0]
    pg = next((p for p in ctx.pages if "business.facebook.com/latest/inbox" in p.url), None)
    if not pg:
        pg = ctx.pages[0] if ctx.pages else ctx.new_page()
        pg.set_viewport_size({"width": 1500, "height": 1100})
        pg.goto(BANDEJA, wait_until="domcontentloaded", timeout=60000)
    for _ in range(40):
        t = texto(pg)
        if "Responde mensajes" in t or "Seguimiento" in t:
            break
        if "loginpage" in pg.url or "Inicia sesión" in t:
            sys.exit("La sesión de Meta ha caducado: hay que abrir la ventana para que Edu entre (ver arriba).")
        time.sleep(0.5)
    if "L U N E R I E" not in texto(pg) and "1639315480899561" not in pg.url:
        sys.exit("La sesión no es la de Lunerie (¿cuenta southshoes?). Edu tiene que entrar con la de Lunerie.")
    return pg


def texto(pg):
    try:
        return pg.evaluate("() => document.body.innerText")
    except Exception:  # noqa: BLE001
        return ""


def lista(pg):
    t = texto(pg)
    i, j = t.find("Seguimiento"), t.find("Asignar esta conversación")
    return t[i + len("Seguimiento"):j if j > 0 else None].strip()


def abrir(pg, nombre):
    pg.get_by_text(nombre, exact=True).first.click()
    pg.wait_for_timeout(3500)
    t = texto(pg)
    i = t.find("Asignar esta conversación")
    j = t.find("Responde en Instagram", i)
    return t[i:j].replace("Asignar esta conversación", "").replace("Abrir menú desplegable", "").strip()


def responder(pg, nombre, mensaje, confirmar):
    hilo = abrir(pg, nombre)
    print("Últimas líneas del hilo:\n  " + "\n  ".join(hilo.splitlines()[-6:]))
    print(f"\nMensaje para {nombre}:\n{mensaje}\n")
    if not confirmar:
        print("ENSAYO: no se ha mandado nada (añade --confirmar).")
        return
    caja = pg.get_by_role("textbox", name="Responde en Instagram…")
    if not caja.count():
        caja = pg.locator('[role="textbox"][contenteditable="true"]').last
    caja.click()
    partes = mensaje.split("\n")
    for k, p in enumerate(partes):
        if p:
            pg.keyboard.insert_text(p)
        if k < len(partes) - 1:
            pg.keyboard.press("Shift+Enter")
    pg.wait_for_timeout(400)
    pg.keyboard.press("Enter")
    pg.wait_for_timeout(4000)
    ultimo = partes[-1].strip() or partes[0].strip()
    ok = ultimo[:40] in abrir(pg, nombre)
    print("MANDADO y visto en el hilo." if ok else "OJO: no veo el mensaje en el hilo; revisar a mano.")


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    cmd = sys.argv[1]
    if cmd == "cerrar":
        subprocess.run(["powershell", "-NoProfile", "-Command",
                        "Get-CimInstance Win32_Process -Filter \"Name='chrome.exe'\" | Where-Object { $_.CommandLine -like "
                        "'*meta-perfil*' -and $_.CommandLine -like '*headless*' } | ForEach-Object { Stop-Process -Id "
                        "$_.ProcessId -Force }"], check=False)
        return
    with sync_playwright() as pw:
        pg = bandeja(pw)
        if cmd == "lista":
            print(lista(pg))
        elif cmd == "hilo":
            print(abrir(pg, sys.argv[2]))
        elif cmd == "responder":
            responder(pg, sys.argv[2], sys.argv[3].replace("\\n", "\n"), "--confirmar" in sys.argv)
        else:
            sys.exit(__doc__)


if __name__ == "__main__":
    main()
