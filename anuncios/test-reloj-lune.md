# Test del reloj Lune · plan de lanzamiento

**Objetivo:** lanzar el test de ~90 € **en las 48 h siguientes a que llegue la muestra del BS** (llega entre el 16 y el
29-oct) y decidir con datos antes del 9-nov. Reglas de decisión: CLAUDE.md, apartados 5.1 y 7.

## 1. Antes de que llegue la muestra (ya)

| Quién | Qué | Estado |
|---|---|---|
| Edu | Formato de moneda «44,95 €»: Configuración → General → Moneda → `{{amount_with_comma_separator}} €` | |
| Edu | Decidir la dirección del aviso legal (completa o como está) | |
| Edu | Instagram @lunerie_co: archivar lo antiguo, bio, avatar, enlace lunerie.es | |
| Edu | Borrar/archivar la página de Facebook antigua (1311701355367588) | |
| Claude | Textos de los anuncios (abajo) y estructura de la campaña | ✅ |
| Claude | Portada: preparada la vuelta a la foto en óvalo si el vídeo nuevo no está a tiempo | |

## 2. El día que llega la muestra (2-3 h de trabajo)

1. **Apuntar cuántos días ha tardado** desde el pedido → ese es el plazo real → Claude quita [PLAZO] de envíos,
   preguntas frecuentes y ficha.
2. **Mirar la pieza:** ¿piedras de resina o vidrio? ¿logo BS en la esfera? ¿el cierre aguanta? ¿parece barato?
   Si algo falla, se para aquí.
3. **Fotos** (móvil, luz de ventana, cartulina blanca o niebla, formato 4:5): reloj entero de frente · detalle de
   la esfera · detalle de las piedras · en la muñeca · en la caja.
4. **Vídeos** (vertical 9:16, 10-15 s cada uno, sin música; la música se pone en Meta):
   - **A** en la muñeca, girándola despacio para que brillen las piedras.
   - **B** abriendo la caja: tapa, reloj dentro, sacarlo.
   - **C** dos relojes juntos (los dos colores) sobre la mesa, la mano coge uno.
   - **D** quitando un eslabón con el extractor (para la duda «¿me quedará grande?»).
5. Pasármelo todo → Claude: fotos a 4:5 y a la ficha, vídeo de portada, anuncios montados.
6. **Quitar la contraseña** de la tienda y **lanzar**.

## 3. Campaña (Meta, cuenta «LUNERIE PUBLI»)

- **Objetivo:** Ventas · evento **Compra** (píxel ya probado).
- **Presupuesto por conjunto (ABO):** 3 conjuntos × 10 €/día × 3 días.
- **Público:** España (península + Baleares), mujeres y hombres 25-60 (mucho regalo lo compran ellos), sin
  intereses (Advantage+ / amplio). Ubicaciones automáticas.
- **Un ángulo por conjunto**, 2 anuncios en cada uno (vídeo + foto). El enlace va a la ficha del reloj.
- **Cada día:** gasto, impresiones, clics, carritos y compras al radar (`cli.py test`). No tocar nada las
  primeras 48 h salvo que un conjunto pase de ~18 € sin un solo carrito.

## 4. Anuncios

Reglas: pocas palabras, sin emojis, sin «¡OFERTA!», sin cuenta atrás, sin «jade», «piedras preciosas» ni «resistente
al agua», sin precio tachado.

### Conjunto 1 · Regalo («para ella»)
- **Texto:** Un reloj que se lleva como una joya. Esfera ovalada, piedras verdes y eslabones finos. Llega en su
  caja, listo para regalar. Envío gratis a península.
- **Titular:** Reloj Lune · 44,95 €
- **Descripción:** Para Navidad, pídelo antes del 1 de diciembre.
- **Creatividades:** vídeo B (abriendo la caja) · foto del reloj en la caja.

### Conjunto 2 · Estilo («vintage que se siente actual»)
- **Texto:** Pequeño, ovalado y con piedras. Un aire vintage que se siente actual, para llevarlo cada día como
  una pulsera fina.
- **Titular:** El reloj Lune
- **Descripción:** Dorado o plateado · envío gratis a península.
- **Creatividades:** vídeo A (en la muñeca) · foto de detalle de la esfera.

### Conjunto 3 · Dos («uno para ti y otro para regalar»)
- **Texto:** Uno para ti y otro para regalar. Añade dos a la cesta y el segundo se queda en 19,95 €.
- **Titular:** El segundo reloj, por 19,95 €
- **Descripción:** Reloj Lune · envío gratis a península.
- **Creatividades:** vídeo C (los dos colores juntos) · foto de los dos relojes.

**Botón:** «Comprar» en los tres.

## 5. Cuándo se para o se sube (resumen)

| Situación | Qué se hace |
|---|---|
| ~18 € gastados en un conjunto sin carritos | Apagar ese conjunto |
| ~36 € gastados en total sin ventas | Parar el test |
| CTR < 1 % o CPC > 0,90 € | Cambiar el vídeo o el texto de ese conjunto |
| Coste por venta entre 12,5 y 17,9 € | Probar otras creatividades |
| ≥ 3 ventas a ≤ 12,5 € cada una | Escalar: subir presupuesto un 20-30 % cada 2 días |
