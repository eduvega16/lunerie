---
name: pedidos-por-instagram
description: "Clienta que pide por DM: enlace de pago con una cesta de la Storefront API (cartCreate) con el nombre de cada collar; la promo entra sola"
metadata:
  node_type: memory
  type: reference
  originSessionId: b078affc-ce0c-4dbb-82ed-b99738b2b422
  modified: 2026-11-16T21:42:49.981Z
---

Si una clienta pide por Instagram, el enlace de pago es una cesta creada con la Storefront API, sin token:
`POST https://lunerie.es/api/2025-07/graphql.json` con `cartCreate`. Cada línea lleva su variante y
`attributes: [{key: "Nombre", value: …}]`, y `buyerIdentity.countryCode: "ES"`. Se le manda el `checkoutUrl`. Los
descuentos automáticos (3x2, 2.ª al 50 %) se aplican solos y el pedido entra con el nombre de cada collar, como desde
la ficha.

**Why:** el 15-nov (3 Collares Signé, 79,80 €) la CLI no tenía permiso para borradores de pedido (`draftOrders` →
ACCESS_DENIED).

**How to apply:**
- Comprobar el total en la respuesta antes de dárselo a Edu.
- Si Edu abre el enlace, no pasa nada: su navegador comparte esa misma cesta. Que no la vacíe ni la cambie.
- La cesta caduca a los ~10 días sin tocarla.
- Si la clienta paga: a QIUHAN «urgente, 3-5 días» con nombre y piedra.
- Los emails de las clientas no se guardan en git.

**Interesadas que preguntan por DM:**
- 16-nov: una chica respondió al reel «Carmen en la palma» con «¿qué precio?, ¿solo hay ese modelo y color?».
- Es el segundo contacto por DM. El otro fue #LUN1008, que acabó pagando con el enlace.
- Se le contesta con todo en un mensaje: precio y promo, dorado o plateado, las 12 lágrimas, el nombre que quiera, la
  cajita, los plazos por separado, el envío y la garantía.
- Se le ofrece hacerle la cesta, con el enlace de la ficha por si prefiere hacerlo ella.
- Los DMs convierten mejor que la cesta: contestar pronto.

Relacionado: [[mensajes-clientas]].
