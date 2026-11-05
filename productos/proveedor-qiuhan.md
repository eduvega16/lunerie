# QIUHAN · proveedor del Collar Signé

Yiwu Qiuhan Jewelry Company Ltd. (Alibaba, producto 1601817911870). Datos de la ficha en CLAUDE.md, apartado 5.2.

## Lo que ha dicho (5-nov)
- **Acero 316L: 5,22 $/ud** mientras dure su descuento; después, **5,80 $** (unos 4,5 € y 5 € al cambio de ~0,86).
- Envío con **seguimiento**.
- Dropshipping: el paquete va **sin logos, sin factura y sin nada parecido** dentro.
- Cómo se trabaja: Edu le manda los pedidos **cada día por el chat** → ellos preparan una lista → Edu la confirma → fabrican y envían.

## Cuentas (calculadora del radar, pago con tarjeta, a 49,95 €)
Coste puesto en España = collar + envío estándar (4,33 € en la ficha de Alibaba; **sin confirmar** para pedidos sueltos).
El radar suma aparte 4,20 € de aranceles por paquete.

| Collar | Coste puesto | CPA breakeven | CPA objetivo (70 %) |
|---|---|---|---|
| 5,22 $ (≈ 4,5 €) | ≈ 8,8 € | **≈ 23,6 €** | ≈ 16,8 € |
| 5,80 $ (≈ 5,0 €) | ≈ 9,4 € | **≈ 22,9 €** | ≈ 16,1 € |

Mejor que el reloj Lune (~17,9 €). Cambia si el envío a España por pieza sale más caro de 4,33 €.

## Respuesta para mandar (en inglés)
Antes de mandarla, poner el nombre y el mes del pedido de prueba y adjuntar las fotos
`marca/referencias-reales/collar-signe-1.jpg` y `collar-signe-5.jpg` (la muestra de la otra fábrica).
La dirección de Edu va solo por el chat de Alibaba, nunca aquí.

```text
Hi friend, thank you! 316L at $5.22 is good for us. We want to start dropshipping with you now.
Before the first order, please confirm these points:

1. SHIPPING TO SPAIN, one piece to my customer: which shipping line, cost per piece, and days from
   shipment to delivery. It must be TAX INCLUDED (DDP / IOSS): my customer pays nothing on delivery.
2. PRODUCTION TIME: how many days from my confirmation to shipment?
3. CHRISTMAS: last day I can send you an order so it arrives in Spain before December 22
   (standard line). And the express price for 1 piece.
4. CHAIN: length and extender (we would like 45 cm + 5 cm extender).
5. PLATING: gold color is PVD or normal plating? Silver color is polished steel?
6. LETTERS: please make it exactly like the attached photos (sample from another factory):
   flat polished nameplate, signature font, tall capital letter, jump ring on the top of the
   capital, the last letter ends in a long straight line with a ring, and the teardrop stone
   (4 prongs) hangs in the center, 2-3 links after the name. Can you do it the same?
   Maximum letters? Can you make accents (á é í ó ú ñ)?
7. STONE COLORS: please send a real photo of your 12 birthstone teardrop colors.
8. PACKAGE: what is inside (bag or box)? Please no "THANK YOU" card, no logo, no invoice,
   no price. Do you have a gift box? Price?
9. Please send me a PHOTO of each necklace before shipping, so I can check the name.
10. TRACKING number in 48 hours after shipping, that works in Spain.
11. If a name is wrong because of a production mistake, you remake it for free. OK?
12. PAYMENT: how do I pay each list? Alibaba order with Trade Assurance is best for me.
13. Every day I will send: order number, name, color (gold/silver), month (stone color),
    customer name, address, postal code, city, phone. Is this OK?

TEST ORDER: I want to place 1 test order now, shipped to my address in Spain like a normal
customer: name "[NOMBRE]", gold, [MES] stone. Please tell me the total price with shipping.

Thank you!
```

### Lo mismo en español (para que Edu sepa qué manda)
Que el 316L a 5,22 $ nos vale y queremos empezar ya. Antes del primer pedido: (1) línea, precio y días del envío
de una pieza a España **con impuestos incluidos** (la clienta no paga nada al recibir); (2) días de fabricación;
(3) último día para que llegue antes del 22 de diciembre y precio del exprés de 1 pieza; (4) largo de cadena y
alargador; (5) baño del dorado y del plateado; (6) la letra igual que la muestra (fotos) y si hace tildes y eñes,
y cuántas letras como máximo; (7) foto real de sus 12 colores; (8) qué lleva el paquete, sin tarjeta «THANK YOU»,
logo, factura ni precio, y si tiene caja de regalo; (9) foto de cada collar antes de enviarlo; (10) seguimiento en
48 h; (11) si se equivocan con el nombre, lo rehacen gratis; (12) pagar cada lista con un pedido de Alibaba
(Trade Assurance); (13) los datos que le mandaremos cada día. Y un **pedido de prueba** a casa de Edu.

## Con la respuesta (lo hace Claude)
- Plazo y Navidad reales → `PLAZO_COLLAR` y `NAVIDAD_COLLAR` en `tema/build.py` (hoy «2-5 semanas» y «15 de
  noviembre», provisionales) → ficha, Preguntas frecuentes y el anuncio 14 de la campaña.
- Caja y tildes → ideas 4 y 7 de `oficina/ideas/2026-11-05-collar.md`.
- Tabla de colores → cambiar la lámina `marca/fotos-ia/lagrimas/lagrimas-12.jpg` (hoy, gotas de Olivia).
- Precio del envío → repetir las cuentas (`cli.py calc 49.95 <coste puesto> --modo tarjeta` en el radar).
- **Si no envía con impuestos incluidos (IOSS)**, Correos le cobra el IVA y la gestión a la clienta al
  entregar: buscar otra línea de envío con él antes de vender más collares.
