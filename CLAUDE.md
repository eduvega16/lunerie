# Lunerie · tienda online de regalos para ella

> **Cómo usar este fichero:** es el `CLAUDE.md` de la carpeta de la tienda (repo git en 2 PCs:
> `C:\Users\edu\lunerie` y `D:\LUNERIE`; `git pull` al empezar, `git push` al terminar); Claude Code lo
> lee solo al abrirla. Actualízalo al final de cada sesión (apartados 6 "Montaje" y 8 "Pendientes").
> Creado el 7-oct-2026 a partir de las sesiones del radar (`D:\aura-ai-portfolio\projects\05_producto_ganador\contexto\`).

---

## 1. Qué es
- **Lunerie**: tienda Shopify (creada el 7-oct-2026) de joyería y relojes pequeños para regalar, mercado **España**, Q4 2026.
- Dueño: **Edu** (programador, nuevo en Python/IA y en e-commerce). Modelo: dropshipping para testear → stock en
  España (Alibaba, exprés) cuando un producto funciona.
- Los productos los encuentra y valida el **radar** (otro proyecto): `D:\aura-ai-portfolio\projects\05_producto_ganador`.
  Allí están: el flujo completo (`contexto/FLUJO.md`), la calculadora (`cli.py calc`), el generador de fichas/textos
  (`cli.py lanzar`) y el registro diario de los tests (`cli.py test`). Esta carpeta es solo para la tienda.

## 2. Cómo trabajar con Edu
- En **español**, sencillo, paso a paso. Es una **brújula práctica**: acciones concretas; los riesgos en una línea y él decide.
- No pedir ni guardar datos personales (dirección, teléfono, NIF): en textos legales dejar huecos `[NIF]`, `[DIRECCIÓN]`.
- Claude **no puede abrir fichas de AliExpress** (captcha, no se fuerza) ni Amazon: Edu manda capturas.
- **Regla fija: ejecutar siempre los comandos dentro de VS Code** (los largos en segundo plano, vigilados con su log o
  `curl`). **Nunca abrir ventanas de terminal** (`Start-Process powershell` y similares). Si algo exige login en el
  navegador, avisar antes y buscar primero la variante sin interacción.

---

## 3. Identidad de marca
- **Nombre:** Lunerie ("lu-ne-rí": luna + *-erie* de *joaillerie*). Comprobado el 7-oct: ninguna joyería con ese nombre;
  lunerie.com aparcado. Dominio de la tienda: **lunerie.es** (ya conectado, ver apartado 6).
  Pendiente: buscar la marca en la OEPM (consultas2.oepm.es/LocalizadorWeb).
- **Estilo:** como **Calné** (calne.co): páginas limpias, fondo blanco, mucho aire, **la pieza manda y la marca casi
  no se ve** (logo pequeño, solo texto).
- **Página de marca (maqueta + ajustes):** https://claude.ai/artifact/MDZWWTrx5E6xxfgC8gfv2A
- **Logos (13-oct), en `marca/logos/`:** logo LUNERIE en tinta / blanco / oro (SVG + PNG, `marca/logos.py`).
  **Monograma oficial: L cursiva (Cormorant Italic) + destello dorado de 4 puntas, fondo verde** →
  `oficial-avatar-redes.png` (perfil de Instagram/TikTok) y `oficial-favicon.png` (pestaña, ya puesto en la tienda).
  Versión en fondo blanco (`monogramas/cursivaB-avatar.png`) solo para lo físico: pegatinas, tarjeta, packaging.
  Variantes descartadas en `marca/logos/monogramas/` (`marca/monogramas.py`). Nada de letras entrelazadas tipo LV.

| Token | Color | Uso |
|---|---|---|
| Blanco | `#FFFFFF` | fondo |
| Tinta | `#16201B` | textos |
| Verde Rolex | `#006039` | **solo** botones y barra superior |
| Oro | `#A6834A` | detalles finos |
| Niebla | `#F2F4F2` | fondo de las fotos de producto |

- **Letras:** Cormorant (logo en MAYÚSCULAS muy espaciadas, títulos) + Jost ligera (texto). Si el tema no las tiene,
  la serif fina y la sans geométrica más parecidas.
- **Shopify:** tema gratuito y sobrio, botones rectos verdes con texto blanco en mayúsculas, logo de texto ~120 px,
  barra superior verde con una frase, fotos todas 1:1 o 4:5 con el mismo fondo claro.
- **Voz:** pocas palabras, cálida, sin gritar. Ej.: anuncio *«Pequeño, ovalado y con piedras. El reloj que parece
  heredado.»* · tarjeta en la caja *«Para llevar cerca.»*
- **Reglas para que parezca cara:** sin emojis, sin «¡OFERTA!», sin contadores; verde solo en lo que se pulsa;
  cada pieza con nombre corto (Lune, Étoile, Nuit…).

---

## 4. Reglas legales y de negocio (España)
- Precios **con IVA incluido** (21 %). Envío gratis a península (Canarias/Ceuta/Melilla fuera al principio: aduana).
  **Baleares: sí, con un pequeño coste de envío** (decidido el 12-oct; importe por fijar), ya explicado en la página
  de Envíos.
- **Devoluciones (12-oct):** por desistimiento, el envío de vuelta lo paga el cliente; si llega roto, defectuoso o
  equivocado, Lunerie. Datos personales del titular: solo en Shopify (aviso legal), nunca en el repositorio.
- **Sin precios tachados inventados:** el precio tachado tiene que ser el **más bajo** que tuvo el producto en los
  30 días anteriores a la rebaja (no vale uno cualquiera de esos 30 días). El ahorro se cuenta con packs ("2.º por X €").
- **Devolución 14 días** (desistimiento) · **garantía legal 3 años** (no poner 2 años como hacen tiendas de fuera).
- **Productos personalizados: sin derecho de desistimiento** (art. 103 c LGDCU), pero si llega defectuoso o mal hecho
  se rehace. Avisar en la ficha: "se graba tal cual lo escribes, mayúsculas incluidas" + casilla de revisión obligatoria.
- **Aviso legal** (LSSI) con nombre, NIF, dirección y email · **banner de cookies** activado.
- No decir: "jade natural", "piedras preciosas/semipreciosas", "esmeralda" (son resina/vidrio/circonita).
  "Resistente al agua / no se oscurece" **solo** si el proveedor lo confirma por escrito.
- **Aranceles** de envíos pequeños desde China: ~3,5 €/ud (lo paga la tienda; ya está en las cuentas del radar).
- Pago: Shopify Payments (tarjeta, Apple/Google Pay) + PayPal. Bizum más adelante con app. COD no es el eje.

---

## 5. Productos

### 5.1 Reloj Lune · reloj vintage de mujer con piedras — ✅ elegido (producto 1)
- **Referencia / prueba de venta:** Calné lo vende desde nov-2025 a 39,95 € y es su n.º 5 en ventas (de 41).
  En Meta España nadie lo anuncia.
- **Modelo:** BS Bee Sister **FA1835** (marca del fabricante, no es réplica). Llamarlo «Lune» está bien, pero no
  decir que lo diseña o fabrica Lunerie. Con las muestras: mirar si la esfera lleva el logo BS (se verá en las fotos).
- **PVP 44,95 €** · upsell "2.º reloj por 19,95 €" · variantes: Dorado·piedra verde, Dorado·piedra azul,
  Plateado·piedra verde (esta solo si la muestra llega bien).
- **Cómo es:** cuarzo, esfera ovalada 12 mm, correa de eslabones 18 cm con piedras ovaladas (resina/vidrio),
  aleación dorada o plateada, pila puesta. Incluye caja de regalo + extractor de eslabones + tarjeta.
- **Avisos obligatorios:** no sumergible · esfera pequeña · correa 18 cm (muñecas < 16 cm: quitar eslabones) ·
  no es reloj de lujo.
- **Objeciones (reseñas):** me quedará grande · se estropea con agua · el cierre · ¿parece barato? · ¿llega para Navidad?
- **Proveedor (decidido el 8-oct):** de momento **AliExpress** "Face-Book Store" 5,59 € + 4,73 € envío
  (https://es.aliexpress.com/item/1005008660299253.html), que envía directo al cliente con su caja.
- **Objetivo: tienda con stock propio, no dropshipping.** Cuando el reloj funcione: stock en España + **packaging
  Lunerie** (caja, tarjeta «Para llevar cerca.», bolsa/papel) y envío desde aquí. Opciones de stock: Alibaba BS FA1835
  ~7,21 € desde 1 ud (Guangzhou Shiyi / Shihe / Taihe) o Shenzhen South America Watch 7,66 €. Antes de dar el paso,
  recalcular el CPA breakeven con el radar (`cli.py calc`) sumando packaging + envío nacional + exprés/DDP.
- **Cuentas (tarjeta, con aranceles, AliExpress):** CPA breakeven **~17,9 €**.
  Test (mismas reglas que el apartado 7): **escalar** con ≥ 3 ventas a CPA ≤ 12,5 € (70 % del breakeven) ·
  12,5-17,9 € iterar creativos · por encima de 17,9 € pierde dinero → matar si no baja ·
  ~18 € gastados sin carritos o ~36 € sin ventas → matar.
- **Muestras:** pedidas (dorado verde, dorado azul, plateado), llegan ~16-29 oct.
- **Decisión pendiente (recomendado b):** "te lo enviamos ajustado a tu muñeca" no se puede cumplir mientras envíe el
  proveedor de AliExpress. (a) preguntar al vendedor si quita eslabones con una nota, o (b) durante el test vender
  "incluye extractor + vídeo para ajustarlo en 2 minutos" y prometer el ajuste cuando haya stock en España.
- **Ficheros generados por el radar** (`cli.py lanzar`), en `05_producto_ganador/data/lanzamientos/reloj-vintage-piedras/`:
  `shopify_productos.csv` (importar en Shopify → entra como borrador), `landing.md` (textos + FAQ + lista
  "⚠️ Revisar antes de publicar"), `anuncios.md` (3 ángulos con guion de 15 s). Ficha fuente:
  `05_producto_ganador/lanzamientos/reloj-vintage.toml` (`marca_tienda = "Lunerie"`).
- Vídeos a grabar con las muestras: relojes en fila "elige tu piedra" · en la muñeca moviéndola · abriendo la caja ·
  quitando un eslabón.

### 5.2 Collar con nombre "firma" + lágrima de piedra del mes — 🟡 por validar (producto 2)
- **Qué es:** cadena dorada, nombre en letra de firma (con trazos) a un lado y colgante de circonita en lágrima del
  color del mes de nacimiento. Plateado / dorado / oro rosa.
- **Prueba de venta:** una tienda lo vende a **63 €** con la foto del proveedor (falta su enlace → mirar sus anuncios
  en Meta y si es de sus más vendidos). Referencia de cómo lo hacen otras: **Olivia Jewelry** (hecho en 4-8 días,
  personalizados sin devolución, caja regalo de pago).
- **Proveedores:** AliExpress **BillionCut** 15,49 € + 4,88 € envío (llega en ~3 semanas, 1.000+ vendidos, sin reseñas) ·
  Alibaba **Yiwu Shangjie Jewelry** (13 años, 4,5/5 con 1.764 valoraciones, ≥ 98 % a tiempo, 22 % recompra,
  top vendedor UE) **4,85 €** de 1 a 49 uds, se elige tipo de letra; envío estándar 26 oct-21 nov (lento).
- **PVP previsto 59,95 €** (por debajo de los 63 €, sin tachado). Pack verde con el reloj.
  CPA breakeven: **18,9 €** con BillionCut · **~30-33 €** con Yiwu Shangjie (~8-10 € puesto).
- **Confirmar con muestra (nombre "Lune"):** que tienen la letra "firma" y el montaje asimétrico · acero 316L +
  chapado (¿PVD?) · línea especial a España (objetivo 7-12 días) y precio exprés DHL · si trabajan con lista diaria
  de pedidos (Excel) y mandan seguimiento · foto de cada pieza antes de enviar · caja neutra sin factura/logo.
- **Cómo funcionará la personalización:** campo "Nombre a grabar" (máx. 10-12 letras) con una app de opciones de
  producto (Easify, Globo… plan gratis) + mes/piedra y metal como variantes + casilla "he revisado el nombre" →
  el pedido llega con el nombre → cada mañana se pasa la lista al proveedor → se pega el seguimiento en Shopify.
- **Plazos Navidad:** "hecho a mano en 3-5 días · entrega 10-15 días laborables"; fecha límite ~**1 de diciembre**
  (Black Friday 27-nov entra); en diciembre opción "envío exprés +9,95 €"; para rezagados, tarjeta regalo imprimible.

### 5.3 Otros candidatos (del radar, por si hay hueco)
Collar de familia / árbol de la vida con nombres (Bervi lo vende 1 año; Amazon 42-57 €; AliExpress 1-7 €) ·
gafas con cámara IA (69,95-79,95 €) · descartados: micro-infusión, paddle surf, pulsera tipo WHOOP, bolso hobo (réplica).

---

## 6. Montaje de la tienda — estado
- [x] Crear la tienda en Shopify (7-oct)
- [x] Datos: nombre LUNERIE, España, EUR, impuestos incluidos en los precios (comprobado el 7-oct por API)
- [x] Dominio **lunerie.es** conectado (visto el 7-oct; cuenta de Shopify con luneriecompany@gmail.com, plan Basic, EUR).
  **Correo de cara al cliente: hola@lunerie.es** (14-oct; en todos los textos legales y páginas, y como correo de
  la tienda en Shopify, visto el 15-oct)
- [~] Redes: **Instagram @lunerie_co** (13-oct; cuenta que Edu ya tenía, ~700 seguidores no orientados, se
      reutiliza por imagen de marca: renombrar a «Lunerie», cuenta profesional, avatar `oficial-avatar-redes.png`,
      bio «Joyas y relojes para regalar. / Para llevar cerca. / Envío gratis a península.», enlace lunerie.es,
      archivar lo antiguo y subir 3-6 publicaciones propias antes de los anuncios). Falta: TikTok y poner el
      enlace de Instagram en el pie de la tienda.
      **Meta (15-oct, comprobado con el conector):** porfolio empresarial **Lunerie** (1639315480899561), separado
      de LaFortuna · cuenta publicitaria **«LUNERIE PUBLI» 4565584937093443** (EUR, activa, **con método de pago**,
      dentro del porfolio) → **es la que se usa** · página «L U N E R I E» **1376893392171782** (página **nueva** creada por Edu el
      15-oct; la antigua 1311701355367588, en lafortuna.club, sobra → borrarla o archivarla) · Instagram **lunerie_co**
      (17841404549468255) enlazado a la cuenta publicitaria. La cuenta suelta 1551796336759107 (sin pago ni
      porfolio) sobra. Claude lo ve con el conector **«Meta ads Koco»** de claude.ai (nombre antiguo) · «pipeboard»
      solo ve LaFortuna: no usarlo para Lunerie.
- [x] Cobros activados por Edu (12-oct). Confirmar que PayPal también está.
- [ ] Envíos: zona España, gratis (decidir Baleares, apartado 4)
- [x] Tema publicado: **«Copia actualizada de Lunerie · marca» (id 209073799507)** = Horizon 1.0.5, actualizado por
  Edu el 12-oct. Shopify crea una **copia nueva con otro id** en cada actualización de Horizon: después de actualizar,
  cambiar el id en este fichero y volver a bajar `tema/tienda/`. En la del 12-oct se conservaron los 5 ficheros de
  `tema/codigo/` y todos los ajustes; esos 5 se quedan en su versión vieja (Shopify no actualiza ficheros
  modificados), así que no reciben los arreglos de Horizon. La anterior «Lunerie · marca» (208665149779) queda sin
  publicar como copia de seguridad.
- **Cómo se cambia el tema publicado: con Shopify CLI** (v4.9; tienda `qjxvnn-xq.myshopify.com`). El conector de
  Shopify de claude.ai **no** puede escribir en el tema publicado ni publicar (solo en temas sin publicar); la CLI sí.
  - **Login hecho en los dos PCs** (`C:\Users\edu\lunerie` el 8-oct, `D:\LUNERIE` el 9-oct, CLI 4.8.4; allí tenía
    sesión de otra cuenta → `shopify auth logout` antes). La CLI no hace login sin terminal interactiva, así que Claude abre una
    ventana: `Start-Process powershell -ArgumentList '-NoExit','-Command','shopify theme list --store qjxvnn-xq.myshopify.com'`
    y Edu entra en el navegador con la cuenta de Lunerie (si pregunta cuenta: «Log in with a different account»; las
    otras guardadas son Koco Essence y Star Brick). Lo mismo con `git push` si GitHub pide login: lanzarlo con
    `GIT_TERMINAL_PROMPT=1` y `GCM_INTERACTIVE=always` y se abre la ventana de GitHub.
  - `tema/tienda/` = copia completa del tema publicado (fuera de git). Si no existe o Edu ha tocado el editor (fotos,
    favicon): `shopify theme pull --store qjxvnn-xq.myshopify.com --theme 209073799507 --path tema/tienda` (la
    carpeta tiene que existir) y pasar sus cambios de `config/settings_data.json` a `build.py`, que si no los pisa.
  - Para subir: `python tema/build.py` (genera los JSON y los copia a `tema/tienda/`) →
    `shopify theme push --store qjxvnn-xq.myshopify.com --theme 209073799507 --path tema/tienda --allow-live --only <ficheros>`.
  - Mientras la tienda tenga contraseña, cambiar el publicado directamente no tiene riesgo. Con la tienda abierta,
    los cambios grandes se prueban antes en un tema sin publicar (`shopify theme push --unpublished`) y Edu lo publica.
  - **Vista previa local:** `shopify theme dev --store qjxvnn-xq.myshopify.com --path tema/tienda` →
    http://127.0.0.1:9292 (recarga sola al cambiar ficheros de `tema/tienda/`, sin tocar la tienda). **Edu no quiere
    ventanas de terminal:** Claude la lanza en segundo plano desde VS Code (Bash con `run_in_background`):
    `shopify theme dev --store qjxvnn-xq.myshopify.com --path tema/tienda --store-password "$(cat .claude/store-password)" 2>&1 | tee .claude/theme-dev.log`.
    La contraseña de la tienda está en `.claude/store-password` (fuera de git; Edu la dio el 10-oct y el 14-oct en `C:\Users\edu\lunerie`; en un PC nuevo
    hay que crear ese fichero). Claude ve si arrancó con `curl http://127.0.0.1:9292` y el log `.claude/theme-dev.log`.
    Crea un tema de desarrollo oculto en Shopify (no se publica). Capturas de pantalla para revisar: Chrome headless
    (`chrome --headless=new --user-data-dir=<temporal> --window-size=1440,2600 --screenshot=… <url>`; Edge se cuelga).
    Ojo: lo que se cambie en `tema/tienda/` a mano se pierde al ejecutar `build.py` si toca esos 5 JSON.
- [~] Tema y marca (apartado 3): copia **"Lunerie · marca"** del tema Horizon (id 208665149779) con
      colores, Cormorant + Jost ligera, botones verdes rectos en mayúsculas, logo de texto espaciado y centrado, barra
      verde «Envío gratis a península · Devolución en 14 días» (sin prometer el ajuste de muñeca) y pie en español con
      fondo niebla. 8-oct: **inicio** (portada sin foto con fondo niebla «Para llevar cerca.» · las piezas en 3 columnas ·
      envío / 14 días / garantía) y **ficha de producto** como la maqueta (fotos 4:5 en carrusel con miniaturas, título
      en Cormorant, garantías con puntos dorados, desplegables Envío / Devoluciones y garantía / Cuidados) · menú
      principal «Piezas · Contacto» (el menú es de la tienda, no del tema).
      **10-oct (subido a producción):** ficha con la estructura de Calné en versión verdadera — migas · título ·
      precio · línea · 4 ventajas (punto dorado «Para Navidad, pídelo antes del 1 de diciembre» [fecha a confirmar
      con el plazo real] · pila puesta y caja de regalo · envío gratis · 3 años + 14 días) · color · botón ancho sin
      selector de cantidad · caja «Segundo reloj por 19,95 €» (descuento automático **creado el 10-oct**, ver abajo) · desplegables Descripción / Ajustar la correa / ¿Se puede mojar? / Envío / Devoluciones y garantía /
      Cuidados · galería ancha (columnas desiguales). La ficha es **la misma para todos los productos**: el collar
      necesitará su plantilla (`product.collar.json`). Inicio: arriba la pieza destacada `reloj-lune` con ficha completa
      (el producto de prueba `reloj-luna-noir` se borró el 12-oct). Página de
      contraseña en español («Muy pronto… Avisarme», `tema/password.json`). NO copiar de Calné: tachado inventado,
      «stock limitado», «solo hoy», «100 % waterproof», 2 años / 100 días.
      Favicon puesto el 13-oct. Falta: foto de portada cuando haya muestras (editor → Portada → Fondo → Imagen) y cambiar **[PLAZO]** en el desplegable
      Envío. Ficheros fuente: `tema/` (`build.py` genera los JSON que se suben a la copia del tema; Shopify no acepta
      `content:` en el CSS personalizado ni `gap` > 48).
- [~] Políticas y páginas: textos en `legal/` (10-oct). Página **Preguntas frecuentes** creada y en el menú
      principal («Piezas · Preguntas frecuentes · Contacto»). **Las 6 políticas las pega Edu** en Configuración →
      Políticas: el conector **no tiene permiso** `write_legal_policies` (las páginas y menús sí). Rellenar los huecos
      de `legal/README.md` en Shopify y en la página de FAQ ([PLAZO], [BALEARES]).
- [x] Banner de cookies de Shopify activado por Edu (14-oct; carga `privacy-banner/storefront-banner.js`). Falta que
      Edu lo mire en incógnito (Aceptar y Rechazar a la vez, texto en español).
- [x] **App Facebook & Instagram instalada por Edu (15-oct)**: píxel **«Lunerie's pixel» 1096538246614496** (porfolio
      Lunerie, uso «publicidad y analítica», cookie propia activa) puesto en la tienda por la app (apiClientId 2329312,
      compartir datos «optimized» + todos los eventos). Solo se activa **con consentimiento** (privacyPurposes
      ANALYTICS/MARKETING → espera al «Aceptar» del banner). **Falta:** asignar el píxel a la cuenta «LUNERIE PUBLI»
      (Configuración del negocio → Orígenes de datos → Conjuntos de datos → Añadir activos) y ver el primer evento
      (Edu acepta cookies en incógnito y navega → Claude mira `ads_get_dataset_stats`).
- [ ] App de TikTok
- [x] **Reloj Lune creado el 10-oct** (`reloj-lune`, activo y en Tienda online): 44,95 €, opción **Color** con
      «Dorado · piedra verde» y «Plateado · piedra verde» (SKU LUNE-DOR-VER / LUNE-PLA-VER), sin control de stock
      (dropshipping), coste 13,82 € (5,59 + 4,73 envío + 3,5 aranceles), fotos del proveedor de
      `tema/fotos productos/reloj/` pasadas a 4:5. Anclado arriba en el inicio. **Falta:** la variante «Dorado · piedra
      azul» (no había foto) y cambiar a fotos propias cuando lleguen las muestras. Cómo se suben fotos desde aquí:
      `stagedUploadsCreate` (PUT) → `curl -X PUT` → `productSet` con `files`/`variants.file`. PayPal ya sale en la ficha.
      **Bolitas de color (10-oct, en producción):** la opción «Color» se ve como círculos (dorado / plateado / oro
      rosa) con «Color  valor elegido» encima, como Calné. Va **por CSS** (`BOLITAS` en `build.py` →
      `tema/codigo/snippets/lunerie-bolitas.liquid`) + un cambio en `tema/codigo/snippets/variant-main-picker.liquid`
      (código del tema guardado en git; `build.py` lo copia a `tema/tienda/`). Funciona con cualquier valor que
      empiece por «Dorado», «Plateado» u «Oro rosa». Las bolitas «oficiales» de Shopify no se pudieron enlazar por API
      (error de restricción de categoría); quedaron creados los colores estándar Dorado/Plateado/Oro rosa y la
      categoría «Relojes de pulsera» en el producto. **Límite:** el CSS personalizado de una sección no admite más
      de 500 caracteres → lo largo va en un snippet. Ficha en móvil: miniaturas bajo la foto, título en mayúsculas
      (Cormorant), caja de oferta **verde con texto blanco** (Edu la prefirió así). Capturas reales de móvil:
      script de Chrome con devtools (`Emulation.setDeviceMetricsOverride` mobile) — las capturas headless normales
      a 390-440 px engañan (parecía que la ficha se salía por la derecha y no es así).
      **Descuento «Segundo reloj por 19,95 €» (10-oct, activo):** automático, compra X lleva Y: por cada reloj Lune,
      otro Lune con 25 € menos (44,95 + 19,95 = 64,90 €; probado en la cesta). Se repite por cada pareja (4 relojes →
      2 descuentos) y se combina con descuentos de envío. Si se cambia el precio del Lune, ajustar los 25 € en
      Descuentos.
      **10-oct (en producción):** línea de Navidad con **bolita roja que late** (bloque `custom-liquid`, `NAVIDAD`
      en `build.py`; quieta si el móvil pide reducir movimiento) · «Llega en su caja de regalo» con **icono de
      regalo** SVG propio (`REGALO`; ya no se menciona la pila) · **aviso en la cesta** «Añade un segundo reloj por
      19,95 €» con un botón por color y su bolita (`tema/codigo/snippets/lunerie-segundo-reloj.liquid`, generado por
      `build.py`; se pinta en `cart-drawer.liquid` y `sections/main-cart.liquid`, copias en `tema/codigo/`). Sale con
      un número impar de Lune; añade por `fetch` y va a /cart. Probado: 1 reloj → aviso → añadir → 64,90 € y el aviso
      desaparece. Página de la cesta en español (`tema/cart.json`). En la vista previa local, el navegador de
      pruebas con perfil nuevo acaba en /password (no tiene la cookie): probar el carrito con `curl` y cookie.
      Shopify Payments ya activo (salen Shop Pay y Google Pay en la cesta).
- [x] **Portada nueva (14-oct, en producción), centrada en el reloj Lune** (crítica de diseño + rediseño):
      portada «El reloj que *parece heredado.*» con la **foto en óvalo y filo dorado** (la firma visual, como la
      esfera) y «Ver el reloj · 44,95 €» + «Segundo reloj por 19,95 €» · «Elige el tuyo» (ficha rápida sin cantidad;
      en móvil sin foto, porque ya está en el óvalo) · «Cómo es» (3 rasgos reales) · franja verde «Uno para ti y otro
      para regalar.» · «Antes de comprar» (4 dudas + enlace a Preguntas frecuentes) · 3 promesas. Fuera «Para llevar
      cerca.» (a Edu no le gusta) y «Las piezas» con un solo producto. Las partes a medida están en
      `tema/codigo/snippets/lunerie-inicio.liquid` (se pintan con secciones «Liquid personalizado»: `parte()` en
      `build.py`). Cuando llegue el collar: sección «Las piezas» de 2 columnas.
      **Cambios del 14-oct (en producción):** titular nuevo «Un reloj que se lleva *como una joya.*» (a Edu no le
      gustaba «parece heredado») · fuera la ficha rápida «Elige el tuyo» (sección `destacado` con `"disabled": true`,
      se puede reactivar) · **portada con vídeo de fondo** (`parte('hero-video')`): vídeo del CDN de Shopify en bucle,
      oscurecido (filtro brightness .72), con **grano de película** (SVG de ruido animado) y el óvalo dorado de línea
      fina con titular, botón y «Segundo reloj por 19,95 €» dentro. **OJO: el vídeo muestra otro reloj (esfera
      «NAIDU», piedras rosas): cambiarlo por uno de las muestras antes de abrir** (URL en `hero-video` de
      `lunerie-inicio.liquid`). Volver a la portada con foto: `parte("hero", arriba=8, abajo=40)` en `build.py`.
      Menú principal (14-oct): «Reloj Lune» (ficha `/products/reloj-lune`) · Preguntas frecuentes · Contacto.
- [ ] Quitar la contraseña de la tienda

> Claude está conectado a Shopify (conector de claude.ai) con la tienda Lunerie. Antes estaba Star Brick: al cambiar
> de tienda se desconecta la otra.
> **Si el conector no carga** (pasó el 12-oct): usar la Admin API con la CLI, que no depende de él:
> `shopify store execute -s qjxvnn-xq.myshopify.com -q "<query>" --json --no-input` (añadir `--allow-mutations` para
> escribir; `--query-file` / `--variable-file` para operaciones largas). Permisos dados por Edu el 12-oct con
> `shopify store auth` (productos, inventario, páginas, políticas, menús, archivos, temas, publicaciones, envíos,
> pedidos en lectura, descuentos); en `D:\LUNERIE` dados el 14-oct. **Sin ventana:** lanzar en segundo plano
> `shopify store auth --store qjxvnn-xq.myshopify.com --scopes <lista> 2>&1 | tee .claude/store-auth.log`: abre el
> navegador solo y Edu acepta (probado el 14-oct). El conector de claude.ai sigue sin `write_legal_policies`.

## 7. Test de ~90 € (por producto)
Meta Ads, ABO: 3 conjuntos (1 ángulo cada uno) × 10 €/día × 3 días = 90 €. Cada día, en el radar:
`uv run python cli.py test <id> --dia N --gasto … --imp … --clicks … --atc … --compras …`
KILL si gastas 1× CPA BE sin carritos o 2× sin ventas · ESCALAR con ≥ 3 ventas a ≤ 70 % del CPA BE ·
alertas si CTR < 1 % o CPC > 0,90 €. Máximo 2 productos en test a la vez.

## 8. Calendario y pendientes (a 14-oct-2026)

### Para empezar la próxima sesión
- **Al abrir:** `git pull`. Shopify: el conector de claude.ai puede no cargar → usar `shopify store execute`
  (apartado 6); tema publicado = **209073799507**.
- **Esperando a Edu:**
  1. ~~Política de privacidad~~: subida la nuestra el 14-oct (gestión automática desactivada).
  2. **Dirección (14-oct): Edu deja la de su casa**, sin oficina virtual. Los textos dicen solo «41940 Tomares
     (Sevilla)»; la LSSI pide el domicilio completo → si Edu quiere, Claude la pone completa al subir (nunca en git).
  3. **Plazo de envío:** por definir cuando llegue la muestra (AliExpress dice ~14 días) → quitar [PLAZO] de envíos,
     FAQ y ficha del reloj (`build.py`).
  4. Envíos en el admin: península gratis + **Baleares con coste** (¿3,95 €?) · @lunerie en TikTok ·
     Meta listo (15-oct: porfolio Lunerie + cuenta «LUNERIE PUBLI» con pago + página + Instagram) → app
     Facebook & Instagram instalada → falta asignar el píxel a LUNERIE PUBLI y ver el primer evento.
- **Siguiente con Claude:** app Facebook & Instagram + píxel · revisar la ficha del reloj con `landing.md`
  · fotos del proveedor en 4:5 (si Edu las pasa) · anuncios cuando lleguen las muestras.

### Resumen de la sesión 12-13 oct
- Horizon actualizado a 1.0.5 por Edu → **copia nueva con otro id** (209073799507); se conservó todo; ids
  cambiados aquí y `tema/tienda/` vuelto a bajar.
- Shopify CLI ahora también hace de Admin API (`shopify store execute`, permisos dados por Edu).
- Borrado el producto de prueba «Reloj Luna Noir». Cobros activados por Edu.
- **Legales subidos a Shopify** con `legal/subir.py` (datos personales solo al ejecutar, nunca en git):
  devolución por desistimiento la paga el cliente; roto/defectuoso/equivocado, Lunerie; personalizados sin
  devolución salvo defecto; Baleares con un pequeño coste.
- **Logos** (`marca/`): logo LUNERIE + monograma oficial (L cursiva + destello, verde) → favicon puesto.
- Calendario hasta Navidad/Reyes (abajo). Fotos de Calné: Edu asume el riesgo; mejor las del proveedor.
**Objetivo: tienda abierta y test del reloj en marcha el lunes 26-oct (como muy tarde el 2-nov)**, para decidir
antes del 9-nov y llegar a Black Friday (27-30 nov) con un producto validado. Fechas límite: Navidad ~4-dic
(AliExpress, ~2 semanas; afinar con el plazo real) · Reyes ~18-dic · después, tarjeta regalo.
- 12-18 oct · tienda lista para cobrar: legales en Shopify, cookies, Meta (página FB + cuenta publicitaria + píxel),
  @lunerie, envíos/Baleares, escribir a Yiwu (collar) si se quiere para Navidad.
- 19-25 oct · muestras → fotos 4:5 y 4 vídeos → 3 anuncios.
- 26 oct-1 nov · quitar contraseña + test de 90 € (3 días). 2-8 nov · decidir. 9-26 nov · escalar + Black Friday.
- **No tocar el precio de 44,95 € hasta Black Friday** (un tachado en BF tiene que ser el precio más bajo de los 30 días anteriores).
- **Fotos:** las de `tema/fotos productos/reloj/` son **de Calné** (Edu lo sabe y asume el riesgo). Plan: sustituirlas
  por las del proveedor (AliExpress/Alibaba) o por fotos propias de las muestras. Mejorarlas con IA (Real-ESRGAN) no
  hace falta a 4K (Shopify las sirve a ~2000 px; ideal 2048×2560): están blandas por compresión (42 KB) y el reloj
  ocupa ~15 % del ancho.

1. ~~Publicar el tema~~ (8-oct). ~~Cobros~~ (12-oct). Login de Shopify CLI y de GitHub hechos en este PC. Pendiente:
   el plazo de envío para cambiar **[PLAZO]** (desplegable Envío).
2. ~~Políticas y páginas legales~~ **subidas el 12-oct** con `legal/subir.py` (aviso legal, devoluciones, envíos,
   términos, contacto + páginas Envíos y Preguntas frecuentes). Falta: [PLAZO], dirección comercial y privacidad
   (ver «Para empezar la próxima sesión»).
   **Edu, en el admin:** envíos (península gratis + Baleares con coste) · foto como primer medio del producto · formato de precio «44,95 €»
   (Configuración → General → Moneda) · @lunerie en redes.
3. Escribir a Alibaba (reloj): precio DDP exprés para 20 y 50 uds (mensaje en la sesión 07-oct del radar). No corre
   prisa: el test va con AliExpress; sirve para preparar el paso a stock propio + packaging.
4. Pedir presupuesto de packaging Lunerie (caja, tarjeta, bolsa) para meterlo en las cuentas del stock propio.
5. Escribir a Yiwu Shangjie (collar) y pedir muestra "Lune"; pasar el enlace de la tienda de 63 €.
6. Decidir lo del "ajustado a tu muñeca" (5.1). La tienda ya **no** lo promete en la barra; la página de marca
   (artifact) aún dice «Te lo enviamos ajustado a tu muñeca» → actualizarla cuando se decida.
7. ~~Decidir Baleares~~ (12-oct: con un pequeño coste de envío; falta fijar el importe).
8. Cuando lleguen las muestras: fotos y vídeos propios → anuncios → test del reloj.

## 9. Enlaces
- Página de marca: https://claude.ai/artifact/MDZWWTrx5E6xxfgC8gfv2A
- Repositorio (privado): https://github.com/eduvega16/lunerie — remoto con `eduvega16@` en la URL porque el PC
  tiene guardada otra cuenta de GitHub (`kocoessence`). `git pull` al empezar, `git push` al terminar.
- Calné (referencia): https://calne.co/products/uthai-womens-watch-ladies-bracelet-luxury-brand-waterproof-retro-natural-dongling-stone-hotan-jade-advanced-chain-watches-gift
- Reloj AliExpress: https://es.aliexpress.com/item/1005008660299253.html
- Reloj Alibaba: https://www.alibaba.com/product-detail/BS-Bee-Sister-1835-FA1835-Latest_1601607745947.html
- Biblioteca de anuncios de Meta: https://www.facebook.com/ads/library/
- OEPM (marcas): https://consultas2.oepm.es/LocalizadorWeb/
