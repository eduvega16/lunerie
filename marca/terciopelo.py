"""Fotos de Navidad sobre terciopelo rojo (13-nov, Edu: «las fotos en un fondo rojo terciopelado rollo navidad»).
Se parte de fotos del collar YA REVISADAS (nombre bien escrito, lágrima en el punto más bajo de la cadena) y se cambia
solo el fondo, para que la IA no rehaga el collar. Nada de lágrimas rojas sobre rojo (no se ven).
    python marca/terciopelo.py <toma> … [--n 1] [--4k]   →  marca/fotos-ia/terciopelo/<toma>-<n>.png
Tomas: ver TOMAS. Imagen: API de Higgsfield (flare = GPT Image 2.5), ~0,13 $ por foto en 2K (0,17 $ en 4K).
REVISAR a tamaño real: el nombre, UNA lágrima en la cadena y que el collar no haya cambiado.
"""
import concurrent.futures, pathlib, sys, urllib.request
import higgsfield_client
from portada_navidad import MODELO

RAIZ = pathlib.Path(__file__).resolve().parent.parent
COLLAR = RAIZ / "marca" / "fotos-ia" / "collar"
REFS = RAIZ / "marca" / "referencias-reales"
SALIDA = RAIZ / "marca" / "fotos-ia" / "terciopelo"

TERCIOPELO = ("rich deep Christmas-red crushed velvet fabric (a deep red like red wine, not orange, not pink) with soft "
              "natural folds and a gentle sheen where the light catches the pile")
LUZ = ("Warm, soft directional light like a winter window in the late afternoon, gentle shadows, luxurious jewelry "
       "editorial look, true-to-life gold. No text, no logo, no watermark, no people unless stated.")
MANTENER = ("Edit the first image. Keep the necklace EXACTLY as it is: the same gold chain, the same name with the same "
            "signature lettering letter by letter, the same single teardrop crystal with its colour, setting and size, "
            "in the same position, shape and scale in the frame. Do not redraw, move or add any jewelry. ")

