---
name: elevenlabs-voz
description: "ElevenLabs para voces en off: plan Free de Edu (cuenta «La fortuna»), qué deja y qué no por API, script marca/voz_elevenlabs.py"
metadata:
  node_type: memory
  type: reference
  originSessionId: b20f0a0e-86fd-4f00-b85b-452279a19989
  modified: 2026-11-13T19:01:47.191Z
---

**5-nov (tarde): Edu pasa al plan Starter** (1 $ el primer mes, luego 6 $/mes; renovación hacia el 5-dic: recordarle antes si lo cancela). Antes, plan **Free**: API y licencia comercial de voz, 10.000 caracteres al mes con eleven_v4. La clave está en `.env.local` como `ELEVENLABS_KEY`. Edu la pegó en el chat el 5-nov y se le recomendó regenerarla.

**Lo que el Free NO deja por API:**
- Voces de la biblioteca pública: error 402 `paid_plan_required`.
- Diseñar voces: error 403.

**Lo que sí funciona:**
- Las voces de serie (premade), en español con `language_code: es` y `eleven_v4`.
- Las «professional» que ya estén en la cuenta (hay un hombre castellano, Martin Osborne).

Para voces de mujer de España sin pagar, Edu puede diseñar o añadir la voz en la web. Usarla después por API puede seguir bloqueado en Free; queda por probar.

Edu quiere voces que suenen a chica normal grabando con el móvil, no a doblaje: elegir voces «conversational»/«social media» de España (muestras en `marca/fotos-ia/ugc-collar/voz/muestras-casual/`), texto hablado y filtro de móvil. La música la pone él en postproducción.

**Voz elegida por Edu (5-nov): «Silvia · expressive»** (`DNtbMnLZ43q8pReedyYw`, biblioteca, social media), con el filtro de móvil (`voz-<nombre>-movil.mp3`). Usarla por defecto en los vídeos UGC.

**13-nov (anuncio 31): las voces generadas frase a frase «suenan poco naturales» (Edu).** Lo que le gustó:
- **Jenni** (`IrS0oRyKeMCyPJVVpPyg`, «Natural & Conversational», de España) con `eleven_v4`.
- **Una sola toma seguida** con texto hablado («Mira cómo llega su collar…»).
- Cortada en trozos con los tiempos de cada palabra (speech-to-text de ElevenLabs, `scribe_v2`).
- Filtro de móvil **sin eco**.

Está en `marca/doblar.py` (`TOMAS`). Para vídeos nuevos, preferir esto a la voz frase a frase. El plan Starter no deja `mp3_44100_192`: usar `_128`.

**Script:** `python marca/voz_elevenlabs.py generar <voice_id> <nombre>` genera el mp3 y el srt con los tiempos exactos. Después `python marca/ugc_montaje.py <nombre>` lo monta.

Relacionado: [[instagram-publicacion-api]].
