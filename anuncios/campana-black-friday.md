# Campaña Black Friday · Meta (preparada el 2-nov-2026)

Plan aprobado por Edu el 2-nov: **35 €/día × 4 días (~140 €)**, lanzar el **jueves 5-nov** y no tocar nada hasta el
**lunes 9-nov** (cada cambio manda el anuncio a revisión y reinicia el aprendizaje). El 9-nov: apagar lo que no traiga
clics baratos ni carritos y subir un 20 % el presupuesto si hay ventas.

Creatividades en `marca/fotos-ia/campana-bf/` (las genera `python marca/campana_bf.py`; precios leídos de la tienda).
Cada anuncio va en **4:5 para el feed y 9:16 para Reels/Stories** (en Meta: «Personalizar por ubicación»).

## Configuración
- **Campaña:** «Lunerie · Black Friday · Ventas (Advantage+)» · objetivo **Ventas** · presupuesto de campaña **35 €/día**.
- **Conjunto:** «España península y Baleares · abierto» · fuera Canarias, Ceuta y Melilla · 18+ · sin intereses ·
  evento **Compra** con el píxel `1096538246614496` · **ubicaciones: solo Facebook e Instagram** (Audience Network
  fuera: en el test se llevó el 69 % de los clics sin una sola visita).
- **Botón:** «Comprar» (los anuncios de joyería que más aguantan en España lo usan; antes llevábamos «Más información»).
- **Al crear por API:** el botón solo con `link`; título y descripción en su sitio (ver CLAUDE.md, 27-oct).
- **URL:** `https://lunerie.es/…?utm_source=meta&utm_medium=paid&utm_campaign=black-friday&utm_content=<id>`
- **Música:** ninguna en los archivos; la pone Meta (biblioteca con licencia) o Edu en la app.

## Antes de gastar (lista)
1. Desde el móvil, abrir la vista previa de un anuncio y pulsar: ver qué se ve en los 3 primeros segundos (banner de
   cookies + portada) y que la visita sale en Shopify (en el test, de 82 clics solo se midieron 11).
2. La campaña vieja «Lune · Lanzamiento» sigue en pausa: no reactivarla (dice 49,95 € y «10 % de regalo»).

## Anuncios

| # | id (`utm_content`) | Creatividad | Destino |
|---|---|---|---|
| 1 | `oferta-telefono` | `1-oferta-telefono-4x5/9x16.jpg` | inicio |
| 2 | `pack-a-juego` | `2-pack-a-juego-4x5/9x16.jpg` | inicio, en los packs (`/#lu-packs-t`) |
| 3 | `carrusel-navidad` | `3-carrusel-1…4` (4:5) | cada tarjeta a su producto; la 4.ª al inicio |
| 4 | `solo-da-la-hora` | `4-solo-da-la-hora-9x16.mp4` + `4-solo-da-la-hora-4x5.jpg` | `/products/reloj-lune` |
| 5 | `para-ti` | `5-para-ti-4x5/9x16.jpg` | `/products/reloj-lune` |
| 6 | `menos-de-40` | `6-menos-de-40-4x5/9x16.jpg` | inicio |
| 7 | `para-tu-madre` / `-hermana` / `-pareja` | `7-para-tu-*-4x5/9x16.jpg` | `/products/reloj-lune` |
| 8 | `oferta-video` | `8-oferta-navidad-9x16.mp4` (+ `1-oferta-telefono-4x5.jpg` en feed) | inicio |

Pendientes de los vídeos reales de Edu (se añaden en el mismo conjunto cuando estén): «¿No sabes qué regalarle?»,
«¿Te quedará grande?» (quitar un eslabón) y «Su nombre, su piedra» (collar con nombre, cuando esté en la tienda).

### Textos (sin emojis; solo lo que es verdad)

**1 · Oferta (teléfono)** · título: *2.ª pieza al 50 % · 3.ª gratis*
> Black Friday en Lunerie: la 2.ª pieza al 50 % y la 3.ª, gratis. Relojes pequeños y joyas con piedras de color, para
> regalar o para ti. Mezcla lo que quieras: el descuento se aplica solo en la cesta. Hasta el 5 de diciembre, el último
> día para que llegue en Navidad. Envío gratis a península.

