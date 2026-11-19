---
name: qiuhan-revisar-direccion
description: "QIUHAN copia el pedido de Alibaba anterior (dirección incluida): en cada pedido, comprobar dirección del pedido de Alibaba y etiqueta de Cainiao contra Shopify"
metadata:
  node_type: memory
  type: project
  originSessionId: b078affc-ce0c-4dbb-82ed-b99738b2b422
  modified: 2026-11-18T09:35:05.106Z
---

QIUHAN monta cada pedido de Alibaba copiando el anterior y contesta con mensajes de plantilla. El 16-nov, el pedido de
#LUN1008 (Marbella) salió con la dirección de #LUN1004 (León). Edu ya lo sospechaba.

**Why:** si se paga sin mirar, el collar personalizado va a la clienta equivocada, y como lleva nombre no se puede revender.

**How to apply:** cada vez que Edu pase un pedido de Alibaba o una etiqueta de Cainiao:
- Comparar destinatario, calle, código postal y teléfono con el pedido de Shopify (`shippingAddress` con la CLI).
- Revisar también nombres, piedras y el total (12 $ + 1 $ por pieza extra).
- Las direcciones solo en el chat, nunca en git.
- **La dirección del pedido de Alibaba (18-nov, Edu): no importa**, QIUHAN pone la de León (#LUN1004) por ir rápido
  y envía a la de su lista. No volver a avisar de eso; lo que se comprueba es la **etiqueta de Cainiao**.
- **En los mensajes a QIUHAN no pedir la foto ni la etiqueta** (Edu, 18-nov: «ya lo sabe»). Ellos la mandan solos;
  Claude la revisa cuando Edu la pase.

Relacionado: [[pedidos-por-instagram]].
