---
name: calidad-fotos-shopify
description: Edu nota que las fotos se ven peor en Shopify que en su PC; generar en 4K y subir JPEG 97 sin submuestreo de color
metadata:
  node_type: memory
  type: feedback
  originSessionId: 61c7e11b-1c66-4770-8562-30e406897eb7
  modified: 2026-11-04T15:07:10.037Z
---

Edu (4-nov): «las fotos en mi PC se ven mejor que luego en Shopify, creo que es clave poner las fotos en buena calidad».

**Why:** medido el 4-nov: Shopify vuelve a comprimir en WebP al servir (≈39,7 dB a 1600 px), y nosotros subíamos JPEG 92 con submuestreo de color 4:2:0 desde imágenes de IA de 2K (1744 px). La compresión del CDN no se controla; el origen sí.

**How to apply:**
- Fotos de IA para la tienda: pedirlas en 4K cuando el modelo lo permita (`marketing-studio/image/flare` acepta `"resolution": "4k"` → 2480×3312; en `collar_ia.py` con `--4k`). Cuesta **0,17 $ por foto** (cobra 0,19 y devuelve 0,02; visto en las transacciones de Higgsfield el 4-nov) frente a ~0,13 $ en 2K; las bloqueadas por el filtro se devuelven enteras. Para pruebas y redes, 2K basta.
- Al subir a Shopify: `im.save(ruta, quality=97, subsampling=0)`, no 92.
- Revisar en la web lo que sirve el CDN (`&width=1200` con `Accept: image/webp`), no solo el fichero local.
- No prometer a Edu que se verá igual que en el PC: la compresión WebP de Shopify sigue ahí.

Relacionado: [[referencias-reales-ia]], [[ver-en-tienda-real]].