**2 · Pack a juego** · título: *Reloj y collar Lune · 57,43 €*
> El reloj Lune y el collar Lune, con las mismas piedras ovaladas. Juntos, 57,43 € (74,90 € por separado): por Black
> Friday, la 2.ª pieza va al 50 %. Envío gratis a península.

**3 · Carrusel de Navidad** · títulos: el nombre de las piezas de cada foto · última: *2.ª al 50 % · 3.ª gratis*
> Tres ideas para regalar esta Navidad: relojes pequeños, anillos y pendientes en el mismo dorado. Black Friday: la 2.ª
> pieza al 50 % y la 3.ª, gratis, hasta el 5 de diciembre.

**4 · Un reloj que solo da la hora** · título: *Reloj Lune · 39,95 €*
> Un reloj que solo da la hora. Sin pantalla, sin avisos y sin tener que cargarlo. Esfera ovalada de 12 mm y piedras
> verdes, 39,95 €. Y por Black Friday, la 2.ª pieza al 50 %.

**5 · Para ti** · título: *Para ti, el reloj Lune*
> No hace falta esperar a que te lo regalen. Un reloj pequeño, con piedras verdes y eslabones finos, para llevarlo todos
> los días. 39,95 € y envío gratis a península.

**6 · Regalos de menos de 40 €** · título: *Regalos de menos de 40 €*
> Regalos de menos de 40 € para esta Navidad: relojes pequeños, aros, pendientes y un collar con piedras de color.
> Black Friday: la 2.ª pieza al 50 % y la 3.ª, gratis.

**7 · Para tu madre / hermana / pareja** · título: *Para tu madre* (o *hermana*, *pareja*)
> Si no sabes qué regalarle: un reloj pequeño, con piedras verdes, que se lleva como una joya. 39,95 €, envío gratis a
> península y 14 días para devolverlo.

**8 · Vídeo de la oferta** · mismo texto y título que el 1.

### Anuncios animados nuevos (4-nov, HyperFrames, sin créditos de IA)

Formatos de `biblioteca/formatos-anuncio.json`, hechos con código en `marca/anuncios-hf/` (un `.html` por anuncio;
`python marca/anuncios-hf/preparar.py` vuelve a leer fotos y precios de la tienda y luego
`npx hyperframes render -c <anuncio>.html`). Salen en `marca/fotos-ia/campana-bf/` en **9:16** (Reels/Stories) y
**4:5** (feed, recorte del mismo vídeo). Sin música (la pone Meta). Las fotos de fondo de 9 y 11 son de IA.

| # | id (`utm_content`) | Creatividad | Destino |
|---|---|---|---|
| 9 | `bloqueo` | `9-bloqueo-9x16/4x5.mp4` (pantalla de bloqueo con avisos) | inicio |
| 10 | `notas` | `10-notas-9x16/4x5.mp4` (lista de regalos en las notas del móvil) | inicio |
| 11 | `lo-sentimos` | `11-lo-sentimos-9x16/4x5.mp4` («Lo sentimos, mamá. Este año no es colonia.») | `/products/reloj-lune` |
| 12 | `piezas-cayendo` | `12-piezas-cayendo-9x16/4x5.mp4` (collar, reloj y anillo caen, como el de SAVA) | inicio |
| 13 | `pack-video` | `13-pack-a-juego-9x16/4x5.mp4` (tarjeta del pack y botón) | inicio, en los packs (`/#lu-packs-t`) |

**9 · Pantalla de bloqueo** · título: *La 3.ª pieza, gratis*
> «Este año no me regales nada.» Ya. Black Friday en Lunerie: la 2.ª pieza al 50 % y la 3.ª, gratis, mezclando relojes
> y joyas. Hasta el 5 de diciembre, el último día para que llegue en Navidad. Envío gratis a península.

**10 · Notas del móvil** · título: *Tu lista de regalos, resuelta*
> Mamá, tu hermana, la amiga invisible… y algo para ti. Relojes pequeños y joyas con piedras de color desde 19,95 €. Por
> Black Friday, la 2.ª pieza al 50 % y la 3.ª, gratis. Hasta el 5 de diciembre.

