"""Fotos del Collar Signé con nombres españoles (3-nov, Edu: «como las de Olivia, con chicas con su nombre y otras piezas
de la tienda», nada de Lucía). Producto: la foto del collar de productos/collar-signe/ cambiando el nombre y el color de
la piedra; puesto: con otras piezas de Lunerie (aros Boucle, reloj Lune, anillo Nuit) y sin cara (corte bajo la nariz).
API de Higgsfield (flare = GPT Image 2.5, ~0,13 $ por foto).
    python marca/collar_ia.py [<carpeta_refs>] [toma ...] [--n 2]   →   marca/fotos-ia/collar/<toma>-<n>.png
<carpeta_refs>: por defecto marca/referencias-reales/, con las fotos REALES de cada pieza (proveedor, amigas) con su
handle de nombre (reloj-lune-1.jpg, reloj-lune-2.jpg…): se mandan todas las de cada pieza. Nunca fotos hechas con IA.
REVISAR SIEMPRE a tamaño real que el nombre esté bien escrito y comparar cada pieza con su foto real.
"""
import concurrent.futures, pathlib, sys, urllib.request
import higgsfield_client
from portada_navidad import MODELO, PIEZA

RAIZ = pathlib.Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "marca" / "fotos-ia" / "collar"
COLLAR = RAIZ / "productos" / "collar-signe"
REFS = RAIZ / "marca" / "referencias-reales"
RESOLUCION = "2k"   # --4k para la máxima calidad (Edu, 4-nov: en Shopify se ven peor que en el PC)
# fotos REALES de la muestra (Yiwu Shangjie, «Marta», 4-nov): referencia del collar para las tomas puestas
COLLAR_REAL = [REFS / "collar-signe-1.jpg", REFS / "collar-signe-5.jpg"]
# 4-nov (Edu): el collar es ASIMÉTRICO: el nombre va en un lado de la cadena, en diagonal, y la lágrima cuelga recta en
# el centro, en el punto más bajo (como collar-signe-1.jpg y la foto de Marta). Ni nombre horizontal en el centro ni
# lágrima pegada al nombre.
DISENO = ("a fine {metal} cable-chain necklace built asymmetrically, exactly like the real photos of the necklace: "
          "a first name cut from a flat, mirror-polished {metal} sheet (not round wire) as a quick, bold handwritten "
          "signature - a tall, clearly legible capital letter with a long lead-in stroke and connected letters, every "
          "letter easy to read; the bright polished metal "
          "catches the light with crisp highlights, so the name shines clearly against the skin. The name hangs "
          "diagonally on one side of the chain (on the left of the picture) and is joined to the chain at exactly two "
          "points: the upper chain is fixed with a tiny jump ring to the top tip of the capital letter, and at the other "
          "end the last letter finishes in a long straight tail stroke that ends in a tiny ring where the lower chain is "
          "fixed. From there the chain continues two or three links down to the lowest point at the centre of the chest, "
          "where a single faceted teardrop crystal in a small {metal} four-prong setting hangs straight down on its own "
          "bail, point down - the crystal hangs from the chain, separate from the letters")
NO = ("a fine {metal} cable-chain necklace built asymmetrically, exactly like the real product photo of the necklace: "
          "a first name cut from a flat polished {metal} sheet (not round wire) as a quick, bold handwritten signature - "
          "a tall pointed capital with a long lead-in stroke and connected letters - is set into "
          "ONE SIDE of the chain (on the left of the picture), running diagonally down along the chain from the "
          "collarbone towards the centre - not horizontal and not centred; the last letter ends in a small loop that "
          "joins the chain, the chain continues two or three links down to the lowest point at the centre of the chest, "
          "and there a single faceted teardrop crystal in a small {metal} prong setting hangs straight down on its own "
          "bail, point down - the crystal hangs from the chain at the centre, separate from the letters")
NO = ("a fine {metal} cable-chain necklace with a first name written in a thin, flowing handwritten signature-style "
          "script made of polished {metal} wire, set horizontally into the chain like in the first reference photo: the "
          "last letter ends in a small loop that joins the chain, and two or three links further along the chain a "
          "single faceted teardrop crystal in a small {metal} prong setting hangs on its own bail - the crystal hangs "
          "from the chain, separate from the letters, never touching or attached to them")
NO = ("Every piece must be EXACTLY like the reference images - same shape, size relative to the body and details; do "
      "not redesign them. The reference photos are real product photos: copy only the pieces named here and ignore any "
      "other jewelry, rings or backgrounds that appear in them. "
      "The name on the necklace must be spelled exactly as given, letter by letter, and must be the only text in the "
      "image: no other text, no logos, nothing written on the watch dial. ")
