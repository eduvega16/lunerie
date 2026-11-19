---
name: olivia-referencia-diseno
description: "Edu usa oliviajewelry.com como referencia de diseño y UX de la ficha; se copia midiendo la web real, no a ojo"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 7f0dea43-fb2c-4818-be0a-6d3b8cbd08f2
  modified: 2026-10-28T22:48:55.988Z
---

Cuando Edu manda una captura de Olivia Jewelry (galería a media pantalla, «Pairs well with», columna que queda fija, rasca, pie, historia bajo la ficha) y dice «como en Olivia», quiere esa estructura y proporciones en Lunerie, no una versión parecida.

**Why:** el 28-oct pidió foto a pantalla completa en PC, carrusel «Te puede interesar» y el scroll de la columna «como Olivia». Mi primer ajuste («pegar el texto a la foto») le gustó menos que las proporciones reales de Olivia: foto con 48 px de margen y texto centrado en su mitad con aire a los dos lados.

**How to apply:** abrir la ficha real con Playwright (`https://www.oliviajewelry.com/products/everyday-essential-gold-hoops`, `wait_until='domcontentloaded'`, no `networkidle`), medir márgenes, anchos y qué queda fijo al hacer scroll con la rueda del ratón, y ajustar Lunerie a esas cifras. Copiar la **estructura y el comportamiento**, no sus afirmaciones: Olivia pone «waterproof», «hipoalergénico» y «2 años de garantía», que en Lunerie no se pueden decir (CLAUDE.md, apartado 4). Relacionado: [[ver-en-tienda-real]], [[pruebas-visuales-lunerie]].

**Instagram (19-nov):** la cuenta buena es **@oliviajewelryco**; @oliviajewelry es otra. Edu quiere que nuestro Instagram y los anuncios se parezcan a ella «lo máximo posible»: «copiar, así funciona el mundo», con nuestro toque y sin sus afirmaciones.
- **Cómo verlo sin iniciar sesión:** el perfil (12 últimas) con Playwright y el perfil `.claude/meta-perfil`, sin pulsar «Continuar con Facebook». Cada publicación, con `curl -A facebookexternalhit` (`og:image` y `og:title` = el texto). Los reels no traen el vídeo.
- Análisis en `oficina/referencias/olivia-ig-2026-11-19/README.md`. Ver también [[estetica-limpia-elegante]].
