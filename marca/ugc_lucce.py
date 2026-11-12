"""UGC del Collar Signé «abrir la cajita» (12-nov, Edu: replicar con IA los planos de un anuncio de Lucce Jewelry,
oficina/referencias/lucce-2026-11-12/planos.jpg). Se copia la ESTRUCTURA (8 planos, el collar manda y la chica casi
no sale), no la persona: la chica es nuestra. Collar «Carmen» con lágrima verde, igual que la foto 1 de la ficha
(producto-verde-carmen-v2: letra, cola ondulada que acaba en anilla, lágrima en el punto más bajo de la cadena) y la
cajita de terciopelo beige de QIUHAN, que es la que recibe la clienta.
    python marca/ugc_lucce.py ancla --n 2                              → marca/fotos-ia/ugc-lucce/ancla-1.png …
    python marca/ugc_lucce.py caja-cara caja-mano … --ancla <png> [--n 2]
Tomas: caja-cara, caja-mano, delante, colgando, abrochar, pellizco, pecho, final (o «todas»).
REVISAR a tamaño real antes de animar: «Carmen» bien escrito y con la misma letra, UNA lágrima en la cadena (forma de
U, nunca colgando del nombre ni de una cadenita en Y), anillas a los dos lados del nombre y la misma cara.
Imagen: API de Higgsfield (flare = GPT Image 2.5), ~0,13 $ por foto en 2K.
"""
import concurrent.futures, pathlib, sys, urllib.request
from PIL import Image
import higgsfield_client
from portada_navidad import MODELO

RAIZ = pathlib.Path(__file__).resolve().parent.parent
REFS = RAIZ / "marca" / "referencias-reales"
COLLAR = RAIZ / "marca" / "fotos-ia" / "collar" / "producto-verde-carmen-v2.jpg"
CAJITA = REFS / "qiuhan-cajita-collar.jpg"
SALIDA = RAIZ / "marca" / "fotos-ia" / "ugc-lucce"

CHICA = ("a young Spanish woman of about 28 with dark brown hair pulled back into a smooth low bun, a few loose strands, "
         "light olive skin with real texture and a few freckles, natural minimal makeup with a soft rosy lip, brown eyes, "
         "wearing a plain mocha-brown satin camisole with thin straps")
COLLAR_TXT = ("a fine gold cable-chain necklace EXACTLY like the necklace in the reference product photo: the name "
              "\"Carmen\" cut from a flat mirror-polished gold sheet in the same handwritten signature lettering (tall "
              "looping capital C, then a-r-m-e-n), sitting diagonally on one side of the chain; the upper chain is "
              "fixed with a tiny jump ring to the top of the capital C, and the last letter ends in a gentle wavy tail "
              "that finishes in a tiny ring where the chain continues; two or three links further, at the lowest point "
              "of the chain, a single faceted emerald-green teardrop crystal in a small gold four-prong setting hangs "
              "straight down on its own bail, threaded on the main chain. Only ONE teardrop; nothing hangs from the name "
              "and there is no Y-shaped extra chain. The name is spelled exactly C-a-r-m-e-n")
CAJA_TXT = ("a small square jewelry box covered in soft beige velvet, with a rounded hinged lid standing open, exactly "
            "like the beige velvet box in the reference photo (no logo, no text on it)")
LOOK = ("Authentic vertical smartphone video frame filmed at home: plain light warm-grey wall behind, a dark-red dried "
        "flower arrangement softly out of focus at one side, soft natural window daylight from the front, slight "
        "phone-camera grain, natural imperfect skin, candid UGC look, not a studio photo, not retouched. No text, no "
        "logo, no watermark.")

TOMAS = {
    "ancla": (CHICA + ", seen from the waist up, facing the phone camera at eye level with a calm, warm expression, her "
              "face fully visible, wearing " + COLLAR_TXT + ". " + LOOK, False),
    "caja-cara": ("The same woman as the reference, seen from the waist up, facing the camera, holds up with both hands "
                  "at chest height " + CAJA_TXT + "; inside the box, on the beige velvet, lies " + COLLAR_TXT +
                  ", the name readable. Her neck is bare (she is not wearing any necklace yet). " + LOOK, True),
    "caja-mano": ("Close-up: a woman's hand with natural nude nails holds " + CAJA_TXT + " towards the camera, filling "
                  "most of the frame; inside, laid flat on the beige velvet, " + COLLAR_TXT + ", the name large, sharp "
                  "and fully readable, the green teardrop next to it. The wall behind is out of focus. " + LOOK, True),
    "delante": ("The same woman as the reference, facing the camera, holds " + COLLAR_TXT + " up by the chain with "
                "both hands in front of her lower face so it hangs in the foreground at the height of her chin, the name "
                "and the green teardrop sharp in focus; her face is softly behind it. Her neck is bare. " + LOOK, False),
    "colgando": ("Close-up of " + COLLAR_TXT + " hanging and gently swaying in the air in front of a plain light "
                 "warm-grey wall, held from above out of frame: the name \"Carmen\" large, sharp and perfectly "
                 "readable, the green teardrop below it. No person visible. " + LOOK, False),
    "abrochar": ("The same woman as the reference, seen from the waist up, facing the camera, both hands raised behind "
                 "her neck fastening the clasp, elbows out, wearing " + COLLAR_TXT + "; the name rests on her "
                 "collarbone, visible. " + LOOK, False),
    "pellizco": ("Close-up of the same woman's neck and collarbone, her lips and chin at the top of the frame and her "
                 "eyes cut off; with the fingertips of both hands she gently holds the chain on each side of the name to "
                 "show it, wearing " + COLLAR_TXT + "; the name sharp and readable on her skin. " + LOOK, False),
    "pecho": ("Close-up of the same woman's collarbone and upper chest, her chin just at the top edge, both hands "
              "softly resting at the sides of the frame, wearing " + COLLAR_TXT + " resting on her skin, the name and the "
              "green teardrop sharp. " + LOOK, False),
    "final": ("The same woman as the reference, seen from the waist up, looking calmly at the camera, both hands "
              "softly framing the necklace on her chest with open fingers, wearing " + COLLAR_TXT + ". " + LOOK, False),
}


def recorte_nombre():
    """Recorte del nombre de la foto de la ficha, para que la letra sea la misma en todas las tomas."""
    p = SALIDA / "ref-nombre-carmen.jpg"
    if not p.exists():
        Image.open(COLLAR).convert("RGB").crop((620, 1050, 1340, 1700)).save(p, quality=95)
    return p


def generar(prompt, destino, refs, res):
    try:
        r = higgsfield_client.subscribe(MODELO, arguments={
            "prompt": prompt, "image_urls": refs, "aspect_ratio": "9:16", "resolution": res,
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
    ancla = a[a.index("--ancla") + 1] if "--ancla" in a else None
    SALIDA.mkdir(parents=True, exist_ok=True)
    pedidas = [t for t in TOMAS if t != "ancla"] if "todas" in a else [t for t in a if t in TOMAS]
    sube = lambda p: higgsfield_client.upload_file(pathlib.Path(p))
    base = ([sube(ancla)] if ancla else []) + [sube(COLLAR), sube(recorte_nombre())]
    caja = sube(CAJITA)
    trabajos = [(TOMAS[t][0], SALIDA / f"{t}-{k + 1}.png", base + ([caja] if TOMAS[t][1] else []))
                for t in pedidas for k in range(n)]
    with concurrent.futures.ThreadPoolExecutor(4) as ex:
        for linea in ex.map(lambda tr: generar(tr[0], tr[1], tr[2], res), trabajos):
            print(linea, flush=True)
