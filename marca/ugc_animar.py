"""Anima los planos del vídeo UGC del Collar Signé con Kling 3.0 por la API de Higgsfield (5-nov). Sin sonido (la voz va
aparte, en montaje). Recorta cada foto a 9:16 antes de mandarla (con su desplazamiento para no cortar la mano).
    python marca/ugc_animar.py ancla-1 cuello-1 … [--modo pro|std] [--seg 4]   → marca/fotos-ia/ugc-collar/clips/<plano>.mp4
REVISAR cada clip: el nombre «Marta» y la lágrima no deben deformarse (Kling a veces lo hace al final: usar el principio).
"""
import concurrent.futures, pathlib, sys, urllib.request
from dotenv import load_dotenv
from PIL import Image
import higgsfield_client

RAIZ = pathlib.Path(__file__).resolve().parent.parent
load_dotenv(RAIZ / ".env.local")
CARPETA = RAIZ / "marca" / "fotos-ia" / "ugc-collar"
CLIPS = CARPETA / "clips"

FIJO = (" Keep the necklace exactly as in the image: the same gold cursive name and the same single teardrop "
        "crystal, which keeps EXACTLY its colour from the image the whole time (it never changes colour), no extra "
        "jewelry, letters do not change or melt. Same face, natural skin. Realistic handheld "
        "smartphone footage, subtle natural camera shake, soft daylight.")
MOVIMIENTO = {
    "ancla": "She smiles warmly at the camera, tilts her head slightly and touches the necklace near her collarbone "
             "with her fingertips.",
    "cuello": "Her fingers gently lift the blue teardrop pendant a little and let it rest back on her skin while she "
              "smiles softly.",
    "nombre": "She holds the gold name between her fingers and tilts it slowly so the polished letters catch the "
              "window light, looking down at it with a soft smile.",
    "mirada": "She looks down at the necklace touching it with her fingers, then lifts her eyes to the camera with a "
              "genuine happy smile.",
    # tomas «dorada» (5-nov, ideas de Pinterest)
    "colgando": "The necklace hanging from her fingers sways gently and turns a little so the gold name catches the "
                "warm light; she smiles at the camera.",
    "palma": "Her open palm moves very slightly towards the camera and the warm light glints on the gold letters; the "
             "necklace stays resting in her palm.",
    "cierre": "She finishes fastening the clasp behind her neck, lets her hair fall and turns her head slightly towards "
              "the camera with a soft smile.",
    "espejo": "Mirror selfie: she gently adjusts the necklace at her collarbone with her fingertips while holding the "
              "phone still, small natural movement.",
}
# 7-nov: vídeos de familia (ugc_familia.py): varios collares en el plano y movimientos propios de cada carpeta
FIJO_VARIOS = (" Keep every necklace exactly as in the image: the same gold cursive names letter by letter and, on each "
               "necklace, its single small teardrop crystal, which keeps EXACTLY its colour from the image the whole "
               "time (it never changes colour); letters do not change or melt; no extra jewelry. Same faces, natural "
               "skin. Realistic handheld smartphone footage, subtle natural camera shake.")
