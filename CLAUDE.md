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
  **Baleares: sí, 3,95 € de envío** (decidido el 12-oct; importe fijado el 15-oct), ya explicado en la página
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
- **PVP 39,95 € desde el 30-oct (Edu, tras el test sin ventas: igual que Calné), **tachado 44,95 €** (el precio más bajo de los 30 días anteriores; 49,95 € no se puede tachar porque solo duró 3 días) y SIN rasca** (sección `rasca` del pie con `"disabled": True`; el código LUNERIE10 sigue existiendo en Descuentos). Antes: **PVP 49,95 € desde el 27-oct** (antes 44,95 €; subido un 10 % para compensar el rasca del 10 %: con el código,
  44,96 €) · **sin upsell** (el «2.º reloj por 19,95 €» se quitó el 27-oct: daba sensación de barato) ·
  variantes: solo Dorado·piedra verde (ver 5.1a).
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

### 5.1a Estado real del Reloj Lune (22-oct) — manda sobre lo de arriba
- **Muestras llegadas el 15-16 oct (pedidas el 7): 8-9 días, todas en bolsita, sin caja ni extractor.** NAIDU y BS
  son **el mismo reloj** (misma correa de piedras ovaladas seguidas y misma caja); solo cambia la marca de la esfera.
  Calidad y peso iguales. **Se vende el NAIDU** (5,27 € en AliExpress frente a ~14 € el BS).
- **Plan A (decidido por Edu el 22-oct): test en drop.** Edu hace los pedidos **a mano en AliExpress** (sin mapear
  DSers por ahora). Si funciona, stock propio (5.1b).
- **Ficha unificada (22-oct):** un solo producto `reloj-lune`, opción **Color = piedra**, siempre dorado:
  **Verde** (LUNE-VERDE, de Face-Book Store «Dark green», coste real 13,95 €) · **Azul, Rosa, Verde claro, Crema,
  Rojo** (LUNE-AZUL/ROSA/VCLARO/CREMA/ROJO, de la tienda de 9 colores del producto DSers «New Colored Gemstones…»,
  coste ~9,61 €). El **plateado** (BS) se probó el 23-oct y se quitó ese mismo día: cuesta encontrarlo en AliExpress. Fotos del proveedor (diseño de piedras seguidas) con su variante + muñeca + medida 18 cm; **fuera
  las fotos de Calné y el plateado**. **Ojo:** en los anuncios del proveedor se mezcla otro diseño (piedras con
  anillas y monedas: «Dark Green»/«Green»/«Yellow» de la tienda de 9 colores) que **no** se vende; la foto del
  anuncio de Face-Book «Dark green» es de ese diseño pero llegó el bueno.
- Los 2 productos importados por DSers entraron **activos y a precio de coste** → pasados a **borrador** (no
  borrarlos). Al importar con DSers: revisar siempre estado y precio.
- **Fase drop en la tienda:** sin prometer caja ni extractor (`CAJA_REGALO = False` en `build.py`; con stock y caja
  → `True`), plazo **7-12 días laborables**, Navidad **antes del 5 de diciembre**, entrega del pago 4-9 días de
  tránsito, que con la preparación que suma Shopify sale como 7-12 laborables (pidiendo el 27-oct: «5 nov-12 nov»,
  comprobado en el pago). Bolitas = color de la piedra con aro dorado (`PIEDRAS` en
  `build.py`).
- **Imágenes con IA (siguiente paso):** script `marca/higgsfield.py` (Marketing Studio 2.5 Flare = GPT Image 2.5,
  referencias: foto del proveedor + foto real de Edu; tomas «producto» en fondo niebla y «modelo» en muñeca). **25-oct:
  la cuenta de la API no tiene créditos** (`not_enough_credits`); la cuenta web (conector de claude.ai) tiene 19,3
  créditos, plan gratis. **Fotos IA (25-oct, `marca/fotos-ia/`):** con el conector de claude.ai y **Nano Banana 2.1**
  (2 créditos/imagen 2K; GPT Image 2.5 pide plan de pago; el gratis solo deja 1 imagen a la vez):
  `lune-verde-modelo-cara.jpg` (estilo Olivia: chica delgada, top blanco, mano al cuello, cara cortada por la nariz)
  y `lune-verde-muneca.jpg`. Referencias: foto del proveedor (Face-Book, verde sobre lino) + foto real de Edu.
  **Fallos de la IA:** cuenta mal las piedras (el reloj tiene **3 y 3**; descartadas 2 fotos de producto con 2+2 y
  3+2) y escribe una marca inventada en la esfera → se borra con OpenCV (inpaint solo de píxeles oscuros y grises,
  sin tocar las agujas doradas). Edu quiere que **se vea «NAIDU»** en la esfera: se consigue editando la foto con
  Nano Banana (foto + recorte de la esfera real como referencias, «spell N-A-I-D-U») y borrando con OpenCV la palabra
  inventada de abajo. Hecho en `lune-verde-modelo-cara.jpg`. Higgsfield por API (`higgsfield-client`, clave `HF_KEY` en `.env.local`,
  fuera de git; **Edu pegó la clave en el chat el 22-oct → regenerarla**). Estética: como **Olivia Jewelry** (limpia,
  producto mejorado + puesta en modelo). Revisar que la IA no cambie piedras/esfera y dejar siempre una foto real.

- **Decisión de Edu (26-oct): el test va SOLO con el verde (dorado).** Quitadas de la ficha las variantes azul,
  rosa, verde claro, crema y rojo (sus fotos siguen en Archivos de Shopify; se recrean si hace falta). Galería
  (26-oct): modelo IA → **producto en niebla** → muñeca IA → **detalle** → **curva** → foto del proveedor → muñeca
  del proveedor → correa 18 cm; la de la modelo es la de la variante. Fotos de producto (`lune-verde-producto/
  detalle/curva.jpg`): la de niebla sale **editando la foto real del proveedor** (cambiar solo el fondo; así no
  cambia el número de piedras) y las otras usan esa como referencia. **Cómo es el real:** 3 piedras a cada lado,
  en las puntas anillas trenzadas vacías (gancho + anilla arriba, anilla + cierre abajo), caja **ovalada** (la IA
  la hace redonda) y pequeña (esfera 12 mm). **Color que se vende (Edu, 26-oct): verde medio-oscuro con vetas
  claras, las 6 iguales** (la foto del proveedor trae una crema: no; ni jade pálido ni malaquita a rayas). Todas
  las fotos de la ficha y del collage corregidas a ese verde el 26-oct (ediciones de 2 créditos con la foto de
  producto como referencia de color). Edu prefiere la esfera **sin marca** en los
  anuncios, pero en el **detalle** de producto sí quiere «NAIDU» y «QUARTZ» (escritos a mano con Jost siguiendo
  el giro de la esfera: `marca/esfera_texto.py` → `lune-verde-detalle.jpg`).
- **Sección «historia» bajo la ficha (26-oct, en producción), como Olivia Jewelry:** foto grande del detalle (2:1 en
  PC, 4:5 en móvil) · franja niebla con 3 datos e iconos dorados (esfera de 12 mm · correa de 18 cm ajustable ·
  garantía de 3 años; **nada de waterproof/hipoalergénico/2 años** como Olivia) · «Pequeño, ovalado *y con
  piedras.*» + texto · collage 2×2 (perfil, curva, toalla, pelo). Código: `tema/codigo/snippets/lunerie-ficha.liquid`
  (`parte('historia', snippet='lunerie-ficha')` en `build.py`); solo sale en `reloj-lune`. Las fotos son **archivos
  de Shopify** con nombre fijo (`lune-editorial-*.jpg`, se leen con `images['…']`); para cambiar una, subir otra
  con el mismo nombre, o mejor `fileUpdate` con `originalSource` (cambia la imagen y conserva nombre y posición).
  Las del collage son las de los anuncios **editadas con el reloj ~35 % más pequeño** (`marca/fotos-ia/editorial/`),
  porque en los vídeos el reloj sale demasiado grande (los vídeos siguen así).
  El CSS de bolitas (`PIEDRAS` en `build.py`) sigue con los 6 colores: no molesta.
  Fotos IA del azul hechas el 25-oct (`marca/fotos-ia/lune-azul-*.jpg`), aparcadas. `marca/naidu.py` escribe
  «NAIDU» en la esfera cuando la IA inventa letras (inpaint + Jost, con giro).
  **Plateado:** Edu encontró en Alibaba un proveedor con el mismo diseño en dorado y plata (verdes). Aparcado: solo
  entra si envía pedidos sueltos a España a buen precio (mensaje en inglés preparado: dropshipping, precio 20/50 uds
  DDP, marca en la esfera, caja, logo propio y mínimo). Para stock propio, buen candidato. Ángulo de anuncio
  «¿dorado o plata?» solo cuando el plateado se pueda comprar.
- **Anuncios con IA (26-oct, `marca/fotos-ia/anuncios/`):** estética de un anuncio de Vacier en TikTok (plano desde
  abajo, puño agarrando una toalla de lino blanca, manga de punto crema, hormigón claro y cielo azul). Fotos
  `lune-verde-toalla-a/b.jpg` (Nano Banana 2.1, 9:16) animadas con **Kling 3.0** (10 créditos / 5 s; Seedance 2.5
  cuesta 35). Higgsfield propone la plantilla «IN THE DARK»: descartarla (`declined_preset_id`).
  **Anuncio 1 (26-oct): `lune-verde-anuncio-1.mp4`**, 13,4 s, 1080x1920, sin audio (música en TikTok/Meta), copia el
  ritmo de un anuncio de Vacier (`ssstik.io_…mp4`): toalla → perfil con mano en la clavícula → macro del reloj →
  mano en el pelo → cielo **al revés** con «LUNERIE» pequeño. Planos en `anuncios/planos/` (foto fija Nano Banana +
  Kling 3.0 **pro, 4 s, `sound: off` = 7 créditos**). Montaje con **`marca/montaje.py`** (cortes secos, giro 180° y
  logo blanco con fundido; `python marca/montaje.py salida.mp4 clip,inicio,duración[,180] … --logo-y 0.72`).
  Ojo: al final de los clips Kling a veces deforma la esfera → usar los primeros 2,5 s.

### 5.1b Plan de stock propio (15-oct) y reloj alternativo «NAIDU»
- **Decisión de Edu (15-oct): pasar a stock propio** (el drop en Navidad no funciona: ~2 semanas de entrega). Orden:
  **validar primero** (test de 90 € con las muestras y AliExpress enviando) → si pasa (~2-8 nov), pedir stock exprés
  DDP → Black Friday y Navidad con entrega 24-72 h, packaging Lunerie y correa ajustada por Edu.
- **Alta de autónomo / Hacienda:** Edu no está dado de alta y **ha decidido no hacerlo hasta que empiece a vender**
  (15-oct). Decisión tomada: no volver a plantearlo. Como particular, el IVA de importación no se recupera (y en
  Alibaba no se pone NIF en «exención de impuestos»).
- **Reloj alternativo:** Foshan Daiyue Watch (Alibaba, 7 años, 4,7/5 con 981 valoraciones, n.º 2 en su categoría):
  https://www.alibaba.com/product-detail/New-Vintage-Women-s-Watch-with_1601581449616.html · esfera **«NAIDU»**
  (el reloj del vídeo de la portada) · correa con piedras ovaladas alternadas con anillas y monedas grabadas · colores
  rosa, verde claro, verde oscuro, blanco, amarillo · **2,75 $/ud (30-50), 2,65 $ (100)** · muestras 7 $/ud + exprés
  17,92 $ por 2 (9-19 días). **Muestras pagadas el 15-oct** (verde claro + verde oscuro, 32,77 € con IVA incluido; entrega más rápida
  27-oct) para comparar con el BS. Las respuestas del chat del proveedor eran del asistente automático de Alibaba.
  Pendiente que confirme: envío DDP del lote y plazo. **Logo propio (respuesta del 16-oct): 500 uds por modelo**;
  con su logo NAIDU, 2-5 uds por modelo. **Decisión de Edu: empezar con NAIDU** y no preguntar más por el logo
  (ni grabado en la tapa) hasta que el test funcione. La marca se nota en la caja, la tarjeta y el nombre «Lune».
  No es el modelo que vende Calné (demanda no probada, mismo estilo).
- **Caja (packaging):** caja tipo cajón 9,5 × 9,5 × 3,5 cm interior con esponja negra con ranura. Edu prefiere la
  **blanca con letras negras** (estilo «VOGUE», pero con LUNERIE en Cormorant en vertical; 1 tinta #16201B; opcional
  destello en oro). Misma caja en Nihao (NH11567891, hasta 1,09 €, mínimo 20, «Nihao Prime» con impuestos incluidos)
  y en Alibaba de fábrica (Yiwu Chunshen, VK-PON-C03, 0,07-0,77 €, mínimo 50, muestra 1,70 €). Pedir a los dos:
  blanca lisa sin texto + impresión propia, pedido mínimo, cliché y DDP. **Diseño elegido (15-oct): «PARA TI» + destello dorado.** `marca/caja.py` → `marca/caja/`: `tapa.pdf`
  (completo, 100 × 100 mm, letras en trazos), `capa-tinta.pdf` (negro), `capa-oro.pdf` (cliché del oro) y
  `maqueta.png`. Fuente Jost añadida a `marca/fuentes/`. Nihao pidió el diseño para presupuestar.
- **Importar:** pedir siempre «DDP to Spain (all taxes and duties included)» y pagar dentro de Alibaba (Trade
  Assurance). < 150 €: Alibaba suele cobrar el IVA en el carrito; > 150 €: DDP del proveedor o pagar IVA + arancel +
  comisión del mensajero al recibir.

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
- **Muestra recibida (25-oct):** pedida el 9-oct, llegó el 23-oct → **14 días (10 laborables)**. La foto del
  proveedor antes de enviar: letra «firma» y lágrima azul muy bien, caja de terciopelo verde; sobra la tarjeta
  «THANK YOU» con huellas → pedir tarjeta neutra.
- **Plazos Navidad:** "hecho a mano en 3-5 días · entrega 10-15 días laborables"; fecha límite ~**1 de diciembre**
  (Black Friday 27-nov entra); en diciembre opción "envío exprés +9,95 €"; para rezagados, tarjeta regalo imprimible.

### 5.3 Otros candidatos (del radar, por si hay hueco)
Collar de familia / árbol de la vida con nombres (Bervi lo vende 1 año; Amazon 42-57 €; AliExpress 1-7 €) ·
gafas con cámara IA (69,95-79,95 €) · descartados: micro-infusión, paddle surf, pulsera tipo WHOOP, bolso hobo (réplica).

### 5.4 Joyas de AliExpress (28-oct) — normalizadas y **PUBLICADAS el 28-oct** (solo Tienda online)
Edu las empujó con DSers (12, entraron **activas, a precio de coste y con tachado = coste** → todas a borrador).
Elegidas 4 (Edu, precios medios); las otras 8 se quedan en borrador sin tocar (anillos arcoíris y pavé, set de 4
pendientes «para una oreja», collar de piedras «naturales», collar/pulsera de estrellas, el 2.º anillo del mes,
aros con perla y collar de perlas «plata 925»). Plantilla `joya`, vendor Lunerie, sin tachado, SKU sin tocar.
- **Anillo Nuit** `anillo-nuit` (11036461891923) · sello con circonita marquesa · Color: Verde oliva / Champán /
  Blanco / Morado × Talla 12 / 14-15 / 17 · coste 3,34-4,71 € · **19,95 € desde el 5-nov** (antes 29,95 €; Edu: «demasiado
  caro»; pidió ~12 €, pero con envío y ~4 € de aranceles por paquete pierde 3-5 € por anillo, y eligió 19,95 €, como
  el Duo; sin tachado). Solo, deja ~1-4 €: no anunciarlo suelto, sirve para sumar al pedido.
- **Pendientes Larme** `pendientes-larme` (11036461629779) · aro con lágrima · 7 colores · coste 1,88 € · **24,95 €**.
  La ficha de AliExpress no dice «Choice»: mirar el plazo a España.
- **Collar Lune** `collar-lune` (11036462121299) · cadena con piedras ovaladas, «a juego con el reloj» · De colores /
  Blanco · 45 + 6 cm · coste 4,93 € · **34,95 €**.
- **Anillo Étoile** `anillo-etoile` (11036462154067) · piedra del mes · Mes (12) × Talla · coste 3,82-4,36 € · **19,95 €
  desde el 5-nov** (antes 29,95 €, igual que el Nuit). Siguen diciendo 29,95 € el carrusel de Navidad de la campaña
  (foto 1, Nuit) y el **anuncio 10** «Notas del móvil» (tarjeta final, Nuit): cambiarlos cuando se toque la campaña
  (después del 9-nov). El vídeo ya está rehecho a 19,95 € (5-nov: solo se refrescaron los precios de
  `marca/anuncios-hf/assets/datos.js` y se volvió a grabar `notas.html`) y es el que lleva el reel del 5-nov; la URL
  nueva está en `anuncios/creatividades-urls.json`. Textos de Instagram ya cambiados.
- Tallas US 6/7/8 = contorno 52 / 54,5 / 57 mm → «12», «14-15», «17» (explicado en la descripción).
- Textos: «acero inoxidable con acabado dorado», «circonita»; **nada** de «oro 18K», hipoalergénico, waterproof,
  «no se oscurece» ni nombres de gemas (los colores del mes van como «rojo oscuro», «azul agua»…).
- Fotos actuales: las del proveedor sin logos ni textos en inglés (OpenCV) y las de producto en
  niebla 4:5 (blanco × color niebla). Se sustituyen en su sitio con `fileUpdate` + `originalSource` para no perder
  la foto de cada variante. Script: scratchpad de la sesión (`normalizar.py`).
  **Orden de la galería (Edu, 28-oct, como Olivia): 1.ª el producto suelto en niebla, 2.ª puesto en persona.**
  **Fotos IA puestas en persona (28-oct, `marca/fotos-ia/joyas/`)**, ya subidas como 2.ª foto de cada ficha (sin
  variante asignada): Nuit (verde oliva en la mano), Larme (pendiente verde en la oreja) y Collar Lune (cuello).
  Étoile aún sin foto IA. Ojo con el collar: la 1.ª versión (Nano Banana) colgaba las piedras como dijes y se
  descartó; el real las lleva **engastadas en la cadena, en línea**. La v2 (API, `marketing-studio/image/flare`,
  prompt insistiendo en «integrated into the chain… never hanging») salió bien.
- Ya montado: colección automática **«Joyas»** (`joyas`, tipo Relojes/Anillos/Pendientes/Collares, publicada; el Reloj Lune entró el 28-oct
  a petición de Edu, en último lugar, así que la fila de 4 del inicio sigue enseñando solo las joyas) · plantilla
  `product.joya.json` (sin correa ni «¿se puede mojar?») · bolitas de los colores nuevos (`PIEDRAS`) · sección
  «Las joyas» del inicio en `build.py` **oculta** (`"disabled": True`: con la colección vacía Horizon pinta productos
  de relleno).
