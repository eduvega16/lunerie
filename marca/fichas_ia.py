"""Fotos IA de las fichas nuevas (30-oct): producto suelto en fondo niebla + puesto en persona, estilo Olivia Jewelry.

Para que todas las fichas sigan la regla de la galería (1.ª el producto suelto en niebla, 2.ª puesto en persona).
API de Higgsfield (flare = GPT Image 2.5, ~0,13 $ por foto); clave HF_KEY en .env.local.
    python marca/fichas_ia.py [<carpeta_refs>] [toma ...] [--n 2] [--4k]      (sin tomas: todas)
4-nov (Edu: «hazlas con IA»): Maille, Galet, Perle y Duo se rehacen con las fotos REALES del proveedor de
marca/referencias-reales/ (<handle>-1.jpg, -2.jpg…; se mandan todas) y en 4K (0,17 $ por foto) → <toma>-<n>.png.
Sépia y Boucle siguen con <carpeta_refs>: una subcarpeta por producto con las fotos del proveedor (mNN.png), las que
baja productos/normalizar_dsers.py. Las salidas van a marca/fotos-ia/fichas/.
"""
import concurrent.futures, pathlib, sys, urllib.request
from dotenv import load_dotenv
import higgsfield_client

RAIZ = pathlib.Path(__file__).resolve().parent.parent
load_dotenv(RAIZ / ".env.local")
MODELO = "marketing-studio/image/flare"
SALIDA = RAIZ / "marca" / "fotos-ia" / "fichas"
REALES = RAIZ / "marca" / "referencias-reales"
HANDLE = {"maille": "reloj-maille", "galet": "reloj-galet", "perle": "reloj-perle", "duo": "anillo-duo"}
RESOLUCION = "2k"

# Cómo es cada pieza de verdad (para que la IA no la rediseñe). Sin texto ni logos en la esfera.
PIEZA = {
    "sepia": "a small rectangular watch with an octagonal-cornered polished gold case, a cream dial with black Roman "
             "numerals and thin blue steel hands, and a plain brown leather strap with a gold buckle",
    "maille": "a small oval watch (dial about 20 x 22 mm) with a slim polished gold case and a small crown at 3 "
              "o'clock, a white mother-of-pearl dial with tiny crystal indices and thin gold hands, short gold bow-shaped "
              "lugs (a small bar above and below the case), on a narrow 7 mm bracelet of fine gold woven wheat-pattern mesh",
    "galet": "an oval watch (24 mm dial) with a thick, rounded, highly polished gold case shaped like a smooth pebble, a "
             "white dial with gold Roman numerals at 12, 3, 6 and 9 and gold hands, on a 10 mm bracelet of polished gold "
             "links in three rows (a wider centre row between two narrow outer rows)",
    "perle": "a small oval watch (dial about 20 x 24 mm) with a pale champagne-gold case, a thin dark ring around a cream "
             "mother-of-pearl dial with tiny crystal indices and gold hands, on a 12 mm bracelet of open, round "
             "champagne-gold links, each holding one round white pearl in its centre, joined by small gold connectors",
    "duo": "an open adjustable gold ring (about 17 mm across) with two domed enamel stones in smooth polished gold bezels "
           "at its two ends, side by side: a long rounded-rectangle milky sage-beige one and a shorter rounded-rectangle "
           "deep navy blue one with subtle darker marbling",
    "boucle": "a pair of medium U-shaped hoop earrings in smooth polished gold, about 18 mm long and 12 mm wide",
}
FIEL = ("Use the piece from the reference images EXACTLY as it is - do not redesign it: {p}. Keep its shape, "
        "proportions, colours, size and every detail. No text, no logo and no brand name on it or in the image. "
        "The reference photos are real product photos: copy only this piece and ignore their backgrounds, gloves, "
        "props, other jewelry and any logo on the dial. ")
NIEBLA = ("Clean high-end jewelry e-commerce photograph: the piece alone on a seamless pale mist-grey background "
          "(#F2F4F2), soft diffused daylight from the upper left, a delicate natural shadow, plenty of negative space, "
          "sharp focus, photorealistic, minimal, in the style of Olivia Jewelry or Mejuri product pages. The piece is "
          "large in the frame, filling about two thirds of its height.")
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
                       "on her wrist, a cream chunky-knit turtleneck. The watch keeps its real size: the oval case "
                       "covers a bit less than half the width of the top of her wrist, as in the reference photo of it "
                       "on a wrist." + PERSONA),
    "galet-persona": ("galet", "Editorial close-up of a woman's wrist wearing this watch, her hand tucking long brown "
                      "hair behind her ear, a soft camel knit sleeve slightly pushed back. The watch keeps its real size: the "
                      "thick oval case covers about half the width of the top of her wrist." + PERSONA),
    "perle-persona": ("perle", "Editorial close-up of a woman's hand wearing this watch, holding a small white "
                      "porcelain teacup, the cuff of a cream knit sweater at the wrist. The watch keeps its real size, as in "
                     "the reference photo of it on a wrist: the oval case covers a bit less than half the width of the "
                     "top of her wrist and the pearls are clearly visible." + PERSONA),
    "duo-persona": ("duo", "Editorial close-up of a woman's hand at her collarbone, wearing this ring on her index "
                    "finger, a cream knit sweater. The ring keeps its real size, as in the reference photo of it on a "
                    "hand: the two enamel stones together are about as wide as the finger." + PERSONA),
    "boucle-persona": ("boucle", "Editorial side close-up of a woman's ear wearing one of these hoops, long brown hair "
                       "tucked behind the ear, jaw and neck visible, a cream knit collar." + PERSONA),
}


def generar(toma, n, carpeta):
    pieza, escena = TOMAS[toma]
    reales = sorted(REALES.glob(f"{HANDLE[pieza]}-*.jpg")) if pieza in HANDLE else []
    rutas = reales or [carpeta / r for r in REFS[pieza]]
    try:
        refs = [higgsfield_client.upload_file(r) for r in rutas]
        res = higgsfield_client.subscribe(MODELO, arguments={
            "prompt": FIEL.format(p=PIEZA[pieza]) + escena, "image_urls": refs, "aspect_ratio": "3:4",
            "resolution": RESOLUCION, "quality": "high", "enhance_prompt": False})
    except Exception as e:  # fallo, moderación o sin créditos: no se da por bueno
        return f"{toma}-{n}", f"ERROR {type(e).__name__}: {e}"
    imgs = (res or {}).get("images") or []
    if not imgs:
        return f"{toma}-{n}", f"SIN IMAGEN: {res}"
    destino = SALIDA / f"{toma}-{n}.png"
    urllib.request.urlretrieve(imgs[0]["url"], destino)
    return f"{toma}-{n}", str(destino)


if __name__ == "__main__":
    args = sys.argv[1:]; veces = 1
    if "--4k" in args:
        args.remove("--4k"); RESOLUCION = "4k"
    if "--n" in args:
        i = args.index("--n"); veces = int(args[i + 1]); del args[i:i + 2]
    carpeta = pathlib.Path(args.pop(0)) if args and pathlib.Path(args[0]).is_dir() else REALES
    SALIDA.mkdir(parents=True, exist_ok=True)
    trabajos = [(t, n) for t in (args or list(TOMAS)) for n in range(1, veces + 1)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
        for toma, r in ex.map(lambda tn: generar(tn[0], tn[1], carpeta), trabajos):
            print(toma, "->", r)
