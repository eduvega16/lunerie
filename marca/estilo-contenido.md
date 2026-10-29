# Estilo de contenido «reloj + joya en el día a día» (29-oct-2026)

Referencia de Edu: vídeo «ideas de contenido, edición joyería» (1. la vida cotidiana: joyas en el metro, en una bolsa de fruta,
comiendo; 2. detrás de escena; 3. comunidad; 4. romper el patrón). Para Lunerie se usan **1 y 4**; el 2 solo con cosas
verdaderas (nunca fingir un taller) y el 3 solo con clientas reales.

## Cómo se ve
- **Juvenil, de móvil**: gran angular con **ojo de pez** y la mano/muñeca muy cerca del objetivo.
- Solo manos y brazo, **sin cara**. Sol natural y color vivo (fruta, calle, metro, terraza).
- **En la misma mano, el reloj Lune y una joya** (anillo Nuit, collar Lune…). El reloj sale grande en el cuadro porque la muñeca
  está cerca del objetivo, no porque se agrande (sigue siendo una esfera de 12 mm).
- Esfera **sin marca** en anuncios. Texto en pantalla: corto, Jost blanca, sin emojis.
- 3:4 para foto (Higgsfield pide 3:4; recortar a 4:5 si hace falta) y 9:16 para vídeo.

## Cómo se genera
- `python marca/combinados.py marca/fotos-ia/combinados <escena> ...` (API de Higgsfield, modelo flare/GPT Image 2.5, ~0,13 $ por foto).
  Escenas: `metro-ojo`, `mercado`, `terraza` (estilo juvenil) y `cafe`, `metro`, `pelo` (estilo sobrio, primera prueba).
- Referencias: `lune-verde-producto.jpg` (reloj), `joyas/nuit-verde-mano-v1.png` (anillo) y `lune-verde-detalle.jpg` (color de las piedras).
- **Nano Banana** solo va por el conector de claude.ai y la cuenta gratis tiene 0,55 créditos (cada imagen cuesta 2): no se usa salvo que
  Edu recargue. Con la API, flare mantiene bien el reloj.

## Qué revisar siempre (lecciones de la primera tanda)
1. **Mirar el reloj a tamaño real (recorte), no en la vista reducida**: ahí las piedras parecían grises y no lo eran.
   Deben ser verde oscuro con vetas claras, 3 a cada lado de la esfera.
2. El **oro** del reloj real, en la foto de producto, es algo más pálido y rosado que el amarillo vivo que pinta la IA: comparar con el real.
3. **Anillo Nuit** en verde oliva: a veces sale ámbar (pasa en `metro-ojo`); `mercado` y `terraza` lo clavan.
4. Escenas de metro: sin carteles ni logos; los pasajeros del fondo son de IA (borrosos).
5. Meta puede etiquetarlo «hecho con IA»: el producto tiene que ser fiel al real.