**11 · Lo sentimos, mamá** · título: *Reloj Lune · 39,95 €*
> Este año, ni colonia ni pijama: el reloj Lune. Pequeño, ovalado y con seis piedras verdes; se lleva como una joya.
> 39,95 € y, por Black Friday, la 2.ª pieza al 50 %. Envío gratis a península.

**12 · Piezas cayendo** · título: *3x2 en relojes y joyas*
> El collar Lune, el reloj Lune y el anillo Nuit. Black Friday: la 2.ª pieza al 50 % y la 3.ª, gratis. Mezcla lo que
> quieras: el descuento se aplica solo en la cesta. Hasta el 5 de diciembre.

**13 · Pack a juego (vídeo)** · título: *Reloj y collar Lune · 57,43 €*
> Las mismas piedras ovaladas en el reloj y en el collar. Juntos, 57,43 € (74,90 € por separado), porque por Black
> Friday la 2.ª pieza va al 50 %. Envío gratis a península.

**14 · Collar Signé · «Su nombre, su piedra»** (carrusel de las 4 fotos IA de la ficha: Marta, Carmen, Elena,
Paula; **nunca las de Olivia**, son de otra marca) · destino `/products/collar-signe` · `utm_content=collar-signe`
> Su nombre en letra de firma y una lágrima del color de su mes. El Collar Signé, en dorado o plateado, 49,95 €. Se
> hace para ella con el nombre que escribas. Y por Black Friday, la 2.ª pieza al 50 %.
(5-nov, Edu: «quita lo del plazo de entrega por ahora»: fuera «llega en 2-5 semanas… antes del 15 de noviembre»;
creatividad nueva 1843881623619209 con las mismas 4 fotos y títulos. Ya no hay que pausarlo el 15-nov.)
Tarjetas: «Su nombre, en letra de firma» · «Y la piedra de su mes» · «En dorado o plateado» · «Collar Signé · 49,95 €».

**16 · Collar Signé · UGC con voz** (5-nov, Edu: «la de Sarah me mola, súbela y ponla en anuncios»). Vídeo 16 s de una
chica de IA enseñando el collar «Marta» dorado con lágrima azul, voz en off de ElevenLabs (Sarah) y subtítulos
(`marca/fotos-ia/ugc-collar/collar-ugc-sarah-9x16.mp4` y `-4x5.mp4`) · destino `/products/collar-signe` ·
`utm_content=collar-ugc` · título: *Collar Signé · 49,95 €*
> Su nombre en letra de firma y una lágrima del color de su mes. El Collar Signé, en dorado o plateado, 49,95 €. Se
> hace para ella con el nombre que escribas. Y por Black Friday, la 2.ª pieza al 50 %.
Sin plazo ni fecha de Navidad (no confirmados). Sin declarar IA (decisión de Edu para la campaña).

**18 · Collar Signé · UGC Carmen luz dorada** (5-nov, Edu: «me flipa»; «ese es el audio, móntalo todo»). Vídeo de 15 s con
ideas de Pinterest: el collar «Carmen» (dorado, lágrima verde pequeña) colgando de los dedos, en la palma, abrochándolo y
selfie en el espejo; voz de Silvia (ElevenLabs) con filtro de móvil y música «Holiday Bells» (`marca/musica/`, de Edu)
mezclada con `marca/con_musica.py` · destino `/products/collar-signe` · `utm_content=collar-carmen` · título *Collar Signé · 49,95 €*
> Imagina su cara cuando vea su nombre. El Collar Signé lleva su nombre en letra de firma y una lágrima pequeña del color
> de su mes. En dorado o plateado, 49,95 €. Y por Black Friday, la 2.ª pieza al 50 %.