- **Al publicar:** quitar `"disabled"` de `joyas` en `build.py` y subir `templates/index.json` · ACTIVE + publicar
  solo en **Tienda online** (no en Facebook & Instagram hasta acabar el test: el catálogo podría colarse en los
  anuncios) · «Joyas» en los menús `main-menu` y `pie-tienda` · `curl -sI` de cada ficha = 200 · pedir una muestra
  de cada una.

---

## 6. Montaje de la tienda — estado
- [x] Crear la tienda en Shopify (7-oct)
- [x] Datos: nombre LUNERIE, España, EUR, impuestos incluidos en los precios (comprobado el 7-oct por API)
- [x] Dominio **lunerie.es** conectado (visto el 7-oct; cuenta de Shopify con luneriecompany@gmail.com, plan Basic, EUR).
  **Correo de cara al cliente: hola@lunerie.es** (14-oct; en todos los textos legales y páginas, y como correo de
  la tienda en Shopify, visto el 15-oct)
- [~] Redes: **Instagram @luneriejewelry** (antes @lunerie_co; usuario cambiado por Edu el 27-oct, mismo id;
      nombre del perfil **«Lunerie | Relojes y joyas»**, que es lo que mira el buscador de Instagram). Cuenta que
      Edu ya tenía (~700 seguidores no orientados), profesional, avatar `oficial-avatar-redes.png`, enlace
      lunerie.es. Bio propuesta (estilo Olivia, sin emojis ni «waterproof»): «Relojes y joyas para regalar. /
      Envío gratis a península · 3 años de garantía · Devolución en 14 días». 27-oct: 6 publicaciones de IA
      subidas (textos propuestos en la sesión: 3 hashtags por post, «reloj de mujer»/«reloj dorado» en el texto);
      los 3 posts viejos enseñan relojes que no se venden (plateado, piedras claras) → archivarlos si Edu quiere.
      Enlace de Instagram en el pie: `INSTAGRAM` en `build.py`. Falta: TikTok.
      **Meta (15-oct, comprobado con el conector):** porfolio empresarial **Lunerie** (1639315480899561), separado
      de LaFortuna · cuenta publicitaria **«LUNERIE PUBLI» 4565584937093443** (EUR, activa, **con método de pago**,
      dentro del porfolio) → **es la que se usa** · página «L U N E R I E» **1376893392171782** (página **nueva** creada por Edu el
      15-oct; la antigua 1311701355367588, en lafortuna.club, sobra → borrarla o archivarla) · Instagram **luneriejewelry**
      (17841404549468255) enlazado a la cuenta publicitaria. La cuenta suelta 1551796336759107 (sin pago ni
      porfolio) sobra. Claude lo ve con el conector **«Meta ads Koco»** de claude.ai (nombre antiguo) · «pipeboard»
      solo ve LaFortuna: no usarlo para Lunerie.
- [x] Cobros activados por Edu (12-oct). Confirmar que PayPal también está.
- [x] **Envíos (15-oct, probado en el pago real):** península **gratis** · Baleares **3,95 €** · Canarias, Ceuta y
      Melilla **sin envío** («El envío no está disponible»). **La tienda usa el sistema nuevo de Shopify, «envíos por
      mercado»**: las tarifas viven en los **mercados**, no en los perfiles de envío (cambiar `deliveryProfile` no
      afecta al pago; ahí quedaron unas zonas «Península»/«Baleares» de prueba que no se usan). Mercados: **España**
      (opción «Envío gratis» 0 €; tenía «Estándar» 6,99 € gratis desde 55 €) · **Baleares** (provincia PM, «Envío a
      Baleares» 3,95 €) · **Canarias, Ceuta y Melilla** (GC, TF, CE, ML, envíos desactivados). API: `marketUpdate` /
      `marketCreate` con `--version unstable` (las provincias en `regionsCondition` solo existen ahí; al crear,
      `delivery.shipping.optionDefinitions`) y **cada tarifa tiene que llevar la ubicación de la tienda**
      (`conditions.originLocationsToAdd: gid://shopify/Location/127723929939`) o no sale en el pago. Permisos de la
      CLI ampliados el 15-oct con `read_markets,write_markets,read_locations,read_delivery_customizations`.
      **Plazo en el pago (27-oct):** `transitTime` 345600-777600 s (4-9 días) en España y Baleares; Shopify le suma
      ~3 días laborables de preparación y el pago muestra fechas a 7-12 días laborables, como la ficha. Se cambia con
      `marketUpdate` → `optionDefinitionsToUpdate.flatRate.rateGroupsToUpdate` (grupos 684876366163 España y
      690779095379 Baleares; repetir nombre, precio y `isActive`). Comprobar envíos en el pago: script de Playwright con dirección y sin pagar (Madrid 28001 / Palma 07001 / Las
      Palmas 35001).
- [x] Tema publicado: **«Copia actualizada de Lunerie · marca» (id 209073799507)** = Horizon 1.0.5, actualizado por
  Edu el 12-oct. Shopify crea una **copia nueva con otro id** en cada actualización de Horizon: después de actualizar,
  cambiar el id en este fichero y volver a bajar `tema/tienda/`. En la del 12-oct se conservaron los 5 ficheros de
  `tema/codigo/` y todos los ajustes; esos 5 se quedan en su versión vieja (Shopify no actualiza ficheros
  modificados), así que no reciben los arreglos de Horizon. La anterior «Lunerie · marca» (208665149779) queda sin
  publicar como copia de seguridad.