TOMAS = {   # nombre: (foto de base o None, refs extra, prompt)
    "plano-sara": (COLLAR / "nombre-sara-verde-1.png", [],
                   MANTENER + "Change only the background and surface: the necklace now lies on " + TERCIOPELO +
                   ", filling the whole frame; the gold glows warmly against the red and the green crystal stands out. "
                   + LUZ),
    "lazo-laura": (COLLAR / "nombre-laura-azul-1.png", [],
                   MANTENER + "Change only the background and surface: the necklace now lies on " + TERCIOPELO +
                   ". In the top right corner, partly out of frame, a loose gold satin ribbon curls softly, and far "
                   "behind at the top a few warm fairy lights are blurred into soft golden bokeh. The blue crystal "
                   "stands out against the red. " + LUZ),
    "regalo-carmen": (COLLAR / "producto-verde-carmen-v2.jpg", [],
                      MANTENER + "Remove the mirror reflection under the crystal. Change only the background and "
                      "surface: the necklace now lies on " + TERCIOPELO + "; out of focus in the background corner, a "
                      "small gift box wrapped in cream paper with a thin gold ribbon, and a couple of tiny gold Christmas "
                      "baubles blurred. The necklace stays the sharp centre of the photo. " + LUZ),
    "cajita-carmen": (None, [COLLAR / "producto-verde-carmen-v2.jpg", SALIDA.parent / "ugc-lucce" / "ref-nombre-carmen.jpg",
                             REFS / "qiuhan-cajita-collar.jpg"],
                      "Luxury Christmas jewelry photograph, top-down at a slight angle: a small square jewelry box covered "
                      "in soft beige velvet, with its rounded hinged lid standing open, exactly like the beige velvet box in "
                      "the third reference photo (no logo, no text), resting on " + TERCIOPELO + ". Inside the box, laid "
                      "on the beige velvet, the gold necklace EXACTLY like the first reference photo: the name \"Carmen\" "
                      "cut from flat mirror-polished gold sheet in the same signature lettering as the second reference "
                      "(tall looping capital C, then a-r-m-e-n), sitting on one side of the chain, and a single faceted "
                      "emerald-green teardrop crystal in a four-prong gold setting threaded on the chain at its lowest "
                      "point; only ONE teardrop, nothing hangs from the name. The name is large, sharp and readable. "
                      "A thin gold ribbon lies loosely next to the box. " + LUZ),
    # 13-nov, tanda 2 (Edu: «sí dale»): plateado, otros nombres y colores (sobre las de terciopelo ya revisadas) y joyas
    "plata-elena": (SALIDA / "base-plata-elena.jpg", [],
                    MANTENER + "The necklace is silver: keep it silver. Change only the background and surface: the "
                    "necklace now lies on " + TERCIOPELO + ", filling the whole frame, extended naturally to a 3:4 frame; "
                    "the light-blue crystal and the polished silver stand out against the red. " + LUZ),
    "nombre-ana": (SALIDA / "plano-sara-1.png", [],
                   "Edit the first image. Keep EVERYTHING exactly the same - the red velvet, the light, the gold chain, its "
                   "path and position, the crystal's size, four-prong setting and position threaded on the chain at its "
                   "lowest point - and change only two things. First, the name now reads exactly \"Ana\" (capital A, then "
                   "n, a) in the same flat mirror-polished gold quick signature lettering, starting at the same jump ring "
                   "and ending in the same long straight stroke and small ring where the chain continues. Second, the "
                   "crystal is a light aqua blue (pale sea-water blue). " + LUZ),
    "nombre-paula": (SALIDA / "lazo-laura-1.png", [],
                     "Edit the first image. Keep EVERYTHING exactly the same - the red velvet, the gold ribbon, the bokeh "
                     "lights, the light, the gold chain, its path and position, the crystal's size, four-prong setting and "
                     "position threaded on the chain at its lowest point - and change only two things. First, the name now "
                     "reads exactly \"Paula\" (capital P, then a-u-l-a) in the same flat mirror-polished gold quick "
                     "signature lettering, starting at the same jump ring and ending in the same long straight stroke and "
                     "small ring where the chain continues. Second, the crystal is clear and colourless like a diamond, "
                     "sparkling. " + LUZ),
    # 13-nov: «Nuria» salía «Muria» (la N de firma parece una M) → «Eva»
    "nombre-eva": (SALIDA / "regalo-carmen-1.png", [],
                     "Edit the first image. Keep EVERYTHING exactly the same - the red velvet, the gift box, the baubles, "
                     "the light, the gold chain, its path and position, the crystal's size, four-prong setting and position "
                     "threaded on the chain at its lowest point - and change only two things. First, the name now reads "
                     "exactly \"Eva\" (capital E, then v, a) in the same flat mirror-polished gold signature lettering, "
                     "ending in the same gentle wavy tail. Second, the crystal is a deep violet purple. " + LUZ),
    "reloj-lune": (RAIZ / "marca" / "fotos-ia" / "lune-verde-producto.jpg", [REFS / "reloj-lune-2.jpg"],
                   "Edit the first image. Keep the watch EXACTLY as it is: the small oval gold case, the dial, the hands, "
                   "the bracelet with three green oval stones on each side and the empty braided rings at the ends, same "
                   "shape, size and position (the second image is a real photo of this watch, for reference only). Change "
                   "only the background and surface: the watch now lies on " + TERCIOPELO + ". " + LUZ),
    "reloj-maille": (RAIZ / "marca" / "fotos-ia" / "fichas" / "maille-niebla-2.png", [],
                     "Edit the first image. Keep the watch EXACTLY as it is: the oval gold case, the dial, the hands and "
                     "the gold mesh strap, same shape, size and position. Change only the background and surface: the "
                     "watch now lies on " + TERCIOPELO + ". " + LUZ),
    "anillo-nuit": (REFS / "anillo-nuit-1.jpg", [],
                    "Edit the first image. Keep the ring EXACTLY as it is: the gold signet band and the olive-green "
                    "marquise stone, same shape, size, angle and position. Change only the background and surface: the "
                    "ring now rests on " + TERCIOPELO + ", with its soft shadow on the velvet. " + LUZ),
    "aros-boucle": (REFS / "aros-boucle-1.jpg", [],
                    "Edit the first image. Keep the two earrings EXACTLY as they are: polished gold U-shaped hoops, same "
                    "shape, size and position. Change only the background and surface: they now lie on " + TERCIOPELO +
                    ", with soft shadows on the velvet. " + LUZ),
}


def generar(prompt, destino, refs, res):
    try:
        r = higgsfield_client.subscribe(MODELO, arguments={
            "prompt": prompt, "image_urls": refs, "aspect_ratio": "3:4", "resolution": res,
            "quality": "high", "enhance_prompt": False})
    except Exception as e:
        return f"{destino.stem}: ERROR {type(e).__name__}: {e}"
    imgs = (r or {}).get("images") or []
    if not imgs:
        return f"{destino.stem}: SIN IMAGEN {r}"
    urllib.request.urlretrieve(imgs[0]["url"], destino)
    return f"{destino.stem}: {destino}"


if __name__ == "__main__":
    a = sys.argv[1:]
    res = "4k" if "--4k" in a else "2k"
    n = int(a[a.index("--n") + 1]) if "--n" in a else 1
    SALIDA.mkdir(parents=True, exist_ok=True)
    pedidas = [t for t in a if t in TOMAS] or list(TOMAS)
    sube = lambda p: higgsfield_client.upload_file(pathlib.Path(p))
    trabajos = []
    for t in pedidas:
        base, extra, prompt = TOMAS[t]
        refs = ([sube(base)] if base else []) + [sube(p) for p in extra]
        trabajos += [(prompt, SALIDA / f"{t}-{k + 1}.png", refs) for k in range(n)]
    with concurrent.futures.ThreadPoolExecutor(4) as ex:
        for linea in ex.map(lambda tr: generar(tr[0], tr[1], tr[2], res), trabajos):
            print(linea, flush=True)
