"""Fotos de partida de los vídeos UGC del Collar Signé (5-nov, Edu: «una modelo de IA con el collar, varios planos de cara,
cuello, enseñándolo con la mano, como un vídeo realista con una voz por detrás»).
Una misma chica en todas las tomas: primero se genera el ANCLA (la cara), se elige, y las demás tomas la llevan de
referencia junto con las fotos REALES del collar. API de Higgsfield (flare = GPT Image 2.5, ~0,13 $ por foto en 2K).
    python marca/ugc_collar.py ancla --n 2 [--version carmen]          → marca/fotos-ia/ugc-collar[-carmen]/ancla-1.png …
    python marca/ugc_collar.py cuello nombre mirada --ancla <png> [--version carmen] [--n 2] [--4k]
VERSIONES: nombre del collar, color de la lágrima y chica. REVISAR a tamaño real: el nombre bien escrito, UNA sola
lágrima colgando (en «mano» salieron dos: no usar esa toma) y la misma cara en todas.
"""
import concurrent.futures, pathlib, sys, urllib.request
import higgsfield_client
from collar_ia import COLLAR_REAL, DISENO
from portada_navidad import MODELO

RAIZ = pathlib.Path(__file__).resolve().parent.parent

CHICAS = {
    "morena": ("the same young Spanish woman of about 27 with wavy chestnut-brown hair worn down, light olive skin with "
               "real texture and a few freckles, natural minimal makeup, brown eyes, wearing a plain white ribbed tank top"),
    "castana-clara": ("the same young Spanish woman of about 25 with straight light-brown hair with soft honey highlights "
                      "tucked behind one ear, fair warm skin with real texture, natural minimal makeup, green-hazel eyes, "
                      "small gold hoop earrings, wearing a soft cream knit top with a wide scoop neckline"),
}
VERSIONES = {   # nombre, color de la lágrima (en inglés para el prompt), chica, carpeta
    "marta": ("Marta", "a clear sapphire blue", "morena", "ugc-collar"),
    "carmen": ("Carmen", "a clear emerald green", "castana-clara", "ugc-collar-carmen"),
    "carmen-dorada": ("Carmen", "a clear emerald green", "castana-clara", "ugc-collar-carmen-2"),   # tomas_dorada
}
LOOK = ("Shot like an authentic vertical smartphone video frame filmed at home: bright bedroom with a window and linen "
        "curtains out of focus behind her, soft natural daylight, slight phone-camera grain, natural imperfect skin, "
        "not a studio photo, not retouched, candid UGC look. No text, no logo, no watermark.")


def tomas(nombre, color, chica):
    collar = ("Around her neck she wears " + DISENO.format(metal="gold") + f", the name reading exactly \"{nombre}\" "
              f"and the teardrop crystal {color}, exactly like the real photos of the necklace provided (same shape, "
              "same setting; only the name and the crystal colour change). There is only ONE teardrop crystal. ")
    c = CHICAS[chica]
    return {
        "ancla": c + ", seen from the chest up, facing the phone camera at eye level with a relaxed, warm half-smile, "
                 "her face fully visible. " + collar + "Her right hand is resting lightly near her collarbone. " + LOOK,
        "cuello": "Close-up of the woman's neck and collarbone, her chin and lips at the top of the frame and her eyes "
                  "cut off, same woman as the reference. " + collar + "Her fingertips hold the teardrop pendant "
                  "gently. " + LOOK,
        "nombre": "Close-up from the side: the same woman as the reference lifts the gold name part of her necklace "
                  "between two fingers to show it, her jaw and cheek visible, eyes looking down at it with a soft smile. "
                  + collar + "The cursive name is large and sharp in the frame. " + LOOK,
        "mirada": c + ", seen from the chest up, looking down at the necklace she touches with one hand and then "
                  "starting to look up at the camera with a genuine happy smile, same woman as the reference. " + collar + LOOK,
        "espejo": "The same woman as the reference, filmed from slightly below the chin to the chest, tilting her head to "
                  "one side so the necklace catches the window light, hand sweeping her hair behind her shoulder. "
                  + collar + LOOK,
    }