**19 · Collar Signé · Carmen palma** y **20 · Collar Signé · Carmen Black Friday** (7-nov, OK de Edu): variantes del 18
con **un solo cambio** cada una (idea del asistente de Meta, corregida: nada de «no se oscurece» sin confirmar ni «−30 %»,
que no existe). Mismos clips, voz, música, texto y título que el 18, pero con el botón **«Más información»** (Edu, 7-nov; el 18 sigue con «Comprar»). Montaje: `marca/ugc_montaje.py` con
`--salida palma` (planos `palma-1:2.4,colgando-1:4,cierre-1:2.6,espejo-1:4`) y `--salida bf --tarjeta bf`; música con
`con_musica.py`; 4:5 = recorte `crop=1080:1350:0:165`. Vídeos en `marca/fotos-ia/campana-bf/19-*` y `20-*`.
- 19: empieza con el collar en la palma (en vez de colgando de los dedos) · `utm_content=collar-carmen-palma`
- 20: tarjeta final con «BLACK FRIDAY · 2.ª pieza al 50 % · 3.ª gratis · Hasta el 5 de diciembre» · `utm_content=collar-carmen-bf`
- **Variante A, guardada** (`collar-ugc-silvia-hook-movil-*`): empieza con «¿Y si este año le regalas su nombre?». Edu la deja
  para cuando el proveedor confirme por escrito la calidad (material, baño, si se oscurece, agua): entonces se rehace con esos datos.

**21 · Collar Signé · UGC madre e hija** y **22 · Collar Signé · UGC dos hijas** (9-nov, OK de Edu tras verlos). Vídeos de
`marca/ugc_familia.py` con voz de Silvia y «Holiday Bells» (`marca/fotos-ia/ugc-madre-hija/` y `ugc-dos-hijas/`; copias en
`campana-bf/21-*` y `22-*`). Objetivo: **subir el valor del pedido con la promo** (2 o 3 collares). Botón «Comprar», destino
`/products/collar-signe`, 4:5 en el feed y 9:16 en Stories/Reels, sin declarar IA (como el resto de la campaña).
- 21 · `utm_content=collar-madre-hija` · título *2 Collares Signé · 74,93 €*
> Uno para ti y otro para tu hija. El Collar Signé lleva su nombre en letra de firma y una lágrima del color de su mes. Por
> Black Friday, el segundo te sale a mitad de precio: los dos por 74,93 €.
- 22 · `utm_content=collar-dos-hijas` · título *3 Collares Signé · 99,90 €*
> ¿Tienes dos hijas? Tres Collares Signé, cada uno con su nombre en letra de firma y la lágrima de su mes. Por Black Friday,
> el tercero es gratis: los tres por 99,90 €.

**23, 24 y 25 · MOFU y BOFU del Collar Signé (9-nov, PREPARADOS, SIN SUBIR).** Salen del embudo TOFU/MOFU/BOFU
(`biblioteca/funnel-meta.json`): el 18, 21 y 22 atraen (TOFU) y faltaba quitar dudas (MOFU) y cerrar (BOFU), que es donde
se atasca (muchos carritos, pocas compras). Sin créditos de IA: `python marca/grabar_vista_previa.py [Nombre] [Mes]`
(capturas de la ficha real en el móvil) → `python marca/mofu_bofu.py`. **Entran con la revisión del 11-nov y el OK de Edu**,
para no mezclarlos con la medición de la cesta nueva. Destino `/products/collar-signe`, sin declarar IA.
- **23 · Cierre (BOFU)** · estático `23-cierre-4x5.jpg` + `-9x16.jpg` · botón «Comprar» · `utm_content=collar-cierre` ·
  título *Collar Signé · 49,95 €*
> Su nombre en letra de firma y la lágrima de su mes. Por Black Friday, la 2.ª pieza al 50 % y la 3.ª, gratis: dos collares
> por 74,93 € o tres por 99,90 €. Hasta el 5 de diciembre. Garantía de 3 años y envío gratis a península.
  **Versión animada (idea de Edu):** `23-cierre-anim-9x16.mp4` / `-4x5.mp4` (6,5 s, `python marca/cierre_animado.py`): el collar baja desde arriba como si lo bajara una mano, se para con un rebote, la lágrima se balancea y entra el texto. Es la foto real animada por partes (sin IA, el nombre no se deforma). Mismo texto y destino; si se sube, mejor como vídeo que el estático.
