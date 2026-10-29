# Cola de aprobación · formato de cada pieza

Un fichero JSON por pieza en `oficina/cola/`, con nombre `AAAA-Wss-NN-slug.json`. Los ficheros que empiezan por `_` son ejemplos.

```json
{
  "id": "2026-W45-01-lune-toalla",
  "estado": "borrador",
  "plataforma": "instagram",
  "formato": "reel",
  "pieza": "reloj-lune",
  "fecha_sugerida": "2026-11-02T19:00:00+01:00",
  "gancho": "Lo que se ve y se lee en los 3 primeros segundos",
  "copy": "Texto de la publicación (pocas palabras, sin emojis).",
  "hashtags": ["#relojdemujer", "#relojvintage", "#regaloparaella"],
  "guion": [
    {"segundos": "0-3", "imagen": "qué se ve", "texto_en_pantalla": "…", "voz": ""}
  ],
  "assets": {
    "existentes": ["marca/fotos-ia/anuncios/planos/3-macro.mp4"],
    "generar": [{"que": "foto en persona del collar", "herramienta": "API Higgsfield (flare)", "coste_estimado_usd": 0.13}]
  },
  "musica": {"origen": "ninguna | pista con licencia | biblioteca de Meta (la añade Edu)", "pista": "", "licencia": ""},
  "montaje": [],
  "publicacion": {"archivos": ["oficina/salida/portada.jpg", "oficina/salida/2.jpg"], "urls": [], "alt_text": "", "ia": true},
  "origen": {"biblioteca": "instantaneos-6", "referencia": "URL de la Biblioteca de anuncios, si la hay"},
  "riesgos": ["lo que podría salir mal: legal, marca, derechos…"],
  "revision": {"notas": "", "aprobado_por": null, "fecha": null}
}
```

## Publicar (`oficina/publicar.py`)
`publicacion` es lo que se sube a Instagram: `archivos` (rutas del repo; las imágenes se pasan a JPEG y se alojan en Archivos de Shopify) o
`urls` (ya públicas; **obligatorio en los reels**, con el MP4 transcodificado). `ia: true` (por defecto) marca la publicación como contenido hecho con IA.
En un carrusel, todas las imágenes deben tener la misma proporción (se recortan según la primera).
`python oficina/publicar.py` lista lo aprobado; con un id hace un ensayo; con `--confirmar` publica y deja `estado: publicado` y `publicacion.resultado`.

## Estados
`idea` → `borrador` (la ha escrito el community manager) → `revisado` (material y montaje listos) → **`aprobado`** (Edu) → `publicado` · o `descartado`.

- Solo el estado `aprobado` puede publicarse, y solo lo pone Edu (o Claude cuando Edu lo dice).
- `assets.generar` es **coste pendiente de tu OK**: no se genera nada hasta que lo apruebes.
- `montaje` lo rellena el editor de vídeo con la lista de planos (clip, inicio, duración) para poder rehacer el vídeo.
