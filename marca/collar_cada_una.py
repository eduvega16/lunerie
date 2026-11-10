"""Piezas de Instagram del plan de 2 al día (9-nov, OK de Edu a los guiones):
  · «Un collar para cada una» (formato 27): el Collar Signé en círculo sobre terciopelo verde botella con un papelito EN
    BLANCO en el centro (el texto lo escribe textos_cada_una.py con la letra de Lunerie): Ana azul · Alba rojo ·
    Sara verde · Laura rosa.
  · Signé plateado: la foto de estudio roja corregida, en plata, «Elena» con lágrima azul claro.
  · Prospecto (formato 28): caja blanca con franja verde y prospecto, todo en blanco (los textos, en local).
  · Polvorón (formato 29): un polvorón envuelto sobre fondo blanco (sin collar).
Base: la foto de estudio roja corregida (sin los textos del post) + las fotos reales de la muestra «Marta».
    python marca/collar_cada_una.py [tomas…] [--n 2]   → marca/fotos-ia/cada-una/<toma>-<n>.png
"""
import concurrent.futures, pathlib, sys, urllib.request
from PIL import Image
import higgsfield_client
import collar_ia as C

RAIZ = C.RAIZ
SALIDA = RAIZ / "marca" / "fotos-ia" / "cada-una"
BASE = SALIDA / "base-estudio-rojo.png"   # post-estudio-rojo-v2-1.jpg sin la franja de texto, a 3:4


def base():
    if not BASE.exists():
        im = Image.open(C.SALIDA / "post-estudio-rojo-v2-1.jpg").convert("RGB")
        im = im.crop((0, 0, im.width, 1100))
        lienzo = Image.new("RGB", (1080, 1440), im.getpixel((5, 1090)))
        lienzo.paste(im, (0, 0))
        SALIDA.mkdir(parents=True, exist_ok=True)
        lienzo.save(BASE)
    return BASE


ESTRUCTURA = (
    "The necklace is built exactly like the one in the first image and the real photos: ONE continuous fine gold "
    "cable chain; the name, cut from a flat mirror-polished gold sheet in the same quick handwritten signature "
    "lettering, is joined to the chain by a tiny jump ring at the top tip of its capital letter and ends in ONE long "
    "straight tail stroke finishing in a small ring; from that ring the SAME chain continues two or three links to a "
    "single faceted pear-shaped crystal in a polished four-prong gold setting whose bail is threaded directly onto the "
    "chain. No extra chain hanging below the name, no Y shape, no second pendant, no extra loops or stray strokes. ")

CIRCULO = (
    "Overhead flat-lay jewelry photograph, shot straight from above, on rich deep bottle-green velvet with a soft "
    "visible pile and gentle natural light from one side, delicate soft shadows. The necklace is laid flat in an almost "
    "perfect circle filling the middle of the frame. The name reads exactly \"{nombre}\" ({letras}) and lies on the "
    "left part of the circle, following its curve; after the name the chain continues two or three links to the crystal, "
    "which lies flat at the bottom of the circle, point outwards; the chain then closes the circle up the right side. "
    "The crystal is {color}. In the exact centre of the circle lies a small rectangular scrap of thick off-white "
    "cotton paper with torn, deckled edges, slightly tilted, COMPLETELY BLANK: no writing, no marks. "
    + ESTRUCTURA +
    "Ultra sharp polished metal, realistic velvet texture, editorial luxury look. The first image is a studio photo of "
    "this necklace and the others are real photos of it (\"Marta\") on a hand and on a stand: use them only for the "
    "necklace and its lettering; never copy the hand, the stand or the white background. "
    "No text anywhere, no logo, no watermark. ")

