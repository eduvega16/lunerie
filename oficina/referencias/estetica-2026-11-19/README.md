# Estética de Lunerie: limpieza y elegancia (Edu, 19-nov)

Edu, con la captura `plantillas-joyeria.png` (un anuncio de Zeely con plantillas de Able, Atolea, Monica Vinader,
Heaven Mayhem, Kendra Scott y Brilliant Earth): «Este es el estilo que deben tener nuestras publicaciones de Instagram
y nuestros anuncios. Limpieza y elegancia». **Manda sobre los formatos ruidosos** (notas del móvil, kcal, bloques de
texto, subtítulos grandes, rojo chillón).

## Qué tienen en común
- **La foto manda y va a sangre:** luz natural y cálida, piel, tela, la pieza puesta de cerca (mano, cuello, oreja),
  cara cortada o de perfil. O la pieza sola, centrada sobre un fondo liso o un degradado suave.
- **Poco texto, centrado, con mucho aire,** en el tercio de arriba (o abajo si arriba está la pieza):
  - la marca pequeña, en mayúsculas muy espaciadas;
  - un titular de 1-2 líneas en serif fina, con la segunda línea (o una palabra) en cursiva;
  - debajo, como mucho, una línea pequeña en sans con mayúsculas espaciadas.
- **La oferta, discreta:** píldoras de borde fino («BUY 2, GET 2 FREE») o una línea pequeña al lado («25% OFF»).
  Nada de bandas, pegatinas, emojis ni flechas.
- **Color:** tonos apagados; como mucho, un fondo liso de color profundo (el burdeos de Monica Vinader) con la pieza
  en su caja.

## Qué NO copiamos
- «EVERY PIECE TURNS HEADS» con letra gruesa y la etiqueta «WATERPROOF»: es la que rompe la elegancia de la hoja.
- Sus afirmaciones: «waterproof», «tarnish-free», «ocean-proof», «lifetime color warranty», «handcrafted in…»,
  «guaranteed to love». Lunerie solo dice lo que el proveedor confirma por escrito (CLAUDE.md, apartado 4).

## Cómo lo hacemos (sin IA, gratis)
`python marca/editorial.py` → `marca/fotos-ia/editorial-limpio/` (4:5 y 9:16). Usa fotos ya revisadas y la letra de
la marca: LUNERIE en Cormorant Medium espaciada, titular en Cormorant Light + Light Italic y línea en Jost con
mayúsculas espaciadas. Hay 4 plantillas:
1. **Puesta:** texto blanco sobre la piel.
2. **Cajita sobre color liso:** burdeos.
3. **Producto solo** sobre su fondo.
4. **Oferta en píldoras** sobre crema.

En 9:16, el texto va dentro de la zona libre de Meta (14-65 % del alto).
