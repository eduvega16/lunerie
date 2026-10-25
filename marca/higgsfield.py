"""Imágenes de producto con Higgsfield (Marketing Studio 2.5 Flare = GPT Image 2.5) a partir de fotos de referencia.

La clave va en .env.local (HF_KEY=id:secreto, fuera de git). Cada imagen gasta créditos.
    python marca/higgsfield.py <salida_dir> <ref1> [ref2 ...]      (refs: URL pública o fichero local)
Las tomas (PROMPTS) siguen la estética de Olivia Jewelry: limpia, producto mejorado y puesto en modelo.
"""
import concurrent.futures, pathlib, sys, urllib.request
from dotenv import load_dotenv
import higgsfield_client

RAIZ = pathlib.Path(__file__).resolve().parent.parent
load_dotenv(RAIZ / ".env.local")
MODELO = "marketing-studio/image/flare"

FIEL = ("Use the watch from the reference images EXACTLY as it is - do not redesign it: the same small oval case "
        "with a rope-twist gold bezel, the same white dial with gold hands and baton indices and the small 'NAIDU' "
        "text, the same bracelet made only of oval green marbled stones, each one set in a gold frame with a "
        "rope-twist edge, joined by short gold links. Keep the stone colour, shape and count. No extra charms, "
        "no added logo, no text in the image.")
PROMPTS = {
    "producto": FIEL + " Clean high-end jewelry e-commerce photograph: the watch lying in a soft, gentle curve on a "
                "seamless pale mist-grey background (#F2F4F2), soft diffused daylight from the upper left, a delicate "
                "natural shadow, plenty of negative space, sharp focus on the dial and the stones, photorealistic, "
                "minimal, in the style of Olivia Jewelry or Mejuri product pages.",
    "modelo": FIEL + " Editorial close-up of a woman's wrist and hand wearing this watch, natural soft daylight, warm "
              "natural skin with real texture, short neutral manicure, a cream knit sleeve slightly pushed back, "
              "light neutral background, shallow depth of field, calm and elegant, photorealistic, in the style of an "
              "Olivia Jewelry campaign photo.",
}


def referencia(r):
    return r if r.startswith("http") else higgsfield_client.upload_file(pathlib.Path(r))


def generar(nombre, refs, salida):
    try:
        res = higgsfield_client.subscribe(MODELO, arguments={
            "prompt": PROMPTS[nombre], "image_urls": refs, "aspect_ratio": "3:4",
            "resolution": "2k", "quality": "high", "enhance_prompt": False})
    except Exception as e:  # fallo, cancelación, moderación o sin créditos: no se da por bueno
        return nombre, f"ERROR {type(e).__name__}: {e}"
    imgs = (res or {}).get("images") or []
    if not imgs:
        return nombre, f"SIN IMAGEN: {res}"
    destino = salida / f"{nombre}.png"
    urllib.request.urlretrieve(imgs[0]["url"], destino)
    return nombre, str(destino)


if __name__ == "__main__":
    salida = pathlib.Path(sys.argv[1]); salida.mkdir(parents=True, exist_ok=True)
    refs = [referencia(r) for r in sys.argv[2:]]
    with concurrent.futures.ThreadPoolExecutor() as ex:
        for nombre, r in ex.map(lambda n: generar(n, refs, salida), PROMPTS):
            print(nombre, "→", r)
