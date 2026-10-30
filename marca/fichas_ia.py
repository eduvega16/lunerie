"""Fotos IA de las fichas nuevas (30-oct): producto suelto en fondo niebla + puesto en persona, estilo Olivia Jewelry.

Para que todas las fichas sigan la regla de la galería (1.ª el producto suelto en niebla, 2.ª puesto en persona).
API de Higgsfield (flare = GPT Image 2.5, ~0,13 $ por foto); clave HF_KEY en .env.local.
    python marca/fichas_ia.py <carpeta_refs> [toma ...]      (sin tomas: todas)
<carpeta_refs> tiene una subcarpeta por producto con las fotos del proveedor (mNN.png), las que baja
productos/normalizar_dsers.py. Las salidas van a marca/fotos-ia/fichas/<toma>.png.
"""
import concurrent.futures, pathlib, sys, urllib.request
from dotenv import load_dotenv
import higgsfield_client

RAIZ = pathlib.Path(__file__).resolve().parent.parent
load_dotenv(RAIZ / ".env.local")
MODELO = "marketing-studio/image/flare"
SALIDA = RAIZ / "marca" / "fotos-ia" / "fichas"

# Cómo es cada pieza de verdad (para que la IA no la rediseñe). Sin texto ni logos en la esfera.
PIEZA = {
    "sepia": "a small rectangular watch with an octagonal-cornered polished gold case, a cream dial with black Roman "
             "numerals and thin blue steel hands, and a plain brown leather strap with a gold buckle",
    "maille": "a small oval watch with a slim polished gold case, a white dial with tiny gold dot indices and thin gold "
              "hands, short gold T-shaped lugs, and a narrow 7 mm bracelet of fine gold woven mesh",
    "galet": "an oval watch with a thick, rounded, highly polished gold case shaped like a smooth pebble, a white "
             "sunburst dial with gold Roman numerals and gold hands, and a bracelet of three-row polished gold links",
    "perle": "a small oval watch with a slim gold case and a cream dial with tiny crystal indices, on a bracelet of "
             "open gold oval links, each holding one small round white pearl",
    "duo": "an open gold ring with two enamel pieces in thin gold bezels at its ends: a long rectangular sage-beige "
           "one and a smaller rectangular deep blue one",
    "boucle": "a pair of medium U-shaped hoop earrings in smooth polished gold, about 18 mm long and 12 mm wide",
}
FIEL = ("Use the piece from the reference images EXACTLY as it is - do not redesign it: {p}. Keep its shape, "
        "proportions, colours, size and every detail. No text, no logo and no brand name on it or in the image. ")
NIEBLA = ("Clean high-end jewelry e-commerce photograph: the piece alone on a seamless pale mist-grey background "
          "(#F2F4F2), soft diffused daylight from the upper left, a delicate natural shadow, plenty of negative space, "
          "sharp focus, photorealistic, minimal, in the style of Olivia Jewelry or Mejuri product pages.")
PERSONA = (" Warm natural skin with real texture, short nude manicure, face cropped below the nose or out of frame, "
           "soft natural daylight, light neutral background, shallow depth of field, calm and elegant, "
           "photorealistic, in the style of an Olivia Jewelry campaign photo.")
REFS = {"sepia": ["sepia/m06.png", "sepia/m02.png"], "maille": ["maille/m08.png", "maille/m01.png"],
        "galet": ["galet/m08.png", "galet/m00.png"], "perle": ["perle/m03.png", "perle/m04.png"],
        "duo": ["anillo/m00.png", "anillo/m03.png"], "boucle": ["aros/m04.png", "aros/m01.png"]}

TOMAS = {
    # producto suelto en niebla (Sépia y Boucle ya lo tienen del proveedor)
    "maille-niebla": ("maille", NIEBLA + " The watch lies flat with the bracelet in a soft open curve."),
    "galet-niebla": ("galet", NIEBLA + " The watch lies flat with the bracelet in a soft open curve."),
    "perle-niebla": ("perle", NIEBLA + " The watch lies flat with the pearl bracelet in a soft open curve."),
    "duo-niebla": ("duo", NIEBLA + " The ring stands upright, seen slightly from above so both enamel pieces show."),
    # puesto en persona
    "sepia-persona": ("sepia", "Editorial close-up of a woman's wrist wearing this watch, her hand lightly holding the "
                      "cuff of an oversized white cotton shirt." + PERSONA),
    "maille-persona": ("maille", "Editorial close-up of a woman's hand resting near her collarbone, wearing this watch "
                       "on her slim wrist, a cream chunky-knit turtleneck." + PERSONA),
    "galet-persona": ("galet", "Editorial close-up of a woman's wrist wearing this watch, her hand tucking long brown "
                      "hair behind her ear, a soft camel knit sleeve slightly pushed back." + PERSONA),
    "perle-persona": ("perle", "Editorial close-up of a woman's hand wearing this watch, holding a small white "
                      "porcelain teacup, the cuff of a cream knit sweater at the wrist." + PERSONA),
    "duo-persona": ("duo", "Editorial close-up of a woman's hand at her collarbone, wearing this ring on her index "
                    "finger, a cream knit sweater." + PERSONA),
    "boucle-persona": ("boucle", "Editorial side close-up of a woman's ear wearing one of these hoops, long brown hair "
                       "tucked behind the ear, jaw and neck visible, a cream knit collar." + PERSONA),
}


def generar(toma, carpeta):
    pieza, escena = TOMAS[toma]
    try:
        refs = [higgsfield_client.upload_file(carpeta / r) for r in REFS[pieza]]
        res = higgsfield_client.subscribe(MODELO, arguments={
            "prompt": FIEL.format(p=PIEZA[pieza]) + escena, "image_urls": refs, "aspect_ratio": "3:4",
            "resolution": "2k", "quality": "high", "enhance_prompt": False})
    except Exception as e:  # fallo, moderación o sin créditos: no se da por bueno
        return toma, f"ERROR {type(e).__name__}: {e}"
    imgs = (res or {}).get("images") or []
    if not imgs:
        return toma, f"SIN IMAGEN: {res}"
    destino = SALIDA / f"{toma}.png"
    urllib.request.urlretrieve(imgs[0]["url"], destino)
    return toma, str(destino)


if __name__ == "__main__":
    carpeta = pathlib.Path(sys.argv[1]); SALIDA.mkdir(parents=True, exist_ok=True)
    elegidas = sys.argv[2:] or list(TOMAS)
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
        for toma, r in ex.map(lambda t: generar(t, carpeta), elegidas):
            print(toma, "->", r)
