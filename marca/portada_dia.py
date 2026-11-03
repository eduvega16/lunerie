"""Fotos de la portada «para cada día» (3-nov, Edu): como el collage de Navidad pero sin caras (el encuadre corta por
debajo de la nariz) y de día: manos cerca de la cara, con una taza, una copa o en el pelo, para que en el móvil se
vean bien las joyas y el reloj juntos, y que se lean como piezas para llevar a diario, no para una ocasión especial.
API de Higgsfield (flare = GPT Image 2.5, ~0,13 $ por foto); clave HF_KEY en .env.local.
    python marca/portada_dia.py <carpeta_refs> [toma ...] [--n 2]
<carpeta_refs>: la primera foto de cada producto, con su handle de nombre (reloj-lune.jpg, anillo-nuit.jpg…).
Salidas en marca/fotos-ia/portada-dia/<toma>-<n>.png (las tomas se llaman como los huecos del collage).
"""
import concurrent.futures, pathlib, sys, urllib.request
import higgsfield_client
from portada_navidad import MODELO, PIEZA as _PIEZA

RAIZ = pathlib.Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "marca" / "fotos-ia" / "portada-dia"

PIEZA = {**_PIEZA,
         "anillo-duo": "a thin open adjustable gold ring topped by two small rectangular enamel plates side by side, a "
                       "longer one in matte beige-grey and a shorter one in deep navy blue",
         "anillo-etoile": "a thick, rounded, highly polished gold band with one rectangular emerald-cut green stone set "
                          "flush into the top",
         "reloj-perle": "a small oval gold watch with a cream dial on a bracelet of open gold links, each link holding one "
                        "small white pearl"}
ESTILO = ("Quiet-luxury editorial photo for a jewelry and watch brand, about wearing it every day. Soft natural "
          "daylight from a window, calm warm-neutral palette: ivory, cream, oatmeal knit, white linen, pale stone. "
          "Close crop on hands, wrist, neck and jawline: the woman's face is NOT shown - the frame cuts off below "
          "her nose, at most her lips and chin are visible. Natural skin texture, short natural nails with nude "
          "polish, minimal makeup. Shot on a full-frame camera with a 50mm lens, shallow depth of field, fine film "
          "grain, clean composition with breathing room. The jewelry and the watch are the clear focus, sharp and "
          "well lit. Every piece of jewelry and every watch must be EXACTLY like the reference images - same shape, "
          "size, colours and details; the watches are small and delicate, do not make them bigger and do not "
          "redesign them. No text, no logos and no brand names anywhere in the image, nothing written on the watch "
          "dials. ")
TOMAS = {
    # En el móvil es la grande: el reloj Lune, el anillo Nuit y el collar Lune juntos
    "izquierda": ("3:4", ["reloj-lune", "anillo-nuit", "collar-lune"],
                  "A woman in a soft cream knit cardigan with a deep V neckline holds a white ceramic coffee cup with "
                  "both hands just below her lips, early in the morning. On her left wrist she wears {reloj-lune}, the "
                  "dial turned towards the camera; on one finger of her right hand she wears {anillo-nuit}; on the bare "
                  "skin of her neck, above the neckline, she wears {collar-lune}. Blurred bright kitchen window behind."),
    # En PC es la del centro (apaisada): la mano en el pelo, con aros, reloj y anillo
    "centro": ("4:3", ["reloj-maille", "aros-boucle", "anillo-duo"],
               "Close-up three-quarter profile of a woman's jaw, neck and ear as she tucks her hair behind her ear with "
               "one hand; her eyes and nose are out of the frame. She wears {aros-boucle} in her ear, {reloj-maille} on "
               "the wrist of the raised hand and {anillo-duo} on one finger of that hand. Crisp white linen shirt, "
               "plain pale stone wall behind, soft daylight."),
    # La tercera: una copa al mediodía, con el reloj de correa y los pendientes con lágrima
    "derecha": ("3:4", ["reloj-sepia", "pendientes-larme", "anillo-etoile"],
                "A woman at a sunny café terrace at lunchtime holds a stemmed glass of white wine near her chin; the "
                "frame cuts off just below her nose, her ear and jaw visible. On the wrist of the hand holding the "
                "glass she wears {reloj-sepia}, clearly visible; on that hand {anillo-etoile}; in her ear "
                "{pendientes-larme}. Oatmeal fine-knit top, blurred white tablecloth and greenery behind."),
}


def generar(toma, n, carpeta):
    formato, piezas, escena = TOMAS[toma]
    for h in piezas:
        escena = escena.replace("{" + h + "}", PIEZA[h])
    try:
        refs = [higgsfield_client.upload_file(carpeta / f"{h}.jpg") for h in piezas]
        res = higgsfield_client.subscribe(MODELO, arguments={
            "prompt": ESTILO + escena, "image_urls": refs, "aspect_ratio": formato,
            "resolution": "2k", "quality": "high", "enhance_prompt": False})
    except Exception as e:  # fallo, moderación o sin créditos: no se da por bueno
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
    carpeta = pathlib.Path(args[0]); SALIDA.mkdir(parents=True, exist_ok=True)
    elegidas = args[1:] or list(TOMAS)
    trabajos = [(t, n) for t in elegidas for n in range(1, veces + 1)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
        for toma, r in ex.map(lambda tn: generar(tn[0], tn[1], carpeta), trabajos):
            print(toma, "->", r)
