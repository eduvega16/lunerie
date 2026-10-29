---
description: Ciclo semanal de la oficina de Lunerie (ideas, piezas, montaje, informe de ads). No publica ni gasta nada: deja todo en la cola para que Edu apruebe.
---

Ejecuta el ciclo semanal de la oficina de Lunerie siguiendo `oficina/README.md`. Argumentos opcionales de Edu: $ARGUMENTS

Hazlo en este orden, usando los agentes de la oficina (cada uno con la herramienta Agent):

1. **Estratega creativo** (`estratega-creativo`): ideas de la semana en `oficina/ideas/`. Que actualice antes las referencias del radar.
2. **Community manager** (`community-manager`): convierte las mejores ideas en piezas en `oficina/cola/` (estado `borrador`), de 5 a 7 piezas.
3. **Editor de vídeo** (`editor-video`): solo para las piezas de vídeo cuyo material ya exista; que monte en `oficina/salida/`.
4. **Experto en ads** (`experto-ads`): informe de la campaña en `oficina/informes/`.

Reglas del ciclo:
- Los agentes 1 y 4 no dependen entre sí: lánzalos a la vez. El 2 espera al 1, y el 3 al 2.
- **No publiques nada, no cambies nada en Shopify ni en Meta y no gastes créditos de IA.** Si alguna pieza necesita generar imágenes o clips, solo
  anota el coste estimado.
- Si un agente falla o no tiene un dato, dilo tal cual; no rellenes huecos.

Al terminar, resume a Edu en pocas líneas, en español:
- Qué piezas están listas para revisar (id, formato, una frase) y cuáles necesitan material nuevo o dinero (y cuánto).
- Qué dice el informe de ads y qué decisión necesita de él.
- Cómo aprobar: poner `"estado": "aprobado"` en la pieza o decírselo a Claude.
