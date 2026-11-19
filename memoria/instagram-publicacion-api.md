---
name: instagram-publicacion-api
description: "Cómo está montada la publicación en Instagram por API (app de Meta, token de página, dónde viven las claves) y qué no hacer con ellas"
metadata:
  node_type: memory
  type: reference
  originSessionId: 7f0dea43-fb2c-4818-be0a-6d3b8cbd08f2
  modified: 2026-11-15T17:38:59.160Z
---

App de Meta de Lunerie: id `2676185462837815` (cuenta de desarrollador «Lunerie Vega»). Instagram `@luneriejewelry` = `17841404549468255`, enlazado a la página «L U N E R I E» `1376893392171782`. Se publica con Facebook Login: host `graph.facebook.com`, token de **página** (no caduca) sacado de un token de usuario largo.

Las claves (`IG_TOKEN`, `IG_USER_ID`, `IG_HOST`, `META_APP_ID`, `META_APP_SECRET`) viven solo en `D:\LUNERIE\.env.local` (ignorado por git). Script: `oficina/publicar.py` (ensayo por defecto, `--confirmar` para publicar; solo piezas `aprobado`).

**Why:** Edu pegó el token y la clave secreta en el chat y pidió subir la clave a git «por si no la apunto». Se negó: lo que entra en git queda en el historial. La clave secreta siempre se puede volver a ver (o restablecer) en developers.facebook.com → app → Configuración → Básica, así que no hace falta copiarla a ningún sitio.

**How to apply:**
- Nunca subir claves a git ni pedir que se peguen en el chat; que las escriba él en `.env.local`. Recomendar restablecer la clave secreta cuando se haya pegado en un chat.
- `.env.local` no se sincroniza entre los 2 PCs (`C:\Users\edu\lunerie` y `D:\LUNERIE`): en el otro hay que recrearlo (token de página: mismo intercambio `fb_exchange_token` con la clave de la app).
- No publicar de verdad sin una pieza `aprobado` y sin confirmarlo con Edu antes. La prueba del 29-oct solo llegó a un contenedor FINISHED sin publicar.

Relacionado: [[oficina-lunerie]].

**4-nov: el token falló un rato y volvió solo** (a las ~17:30 ya publicaba; fallo temporal de Meta o de la app). **Si falla otra vez, volver a probar antes de pedirle nada a Edu.** Lo que pasó: el token dejó de valer (al publicar: error 190 «permission(s) must be granted before impersonating a user's page»; con el token de la app, «API access blocked», código 200). Las tareas programadas fallarán hasta arreglarlo. Arreglo sin pasar tokens por el chat: Edu genera un token de usuario en el Explorador de la API Graph, lo pega en `.env.local` como `IG_TOKEN_USUARIO=` y se corre `python oficina/renovar_token.py` (lo cambia por el de página y lo comprueba). Antes de dar por buena una tarea programada, probar el token (`GET /<IG_USER_ID>?fields=username`).

**13-nov: se publica SOLO desde `D:\LUNERIE`** (decisión de Edu). El otro PC estuvo apagado y se perdieron publicaciones. Aquí los temporizadores de activación están encendidos, y enchufado no se suspende solo.
- Las claves también están en `C:\Users\edu\lunerie\.env.local`. Allí hay que quitar las tareas con `publicar_programado.py quitar`.
- `publicar.py` se salta una pieza si su **primera línea** ya está en las 12 últimas publicaciones: no repetir primeras líneas entre piezas cercanas.
- Para publicar algo «ya», quitar antes su tarea (`quitar <id>`).
- **15-nov: el otro PC seguía con sus tareas** (allí nunca se ejecutó `quitar`) y publicó la de las 12:30. Al abrir
  sesión en cualquiera de los dos PCs, mirar en Instagram (`/media` con `timestamp`) qué ha salido antes de republicar.

**Programar (3-nov):** la API no programa, así que las piezas aprobadas se programan en el Programador de tareas de Windows de este PC con `python oficina/publicar_programado.py programar` (pythonw, sin ventanas; registro en `oficina/publicaciones.log`). Edu aprobó así el plan hasta el 20-nov («dale con las publicaciones»). Antes de aprobar una pieza en su nombre, revisar texto y fotos a tamaño real. Al abrir sesión, mirar el log y hacer commit de la cola.

**19-nov: Edu se va una semana al portátil (hasta ~26-nov); Instagram sigue saliendo desde D:.**
- Quedan 18 tareas hasta el 25-nov 19:30, todas revisadas en seco. Las pasadas se borraron.
- D: tiene que estar encendido o suspendido y con la sesión abierta (tareas «Interactive»). Se le pidió a Edu pausar Windows Update.
- `programar` admite ids desde el 19-nov (`programar <ID>…`). En el portátil, solo así, nunca a secas: su cola dice «aprobado» en lo que publica D: y saldría dos veces.
- `publicar.py` lee la salida de la CLI de Shopify en utf8 desde el 19-nov. Antes daba un UnicodeDecodeError en el log, sin consecuencias.
- **Al volver a D:**
  1. Commit de `oficina/cola`.
  2. `git pull`.
  3. Mirar el log.
