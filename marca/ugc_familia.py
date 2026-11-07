"""Vídeos UGC del Collar Signé para regalar en familia (7-nov, Edu: «un vídeo que sea para ti y para tu hija, otro para
tus dos hijas… hacer más recurrencia de las promos, que son jugosas»). Empujan la promo real de Black Friday
(2.ª pieza al 50 %, 3.ª gratis, hasta el 5-dic): 2 collares = 74,93 €, 3 collares = 99,90 €.
Mismo flujo que ugc_collar.py: primero el ANCLA (las caras juntas), se elige, y los demás planos la llevan de referencia
junto con las fotos REALES del collar. API de Higgsfield (flare, ~0,13 $ por foto en 2K), en 9:16 directamente para
que no se corten las caras al recortar.
    python marca/ugc_familia.py <version> ancla --n 2              → marca/fotos-ia/ugc-<version>/ancla-1.png …
    python marca/ugc_familia.py <version> palmas cierre … --ancla <png> [--n 2]
    versiones: madre-hija (Elena + Sara) · dos-hijas (Ana, la madre, + Marta y Laura)
Luego: ugc_animar.py --carpeta ugc-<version> … y ugc_montaje.py --carpeta ugc-<version> --tarjeta dos|tres
Las hijas son ADULTAS (20-28 años). REVISAR a tamaño real: cada nombre bien escrito, UNA lágrima por collar, pequeña,
ensartada en el punto más bajo de la cadena (nunca colgando del nombre), y las mismas caras en todos los planos.
"""
import concurrent.futures, pathlib, sys, urllib.request
from dotenv import load_dotenv

RAIZ = pathlib.Path(__file__).resolve().parent.parent
load_dotenv(RAIZ / ".env.local")
import higgsfield_client
from collar_ia import COLLAR_REAL, DISENO
from portada_navidad import MODELO

PIEZA = (DISENO.format(metal="gold") + ". The necklace is SUBTLE and delicate: a very fine chain, and the teardrop "
         "crystal is SMALL (about 7 mm long, no bigger than the capital letter of the name). Exactly like the real "
         "photos of the necklace provided (same shape and setting; only the name and the crystal colour change). "
         "Only ONE teardrop per necklace, threaded on the chain at its lowest point, never hanging from the name.")


def collar(nombre, color):
    return f"a necklace whose name reads exactly \"{nombre}\" with a {color} teardrop crystal"


FAMILIAS = {
    "madre-hija": {
        "personas": {
            "madre": ("a Spanish woman of about 52 with shoulder-length dark-blonde hair with a little natural grey, warm "
                      "light skin with real texture and soft smile lines, natural makeup, small pearl stud earrings, "
                      "wearing a soft camel V-neck sweater"),
            "hija": ("her adult daughter, a Spanish woman of about 25 with long straight dark-brown hair, light olive "
                     "skin with real texture, natural minimal makeup, wearing a white cotton shirt open at the collar"),
        },
        "collares": {"madre": ("Elena", "clear emerald green"), "hija": ("Sara", "clear light sky-blue")},
        "look": ("Shot like an authentic vertical smartphone video frame at home in late afternoon: a cosy living room "
                 "with warm lamp light, a beige sofa with a knit blanket and, far behind and out of focus, the warm "
                 "fairy lights of a small Christmas tree as soft bokeh; slight phone-camera grain, natural imperfect "
                 "skin, candid UGC look, not a studio photo, not retouched. No text, no logo, no watermark."),
    },
    "dos-hijas": {
        "personas": {
            "madre": ("a Spanish woman of about 55 with a short chestnut bob, warm skin with real texture and smile "
                      "lines, natural makeup, wearing a cream cable-knit sweater with a round neck open at the throat"),
            "mayor": ("her older adult daughter, a Spanish woman of about 28 with long wavy light-brown hair, fair warm "
                      "skin, natural makeup, wearing a black fine-knit top with a scoop neckline"),
            "pequena": ("her younger adult daughter, a Spanish woman of about 22 with dark hair in a loose low bun, "
                        "light olive skin, natural minimal makeup, wearing a pale blue cotton shirt open at the collar"),
        },
        "collares": {"madre": ("Ana", "clear violet purple"), "mayor": ("Marta", "clear deep red"),
                     "pequena": ("Laura", "clear soft pink")},
        "look": ("Shot like an authentic vertical smartphone video frame on a weekend morning: a bright kitchen with "
                 "white tiles and a light wooden table, coffee cups and a vase of eucalyptus, soft natural daylight from "
                 "a big window; slight phone-camera grain, natural imperfect skin, candid UGC look, not a studio photo, "
                 "not retouched. No text, no logo, no watermark."),
    },
}


