"""Fotos del Collar Signé con nombres españoles (3-nov, Edu: «como las de Olivia, con chicas con su nombre y otras piezas
de la tienda», nada de Lucía). Producto: la foto del collar de productos/collar-signe/ cambiando el nombre y el color de
la piedra; puesto: con otras piezas de Lunerie (aros Boucle, reloj Lune, anillo Nuit) y sin cara (corte bajo la nariz).
API de Higgsfield (flare = GPT Image 2.5, ~0,13 $ por foto).
    python marca/collar_ia.py <carpeta_refs> [toma ...] [--n 2]   →   marca/fotos-ia/collar/<toma>-<n>.png
<carpeta_refs>: la primera foto de cada producto con su handle de nombre (aros-boucle.jpg, reloj-lune.jpg…).
REVISAR SIEMPRE a tamaño real que el nombre esté bien escrito.
"""
import concurrent.futures, pathlib, sys, urllib.request
import higgsfield_client
from portada_navidad import MODELO, PIEZA

RAIZ = pathlib.Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "marca" / "fotos-ia" / "collar"
COLLAR = RAIZ / "productos" / "collar-signe"
# 4-nov (Edu): la lágrima NO va pegada al nombre: cuelga suelta de la cadena, un poco después del final del nombre.
DISENO = ("a fine {metal} cable-chain necklace with a first name written in a thin, flowing handwritten signature-style "
          "script made of polished {metal} wire, set horizontally into the chain; a short length of plain chain after "
          "the end of the name, a single faceted teardrop crystal in a small {metal} prong setting hangs on its own "
          "tiny jump ring from the chain - the crystal is separate from the letters and never touches or attaches to them")
NO = ("Every piece must be EXACTLY like the reference images - same shape, size and details; do not redesign them. "
      "The name on the necklace must be spelled exactly as given, letter by letter, and must be the only text in the "
      "image: no other text, no logos, nothing written on the watch dial. ")
TOMAS = {
    # foto de producto: la del collar, cambiando solo el nombre y el color de la piedra
    "producto-dorado": ("3:4", [COLLAR / "collar-signe-1.jpg"],
        "Edit the reference product photo: keep exactly the same gold necklace, angle, light grey background, reflection "
        "and lighting, but the name now reads exactly \"Marta\" (capital M, then a-r-t-a) in the same gold signature "
        "script, and the teardrop crystal is a bright medium blue. "),
    "producto-plateado": ("3:4", [COLLAR / "collar-signe-3.jpg"],
        "Edit the reference product photo: keep exactly the same silver necklace, angle, white background and "
        "lighting, but the name now reads exactly \"Paula\" (capital P, then a-u-l-a) in the same silver signature "
        "script, and the teardrop crystal is soft pink. "),
    # puesto, sin cara
    "modelo-tirantes": ("3:4", [COLLAR / "collar-signe-1.jpg", "aros-boucle"],
        "Quiet-luxury editorial jewelry photo in soft natural daylight against a pale grey wall. A young woman with "
        "light brown hair pulled back, wearing a white ribbed cotton tank top; the frame cuts off just below her nose, "
        "from her lips down to her chest. Around her neck she wears " + DISENO.format(metal="gold") + ", the name "
        "reading exactly \"Elena\" and the teardrop crystal soft yellow; in her ear she wears {aros-boucle}. Natural skin "
        "texture, fine film grain. "),
    "modelo-hombro": ("3:4", [COLLAR / "collar-signe-1.jpg", "reloj-lune", "anillo-nuit"],
        "Quiet-luxury editorial jewelry photo in soft natural daylight against a warm off-white wall. A young woman in "
        "a white strapless top rests one hand on her opposite shoulder; the frame cuts off just below her nose, from "
        "her lips down to her chest. Around her neck she wears " + DISENO.format(metal="gold") + ", the name reading "
        "exactly \"Carmen\" and the teardrop crystal green. On the wrist of the hand on her shoulder she wears "
        "{reloj-lune}, and on one finger {anillo-nuit}. Natural skin texture, fine film grain. "),
}


def generar(toma, n, refs_dir):
    formato, refs, escena = TOMAS[toma]
    rutas = []
    for r in refs:
        if isinstance(r, str):
            escena = escena.replace("{" + r + "}", PIEZA[r]); rutas.append(refs_dir / f"{r}.jpg")
        else:
            rutas.append(r)
    try:
        urls = [higgsfield_client.upload_file(r) for r in rutas]
        res = higgsfield_client.subscribe(MODELO, arguments={
            "prompt": escena + NO, "image_urls": urls, "aspect_ratio": formato,
            "resolution": "2k", "quality": "high", "enhance_prompt": False})
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
    if "--n" in args:
        i = args.index("--n"); veces = int(args[i + 1]); del args[i:i + 2]
    refs_dir = pathlib.Path(args[0]); SALIDA.mkdir(parents=True, exist_ok=True)
    trabajos = [(t, n) for t in (args[1:] or list(TOMAS)) for n in range(1, veces + 1)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
        for toma, r in ex.map(lambda tn: generar(tn[0], tn[1], refs_dir), trabajos):
            print(toma, "->", r)
