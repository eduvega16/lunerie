---
name: meta-ads-lecciones
description: "Lecciones de la campaña de Meta de Lunerie (Audience Network, banner de cookies, qué cifras fiarse) y cómo hablar de estilo vs. mentiras con Edu"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 7f0dea43-fb2c-4818-be0a-6d3b8cbd08f2
  modified: 2026-11-14T22:32:07.445Z
---

**Audience Network ensucia las cifras.** Con ubicaciones automáticas, el 69 % de los clics salientes del 28-29 oct venía de Audience Network (0,01 € por clic, 0 visitas). Excluido el 29-oct (conjunto solo Facebook e Instagram). Al crear conjuntos nuevos: ubicaciones manuales Facebook + Instagram desde el principio, y mirar siempre el desglose por plataforma antes de sacar conclusiones de CTR/CPC o de vídeo contra foto.

**Why:** Edu se enfadó («vaya cagada»); el riesgo no se señaló al montar la campaña y las primeras lecturas (también las del agente experto-ads) concluyeron cosas falsas.

**How to apply:** revisar el desglose por ubicación en cualquier informe de ads; desconfiar de CTR altos con CPC de céntimos. El píxel de Meta no dispara hasta contestar el banner de cookies (UE), así que «visitas a la página» infravalora; el banner en móvil debe ser compacto (Aceptar y Rechazar iguales).

**Estilo vs. verdad.** Cuando Edu pidió copiar tácticas de un competidor (cuenta atrás, escasez, «waterproof»), respondí con una lista de prohibiciones y se enfadó («menudo experto de mierda»). Lo que funcionó: separar (1) reglas de **estilo** que son suyas y puede cambiar (cuenta atrás, ¡oferta!, tachado real, packs) y se hacen si él lo decide, de (2) lo que **no se escribe** por falso o ilegal (waterproof sin confirmar, escasez inventada, reseñas o cifras de clientes inventadas, marcas ajenas), y ofrecer alternativas reales para vender (packs, regalo con la compra, caja, Black Friday real con fecha). Nada de sermones: una línea de motivo y pasar a lo que sí se puede hacer.

**Urgencia (18-nov):** Edu pidió urgencia «aunque sea un poco mentira» (alta demanda, «4 pedidos la última hora»). Funcionó
contestar en una línea que lo inventado es publicidad engañosa y ofrecer en el acto la urgencia verdadera: cuenta atrás hasta
el fin real de la promo, «después vuelve a su precio» (si de verdad vuelve) y «pídelo ahora y llega para Navidad» sin fecha.
Lo aceptó a la primera («dale») y pidió integrarla en ficha y cesta.

**Ofertas (2-nov):** Edu quiere vender fuerte y pronto («se sabe que se vende aunque no sea el 29 de noviembre»):
aceptó llamar «Black Friday» a la promo desde el 2-nov, con una sola frase («2.ª pieza al 50 % y la 3.ª, gratis») y
una fecha de fin real (5-dic) puesta también en Shopify. Proponerle siempre la versión comercial que sea verdad, no
la más prudente.

**Antes de prometer «lanzo la campaña»:** comprobar al empezar que el conector «Meta ads Koco» está cargado en la
sesión (el 2-nov no lo estaba y hubo que dejarle la campaña preparada). En 9:16, el texto de los anuncios entre el
14 % de arriba y el 35 % de abajo, sin tapar la pieza.

**Montar campañas con el conector (4-nov, la de Black Friday, 16 anuncios):** el conector trabaja en **borrador**
(nada gasta hasta `ads_activate_entity`). Los archivos se suben a Archivos de Shopify (`anuncios/subir_creatividades.py`) y
Meta los baja por URL. En **carruseles** usar `image_hash` (subir antes con `ads_creative_upload_media`): con `image_url`
Meta lo rechaza al publicar. Poner siempre un **tope de gasto** (`spend_cap`) igual al plan aprobado antes de publicar.
Revisar el borrador entero (`object_state=draft`) sin errores antes de publicar. Declarar IA en el anuncio: Edu dijo que no.

**Cambiar un anuncio activo (5-nov):**
1. Crear una creatividad nueva con `ads_create_creative`.
2. Asignarla con `ads_update_entity` y `{"creative":{"creative_id":…}}`. Queda en borrador.
3. Publicar con `ads_activate_entity` y `object_ids=[ad]`. Hay que añadir `publish_as_active=true` si estaba en pausa.

El anuncio vuelve a revisión y reinicia su aprendizaje. Pausar (`{"status":"PAUSED"}`) se aplica al momento.

El asistente de Meta del Administrador puede no contar el día en curso: comprobar con el conector.

**Consejos del asistente de Meta (7-nov):** Edu pega sus respuestas para que las comente. Hay que separar lo útil de lo que no vale:
- Lo útil: variantes de un anuncio que funciona, cambiando una sola cosa cada vez. Salen gratis montando los mismos clips con `ugc_montaje.py`.
- Lo que no vale:
  - Ignora el tope de gasto (`spend_cap`).
  - Pide «unas 50 compras por conjunto» y «70 € sin compra», reglas de cuentas grandes. Usar las de CLAUDE.md, apartado 7.
  - Propone textos falsos («no se oscurece» sin confirmar, «−30 %» que no existe). Cambiarlos por la oferta real.

**Cambiar el botón o el texto de un anuncio publicado** es una creatividad nueva: vuelve a revisión, pierde lo aprendido y los me gusta. En anuncios recién creados, en revisión, no cuesta nada. El 7-nov Edu quiso «Más información» en vez de «Comprar» y decidió no tocar el 18, que es el que vende. Avisarle de esto antes de tocar un anuncio que va bien. Edu quiere ver el vídeo antes de subirlo ([[ensenar-antes-de-subir]]).

**¿Anuncio u orgánico? (14-nov):** en Shopify, «Instagram» o «Facebook» como origen de un pedido es la app desde la que
llegó, no quiere decir orgánico. Lo que decide son las UTM de la visita (`customerJourneySummary` del pedido con
`shopify store execute`): si lleva `utm_medium=paid` y un `utm_content` de anuncio (p. ej. `collar-carmen`), vino del
anuncio, porque lo orgánico no puede traer esas etiquetas (enlaces de posts no clicables, bio sin UTM). Cruzarlo con las
compras por anuncio en Meta. Así se vio que las 3 ventas reales (#LUN1004, 1006 y 1007) son del anuncio 18.

**Prueba de creatividades (18-nov, reel de AgenciaTech que trajo Edu):** con varios anuncios en un conjunto, Meta mete casi
todo en uno (el 18) y los demás no se prueban. La prueba de creatividades reparte un presupuesto aparte a partes iguales
entre 2-7 anuncios dentro de la misma campaña, sin reiniciar el aprendizaje; no se puede cambiar una vez empezada y empieza
como pronto al día siguiente. El conector la crea con `ads_experiment_abtest_create_test` (celdas = ids de anuncio) y la
cuenta es apta (`ads_experiment_check_eligibility`). Con nuestro presupuesto no da para decidir por compras: elegir como
KPI el coste por pago iniciado (`cost_per_action_type:omni_initiated_checkout`) y mirar compras y carritos de secundarios.
Crearla solo con el OK de Edu (es gasto).

Relacionado: [[instagram-publicacion-api]], [[estilo-contenido-juvenil]], [[oficina-lunerie]].