LOOK_DORADA = ("Shot like an authentic vertical smartphone video frame: warm golden-hour sunlight from a window low on one "
               "side, soft warm shadows, beige and sand tones, linen curtain glow, slight phone-camera grain, natural "
               "imperfect skin, candid UGC look, not a studio photo. No text, no logo, no watermark.")


def tomas_dorada(nombre, color, chica):
    """5-nov (Edu: «algo diferente», «la piedra es demasiado grande, el collar es más sutil», «un plano con el collar en
    las manos, quitado del cuello»): ideas de Pinterest (búsqueda «ugc content jewelry»): collar colgando de los dedos,
    en la palma, abrochándolo, selfie en el espejo con la cara tapada por el móvil, luz cálida de atardecer."""
    pieza = (DISENO.format(metal="gold") + f", the name reading exactly \"{nombre}\" and the teardrop crystal {color}. "
             "The necklace is SUBTLE and delicate: a very fine chain, and the teardrop crystal is SMALL (about 7 mm "
             "long, no bigger than the capital letter of the name). Exactly like the real photos of the necklace "
             "provided (same shape and setting; only the name and the crystal colour change). Only ONE teardrop. ")
    c = CHICAS[chica].replace("wearing a soft cream knit top with a wide scoop neckline",
                              "wearing an oversized beige linen shirt, open at the collar")
    sin_collar = "Her neck is bare: she is NOT wearing any necklace, the only necklace is the one in her hand. "
    return {
        "colgando": "Vertical phone video frame: in the foreground, sharp, her hand holds the necklace up by the chain "
                    "between thumb and index finger so it hangs straight down and sways, the name and the small teardrop "
                    "clearly visible, as if she just took it off to show it to the camera; behind it, out of focus, " + c
                    + ", smiling at the camera. " + sin_collar + "The necklace is " + pieza + LOOK_DORADA,
        "palma": "Close-up from above of her open palm held towards the camera, with the necklace resting loosely "
                 "coiled in it, the cursive name lying flat and fully readable and the small teardrop next to it; her "
                 "beige linen sleeve at the edge of the frame. The necklace is " + pieza + LOOK_DORADA,
        "cierre": c + ", seen from behind and slightly to the side at shoulder height, lifting her hair with one hand "
                  "while fastening the necklace clasp at the back of her neck with the other; the name rests on the "
                  "side of her collarbone, visible over her shoulder. The necklace is " + pieza + LOOK_DORADA,
        "espejo": c + ", taking a mirror selfie in a warm sunlit bedroom: the phone covers most of her face, one hand "
                  "lightly touching the necklace at her collarbone; the necklace is clearly visible in the reflection. "
                  "The necklace is " + pieza + LOOK_DORADA,
        "clavicula": "Close-up of her collarbone and neck in warm golden light, her lips and chin at the top of the "
                     "frame; one fingertip slowly tracing the gold name on her skin. Same woman as the reference. "
                     "The necklace is " + pieza + LOOK_DORADA,
    }


def subir(r):
    return higgsfield_client.upload_file(pathlib.Path(r))


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
    ancla = a[a.index("--ancla") + 1] if "--ancla" in a else None
    version = a[a.index("--version") + 1] if "--version" in a else "marta"
    nombre, color, chica, carpeta = VERSIONES[version]
    salida = RAIZ / "marca" / "fotos-ia" / carpeta
    salida.mkdir(parents=True, exist_ok=True)
    T = (tomas_dorada if version.endswith("-dorada") else tomas)(nombre, color, chica)
    pedidas = [t for t in a if t in T]
    refs = ([subir(ancla)] if ancla else []) + [subir(c) for c in COLLAR_REAL]
    trabajos = [(T[t], salida / f"{t}-{k + 1}.png") for t in pedidas for k in range(n)]
    with concurrent.futures.ThreadPoolExecutor(4) as ex:
        for linea in ex.map(lambda tr: generar(tr[0], tr[1], refs, res), trabajos):
            print(linea, flush=True)
