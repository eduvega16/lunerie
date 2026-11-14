"""Reel «Tres en raya» (14-nov; idea de un reel de @lostandfoundshoppe que trajo Edu, en biblioteca/ideas-reels.json).
Tablero de tres en raya de cinta crema sobre terciopelo rojo, visto desde arriba; las X son cruces de cinta y las «O»,
tres piezas redondas de Lunerie: el Collar Signé enrollado (centro), el Reloj Lune cerrado en círculo (abajo a la
izquierda) y el anillo Nuit (arriba a la derecha). Las tres hacen la diagonal: tres en raya = la 3.ª, gratis.

Todo sale de UNA foto final (así nada cambia entre fotogramas):
    python marca/tres_en_raya.py foto [--n 2] [--4k]        → marca/fotos-ia/tres-en-raya/final-<n>.png
    python marca/tres_en_raya.py vacio <final.png> [--n 2]  → …/vacio-<n>.png (la misma foto sin X ni piezas)
    python marca/tres_en_raya.py montar <final.png> <vacio.png>  → …/tres-en-raya-9x16.mp4 y -4x5.mp4
REVISAR la foto final a tamaño real: el nombre «Carmen», UNA lágrima verde en el punto más bajo, el Lune con 3 piedras a
cada lado (verde medio con vetas claras) y el Nuit fino con la piedra marquesa verde oliva.
Imagen: API de Higgsfield (flare = GPT Image 2.5), ~0,13 $ por foto en 2K (0,17 $ en 4K).
"""
import concurrent.futures, pathlib, sys, urllib.request
from dotenv import load_dotenv

RAIZ = pathlib.Path(__file__).resolve().parent.parent
load_dotenv(RAIZ / ".env.local")
SALIDA = RAIZ / "marca" / "fotos-ia" / "tres-en-raya"
REFS = RAIZ / "marca" / "referencias-reales"
FOTOS = RAIZ / "marca" / "fotos-ia"
MODELO = "marketing-studio/image/flare"

TERCIOPELO = ("rich deep Christmas-red crushed velvet (a deep red like red wine, not orange, not pink), laid flat and "
              "smooth so the board reads clearly, with a soft sheen where the light catches the pile")
LUZ = ("Soft, even, warm daylight from above, gentle soft shadows under the jewelry and the tape, true-to-life gold, "
       "crisp focus everywhere. No text, no logo, no watermark, no people, no hands.")

PROMPT_FINAL = (
    "Top-down flat-lay photograph, camera exactly overhead, vertical 9:16 frame. On " + TERCIOPELO + " a game of "
    "noughts and crosses (tic-tac-toe) has been made by hand with strips of cream-white paper masking tape: two "
    "vertical and two horizontal tape strips form the 3x3 board, slightly imperfect and rotated about 8 degrees, the "
    "board centred in the frame and filling about 85 % of its width, with plenty of empty velvet above and below. "
    "Exactly three crosses (X), each made of two short strips of the same tape, sit in three cells: middle-left, "
    "top-left and middle-right. The other three cells hold real jewelry instead of noughts (O), each one forming a "
    "circle, and together they make a winning diagonal line from bottom-left through the centre to top-right:\n"
    "- CENTRE cell: the gold name necklace from the first reference photo, its chain laid in a neat round loop. The "
    "name \"Carmen\" is cut from flat mirror-polished gold sheet in the same quick signature lettering as the second "
    "reference (tall looping capital C, then a-r-m-e-n), sitting on the upper part of the loop, large, sharp and "
    "readable; a single faceted emerald-green teardrop crystal in a four-prong gold setting is threaded on the chain "
    "at the lowest point of the loop. Only ONE teardrop; nothing hangs from the name.\n"
    "- BOTTOM-LEFT cell: the vintage gold watch from the third reference photo, its bracelet closed into a circle: an "
    "oval case framed by a twisted rope-pattern gold bezel, a white oval dial with thin gold baton markers and gold "
    "hands, and a bracelet of oval gold links each holding one oval medium-green stone with light veins - exactly "
    "three stones on each side of the case, all six the same green.\n"
    "- TOP-RIGHT cell: the gold ring from the fourth reference photo, lying flat with the stone facing up: a slim "
    "polished gold signet ring whose rounded top tapers into a thin band, set with one marquise-cut olive-green "
    "crystal in a thin smooth gold bezel. Delicate, not chunky.\n"
    "True-to-life relative sizes: the ring is the smallest piece, the watch circle is about the size of a wrist, the "
    "necklace loop is the biggest; every piece stays inside its own cell without touching the tape. " + LUZ)

