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
- **PVP 49,95 € desde el 27-oct** (antes 44,95 €; subido un 10 % para compensar el rasca del 10 %: con el código,
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
  Blanco / Morado × Talla 12 / 14-15 / 17 · coste 3,34-4,71 € · **29,95 €**.
- **Pendientes Larme** `pendientes-larme` (11036461629779) · aro con lágrima · 7 colores · coste 1,88 € · **24,95 €**.
  La ficha de AliExpress no dice «Choice»: mirar el plazo a España.
- **Collar Lune** `collar-lune` (11036462121299) · cadena con piedras ovaladas, «a juego con el reloj» · De colores /
  Blanco · 45 + 6 cm · coste 4,93 € · **34,95 €**.
- **Anillo Étoile** `anillo-etoile` (11036462154067) · piedra del mes · Mes (12) × Talla · coste 3,82-4,36 € · **29,95 €**.
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
      la redacción son de Claude, así que **cada amiga tendría que dar el OK a su texto**. Se subieron con la CLI
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

## 8. Calendario y pendientes (a 27-oct-2026)

### Para empezar la próxima sesión (después del 27-oct) — abrir conversación nueva por sesión.
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
- **29-oct: diagnóstico del píxel** (`oficina/informes/ads-diagnostico-pixel-2026-10-29.md`): el píxel 1096538246614496 está bien enlazado a la cuenta y al conjunto de anuncios (optimiza por compra) y la URL de destino es correcta; la página carga rápido. El problema de medir clics: el píxel no dispara hasta contestar el banner de cookies y en móvil el banner tapaba el 40 % de la primera pantalla. **Banner compactado en móvil** (build.py, sección `cookies` del pie; Aceptar y Rechazar iguales). **Dominio lunerie.es verificado en Meta el 29-oct** (etiqueta meta en `snippets/meta-tags.liquid`; no quitarla). Pendiente de Edu: sesiones por UTM en Shopify.
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
  Primera semana de contenido: 7 piezas en `borrador` (`oficina/cola/2026-W45-*`), pendientes de tu OK de gasto: 0,91 $.
  **Aún no publica nada**: falta conectar la API oficial de Instagram y una pista de música con licencia. `.gitignore`: `.claude/agents/` y
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
