---
name: higgsfield-solo-con-permiso
description: "Nada en Higgsfield (ni API ni conector, ni fotos ni vídeos) sin el permiso explícito de Edu para esa tanda; una idea de reel se guarda como idea, no se produce"
metadata:
  node_type: memory
  type: feedback
  originSessionId: b20f0a0e-86fd-4f00-b85b-452279a19989
  modified: 2026-11-14T18:31:44.872Z
---

No se genera nada en Higgsfield (API o conector: fotos, ediciones, Kling) sin que Edu diga «sí» a esa tanda en concreto, con su coste delante. Que acepte una idea o diga qué piezas salen no es permiso para generar.

**Why:** el 14-nov Edu mandó el reel del tres en raya y dijo qué piezas quería («el collar nuestro, los anillos y los relojes»). Claude lo tomó como un OK y generó 5 fotos en 4K (~0,85 $) sin preguntar. Edu cortó: «No ejecutes nada en Higgsfield sin mi permiso. Guárdalo como idea solamente».

**How to apply:**
- Ideas de reels que trae Edu: se analizan y se guardan en `biblioteca/ideas-reels.json` con su coste. Antes de gastar un céntimo, la pregunta va sola: «¿Lo genero? Son ~X $».
- Vale lo mismo para ElevenLabs y cualquier otra API de pago.
- Lo local y gratis (ffmpeg, PIL, montar con fotos que ya existen) sí se puede hacer sin preguntar.

Relacionado: [[oficina-lunerie]], [[ensenar-antes-de-subir]], [[reels-referencia]].
