"""Fotos de la portada de Navidad (1-nov): tres fotos en fila, de noche y con flash, como la portada de Caducci pero
con los colores de Lunerie (terciopelo verde botella y dorados). Cada foto lleva relojes y joyas reales de la tienda.
API de Higgsfield (flare = GPT Image 2.5, ~0,13 $ por foto); clave HF_KEY en .env.local.
    python marca/portada_navidad.py <carpeta_refs> [toma ...] [--n 2]
<carpeta_refs>: la primera foto de cada producto, con su handle de nombre (reloj-lune.jpg, anillo-nuit.jpg…).
Salidas en marca/fotos-ia/portada-navidad/<toma>-<n>.png
"""
import concurrent.futures, pathlib, sys, urllib.request
from dotenv import load_dotenv
import higgsfield_client

RAIZ = pathlib.Path(__file__).resolve().parent.parent
load_dotenv(RAIZ / ".env.local")
MODELO = "marketing-studio/image/flare"
SALIDA = RAIZ / "marca" / "fotos-ia" / "portada-navidad"

# Cómo es cada pieza de verdad (para que la IA no la rediseñe)
PIEZA = {
    # 4-nov (Edu): sacado de las fotos reales (marca/referencias-reales/), no de las de IA; en la muñeca es más grande
    # de lo que lo pintaba («small/tiny» fuera)
    "reloj-lune": "a vintage gold watch with an oval case framed by a twisted rope-pattern gold bezel, a small crown on "
                  "the side and a white oval dial with thin gold baton markers and gold hands; the bracelet is made of "
                  "oval gold links, each holding one oval dark-green stone with light veins in a rope-textured gold "
                  "frame - exactly three on each side of the case, all six the same green - joined by short hinged gold "
                  "links. On the wrist the oval case covers about half the width of the top of the wrist",
    "reloj-galet": "an oval watch with a thick, rounded, highly polished gold case like a smooth pebble, a white dial "
                   "with gold Roman numerals, on a bracelet of polished three-row gold links",
    "reloj-maille": "a small oval gold watch with a white dial on a narrow bracelet of fine gold woven mesh",
    "reloj-sepia": "a small rectangular gold watch with a cream dial and black Roman numerals on a plain brown "
                   "leather strap",
    "anillo-nuit": "a slim polished gold signet ring whose smooth rounded top tapers into a thin band, set with one "
                   "marquise-cut faceted olive-green crystal held flush in a thin smooth gold bezel, its two points "
                   "aligned with the finger (one towards the fingertip); the stone is a little shorter than the finger "
                   "is wide - elegant and delicate, not chunky or oversized",
    "collar-lune": "a very fine gold chain necklace with small round coloured stones (red, blue, green, pink) set "
                   "directly in line into the chain at intervals - the stones are part of the chain, never hanging",
    "pendientes-larme": "small gold huggie hoop earrings, each with one dangling emerald-green teardrop crystal",
    "aros-boucle": "medium U-shaped hoop earrings in smooth polished gold",
}
ESTILO = ("Candid editorial fashion campaign photo for a vintage jewelry and watch brand, Christmas party at night. "
          "Shot on a 35mm film camera with direct on-camera flash: bright flash highlights on skin and gold, deep rich "
          "shadows, visible film grain, slightly warm colour. Interior of an old elegant salon: bottle-green velvet, "
          "antique gold damask wallpaper, warm table lamps and candles in the background. Real women in their "
          "twenties with natural skin texture and glossy dark-red nails. Every piece of jewelry and every watch must "
          "be EXACTLY like the reference images - same shape, size, colours and details; do not redesign them. "
          "No text, no logos and no brand names anywhere in the image, nothing written on the watch dials. ")
TOMAS = {
    "izquierda": ("3:4", ["reloj-galet", "anillo-nuit", "aros-boucle"],
                  "A blonde woman in a black velvet dress sits at an antique desk with old books, talking on a cream "
                  "vintage rotary telephone, the receiver at her ear and the curly cord across her chest. Her other "
                  "hand is raised beside her face with the fingers spread, showing the jewelry. She wears {reloj-galet} "
                  "on that wrist, {anillo-nuit} on one finger and {aros-boucle}. Half-body portrait, she looks at the "
                  "camera with a knowing, amused expression."),
    "centro": ("4:3", ["reloj-lune", "collar-lune", "reloj-maille"],
               "Two friends lounge on a deep bottle-green velvet sofa with old-gold velvet cushions, two champagne "
               "coupes on a small table. The woman on the left has long dark curly hair and an emerald satin slip "
               "dress; she wears {reloj-lune} on her wrist, her hand resting on her knee so the watch is clearly "
               "visible, and {collar-lune}. The woman on the right has straight light-brown hair and a black dress "
               "with long sleeves pushed up; she leans in with her hand near her cheek, wearing {reloj-maille}. Both "
               "look at the camera, relaxed and confident. Wide shot, both full upper bodies and the sofa visible."),
    "derecha": ("3:4", ["reloj-sepia", "pendientes-larme"],
                "Close-up portrait of a young woman with voluminous dark curly hair and red lips, looking sideways out "
                "of frame, holding a champagne coupe near her chin with one hand. On that wrist she wears "
                "{reloj-sepia}, clearly visible in the foreground, and she wears {pendientes-larme}. Bottle-green "
                "velvet behind her."),
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
