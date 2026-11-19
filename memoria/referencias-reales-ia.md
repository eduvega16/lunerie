---
name: referencias-reales-ia
description: "Para generar fotos con IA, usar como referencia fotos REALES de cada pieza (proveedor, amigas), nunca otra foto hecha con IA; el Lune es algo más grande de lo que lo saco"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 3ec63fac-4698-4f81-aa1b-7b9d682aaacb
  modified: 2026-11-14T18:33:54.665Z
---

Al generar fotos con IA (Higgsfield/flare), las referencias de cada pieza tienen que ser **fotos reales**, no fotos que ya hicimos con IA. Y el reloj Lune en la muñeca es **algo más grande** de lo que lo estaba generando.

**Why:** Edu, 4-nov: «el Lune lo generas demasiado pequeño, es un poco más grande; estás usando una imagen de IA para generar otra con IA, mira las reales». La primera foto de la ficha del Lune (`lune-verde-producto.jpg`, en niebla) es una edición con IA, y en los prompts pedía «small and delicate, do not make them bigger», así que el reloj salía diminuto. Lo mismo pasa con la primera foto de Maille, Galet, Perle y Duo (en niebla hechas con IA el 30-oct).

**How to apply:**
- **Lune:** fotos del proveedor en la ficha (las 2 últimas: `S6514a93…` y `S0196b43…`, una en la muñeca) y las fotos reales de las amigas (`lune-opinion-1/2/3/5.jpg` en Archivos de Shopify).
- **Otros productos:** las fotos del proveedor de cada ficha, no la 1.ª en niebla si es de IA.
- No escribir en el prompt que el reloj es pequeño ni que no lo agrande: pedir que tenga el mismo tamaño respecto a la muñeca que en la foto real.
- Comparar el resultado con la foto real de la muñeca antes de darlo por bueno.
- **4-nov, ya montado:** las fotos reales están en `marca/referencias-reales/` (`<handle>-1.jpg`, `-2.jpg`…; `collar_ia.py` manda todas las de cada pieza). Funcionó: con ellas el Lune salió con su bisel trenzado y a su tamaño, y el Nuit fino. Maille, Galet, Perle y Duo añadidos el 4-nov por la noche desde las fotos del proveedor de su ficha (no hace falta pedírselas a Edu: están en Shopify, después de las 2 de IA).
- La IA pinta las piedras del Lune verde oscuro con vetas negras aunque la referencia sea real → `marca/piedras_lune.py` (OpenCV) las pasa a verde medio con vetas claras. Revisar siempre las piedras en un recorte a tamaño real junto a `reloj-lune-2.jpg`.

- **14-nov, bodegón desde arriba con varias piezas a la vez (tablero del tres en raya, `marca/tres_en_raya.py`):** Edu lo rechazó: «el reloj no es así ni el collar, está muy mal». Generar desde cero varias piezas juntas y en formas nuevas (reloj cerrado en círculo, collar en aro) no sale fiel, aunque las referencias sean reales y yo lo dé por bueno en el recorte. Para ideas así: grabarlo de verdad (Edu) o montarlo con fotos reales ya revisadas, no generarlo.

Relacionado: [[estilo-contenido-juvenil]], [[lujo-pdpaola]], [[higgsfield-solo-con-permiso]].
