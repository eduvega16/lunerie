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

Si cambia un precio: `preparar.py` + volver a grabar los vídeos, y cambiar el precio en estos textos («desde 19,95 €»
del 10 es el más barato de la tienda hoy: aros Boucle y anillo Duo).

## Reglas (no cambian)
- KILL / ESCALAR como en CLAUDE.md, apartado 7, pero con el margen por pedido de la promo (~15-20 €): si a los 4 días
  no hay carritos, el problema no es el presupuesto.
- Nada de «últimas unidades», cuenta atrás inventada, «waterproof», opiniones de clientas inventadas ni marcas ajenas.
- Las fotos son de IA (escenas): las piezas y los precios son los reales de la tienda.
