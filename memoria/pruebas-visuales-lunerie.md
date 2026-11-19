---
name: pruebas-visuales-lunerie
description: "Cómo comprobar la tienda en este PC (Playwright con el Chrome instalado) y a qué anchos, incluido el de la pantalla de Edu"
metadata:
  node_type: memory
  type: reference
  originSessionId: 7f0dea43-fb2c-4818-be0a-6d3b8cbd08f2
  modified: 2026-10-28T22:49:00.656Z
---

La pantalla de Edu en PC mide unos **2554×1316** (sus capturas salen de 2309 a 2554 px de ancho). Un diseño que solo se ve bien a 1440 puede quedar descuadrado en la suya: el 28-oct el texto de la ficha quedaba a ~300 px de la foto en su pantalla y a ~150 px en 1440.

**How to apply:** tras cada cambio al tema, comprobarlo en la tienda real (`lunerie.es`, con `?x=<número>` distinto cada vez para evitar caché) a **2554×1316**, **1440×900** y móvil **390×844** (`is_mobile`, `has_touch`, `device_scale_factor=2`). Playwright de Python no tiene su navegador descargado en este PC: usar `chromium.launch(executable_path="C:/Program Files/Google/Chrome/Application/chrome.exe")` (y usar `wait_until='domcontentloaded'` + `wait_for_timeout`). Para ver el scroll de verdad, `page.mouse.wheel`; `scrollTo` no movía la página. El banner de cookies tapa la parte de abajo: ocultar `#shopify-pc__banner` antes de la captura. Los ajustes de tema se suben con la CLI de Shopify (CLAUDE.md, apartado 6); tras subirlos, esperar unos segundos y volver a leer. Relacionado: [[ver-en-tienda-real]], [[olivia-referencia-diseno]].
