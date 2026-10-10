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
  **Baleares: por decidir** (gratis, con coste o fuera); la barra dice «península», así que hay que dejarlo claro
  en la página de Envíos.
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
- [x] Dominio **lunerie.es** conectado (visto el 7-oct; email de la tienda luneriecompany@gmail.com, plan Basic, EUR)
- [ ] Reservar @lunerie en Instagram y TikTok
- [ ] Cobros: Shopify Payments + PayPal (pide datos de autónomo/empresa)
- [ ] Envíos: zona España, gratis (decidir Baleares, apartado 4)
- [x] Tema **"Lunerie · marca"** (id 208665149779) **publicado por Edu el 8-oct**.
- **Cómo se cambia el tema publicado: con Shopify CLI** (v4.9; tienda `qjxvnn-xq.myshopify.com`). El conector de
  Shopify de claude.ai **no** puede escribir en el tema publicado ni publicar (solo en temas sin publicar); la CLI sí.
  - **Login hecho en los dos PCs** (`C:\Users\edu\lunerie` el 8-oct, `D:\LUNERIE` el 9-oct, CLI 4.8.4; allí tenía
    sesión de otra cuenta → `shopify auth logout` antes). La CLI no hace login sin terminal interactiva, así que Claude abre una
    ventana: `Start-Process powershell -ArgumentList '-NoExit','-Command','shopify theme list --store qjxvnn-xq.myshopify.com'`
    y Edu entra en el navegador con la cuenta de Lunerie (si pregunta cuenta: «Log in with a different account»; las
    otras guardadas son Koco Essence y Star Brick). Lo mismo con `git push` si GitHub pide login: lanzarlo con
    `GIT_TERMINAL_PROMPT=1` y `GCM_INTERACTIVE=always` y se abre la ventana de GitHub.
  - `tema/tienda/` = copia completa del tema publicado (fuera de git). Si no existe o Edu ha tocado el editor (fotos,
    favicon): `shopify theme pull --store qjxvnn-xq.myshopify.com --theme 208665149779 --path tema/tienda` (la
    carpeta tiene que existir) y pasar sus cambios de `config/settings_data.json` a `build.py`, que si no los pisa.
  - Para subir: `python tema/build.py` (genera los JSON y los copia a `tema/tienda/`) →
    `shopify theme push --store qjxvnn-xq.myshopify.com --theme 208665149779 --path tema/tienda --allow-live --only <ficheros>`.
  - Mientras la tienda tenga contraseña, cambiar el publicado directamente no tiene riesgo. Con la tienda abierta,
    los cambios grandes se prueban antes en un tema sin publicar (`shopify theme push --unpublished`) y Edu lo publica.
  - **Vista previa local:** `shopify theme dev --store qjxvnn-xq.myshopify.com --path tema/tienda` →
    http://127.0.0.1:9292 (recarga sola al cambiar ficheros de `tema/tienda/`, sin tocar la tienda). **Edu no quiere
    ventanas de terminal:** Claude la lanza en segundo plano desde VS Code (Bash con `run_in_background`):
    `shopify theme dev --store qjxvnn-xq.myshopify.com --path tema/tienda --store-password "$(cat .claude/store-password)" 2>&1 | tee .claude/theme-dev.log`.
    La contraseña de la tienda está en `.claude/store-password` (fuera de git; Edu la dio el 10-oct; en el otro PC
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
      selector de cantidad · caja «Segundo reloj por 19,95 €» (niebla con borde oro; **crear ese descuento antes de
      abrir**) · desplegables Descripción / Ajustar la correa / ¿Se puede mojar? / Envío / Devoluciones y garantía /
      Cuidados · galería ancha (columnas desiguales). La ficha es **la misma para todos los productos**: el collar
      necesitará su plantilla (`product.collar.json`). Inicio: arriba la pieza destacada `reloj-luna-noir` (producto
      de prueba de Edu: 195 € con tachado 245 €, sin stock, primer medio un vídeo) con ficha completa. Página de
      contraseña en español («Muy pronto… Avisarme», `tema/password.json`). NO copiar de Calné: tachado inventado,
      «stock limitado», «solo hoy», «100 % waterproof», 2 años / 100 días.
      Falta: favicon, foto de portada cuando haya muestras (editor → Portada → Fondo → Imagen) y cambiar **[PLAZO]** en el desplegable
      Envío. Ficheros fuente: `tema/` (`build.py` genera los JSON que se suben a la copia del tema; Shopify no acepta
      `content:` en el CSS personalizado ni `gap` > 48).
- [~] Políticas y páginas: textos en `legal/` (10-oct). Página **Preguntas frecuentes** creada y en el menú
      principal («Piezas · Preguntas frecuentes · Contacto»). **Las 6 políticas las pega Edu** en Configuración →
      Políticas: el conector **no tiene permiso** `write_legal_policies` (las páginas y menús sí). Rellenar los huecos
      de `legal/README.md` en Shopify y en la página de FAQ ([PLAZO], [BALEARES]).
- [ ] Banner de cookies (Configuración → Privacidad del cliente)
- [ ] Apps: Facebook & Instagram (píxel Meta), TikTok
- [x] **Reloj Lune creado el 10-oct** (`reloj-lune`, activo y en Tienda online): 44,95 €, opción **Color** con
      «Dorado · piedra verde» y «Plateado · piedra verde» (SKU LUNE-DOR-VER / LUNE-PLA-VER), sin control de stock
      (dropshipping), coste 13,82 € (5,59 + 4,73 envío + 3,5 aranceles), fotos del proveedor de
      `tema/fotos productos/reloj/` pasadas a 4:5. Anclado arriba en el inicio. **Falta:** la variante «Dorado · piedra
      azul» (no había foto) y cambiar a fotos propias cuando lleguen las muestras. Cómo se suben fotos desde aquí:
      `stagedUploadsCreate` (PUT) → `curl -X PUT` → `productSet` con `files`/`variants.file`. PayPal ya sale en la ficha.
- [ ] Quitar la contraseña de la tienda

> Claude está conectado a Shopify (conector de claude.ai) con la tienda Lunerie. Antes estaba Star Brick: al cambiar
> de tienda se desconecta la otra.

## 7. Test de ~90 € (por producto)
Meta Ads, ABO: 3 conjuntos (1 ángulo cada uno) × 10 €/día × 3 días = 90 €. Cada día, en el radar:
`uv run python cli.py test <id> --dia N --gasto … --imp … --clicks … --atc … --compras …`
KILL si gastas 1× CPA BE sin carritos o 2× sin ventas · ESCALAR con ≥ 3 ventas a ≤ 70 % del CPA BE ·
alertas si CTR < 1 % o CPC > 0,90 €. Máximo 2 productos en test a la vez.

## 8. Pendientes (a 10-oct-2026)
1. ~~Publicar el tema~~ (hecho el 8-oct). Login de Shopify CLI y de GitHub hechos en este PC. Pendiente: el plazo de envío para cambiar **[PLAZO]** (desplegable Envío).
2. **Siguiente con Claude (necesita el conector de Shopify reconectado): políticas y páginas legales.** Borradores
   ya escritos en `legal/` (10-oct; huecos en `legal/README.md`: [NOMBRE], [NIF], [DIRECCIÓN], [PLAZO], [BALEARES],
   quién paga la devolución). Falta que Edu rellene los huecos y crearlas en Shopify (solo existe la página Contacto). Después: crear el reloj Lune (`reloj-lune`, 44,95 €,
   3 variantes) a partir de `landing.md` del radar con las fotos provisionales de `tema/fotos_prueba.py`, y anclarlo
   en el inicio en vez de `reloj-luna-noir` (cambiar `"product"` en la sección `destacado` de `build.py`).
   **Edu, en el admin:** Shopify Payments + PayPal (empezar ya: tarda en aprobarse) · envíos + Baleares · foto como
   primer medio del producto · formato de precio «195,00 €» (Configuración → General → Moneda) · @lunerie en redes.
3. Escribir a Alibaba (reloj): precio DDP exprés para 20 y 50 uds (mensaje en la sesión 07-oct del radar). No corre
   prisa: el test va con AliExpress; sirve para preparar el paso a stock propio + packaging.
4. Pedir presupuesto de packaging Lunerie (caja, tarjeta, bolsa) para meterlo en las cuentas del stock propio.
5. Escribir a Yiwu Shangjie (collar) y pedir muestra "Lune"; pasar el enlace de la tienda de 63 €.
6. Decidir lo del "ajustado a tu muñeca" (5.1). La tienda ya **no** lo promete en la barra; la página de marca
   (artifact) aún dice «Te lo enviamos ajustado a tu muñeca» → actualizarla cuando se decida.
7. Decidir Baleares (apartado 4) antes de configurar los envíos.
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
