"""Login de la CLI de Shopify (temas) sin abrir ventana de terminal: `shopify auth login` en una consola invisible.

Elige «Log in with a different account» si ya hay otra sesión (p. ej. Star Brick) y el navegador se abre solo con
el código; Edu entra con luneriecompany@gmail.com. Necesita `pip install pywinpty`. Lanzarlo en segundo plano:
    python -u tema/login_cli.py 2>&1 | tee .claude/shopify-login.log
Para volver a otra cuenta guardada: `shopify auth login --alias <email>`.
"""
import re, time
from winpty import PtyProcess

ANSI = re.compile(r"\x1b\[[0-9;?]*[ -/]*[@-~]|\x1b\][^\x07]*\x07")
p = PtyProcess.spawn("cmd /c shopify auth login", dimensions=(40, 160))
pulsado = elegido = False
fin = time.time() + 600   # 10 minutos para entrar
while p.isalive() and time.time() < fin:
    try:
        texto = ANSI.sub("", p.read(4096))
    except EOFError:
        break
    if texto.strip():
        print(texto, end="", flush=True)
    # «Which account…?» → bajar a «Log in with a different account» y confirmar
    if not elegido and re.search(r"different account", texto, re.I):
        time.sleep(0.5)
        p.write("\x1b[B")
        time.sleep(0.3)
        p.write("\r")
        elegido = True
    if not pulsado and re.search(r"press any key", texto, re.I):
        time.sleep(0.5)
        p.write("\r")
        pulsado = True
print("\n[fin] código de salida:", p.exitstatus, flush=True)
