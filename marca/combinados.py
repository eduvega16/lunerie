"""Fotos de "reloj + joya" en escenas del día a dia (Higgsfield, Marketing Studio 2.5 Flare = GPT Image 2.5).

La clave va en .env.local (HF_KEY=id:secreto, fuera de git). Cada imagen gasta créditos (~0,13 $).
    python marca/combinados.py <salida_dir> [escena ...]       (sin escenas: todas)
Estilo de la biblioteca de contenido: solo manos y detalle, sin cara, luz natural, tonos niebla/lino.
"""
import concurrent.futures, pathlib, sys, urllib.request
from dotenv import load_dotenv
import higgsfield_client

RAIZ = pathlib.Path(__file__).resolve().parent.parent
FOTOS = RAIZ / "marca" / "fotos-ia"
load_dotenv(RAIZ / ".env.local")
MODELO = "marketing-studio/image/flare"

# Esfera sin marca (Edu la prefiere así en anuncios): no se pide NAIDU.
RELOJ = ("Use the watch from the first reference image EXACTLY as it is - do not redesign it: the same small oval "
         "case with a rope-twist gold bezel, a white dial with thin gold hands and baton indices and NO text or "
         "logo on the dial, the same bracelet made only of oval dark green marbled stones, 3 on each side, each set "
         "in a gold frame, joined by short gold links. Keep the stone colour, shape and count. The watch is small "
         "(the case is only 12 mm wide), so it must look delicate on the wrist, never oversized. ")
ANILLO = ("The ring from the second reference image must be exactly as in that image: a yellow-gold signet-style ring "
          "with one marquise-cut stone in a clear OLIVE GREEN (peridot green), not amber, not brown. ")
COLLAR = ("The necklace from the second reference image must be exactly as in that image: a fine gold chain with "
          "oval green stones set INTO the chain in a line, never hanging as pendants. ")
CIERRE = (" Photorealistic, natural skin with real texture, short neutral manicure, no face visible, no text, no "
          "logos, no extra jewelry. Soft natural daylight, calm and elegant.")

# Estilo "juvenil" (29-oct): ojo de pez, mano muy cerca de la cámara, vida cotidiana, color vivo. El reloj ocupa más cuadro
# porque la muñeca está cerca del objetivo, no porque se agrande el reloj (sigue siendo pequeño en la muñeca).
COLOR3 = ("The third reference image is a macro of the watch: copy the colour of its stones exactly - a clearly GREEN deep forest green with lighter green veins, never black, charcoal or grey. ")
RELOJ2 = ("Use the watch from the first reference image EXACTLY as it is: a small oval case with a rope-twist WARM "
          "YELLOW-gold bezel (not rose gold, not pink), white dial with thin gold hands and NO text or logo, and a "
          "bracelet made only of oval DEEP FOREST-GREEN marbled stones with paler green veins (3 on each side of the "
          "case), each stone set in a yellow-gold frame, joined by short gold links. The stones must be clearly green, "
          "never brown, grey or blue. The watch is large and sharp in the frame because the wrist is close to the "
          "camera lens, its face about a quarter of the image width, but it stays a delicate small watch on a slim "
          "wrist. ")
JUVENIL = (" Youthful social-media photography, shot on a phone-style wide lens with a strong fisheye distortion, the "
           "hand and wrist very close to the camera, vivid natural sunlight and saturated real-life colours. "
           "Photorealistic, natural skin with real texture and tiny imperfections, nude manicure, no face visible, no "
           "text, no logos, no brand names, no extra jewelry besides the pieces mentioned.")

