"""Collar con nombre «Signé» (3-nov): crea el producto en BORRADOR con 24 variantes (Color: Dorado/Plateado × Mes) y
sus fotos en 4:5. Personalización (nombre, piedra del mes, casilla) en la plantilla «collar»
(tema/codigo/snippets/lunerie-collar.liquid). Proveedor: QIUHAN (Alibaba 1601817911870), pedidos a mano.
Fotos: las que bajó Edu (de la web de Olivia Jewelry; Edu asume el riesgo, cambiarlas por las del primer pedido real).
    python productos/collar_signe.py <carpeta de fotos>
"""
import os, pathlib, subprocess, sys
from PIL import Image
from gql import gql
from normalizar_dsers import LOC, crop45, niebla

HANDLE, TITULO, PRECIO = "collar-signe", "Collar Signé", "49.95"
MESES = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
         "Noviembre", "Diciembre"]
COLORES = ["rojo oscuro", "morado", "azul agua", "blanco", "verde", "violeta", "rojo", "verde oliva", "azul oscuro",
           "rosa", "amarillo", "azul"]
# fichero, tipo («prod» = fondo a niebla), centro x, texto alternativo
FOTOS = [("Signature_Name_and_Birthstone_Necklace.webp", "prod", .5, "Collar Signé dorado con nombre en letra de firma y lágrima verde"),
         ("645643564.webp", "vida", .45, "Collar Signé dorado puesto, con un nombre de ejemplo y lágrima azul agua"),
         ("Mask_group-26_ff4d6846-2898-459b-9369-eb9240a0ee8b.webp", "prod", .5, "Collar Signé plateado con lágrima verde"),
         ("script-initial-birthstone-necklace.webp", "vida", .5, "Collar Signé dorado de cerca, con lágrima roja")]
FOTO_COLOR = {"Dorado": 0, "Plateado": 2}
DESC = ("<p>Su nombre en letra de firma y, a un lado, una lágrima del color de su mes. Un collar fino para llevar cada "
        "día, sin quitárselo.</p><ul>"
        "<li>Acero inoxidable con acabado dorado o plateado.</li>"
        "<li>El nombre que elijas, de hasta 10 letras, en letra de firma.</li>"
        "<li>Circonita en forma de lágrima, del color del mes.</li>"
        "<li>Se hace para ti, con el nombre tal cual lo escribes.</li></ul>"
        "<p><strong>Los colores:</strong> " + " · ".join(f"{m.lower()}, {c}" for m, c in zip(MESES, COLORES)) + ".</p>"
        "<p>En las fotos, nombres de ejemplo.</p>")   # la devolución va en «Envío y devoluciones» (5-nov)
SEO = "Collar con nombre en letra de firma y lágrima del color de su mes, dorado o plateado. Envío gratis a península."


def subir(rutas):
    ins = [{"filename": p.name, "mimeType": "image/jpeg", "resource": "IMAGE", "httpMethod": "PUT"} for p in rutas]
    T = gql("""mutation($i:[StagedUploadInput!]!){ stagedUploadsCreate(input:$i){ stagedTargets{ url resourceUrl parameters{ name value } } userErrors{ field message } } }""",
            {"i": ins}, True)["stagedUploadsCreate"]["stagedTargets"]
    for r, t in zip(rutas, T):
        hdr = []
        for prm in t["parameters"]:
            hdr += ["-H", f"{prm['name']}: {prm['value']}"]
        code = subprocess.run(["curl", "-s", "-o", os.devnull, "-w", "%{http_code}", "-X", "PUT", "-H", "Content-Type: image/jpeg",
                               *hdr, "--data-binary", f"@{r}", t["url"]], capture_output=True, text=True).stdout
        assert code == "200", (r, code)
    return [t["resourceUrl"] for t in T]


# 3-nov (Edu): fuera las fotos de Olivia; van las de IA con nombres españoles (marca/collar_ia.py). Se cambian en su
# sitio (fileUpdate: conservan el enlace con la variante Dorado / Plateado) y se ordenan: producto, puesto, puesto, plateado.
FOTOS_IA = [("producto-dorado-2", "prod", "Collar Signé dorado con el nombre Marta y lágrima azul"),
            ("modelo-hombro-2", "vida", "Collar Signé dorado con el nombre Carmen y lágrima verde, con el reloj Lune y el anillo Nuit"),
            ("producto-plateado-2", "prod", "Collar Signé plateado con el nombre Paula y lágrima rosa"),
            ("modelo-tirantes-2", "vida", "Collar Signé dorado con el nombre Elena y lágrima amarilla, con los aros Boucle")]