def tomas(version):
    F = FAMILIAS[version]
    P, C, look = F["personas"], {k: collar(*v) for k, v in F["collares"].items()}, F["look"]
    pieza = "Each necklace is " + PIEZA + " "
    misma = "Same people as in the reference image (same faces, hair and clothes). "
    if version == "madre-hija":
        return {
            "ancla": ("Vertical phone selfie held by the daughter at arm's length: " + P["madre"] + " and " + P["hija"]
                      + ", cheek to cheek on the sofa, both laughing softly at the camera, faces fully visible, seen "
                      "from the chest up. The mother wears " + C["madre"] + "; the daughter wears " + C["hija"] + ". "
                      + pieza + look),
            "palmas": ("Close-up from above of two open palms held side by side towards the camera: on the left an "
                       "older woman's hand with a thin gold wedding band and a camel knit sleeve, on the right a younger "
                       "woman's hand with a white cotton cuff. In the left palm rests, loosely coiled, " + C["madre"]
                       + "; in the right palm, " + C["hija"] + ". Both cursive names lie flat and fully readable. "
                       + misma + pieza + look),
            "cierre": ("The daughter stands behind her seated mother and fastens the necklace clasp at the back of her "
                       "mother's neck, looking down at it with a tender smile; the mother smiles at the camera and "
                       "touches the pendant at her collarbone. The mother wears " + C["madre"] + ", the name visible on "
                       "her collarbone; the daughter wears " + C["hija"] + ". " + misma + pieza + look),
            "cuellos": ("Close-up of two necklines side by side, the mother's camel V-neck on the left and the "
                        "daughter's open white collar on the right, their chins and smiling lips at the top of the "
                        "frame and their eyes cut off; they lean towards each other. On the left, " + C["madre"]
                        + "; on the right, " + C["hija"] + ". Both names sharp and readable. " + misma + pieza + look),
        }
    return {
        "ancla": ("Vertical phone selfie held by the younger daughter at arm's length: " + P["madre"] + " in the "
                  "middle, hugged by " + P["mayor"] + " on one side and " + P["pequena"] + " on the other, the three "
                  "smiling at the camera, faces fully visible, seen from the chest up. The mother wears " + C["madre"]
                  + "; the older daughter wears " + C["mayor"] + "; the younger daughter wears " + C["pequena"] + ". "
                  + pieza + look),
        "mesa": ("Overhead phone shot of a light wooden kitchen table: on a linen napkin lie three necklaces side by side, "
                 "each one laid out in a loose U shape with its cursive name flat and fully readable - from left to "
                 "right " + C["mayor"] + ", " + C["pequena"] + " and " + C["madre"] + "; a woman's hand with a cream "
                 "knit sleeve is placing the third one; coffee cups at the edge of the frame. " + pieza + look),
        # 7-nov: la 1.ª vez volvió a meter a la madre (salían las tres): ahora se insiste en que son SOLO DOS
        "hermanas": ("Vertical phone selfie of ONLY TWO young women, the two sisters, cheek to cheek at the kitchen "
                     "table, laughing, faces fully visible, from the chest up. EXACTLY TWO people in the frame: the "
                     "mother from the reference image is NOT in this shot. On the left " + P["mayor"] + " wearing "
                     + C["mayor"] + "; on the right " + P["pequena"] + " wearing " + C["pequena"] + ". Same two "
                     "daughters as in the reference image (same faces, hair and clothes). " + pieza + look),
        "cuello": ("Close-up of the mother's neck and collarbone above her cream sweater, her chin and smiling lips at "
                   "the top of the frame and her eyes cut off; one fingertip gently touches the gold name of "
                   + C["madre"] + ", sharp and readable. " + misma + pieza + look),
    }


def generar(prompt, destino, refs, res):
    for aspecto in ("9:16", "3:4"):
        try:
            r = higgsfield_client.subscribe(MODELO, arguments={
                "prompt": prompt, "image_urls": refs, "aspect_ratio": aspecto, "resolution": res,
                "quality": "high", "enhance_prompt": False})
        except Exception as e:
            if aspecto == "9:16" and "aspect" in str(e).lower():
                continue
            return f"{destino.stem}: ERROR {type(e).__name__}: {e}"
        imgs = (r or {}).get("images") or []
        if not imgs:
            return f"{destino.stem}: SIN IMAGEN {r}"
        urllib.request.urlretrieve(imgs[0]["url"], destino)
        return f"{destino.stem} ({aspecto}): {destino}"
    return f"{destino.stem}: ERROR sin formato válido"


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] not in FAMILIAS:
        sys.exit(__doc__)
    version = a[0]
    res = "4k" if "--4k" in a else "2k"
    n = int(a[a.index("--n") + 1]) if "--n" in a else 1
    ancla = a[a.index("--ancla") + 1] if "--ancla" in a else None
    salida = RAIZ / "marca" / "fotos-ia" / f"ugc-{version}"
    salida.mkdir(parents=True, exist_ok=True)
    T = tomas(version)
    pedidas = [t for t in a[1:] if t in T]
    refs = ([higgsfield_client.upload_file(pathlib.Path(ancla))] if ancla else []) + \
           [higgsfield_client.upload_file(pathlib.Path(c)) for c in COLLAR_REAL]
    trabajos = [(T[t], salida / f"{t}-{k + 1}.png") for t in pedidas for k in range(n)]
    with concurrent.futures.ThreadPoolExecutor(4) as ex:
        for linea in ex.map(lambda tr: generar(tr[0], tr[1], refs, res), trabajos):
            print(linea, flush=True)