TOMAS = {
    # foto de producto: la del collar, cambiando solo el nombre y el color de la piedra
    "producto-dorado": ("3:4", [COLLAR / "collar-signe-1.jpg"],
        "Edit the reference product photo: keep exactly the same gold necklace, angle, light grey background, reflection "
        "and lighting, but the name now reads exactly \"Marta\" (capital M, then a-r-t-a) in the same gold signature "
        "script, and the teardrop crystal is a bright medium blue. "),
    # 6-nov (Edu): la de Marta con la piedra verde y «Carmen» (el verde es el color que más se ve en las fotos de
    # producto); se edita la de Marta ya aprobada y la original verde (Olivia) sirve solo de referencia del color
    "producto-verde": ("3:4", [SALIDA / "producto-dorado-2.png", COLLAR / "collar-signe-1.jpg"],
        "Edit the first image. Keep EVERYTHING exactly the same - the gold chain, the angle, the light background, the "
        "reflection, the lighting and the framing - and change only two things. First, the name now reads exactly "
        "\"Carmen\" (a clearly readable capital C - an open round curve, never a V - then a-r-m-e-n) in the same thin "
        "gold signature script as \"Marta\", with the same long lead-in stroke, the same tiny jump ring at the top of the "
        "capital and the same straight tail ending in a small ring; the name keeps the same diagonal position on the "
        "left side of the chain. Second, the teardrop crystal is a vivid deep emerald green, exactly the green of the "
        "crystal in the second image, and its reflection below is green too. The second image is only a colour "
        "reference: ignore its name. "),
    "producto-plateado": ("3:4", [COLLAR / "collar-signe-3.jpg"],
        "Edit the reference product photo: keep exactly the same silver necklace, angle, white background and "
        "lighting, but the name now reads exactly \"Paula\" (capital P, then a-u-l-a) in the same silver signature "
        "script, and the teardrop crystal is soft pink. "),
    # puesto, sin cara
    "modelo-tirantes": ("3:4", [*COLLAR_REAL, "aros-boucle"],
        "Quiet-luxury editorial jewelry photo in soft natural daylight against a pale grey wall. A young woman with "
        "light brown hair pulled back, wearing a white ribbed cotton tank top; the frame cuts off just below her nose, "
        "from her lips down to her chest. Around her neck she wears " + DISENO.format(metal="gold") + ", the name "
        "reading exactly \"Elena\" and the teardrop crystal soft yellow; in her ear she wears {aros-boucle}, one per ear, "
        "at the same size relative to the earlobe as in the reference photo of the hoops on an ear. Natural skin "
        "texture, fine film grain. "),
    "modelo-hombro": ("3:4", [*COLLAR_REAL, "reloj-lune", "anillo-nuit"],
        "Quiet-luxury editorial jewelry photo in soft natural daylight against a warm off-white wall. A young woman in "
        "a white strapless top rests one hand on her opposite shoulder; the frame cuts off just below her nose, from "
        "her lips down to her chest. Around her neck she wears " + DISENO.format(metal="gold") + ", the name reading "
        "exactly \"Carmen\" and the teardrop crystal green. On the wrist of the hand on her shoulder she wears "
        "{reloj-lune}; the watch faces the camera and keeps the same size relative to the wrist as in the reference "
        "photo of the watch on a wrist. On her ring finger she wears {anillo-nuit}, at the same size relative to the "
        "finger as in the reference photo of the rings on a hand. Natural skin texture, fine film grain. "),
    # 4-nov: editar las fotos ya elegidas (reloj, anillo y aros buenos) cambiando solo el collar
    "editar-hombro": ("3:4", [SALIDA / "editar-hombro-2-v2.png", *COLLAR_REAL],
        "Edit the first image. Keep EVERYTHING exactly the same - the woman, her pose, skin, hair, strapless top, wall, "
        "light, framing, the watch on her wrist and the ring on her finger, pixel for pixel - and change only the "
        "necklace: it becomes " + DISENO.format(metal="gold") + ", the name reading exactly \"Carmen\" (a clearly "
        "readable capital C - an open round curve, never a V - then a-r-m-e-n) and the teardrop crystal green. The "
        "watch stays exactly as it is in the first image, including its six opaque, polished green cabochon stones "
        "with light veins (not faceted, not transparent). The other images are real photos of the necklace: use them "
        "only for how the necklace is built. "),
    "editar-tirantes": ("3:4", [SALIDA / "editar-tirantes-2-v2.png", *COLLAR_REAL],
        "Edit the first image. Keep EVERYTHING exactly the same - the woman, her pose, skin, hair, ribbed tank top, "
        "wall, light, framing and the hoop earrings, pixel for pixel - and change only the necklace: it becomes "
        + DISENO.format(metal="gold") + ", the name reading exactly \"Elena\" (a clearly readable capital E, then "
        "l-e-n-a) and the teardrop crystal soft yellow. The other images are real photos of the necklace: use them only for how the "
        "necklace is built. "),
}


def generar(toma, n, refs_dir):
    formato, refs, escena = TOMAS[toma]
    rutas = []
    for r in refs:
        if isinstance(r, str):
            fotos = sorted(refs_dir.glob(f"{r}-*.jpg")) or [refs_dir / f"{r}.jpg"]
            escena = escena.replace("{" + r + "}", PIEZA[r]); rutas += fotos
        else:
            rutas.append(r)
    try:
        urls = [higgsfield_client.upload_file(r) for r in rutas]
        res = higgsfield_client.subscribe(MODELO, arguments={
            "prompt": escena + NO, "image_urls": urls, "aspect_ratio": formato,
            "resolution": RESOLUCION, "quality": "high", "enhance_prompt": False})
    except Exception as e:
        return f"{toma}-{n}", f"ERROR {type(e).__name__}: {e}"
    imgs = (res or {}).get("images") or []
    if not imgs:
        return f"{toma}-{n}", f"SIN IMAGEN: {res}"
    destino = SALIDA / f"{toma}-{n}.png"
    urllib.request.urlretrieve(imgs[0]["url"], destino)
    return f"{toma}-{n}", str(destino)


if __name__ == "__main__":
    args = sys.argv[1:]
    veces = 1
    if "--4k" in args:
        args.remove("--4k"); RESOLUCION = "4k"
    if "--n" in args:
        i = args.index("--n"); veces = int(args[i + 1]); del args[i:i + 2]
    refs_dir = REFS
    if args and pathlib.Path(args[0]).is_dir():
        refs_dir = pathlib.Path(args.pop(0))
    SALIDA.mkdir(parents=True, exist_ok=True)
    trabajos = [(t, n) for t in (args or list(TOMAS)) for n in range(1, veces + 1)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
        for toma, r in ex.map(lambda tn: generar(tn[0], tn[1], refs_dir), trabajos):
            print(toma, "->", r)
