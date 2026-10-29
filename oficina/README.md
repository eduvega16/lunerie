# La oficina de Lunerie

Equipo de agentes de Claude Code que trabaja el contenido y los anuncios de Lunerie. **Edu aprueba; los agentes proponen y preparan.**
Creada el 29-oct-2026. Los agentes viven en `.claude/agents/` y el ciclo semanal es el comando `/oficina-semana`.

```
 radar (05_producto_ganador)        biblioteca/ (hooks, skills)
          │ lectura                         │
          ▼                                 ▼
   ESTRATEGA CREATIVO ──ideas──► COMMUNITY MANAGER ──piezas──► EDITOR DE VÍDEO
   oficina/ideas/                oficina/cola/                 oficina/salida/
                                       │                              │
   EXPERTO EN ADS ──informe──► oficina/informes/                      │
   (solo lectura de Meta)              ▼                              ▼
                                  EDU REVISA Y APRUEBA  ◄─────────────┘
                                       │  estado: aprobado
                                       ▼
                               publicar (a mano o, más adelante, por la API de Instagram)
```

## Los cuatro roles
| Rol | Qué hace | Qué NO puede hacer |
|---|---|---|
| **Estratega creativo** | Busca ideas: competencia (radar + Biblioteca de anuncios de Meta), biblioteca de ganchos, tendencias | Producir piezas, publicar, gastar |
| **Community manager** | Convierte ideas en piezas (copy, guion, hashtags, assets) en la cola | Publicar, generar con créditos sin tu OK de coste |
| **Editor de vídeo** | Monta reels y anuncios con ffmpeg (`marca/montaje.py`): cortes, logo y música con licencia | Publicar, generar clips con IA |
| **Experto en ads** | Lee la campaña y la compara con las reglas KILL/ESCALAR | **Tocar presupuestos, pausar, activar o crear anuncios** (solo tiene herramientas de lectura) |

## Reglas de la oficina
1. **Nada se publica sin `estado: aprobado`**, que solo pone Edu (o Claude cuando Edu lo dice).
2. **El dinero lo confirma Edu**: presupuesto de anuncios, créditos de IA y cualquier compra. Los agentes declaran el coste, no lo gastan.
3. **Marca** (CLAUDE.md, apartado 3): pocas palabras, cálida, sin emojis, sin «¡OFERTA!», sin contadores, sin urgencia falsa.
4. **Legal** (apartado 4): nada de oro, piedras preciosas, waterproof ni hipoalergénico; el reloj no es sumergible; plazos y garantías reales.
5. **Nada inventado**: ni testimonios ni reseñas, ni siquiera «de ejemplo». La leyenda del castillo es un cuento («cuentan que…»), nunca un dato.
6. De la competencia se copia la **forma** (estructura, formato, gancho), nunca el texto ni sus promesas.
7. **Música con licencia.** Una pista comercial sin derechos puede tumbar un anuncio o la cuenta. Opciones: pista libre con licencia comercial (apuntar nombre y licencia
   en la pieza) o, en anuncios, la música de la biblioteca de Meta que Edu añade dentro de la app. La API de Instagram no permite la música de tendencia.
8. **Etiqueta de IA**: Meta marca como «hecho con IA» lo que lo parece. Las imágenes tienen que ser fieles al producto real.
9. Dos cuentas que nunca se mezclan: aquí solo la cuenta publicitaria «LUNERIE PUBLI» (4565584937093443). LaFortuna no es de este proyecto.

## Carpetas
- `ideas/` · propuestas del estratega (`AAAA-Wss.md`).
- `cola/` · una pieza por fichero JSON; formato en `cola/ESQUEMA.md`.
- `salida/` · vídeos montados (no va a git).
- `informes/` · informes del experto en ads.
- `referencias/` · datos del radar sobre la competencia (se regeneran con `python oficina/radar_a_oficina.py`).

## El radar (05_producto_ganador)
Proyecto aparte en `D:\aura-ai-portfolio\projects\05_producto_ganador`. La oficina **solo lee** su base de datos (`radar_a_oficina.py`, en modo solo lectura).
Hoy aporta ~177 anuncios de joyería y relojes de 31 tiendas y las tendencias de TikTok (datos del 6-oct: conviene volver a ejecutarlo).
Notas de la revisión del 29-oct: ver «Radar» en `CLAUDE.md`.

## Ver la oficina «estilo Habbo»
Extensión de VS Code **Pixel Agents** (MIT): cada agente es un personaje que se sienta y teclea mientras trabaja. Solo muestra lo que se ejecuta **en este PC**
(no rutinas en la nube). Las salas se pintan en su editor de diseño (Layout): una por rol.

## Qué falta (por orden)
1. Publicar por la API oficial de Instagram lo `aprobado`: **el script `publicar.py` está hecho** (29-oct) y probado hasta el contenedor «FINISHED» (sin publicar). El token es el de la
   página «L U N E R I E» (no caduca) y vive en `.env.local` (`IG_TOKEN`, `IG_USER_ID`, `META_APP_ID`, `META_APP_SECRET`; nunca en git). Falta probar una publicación real
   cuando haya una pieza `aprobado`. La API **no programa**: quien lanza el
   script pone la hora. Los reels necesitan además el MP4 ya alojado y la música no se puede añadir por API.
2. Pista de música libre con licencia comercial y registrada.
3. Volver a ejecutar el radar y refrescar `referencias/`.
4. TikTok (cuando exista la cuenta).
