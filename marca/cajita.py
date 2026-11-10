"""Foto de la ficha del Collar Signé con la cajita de terciopelo beige en la que llega (10-nov, Edu). La cajita sale de la
foto de catálogo de QIUHAN (marca/referencias-reales/qiuhan-cajita-collar.jpg, recorte de qiuhan-cajitas-catalogo.jpg);
el collar, de la foto de estudio corregida + la muestra real «Marta». Cambiarla por la foto real de #LUN1006 cuando llegue.
    python marca/cajita.py [--n 3]   → marca/fotos-ia/cajita/cajita-<n>.png
"""
import concurrent.futures, pathlib, sys, urllib.request
import higgsfield_client
import collar_ia as C
from collar_cada_una import base

RAIZ = C.RAIZ
SALIDA = RAIZ / "marca" / "fotos-ia" / "cajita"
CAJA = RAIZ / "marca" / "referencias-reales" / "qiuhan-cajita-collar.jpg"
PROMPT = (
    "Luxury jewelry product photograph on a seamless, very light cool grey-white background (#F2F4F2), soft even studio "
    "light and a gentle soft shadow. In the centre, ONE small square jewelry box covered in soft beige velvet with cut "
    "(chamfered) corners, exactly like the open box in the first reference image: hinged lid open upright at about 100 "
    "degrees, plain beige velvet inside the lid, and a beige velvet pad in the base with a small slit. Resting on the pad "
    "is the gold necklace of the other reference images: the name \"Marta\" (a tall pointed capital M with a long lead-in "
    "stroke, then a-r-t-a) cut from a flat mirror-polished gold sheet in quick handwritten signature lettering, joined to "
    "a fine gold cable chain by a tiny ring at the top of the capital and ending in ONE long straight tail stroke with a "
    "small ring; two or three links later a SMALL faceted pear-shaped crystal in a vivid emerald green, in a four-prong "
    "gold setting, is threaded directly onto the chain; the rest of the chain goes into the slit of the pad. The box is "
    "about 7 cm wide, so the name spans about half the width of the pad and the crystal is clearly smaller than the "
    "capital M. Front three-quarter view, slightly from above, the box filling about 60 % of the frame width. Only this "
    "one box: no other boxes, no ring, no heart pendant, no text, no logo, no watermark.")


def generar(n):
    try:
        urls = [higgsfield_client.upload_file(r) for r in (CAJA, base(), *C.MUESTRA)]
        r = higgsfield_client.subscribe(C.MODELO, arguments={
            "prompt": PROMPT, "image_urls": urls, "aspect_ratio": "3:4", "resolution": "2k", "quality": "high",
            "enhance_prompt": False})
        url = ((r or {}).get("images") or [{}])[0].get("url")
        if not url:
            return n, f"SIN IMAGEN {r}"
        destino = SALIDA / f"cajita-{n}.png"
        urllib.request.urlretrieve(url, destino)
        return n, str(destino)
    except Exception as e:
        return n, f"ERROR {e}"


if __name__ == "__main__":
    veces = int(sys.argv[sys.argv.index("--n") + 1]) if "--n" in sys.argv else 3
    SALIDA.mkdir(parents=True, exist_ok=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
        for n, r in ex.map(generar, range(1, veces + 1)):
            print(n, "->", r, flush=True)