PLATEADO = (
    "Edit the first image. Keep EVERYTHING exactly the same - the U shape of the chain, the pure white background, the "
    "light, the soft shadow, the framing, how the name joins the chain, the long straight tail stroke ending in a small "
    "ring, and the crystal threaded directly on the chain at the lowest point of the U with the same size and four-prong "
    "setting - and change only three things. First, all the metal (chain, name, rings and setting) is now polished "
    "sterling-silver coloured, cool bright silver, no gold at all. Second, the name now reads exactly \"Elena\" (a tall, "
    "clearly readable capital E, then l-e-n-a) in the same flat mirror-polished quick signature lettering, ending in ONE "
    "long straight stroke - nothing else: no extra loops, no second tail. Third, the crystal is a pale icy light blue, "
    "like a clear aquamarine-coloured zircon, bright and transparent. The other images are real photos of the necklace "
    "\"Marta\": use them only for the lettering style. No text, no logo. ")

PROSPECTO = (
    "Overhead flat-lay photograph, shot straight from above, on a light white Carrara marble surface with soft grey "
    "veins, soft natural daylight from the top left, delicate shadows. In the centre, a small rectangular white "
    "cardboard box like a pharmacy box, lying flat, with ONE plain deep green band (#006039) across its front; its top "
    "flap is open and the gold necklace spills out of the box onto the marble: the name \"Marta\" exactly as in the "
    "reference images and its single crystal, a vivid deep emerald green. Next to the box, to the right, a folded "
    "paper leaflet half unfolded and lying flat, thin white paper with visible fold creases. The box front, the green "
    "band and the leaflet are COMPLETELY BLANK: no letters, no lines of text, no logos, no crosses, no symbols. "
    + ESTRUCTURA +
    "Leave the top fifth of the frame as empty marble. Clean, witty editorial still life. ")

POLVORON = (
    "Studio food photograph on a seamless pure white background with soft, even studio light and a delicate soft "
    "shadow, matching a luxury jewelry catalogue. A single traditional Spanish polvoron (a round, crumbly, pale golden "
    "shortbread dusted with powdered sugar, about 5 cm wide) sits half unwrapped from its thin white tissue paper "
    "wrapper with twisted ends, a few crumbs and a little powdered sugar around it. Seen from a slight high angle, "
    "centred, sharp, appetising and real. Leave the top and bottom fifths of the frame as empty white background. No "
    "text, no logo, no brand, no watermark. ")

EDITAR_CIRCULO = (
    "Edit the first image. Keep EVERYTHING exactly the same - the green velvet, the light, the framing, the blank paper "
    "in the centre, the circle of the chain, the position of the name, the long straight tail stroke ending in a small "
    "ring, and the crystal threaded on the chain at the bottom of the circle with the same size and setting - and change "
    "only two things. First, the name now reads exactly \"Elena\" (a tall, clearly readable capital E, then l-e-n-a) in "
    "the same flat mirror-polished gold quick signature lettering, ending in ONE long straight stroke - nothing else: no "
    "extra loops, no second tail. Second, the crystal is a deep ruby red. The paper stays completely blank. ")

# 10-nov (Edu): en círculo cerrado parecía una PULSERA y la lágrima, demasiado grande → se editan las 4 buenas
ABRIR = (
    "Edit the first image. Keep EXACTLY the same: the green velvet, the light, the framing, the small scrap of torn paper "
    "in the centre (it stays completely blank), the name exactly as it is written (same letters, same lettering, same "
    "position and size), its long straight tail stroke ending in a small ring, and the colour of the crystal. Change "
    "only two things. First, it must clearly read as a NECKLACE laid flat, not a bracelet: the chain is OPEN at the top "
    "centre - its two ends lie a few centimetres apart, one ending in a small polished gold lobster-claw clasp and the "
    "other in a short extender chain of about 5 cm finished with a tiny plain gold tag - and the chain is laid as a "
    "relaxed, slightly taller oval, like a fine necklace dropped on the velvet, not a perfect closed ring. Second, the "
    "pear-shaped crystal is MUCH smaller and more delicate: about half its current size, clearly smaller than the "
    "capital letter of the name, still in its four-prong gold setting with its bail threaded directly on the chain at "
    "the bottom of the oval, right after the name. No text anywhere. ")