ESCENAS = {
    "metro-ojo": dict(
        refs=["lune-verde-producto.jpg", "joyas/nuit-verde-mano-v1.png", "lune-verde-detalle.jpg"],
        prompt=RELOJ2 + ANILLO + COLOR3 + "A woman's fist gripping a vertical steel pole inside a generic subway car, shot from "
               "just below and very close with a fisheye lens, so the curved ceiling lights and the seats bend around "
               "the hand. The watch on her wrist is in the foreground, facing the camera, and the ring is on the "
               "finger on the pole. Passengers blurred in the background, no signs, no readable text." + JUVENIL),
    "mercado": dict(
        refs=["lune-verde-producto.jpg", "joyas/nuit-verde-mano-v1.png", "lune-verde-detalle.jpg"],
        prompt=RELOJ2 + ANILLO + COLOR3 + "Overhead fisheye shot of a woman's hand reaching into a black mesh tote bag full of "
               "oranges, peaches and green grapes, picking up a peach. The watch is on the wrist of that hand, large "
               "in the foreground, and the ring is on one finger. Warm midday sun, concrete pavement at the edges." +
               JUVENIL),
    "terraza": dict(
        refs=["lune-verde-producto.jpg", "joyas/nuit-verde-mano-v1.png", "lune-verde-detalle.jpg"],
        prompt=RELOJ2 + ANILLO + COLOR3 + "A woman's hand holding a tall iced coffee in a clear cup with a paper straw on a "
               "sunny city street terrace, seen from slightly above with a fisheye lens. The watch is on the wrist "
               "holding the cup, large in the foreground, and the ring is on one finger. Blurred cafe tables and "
               "bicycles behind." + JUVENIL),
    "cafe": dict(
        refs=["lune-verde-producto.jpg", "joyas/nuit-verde-mano-v1.png"],
        prompt=RELOJ + ANILLO + "Overhead close-up photograph of a woman's two hands holding a small white ceramic "
               "coffee cup with a gold spoon, on a pale linen tablecloth. The watch is on one wrist and the ring on "
               "a finger of the same hand, both clearly visible. Warm light-grey and cream tones, a few crumbs of a "
               "croissant on a plate at the edge." + CIERRE),
    "metro": dict(
        refs=["lune-verde-producto.jpg", "joyas/nuit-verde-mano-v1.png"],
        prompt=RELOJ + ANILLO + "Close-up photograph of a woman's hand gripping a vertical metal handrail inside a "
               "generic modern subway car, seen from the side, the watch on the wrist and the ring on a finger of "
               "the same hand, both sharp and clearly visible. Blurred background of a plain train interior and "
               "seats, no signs, no readable text, no brand logos. Cream knit sleeve slightly pushed back." + CIERRE),
    "pelo": dict(
        refs=["lune-verde-producto.jpg", "joyas/collar-lune-cuello-v2-api.png"],
        prompt=RELOJ + COLLAR + "Editorial close-up of a woman tucking a strand of long brown hair behind her ear, "
               "face cropped out just below the nose, the watch on her wrist near her neck and the necklace visible "
               "on the collarbone, a simple cream top. Shallow depth of field, light neutral background." + CIERRE),
}


def referencia(nombre):
    return higgsfield_client.upload_file(FOTOS / nombre)


def generar(nombre, salida):
    e = ESCENAS[nombre]
    try:
        res = higgsfield_client.subscribe(MODELO, arguments={
            "prompt": e["prompt"], "image_urls": [referencia(r) for r in e["refs"]], "aspect_ratio": "3:4",
            "resolution": "2k", "quality": "high", "enhance_prompt": False})
    except Exception as ex:  # fallo, cancelación, moderación o sin créditos: no se da por bueno
        return nombre, f"ERROR {type(ex).__name__}: {ex}"
    imgs = (res or {}).get("images") or []
    if not imgs:
        return nombre, f"SIN IMAGEN: {res}"
    destino = salida / f"{nombre}.png"
    urllib.request.urlretrieve(imgs[0]["url"], destino)
    return nombre, str(destino)


if __name__ == "__main__":
    salida = pathlib.Path(sys.argv[1]); salida.mkdir(parents=True, exist_ok=True)
    elegidas = sys.argv[2:] or list(ESCENAS)
    with concurrent.futures.ThreadPoolExecutor() as ex:
        for nombre, r in ex.map(lambda n: generar(n, salida), elegidas):
            print(nombre, "->", r)
