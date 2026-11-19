---
name: instagram-mensajes
description: Leer y contestar los DM de Instagram de Lunerie con oficina/mensajes_ig.py (Business Suite headless); la API no ve los DM
metadata:
  node_type: memory
  type: reference
  originSessionId: b078affc-ce0c-4dbb-82ed-b99738b2b422
  modified: 2026-11-17T22:03:17.587Z
---

Los mensajes directos de Instagram de Lunerie se leen y contestan con `python oficina/mensajes_ig.py lista | hilo "<nombre>" | responder "<nombre>" "<texto>" [--confirmar]`.

- El script usa la bandeja de Meta Business Suite con Chrome sin ventana, perfil `.claude/meta-perfil`, puerto 9223.
- Edu entró en ese perfil el 17-nov-2026 con la cuenta de Facebook que administra Lunerie. La cuenta «Eduardo Vega» solo ve southshoes: si la sesión cae ahí, hay que pedirle que entre con la otra o con «Continuar con Instagram».
- **La API no sirve para los DM.** La clave tiene `instagram_manage_messages`, pero devuelve 0 conversaciones porque la app «Lunerie Claude Publisher» está en modo desarrollo. Publicarla da «no se han completado todos los requisitos»; se descartó el 17-nov.
- **Enviar solo con el OK de Edu a ese texto.** Sin `--confirmar` el script solo hace un ensayo.
- Las respuestas siguen [[mensajes-clientas]].
- Si la sesión caduca, avisar a Edu antes de abrir una ventana visible ([[sin-ventanas-terminal]]).
- En «Marta Rico» hay conversaciones personales de Edu: no tocarlas.

Relacionado: [[instagram-publicacion-api]], [[shopify-admin-navegador]], [[pedidos-por-instagram]].
