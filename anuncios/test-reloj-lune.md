# Test del reloj Lune · campaña de Meta

**Estado (cierre del 27-oct, noche):** campaña **rehecha al formato Advantage+**, **en borrador y SIN ACTIVAR** en
«LUNERIE PUBLI» (no gasta nada). Falta solo quitar las opiniones de ejemplo de la ficha: la tienda ya está abierta y
no se mandan anuncios a una página con opiniones inventadas. La campaña vieja (ABO) la borra Edu a mano.
Fase drop: solo el verde, 49,95 € (44,96 € con el rasca del 10 %), sin caja, entrega 7-12 días laborables.
Reglas de decisión: CLAUDE.md, apartados 5.1 y 7.

## 1. Antes de activarla (en este orden)

| Quién | Qué |
|---|---|
| Claude | Quitar las **opiniones de ejemplo** de la ficha (en cuanto Edu diga que su compañero ya las vio) |
| ~~Claude~~ | ~~Plazo del pago en 7-12 días~~ **Hecho el 27-oct** (pago probado: Madrid y Palma «5 nov-12 nov», Las Palmas sin envío) |
| Edu | Instagram **@luneriejewelry** (cambiado el 27-oct; nombre «Lunerie \| Relojes y joyas»): pegar la bio y los textos de `anuncios/instagram.md`, fijar 3 y archivar lo antiguo (los anuncios salen con esa cuenta) |
| ~~Edu~~ | ~~Quitar la contraseña de la tienda~~ **Hecho el 27-oct** (la tienda ya está abierta) |
| Edu | **Borrar la campaña vieja** «Lune · Test 90 € · Ventas (ABO)» (52564402827594) en el Administrador de anuncios: marcar solo esa → papelera. El conector no puede borrar una campaña que nunca se publicó |
| Claude | **Publicar solo la campaña nueva** con el conector (`ads_activate_entity` sobre 52564454147994, `publish_as_active=true`). No usar «Publicar» en el Administrador de anuncios mientras exista el borrador viejo |

## 2. Por qué está montada así (tendencia de Meta, octubre de 2026)

- Meta recomienda **campañas de ventas Advantage+**: presupuesto a nivel de campaña, público Advantage+ y
  ubicaciones automáticas. Según Meta, bajan de media un 9 % el coste por compra frente a campañas con restricciones.
- **No segmentar:** con el sistema de anuncios actual (Andromeda), Meta elige a quién enseñar cada anuncio según
  el propio anuncio. Los intereses y las edades estrechas le quitan margen. Lo que sí se fija: país, zonas sin
  envío y mayores de 18.
- **Pocos conjuntos y anuncios variados:** dividir 30 €/día en 3 conjuntos deja cada uno sin datos. Con un solo
  conjunto, Meta mueve el dinero al anuncio que funciona. La variedad tiene que estar en los anuncios (ángulos,
  escenas y formatos distintos), no en el público.
- Lo que cambia para leer el test: ya no se compara «conjunto contra conjunto». Se mira la campaña entera (¿vende
  el reloj?) y, dentro, qué anuncio se lleva el gasto y las ventas.

