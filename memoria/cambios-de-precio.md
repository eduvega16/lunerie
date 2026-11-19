---
name: cambios-de-precio
description: "Al cambiar un precio en Lunerie, buscar y rehacer todo lo que lo enseña (reels programados, vídeos HyperFrames, cola, anuncios)"
metadata:
  node_type: memory
  type: project
  originSessionId: e9e73fdb-4e3d-49c0-95eb-029d0dc6ddc1
  modified: 2026-11-15T17:38:57.298Z
---

Cuando cambia el precio de una pieza en la tienda, el precio viejo sigue en el material ya hecho: piezas de la cola
de Instagram (`oficina/cola`, también las programadas), vídeos de HyperFrames (leen `marca/anuncios-hf/assets/datos.js`)
y anuncios de Meta. Hay que buscarlo y avisar a Edu, o rehacerlo.

**Why:** el 5-nov-2026 los anillos Nuit y Étoile bajaron a 19,95 € y el reel «Notas del móvil», programado para ese
mismo día, seguía diciendo 29,95 €. Edu dijo «sí» a rehacerlo.

**How to apply:** vídeos de HyperFrames: refrescar SOLO los precios de `datos.js` (con `precio()` de `preparar.py`, no
el script entero, que vuelve a bajar las fotos), grabar el `.html`, subirlo con `anuncios/subir_creatividades.py`
(borrando antes su línea del JSON) y cambiar la URL en la pieza de la cola. Los anuncios de Meta se cambian solo cuando
toque revisar la campaña (cada cambio la manda a revisión), con el OK de Edu. Relacionado: [[oficina-lunerie]],
[[meta-ads-lecciones]], [[plazos-sin-sumar]].

**15-nov (Collar Signé 49,95 → 39,90 €):** el precio viejo también va DENTRO de las imágenes (historias y posts de
terciopelo, kcal, carrusel de dudas, tarjetas finales de los vídeos), no solo en los textos: buscarlo en los scripts de
`marca/` (`grep "49,95"`), cambiar la constante, volver a montar y comparar con la versión de git (solo debe cambiar la
zona del precio). Ojo: el Pillow de `C:\Users\edu\lunerie` pinta Jost un peso más fino que el de `D:\LUNERIE`; si la
pieza se montó en el otro PC, bajar un peso o cambia la letra. En los textos, «39,90 € (antes 49,95 €)» (tachado legal:
nunca estuvo más barato).
