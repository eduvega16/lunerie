---
name: hacerlo-claude-no-sidekick
description: "Si Claude puede hacer algo en Shopify (CLI o navegador), lo hace él; no pasar prompts para Sidekick ni pasos para que los haga Edu"
metadata:
  node_type: memory
  type: feedback
  originSessionId: b078affc-ce0c-4dbb-82ed-b99738b2b422
  modified: 2026-11-15T23:37:50.493Z
---

Cuando una tarea de Shopify se puede hacer desde aquí (CLI, Storefront API o el admin con el Chrome de depuración),
Claude la hace él en vez de redactar un prompt para Sidekick o una lista de pasos para Edu.

**Why:** el 15-nov, con el correo de bienvenida, Edu preguntó «¿puedes subirlo tú?». Claude le preparó un prompt para
Sidekick, que solo encontró un borrador de Flow y no montó nada. Edu respondió «hazlo tú».

**How to apply:** probar primero la vía propia ([[shopify-admin-navegador]]). Sidekick o Edu solo para lo que de verdad
no llega (permisos que solo puede dar él, pagos, iniciar sesión). Los límites siguen igual: activar, gastar o publicar
necesita su OK ([[preguntar-antes-cambios-fuera-de-tarea]]).
