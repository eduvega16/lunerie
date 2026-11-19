---
name: videos-ugc
description: "Cómo salen bien los vídeos UGC con IA de Lunerie (gusto de Edu y fallos de Kling): cosas que no se ven en el código"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 852723d9-a068-4c0d-8a0b-ea52d7731609
  modified: 2026-11-06T22:19:13.801Z
---

Lo que Edu aprobó el 5-nov fue el vídeo de **Carmen en luz dorada**: «me flipa». Lo que rechazó:
- el vídeo de HyperFrames con el nombre escrito («sale del tirón Marta, ¿eso qué es?»);
- un segundo UGC casi igual al primero («algo diferente»);
- la lágrima grande («el collar es más sutil»);
- las voces de serie («parece una dobladora»);
- la música alta.

**Why:** quiere que parezca grabado de verdad por una chica normal con el móvil, y que cada vídeo nuevo sea distinto a los anteriores, para tener variedad en Meta.

**How to apply:**
- Cada vídeo, con escenario, luz, ropa y planos nuevos. Ideas de Pinterest («ugc content jewelry»): collar colgando de los dedos, en la palma, abrochándolo, selfie en el espejo con el móvil tapando la cara. Pinterest pide login, pero la cuadrícula se ve detrás.
- Lágrima pequeña: no más grande que la mayúscula del nombre.
- Voz: Silvia ([[elevenlabs-voz]]) con filtro de móvil, en tono de presentadora. Nada de «me lo regalaron», que sería un testimonio inventado.
- Música: siempre 18 dB por debajo de la voz (`con_musica.py`).
- Revisar cada clip de Kling por fotogramas, porque hacia el segundo 2,5-3 a veces cambia la cara o el color de la lágrima. Pasó con verde → azul, y se arregla con «keeps exactly its colour». Si falla, cortar el plano antes (`--planos x:2.6`) o rehacerlo.
- Antes de subir, ruta local + OK de Edu ([[ensenar-antes-de-subir]]).

Coste: unos 2,5-3 $ por vídeo (fotos flare + 4 clips de Kling 3.0 pro).

**6-nov:**
- **Rechazó** un reel montado con sus fotos y vídeos reales de la muestra (`reel_muestra.py`): «demasiado casero». Se veían las pelusas sobre el fondo negro, y no le gustó el texto «Antes de venderlo, pedimos uno». Lo real del móvil no le vale tal cual. Prefiere IA con estética cuidada: estudio de Olivia o UGC bien iluminado.
- **Aprobó** el reel de la cámara digital (`reel_camara.py`), sacado de un reel que mandó él: fotos de estudio pasando en la pantalla de una cámara antigua.
- Cuando manda un reel de referencia, copiar el formato, no la marca ni el contenido.

Para reels de la competencia y el plan con Lola Rose (3 chicas, la caja primero, varias piezas al final), ver [[reels-referencia]].
