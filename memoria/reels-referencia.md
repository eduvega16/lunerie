---
name: reels-referencia
description: Cómo ver por dentro un reel o anuncio de la competencia que manda Edu (sin login) y dónde guardarlo; Lola Rose (13-nov) como modelo de UGC con varias chicas
metadata:
  node_type: memory
  type: reference
  originSessionId: b20f0a0e-86fd-4f00-b85b-452279a19989
  modified: 2026-11-16T19:15:03.396Z
---

Edu manda enlaces de reels de Instagram o pide mirar una marca en la biblioteca de anuncios. Instagram no enseña el vídeo sin iniciar sesión.

**Cómo verlo:**
- Bajar la página con `curl -A "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)"`. Las etiquetas `og:video` (MP4 directo), `og:image` y `og:title` (cuenta y texto) suelen venir.
- Con el MP4, ffmpeg saca un fotograma por segundo en una hoja (`fps=1,scale=240:-1,tile=7x4`) y unos planos clave más grandes (filtro `select='eq(n\,X)+…'` con `-fps_mode vfr`; esta versión de ffmpeg no acepta `-vsync`).
- El audio se transcribe con ElevenLabs speech-to-text (`scribe_v2`, `tag_audio_events`) para saber si lleva voz o solo música ([[elevenlabs-voz]]).
- Si solo hay portada (`og:image`), decirlo y pedirle a Edu lo que pasa después.

**Biblioteca de anuncios:** buscar el nombre con `ads_library_search` para sacar el `page_id` de la marca. Después, `page_ids` + `ad_active_status: ACTIVE` da los anuncios activos con su título y su fecha de creación. Con `countries: ["ES"]` sale el total en España. Esta búsqueda no da el texto del anuncio ni el vídeo.

**Dónde se guarda:** fotogramas en `oficina/referencias/<marca>-<fecha>/` y notas en `oficina/referencias/competidores.md`: qué es, cómo es el vídeo plano a plano, qué se coge y qué no.

**Lola Rose (13-nov, Edu: «perfe memoriza»):**
- **El vídeo:** 25 s, solo música, corte cada ~1 s y 3 chicas distintas. Orden: caja abierta en la mesa → reloj de cerca → puesto → varias piezas juntas en la muñeca.
- **Los anuncios:** ~103 activos, casi todos de los últimos 4 días.
- **Plan acordado:** esperar 3-4 días a ver cómo va el anuncio 31 («abrir la cajita»). Si funciona, hacer esa estructura con 3 chicas nuestras, la cajita y el collar. El plano final, con el Lune y el Nuit juntos, vende el 3x2. Unos 4-5 $.
- **No se copia:** la escasez sin probar, los nombres de piedras ni los colgantes de trébol.

**Lucce «¿Todavía lo estás pensando?» (16-nov, Edu: «memorízalo como posible anuncio»):**
- Queda como **candidato 32 sin producir**. Guion, coste y cuándo producirlo, en `anuncios/campana-black-friday.md`.
- Producirlo cuando haya conjunto de retargeting aparte, o si la cesta sigue sin pagos con el «Comprar ahora».
- Antes de gastar, el «sí» de Edu ([[higgsfield-solo-con-permiso]]).
- Sacarlo al revisar la campaña.

Relacionado: [[videos-ugc]], [[biblioteca-contenido]], [[meta-ads-lecciones]].
