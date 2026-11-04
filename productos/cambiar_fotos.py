"""Cambia fotos de la galería de cualquier producto EN SU SITIO (fileUpdate + originalSource: conserva la posición, el
texto alternativo y la variante que la usa). Recorta a 4:5 y guarda una copia JPEG 97 sin submuestreo de color junto a
la imagen original (Edu, 4-nov: «las fotos se ven peor en Shopify»), que es la que se sube.
    python productos/cambiar_fotos.py <handle> <imagen> <posición> [<imagen> <posición> …]
Ejemplo: python productos/cambiar_fotos.py reloj-maille marca/fotos-ia/fichas/maille-niebla-1.png 1
"""
import pathlib, sys
from PIL import Image
from gql import gql
from normalizar_dsers import crop45
from collar_signe import subir


def cambiar(handle, pares):
    M = gql('query($h: String!){ productByHandle(handle: $h){ media(first: 30){ nodes{ id alt } } } }',
            {"h": handle})["productByHandle"]["media"]["nodes"]
    rutas = []
    for img, _ in pares:
        img = pathlib.Path(img)
        r = img.with_suffix(".jpg")
        crop45(Image.open(img).convert("RGB")).save(r, quality=97, subsampling=0); rutas.append(r)
    fuentes = subir(rutas)
    gql("""mutation($f:[FileUpdateInput!]!){ fileUpdate(files:$f){ userErrors{ field message } } }""",
        {"f": [{"id": M[pos - 1]["id"], "originalSource": s} for s, (_, pos) in zip(fuentes, pares)]}, True)
    for (img, pos) in pares:
        print(f"{handle} {pos}: {M[pos - 1]['alt']}  <-  {img}")


if __name__ == "__main__":
    a = sys.argv[1:]
    cambiar(a[0], [(a[i], int(a[i + 1])) for i in range(1, len(a), 2)])