MANTENER = ("Edit the first image. Keep EVERYTHING else exactly as it is, pixel for pixel: the red velvet and its "
            "texture, the light, the camera, the remaining tape strips, the three tape crosses, the gold name necklace "
            "with the name \"Carmen\" letter by letter and its single green teardrop, and the gold ring, all in the "
            "same position, shape and size. ")

PROMPT_ARREGLO = (
    MANTENER + "Change only these things:\n"
    "1. Remove the top-most horizontal tape strip (the one above the top row) and the bottom-most horizontal tape "
    "strip (the one below the bottom row), so the board is a classic open tic-tac-toe grid made of just two vertical "
    "and two horizontal strips, like a hash sign; fill the space where they were with the same red velvet.\n"
    "2. The watch (bottom-left): its bracelet must have exactly SIX green stones, three on each side of the case; "
    "the link at the top of the circle, opposite the case, becomes a plain gold hinged link with no stone. Keep the "
    "case, dial, hands and the circle shape the same.\n"
    "3. The six stones of the watch are a medium-dark green with fine light cream veins, all six the same, exactly "
    "like the real watch in the second image (not pale jade, no dark veins).")

PROMPT_VACIO = (
    "Edit the first image. Keep the red velvet, its texture and folds, the light, the camera and the two vertical and "
    "two horizontal tape strips of the board exactly as they are, pixel for pixel. Remove only the three tape "
    "crosses and the three pieces of jewelry (the necklace, the watch and the ring) and their shadows, filling those "
    "areas with the same red velvet so the board is empty, ready to play.")

TOMAS = {
    "final": ([FOTOS / "collar" / "producto-verde-carmen-v2.jpg", FOTOS / "ugc-lucce" / "ref-nombre-carmen.jpg",
               REFS / "reloj-lune-2.jpg", REFS / "anillo-nuit-1.jpg"], PROMPT_FINAL),
    "arreglo": ([REFS / "reloj-lune-2.jpg"], PROMPT_ARREGLO),    # la base (final-N.png) va delante
    "vacio": ([], PROMPT_VACIO),
}


def generar(cliente, prompt, destino, refs, res):
    try:
        r = cliente.subscribe(MODELO, arguments={
            "prompt": prompt, "image_urls": refs, "aspect_ratio": "9:16", "resolution": res,
            "quality": "high", "enhance_prompt": False})
    except Exception as e:
        return f"{destino.stem}: ERROR {type(e).__name__}: {e}"
    imgs = (r or {}).get("images") or []
    if not imgs:
        return f"{destino.stem}: SIN IMAGEN {r}"
    urllib.request.urlretrieve(imgs[0]["url"], destino)
    return f"{destino.stem}: {destino}"


def fotos(toma, refs_extra, prompt, n, res):
    import higgsfield_client
    SALIDA.mkdir(parents=True, exist_ok=True)
    refs = [higgsfield_client.upload_file(pathlib.Path(p)) for p in refs_extra]
    previas = len(list(SALIDA.glob(f"{toma}-*.png")))
    trabajos = [SALIDA / f"{toma}-{previas + k + 1}.png" for k in range(n)]
    with concurrent.futures.ThreadPoolExecutor(4) as ex:
        for linea in ex.map(lambda d: generar(higgsfield_client, prompt, d, refs, res), trabajos):
            print(linea, flush=True)


if __name__ == "__main__":
    a = sys.argv[1:]
    res = "4k" if "--4k" in a else "2k"
    n = int(a[a.index("--n") + 1]) if "--n" in a else 1
    if not a:
        sys.exit(__doc__)
    if a[0] == "foto":
        refs, prompt = TOMAS["final"]
        fotos("final", refs, prompt, n, res)
    elif a[0] in ("arreglo", "vacio") and len(a) > 1:
        refs, prompt = TOMAS[a[0]]
        fotos(a[0], [pathlib.Path(a[1])] + refs, prompt, n, res)
    else:
        sys.exit(__doc__)
