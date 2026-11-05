"""Fotos de partida del vídeo UGC del Collar Signé (5-nov, Edu: «una modelo de IA con el collar, varios planos de cara,
cuello, enseñándolo con la mano, como un vídeo realista con una voz por detrás»).
Una misma chica en todas las tomas: primero se genera el ANCLA (la cara), se elige, y las demás tomas la llevan de
referencia junto con las fotos REALES del collar. API de Higgsfield (flare = GPT Image 2.5, ~0,13 $ por foto en 2K).
    python marca/ugc_collar.py ancla --n 2                       → marca/fotos-ia/ugc-collar/ancla-1.png, ancla-2.png
    python marca/ugc_collar.py cuello mano espejo ... --ancla marca/fotos-ia/ugc-collar/ancla-1.png [--n 2] [--4k]
REVISAR a tamaño real: el nombre «Marta» bien escrito, la lágrima azul colgando y la misma cara en todas.
"""
import concurrent.futures, pathlib, sys, urllib.request
import higgsfield_client
from collar_ia import COLLAR_REAL, DISENO
from portada_navidad import MODELO

RAIZ = pathlib.Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "marca" / "fotos-ia" / "ugc-collar"

CHICA = ("the same young Spanish woman of about 27 with wavy chestnut-brown hair worn down, light olive skin with real "
         "texture and a few freckles, natural minimal makeup, brown eyes, wearing a plain white ribbed tank top")
LOOK = ("Shot like an authentic vertical smartphone video frame filmed at home: bright bedroom with a window and linen "
        "curtains out of focus behind her, soft natural daylight, slight phone-camera grain, natural imperfect skin, "
        "not a studio photo, not retouched, candid UGC look. No text, no logo, no watermark.")
COLLAR = ("Around her neck she wears " + DISENO.format(metal="gold") + ", the name reading exactly \"Marta\" and the "
          "teardrop crystal a clear sapphire blue, exactly like the real photos of the necklace provided. ")

TOMAS = {
    "ancla": CHICA + ", seen from the chest up, facing the phone camera at eye level with a relaxed, warm half-smile, "
             "her face fully visible. " + COLLAR + "Her right hand is resting lightly near her collarbone. " + LOOK,
    "cuello": "Close-up of the woman's neck and collarbone, her chin and lips at the top of the frame and her eyes "
              "cut off, same woman as the reference. " + COLLAR + "Her fingertips hold the blue teardrop pendant "
              "gently. " + LOOK,
    "mano": "The same woman as the reference, face slightly out of focus and smiling in the background, while her hand "
            "in the foreground lifts the blue teardrop pendant and the chain towards the camera between thumb and "
            "index finger, as if showing it to a friend on a video call. " + COLLAR + LOOK,
    "nombre": "Close-up from the side: the same woman as the reference lifts the gold name part of her necklace "
              "between two fingers to show it, her jaw and cheek visible, eyes looking down at it with a soft smile. "
              + COLLAR + "The cursive name is large and sharp in the frame. " + LOOK,
    "mirada": CHICA + ", seen from the chest up, looking down at the necklace she touches with one hand and then "
              "starting to look up at the camera with a genuine happy smile, same woman as the reference. " + COLLAR + LOOK,
    "espejo": "The same woman as the reference, filmed from slightly below the chin to the chest, tilting her head to "
              "one side so the necklace catches the window light, hand sweeping her hair behind her shoulder. "
              + COLLAR + LOOK,
}


def subir(r):
    return higgsfield_client.upload_file(pathlib.Path(r))


def generar(toma, n, refs, res):
    try:
        r = higgsfield_client.subscribe(MODELO, arguments={
            "prompt": TOMAS[toma], "image_urls": refs, "aspect_ratio": "3:4", "resolution": res,
            "quality": "high", "enhance_prompt": False})
    except Exception as e:
        return f"{toma}-{n}: ERROR {type(e).__name__}: {e}"
    imgs = (r or {}).get("images") or []
    if not imgs:
        return f"{toma}-{n}: SIN IMAGEN {r}"
    destino = SALIDA / f"{toma}-{n}.png"
    urllib.request.urlretrieve(imgs[0]["url"], destino)
    return f"{toma}-{n}: {destino}"


if __name__ == "__main__":
    a = sys.argv[1:]
    res = "4k" if "--4k" in a else "2k"
    n = int(a[a.index("--n") + 1]) if "--n" in a else 1
    ancla = a[a.index("--ancla") + 1] if "--ancla" in a else None
    tomas = [t for t in a if t in TOMAS]
    SALIDA.mkdir(parents=True, exist_ok=True)
    refs = ([subir(ancla)] if ancla else []) + [subir(c) for c in COLLAR_REAL]
    trabajos = [(t, k + 1) for t in tomas for k in range(n)]
    with concurrent.futures.ThreadPoolExecutor(4) as ex:
        for linea in ex.map(lambda tk: generar(tk[0], tk[1], refs, res), trabajos):
            print(linea, flush=True)