- **Cómo se cambia el tema publicado: con Shopify CLI** (v4.9; tienda `qjxvnn-xq.myshopify.com`). El conector de
  Shopify de claude.ai **no** puede escribir en el tema publicado ni publicar (solo en temas sin publicar); la CLI sí.
  - **Login hecho en los dos PCs** (`C:\Users\edu\lunerie` el 8-oct, `D:\LUNERIE` el 9-oct y otra vez el **2-nov**: la
    CLI se había quedado solo con la sesión de Star Brick y daba «you don't have access to this dev store»). **Login sin
    ventana (2-nov):** `python -u tema/login_cli.py 2>&1 | tee .claude/shopify-login.log` en segundo plano (consola
    invisible con `pywinpty`, ya instalado en `D:\LUNERIE`): elige «Log in with a different account», el navegador se
    abre solo con el código y Edu entra con **luneriecompany@gmail.com**. La sesión de Star Brick sigue guardada
    (`shopify auth login --alias starbrickstore@gmail.com` para volver). Lo mismo con `git push` si GitHub pide login:
    lanzarlo con `GIT_TERMINAL_PROMPT=1` y `GCM_INTERACTIVE=always` y se abre la ventana de GitHub.
  - **Sin la CLI de temas (2-nov):** `python tema/subir_api.py <id del tema> <ficheros…>` sube ficheros de `tema/tienda/`
    por la Admin API (`themeFilesUpsert`, va con `shopify store execute`); funcionó también en el tema publicado.
    Antes de subir al publicado, comparar sus ficheros con la versión de git (se leen con `theme(id){files(filenames:…)}`)
    para no pisar cambios hechos en el editor.
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
      **27-oct:** privacidad sin tabla (en móvil descuadraba la página: un bloque por uso de los datos) y «Quién
      trata tus datos» al final. `legal/subir.py` ahora sube solo lo que se le diga (`python legal/subir.py
      privacidad.md`) y, sin las variables LUNERIE_*, coge nombre/NIF/dirección de la política publicada.
      **Nada de tablas en los textos legales** (no caben en el móvil).
- [x] Banner de cookies de Shopify activado por Edu (14-oct; carga `privacy-banner/storefront-banner.js`). Falta que
      Edu lo mire en incógnito (Aceptar y Rechazar a la vez, texto en español).
- [x] **App Facebook & Instagram instalada por Edu (15-oct)**: píxel **«Lunerie's pixel» 1096538246614496** (porfolio
      Lunerie, uso «publicidad y analítica», cookie propia activa) puesto en la tienda por la app (apiClientId 2329312,
      compartir datos «optimized» + todos los eventos). Solo se activa **con consentimiento** (privacyPurposes
      ANALYTICS/MARKETING → espera al «Aceptar» del banner). Píxel **asignado a «LUNERIE PUBLI»** (15-oct) · compartir
      datos «Máximo» · catálogo de Shopify sincronizado con Meta (2654127555016345). **Probado el 15-oct** con Chrome automático
      (Playwright, `ctx.request.post` a /password para entrar): antes de «Aceptar» no sale nada hacia Meta; después
      salen PageView, ViewContent, AddToCart, InitiateCheckout (y SubscribedButtonClick) con el id del píxel, y Meta
      marca `last_fired_time`. Banner en español con Aceptar / Rechazar / Administrar preferencias. **Pedido de prueba**
      (modo de prueba de Shopify Payments, tarjeta 4242…, pedidos #LUN1001-1003 marcados como prueba): sale
      AddPaymentInfo y **Purchase** con valor y moneda. Pendiente: eventos de servidor (API de conversiones) con la
      primera venta real. Modo de prueba **apagado** por Edu (15-oct).
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
      fina con titular, botón y «Segundo reloj por 19,95 €» dentro. **27-oct: vídeo nuevo del Lune verde**
      (`marca/portada.py` con los clips de Kling → `marca/portada/`): en móvil, vertical con fundidos (8 s); en PC,
      tres planos en fila de ida y vuelta (5,2 s); los dos en bucle sin salto. Se elige con `<source media>`; mientras
      carga se ve su primer fotograma (archivos `lune-portada-movil.jpg` / `lune-portada-pc.jpg`). Si se rehacen,
      subir los vídeos como archivo de Shopify (VIDEO, staged upload POST) y cambiar las 2 URL en `hero-video` de
      `lunerie-inicio.liquid`. Volver a la portada con foto: `parte("hero", arriba=8, abajo=40)` en `build.py`.
      Menú principal (14-oct): «Reloj Lune» (ficha `/products/reloj-lune`) · Preguntas frecuentes · Contacto.
- [x] **Rasca del 10 % (27-oct, en producción)**, como el de Olivia Jewelry: ventana «Rasca y descubre · Tenemos
      un regalo para tu primer pedido» con lámina dorada (canvas) y, en PC, 4 fotos editoriales a la derecha. Sale
      **una vez** en el inicio y en las fichas, a los **25 s** de estar en la web (cambiado el 28-oct; antes 8 s o al bajar media página; el tiempo cuenta entre
      páginas de la visita y no sale al bajar), y **espera a que se conteste el
      banner de cookies** (`#shopify-pc__banner`; es `fixed`, así que se mira con `getClientRects`, no con
      `offsetParent`). Al rascar ~45 % (o «¿Prefieres no rascar? Descúbrelo aquí») mete el código en la cesta con
      `cart/update.js` + `discount` (igual que Horizon), aunque esté vacía: al añadir el reloj, 49,95 → 44,96 €.
      Cerrado sin rascar, vuelve a los 7 días (`localStorage` «lu-rasca»). Código **LUNERIE10** (Descuentos →
      «Rasca · 10 %», DiscountCodeNode 1859009708371): 10 % a todo, un uso por cliente, no se suma a otros
      descuentos de producto ni de pedido. Código: `tema/codigo/snippets/lunerie-rasca.liquid`,
      pintado desde la sección `rasca` del pie (`footer-group.json` en `build.py`). **Es un regalo igual para todos,
      no un sorteo: nada de «prueba suerte»** (engañoso si a todos les toca lo mismo). CPA breakeven a 49,95 €:
      ~22 € sin código y ~17,9 € con el código (lo mismo que antes a 44,95 €); para el test, contar con ~17,9 €.
      **Cambios del 27-oct (noche):** a **pantalla completa** (PC: texto a la izquierda y 4 fotos a la derecha;
      móvil: 2 fotos arriba), lámina con **purpurina que brilla** (canvas animado) y **brochazos** detrás de «RASCA
      AQUÍ», y el código **solo entra en la cesta cuando la clienta pulsa «Añadir el descuento a mi cesta»**.
- [x] **Opiniones (27-oct, en producción)** bajo la ficha, como Olivia: arriba a la izquierda «Añadir opinión»,
      a la derecha la media; tarjetas en niebla con la foto a la derecha; estrellas y número bajo el título (solo si
      hay opiniones). **Las publicadas son metaobjetos «Opinión»** (Contenido → Metaobjetos → Opinión → Añadir
      entrada: nombre, estrellas, texto, foto, fecha, origen «Compra verificada» / «Recibido como regalo», producto;
      solo salen las «Activas»). El botón abre un **formulario de contacto de Shopify que llega a hola@lunerie.es**
      (nombre, email, estrellas, opinión y permiso para publicar; la foto la mandan por email). Código:
      `tema/codigo/snippets/lunerie-opiniones.liquid` (sección `opiniones` y bloque `estrellas` en `build.py`).
      Permisos de metaobjetos dados a la CLI el 27-oct (si `shopify store auth` dice «Port 13387 is already in use»,
      matar el `node` que lo ocupa). `shopify theme dev` da «you don't have access to this dev store»: para ver algo
      sin tocar la tienda, `shopify theme push --unpublished` y el enlace `?preview_theme_id=`.
      **28-oct: 4 opiniones de amigas publicadas** (origen «Recibido como regalo», producto `reloj-lune`, fecha
      28-oct, media 4,8): **María R.** 5 · **Lucía S.** 5 · **Carla R.** 4 (la de los eslabones) · **Silvia F.** 5.
      Las fotos (de WhatsApp, 720×960, sin EXIF) son archivos de Shopify `lune-opinion-1/2/3/5.jpg`. Edu dio los
      nombres y las estrellas, dijo que daba igual quién llevara cada texto y pidió retocarlos: el contenido sale de
      lo que contaron (chulo, parece una joya, eslabones en 5 min con el vídeo, invierno con la ropa); el reparto y
      la redacción son de Claude, así que cada amiga tenía que dar el OK a su texto (**dado el 1-nov**). Se subieron con la CLI
      (`stagedUploadsCreate` → `fileCreate` → `metaobjectCreate` con `capabilities.publishable.status: ACTIVE`);
      para cambiar un texto, `metaobjectUpdate`. La foto n.º 5 enseña la marca «BS Bee Sister» en la esfera y la
      del detalle de la ficha pone «NAIDU» (Edu aún no ha decidido nada). Para añadir más: Contenido →
      Metaobjetos → Opinión, o la CLI.
- [x] **Pie nuevo (27-oct, en producción), como el de Olivia Jewelry:** 4 columnas (Sobre Lunerie · La tienda ·
      Información · Cartas de Lunerie con suscripción y «Puedes darte de baja cuando quieras. Privacidad») + medios
      de pago (los activos en Shopify, salen solos) + línea con © y redes (Instagram luneriejewelry y la página de
      Facebook; **TikTok: añadir `tiktok_url` en `build.py` cuando exista**). Menús de la tienda **«pie-tienda»**
      (Reloj Lune, Preguntas frecuentes, Contacto) y **«pie-informacion»** (Envíos, Devoluciones, Privacidad,
      Términos, Aviso legal, **Preferencias de cookies** → `/#preferencias-cookies`, que reabre el panel del banner
      con `window.privacyBanner.showPreferences()`, sección `cookies` del pie). En móvil, los menús son
      desplegables. El texto del campo de email («Tu email») es un cambio en `locales/es.json` que hace `build.py`
      (si se vuelve a bajar el tema, se vuelve a aplicar al ejecutarlo). El menú «footer» (Buscar) ya no se usa.
- [x] **Vídeo en el collage (27-oct, en producción):** la foto de la toalla del collage de la historia es ahora
      un vídeo en bucle recortado a 4:5 (`marca/videos-ficha/lune-collage-toalla.mp4`, toalla-a, que no repite la
      foto). La fila «De cerca» de abajo se **ocultó** el mismo día tras una crítica de diseño: era más estrecha que
      todo lo de alrededor, metía el azul del cielo justo antes de la foto de detalle y repetía la escena de la
      toalla del collage. Volver a enseñarla (quitar `"disabled"` en `build.py`) cuando haya **vídeos reales**.
- [x] **«De cerca» + envío gratis junto al precio (27-oct, en producción):** bajo la ficha, fila de 3 vídeos
      verticales (toalla-a, macro, toalla-b; `marca/videos-ficha/`, subidos a Archivos de Shopify) que se reproducen
      solos al verse (con «reducir movimiento», con controles). `parte('videos')` en `lunerie-ficha.liquid`; para
      añadir uno (los reales de Edu: muñeca, quitar un eslabón), subir mp4 + primer fotograma .jpg y añadir su URL a
      la lista. Título honesto «De cerca», no «As seen on you» (no son de clientas). Solo clips donde el reloj se ve
      de su tamaño (en perfil/pelo de Kling sale grande; el macro, solo los primeros 2,5 s en ida y vuelta porque al
      final deforma la esfera). Etiqueta «Envío gratis a península» al lado del precio (grupo `precio` en `build.py`).
      **Rasca arreglado en móvil:** las fotos de arriba se salían de su franja y tapaban el texto.
- [x] **«Segundo reloj por 19,95 €» quitado (27-oct):** `SEGUNDO_RELOJ = False` en `build.py` (fuera la franja verde
      del inicio, la caja verde de la ficha y el aviso de la cesta; bajo el botón de la portada ahora pone «Envío
      gratis a península») · descuento automático **desactivado** (no borrado) · quitado de Preguntas frecuentes y
      del ejemplo de los Términos. Volver: `True` + reactivarlo en Descuentos.
- [x] Contraseña de la tienda **quitada** (visto el 27-oct por la noche).
- [x] **Google Search Console verificado (9-nov)**: propiedad «Prefijo de la URL» `https://lunerie.es` con la etiqueta
      `google-site-verification` en `snippets/meta-tags.liquid` (junto a la de Meta; no quitarla). El DNS de lunerie.es
      está en **Piensa Solutions** (no en Shopify; solo entra Edu): si algún día se quiere la propiedad de dominio, TXT
      nuevo sin tocar el SPF de buzondecorreo (correo de hola@). Shopify no sirve archivos HTML en la raíz. Sitemap:
      `sitemap.xml`.

> **OJO (22-oct): el conector de Shopify de claude.ai está conectado a STAR BRICK (otra tienda de Edu), no a Lunerie.**
> Solo puede estar en una tienda a la vez. **Para Lunerie, usar SIEMPRE la CLI** (`shopify store execute -s
> qjxvnn-xq.myshopify.com`), que sí apunta a Lunerie. Comprobar con `get-shop-info` antes de usar el conector.
> **Si el conector no carga** (pasó el 12-oct): usar la Admin API con la CLI, que no depende de él:
> `shopify store execute -s qjxvnn-xq.myshopify.com -q "<query>" --json --no-input` (añadir `--allow-mutations` para
> escribir; `--query-file` / `--variable-file` para operaciones largas). Permisos dados por Edu el 12-oct con
> `shopify store auth` (productos, inventario, páginas, políticas, menús, archivos, temas, publicaciones, envíos,
> pedidos en lectura, descuentos); en `D:\LUNERIE` dados el 14-oct. **Sin ventana:** lanzar en segundo plano
> `shopify store auth --store qjxvnn-xq.myshopify.com --scopes <lista> 2>&1 | tee .claude/store-auth.log`: abre el
> navegador solo y Edu acepta (probado el 14-oct). El conector de claude.ai sigue sin `write_legal_policies`.

## 7. Test de ~90 € (por producto)
Meta Ads **Advantage+ de ventas** (cambiado el 27-oct, como recomienda Meta ahora): **1 campaña con presupuesto de
campaña 30 €/día × 3 días = 90 €, 1 solo conjunto con público abierto** (solo país, exclusiones de envío y 18+,
sin intereses ni edades sugeridas; ubicaciones automáticas) y **varios anuncios distintos dentro** (ángulos y
formatos diferentes: la creatividad hace de segmentación). Meta reparte el gasto hacia el anuncio que vende; no
apagar anuncios las primeras 48 h. El antiguo ABO de 3 conjuntos × 10 € ya no se usa. Cada día, en el radar:
`uv run python cli.py test <id> --dia N --gasto … --imp … --clicks … --atc … --compras …`
KILL (se mira en la campaña) si gastas 1× CPA BE sin carritos o 2× sin ventas · ESCALAR con ≥ 3 ventas a ≤ 70 %
del CPA BE (subir el presupuesto de la campaña un 20 % cada 2-3 días) · alertas si CTR < 1 % o CPC > 0,90 €.
«Aprendizaje limitado» es normal con este presupuesto (Meta pide ~50 compras/semana). Máximo 2 productos en test.

## 8. Calendario y pendientes (a 8-nov-2026)

### Para empezar la próxima sesión (después del 2-nov) — abrir conversación nueva por sesión.
**6-nov: PRIMERA VENTA REAL**, pedido **#LUN1004**: Collar Signé dorado, mes de diciembre (lágrima azul), 49,95 €, pagado
con Shopify Payments. Viene de Meta, **anuncio 18** (`utm_content` collar-carmen, el vídeo de Carmen con música). Edu hace
él mismo el pedido al proveedor, **QIUHAN**, que el 6-nov lo confirmó todo: 13,22 $ por pedido con envío **con impuestos
incluidos (DDP/IOSS)**, cajita beige de 1 $, tildes, cadena de 40 + 5 cm, foto antes de enviar y lo rehacen si se
equivocan. Diseño: **una anilla a cada lado del nombre, a media altura** (no arriba de la mayúscula como «Marta»).
Alibaba cobra además el IVA en el pago: **#LUN1004 costó 14,85 € pagado con PayPal → CPA breakeven del collar
≈ 20,8 €**. Detalle y tabla de colores en `productos/proveedor-qiuhan.md`.
En su tabla, nuestro «Diciembre · azul» es **«December · Zircon»** (el azul claro). Campaña a las ~10:45: 67,88 € de los 140 € del tope, y sale a ~68 € por venta (breakeven ~20-23 €). **No tocar
hasta el 9-nov**; entonces, consejo: pausar el 16 y dejar que el 18 se lleve el gasto.
**Pendiente (6-nov, noche):** (1) QIUHAN prepara la lista de #LUN1004; cuando mande la **foto del collar antes de
enviarlo**, revisar la «I», la lágrima azul claro y las anillas a los lados antes de que Edu dé el OK. (2) **Meta:
hablado el 6-nov, no se toca nada hasta el 9-nov** (el diagnóstico del asistente de Meta no cambia el plan). (3) Ficha
del Collar Signé: la foto de **Marta azul (posición 4) y la de Paula (plateado)** cuelgan la lágrima del nombre, que no es
así (ver abajo); **Edu no ha dicho si se cambian** por Laura/Alba/Sara → no tocarla sin su OK. (4) QIUHAN tiene que
contestar al mensaje «NEW QUESTION … about new products» (6-nov, solo en el chat): catálogo de personalizados para
dropshipping —pulsera con nombre (misma letra), inicial, pulsera de piedra del mes, anillo con nombre, collar de familia
con 2-4 nombres— con precio en 316L, días de fabricación y de envío a España con impuestos incluidos (DDP/IOSS), fotos
reales, qué se personaliza, cajita y descuento por volumen. (5) Sin respuesta de Edu: si las anillas del nombre van a
media altura a los lados (lo que dijo QIUHAN) o arriba de la mayúscula (como las fotos de IA).
**6-nov (noche): ENFOQUE EN PERSONALIZABLES y REDES AL 80 % COLLAR SIGNÉ (Edu).**
- **Decisión de Edu:** Lunerie se centra en **productos personalizables como Olivia** (collar con nombre, piedra del mes…);
  relojes y demás joyas pasan a **complementos**. Motivo: la primera venta fue el Signé (anuncio 18) y los relojes llevan
  semanas sin vender. Antes de ampliar el catálogo, ver la foto y la calidad del primer pedido de QIUHAN.
- **Regla de redes (Edu): el 80 % de lo que se sube a Instagram es el Collar Signé**; el otro 20 % (uno de cada cinco),
  relojes y demás joyas. Las piezas que no son del Signé se quedan **«aprobado» sin `fecha_sugerida`** (así
  `publicar_programado.py programar` no las coge): «Lo sentimos, mamá» (W45-15), Nuit (W45-03), Collar Lune (W45-05),
  Larme (W45-07), Sépia (W47-01) y «Cinco relojes» (W46-04). **Este calendario manda sobre la lista del 3-nov.**
  Programadas en este PC (todas a las 19:30 salvo el carrusel): 7-nov **Laura azul** (W45-21) · 8-nov 12:30 **carrusel
  «Una lágrima para cada mes»** (W45-17: lámina + Carmen + mano al sol, «¿En qué mes naciste?») · 9-nov **reel de la
  cámara** (W46-13, OK de Edu) · 10-nov «Un martes cualquiera» (W46-10) · 11-nov **foto regalo «dedos-1»** (W45-19) ·
  12-nov **Alba rojo** (W46-11) · 13-nov «Regalos por precio» (W46-01) · 15-nov **Sara verde** (W46-12) · 18-nov **Marta
  rojo** (W47-02). Huecos para el Signé: 17-nov («Comenta tu mes», reel con HyperFrames, gratis) y 20-nov (el **primer
  pedido real** con la foto de QIUHAN, sin el nombre de la clienta o con su permiso).
- **Cómo es el collar de verdad (Edu, 6-nov, con fotos):** la lágrima va **ensartada en la cadena principal, en el punto
  más bajo (forma de U)**, 2-3 eslabones después del final del nombre; **nunca colgando de la anilla del nombre ni de una
  cadenita debajo (forma de Y)**, y **sin cola de más** después de la última letra (un solo trazo recto que acaba en la
  anilla). Revisar cada foto del collar a tamaño real antes de programarla. Las de la ficha Marta azul y Paula lo tienen mal.
- **Fotos nuevas del Signé, estilo estudio de Olivia** (`marca/collar_ia.py`, ~0,13 $ cada una; fondo blanco, nombre en
  diagonal, lágrima grande): tomas `estudio-rojo/azul` → `estudio-rojo/azul-v2` (arreglan la forma de Y con
  `ARREGLO_CADENA`) → `nombre-laura-azul`, `nombre-alba-rojo`, `nombre-sara-verde` (`CAMBIO_NOMBRE` sobre la roja
  corregida) y `dedos` (colgando de los dedos al sol, formato de Pinterest). Los posts llevan su versión con texto:
  `marca/fotos-ia/collar/post-*.jpg`. Descartadas: `estudio-azul-v2` (la «t» tenía una raya de más) e **«Irene»** (la I
  de firma sale como una V, «Vrene», igual que la C de «Varmen»).
- **Fotos y vídeos reales de la muestra «Marta»** (Edu, 6-nov): `marca/referencias-reales/muestra-marta/` (fotos 1-12;
  los `.mov` del iPhone, 44 MB, solo en este PC, fuera de git). `collar_ia.py` usa `foto-10` y `foto-06` (`MUESTRA`) y
  `foto-08` para la cadena.
- **Reel con la muestra real descartado** (`marca/reel_muestra.py`, Edu: «demasiado casero», pelusas sobre fondo negro y
  no le gustó «Antes de venderlo, pedimos uno»). Prefiere IA con estética de estudio.
- **Reel de la cámara digital** (idea de Edu, reel de @mybirdyboutique): `python marca/reel_camara.py camara --n 2`
  (cámara compacta plateada por detrás, IA) → `… montar <camara.png>`: en la pantalla pasan Laura, Alba, Sara, dedos,
  Marta rojo y dedos-2 con un destello y acaba en la tarjeta «Collar Signé con su nombre y su piedra». 7,6 s, sin sonido
  (la API no pone música). `marca/fotos-ia/reel-camara/reel-camara-9x16.mp4`, subido a Archivos de Shopify (URL en W46-13).
- **Pinterest (6-nov, sin iniciar sesión):** ideas en `oficina/ideas/2026-11-06-pinterest.md` y capturas en
  `oficina/referencias/pinterest-2026-11-06/`.
- **Reel de Carmen (W45-20) recuperado:** a las 19:30 Instagram dio ERROR un momento y el script se rindió; minutos
  después el contenedor estaba FINISHED y se publicó a mano (https://www.instagram.com/reel/DfaQYrFtDXN/). Arreglado
  `esperar()` en `oficina/publicar.py`: un ERROR ya no corta, sigue mirando hasta agotar los intentos. Si vuelve a
  pasar: `media_publish creation_id=<contenedor>` (vale 24 h). El post de Galet (W45-12) salió solo a las 19:30.
**7-nov (Meta, OK de Edu):** tope de la campaña de Black Friday subido a **200 €** (llega al 9-nov; el 6-nov a la noche
iban 91,75 €, 1 venta, 16 carritos). Anuncios nuevos **19 «Carmen palma»** y **20 «Carmen Black Friday»** (variantes del 18,
detalle en `anuncios/campana-black-friday.md`); el 14 y el 16 siguen hasta el 9-nov. La variante A (gancho «¿Y si este año
le regalas su nombre?») espera la respuesta de QIUHAN sobre la calidad (mensaje del 7-nov: 316L en todas las piezas, PVD o
baño normal y micras, si se oscurece, agua/sudor/perfume, sin níquel, control de cada collar). **Solo si lo confirman por
escrito** se puede poner «no se oscurece» o «puedes ducharte con él» en ficha y anuncios. Retargeting aparte: aparcado
(poca gente; Advantage+ ya lo hace); el 9-nov, crear los públicos y mirar su tamaño.
**Botones (7-nov, Edu):** el 19 y el 20 llevan **«Más información»**; el 18, el 14 y el 16 siguen con «Comprar» y no se tocan
hasta el 9-nov (cambiar el botón = creatividad nueva: vuelve a revisión, pierde lo aprendido y los me gusta). Mismo vídeo
en el 18 y el 19/20 → **el 9-nov, comparar carritos y compras por botón** y, si gana «Más información», ponérselo a los que
sigan. **Para el 9-nov:** (1) leer la campaña con el conector (el asistente del Administrador no cuenta el día en curso);
(2) 14 y 16 con nuestra regla (CPA BE ~21 €: 16 fuera si pasa de ~21 € sin carritos; 14 fuera si pasa de ~42 € sin
ventas), no con la de Meta (50 compras / 70 €); (3) botones; (4) públicos de retargeting (gratis) y su tamaño; (5) decidir
presupuesto a partir del tope de 200 €; (6) enseñar a Edu los 2 vídeos de familia (madre e hija, dos hijas) y, con su OK, meterlos en el conjunto. Pendiente de QIUHAN: la letra de «Isa» (Susan buscaba la de la muestra «Marta»),
la foto del collar antes de enviarlo y la respuesta de calidad.
**9-nov (Meta, OK de Edu):** a media mañana, 169,29 € gastados, 54 carritos (Meta), 2 pedidos reales (Shopify) →
~85 €/pedido; 0 ventas desde el 7-nov. El 18: 108,87 €, 43 carritos, 2 compras; el 14: 39,35 € sin ventas; el 16: 16,98 €
(1 carrito); el 19 y el 20 sin entrega (Meta no los enseña) → **no hay comparación de botones**. **Hecho:** anuncios **14 y
16 en PAUSA** (comprobado) y **tope de la campaña a 270 €** (Edu pidió 250 €, pero Meta no deja bajar de 269,30 € mientras
haya cargos pendientes; publicado solo el cambio de la campaña con `object_ids`, comprobado). **El 11-nov hay que PARARLA a
mano al llegar a ~220 €** (lo pactado: +50 € para medir la cesta nueva con el 18) y decidir si sigue. **Regla para el 11-nov:** CPA
≤ ~30 € (con packs) → seguir a 35 €/día y escalar poco a poco; ≥ ~50 € → parar y revisar ficha y oferta antes de gastar más.
**Vídeos de familia SUBIDOS (9-nov, OK de Edu):** anuncios **21 «UGC madre e hija»** (52567501902994) y **22 «UGC dos hijas»**
(52567501912794) en el mismo conjunto, botón «Comprar», 4:5 + 9:16, textos con el precio del pack (74,93 € / 99,90 €);
detalle en `anuncios/campana-black-friday.md`. Para subir vídeos a Meta: `anuncios/subir_creatividades.py <ficheros>` →
URL exacta de `creatividades-urls.json` (no inventarse el final: falla con «Unable to fetch») → `ads_creative_upload_media`
→ `ads_create_creative` con `placement_customizations` (4:5 de reserva + 9:16 en story/reels) → `ads_create_ad` (queda en
borrador) → `ads_activate_entity` con `object_ids` de los anuncios nuevos (no publica las recomendaciones a medias). Shopify 9-nov (hasta media mañana): 19 sesiones, 6 con carrito, 2 al
pago (antes ~1 de cada 5), aún pocos datos. Las 2 recomendaciones de Meta a medias (anuncios 14 y 3) siguen sin publicar.
**9-nov, anuncios MOFU/BOFU PREPARADOS (Edu: «dale caña»), SIN SUBIR:** 23 estático de cierre, 24 carrusel de dudas y 25 grabación de pantalla de la vista previa del nombre (`marca/grabar_vista_previa.py` → `marca/mofu_bofu.py`, sin IA; textos en `anuncios/campana-black-friday.md`). **Entran el 11-nov con la revisión, si Edu da el OK.** ffmpeg en este PC: `imageio_ffmpeg.get_ffmpeg_exe()` (pip `imageio-ffmpeg`; no está en el PATH).
**9-nov, cesta (EN PRODUCCIÓN, OK de Edu, probado en lunerie.es), tras un análisis de otro Claude que trajo Edu:**
(1) **Las 12 variantes doradas del Collar Signé comparten la foto de la lágrima verde** (y las plateadas otra), así que en la
cesta un collar de diciembre salía con piedra verde → ahora la cesta y el cajón enseñan **la gota del mes elegido**
(`snippets/lunerie-cesta-gota.liquid`, lee `lagrima-NN.png`; si falta, la foto normal), pintada desde
**`snippets/cart-products.liquid` (otro fichero de Horizon modificado, copia en `tema/codigo/`)**. (2) Los avisos del bloque
verde empiezan por «Black Friday · …». (3) **Fuera el campo «Descuento» de la cesta** (CSS `.cart-discount` en
`lunerie-cesta-confianza.liquid`): la promo se aplica sola; los códigos se meten en el pago. **Descartado de ese análisis**
(reglas de Edu): «Elaboración y envío: 7-12 días» (suma de plazos), «se graba a mano» (no es verdad: chapa de QIUHAN),
«antes del 5-dic para Navidad» (quitado el 5-nov; si vuelve, fecha más temprana y confirmada con QIUHAN), cambiar la fecha
del pago, Bizum (más adelante) y reenfocar el anuncio a Navidad.
**9-nov: Edu DESACTIVÓ las fechas de entrega estimadas del pago** (estaban en automático: en el método de envío salía
«llega el día X», que no es verdad porque Shopify no cuenta los días de fabricación). **No volver a activarlas.** Aun así
el pago seguía poniendo «Envío gratis · 4 a 9 días hábiles» (el tiempo de transporte de las tarifas) → **quitado el mismo
día** de las dos tarifas (España y Baleares) con `marketUpdate` (`--version unstable`): `rateGroupsToUpdate` con el mismo
precio y `transitTimeMinSeconds`/`transitTimeMaxSeconds` a `null` (comprobado al leerlo de nuevo: precio, activas y
Canarias/Ceuta/Melilla sin envío, igual que antes). Los plazos quedan solo como texto («sale en 3-5 días laborables» en
ficha y cesta; los dos plazos por separado en Envíos y FAQ). Pendiente: en el resumen del pago el collar sigue saliendo
con la foto de la variante (lágrima verde en todos los meses dorados); el pago no se puede cambiar desde el tema.
**8-nov:**
- **Meta a las ~19:30:** 144,19 € de 200 €, ~218 clics a 0,66 €, 35 carritos, 6 pagos empezados. Shopify: 2 pedidos
  válidos (#LUN1004 y #LUN1006, 149,85 €, 4 collares; #LUN1005 reembolsado) → **~72 € por pedido** (breakeven ~21 €),
  ~-90 € en margen. El 18 lleva 84,32 € (30 carritos, 2 compras; hoy ~38 € sin vender), el 14 38,91 € sin ventas, el 16
  16,91 € (1 carrito); el 19 y el 20 casi sin gastar (0,73 / 0,06 €) → **el 9-nov no habrá datos para comparar botones**.
  El tope se acaba el 9-nov por la tarde. En el Administrador hay 2 recomendaciones de Meta a medias (no publicadas) en
  los anuncios 14 y 3 (música aleatoria, carrusel a vídeo): consejo, no publicarlas; y el borrador viejo «NO PUBLICAR».
- **EL ATASCO ES LA CESTA (ShopifyQL, 5-8 nov):** móvil 113 sesiones → 29 con carrito → **6 al pago** → 2 compras (PC: 29
  sesiones, 0 carritos). **Cesta nueva EN PRODUCCIÓN (OK de Edu, probada en lunerie.es):** (1) el texto del envío salía
  «Aranceles e impuestos incluidos. Los gastos de envío se calculan en la página de pago» porque la tienda usa las claves
  `duties_and_taxes_included_*` y el arreglo del 5-nov solo cambiaba `taxes_included_*`; ahora `build.py` pone las 8
  claves con regex → «Impuestos incluidos. Envío gratis a península (Baleares, 3,95 €).» (2) Bloque de la promo **en
  verde**, sin «Ver relojes / Ver joyas» (sacaban de la cesta): con 1 pieza, carrusel de tarjetas en horizontal
  (`CESTA_EXTRA`: aros Boucle, anillo Duo, pendientes Larme, y collar Lune si una ya está en la cesta) con el precio real
  con la promo (19,95 → 9,98 €: la mitad de la más barata, en céntimos hacia abajo) y botón «Añadir» (fetch → /cart).
  Probado: collar + aros = 59,93 €, igual que Shopify. **En la página de la cesta va arriba** (en PC, columna izquierda);
  **en el cajón, debajo de las piezas** (Edu: arriba no le gustó). En el cajón, `.cart-drawer__items{flex-shrink:0}` para
  que el carrusel no aplaste la pieza. (3) Bajo «Pagar»: «Se hace para ti y sale en 3-5 días laborables» (solo con el
  collar) + «Garantía de 3 años · Pago seguro» (`lunerie-cesta-confianza.liquid`, generado por `build.py`). Ficheros:
  `lunerie-segundo-reloj.liquid` (generado), `cart-drawer.liquid`, `sections/main-cart.liquid` y **`snippets/cart-summary.liquid`
  (nuevo modificado de Horizon, copia en `tema/codigo/`)**. Ojo: `tema/tienda/` de este PC estaba desfasado (el
  `es.json` del 5-nov se subió desde el otro PC): antes de subir, bajar el fichero en vivo y comparar.
  Siguiente: ver en unos días si sube el paso carrito → pago (ShopifyQL `sessions_that_reached_checkout`). El email de
  carrito abandonado de Shopify (Marketing → Automatizaciones) **está activo** (Edu, 8-nov).
- **Instagram:** el carrusel «Una lágrima para cada mes» (W45-17) salió solo a las 12:31. Las tareas programadas ahora
  despiertan el PC de la suspensión (ver «Redes (3-nov)»): **dejar el PC suspendido, no apagado**. Siguiente: 9-nov 19:30,
  reel de la cámara (W46-13).
- **Ocultar los Me gusta no se puede por API** (ni al publicar ni después; solo `comment_enabled`): lo hace Edu en la app,
  publicación por publicación (··· → Ocultar recuento de Me gusta). Edu borró sin querer una publicación que había subido
  él desde la app (todas las de la cola siguen): se restaura en Tu actividad → Eliminado recientemente (30 días).
- **Bio propuesta con la promo** (144 caracteres): «Collares con nombre y relojes pequeños para regalar. / Black Friday:
  2.ª pieza al 50 % y la 3.ª, gratis. Hasta el 5-dic. / Envío gratis a península.» (sin «Devolución en 14 días»: los
  collares con nombre no se devuelven). Al acabar la promo (5-dic), quitar la línea de Black Friday.
- **Facebook (Edu: «sube las publicaciones a Facebook también»), A MEDIAS:** el token de la página no tiene
  `pages_manage_posts`. Edu lo activó en la app «Lunerie Claude Publisher» (caso de uso «Administra las páginas» →
  `pages_manage_posts` «Listo para prueba»). **Falta:** generar en el Explorador un **token de usuario** con los 6 permisos
  (los 5 de antes + `pages_manage_posts`), pegarlo en `.env.local` como `IG_TOKEN_USUARIO=` y ejecutar
  `python oficina/renovar_token.py`; comprobar con `debug_token` que el token de página lleva `pages_manage_posts`.
  Después: que `publicar.py` publique también en la página (`/{page-id}/photos`, carrusel como varias fotos,
  reels con `/video_reels`), programando en el servidor de Facebook con `scheduled_publish_time` (no depende del PC), y
  repartir en Facebook las del Collar Signé ya publicadas en Instagram (no todas el mismo día). Un token con permisos de
  más (anuncios, WhatsApp…) que mandó Edu no se guardó. Edu pegó 2 tokens de usuario en el chat (caducan en 1-2 h).
  Alternativa sin permisos: compartir automático en Instagram (Centro de cuentas → Compartir entre perfiles); sin
  comprobar si copia lo publicado por API.

**7-nov (tarde-noche):**
- **Pedidos nuevos:** **#LUN1005** (Collar Signé dorado, junio, 49,95 €, PayPal) → a las 15:31 la clienta **pidió cancelarlo**
  desde la tienda; Edu no lo había encargado a QIUHAN → aceptar y devolver entero (texto del email propuesto en la sesión:
  ofrecer cambiar nombre/piedra antes de cancelar; si no contesta en 24 h, cancelar). **#LUN1006**: **3 Collares Signé**
  (2 dorados de marzo + 1 plateado de junio) por 99,90 € con el 3x2 → pedírselos a QIUHAN. Meta solo cuenta 2 compras
  (la 3.ª, seguramente sin cookies).
- **Meta a las ~21 h:** 105,56 € de 200 €, 154 clics a 0,69 €, 21 carritos, 2 compras (Meta). **El 18 vende: 46,40 €, 2
  compras (23,20 €/compra, casi el breakeven ~21 €)**; el 14 lleva 38,31 € sin ventas (límite ~42 €) y el 16, 16,86 € sin
  carritos (límite ~21 €): el 9-nov, seguramente fuera los dos. El 20 aún sin gastar.
- **Instagram:** la tarea de Laura azul (W45-21) de las 19:30 no corrió (PC apagado) → publicada a mano a las 20:28.
- **Vídeos UGC de familia (Edu: «para ti y para tu hija», «para tus dos hijas», usar más las promos)**, sin subir a Meta:
  `marca/ugc_familia.py` (fotos 9:16 con varias personas; las hijas, adultas) → `ugc_animar.py --carpeta ugc-<v>` →
  `ugc_montaje.py --carpeta ugc-<v> --tarjeta dos|tres`. **«Uno para ti… y otro para tu hija»** (Elena + Sara, salón con
  árbol, 16 s, tarjeta «2 collares · 74,93 € · El 2.º, a mitad de precio») y **«¿Tienes dos hijas?»** (Ana + Marta +
  Laura, cocina, 14 s, «3 collares · 99,90 € · El 3.º, gratis»), voz de Silvia + Holiday Bells, 9:16 y 4:5 en
  `marca/fotos-ia/ugc-madre-hija/` y `ugc-dos-hijas/`. Precio de 2 Signé = 74,93 € (Shopify: la más barata al 50 % en
  céntimos hacia abajo). Coste ~5 $. **Propuesta: meterlos el 9-nov** con la revisión (Edu aún no los ha visto/aprobado).
  Ideas siguientes: abuela-madre-hija, hermanas, mejor amiga, madre y suegra.
- **Vista previa del nombre EN PRODUCCIÓN (Edu, visto en Olivia):** bajo el campo «Nombre» del Collar Signé, caja crema
  (#FAF7F1, recta) con el nombre en letra de firma dorada mientras se escribe (plateada si eligen Plateado) y «Vista previa
  orientativa de la letra». Letra **Hurricane** (OFL, `assets/lunerie-firma.woff2`, alojada en el tema; `build.py` ya copia
  los .woff2). Olivia usa Sacramento (redonda, no se parece a la nuestra); Herr Von Muellerhoff se probó y Edu dijo «es
  demasiado» (además su «I» parece un 9): queda en `assets/lunerie-firma-herr.woff2`, se cambia con `firma` en
  `lunerie-collar.liquid`. **Ojo:** en un bloque `{% liquid %}` no valen comentarios al final de la línea. Cuando QIUHAN
  mande su letra real, valorar si cambiarla. **8-nov (Edu: «la gente hace clic en el visualizador en vez del input»), en producción:** la caja crema ES el campo `properties[Nombre]` (se escribe en ella en letra de firma, «Escribe su nombre» de marcador, clic en cualquier punto de la caja = escribir, mayúscula inicial en el móvil) y debajo, en letra normal, «Se hará así: **Carmen**» para revisar I/J y mayúsculas. Probado en lunerie.es: la cesta recibe «Nombre: Carmen».

**6-nov (en producción, OK de Edu):**
- **Plazos del collar (Edu): 3-5 días laborables de fabricación y 3-5 de envío** («5-7 y 3-10 es demasiado tiempo»;
  QIUHAN dijo 5-7 y 3-10: si se retrasan, ojo). En la ficha, como Olivia, **solo lo que tarda en salir**: bajo el botón
  «Se hace para ti y sale en 3-5 días laborables · Envío gratis a península · Garantía de 3 años» y lo mismo en «Envío y
  devoluciones» (`HECHO_COLLAR` en `build.py`); nada del tránsito. Los dos plazos, por separado, en Envíos (política y
  página) y Preguntas frecuentes.
- **Foto 1 del Collar Signé = «Carmen» con lágrima verde** (Edu: «el verde es el color que más se ve en las fotos de
  producto»). Es la de Marta editada (`python marca/collar_ia.py producto-verde --n 3 --4k`; elegida por Edu la
  `producto-verde-3`) y cambiada en su sitio con `cambiar_fotos.py`, así que sigue siendo la foto de las 12 variantes
  doradas y la que sale en la sección del collar del inicio. **Marta (azul) sigue en la galería, en la posición 4**.
- **Panel «Elige la piedra» con fotos reales de las gotas, como Olivia:** `python marca/lagrimas.py --recortes --subir`
  recorta las 12 gotas de la tabla de Olivia (la misma de la lámina; Edu asume el riesgo) con fondo transparente y las sube
  como `lagrima-01.png` … `lagrima-12.png` a Archivos de Shopify. `lunerie-collar.liquid` las lee con
  `images['lagrima-NN.png']` (en el panel y en el botón con la piedra elegida) y, si falta una, pinta la gota dibujada.
  Ojo: en un `<svg>`, `.hidden` no existe: se oculta con `toggleAttribute('hidden')`. Cambiarlas cuando el proveedor
  mande su tabla.
**3-nov (en producción, pedido por Edu):** barra de arriba en **rojo #CA3801** (el de Olivia en su Black Friday;
`PROMO_ROJO` en `build.py`, solo con `PROMO`) · **«Packs para regalar» justo después de la portada** · escaparates y
reseñas del inicio **llenan el ancho en PC** (antes, en la pantalla de Edu quedaba un hueco a la derecha): `--n` =
tarjetas a la vez (relojes 3/4/5 a 750/1100/1500 px; joyas y reseñas 2/3/4 a 750/1100/1700) y, si hay menos, se
centran. **«Lujo como PDPaola» (3-nov, en producción, OK de Edu a todo; regla: solo grita la barra roja, la promo
se mantiene pero en pequeño):** fichas (las 4 plantillas) con columnas desiguales → **fotos de dos en dos en 2/3 y
texto en 1/3** (desde 1200 px; `equal_columns: False`, 4 px entre fotos, sin la primera grande), sin migas, la foto
justo bajo la cabecera; en el móvil, contador «1/7» en vez de miniaturas · promo en **una línea bajo el precio**
(`OFERTA_FICHA`: «BLACK FRIDAY» en el rojo de la barra + texto; fuera la caja verde) · ventajas en **texto pequeño
gris bajo el botón** (`VENTAJAS`; fuera la bolita roja que latía y los iconos) · fuera la etiqueta «Envío gratis» del
precio, el **botón amarillo de PayPal** (`.accelerated-checkout-block` oculto por CSS; PayPal sigue en el pago) y el
icono del carrito · «Te puede interesar» se queda. Inicio: bajo el collage, sin la franja en tinta ni «BLACK FRIDAY»
gigante (ceja roja pequeña + «Relojes y joyas *para regalar.*» + promo en una línea), y sin las etiquetas oscuras
(«LUNE»…) sobre las fotos de los escaparates. Ojo: el CSS personalizado de una sección solo lleva el prefijo de la
sección en la primera regla: si el tema gana, `!important`. El botón se queda en «Agregar al carrito» (Edu, 3-nov).
**Portada «para cada día» (3-nov, en producción, pedida por Edu):** las fotos de Navidad no le convencían (en el
móvil no se veían las joyas). Ahora, de día y **sin caras** (corte bajo la nariz), en el mismo collage: taza de café
con Lune + Nuit + collar Lune (grande en el móvil) · mano en el pelo con Boucle + Maille + Duo (centro en PC) · copa
en una terraza con Sépia + Étoile + Larme. `marca/portada_dia.py` (6 fotos, ~0,80 $; elegidas izquierda-1, centro-2 —en
la 1 el Maille salía redondo— y derecha-2), archivos de Shopify `portada-dia-*.jpg`; en el móvil el collage va al
revés (la grande a la izquierda). Volver a las de Navidad: `foto = 'portada-navidad-'` en `hero-navidad`.
Más tarde (Edu: «más grandes y a todo el ancho»): en PC las tres a todo el ancho (`aspect-ratio: 2.35/1`, 27,5 % +
46 % + 27,5 %) y en el móvil más grandes y con zoom hacia las joyas (`transform: scale` por foto, dentro de
`.lu-hn__recorte` para no tapar el borde de papel). **Revelado** (Edu: «se ven muy IA», «los relojes algo pequeños»): `marca/revelar.py` → `portada-dia/revelado/` (encuadre más cerca de las joyas, sin agrandar el reloj respecto a la muñeca: la esfera mide 12 mm, y acabado de película: más cálido, menos saturado, negros levantados, viñeta y grano). Las 3 de la portada se cambiaron en Shopify con `fileUpdate` (mismo nombre) y el carrusel del martes las usa.
**Enfoque «para llevar cada día»** (Edu: en Instagram y en una campaña futura): ideas del estratega en
`oficina/ideas/2026-11-03-cada-dia.md`. Hecho el carrusel **«Un martes cualquiera»** (`marca/martes.py` →
`marca/fotos-ia/martes/1-7.jpg`): 6 horas del día (café, metro, trabajo, mercado, pausa, copa) con las 11 piezas y la
tarjeta final «Un reloj que solo da la hora» (3 fotos nuevas con `portada_dia.py metro trabajo mercado`, ~0,40 $).
**Redes (3-nov, OK de Edu «dale con las publicaciones»):** plan del community manager hasta el 20-nov en
`oficina/cola` (26 piezas). **10 publicaciones de Instagram aprobadas y PROGRAMADAS** en el Programador de tareas de
Windows de ESTE PC (`D:\LUNERIE`, carpeta «\Lunerie\»), con `oficina/publicar_programado.py` (pythonw, sin ventanas;
registro en `oficina/publicaciones.log`, fuera de git): 4-nov Lune café · 5-nov carrusel Black Friday · 6-nov Galet ·
9 Nuit · **10 «Un martes cualquiera»** · 12 collar · 13 regalos por precio · 15 Larme · 18 Sépia · 20 cinco relojes.
Solo salen si el PC está encendido **o en suspensión** (8-nov: la tarea lo despierta; los temporizadores de activación están habilitados y el PC no se suspende solo) con la sesión abierta; apagado no. Si se enciende después, publica solo si no han pasado más de 3 h (`RETRASO_MAX`); si no, la pieza sigue «aprobado» y se publica a mano
(`python oficina/publicar.py <id> --confirmar`). Ver: `python oficina/publicar_programado.py tareas`; quitar:
`… quitar [id]`. **Al abrir sesión: mirar el log y que las publicadas pasen a «publicado»** (y hacer commit de la cola).
A mano (Edu): stories con pegatinas, reels con música, Facebook (Business Suite) y editar el texto de los 3 posts del
29-oct que dicen «Lune 49,95 €».
**4-nov (hecho, en producción): fotos de Carmen y Elena del Collar Signé rehechas** con fotos REALES de referencia
(carpeta nueva **`marca/referencias-reales/`**: `reloj-lune-1/2` del proveedor, `anillo-nuit-1/2`, `aros-boucle-1/2` y las
de las amigas; `collar_ia.py` las usa por defecto y manda todas las de cada pieza). Lágrima colgando de la cadena 2-3
eslabones después del nombre (como el real) · Lune con bisel trenzado y la caja ocupando ~media muñeca · Nuit fino, que
se estrecha, piedra a lo largo del dedo. `PIEZA` de Lune y Nuit reescritas (en `portada_navidad.py`, la usan también
`portada_dia.py` y `collar_ia.py`) y fuera el «small, do not make bigger» de `portada_dia.py`. La IA sigue pintando las
piedras del Lune **verde oscuro con vetas negras**: se arreglan en local con **`marca/piedras_lune.py`** (OpenCV, gratis;
verde medio con vetas claras, comparar con `reloj-lune-2.jpg`). Elegidas `modelo-hombro-1-piedras` (Carmen) y
`modelo-tirantes-2` (Elena), cambiadas en su sitio con `python productos/collar_signe.py --cambiar <toma> <posición> …`.
Las anteriores quedan como `*-v1.png`. La de Marta estaba bien (no se tocó).
**Corrección de Edu (4-nov): el collar es ASIMÉTRICO** — el nombre va en diagonal en un lado de la cadena (a la izquierda
de la foto) y la lágrima cuelga recta en el centro, en el punto más bajo (como `collar-signe-1.jpg` y la de Marta); nada de
nombre horizontal en el centro con la lágrima a un lado. `DISENO` en `collar_ia.py` ya lo dice. Arreglado **editando**
las dos fotos elegidas (tomas `editar-hombro` / `editar-tirantes`: cambia solo el collar y conserva reloj, anillo y aros)
→ en la ficha `editar-hombro-2` (Carmen, elegida por Edu) y `editar-tirantes-2` (Elena). Coste total del día: 8 fotos, ~1,05 $.
**Fotos reales de la muestra del collar (Edu, 4-nov)** en `marca/referencias-reales/collar-signe-1..5.jpg` («Marta», lágrima
azul, de Yiwu Shangjie) + `caja-collar-1.jpg` (caja de terciopelo verde, por dentro negra); sin EXIF. `collar_ia.py` usa ya la
1 y la 5 (`COLLAR_REAL`) en vez de la foto de Olivia. Cómo es de verdad: el nombre va **recortado de chapa plana pulida**
(no hilo redondo), firma rápida con la mayúscula alta y un trazo largo de entrada; unido a la cadena por arriba y por el final;
lágrima grande de 4 garras colgando de su asa en el punto más bajo. Son también las que hay que mandar a QIUHAN para la letra.
**Carmen y Elena rehechas con la muestra real (4-nov, tarde, en producción):** nombre de chapa plana pulida, unido a la
cadena con una anilla **en la punta de arriba de la mayúscula** y, al final, **un trazo largo y recto que acaba en otra
anilla** (como la barra de la «t» de Marta); de ahí, 2-3 eslabones hasta la lágrima en el centro. Hechas en **4K**
(`collar_ia.py … --4k`, 2480×3312) editando las anteriores. **Coste del 4K (transacciones de Higgsfield, 4-nov):
cobra 0,19 $ y devuelve 0,02 $ → 0,17 $ por foto** (frente a ~0,13 $ en 2K); la que bloquea el filtro se devuelve
entera. La tanda de 5 costó 0,68 $. En Carmen el reloj se volvió a pegar desde la versión
aprobada (la IA lo cambió: bisel de bolitas en vez de trenzado); queda `editar-hombro-2-reloj.png`. Elena:
`editar-tirantes-1.png`. Descartadas: una que ponía «Varmen» (pedir mayúscula «pointed» convierte la C en V: no usarlo)
y otra que ponía «Zlema». Higgsfield bloqueó una por filtro (top palabra de honor; pasa a veces, repetir).
**Calidad en Shopify (Edu: «en mi PC se ven mejor»):** la pérdida es sobre todo la compresión WebP del CDN de Shopify (no
se controla; ~39,7 dB a 1600 px). Lo que sí ayuda: generar en 4K y subir JPEG calidad 97 **sin submuestreo de color**
(`subsampling=0`; ya en `collar_signe.py`). Faltan por pasar a esa calidad: `normalizar_dsers.py`, `campana_bf.py`,
`martes.py`, `revelar.py`, `oficina/publicar.py`, `tema/fotos_prueba.py` (guardan a 90-92).
**Referencias reales de Maille, Galet, Perle y Duo (4-nov, noche):** sacadas de las fotos del proveedor de cada ficha
(las de después de las 2 de IA), solo en dorado: `reloj-maille-1..3`, `reloj-galet-1..2` (sin foto en la muñeca),
`reloj-perle-1..3`, `anillo-duo-1..3` en `marca/referencias-reales/`. Las fotos reales de la muestra del collar **no van
a la ficha** (Edu, 4-nov). **Con ellas se rehicieron en 4K (Edu: «hazlas con IA») las 2 fotos de IA de cada ficha**
(1.ª en niebla, 2.ª puesta), en producción con el OK de Edu: `python marca/fichas_ia.py <tomas> --n 2 --4k` (16 fotos, ~2,70 $; descripción
de cada pieza sacada de las reales + medidas de la ficha + «tamaño real en la muñeca»). Elegidas: Maille niebla-2 y
persona-1 · Galet niebla-2 y persona-1 · Perle niebla-1 y persona-2 · Duo niebla-1 y persona-1. Subidas con el script
nuevo **`python productos/cambiar_fotos.py <handle> <imagen> <posición> …`** (para cualquier producto: recorta a 4:5,
JPEG 97 sin submuestreo, `fileUpdate` en su sitio; la variante «Dorado» de Maille y Galet sigue con su foto). `portada_dia.py` / `portada_navidad.py` aún leen la 1.ª foto de una carpeta: para usarlas,
pasarles estas (o hacer que manden todas, como `collar_ia.py`).

**5-nov: lámina de las 12 lágrimas en la ficha del Collar Signé (Edu), 5.ª foto de la galería.** Sale de la tabla en
inglés «BIRTHSTONE CHART» que bajó Edu (Downloads/LUNERIE/collar personalizable/7.webp, de Olivia, como las otras fotos
del collar): `python marca/lagrimas.py` recorta las 12 gotas y monta una 4:5 en español con la letra de Lunerie
(«Una lágrima para cada mes», mes + nombre del color, **sin nombres de gemas**, nota «Circonita… colores orientativos»)
→ `marca/fotos-ia/lagrimas/lagrimas-12.jpg`. Cambiarla por una propia cuando QIUHAN mande la tabla real de sus colores.
**5-nov, mañana: la campaña ya gastaba** (13,47 €, 17 clics a 0,79 €, 1 carrito); Meta mete casi todo en el carrusel del
**Collar Signé** (11,66 €, 13 clics) → el plazo del collar importa más: pedir a QIUHAN los días reales.
**5-nov: QIUHAN contestó** — acero **316L a 5,22 $** (descuento; luego 5,80 $), seguimiento, dropshipping sin logos
ni factura en el paquete, pedidos **cada día por el chat** (ellos hacen la lista y Edu la confirma). Con envío a 4,33 €
(sin confirmar), **CPA breakeven ≈ 23 €** a 49,95 €. Respuesta en inglés (13 preguntas + pedido de prueba a casa de
Edu) y qué cambiar con lo que conteste: **`productos/proveedor-qiuhan.md`**. Lo crítico: envío con impuestos
incluidos (IOSS), días reales y la letra igual que la muestra.
**5-nov: ficha del collar «como Olivia, sin pillarse los dedos» (Edu: «creamos demasiada fricción»), en producción:**
fuera la línea «Para Navidad, pídelo antes del 15 de noviembre», el plazo «llega en 2-5 semanas» y el aviso de «no
admite devolución» bajo el campo del nombre (y de la descripción). Ventajas: «Envío gratis a península · Garantía de
3 años». Un solo desplegable **«Envío y devoluciones»** con la estructura del de Olivia: se hacen para ti y salen en
**5-7 días laborables** (`HECHO_COLLAR` en `build.py`, los días de QIUHAN) · las piezas sin nombre se devuelven en 14
días; las personalizadas no, «aun así, si algo no está bien, escríbenos y lo arreglamos» · en cursiva, «el nombre se hace
tal cual lo escribes, mayúsculas incluidas». **El equilibrio (Edu): la ficha, corta como Olivia; los plazos, en los
textos legales.** Envíos (política y página) y Preguntas frecuentes: piezas con nombre = **5-7 días laborables de
fabricación y después 3-10 de envío, por separado**; para Navidad, «tardan más: pídelas con tiempo». **REGLA DE EDU:
nunca escribir la suma de los plazos ni una fecha calculada (en la web, los textos legales ni nada): la suma la hace la
clienta.** En Devoluciones, «se hace tal cual lo escribes» (no «se graba»: QIUHAN lo hace en chapa). Ojo: la fecha que
enseña el pago (7-12 días laborables) no cuenta los días de hacerlo (el anuncio 14 ya va sin plazo, ver abajo).
**QIUHAN, 2.ª respuesta (5-nov):** letras sin límite, envío ~7 $ por pedido, bolsita sin logo 0,5 $ o cajita de
terciopelo beige 1 $ → con la cajita, CPA breakeven ≈ 20,6 €. Detalle, preguntas pendientes y la siguiente respuesta en
`productos/proveedor-qiuhan.md`.
**Siguiente con el collar (5-nov, noche):** Edu manda a QIUHAN la 3.ª respuesta en inglés (está en
`productos/proveedor-qiuhan.md`, con las fotos `collar-signe-1/5.jpg`), **sin pedido de prueba** (Edu no quiere pedir
muestra: el primer pedido de una clienta hace de prueba, con foto obligatoria antes de enviarlo), y **a la vez pregunta
lo mismo a Yiwu Shangjie** (la de la muestra que ya conoce; mensaje en el mismo fichero). Si los dos valen, mejor
Shangjie (calidad probada, caja verde). Claude recomienda la **cajita de 1 $** (solo
0,5 $ más que la bolsita; preguntar si la hay en verde oscuro, si no la beige; nada de bolsita turquesa, recuerda a
Tiffany), pero Edu aún no lo ha decidido. No poner «llega en su cajita» en la ficha hasta ver una foto real. **Lo
crítico sigue sin contestar: si el envío de 7 $ va con impuestos incluidos (IOSS/DDP).** Con su respuesta: plazos,
lámina de colores y cuentas (lista en el mismo fichero).
**Desplegable «Descripción» arreglado (5-nov, en producción, Edu: «la descripción no está puesta en ningún producto»):**
salía vacío en todas las fichas desde el 10-oct, porque el bloque `product-description` de Horizon necesita
`"text": "{{ closest.product.description }}"` en sus ajustes (está en `build.py`; subidas las 5 plantillas de producto y
comprobadas las 12 fichas en Chrome). Revisadas las 12 descripciones: solo cambió la del Collar Signé («colgando en el
centro, una lágrima», no «a un lado»; `DESC` en `productos/collar_signe.py`). Ojo: `curl` a lunerie.es puede devolver
«Verifying your connection…» si se hacen muchas peticiones: comprobar con Playwright.
**Collar en el inicio (5-nov, en producción, OK de Edu tras ver la vista previa en el tema de prueba):** sección
`collar` justo debajo de la portada (`parte('collar')` en `lunerie-inicio.liquid`): en PC, Carmen puesta + Marta suelta
(2.ª y 1.ª foto del producto) y el texto en el tercio derecho, más grande desde 1700 px; en el móvil, Carmen y el texto
debajo. «Nuevo · Con su nombre» · «Su nombre, *su piedra.*» · las 12 lágrimas · precio · «Personalizar el collar».
**Edu pide ver la vista previa aquí antes de subir cambios de diseño**: subir antes al tema de prueba 210513527123 y
enseñar capturas (`.claude/preview/`, fuera de git) + el enlace `?preview_theme_id=`.
**Instagram (5-nov):** carrusel de Black Friday (`W45-09`) publicado solo a las 12:31 (sin «creadas con IA» en el pie,
comprobado) y reel «Notas del móvil» (`W45-14`) a las 19:31, con el vídeo nuevo.

**5-nov (tarde): vídeo UGC del Collar Signé, en Instagram y en la campaña (Edu: «la de Sarah me mola, súbela y ponla en
anuncios»).** El vídeo de HyperFrames («Su nombre, su piedra») se descartó: a Edu no le gustó y tenía un salto al final
(GSAP `scale` sobre una imagen centrada con `transform: translate` en CSS: no volver a hacerlo). Nuevo flujo **UGC realista**,
reutilizable para otras piezas:
1. `python marca/ugc_collar.py ancla --n 2`: la cara de la chica, con las fotos reales del collar como referencia.
2. Se elige el ancla y se generan los planos con ella: `… cuello nombre mirada --ancla <png>` (flare 2K, ~0,13 $ cada uno).
   Hay que revisar que no salgan dos lágrimas: pasó en «mano» y se descartó.
3. `python marca/ugc_animar.py <planos>` con **Kling 3.0 pro por la API** (`kling-video/v3.0/pro/image-to-video`,
   `image_url`, `duration` 4, `sound` off, 9:16; el recorte 9:16 se hace antes). La API lista 95 modelos en
   `GET https://api.higgsfield.ai/models` (Kling, Seedance, Wan…), **sin voz**.
4. Voz: `python marca/voz_elevenlabs.py generar <voice_id> <nombre>` (ElevenLabs, plan Free; ver memoria) o edge-tts gratis.
5. `python marca/ugc_montaje.py <nombre>`: clips de 4 s, voz, subtítulos cortos entre la barbilla y el collar y tarjeta
   final con el precio; los subtítulos se cortan al salir la tarjeta.

Coste total ~2,5-3 $. Vídeo elegido: `marca/fotos-ia/ugc-collar/collar-ugc-sarah-9x16.mp4` (+ `-4x5`).
- **Reel publicado** el 5-nov a las 13:51 (`2026-W45-16`).
- **Anuncio 16** `52566612235194` en el mismo conjunto: 4:5 en feed y 9:16 en Stories y Reels, sin plazo ni fecha de
  Navidad y sin declarar IA. Ya son 17 anuncios.
- Las piezas 17-19 del collar (carrusel, stories, foto) siguen en borrador.
- **Segundo vídeo UGC, «Carmen» en luz dorada (Edu: «me flipa»)**, con ideas de Pinterest: colgando de los dedos → en
  la palma → abrochándolo → selfie en el espejo (`python marca/ugc_collar.py … --version carmen-dorada`, lágrima
  pequeña). Montaje con `--planos colgando-1:4,palma-1:2.4,cierre-1:2.6,espejo-1:4`: en el cierre, a partir del segundo
  3, Kling cambia la cara. **Voz: Silvia** (ElevenLabs Starter, biblioteca) con filtro de móvil; Edu no quiere voces de
  «doblaje». Vídeo: `marca/fotos-ia/ugc-collar-carmen-2/collar-ugc-silvia-movil-9x16.mp4` (+ `-4x5`, recorte y=165).
  Edu le pone música y lo devuelve para la campaña y un reel. Limpieza del 5-nov: borradas las otras voces y vídeos de
  prueba, el primer vídeo de Carmen y el vídeo descartado de HyperFrames. Se conservan los clips de origen y las anclas.
  **Con la música de Edu** («Holiday Bells», `marca/musica/holiday-bells.m4a`; el título del archivo es un id, parece de la
  biblioteca de sonidos de Meta) mezclada con `python marca/con_musica.py <vídeo> <música>` (la música baja cuando habla,
  -14 LUFS): **anuncio 18** `52566698768994` en la campaña y **reel programado el 6-nov 19:30** (`2026-W45-20`).
- **Cesta (5-nov, en producción, Edu: «pone total estimado, el envío es gratis no?»):** «Total» en vez de «Total estimado» y
  «Impuestos incluidos. Envío gratis a península (Baleares, 3,95 €).» en vez de «Descuentos y envío calculados en la página
  de pago» (`CAMBIOS_CESTA` en `build.py`, sobre `locales/es.json`). Motivo: del 4 al 5-nov, 7 sesiones con carrito (6 de
  Meta, todas en la ficha del collar, casi todas en móvil) y **0 llegaron al pago**; Edu probó el pago y funciona.
- **Nota del equipo** (formato 26 de la biblioteca, visto en Olivia): `python marca/nota_equipo.py` →
  `marca/fotos-ia/campana-bf/17-nota-equipo-9x16.jpg` / `-4x5.jpg` (fondo tinta, la promo y el ejemplo Collar Signé +
  Reloj Lune + aros Boucle = 109,85 € → 89,90 € con el 3x2, comprobado). **Sin publicar: falta el OK de Edu.**
- **El asistente de Meta del Administrador** dijo el 5-nov que la campaña «no entregaba»: miraba hasta el día anterior
  (0,08 € el 4-nov) y no el día en curso (35,87 € el 5-nov). Comprobar siempre con el conector antes de hacerle caso.
- **PENDIENTE (recordárselo a Edu): ElevenLabs Starter**, contratado el 5-nov por 1 $ el primer mes para usar voces de la
  biblioteca por la API (el plan Free no deja: error 402). **Se renueva solo hacia el 5-dic a 6 $/mes**: antes de esa
  fecha, preguntar a Edu si lo cancela (Suscripción en elevenlabs.io) o lo mantiene. Plan Starter, no Creator.
- **Anuncio 14 sin plazo** (Edu, 5-nov: «quita lo del plazo de entrega por ahora»): texto sin «2-5 semanas» ni «antes
  del 15 de noviembre» (creatividad 1843881623619209). **Ya no hay que pausarlo el 15-nov.** La ficha ya no daba plazo.
- Ideas del estratega en `oficina/ideas/2026-11-05-collar.md`.

**CAMPAÑA DE BLACK FRIDAY PUBLICADA (4-nov, ~18:40, OK de Edu: «lanzamos ahora», «lo testeamos»).**
«Lunerie · Black Friday · Ventas (Advantage+)» `52566458999794` · conjunto `52566459008194` (península + Baleares,
solo FB+IG, Advantage+ audiencia, compra con el píxel) · **35 €/día con tope de gasto de 140 €** (se para sola) ·
**16 anuncios** (los 8 del plan del 2-nov, con «para tu madre/hermana/pareja» como 3, + los 5 animados + el carrusel del
collar Signé). Ids en `anuncios/campana-bf-meta.json`; textos en `anuncios/campana-black-friday.md`. Sin declarar IA (Edu).
Cómo se montó: archivos subidos a Archivos de Shopify con `python anuncios/subir_creatividades.py` (URLs en
`anuncios/creatividades-urls.json`) → Meta los baja por URL. **Trampas:** en los carruseles, `image_url` deja «picture» y
«image_hash» a la vez y Meta lo rechaza → subir antes la foto (`ads_creative_upload_media`) y usar `image_hash`; Shopify
tarda unos segundos en servir una foto recién subida («Image Wasn't Downloaded» → reintentar). Cada anuncio: 4:5 en el
feed + 9:16 en Stories/Reels (`placement_customizations`). **No tocar hasta el 9-nov**; **el 14 (collar) hay que pausarlo
el 15-nov** si sigue activo (promete Navidad pidiendo antes del 15). Pendiente: clic real desde el móvil (anuncio →
tienda) y mirar que la visita sale en Shopify.

**Instagram (4-nov, noche; Edu: «lo que tú consideres», solo Instagram, Facebook no):** 5 stories de Black Friday
publicadas · reels de los anuncios animados programados: «Notas del móvil» 5-nov 19:30 y «Lo sentimos, mamá» 7-nov 19:30
(`2026-W45-14/15`, vídeo desde la URL de Shopify de `anuncios/creatividades-urls.json`). `publicar.py` ahora sube **todas**
las stories de una pieza (antes solo la primera), las deja en 9:16 (antes las recortaba a 4:5) y guarda a calidad 97.
Fuera de todos los pies la frase «Imagen creada con IA» (Edu); la marca «hecho con IA» de la API sigue puesta.

**4-nov (tarde): biblioteca ampliada, anuncios animados y Instagram roto.**
- **ARREGLADO (4-nov, ~17:30): la clave de Instagram volvió a funcionar sola** (Edu pidió probar de nuevo; la app se llama
  «Lunerie Claude Publisher»). Post del café publicado: https://www.instagram.com/p/DfU48aClgsA/. Las tareas
  programadas siguen en pie (la siguiente, el carrusel del 5-nov a las 12:30). `renovar_token.py` queda por si vuelve a
  fallar. Lo que pasó antes:
- **(histórico) INSTAGRAM NO PUBLICABA:** al ir a publicar el post del café (Edu: «no esperamos a las 7»), Meta respondió error 190 y,
  con el token de la app, «API access blocked». **Las tareas programadas van a fallar hasta arreglarlo** (no publican
  nada; la pieza sigue «aprobado»). La del 4-nov a las 19:30 se quitó; foto y texto para subirla a mano en
  `oficina/salida/2026-W45-08-lune-cafe-hora/`. Arreglo (lo hace Edu, en su cuenta): mirar avisos de la app «Lunerie
  Vega» en developers.facebook.com → generar token de usuario en el Explorador de la API Graph → pegarlo en
  `.env.local` como `IG_TOKEN_USUARIO=` → `python oficina/renovar_token.py` (nuevo: lo cambia por el de página).
  Después, volver a programar la del café (`publicar_programado.py`).
- **Biblioteca (capturas de Edu):** `biblioteca/formatos-anuncio.json` (25 formatos de anuncio de Black Friday con su
  adaptación y si encajan), `ideas-reels.json` («Déjame limpiar mi cámara», storyboard UGC, «solo el 1 % lo pausa»,
  «comenta X») y `herramientas.json` (HyperFrames, Open Higgsfield, VoiceStudio…; ninguno instalado salvo HyperFrames).
- **HyperFrames instalado** (HeyGen, Apache 2.0, v0.9.12, telemetría desactivada) en `marca/anuncios-hf/` (node_modules
  fuera de git): anuncios animados hechos con HTML + GSAP, **sin créditos de IA**. `preparar.py` baja fotos y precios
  reales de la tienda (`assets/datos.js`); cada anuncio es un `.html`; para mirar fotogramas, copiarlo a `index.html` y
  `npx hyperframes snapshot --at …`; para grabar, `npx hyperframes render -c <anuncio>.html -q delivery -o …`. Hechos 5
  (9:16 + recorte 4:5, en `marca/fotos-ia/campana-bf/` 9-13): pantalla de bloqueo, notas del móvil, «Lo sentimos, mamá»,
  piezas cayendo (recortes PNG con fondo transparente) y pack a juego. Textos y destinos en
  `anuncios/campana-black-friday.md`. Zona segura en 9:16: texto entre y=270 y y=1248 (abajo tapan los botones de Meta).
  Ojo: `mix-blend-mode` dentro de algo que GSAP mueve no funciona (se aísla): usar recortes PNG.

**DÓNDE NOS QUEDAMOS (2-nov, noche) — leer esto primero; manda sobre los bloques de abajo.**
- **EN PRODUCCIÓN (OK de Edu, 2-nov): portada en collage + BLACK FRIDAY.** `parte('hero-navidad')` en
  `lunerie-inicio.liquid`: las 3 fotos de Navidad montadas como **copias de papel** (borde irregular con `clip-path`
  —dos polígonos, `--lu-papel-a/b`—, sombra suave, giradas 1-3°) sobre niebla. Móvil: la del teléfono grande y la del
  sofá y la de la copa encima, a la izquierda (como el móvil de Caducci); PC: la del sofá en el centro. Debajo, franja
  en tinta: «Relojes y joyas para regalar · BLACK FRIDAY · La 2.ª pieza al 50 % y la 3.ª, gratis · Mezcla relojes y
  joyas · Envío gratis a península» + botones + «Hasta el 5 de diciembre: el último día para que llegue en Navidad».
  Barra: «Black Friday · 2.ª pieza al 50 % · 3.ª gratis» (`PROMO_BARRA`); caja verde de las fichas: «BLACK FRIDAY /
  2.ª AL 50 % · 3.ª GRATIS … Hasta el 5 de diciembre»; Preguntas frecuentes: «¿Cómo funciona la oferta de Black
  Friday?». **Decisión de Edu: Black Friday desde ya** (se vende aunque no sea el 27-nov), **una sola frase** para
  los dos descuentos, y **fin real el 5-dic**: los dos descuentos automáticos tienen `endsAt` 5-dic 23:59 (hora de
  España). **El 27-nov, si va bien, código del 10 %** (ojo: no se suma a la escalera; solo le sirve a quien compra 1).
  En anuncios el gancho corto puede ser «3x2 en relojes y joyas».
- **Campaña nueva de Meta (plan aprobado por Edu, 2-nov): 35 €/día × 4 días (~140 €)**, lanzar ~5-nov, sin tocar hasta
  el 9-nov; 1 campaña Advantage+ ventas, 1 conjunto (península + Baleares, solo FB+IG), **8 anuncios** con ángulos
  distintos: oferta «3x2 en relojes y joyas» · collar «Su nombre, su piedra» · «Un reloj que solo da la hora» ·
  «¿No sabes qué regalarle?» (vídeo real) · por destinataria (madre/hermana/pareja) · «¿Te quedará grande?» (eslabón) ·
  «Para ti · foto» rehecho · carrusel «Regalos de menos de 40 €». Cuentas: a 0,79 €/clic y ~15-20 € de margen por pedido
  haría falta un 4-5 % de conversión → objetivo CPC ≤ 0,40 € y 2 piezas por pedido. **Edu graba** con el móvil (muñeca
  con el Lune, ponérselo a alguien, quitar un eslabón, collar de cerca y puesto, relojes en fila); las amigas, si se
  prestan. Antes de gastar: clic real desde el móvil (anuncio → tienda) y ver por qué solo 11 de 82 clics llegaban.
- **Collar con nombre (5.2): Edu quiere meterlo ya.** Muestra de **Yiwu Shangjie** (Alibaba): pedida el 9-oct, llegó el
  23-oct con caja de terciopelo verde. **3-nov:** Yiwu Shangjie ya no tiene el anuncio publicado (le dice a Edu que lo
  sigue fabricando); Edu pasa otro proveedor, **QIUHAN** (Alibaba, producto 1601817911870; Alibaba pide captcha a
  Claude, datos de la captura de Edu): **Yiwu Qiuhan Jewelry Company Ltd.**, 7 años, top vendedor UE, 4,6/5 (604
  valoraciones de la tienda; este collar, sin reseñas), ≥97 % a tiempo, 36 % de recompra, España entre sus mercados ·
  acero inoxidable con baño de oro 18K (así lo anuncian), nombre en letra de firma + lágrima de piedra del mes a un
  lado, 3 colores · **4,56 €** (1-49 uds, con un 10 % hasta el 31-dic; 5,06 € sin él) · envío estándar **4,33 €**,
  entrega garantizada **15 nov-11 dic** (lenta para Navidad: pedir precio del exprés) · ofrece dropshipping. Puesto en
  España ~9 € + posible cargo de aduana. **Edu (3-nov):** personalización = letra + piedra; solo **oro y plata** (el oro
  rosa, no por ahora); **la letra, la misma de la muestra de Yiwu Shangjie que ya tiene** (mandarle foto); **exprés: 24 €
  y llega a principios de diciembre** → por pieza suelta se come el margen (coste ~28,6 €; CPA breakeven ~19 € a
  59,95 €), así que exprés solo para un envío conjunto a España. Falta: plazo real de fabricación + envío estándar,
  precio del exprés para 5-10 piezas juntas, largo de cadena y material (mensaje en inglés del 3-nov en la sesión).
  **FICHA HECHA (3-nov), producto «Collar Signé» `collar-signe` (11059049267539) en estado OCULTO (UNLISTED: solo con el
  enlace https://lunerie.es/products/collar-signe, fuera de colecciones y buscador), 49,95 € (propuesta; Olivia 48,95 €),
  Color Dorado/Plateado × Mes (24 variantes, SKU SIGNE-DOR-01…), sin control de stock. `productos/collar_signe.py`.
  Plantilla `product.collar.json` + `tema/codigo/snippets/lunerie-collar.liquid` (como Olivia): panel lateral con las 12
  lágrimas (colores sin nombres de gemas), campo «Nombre» (máx. 10 letras, propiedad del pedido: sale en la cesta y en
  el pedido) y casilla obligatoria «He revisado el nombre»; sin piedra elegida no deja añadir; sin barra fija de compra.
  Probado en la tienda real (cesta: «Dorado / Mayo · Nombre: …»; el Black Friday se le aplica). **Más tarde (Edu):**
  fuera la casilla obligatoria (queda el aviso «se graba tal cual lo escribes») y la línea «Se hace para ti… llega en…»;
  fotos de Olivia sustituidas por 4 de IA con nombres españoles (`marca/collar_ia.py`, ~1 $): Marta (azul, producto
  dorado) · Carmen (verde, con el Lune y el Nuit) · Elena (amarilla, con los aros Boucle) · Paula (rosa, plateado).
  **Nunca «Lucía»** en ejemplos (Edu). Nombres revisados a tamaño real. Cambiarlas por fotos reales con el primer pedido.
  **4-nov: A LA VENTA** (OK de Edu al nombre «Collar Signé» y a 49,95 €): ACTIVE, solo Tienda online, entra solo en
  «Joyas» (último del escaparate del inicio). Galería: las 4 de IA y detrás otra vez las 4 de Olivia (Edu: «no restan»).
  Bolita del plateado arreglada en toda la tienda (fuera «Plateado» de `PIEDRAS`: salía verdosa en Maille, Galet y collar).
  **Pendiente:** fecha de Navidad y plazo reales cuando conteste QIUHAN (ahora «antes del 15 de noviembre»). Plazo provisional «2-5 semanas» y Navidad «antes
  del 15 de noviembre» (`PLAZO_COLLAR`, `NAVIDAD_COLLAR` en build.py) hasta que QIUHAN diga los días reales. Para
  lanzarlo: OK de Edu (nombre, precio, plazo) → status ACTIVE (entra solo en «Joyas» por tipo Collares).
  Cada pedido: copiar el nombre, el color y el mes del pedido de Shopify al proveedor. **Falta de Edu:** enlace de Alibaba, fotos/vídeo de la muestra y la respuesta
  del proveedor al mensaje en inglés (pedidos sueltos a España con nombre, coste y plazo DDP, sin tarjeta «THANK YOU»,
  lista diaria + seguimiento en 48 h, foto antes de enviar). Ficha: campo «Nombre» (máx. 10 letras) + mes/piedra +
  metal + casilla obligatoria, hecho en el tema sin app. Último pedido para Navidad ~1-dic.
- **«Packs para regalar» EN PRODUCCIÓN (OK de Edu, 2-nov)** en el hueco tras las opiniones (`parte('packs')`): A juego
  (Lune + collar Lune, 57,43 €) · Para cada día (Sépia + Boucle, 44,93 €) · El regalo completo (Galet + Duo + Boucle,
  54,90 €). Solo piezas sin talla; el color se elige en la tarjeta y «Añadir el pack» mete todo con `/cart/add.js`.
  **Probado en lunerie.es:** el precio de cada tarjeta = el total que cobra Shopify en la cesta. El precio se calcula en
  Liquid (céntimos, la más barata al 50 % redondeando hacia abajo, o gratis con 3); si cambia la promo, cambiarlo ahí.
- **Anuncios de la campaña HECHOS (2-nov), sin gastar créditos:** `python marca/campana_bf.py` → `marca/fotos-ia/campana-bf/`
  (4:5 y 9:16, precios leídos de la tienda; en 9:16 el texto entre el 14 % de arriba y el 35 % de abajo): oferta con la
  foto del teléfono · pack a juego · carrusel de Navidad (3 fotos con piezas y precios + tarjeta) · «Un reloj que solo
  da la hora» (vídeo 10 s + foto) · «Para ti» · «Regalos de menos de 40 €» · «Para tu madre / hermana / pareja» ·
  vídeo de la oferta (9 s). Sin música (la pone Meta). **Textos, destinos con UTM y configuración en
  `anuncios/campana-black-friday.md`.** **El conector de Meta («Meta ads Koco») no estaba cargado en la sesión del 2-nov:**
  para que Claude cree la campaña hay que tenerlo conectado en claude.ai; si no, la monta Edu en el Administrador.
- **Tema de prueba** «Prueba home 29-oct» (210513527123) tiene lo mismo que el publicado en inicio, barra y fichas.

**DÓNDE NOS QUEDAMOS (1-nov, tarde).**
- **En producción (lunerie.es):** 11 productos activos (5 relojes: Lune, Sépia, Maille, Galet, Perle · 6 joyas: Larme,
  Nuit, Collar Lune, Étoile, Boucle, Duo), colecciones **Relojes** y **Joyas** (esta, solo joyas) en el menú, inicio
  con escaparates partidos + reseñas, **promo «3x2 en toda la tienda · 2.ª pieza al 50 %»** (descuentos automáticos,
  barra fija, caja en fichas, aviso en la cesta y FAQ) y reseñas sin «Recibido como regalo». Campaña de Meta sigue
  **pausada**. No quedan borradores.
- **Sin decidir (Edu): la portada de Navidad** (3 fotos con flash + franja de la promo) está **solo en el tema de
  prueba** «Prueba home 29-oct» (210513527123): https://lunerie.es/?preview_theme_id=210513527123. En producción
  sigue la portada con **vídeo**. Edu aún no sabe si se queda con estas fotos. Para publicarla: `build.py` ya la tiene
  (`parte("hero-navidad")`), así que basta con `python tema/build.py` + push de `templates/index.json` y
  `snippets/lunerie-inicio.liquid` al tema publicado. **Ojo:** mientras no se decida, cualquier push de
  `templates/index.json` o `lunerie-inicio.liquid` al publicado sube también la portada nueva → si hay que subir otra
  cosa antes, volver a poner `parte("hero-video", …)` en `build.py`. Para rehacer fotos: `python marca/portada_navidad.py
  <refs> [izquierda|centro|derecha] --n 2` (refs = 1.ª foto de cada producto con su handle de nombre).
- **Hueco libre en el inicio** tras las reseñas (donde estaba «Así son las piezas»): Edu pensará qué poner.
- **Siguiente con Claude:** decidir la portada → campaña nueva de Meta con la promo como gancho («3x2 en relojes y joyas
  para regalar», todos los anuncios a los precios nuevos; los viejos dicen 49,95 € y «10 % de regalo») → Black
  Friday (el 20 % con código va ahí, con fecha de fin).
- **Pendiente de Edu:** coste del envío del Maille · muestras de los productos nuevos · regenerar la clave de
  Higgsfield (en este PC funcionó el 1-nov con la de `.env.local`).

**Detalle del 1-nov:**
- **Publicados los 6 nuevos** (OK de Edu): Sépia, Maille, Galet, Perle, aros Boucle (con **los dos tamaños**, decidido) y
  anillo Duo → ACTIVE solo en Tienda online; fichas 200 y «Agregar al carrito» comprobados (`/products/<handle>.js`).
- **Borrados todos los demás borradores** (14, a petición de Edu): los 4 relojes descartados, las 8 joyas de DSers del
  28-oct y los 2 productos DSers del 21-oct (los de la fuente del Lune; antes se decía «no borrarlos»; Edu pide los
  pedidos a mano en AliExpress). Ninguna foto suya la usaba otro producto (comprobado antes de borrar).
- **Colección nueva «Relojes»** (`relojes`, automática por tipo = Relojes, orden manual: Lune, Sépia, Maille, Galet,
  Perle, publicada en Tienda online). En `main-menu` y `pie-tienda`, «Reloj Lune» → **«Relojes»**.
- Colección `joyas` (todas las piezas, orden manual) reordenada: **los 5 relojes primero** y luego las joyas → «Las
  piezas» del inicio enseña el Lune grande + Sépia, Maille, Galet y Perle (sin tocar el tema). Ojo: el menú «Joyas»
  apunta a esa colección, que también tiene los relojes (si molesta, crear una de solo joyas y cambiar el menú).
- **Inicio nuevo (1-nov, EN PRODUCCIÓN con el OK de Edu; probado antes en «Prueba home 29-oct» 210513527123):** como el carrusel de Caducci, dos **escaparates** que se deslizan (`parte('escaparate')` en
  `lunerie-inicio.liquid`, `coleccion: 'relojes'` / `'joyas'`): tarjeta partida con la foto en persona (2.ª del
  producto) + el producto en niebla (1.ª), etiqueta con el nombre, nombre, **«Frase corta»** (campo de producto
  `custom.frase`, se cambia en el Admin) y precio con el tachado si lo hay. Relojes en tarjeta alta (4:5); joyas en
  tarjeta ancha (8:5: aros, anillos y collar son anchos). Debajo, **«Lo que nos cuentan»** (`parte('opiniones')`):
  las opiniones activas en fila, con la media real (sin cifras inventadas tipo «135.000 mujeres»). «Las piezas»
  queda con `"disabled"`. **«Así son las piezas» (`como_es`) oculta** (a Edu no le gusta): hueco tras las opiniones
  para otra cosa, por decidir. **Colección `joyas` = solo Anillos/Pendientes/Collares desde el 1-nov** (el menú «Joyas» ya
  no enseña relojes); «Te puede interesar» recomienda por tanto solo joyas. Para subirlo: `python tema/build.py` →
  push de `templates/index.json`, `snippets/lunerie-inicio.liquid` y `snippets/lunerie-combina.liquid`.
  El validador de la skill `shopify-liquid` no funciona en este PC (le falta `@shopify/theme-check-common`): usar
  `shopify theme check --path tema/tienda`. Playwright para Python instalado el 1-nov en este PC.
- **PROMO EN MARCHA (1-nov, Edu: «que sea atractiva y saquemos pasta»): «3x2 en toda la tienda · 2.ª pieza al 50 %»**,
  mezclando relojes y joyas. Dos descuentos automáticos en Shopify sobre las colecciones Relojes + Joyas:
  **«2.ª pieza al 50 %»** (DiscountAutomaticNode 1860761354579, compra 1 → 1 al 50 %) y **«3x2: la 3.ª pieza, gratis»**
  (1860761387347, compra 2 → 1 gratis); no se combinan entre sí ni con códigos (sí con envío). Shopify descuenta la
  pieza más barata y aplica el que más ahorra (probado en cestas reales: Sépia + Boucle 69,90 → 44,93 €; Lune +
  Boucle + Duo 79,85 → 59,90 €). Cuentas: con la promo ningún pedido deja menos que una pieza sola (~18 € un reloj
  barato, ~14,5 € el Lune), salvo Lune + Maille (~11,6 €); 2.º gratis NO (~8 €) y un 20 % fijo con código tampoco
  (guardarlo para Black Friday). En el tema: **`PROMO = True`** en `build.py` → frase en la barra de arriba (**sola y fija**:
  Edu quitó el envío gratis y las devoluciones de la barra el 1-nov; con `PROMO = False` vuelven), caja verde «3x2 EN TODA LA TIENDA» en todas las fichas (bloque `oferta`) y aviso en la cesta
  según el número de piezas (`snippets/lunerie-segundo-reloj.liquid`, nombre antiguo). En Preguntas frecuentes:
  «¿Cómo funciona el 3x2?» y «¿Llegan juntas?» (pueden llegar en paquetes distintos). Quitarla: `PROMO = False` +
  desactivar los dos descuentos. Los anuncios nuevos pueden usarla.
- **Portada de Navidad (1-nov, en el tema de prueba 210513527123; falta el OK de Edu para producción):** como la de
  Caducci pero con los colores de Lunerie. Tres fotos de noche con flash (terciopelo verde botella, dorados, velas)
  con piezas reales: izquierda Galet + anillo Nuit + aros Boucle · centro Lune + collar Lune + Maille · derecha Sépia +
  pendientes Larme. Script `marca/portada_navidad.py` (API de Higgsfield, 6 fotos ≈ 0,80 $; salen en
  `marca/fotos-ia/portada-navidad/`, elegidas izquierda-1, centro-1 y derecha-2). Archivos de Shopify
  `portada-navidad-izquierda/centro/derecha.jpg`. Debajo, franja en tinta: «Regalos para esta Navidad · Relojes y
  joyas para regalar · 3x2 EN TODA LA TIENDA · y la 2.ª pieza al 50 %» + «Ver los relojes» / «Ver las joyas» + envío
  gratis y fecha de Navidad (nada de estrellas, «135.000» ni «solo 50 piezas»). En móvil solo la foto del centro, para
  que la promo se vea arriba. `parte('hero-navidad')` en `lunerie-inicio.liquid`; volver al vídeo: `parte("hero-video")`
  en `build.py`. Fidelidad revisada en recortes a tamaño real (el Lune sale pequeño; la esfera algo redonda).
- **Opiniones: las 4 amigas dieron el OK a sus textos (1-nov)**; ya no es un pendiente. La etiqueta «Recibido como
  regalo» ya **no se enseña** (Edu, 1-nov; en la ficha y en el inicio); el dato sigue en el metaobjeto y «Compra
  verificada» sí sale cuando la haya.
- Sigue pendiente de Edu: coste del envío del Maille, muestras de los nuevos, regenerar la clave de Higgsfield.
  Siguiente con Claude: la campaña «Un reloj que solo da la hora» (punto 2 de abajo).

**DÓNDE NOS QUEDAMOS (30-oct, noche) — leer esto primero; el detalle de cada punto está en las entradas del 30-oct de abajo.**
- **Estado:** tienda abierta · **campaña de Meta PAUSADA** (66,40 €, 0 ventas; no reactivar sus anuncios: dicen 49,95 € y
  «10 % de regalo») · Reloj Lune a **39,95 € con tachado 44,95 €** (quitar el tachado hacia mediados de noviembre o antes de
  Black Friday) · rasca desactivado (el código LUNERIE10 sigue activo en Descuentos) · **Lunerie = tienda de relojes pequeños
  vintage**, dropshipping con pedidos a mano de Edu · **6 productos nuevos en BORRADOR** con fichas, fotos IA y plantilla
  «reloj»: Sépia, Maille, Galet, Perle, aros Boucle y anillo Duo.
- **Pendiente de Edu:**
  1. OK a las fichas nuevas (Admin → producto → Vista previa).
  2. Aros Boucle: ¿dejar solo el mediano (18 mm)? Ahora tiene pequeño + mediano.
  3. Coste del envío a España del Maille (no es «Choice»).
  4. Pedir muestra de cada producto nuevo (calidad, plazo real y si la correa del Sépia es piel de verdad).
  5. Borrar los 4 relojes descartados (siguen en borrador): GREALY cuadrado, piedras de colores, tonel rosa y rectangular
     con brillantes.
  6. **Regenerar la clave de Higgsfield** (se pegó en el chat el 30-oct) y ponerla él mismo en `.env.local` de los dos PCs.
     En `C:\Users\edu\lunerie\.env.local` ahora solo está `HF_KEY` (las claves de Instagram siguen solo en `D:\LUNERIE`).
- **Siguiente con Claude:**
  1. Con el OK: publicar los 6 (ACTIVE + solo Tienda online; entran solos en la colección `joyas` por tipo), revisar cómo queda
     la sección «Las piezas» del inicio con más productos y cambiar el menú «Reloj Lune» por una colección de relojes.
  2. Campaña nueva **«Un reloj que solo da la hora»** con la colección entera: fotos en `marca/fotos-ia/campana-hora/`;
     animar los 3 clips (~1-1,50 $, Kling por la API) y montar el vídeo; guion para que las amigas graben clips reales;
     8-10 anuncios (vídeos + «Para ti · foto», que fue el que más clics trajo), todos a los precios nuevos.
  3. Mirar la ficha antes de volver a gastar: con 11 visitas medidas de Meta, nadie añadió al carrito (ShopifyQL ya
     disponible, ver la entrada del test).
- Fotos IA: en git van los JPG; los PNG originales se quedan en el disco (están en `.gitignore`).
- **30-oct (tarde): Edu importó 8 relojes y 2 joyas con DSers → entraron ACTIVOS y a precio de coste (otra vez): pasados a borrador al momento.** Hecho el primero, **Reloj Sépia** (`reloj-sepia`, rectangular con correa marrón/negra, Lucky Fox L19, Choice, coste 4,49/5,14 € sin envío, **34,95 €**, BORRADOR): variantes sobrantes borradas, colores en español, fotos en niebla 4:5 sustituidas en su sitio, inventario arreglado y **plantilla nueva `product.reloj.json`** (la de joya + «¿Se puede mojar?»; la correa va en la descripción). Bolita «Marrón» añadida a `PIEDRAS`. **Hechos también (OK de Edu), todos en BORRADOR con plantilla y foto por variante:** **Reloj Maille** (`reloj-maille`, oval con malla, BS Bee Sister FA1837, Dorado/Plateado, 39,95 €; no es Choice: falta el coste del envío) · **Reloj Galet** (`reloj-galet`, oval grueso, Dorado/Plateado, 34,95 €) · **Reloj Perle** (`reloj-perle`, perlas de imitación, sin variantes, 34,95 €) · **Aros Boucle** (`aros-boucle`, en U, Pequeño 14 mm / Mediano 18 mm, 19,95 €) · **Anillo Duo** (`anillo-duo`, esmalte azul y beige, ajustable, 19,95 €). Scripts para repetirlo en la próxima importación: `productos/normalizar_dsers.py` + `productos/gql.py`. **Fotos IA puestas el 30-oct** (`marca/fichas_ia.py` → `marca/fotos-ia/fichas/`, ~1,30 $): producto en niebla de Maille, Galet, Perle y Duo + puesto en persona de los 6 (estilo Olivia: punto crema, cara cortada); todas las fichas siguen la regla 1.º niebla · 2.º persona · luego las del proveedor; en Maille y Galet la foto de la variante «Dorado» es la de niebla. (La de Perle en persona la bloqueó el filtro de Higgsfield con «manos sobre un vestido a la cintura»: se rehízo con una taza.) **Modelo de trabajo (Edu, 30-oct): dropshipping de momento; Edu hace cada pedido a mano y elige el proveedor** (el asociado en DSers u otro), hasta ver qué se vende; el stock propio, más adelante. **Falta para publicar:** OK de Edu a las fichas, ACTIVE + solo Tienda online, y pedir muestras. **Descartados:** GREALY (copia del Cartier Panthère), el de piedras de colores («jade natural», pisa al Lune), tonel rosa y rectangular con brillantes. `@idempotent` va en el CAMPO de la mutación, no en la operación.
- **DECISIÓN DE EDU (30-oct): Lunerie = «la tienda de los relojes pequeños vintage»**, con las joyas de acompañantes. La tienda sigue con el aspecto y el tono de Olivia Jewelry y se vende como Caducci, pero solo con lo verdadero: **colección de 3-5 relojes pequeños** (no uno solo) + pack (reloj + joya o dos relojes) + muchos anuncios (15-20 variaciones con IA). Nada de escasez falsa, «waterproof», «Italy» ni marcas ajenas. **Plan B: el collar con nombre (5.2)**, que a Edu le gusta por la personalización; se aparca hasta ver si los relojes funcionan (para Navidad, decidir hacia el 10-nov: los personalizados tienen fecha límite ~1-dic). Siguiente: Edu manda capturas de 2-4 relojes pequeños de AliExpress → fichas → campaña nueva («Un reloj que solo da la hora», fotos en `marca/fotos-ia/campana-hora/`; clips animados pendientes, ~1-1,50 $).
- **30-oct: resultado del test de Meta (65,54 € hasta las 10 h): 0 ventas, 0 pagos empezados, 0 carritos medidos.** Solo FB+IG: ~82 clics salientes a ~0,79 €/clic, CTR ~0,9 %, pero solo 11 visitas medidas por el píxel. Por clics gana **«Para ti · foto»** (37 clics, 0,60 €/clic), luego «Regalo · vídeo» (19, 0,69 €); «Estilo» es el peor. Según la regla KILL, no pasa; el atasco está después del clic (precio, plazo, ventanas, confianza o medición). **Edu bajó el Lune a 39,95 € y quitó el rasca.** **Campaña PAUSADA el 30-oct (~11 h) con 66,40 € gastados** (sus anuncios decían «49,95 €» y «10 % de regalo»: no reactivarlos). Nueva idea de campaña (30-oct): moda del «reloj de la abuela» (Gen Z, desconectar del smartwatch) → «Un reloj que solo da la hora», con gente; Caducci tiene 563 anuncios activos en Meta y Calné ninguno en España. **Shopify (ShopifyQL, permiso `read_reports,read_analytics` dado el 30-oct; consulta `FROM sessions SHOW sessions, sessions_with_cart_additions, average_session_duration, bounce_rate GROUP BY utm_source …` con `shopifyqlQuery`):** del 28 al 30-oct, 66 sesiones en total y **0 con carrito**; con `utm_source=meta` solo **11** (8 móvil, 3 PC), 75 % de rebote, ~2,5 min de media en móvil. De ~82 clics salientes solo se ven 11 visitas: Shopify también depende del banner de cookies, así que no se sabe si el resto se fue antes de cargar o no contestó al banner.
**Dónde nos quedamos (27-oct, ~23 h): CAMPAÑA LANZADA.**
- **28-oct: la campaña tardó ~12 h en arrancar** (a las 11 h, 0 € y 1 impresión, sin errores, con 5 anuncios en
  «pending · preparing»). Al mediodía ya gastaba sola, sin tocar nada: **1,51 €, 227 impresiones, 2 clics**
  (Estilo · vídeo y Para ti · foto, CTR ~3 %), 0 carritos. Es normal en una cuenta nueva: Meta suelta poco a poco.
  Algunos anuncios siguen «preparing» aunque ya gastan. **El test de 3 días cuenta desde el 28-oct** (día 1).
  12:10-13:08 Edu aplicó en el Administrador la música y otras recomendaciones de Meta a los 6 anuncios: volvieron
  a revisión (aprobados 12:13 y 13:10) y el aprendizaje se reinició, sin coste (solo llevaba 1,5 €). Meta generó
  vídeos nuevos (1453802080087465 regalo, 1145325581356601 para ti, 1862931217923569 estilo) y las fotos pasaron
  al botón «Ver detalles» (SEE_DETAILS); los vídeos siguen con «Más información». **Desde aquí, no tocar nada
  hasta el 30-oct**: cada cambio en un anuncio lo manda a revisión y reinicia el aprendizaje.
- **29-oct: home integrada con las joyas (en producción).** Portada con el mismo vídeo y titular de marca «Relojes y
  joyas *para regalar.*» (botón «Ver el reloj · 49,95 €» + enlace «Ver las joyas») · sección **«Las piezas»**
  (`parte('piezas')` en `lunerie-inicio.liquid`, cuadrícula propia con la colección `joyas`: Lune grande a la izquierda
  y 4 joyas en 2×2; móvil: Lune a todo el ancho) que sustituye a la fila «Las joyas» de Horizon (ya no existe en
  `build.py`) · «Así son las piezas» (rasgos para todo, no solo el reloj) · «Antes de comprar» con Navidad / «¿Me
  quedará bien?» (correa + guía de tallas) / «¿Se pueden mojar?». Probado antes en el tema sin publicar «Prueba home
  29-oct» (210513527123), que sigue ahí y se puede borrar. Para ver el scroll en PC con Playwright hay que mover
  `.page-wrapper` (el `body` tiene `overflow:hidden`); en móvil, capturar con `locator(...).screenshot()`.
- **29-oct: diagnóstico del píxel** (`oficina/informes/ads-diagnostico-pixel-2026-10-29.md`): el píxel 1096538246614496 está bien enlazado a la cuenta y al conjunto de anuncios (optimiza por compra) y la URL de destino es correcta; la página carga rápido. El problema de medir clics: el píxel no dispara hasta contestar el banner de cookies y en móvil el banner tapaba el 40 % de la primera pantalla. **Banner compactado en móvil** (build.py, sección `cookies` del pie; Aceptar y Rechazar iguales). **Dominio lunerie.es verificado en Meta el 29-oct** (etiqueta meta en `snippets/meta-tags.liquid`; no quitarla). **Audience Network excluido el 29-oct** (el 69 % de los clics salientes venía de ahí, a 0,01 €, sin visitas: conjunto 52564454188194 ahora solo Facebook e Instagram; las cifras de CTR/CPC de 28-29 oct, y la idea de que el vídeo gana a la foto, están contaminadas por esos clics). Pendiente de Edu: sesiones por UTM en Shopify.
- **28-oct:** en `settings_data.json` del tema hay un bloque de la app **Loox** que `build.py` no tiene: no subir
  `config/settings_data.json` sin añadirlo antes.
- **La tienda YA ESTÁ ABIERTA** (sin contraseña, comprobado el 27-oct por la noche).
- **Campaña de Meta ACTIVA desde el 27-oct (~23 h):** «Lune · Lanzamiento · Ventas (Advantage+)»
  (52564454147994), 30 €/día, conjunto «España península y Baleares · abierto» (52564454188194).
  **Anuncios que corren (28-oct, ~00 h): fotos «· v3» y vídeos «· v4 música»**, todos con botón **«Más
  información»** (Edu); las fotos con música automática de Meta (solo se puede en fotos) y los vídeos con
  «Agua» (Mariano) metida en el archivo. Ids, origen de la música y el aviso de derechos en
  `anuncios/test-reloj-lune.md`. El resto (originales, «v2», vídeos «v3»), en pausa con 0 €.
  Los 6 originales están **en pausa** con 0 € gastados: Meta avisaba «no se entregará en
  18 ubicaciones» (Reels in-stream +17) porque llevaban título y descripción dentro del botón (`call_to_action.value.
  link_title/link_description`, obsoletos). **Al crear anuncios por API: el botón solo con `link`** (título en
  `video_data.title` / `link_data.name`, descripción en `link_description` / `description`) y las mejoras
  automáticas en `OPT_OUT` (`degrees_of_freedom_spec`). Queda un borrador «NO PUBLICAR · borrador de prueba
  sobrante» (52564507156794) en pausa: no publicarlo. A partir de aquí, 48 h sin tocar nada (apartado 7).
- **Campaña vieja** «Lune · Test 90 € · Ventas (ABO)» (52564402827594): Edu dijo borrarla, pero la herramienta
  **no puede borrar una campaña que nunca se publicó** (error 1487564 «New campaigns need to be either active or
  paused»; se volvió a dejar en pausa, sin errores). **La borra Edu** en el Administrador de anuncios: marcar solo
  esa → papelera (no «Descartar todos los borradores», que se llevaría la nueva). Mientras exista, no usar el botón
  «Publicar» del Administrador.
- **Instagram (27-oct):** usuario **@luneriejewelry**, nombre «Lunerie | Relojes y joyas», enlace del pie de la
  tienda ya cambiado. Bio y textos de las 6 publicaciones de IA en **`anuncios/instagram.md`** (Edu los pega;
  fijar 3; archivar los 3 posts viejos con relojes que no se venden).
- **Resto, hecho y subido:** tema publicado 209073799507 · precio 49,95 € · rasca del 10 % (LUNERIE10) · opiniones
  con metaobjetos + formulario a hola@lunerie.es (Edu tiene que mandarse una de prueba) · portada con vídeo del
  verde · plazo del pago 7-12 días laborables (comprobado). Higgsfield (conector): quedan 0,55 créditos.
- **28-oct (tarde): fotos IA y ficha a pantalla completa.**
  - **API de Higgsfield con saldo** (Edu puso 10 € el 28-oct; la clave de `.env.local` es la misma de siempre).
    Modelo `marketing-studio/image/flare` (GPT Image 2.5): 2k, calidad alta, **~0,13 $ por foto**; acepta 3:4 pero
    **no 4:5** (recortar luego a 4:5 con PIL). **Nano Banana solo va por el conector** (no está en la API).
  - **Reloj Lune (en producción):** galería con el reloj suelto en niebla primero y la modelo segunda; la variante
    «Verde» pasó a la foto del producto suelto (una variante solo admite una foto: quitar la vieja y luego poner la nueva).
  - **Ficha a pantalla completa en PC, como Olivia** (`ficha` en `build.py`, vale para reloj y joyas): sección a
    todo el ancho (`content-full-width`, `equal_columns`, `gap` 0), foto con 48 px de margen y detalles centrados en su
    mitad con 34 rem de ancho (`PRODUCT_CSS`). Medido contra oliviajewelry.com a 2554 px (la pantalla de Edu): casi igual.
    Para ver la web con Playwright en este PC: `chromium.launch(executable_path=<Chrome instalado>)`, no hay navegador
    propio descargado; `wait_until='domcontentloaded'` (Olivia nunca queda «idle»).
  - **«Te puede interesar» (28-oct, como el «Pairs well with» de Olivia):** carrusel de 4 tarjetas (foto, nombre, precio,
    «Ver») al final de la columna de detalles, con los demás productos de la colección `joyas` sin el actual (incluye el
    Reloj Lune). Va en el Reloj Lune y en **todas las joyas** (`_con_combina` en `build.py`). Código:
    `tema/codigo/snippets/lunerie-combina.liquid`. Ojo: el `ul { padding-inline-start }` de `PRODUCT_CSS` afecta a
    cualquier lista de la ficha (por eso lleva `padding:0!important`).
  - **Columna de detalles fija «como Olivia» (28-oct):** la columna medía más que la pantalla y, fija arriba, no se veía
    nunca su final. El mismo snippet calcula `top = -(alto − pantalla + 16)` (ResizeObserver): la columna sube con el
    scroll hasta que su final toca el borde de abajo y ahí se queda; si cabe entera, queda fija arriba como antes.
  - **«La leyenda» de las joyas (28-oct, idea de Edu):** texto corto sobre los desplegables con una historia inventada
    del castillo de **Lunerie «donde la luna guarda sus joyas»** (Nuit: la reina y las noches sin luna · Larme: lágrimas
    de alegría hechas piedra · Collar Lune: la luz de la luna prendida en la cadena · Étoile: una estrella por mes en la
    torre más alta). El párrafo «Por qué lo elegimos» se quitó el 28-oct (no le gustaba a Edu). Está en `tema/codigo/snippets/lunerie-leyenda.liquid` (un `when` por handle).
    **Regla:** es un cuento («cuentan que», «dicen que»), nunca un dato: nada de «hecha a mano», oro, piedras preciosas
    ni un origen real. El Reloj Lune no la lleva todavía; Edu quiere darle forma más adelante (mundo del castillo).
  - **Zoom de las fotos en móvil (28-oct):** al tocar una foto, el tema (Horizon) abría la ventana de zoom ya ampliada
    a **1,5×** (`DEFAULT_ZOOM` en `assets/drag-zoom-wrapper.js`, solo móvil). Ahora abre a 1× (`START_ZOOM`); el doble
    toque amplía a 1,5× y se puede pellizcar. Es un fichero de Horizon **modificado**: la copia buena está en
    `tema/codigo/assets/` (`build.py` copia ahí también los `*.js`) y, como los otros ficheros modificados, no recibe
    los arreglos de Horizon al actualizar el tema.
  - **Joyas PUBLICADAS (Edu, 28-oct tarde):** las 4 ACTIVE solo en Tienda online (no en Facebook e Instagram) ·
    «Joyas» en `main-menu` y `pie-tienda` · sección «Las joyas» del inicio activada · foto IA de Étoile (2.ª foto) ·
    plantilla **`product.anillo.json`** (los dos anillos; es la de joya + desplegable «¿Cuál es tu talla?» bajo el selector:
    contorno del dedo en mm → talla 12 = 52 mm, 14-15 = 54,5 mm, 17 = 57 mm; fuera de 51-59 mm, escribir a hola@) ·
    SEO y descripción del Lune sin «dorado o plateado», «caja de regalo» ni «seis colores».
  - **TRAMPA DE DSERS (28-oct): las variantes importadas salían «NO DISPONIBLE» en la tienda** aunque Admin decía
    `availableForSale: true`. Su inventario estaba solo en el «almacén» `dsers-fulfillment-service`. Arreglo (como el
    Lune): `tracked: false` en las variantes, `inventoryActivate` en el almacén de la tienda (Location 127723929939)
    y `inventoryDeactivate` del nivel de DSers. **Las mutaciones de inventario exigen `@idempotent(key: "<uuid>")`**.
    Al importar con DSers, hacerlo siempre antes de publicar y comprobar con `https://lunerie.es/products/<handle>.js`
    (`available`) y que el botón de la ficha diga «AGREGAR AL CARRITO».
  - **Trampa de mi script `gql.py`:** el CLI devuelve los fallos como `{"error": …}` (sin «s») y no los detectaba:
    comprobar siempre el resultado leyendo el dato otra vez.
- **29-oct: revisión de Sidekick (el asistente de Shopify) de las fichas de joyas.** Hecho: las opiniones ya dicen lo
  suyo en cada pieza (la frase de «el reloj para probarlo» la quitó Edu el 29-oct del todo; cada tarjeta sigue llevando su etiqueta «Recibido como regalo»; el mensaje vacío dice «tus pendientes /
  tu anillo / tu collar»: `lunerie-opiniones.liquid`) y la línea de ventajas lleva el plazo: «Envío gratis a península,
  con seguimiento · llega en 7-12 días laborables» (todas las fichas). **Pendiente, necesita datos reales:** medidas y
  peso de Larme (captura de la ficha de AliExpress), qué presentación recibe la clienta (foto real y frase cuando
  lleguen las muestras: hoy van en bolsita, sin caja) y opiniones de las joyas (no se rellenan; solo reales). Decididos
  por Edu/Claude: no reorientar la portada (el reloj es el producto del test) y no bajar precios (apartado 5.4).
  **Pedidos reales: ninguno** (solo los 3 de prueba del 15-oct, reembolsados); los «checkouts completados» del informe de
  tráfico son pruebas, y las visitas del navegador automático de Claude también suman en ese informe.
- **29-oct: vídeo del collage vacío en iPhone.** Los mp4 subidos a Archivos de Shopify se sirven desde su URL
  «original» (`cdn.shopify.com/videos/c/o/v/<id>.mp4`) con `Content-Type: application/octet-stream` + `nosniff`: Chrome
  los reproduce, **Safari del iPhone no** (la casilla salía vacía en la ficha del Lune). Arreglo: usar la versión
  transcodificada (`…/c/vp/<id>/<id>.HD-720p-….mp4`, `video/mp4`, con rangos), que sale de `Video.sources` en la API
  (`query{files(query:"media_type:VIDEO"){nodes{... on Video{sources{url mimeType}}}}}`). Cambiado en el collage y en la
  fila «De cerca» (oculta). **Sin comprobar en un iPhone real** (Playwright no tiene WebKit útil en este PC).
  **Pendiente:** el vídeo de la portada (`parte('hero-video')` en `lunerie-inicio.liquid`) usa las mismas URLs
  «originales» → mismo riesgo en iPhone.
- **29-oct: `biblioteca/`** (idea de Edu: «una base de datos para crear contigo y para las campañas»): `hooks.json` (80
  ganchos con huecos de @karoempowerment, 4 categorías de 20; 10 con idea de adaptación a Lunerie), `skills-claude.json`
  (13 skills de @lucasacosta.ia, **sin instalar ni revisar**) y un `README.md` con reglas y cómo ampliarla. Se usa al
  escribir anuncios y guiones: se adapta la FORMA del gancho, y los de primera persona solo si son verdad (nada de
  testimonios inventados). Cada captura nueva de Edu = una entrada nueva con su `fuente`.
- **29-oct: LA OFICINA (`oficina/`, agentes en `.claude/agents/`, comando `/oficina-semana`).** Equipo de 4 agentes de Claude Code
  para contenido y ads; **Edu aprueba, los agentes proponen**: `estratega-creativo` (ideas: radar + Biblioteca de anuncios de Meta +
  `biblioteca/`), `community-manager` (piezas en `oficina/cola/`, JSON con estados `borrador→revisado→aprobado→publicado`),
  `editor-video` (ffmpeg con `marca/montaje.py`, que desde hoy admite `--musica pista.mp3 [--vol] [--musica-inicio]`) y `experto-ads`
  (solo herramientas de LECTURA de Meta: no puede tocar presupuestos ni anuncios). Reglas y diagrama en `oficina/README.md`.
  Primera semana de contenido: 7 piezas en `borrador` (`oficina/cola/2026-W45-*`) + 3 de la W46 (y las de abajo); coste pendiente de OK: 0,91 $.
  **Publicar en Instagram ya funciona (29-oct, ver «Publicación en Instagram por API»)**; falta una pista de música con licencia. `.gitignore`: `.claude/agents/` y
  `.claude/commands/` ahora SÍ van a git (el resto de `.claude/` no). **Verla «estilo Habbo»:** extensión de VS Code *Pixel Agents*
  (pablodelucca, MIT, v1.5.0, instalada el 29-oct): abrir su panel con la paleta de comandos y aceptar que instale sus ganchos en Claude Code;
  solo muestra lo que corre en este PC (no rutinas en la nube) y las salas se pintan en su editor de diseño.
- **Radar (`D:\aura-ai-portfolio\projects\05_producto_ganador`), revisado a fondo el 29-oct.** Funciona (20 tests OK; embudo Meta → Claude → Shopify →
  AliExpress → informe) pero los datos son del **6-7 oct**: 2.435 anuncios, **177 de joyería y relojes de 31 tiendas** (que la oficina lee con
  `python oficina/radar_a_oficina.py`, en solo lectura) y la tabla `tests` **vacía** (la campaña del Lune no se registró con `cli.py test`).
  Hallazgos: (1) el **lanzador y su ficha `reloj-vintage.toml` están desfasados** respecto a Lunerie («ajustado a su muñeca», caja de regalo, plateado,
  2.º reloj por 19,95 €, emojis en los guiones): no reutilizar su `anuncios.md`; la verdad es ESTE fichero. (2) Usa la **API de Anthropic** (clave en
  `D:\aura-ai-portfolio\.env`, coste aparte de la suscripción). (3) Raspa la Biblioteca de anuncios de Meta y el Creative Center de TikTok con un navegador
  (riesgo con sus términos de uso; la alternativa oficial es la herramienta `ads_library_search` del conector de Meta, que usa el estratega). (4) Su
  `contexto/LUNERIE.md` es una copia vieja (sin commit). (5) `data/.browser_profile` guarda la sesión de TikTok: está fuera de git, no subirla.
  Lo que enseñan los datos: los anuncios de joyería con más de 60 días son casi todos **vídeo + botón «Comprar»** con **contrareembolso, envío gratis,
  «últimas unidades» y emojis** (ZafiroMadrid 36 anuncios y 472 días; MF Watches 25 y 197). Lunerie hace lo contrario por diseño: hay hueco
  para un tono más sobrio. Pendiente: volver a ejecutar el radar con keywords de regalo y joyería.
- **29-oct: Publicación en Instagram por API (hecha, en producción).** Script **`oficina/publicar.py`**: `python oficina/publicar.py` lista lo `aprobado`;
  con un id hace un **ensayo** (sin red, sin publicar); con `--confirmar` publica y deja `estado: publicado` + `publicacion.resultado`. Solo publica piezas
  `aprobado` con material (`publicacion.archivos` o `publicacion.urls`, formato en `oficina/cola/ESQUEMA.md`). Convierte a JPEG y recorta a 4:5 (Instagram no admite
  más estrecho), aloja la imagen en **Archivos de Shopify** para tener URL pública (espera a que el CDN la sirva y reintenta si Instagram da el error 2207052) y marca
  la publicación como **hecha con IA** (`is_ai_generated`). Límites de la API: **no programa** (la hora la pone quien lanza el script), **no añade música**, los reels
  necesitan el MP4 ya público (`publicacion.urls`; sin hacer), carrusel con la misma proporción en todas las imágenes. **Probado de verdad:** 3 fotos publicadas el 29-oct en
  `@luneriejewelry`: mercado (`/p/DfFIJFGjpU6/`), terraza (`/p/DfFJlcdls6q/`) y metro (`/p/DfFJobvFlLy/`), todas con el OK de Edu al texto antes de publicar.
  **Montaje de Meta:** app de desarrollador id `2676185462837815` (cuenta «Lunerie Vega»), Facebook Login, **token de la PÁGINA «L U N E R I E»** (no caduca; sacado de un token de usuario
  largo con la clave de la app). Instagram `17841404549468255`. Las claves (`IG_TOKEN`, `IG_USER_ID`, `IG_HOST`, `META_APP_ID`, `META_APP_SECRET`) están **solo en `D:\LUNERIE\.env.local`** (git lo ignora; no se
  sincroniza entre los 2 PCs). **Regla: nunca claves en git ni en el chat** (Edu pegó el token y la clave secreta en el chat y pidió subir la clave a git «por si no la apunto»: no se hizo; se puede ver o
  restablecer en developers.facebook.com → app → Configuración → Básica; **recomendado restablecerla**, y si se restablece hay que repetir el intercambio del token). Perfil de Chrome para iniciar sesión en Meta
  con Playwright: `.claude/meta-perfil` (fuera de git; el inicio de sesión lo hace Edu, no Claude).
- **29-oct: contenido «reloj + joya en el día a día» (estilo juvenil con ojo de pez).** Referencia de Edu: vídeo «ideas de contenido, edición joyería» (la vida cotidiana, detrás de
  escena, comunidad, romper el patrón; se usan 1 y 4, y el 2 y 3 solo con cosas verdaderas). **Estilo y cómo se genera en `marca/estilo-contenido.md`**; script `marca/combinados.py`
  (escenas `metro-ojo`, `mercado`, `terraza`, `cafe`, `metro`, `pelo`; API de Higgsfield, ~0,13 $ por foto). **Saldo de la API: 18,31 $ (4-nov, por la noche**: quedaban 3,31 $ y Higgsfield regaló 15 $ por verificar el email; el 29-oct eran 8,73 $; 4K = 0,17 $ por foto; el detalle de cada cobro se ve en Higgsfield → transacciones); el conector de Higgsfield (Nano Banana) tiene
  **0,55 créditos** (2 por imagen): no se usa. **Lección: juzgar el color de las piedras del reloj en un recorte a tamaño real**, no en la vista reducida (parecían grises y son verde oscuro con vetas);
  el oro del reloj real es algo más pálido y rosado que el amarillo vivo que pinta la IA. Fotos en `marca/fotos-ia/combinados/` (los `.png` no van a git, los `.jpg` sí).
  Idea nueva de Edu (captura de @star.rreyai): **storyboard de 6 escenas UGC en una imagen 9:16 y luego vídeo siguiendo la secuencia, sin voz en off** (pendiente de probar; hay que ver el coste de animar por la API).
- **29-oct: competidor Caducci** (`oficina/referencias/competidores.md`): relojes pequeños vintage de mujer a 59,95-69,95 USD (tachado 79,95-92,95), web en inglés, escala en TikTok UE
  (campaña «CBO SCALING / EU-A»), 61,4 mil seguidores y 967 mil me gusta; ofrece pack «compra 2, llévate 2 + pulsera», caja de regalo, kit de ajuste de talla, cuenta atrás, «solo 50 piezas»,
  «waterproof / lifetime», «Designed in Italy», «135.000 clientes» y «looks like a Cartier». **Valida la categoría, no su rentabilidad** (sus ventas no se ven). **Decisión sobre estilo (Edu, 29-oct):** las reglas de
  «sin cuenta atrás / sin ¡oferta! / sin tachado» eran de estilo (apartado 3) y las puede cambiar Edu; **lo que no se escribe nunca** es lo falso o no comprobable: waterproof sin confirmar, escasez inventada («solo quedan 50»),
  reseñas o nº de clientes inventados, marcas ajenas. Sí valen packs, regalo con la compra, caja y tarjeta Lunerie, y **Black Friday real con cuenta atrás hasta el 30-nov y código de descuento**.
- **29-oct: campaña de Meta, diagnóstico y arreglos** (detalle en `oficina/informes/ads-2026-10-29*.md` y `ads-diagnostico-pixel-2026-10-29.md`): a las ~14 h, 36,29 € gastados, 0 pedidos y 0 checkouts
  abandonados desde el lanzamiento (los 6 abandonados son del 27-oct por la tarde, pruebas). **El píxel `1096538246614496` está bien enlazado** a la cuenta «LUNERIE PUBLI» y al conjunto (optimiza por compra) y la
  URL de destino es correcta (`lunerie.es/products/reloj-lune?utm_source=meta&…`); la página carga en 1,8 s con 4G. **Causas de que los clics no se midieran:** (1) el píxel no dispara hasta contestar el banner
  de cookies y en móvil el banner tapaba el 40 % de la primera pantalla → **banner compactado en móvil** (`tema/build.py`, sección `cookies` del pie; Aceptar y Rechazar iguales y lado a lado); (2) **el 69 % de los clics
  salientes (44 de 64) venía de Audience Network**, a 0,01 € y sin ninguna visita → **excluido el 29-oct (~19 h) con el OK de Edu**: conjunto `52564454188194` ahora solo Facebook e Instagram (quedó «IN_PROCESS» en
  revisión; comprobar que vuelve a Activo). Por eso las cifras de CTR/CPC de 28-29 oct y «el vídeo gana a la foto» **no son fiables**. En ubicaciones reales: ~20 clics salientes por ~21,8 € (~1,09 €/clic), CTR ~0,5 %, 4 visitas
  medidas. **El test no ha probado ni desmentido el producto** (pocos clics reales); la regla KILL (gasto > 2× breakeven sin ventas) se cumple en papel pero con datos contaminados. **Dominio `lunerie.es` verificado en Meta**
  (etiqueta `facebook-domain-verification` en `snippets/meta-tags.liquid`; no quitarla). Shopify (Sidekick): 9 sesiones con `utm_source=meta` desde el 28-oct, que coinciden con las 9 visitas de Meta y dependen del mismo
  banner. **Creativos (solo ubicaciones reales):** Para ti·foto 10 clics por 5,71 €, Regalo·vídeo 7 por 5,40 €, Para ti·vídeo 2, Estilo·vídeo 1, Estilo·foto 0, Regalo·foto 0; **no se apaga ninguno hasta pasadas las 48 h
  (30-oct mediodía) y con datos limpios**. **Pendiente de Edu:** decidir si pausa o deja correr (consejo: dejar hasta mañana), comprobar «Probar eventos» desde el móvil y que el conjunto vuelve a Activo.
- **29-oct: lo que enseñó el primer ciclo de la oficina.** `/oficina-semana` funcionó (estratega: 5 ideas en `oficina/ideas/2026-W44.md`; experto en ads: informes; community manager: piezas W46). Pixel Agents: los ganchos están
  instalados (`~/.claude/settings.json`, copia en `settings.json.pixel-agents.backup`); muestra **una persona por sesión de Claude Code abierta** (aparecen también las de otros proyectos: para ver solo Lunerie hay que cerrar esas
  ventanas). Piezas nuevas en la cola: W44-08/09/10 (mercado, terraza, metro; **ya publicadas**), W46-01..03. Posible bot de Telegram/WhatsApp para controlar la oficina desde el móvil: **aparcado por Edu**.
- **Siguiente con Claude:** apuntar cada día gasto, clics, carritos y
  compras en el radar (`cli.py test`) → vídeos reales de Edu como anuncios nuevos en el mismo conjunto → ~~opiniones
  de amigas~~ (hechas el 28-oct, apartado 6; falta el OK de cada una a su texto) → vídeo de 2 min ajustando la correa.

### Sesión del 25-27 oct
- **Hecho el 23-25 oct:** plateado (BS) puesto y quitado (difícil de encontrar) · skills de Instagram instaladas
  (`~/.claude/skills/ig-*`, del repo Jakeschincariol/instagram-agent-skill, revisadas: solo escriben, no publican;
  en este PC los scripts van con `python`, no `python3`) · collar recibido en 14 días, muy bien, con caja de
  terciopelo verde · **fotos IA del verde** con Higgsfield/Nano Banana (`marca/fotos-ia/`: modelo estilo Olivia con
  «NAIDU» en la esfera + muñeca), todavía **no subidas a la tienda**.
- **Higgsfield (25-oct):** prueba Plus de 3 días **activa** (2.º intento, con tarjeta; con Apple Pay no entró) →
  **109,3 créditos hasta el 28-oct 21:15** (hora de España); **renovación cancelada** (no se cobran los 49 €). Los
  créditos de la prueba solo se ven por el conector, no en la web. Con Plus también hay GPT Image 2.5. Después
  vuelve al plan gratis. API: con saldo desde el 28-oct (ver arriba); por imagen Qwen Edit 0,075 $, Grok 0,09 $
  (no tiene Nano Banana).
- **Hecho el 26-27 oct:** ficha solo en verde con fotos IA y sección estilo Olivia · anuncio 1 (Kling) · **portada
  con vídeo del Lune verde** (27-oct) y textos del inicio sin «seis colores» ni «llega en su caja» · galería de la
  ficha en cuadrícula (Edu) y sin la foto de 18 cm · **rasca del 10 %** (apartado 6).
- **27-oct:** fuera el «Segundo reloj por 19,95 €» y **precio a 49,95 €** (con el rasca, 44,96 €). Falta quitarlo
  de los anuncios (`anuncios/test-reloj-lune.md`: ángulo «Uno para ti y otro para regalar» y precio 44,95 €).
- **Formato de precio:** cambiado por Edu el 27-oct a `{{amount_with_comma_separator}} €` (sale «49,95 €»).

### Sesión del 22-oct
- **Hecho el 22-oct:** Reloj Lune unificado en 6 colores con fotos del proveedor y fase drop sin caja (apartado
  5.1a) · Higgsfield preparado (`.env.local`) · el conector de Shopify de claude.ai apunta a **Star Brick**: para
  Lunerie, solo la CLI.
- **Siguiente con Claude:** prueba de imágenes con Higgsfield (2 del verde: producto limpio en fondo niebla 4:5 +
  puesto en modelo, estética Olivia Jewelry) → si gusta, el resto de colores → fotos y vídeo de portada → montar
  los anuncios (`anuncios/test-reloj-lune.md`; ojo, sus textos aún dicen «llega en su caja» y «dorado o plateado»:
  ajustarlos a la fase drop) → quitar la contraseña y lanzar el test.
- **Edu:** formato de precio «44,95 €» · Instagram · borrar la página de Facebook antigua · regenerar la clave de
  Higgsfield · grabar los vídeos con las muestras (muñeca, dos colores, quitar eslabón) · recordar a Nihao el
  presupuesto de las cajas · llega la muestra NAIDU de Alibaba (~31 oct-4 nov) y el collar.

### Pendientes anteriores (14-16 oct)
- **Al abrir:** `git pull`. Shopify: el conector de claude.ai puede no cargar → usar `shopify store execute`
  (apartado 6); tema publicado = **209073799507**.
- **Esperando a Edu:**
  1. ~~Política de privacidad~~: subida la nuestra el 14-oct (gestión automática desactivada).
  2. **Dirección (14-oct): Edu deja la de su casa**, sin oficina virtual. Los textos dicen solo «41940 Tomares
     (Sevilla)»; la LSSI pide el domicilio completo → si Edu quiere, Claude la pone completa al subir (nunca en git).
  3. **Plazo de envío:** por definir cuando llegue la muestra (AliExpress dice ~14 días) → quitar [PLAZO] de envíos,
     FAQ y ficha del reloj (`build.py`).
  4. ~~Envíos~~ (15-oct: península gratis, Baleares 3,95 €, Canarias/Ceuta/Melilla fuera) · @lunerie en TikTok ·
     Meta listo (15-oct: porfolio Lunerie + cuenta «LUNERIE PUBLI» con pago + página + Instagram) → app
     Facebook & Instagram instalada → píxel asignado a LUNERIE PUBLI y probado (15-oct).
- **Prioridad (16-oct): darle caña al test.** Plan completo en **`anuncios/test-reloj-lune.md`**: lanzar en las 48 h
  siguientes a que llegue la muestra del BS (lista de lo que hacer ese día, fotos y vídeos a grabar, campaña ABO
  3 × 10 €/día y los textos de los 3 anuncios). Para montar la campaña desde aquí hace falta el conector
  «Meta ads Koco» cargado en la sesión (si no, Edu la crea en el Administrador de anuncios con ese fichero).
- **16-oct:** «Cómo es» de la portada reescrito («El reloj Lune, de cerca» · «Una esfera delicada»… sin decir de
  qué son las piedras).

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
- **No tocar el precio de 49,95 € (puesto el 27-oct) hasta Black Friday** (un tachado en BF tiene que ser el precio
  más bajo de los 30 días anteriores; del 27-oct al 27-nov son 31 días). Como el rasca da un 10 % a todo el que
  rasca, en BF es más seguro un **código** («−20 % con BLACK20») que un precio tachado.
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