def fotos_ia():
    ia = pathlib.Path(__file__).resolve().parent.parent / "marca" / "fotos-ia" / "collar"
    salida = pathlib.Path(__file__).resolve().parent / "collar-signe"
    p = gql('query($h: String!){ productByHandle(handle: $h){ id media(first: 10){ nodes{ id } } } }', {"h": HANDLE})["productByHandle"]
    M = [m["id"] for m in p["media"]["nodes"]]   # [dorado, modelo, plateado, de cerca] (las de Olivia)
    rutas = []
    for nombre, tipo, _ in FOTOS_IA:
        im = crop45(Image.open(ia / f"{nombre}.png").convert("RGB"))
        im = niebla(im) if tipo == "prod" else im
        r = salida / f"{HANDLE}-{nombre}.jpg"; im.save(r, quality=97, subsampling=0); rutas.append(r)
    fuentes = subir(rutas)
    destino = [M[0], M[1], M[2], M[3]]           # dorado→dorado, modelo→modelo, plateado→plateado, de cerca→Elena
    gql("""mutation($f:[FileUpdateInput!]!){ fileUpdate(files:$f){ userErrors{ field message } } }""",
        {"f": [{"id": m, "originalSource": s, "alt": alt} for m, s, (_, _, alt) in zip(destino, fuentes, FOTOS_IA)]}, True)
    gql("""mutation($p:ID!,$m:[MoveInput!]!){ productReorderMedia(id:$p, moves:$m){ mediaUserErrors{ field message } } }""",
        {"p": p["id"], "m": [{"id": M[3], "newPosition": "2"}, {"id": M[2], "newPosition": "3"}]}, True)
    print("fotos cambiadas")


def cambiar(pares):
    """Cambia fotos sueltas en su sitio: [(toma de marca/fotos-ia/collar, posición en la galería 1..n)].
    Conserva posición, texto alternativo y variante (fileUpdate + originalSource)."""
    ia = pathlib.Path(__file__).resolve().parent.parent / "marca" / "fotos-ia" / "collar"
    salida = pathlib.Path(__file__).resolve().parent / "collar-signe"
    M = gql('query($h: String!){ productByHandle(handle: $h){ media(first: 20){ nodes{ id alt } } } }', {"h": HANDLE})["productByHandle"]["media"]["nodes"]
    rutas = []
    for toma, _ in pares:
        r = salida / f"{HANDLE}-{toma}.jpg"; crop45(Image.open(ia / f"{toma}.png").convert("RGB")).save(r, quality=97, subsampling=0); rutas.append(r)
    fuentes = subir(rutas)
    gql("""mutation($f:[FileUpdateInput!]!){ fileUpdate(files:$f){ userErrors{ field message } } }""",
        {"f": [{"id": M[pos - 1]["id"], "originalSource": s} for s, (_, pos) in zip(fuentes, pares)]}, True)
    for (toma, pos) in pares:
        print(f"{pos}: {M[pos - 1]['alt']}  <-  {toma}")


if __name__ == "__main__" and sys.argv[1:] == ["--fotos-ia"]:
    fotos_ia(); sys.exit()

if __name__ == "__main__" and sys.argv[1:2] == ["--cambiar"]:   # --cambiar <toma> <posición> [<toma> <posición> …]
    a = sys.argv[2:]; cambiar([(a[i], int(a[i + 1])) for i in range(0, len(a), 2)]); sys.exit()

if __name__ == "__main__":
    origen = pathlib.Path(sys.argv[1]); salida = pathlib.Path(__file__).resolve().parent / "collar-signe"
    salida.mkdir(exist_ok=True)
    rutas = []
    for n, (f, tipo, cx, _) in enumerate(FOTOS):
        im = crop45(Image.open(origen / f).convert("RGB"), cx, .5)
        im = niebla(im) if tipo == "prod" else im
        r = salida / f"{HANDLE}-{n + 1}.jpg"; im.save(r, quality=97, subsampling=0); rutas.append(r)
    fuentes = subir(rutas)
    files = [{"originalSource": s, "alt": alt, "contentType": "IMAGE"} for s, (_, _, _, alt) in zip(fuentes, FOTOS)]
    variantes = []
    for color in ("Dorado", "Plateado"):
        for i, mes in enumerate(MESES):
            variantes.append({
                "optionValues": [{"optionName": "Color", "name": color}, {"optionName": "Mes", "name": mes}],
                "price": PRECIO, "sku": f"SIGNE-{color[:3].upper()}-{i + 1:02d}",
                "inventoryItem": {"tracked": False}, "file": files[FOTO_COLOR[color]],
                "inventoryQuantities": [{"locationId": LOC, "name": "available", "quantity": 0}]})
    r = gql("""mutation($i: ProductSetInput!) { productSet(synchronous: true, input: $i) {
                 product { id handle status variants(first: 30) { nodes { title } } media(first: 10) { nodes { id } } }
                 userErrors { field message } } }""",
            {"i": {"title": TITULO, "handle": HANDLE, "vendor": "Lunerie", "productType": "Collares", "status": "DRAFT",
                   "templateSuffix": "collar", "descriptionHtml": DESC,
                   "seo": {"title": f"{TITULO} | Lunerie", "description": SEO},
                   "productOptions": [{"name": "Color", "position": 1, "values": [{"name": "Dorado"}, {"name": "Plateado"}]},
                                      {"name": "Mes", "position": 2, "values": [{"name": m} for m in MESES]}],
                   "files": files, "variants": variantes}}, True)
    p = r["productSet"]["product"]
    print(p["id"], p["handle"], p["status"], len(p["variants"]["nodes"]), "variantes,", len(p["media"]["nodes"]), "fotos")