AZUL = "a vivid deep sapphire blue, exactly the blue of the real crystal in the reference photos"
TOMAS = {
    "circulo-ana-azul": ("3:4", "base", CIRCULO.format(nombre="Ana", letras="a tall, clearly readable capital A, then "
                                                       "n-a", color=AZUL)),
    "circulo-alba-rojo": ("3:4", "base", CIRCULO.format(nombre="Alba", letras="a tall, clearly readable capital A, then "
                                                        "l-b-a", color="a deep ruby red")),
    "circulo-sara-verde": ("3:4", "base", CIRCULO.format(nombre="Sara", letras="a tall, clearly readable capital S, "
                                                         "then a-r-a", color="a vivid deep emerald green")),
    "circulo-laura-rosa": ("3:4", "base", CIRCULO.format(nombre="Laura", letras="a clearly readable capital L, then "
                                                         "a-u-r-a", color="a soft pastel pink")),
    # 9-nov: la «A» mayúscula de firma sale como una X o una N («Xlba», «Nna»): Ana y Alba cambiadas por Marta y Elena
    "circulo-marta-azul": ("3:4", "base", CIRCULO.format(nombre="Marta", letras="a tall pointed capital M with a long "
                                                         "lead-in stroke, then a-r-t-a, exactly as in the reference photos",
                                                         color=AZUL)),
    # 9-nov: generada de cero escribía «Menta» (copia el estilo de Marta): se edita la de Marta azul
    "editar-elena-rojo": ("3:4", "marta", EDITAR_CIRCULO),
    "circulo-elena-rojo": ("3:4", "base", CIRCULO.format(nombre="Elena", letras="a tall, clearly readable capital E, "
                                                         "then l-e-n-a", color="a deep ruby red")),
    "abrir-marta-azul": ("3:4", "circulo-marta-azul-2", ABRIR),
    "abrir-elena-rojo": ("3:4", "editar-elena-rojo-1", ABRIR),
    # la edición volvió azul la lágrima de Elena: solo el color
    "abrir-elena-rojo-color": ("3:4", "abrir-elena-rojo-1", "Edit the first image. Keep EVERYTHING exactly the same - "
        "the velvet, the paper, the chain, the clasp, the extender, the name \"Elena\" and the size and position of "
        "the small crystal - and change only the colour of the crystal: it is now a deep ruby red, like a red "
        "zircon, bright and transparent. No text anywhere. "),
    "abrir-sara-verde": ("3:4", "circulo-sara-verde-1", ABRIR),
    "abrir-laura-rosa": ("3:4", "circulo-laura-rosa-1", ABRIR),
    "plateado-elena": ("3:4", "base", PLATEADO),
    "prospecto": ("3:4", "base", PROSPECTO),
    "polvoron": ("3:4", None, POLVORON),
}


def generar(toma, n):
    formato, refs, prompt = TOMAS[toma]
    try:
        fotos = ({"base": [base(), *C.MUESTRA], "marta": [SALIDA / "circulo-marta-azul-2.png", *C.MUESTRA], None: []}[refs]
                 if refs in ("base", "marta", None) else [SALIDA / f"{refs}.png", *C.MUESTRA])
        urls = [higgsfield_client.upload_file(r) for r in fotos]
        res = higgsfield_client.subscribe(C.MODELO, arguments={
            "prompt": prompt, "image_urls": urls, "aspect_ratio": formato, "resolution": C.RESOLUCION,
            "quality": "high", "enhance_prompt": False})
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
    base()
    trabajos = [(t, n) for t in (args or list(TOMAS)) for n in range(1, veces + 1)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
        for toma, r in ex.map(lambda tn: generar(*tn), trabajos):
            print(toma, "->", r, flush=True)
