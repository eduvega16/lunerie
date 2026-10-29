# Diagnóstico del píxel y de los clics (29-oct-2026)

Pregunta de Edu: ¿está bien enlazada la cuenta de Meta al píxel y viceversa? ¿Por qué hay 117 clics salientes y solo 9 visitas a la página de destino?

## Lo que está bien (comprobado con el conector de Meta)
- **Píxel «Lunerie's pixel» 1096538246614496**: activo, creado el 15-oct, en el porfolio Lunerie (1639315480899561), con cookie propia y uso «publicidad y analítica».
- **Última señal del navegador y del servidor** el 29-oct por la mañana: llegan los dos canales (el del servidor es el de la app de Facebook e Instagram de Shopify).
- **La cuenta «LUNERIE PUBLI» 4565584937093443 lo tiene como único conjunto de datos** y el conjunto de anuncios «España península y Baleares · abierto» (52564454188194) usa ese mismo píxel con **optimización por compra** (`OFFSITE_CONVERSIONS`, evento `PURCHASE`). Enlazado en los dos sentidos.
- **URL de destino de los anuncios** correcta: `lunerie.es/products/reloj-lune?utm_source=meta&utm_medium=paid&utm_campaign=test-lune&utm_content=…`.
- Calidad de los eventos: 6,9/10 en PageView y 7,4/10 en ViewContent.
- Desde el 28-oct el píxel recibe PageView (~167) y ViewContent (~80); **no ha llegado ningún AddToCart ni InitiateCheckout**.

## Qué pasaba con los clics
- **La página no es lenta**: con 4G carga en 1,8 s (la foto principal en 0,7 s) y con una conexión mala, en 10,6 s (la foto en 2,7 s).
- **El píxel no dispara hasta que se contesta el banner de cookies** (comprobado: 0 peticiones a Meta antes de aceptar; al aceptar salen PageView y ViewContent; al rechazar, ninguna). Es lo correcto en la UE, pero quien llega desde Instagram y no toca el banner **no queda medido**.
- **En el móvil el banner ocupaba 360 px de 844** (más del 40 % de la primera pantalla) y tapaba título, precio y botón: invitaba a irse sin contestar. Esa es, con lo que he podido medir, la causa más probable de la distancia entre clics y visitas medidas. No es la única posible: no he podido ver las sesiones reales de Shopify (la CLI no tiene `read_reports`).

## Qué se cambió (29-oct, en producción)
- Banner compacto en móvil (alto de 360 a 184 px, mismo texto): «Aceptar» y «Rechazar» **del mismo tamaño y lado a lado**, «Administrar preferencias» debajo. El PC no cambia. Código en `tema/build.py` (sección `cookies` del pie).
- Comprobado: aceptar dispara el píxel y rechazar no.

## Pendiente de comprobar por Edu (yo no puedo)
1. **Shopify → Analíticas → Informes → Sesiones por fuente/UTM** desde el 28-oct: cuántas sesiones llegan con `utm_source=meta`. Eso no depende del banner y dice si el tráfico llega de verdad.
2. ~~Verificación del dominio `lunerie.es`~~ **Hecha el 29-oct** (etiqueta meta en la cabecera del tema; Edu pulsó «Verificar» y quedó verificado).
3. En el Administrador de eventos de Meta, abrir «Probar eventos» desde el móvil y comprobar que llegan PageView y ViewContent tras aceptar.

## Lectura
Con el banner arreglado se medirán más visitas, pero **eso no cambia por sí solo el resultado de ventas**: 0 pedidos en Shopify y 0 checkouts abandonados desde el lanzamiento. El número de clics (147) aún es pequeño para sacar conclusiones sobre la oferta.
