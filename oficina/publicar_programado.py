"""Publica a su hora las piezas aprobadas de la cola, con el Programador de tareas de Windows y sin abrir ventanas.

La API de Instagram no programa publicaciones, así que cada pieza aprobada tiene una tarea de Windows (carpeta
«\\Lunerie\\» del Programador de tareas) que lanza este script con pythonw a la hora de `fecha_sugerida`. Solo funciona si
este PC está encendido o en suspensión (8-nov: la tarea lo despierta, `-WakeToRun`) y con la sesión de Edu abierta; si
estaba apagado, la tarea corre al encenderlo (`-StartWhenAvailable`) pero solo publica si no han pasado más de
RETRASO_MAX horas; si no, la pieza sigue «aprobado» para publicarla a mano. Todo queda en oficina/publicaciones.log (fuera de git).

    python oficina/publicar_programado.py programar          crea o rehace una tarea por pieza aprobada con fecha futura
    python oficina/publicar_programado.py tareas             lista las tareas de Lunerie
    python oficina/publicar_programado.py quitar [ID]        borra la tarea de una pieza (o todas)
    pythonw oficina/publicar_programado.py publicar ID [--ensayo]   lo que ejecuta cada tarea
"""
import datetime, json, os, pathlib, subprocess, sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
COLA = RAIZ / "oficina" / "cola"
LOG = RAIZ / "oficina" / "publicaciones.log"
CARPETA = "\\Lunerie\\"
SIN_VENTANA = getattr(subprocess, "CREATE_NO_WINDOW", 0)
PYTHON = pathlib.Path(sys.executable).with_name("python.exe")
PYTHONW = pathlib.Path(sys.executable).with_name("pythonw.exe")
RETRASO_MAX = 3   # horas: más tarde ya no se publica sola (no pisar la pieza del día siguiente ni salir a deshoras)


def apuntar(texto):
    with LOG.open("a", encoding="utf8") as f:
        f.write(f"[{datetime.datetime.now():%Y-%m-%d %H:%M:%S}] {texto.rstrip()}\n")


def publicar(pieza, ensayo=False):
    """Lanza publicar.py con una consola oculta (así tampoco abren ventana el shopify y el curl que usa por dentro)."""
    f = next(COLA.glob(f"{pieza}*.json"), None)
    fecha = json.loads(f.read_text(encoding="utf8")).get("fecha_sugerida") if f else None
    if fecha and not ensayo:
        retraso = datetime.datetime.now().astimezone() - datetime.datetime.fromisoformat(fecha)
        if retraso > datetime.timedelta(hours=RETRASO_MAX):
            apuntar(f"{pieza} → NO publicada: la tarea arrancó {retraso.total_seconds() / 3600:.1f} h tarde "
                    f"(PC apagado a su hora); publicarla a mano")
            return
    orden = [str(PYTHON), str(RAIZ / "oficina" / "publicar.py"), pieza] + ([] if ensayo else ["--confirmar"])
    r = subprocess.run(orden, cwd=RAIZ, capture_output=True, text=True, encoding="utf8", errors="replace",
                       creationflags=SIN_VENTANA, env={**os.environ, "PYTHONIOENCODING": "utf-8"})
    apuntar(f"{'ENSAYO ' if ensayo else ''}{pieza} → código {r.returncode}\n{r.stdout}{r.stderr}")


def powershell(script):
    return subprocess.run(["powershell", "-NoProfile", "-NonInteractive", "-Command", script], capture_output=True,
                          text=True, encoding="utf8", errors="replace", creationflags=SIN_VENTANA)


def programar():
    ahora = datetime.datetime.now().astimezone()
    for f in sorted(COLA.glob("20*.json")):
        p = json.loads(f.read_text(encoding="utf8"))
        if p.get("estado") != "aprobado" or p.get("plataforma") != "instagram" or not p.get("fecha_sugerida"):
            continue
        cuando = datetime.datetime.fromisoformat(p["fecha_sugerida"])
        if cuando <= ahora:
            print(f"{p['id']}: su fecha ya ha pasado ({cuando:%d-%m %H:%M}); se publica a mano")
            continue
        local = cuando.astimezone().strftime("%Y-%m-%dT%H:%M:%S")
        r = powershell(
            f"$a = New-ScheduledTaskAction -Execute '{PYTHONW}' -Argument '\"{__file__}\" publicar {p['id']}' "
            f"-WorkingDirectory '{RAIZ}'; "
            f"$t = New-ScheduledTaskTrigger -Once -At ([datetime]'{local}'); "
            "$s = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -WakeToRun -StartWhenAvailable "
            "-ExecutionTimeLimit (New-TimeSpan -Minutes 20); "
            f"Register-ScheduledTask -TaskPath '{CARPETA}' -TaskName '{p['id']}' -Action $a -Trigger $t -Settings $s "
            f"-Description 'Lunerie: publica en Instagram la pieza {p['id']} (oficina/publicar_programado.py)' -Force | Out-Null")
        print(f"{p['id']}: {'programada para el ' + cuando.strftime('%d-%m %H:%M') if r.returncode == 0 else 'ERROR ' + r.stderr.strip()}")


if __name__ == "__main__":
    accion, *resto = sys.argv[1:] or ["tareas"]
    if accion == "publicar":
        publicar(resto[0], ensayo="--ensayo" in resto)
    elif accion == "programar":
        programar()
    elif accion == "quitar":
        nombre = f"-TaskName '{resto[0]}'" if resto else ""
        print(powershell(f"Get-ScheduledTask -TaskPath '{CARPETA}' {nombre} | Unregister-ScheduledTask -Confirm:$false").stderr or "hecho")
    else:
        print(powershell(f"Get-ScheduledTask -TaskPath '{CARPETA}' | ForEach-Object {{ $_.TaskName + '  ' + "
                         "($_.Triggers[0].StartBoundary) + '  ' + $_.State }").stdout or "ninguna")
