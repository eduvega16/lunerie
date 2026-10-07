# Lunerie · tienda online de regalos para ella

> **Cómo usar este fichero:** cópialo a la carpeta nueva de la tienda (p.ej. `D:\lunerie\`) con el nombre `CLAUDE.md`.
> Claude Code lo lee solo al abrir esa carpeta. Actualízalo al final de cada sesión (apartado "Estado" y "Pendientes").
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

---

## 3. Identidad de marca
- **Nombre:** Lunerie ("lu-ne-rí": luna + *-erie* de *joaillerie*). Comprobado el 7-oct: ninguna joyería con ese nombre;
  lunerie.com aparcado; **lunerie.es sin web** (confirmar al comprar; alternativa lunerie.co, como Calné).
  Pendiente: reservar **@lunerie** en Instagram y TikTok · buscar en la OEPM (consultas2.oepm.es/LocalizadorWeb).
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
- **Sin precios tachados inventados** (el tachado debe ser un precio real de los últimos 30 días). El ahorro se
  cuenta con packs ("2.º por X €").
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
- **Modelo:** BS Bee Sister **FA1835** (marca del fabricante, no es réplica; no venderlo como marca propia).
- **PVP 44,95 €** · upsell "2.º reloj por 19,95 €" · variantes: Dorado·piedra verde, Dorado·piedra azul,
  Plateado·piedra verde (esta solo si la muestra llega bien).
- **Cómo es:** cuarzo, esfera ovalada 12 mm, correa de eslabones 18 cm con piedras ovaladas (resina/vidrio),
  aleación dorada o plateada, pila puesta. Incluye caja de regalo + extractor de eslabones + tarjeta.
- **Avisos obligatorios:** no sumergible · esfera pequeña · correa 18 cm (muñecas < 16 cm: quitar eslabones) ·
  no es reloj de lujo.
- **Objeciones (reseñas):** me quedará grande · se estropea con agua · el cierre · ¿parece barato? · ¿llega para Navidad?
- **Proveedores:** muestra/test AliExpress "Face-Book Store" 5,59 € + 4,73 € envío
  (https://es.aliexpress.com/item/1005008660299253.html) · stock Alibaba BS FA1835 ~7,21 € desde 1 ud
  (Guangzhou Shiyi / Shihe / Taihe) o Shenzhen South America Watch 7,66 €.
- **Cuentas (tarjeta, con aranceles):** CPA breakeven **~17,9 €** (AliExpress) / ~16,1 € (stock Alibaba).
  Test: CPA ≤ 14 € escalar · 14-20 € iterar creativos · > 20 € o ~40 € sin ventas → matar.
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
- Claude está conectado a Shopify (conector de claude.ai) con la tienda Lunerie. Antes estaba Star Brick: al cambiar de tienda se desconecta la otra.
- [ ] Cobros: Shopify Payments + PayPal (pide datos de autónomo/empresa)
- [ ] Envíos: zona España, gratis
- [~] Tema y marca (apartado 3): copia **"Lunerie · marca"** del tema Horizon (id 208665149779, SIN publicar) con
      colores, Cormorant + Jost ligera, botones verdes rectos en mayúsculas, logo de texto espaciado y centrado, barra
      verde «Envío gratis a península · Devolución en 14 días» (sin prometer el ajuste de muñeca) y pie en español con
      fondo niebla. Falta: que Edu la revise y la **publique** (Claude no puede publicar temas ni tocar el publicado),
      el menú principal y el favicon. Ficheros fuente: `tema/` (`build.py` genera los 3 JSON que se suben a la copia del tema).
- [ ] Políticas (devoluciones, envíos, privacidad, términos) + aviso legal + páginas Contacto / Preguntas frecuentes /
      Envíos — **Claude las redacta** con huecos para nombre, NIF y dirección
- [ ] Banner de cookies (Configuración → Privacidad del cliente)
- [ ] Apps: Facebook & Instagram (píxel Meta), TikTok
- [ ] Importar el reloj (CSV) → revisar "⚠️ Revisar" de `landing.md` → fotos propias → publicar
- [ ] Quitar la contraseña de la tienda

## 7. Test de 100 € (por producto)
Meta Ads, ABO: 3 conjuntos (1 ángulo cada uno) × 10 €/día × 3 días. Cada día, en el radar:
`uv run python cli.py test <id> --dia N --gasto … --imp … --clicks … --atc … --compras …`
KILL si gastas 1× CPA BE sin carritos o 2× sin ventas · ESCALAR con ≥ 3 ventas a ≤ 70 % del CPA BE ·
alertas si CTR < 1 % o CPC > 0,90 €. Máximo 2 productos en test a la vez.

## 8. Pendientes (a 7-oct-2026, fin de la sesión 1 en esta carpeta)
1. **Edu:** revisar el tema en `https://lunerie.es/?preview_theme_id=208665149779` y publicarlo
   (Tienda online → Temas → «Lunerie · marca» → ⋯ → Publicar). Si algo se ve raro (sobre todo el logo), captura a Claude.
2. Siguiente con Claude: **políticas y páginas legales**, creadas directamente en Shopify (solo existe la página Contacto).
   Después: crear el reloj Lune como borrador a partir de `landing.md` del radar.
3. Escribir a Alibaba (reloj): precio DDP exprés para 20 y 50 uds (mensaje en la sesión 07-oct del radar).
4. Escribir a Yiwu Shangjie (collar) y pedir muestra "Lune"; pasar el enlace de la tienda de 63 €.
5. Decidir lo del "ajustado a tu muñeca" (5.1). La tienda ya **no** lo promete en la barra; la página de marca
   (artifact) aún dice «Te lo enviamos ajustado a tu muñeca» → actualizarla cuando se decida.
6. Cuando lleguen las muestras: fotos y vídeos propios → anuncios → test del reloj.

## 9. Enlaces
- Página de marca: https://claude.ai/artifact/MDZWWTrx5E6xxfgC8gfv2A
- Repositorio (privado): https://github.com/eduvega16/lunerie — remoto con `eduvega16@` en la URL porque el PC
  tiene guardada otra cuenta de GitHub (`kocoessence`). `git pull` al empezar, `git push` al terminar.
- Calné (referencia): https://calne.co/products/uthai-womens-watch-ladies-bracelet-luxury-brand-waterproof-retro-natural-dongling-stone-hotan-jade-advanced-chain-watches-gift
- Reloj AliExpress: https://es.aliexpress.com/item/1005008660299253.html
- Reloj Alibaba: https://www.alibaba.com/product-detail/BS-Bee-Sister-1835-FA1835-Latest_1601607745947.html
- Biblioteca de anuncios de Meta: https://www.facebook.com/ads/library/
- OEPM (marcas): https://consultas2.oepm.es/LocalizadorWeb/