MOV_CARPETA = {
    "ugc-madre-hija": {
        "ancla": "Selfie: mother and daughter laugh softly and press their cheeks together; the selfie arm moves "
                 "slightly.",
        "palmas": "Both open palms move very slightly towards the camera and the warm lamp light glints on the gold "
                  "letters; the two necklaces stay resting in the palms.",
        "cierre": "The daughter finishes fastening the clasp behind her mother's neck and rests her hands on her "
                  "mother's shoulders; the mother smiles at the camera and touches the pendant.",
        "cuellos": "They lean their heads together and laugh softly; small natural movement, the necklaces sway "
                   "slightly.",
    },
    "ugc-dos-hijas": {
        "ancla": "Selfie: the three of them laugh and squeeze closer together; the selfie arm moves slightly.",
        "mesa": "The hand finishes placing the third necklace on the linen napkin and pulls back slowly; the other two "
                "necklaces stay completely still.",
        "hermanas": "Selfie: the two sisters laugh and press their cheeks together; the selfie arm moves slightly.",
        "cuello": "Her fingertip gently touches the gold name on her collarbone, then she smiles; the teardrop sways "
                  "slightly.",
    },
}
# 12-nov: UGC «abrir la cajita» (ugc_lucce.py, estructura del anuncio de Lucce): una sola chica y un solo collar → FIJO
MOV_UNO = {
    "ugc-lucce": {
        "caja-cara": "She holds the open beige velvet box still towards the camera at chest height, smiles softly and "
                     "tilts it very slightly so the necklace inside catches the light.",
        "caja-mano": "The hand holding the open box moves very slightly closer to the camera and the light glints on the "
                     "gold letters; the necklace stays lying still in the box.",
        "delante": "She lifts the necklace a little with both hands, holding the chain on each side of the name, and "
                   "smiles softly at the camera.",
        "colgando": "The necklace hanging in the air sways gently and turns a little so the gold name catches the light.",
        "abrochar": "She finishes fastening the clasp behind her neck, lowers her hands slowly and smiles softly at the "
                    "camera.",
        "pellizco": "Her fingertips gently hold the chain on each side of the name and tilt it slightly so the polished "
                    "letters catch the light; her lips smile softly.",
        "pecho": "Her hands slowly move in to frame the necklace on her chest, small natural movement; the teardrop sways "
                 "slightly.",
        "ancla": "She looks calmly at the camera, raises both hands and softly frames the necklace on her chest with open "
                 "fingers, then smiles.",
    },
}
DESPLAZAMIENTO = {"nombre": 0.10, "colgando": 0.0, "espejo": 0.75}   # dónde empieza el recorte 9:16 (0 = izquierda, 0.5 = centro)


def recorte_916(png):
    im = Image.open(png).convert("RGB")
    w = round(im.height * 9 / 16)
    x0 = round((im.width - w) * DESPLAZAMIENTO.get(png.stem.rsplit("-", 1)[0], 0.5))
    destino = CLIPS / f"{png.stem}-916.jpg"
    im.crop((x0, 0, x0 + w, im.height)).save(destino, quality=95, subsampling=0)
    return destino


def animar(plano, modo, seg):
    try:
        url = higgsfield_client.upload_file(recorte_916(CARPETA / f"{plano}.png"))
        clave, propios = plano.rsplit("-", 1)[0], MOV_CARPETA.get(CARPETA.name)
        uno = MOV_UNO.get(CARPETA.name)
        prompt = (uno[clave] + FIJO if uno else
                  propios[clave] + FIJO_VARIOS if propios else MOVIMIENTO[clave] + FIJO)
        r = higgsfield_client.subscribe(f"kling-video/v3.0/{modo}/image-to-video", arguments={
            "image_url": url, "prompt": prompt, "duration": seg,
            "sound": "off", "aspect_ratio": "9:16"})
    except Exception as e:
        return f"{plano}: ERROR {type(e).__name__}: {e}"
    v = (r or {}).get("video") or ((r or {}).get("videos") or [None])[0]
    if not v:
        return f"{plano}: SIN VÍDEO {r}"
    destino = CLIPS / f"{plano}.mp4"
    urllib.request.urlretrieve(v["url"], destino)
    return f"{plano}: {destino}"


if __name__ == "__main__":
    a = sys.argv[1:]
    modo = a[a.index("--modo") + 1] if "--modo" in a else "pro"
    seg = int(a[a.index("--seg") + 1]) if "--seg" in a else 4
    if "--carpeta" in a:
        CARPETA = RAIZ / "marca" / "fotos-ia" / a[a.index("--carpeta") + 1]
        CLIPS = CARPETA / "clips"
    planos = [p for p in a if (CARPETA / f"{p}.png").exists()]
    CLIPS.mkdir(parents=True, exist_ok=True)
    with concurrent.futures.ThreadPoolExecutor(4) as ex:
        for linea in ex.map(lambda p: animar(p, modo, seg), planos):
            print(linea, flush=True)
