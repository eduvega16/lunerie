# Textos legales y páginas de Lunerie

**Subidos a Shopify el 12-oct** con `subir.py` (políticas en **Configuración → Políticas**, páginas «Envíos» y
«Preguntas frecuentes» en **Tienda online → Páginas**). Para volver a subir tras cambiar un texto:
`PYTHONIOENCODING=utf-8 LUNERIE_NOMBRE="…" LUNERIE_NIF="…" LUNERIE_DIRECCION="…" python legal/subir.py`
(los datos personales se piden a Edu o se leen del aviso legal publicado; no se guardan en el repositorio).
Privacidad subida el 14-oct (Edu desactivó la gestión automática de Shopify).
Decidido el 12-oct: Baleares con un pequeño coste de envío · devolución por desistimiento la paga el cliente; si
llega defectuoso, roto o equivocado, Lunerie · personalizados sin devolución salvo defecto. Sigue pendiente [PLAZO].

Huecos (los personales se rellenan solo al subir):

| Hueco | Qué poner |
|---|---|
| `[NOMBRE]` | Nombre y apellidos del titular (autónomo) o razón social |
| `[NIF]` | NIF / CIF |
| `[DIRECCIÓN]` | Domicilio fiscal completo |
| `[DIRECCIÓN DE DEVOLUCIONES]` | Dónde se reciben devoluciones en España (puede ser la misma) |
| `[PLAZO]` | Días laborables de entrega reales del proveedor (el radar estima 10-15) |
| `[BALEARES]` | Decisión pendiente: gratis / con coste / sin envío |
| `[QUIÉN PAGA LA DEVOLUCIÓN]` | Si el cliente paga el envío de vuelta (lo permite la ley si se avisa) o lo paga Lunerie |

| Fichero | Dónde va en Shopify |
|---|---|
| `aviso-legal.md` | Política «Aviso legal» (LSSI) |
| `devoluciones.md` | Política de reembolso |
| `envios.md` | Política de envío + página «Envíos» |
| `privacidad.md` | Política de privacidad |
| `terminos.md` | Términos del servicio (condiciones generales de venta) |
| `contacto.md` | Información de contacto |
| `preguntas-frecuentes.md` | Página «Preguntas frecuentes» |

Son borradores redactados por Claude, no por un abogado: conviene una revisión rápida antes de abrir la tienda.