- **24 · Dudas (MOFU)** · carrusel de 6 tarjetas 4:5 `24-dudas-1..6.jpg` (portada · ¿y si me equivoco con el nombre? ·
  ¿qué piedra? · ¿cuánto tarda? · ¿y si algo no está bien? · la oferta) · botón «Más información» · `utm_content=collar-dudas`
  · título *Collar Signé · 49,95 €*. Subir antes cada foto con `ads_creative_upload_media` y usar `image_hash`.
> Lo que más nos preguntáis antes de regalarlo: el nombre lo ves escrito antes de pagar, la lágrima es la de su mes, sale en
> 3-5 días laborables y tiene 3 años de garantía.
- **25 · Vista previa (MOFU)** · grabación de pantalla 11 s `25-vista-previa-9x16.mp4` + `-4x5.mp4` (elegir la piedra →
  escribir «Carmen» → «Revísalo antes de pagar» → tarjeta de cierre), sin sonido (música de Meta) · botón «Comprar» ·
  `utm_content=collar-vista-previa` · título *Escribe su nombre y míralo*
> Escribe su nombre y míralo en letra de firma antes de pagar. Elige la lágrima de su mes y listo: se hace tal cual lo
> escribes y sale en 3-5 días laborables. Por Black Friday, la 2.ª pieza al 50 %.
- **No dicen:** la suma de plazos ni fechas, «se graba a mano», material o «no se oscurece» (sin confirmar por QIUHAN), ni
  que la letra de la vista previa sea la exacta (es «orientativa», y sale escrito en la captura).
- Pendiente con la foto real de QIUHAN (#LUN1004): el carrusel «Así se hace tu collar» (escribes → eliges → se hace → foto
  antes de enviarlo), si Edu decide prometer esa foto a las clientas.

Si cambia un precio: `preparar.py` + volver a grabar los vídeos, y cambiar el precio en estos textos («desde 19,95 €»
del 10 es el más barato de la tienda hoy: aros Boucle y anillo Duo).

## Reglas (no cambian)
- KILL / ESCALAR como en CLAUDE.md, apartado 7, pero con el margen por pedido de la promo (~15-20 €): si a los 4 días
  no hay carritos, el problema no es el presupuesto.
- Nada de «últimas unidades», cuenta atrás inventada, «waterproof», opiniones de clientas inventadas ni marcas ajenas.
- Las fotos son de IA (escenas): las piezas y los precios son los reales de la tienda.

## Relanzamiento (11-nov, OK de Edu)

Campaña reactivada a **15 €/día**, tope de gasto **300 €** (llevaba 199,29 €). Solo 4 anuncios: **18** (Carmen), **21**
(madre e hija) y dos nuevos, los dos con voz de Silvia (ElevenLabs, filtro móvil) + «Holiday Bells», 4:5 en feed y 9:16
en Stories/Reels, botón «Comprar», título *Collar Signé · 49,95 €*:

- **28 · De cerca** (`marca/reel_macro.py --oro18` + `marca/doblar.py` + `marca/con_musica.py --bajo 11`):
  la chica abrochándolo → primeros planos del nombre y la lágrima (foto 4K) → mano → 12 lágrimas → collar cayendo con
  «El 3.º, gratis · hasta el 5 de diciembre». `utm_content=collar-de-cerca`.
  Texto: «Te van a preguntar de dónde es. / Su nombre en letra de firma y una lágrima del color de su mes. Acero con
  baño de oro de 18K, garantía de 3 años y su cajita de regalo. / Black Friday: el 3.º collar, gratis. Hasta el 5 de
  diciembre.»
- **29 · UGC Sarah** (`marca/reel_ugc_sarah.py`): Sarah con «Marta» azul y el mismo final. `utm_content=collar-sarah`.

Estructura copiada (no el vídeo) del anuncio de Lucce Jewelry (Biblioteca de Meta 911578845041121). «Baño de oro de
18K» confirmado por QIUHAN por escrito el 11-nov; **nada de waterproof** (0,03 micras). Regla: ~42 € sin ventas →
parar; ≤ 30 €/pedido → subir un 20 % cada 2-3 días.
