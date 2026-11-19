---
name: redes-solo-instagram
description: "Redes: Instagram y página de Facebook (publicar_facebook.py). Sin «creada con IA» en los textos y, desde el 18-nov, sin la etiqueta de IA de la API; Claude elige el contenido orgánico"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 61c7e11b-1c66-4770-8562-30e406897eb7
  modified: 2026-11-04T22:25:02.085Z
---

Edu (4-nov): «si en Facebook te tienes que gastar tiempo, tira con Instagram nada más» y, sobre qué publicar, «lo que tú consideres». También: «no pongas imagen generada con IA» en los textos de las publicaciones.

**Why:** quiere avanzar rápido y que Claude decida el contenido orgánico dentro del plan; la frase de IA en el pie no le gusta.

**How to apply:**
- Redes orgánicas: Instagram (feed, carruseles, reels, stories). **8-nov: Edu pidió subir las publicaciones también a Facebook.**
  El token de la página ya tiene `pages_manage_posts` (fotos con `oficina/publicar_facebook.py <id>`). Facebook sí deja programar por API (`scheduled_publish_time`).
  Estado al irse Edu (8-nov): permiso activado en la app (caso de uso «Administra las páginas»), falta el token de
  usuario nuevo en `.env.local`. Edu tiende a pegar los tokens en el chat: pedirle «hecho» y que lo pegue en el fichero.
- Ocultar los Me gusta y restaurar publicaciones borradas no se puede por API: lo hace Edu en la app.
- Puedo elegir y programar piezas orgánicas que cumplan las reglas de la marca (verdad, precios reales); dejar constancia en la pieza («aprobado por Claude con permiso de Edu») y contárselo. El dinero (anuncios, presupuestos) sigue necesitando su OK explícito.
- Ningún pie lleva «Imagen/Vídeo creado con IA». **18-nov: Edu pidió quitar también la etiqueta de la API** («que Instagram la ponga sola»): `publicar.py` ya no manda `is_ai_generated` salvo que la pieza lleve `publicacion.etiqueta_ia: true`. Ojo: los archivos de Higgsfield no traen metadatos C2PA y además se vuelven a guardar con PIL, así que Instagram casi nunca la pondrá solo. Riesgo avisado (Meta pide etiquetar vídeo realista hecho con IA): él decide.
- Los reels por API salen sin música: recordarle que la puede añadir desde la app.

Relacionado: [[instagram-publicacion-api]], [[oficina-lunerie]].
