---
name: shopify-admin-navegador
description: "Lo que la API/CLI de Shopify no deja (Messaging, ajustes, grabaciones de Propel) lo hace Claude en el admin con un Chrome de depuración + Playwright (oficina/admin_shopify.py); sin ventana si la sesión sigue viva"
metadata:
  node_type: memory
  type: reference
  originSessionId: b078affc-ce0c-4dbb-82ed-b99738b2b422
  modified: 2026-11-16T20:08:08.165Z
---

Cuando la CLI no tiene permiso o no hay API (Shopify Email/Messaging, automatizaciones, algunos ajustes), Claude maneja
el admin con un Chrome aparte con `--remote-debugging-port=9222` y el perfil `D:/LUNERIE/.claude/shopify-perfil`
(fuera de git; Edu inicia sesión él, Claude nunca toca contraseñas) y Playwright `connect_over_cdp`. Herramienta e
instrucciones: `oficina/admin_shopify.py` (`esperar`, `abrir`, `app`, `asunto`, `seccion`, `pegar_liquid`).

**Why:** el 15-nov el correo de bienvenida solo se podía montar en Messaging (no hay API) y Edu dijo «hazlo tú». Se hizo
entero así y quedó en borrador con prueba mandada.

**Sin ventana (16-nov):** si la sesión guardada sigue viva, el mismo Chrome con `--headless=new` entra al admin sin
abrir nada y sin que Edu haga nada. Así se leyeron las grabaciones de Propel Replays (`oficina/propel_replays.py`), los
pagos y las automatizaciones. Solo para LEER; cerrarlo al acabar (`propel_replays.py cerrar`). Si sale la página de
entrar, entonces sí con ventana y que entre Edu.

**How to apply:** avisar a Edu antes de abrir Chrome (tiene que entrar él) y lanzarlo en segundo plano (nada de
ventanas de terminal, ver [[sin-ventanas-terminal]]). El contenido de las apps va en un iframe (`app(pg)`). Activar,
pagar o publicar algo desde ahí sigue pidiendo su OK. Relacionado: [[hacerlo-claude-no-sidekick]].