Fuentes: [Meta: Advantage+ sales campaigns](https://www.facebook.com/business/help/1362234537597370) ·
[Meta: volumen de anuncios](https://www.facebook.com/business/help/2720085414702598) ·
[Techsist Labs: presupuestos pequeños 2026](https://techsistlabs.com/insights/meta-ads-small-budgets-2026/) ·
[Skaleit: estructura tras Andromeda](https://skaleit.agency/blog/meta-ads-testing-structure-post-andromeda/) ·
[Superscale: CBO vs ABO 2026](https://superscale.ai/learn/cbo-vs-abo-advantage-plus/)

## 3. Campaña montada

- **Campaña:** «Lune · Lanzamiento · Ventas (Advantage+)» · id **52564454147994** · objetivo Ventas · compra del
  píxel 1096538246614496 · **30 €/día a nivel de campaña** (3 días = 90 €) · puja de volumen máximo, sin tope.
- **1 conjunto:** «España península y Baleares · abierto» (52564454188194) · España sin Canarias, Ceuta ni Melilla
  (excluidas con círculos sobre cada isla y ciudad: no enviamos allí) · 18+ · **sin edades, sexo ni intereses
  sugeridos** · ubicaciones automáticas · página «L U N E R I E» + Instagram luneriejewelry (antes lunerie_co; mismo id).
- **6 anuncios** (vídeo 9:16 + foto 4:5 de cada ángulo), botón **«Más información»** (Edu, 27-oct; antes
  «Comprar»), a
  `lunerie.es/products/reloj-lune?utm_source=meta&utm_medium=paid&utm_campaign=test-lune&utm_content=<ángulo>-<formato>`.
  **Los que corren** (28-oct, ~00 h): fotos «· v3» y vídeos «· v4 música»:

  | Anuncio | id |
  |---|---|
  | Regalo · vídeo · v4 música | 52564510681994 |
  | Regalo · foto · v3 | 52564508051194 |
  | Estilo · vídeo · v4 música | 52564510653794 |
  | Estilo · foto · v3 | 52564508048994 |
  | Para ti · vídeo · v4 música | 52564510638394 |
  | Para ti · foto · v3 | 52564507938794 |

  En pausa, con 0 € gastados: los 6 originales (sin «v2/v3»; Meta no los sacaba en 18 ubicaciones porque el
  título y la descripción iban también dentro del botón, un campo obsoleto), los 6 «· v2» (botón «Comprar») y
  los 3 vídeos «· v3» (sin música: 52564508053394, 52564508062194, 52564508065594).
- Mejoras automáticas de Meta (Advantage+ creativo) **desactivadas**: no reescribe los textos ni toca las fotos
  (se quedan así por la voz de marca). **Excepción: música automática de Meta (`audio`) activada en las 3 fotos**
  (Meta solo pone música a anuncios de foto: Reels, Historias y Feed de Instagram; en vídeo no se puede).
- **Música de los vídeos:** «Miracles» de Spatial (elegida por Edu el 27-oct; `marca/musica/miracles-spatial.m4a`,
  4 min, de Meta Sound Collection, confirmado por Edu). Mezclada en `test-lune/con-musica/*.mp4`: tramo desde
  **1:12** (Edu: «ese cachito es más suave»; 1:12-1:14 es el final de la parte fuerte y de 1:14 a 1:35 la suave),
  entrada 0,4 s, salida 1,5 s, −14 LUFS; la imagen no se toca. Primera mezcla (desde 0:21,85) descartada.
  **Al final no se usa:** Edu eligió otra (abajo). Se queda de recambio.
- **Música que va en los vídeos «· v4» (27-oct, ~23:55): `marca/musica/agua-mariano.mp3`** («Agua», Mariano;
  24,5 s). Ojo: el archivo es el audio de un TikTok bajado con ssstik.io y renombrado (mismo tamaño, hora y
  codificador), no una descarga de la biblioteca de Meta. Claude avisó del riesgo de derechos; **Edu dice que lo
  comprobó con una herramienta y no tiene copyright, y decidió usarla.** Si Meta silencia o rechaza un vídeo,
  cambiar a «Miracles» (`test-lune/con-musica/`). Mezcla en `test-lune/con-musica-agua/` desde el segundo 3,3
  (antes hay un fundido), −14 LUFS (el original venía a −33: subido ~19 dB). Subidos a Archivos de Shopify
  (`anuncio-lune-agua-*.mp4`; para Meta se usa `originalSource.url`, 1080×1920, porque las copias de Shopify
  bajan a 606×1080) y de ahí a Meta: vídeos 1663797128692857 (para ti), 1674516044056794 (estilo),
  1679453257127833 (regalo).
  Nada de canciones conocidas ni de TikTok (sin licencia para anuncios).
- **Aviso de IA:** Edu decidió no declararlo (27-oct).
- **Borrador viejo:** «Lune · Test 90 € · Ventas (ABO)» (52564402827594, 3 conjuntos × 10 €) sigue en borrador sin
  publicar. No publicarlo; borrarlo cuando Edu diga.
- **Creatividades** (`marca/fotos-ia/anuncios/test-lune/`; copias en Archivos de Shopify como `anuncio-lune-*`):
  - Regalo: vídeo toalla → macro → toalla → cielo con «LUNERIE» (10 s) · foto editorial de perfil.
  - Estilo: vídeo macro en ida y vuelta (10 s) · foto del reloj en curva sobre gris.
  - Para ti: vídeo toalla-a en ida y vuelta (12 s) · foto de la muñeca con jersey.
  - Solo clips donde el reloj se ve de su tamaño (en perfil y pelo de Kling sale demasiado grande).

## 4. Textos

Reglas: pocas palabras, sin emojis, sin «¡OFERTA!», sin cuenta atrás, sin «jade», «piedras preciosas» ni
«resistente al agua», sin precio tachado. Descripción en los tres: «Envío gratis a península».

| Ángulo | Texto principal | Titular |
|---|---|---|
| Regalo | Un reloj que se lleva como una joya. Esfera ovalada de 12 mm, piedras verdes y eslabones finos. Para Navidad, pídelo antes del 5 de diciembre. Y un 10 % de regalo en tu primer pedido. | Reloj Lune · 49,95 € |
| Estilo | Pequeño, ovalado y con piedras. Un aire vintage que se siente actual, para llevarlo cada día como una pulsera fina. Y un 10 % de regalo en tu primer pedido. | El reloj Lune · 49,95 € |
| Para ti | No hace falta esperar a que te lo regalen. Un reloj pequeño, con piedras verdes y eslabones finos, para llevarlo todos los días. Y un 10 % de regalo en tu primer pedido. | Para ti, el reloj Lune |

## 5. Después

- **Lo que más mueve la aguja ahora es la variedad de anuncios.** Los 6 actuales son de IA y casi todos con la
  misma escena (toalla). Los **vídeos reales de Edu** con la muestra (en la muñeca girándola, quitando un eslabón,
  abriendo el paquete) entran como **anuncios nuevos en el mismo conjunto**, sin tocar los que ya corren.
- **Cada día:** gasto, impresiones, clics, carritos y compras al radar (`cli.py test`). **No tocar nada las
  primeras 48 h** (ni presupuesto ni anuncios) salvo que la campaña pase de ~18 € sin un solo carrito.
- «Aprendizaje limitado» saldrá casi seguro: es normal con 30 €/día. No es motivo para cambiar nada.

| Situación (se mira en la campaña) | Qué se hace |
|---|---|
| ~18 € gastados sin carritos | Revisar la ficha y los anuncios; si nada falla, parar |
| ~36 € gastados sin ventas | Parar el test |
| Un anuncio con gasto y CTR < 1 % tras 48 h | Apagar ese anuncio y meter uno nuevo |
| CPC > 0,90 € en la campaña | Cambiar vídeos o textos |
| Coste por venta entre 12,5 y 17,9 € | Probar otras creatividades |
| ≥ 3 ventas a ≤ 12,5 € cada una | Escalar: subir el presupuesto de la campaña un 20 % cada 2-3 días |
