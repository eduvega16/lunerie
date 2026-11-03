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
        "<li>Se hace para ti: el nombre se graba tal cual lo escribes, con mayúsculas y tildes.</li></ul>"
        "<p><strong>Los colores:</strong> " + " · ".join(f"{m.lower()}, {c}" for m, c in zip(MESES, COLORES)) + ".</p>"
        "<p>En las fotos, nombres de ejemplo.</p>"
        "<p>Al ser una pieza personalizada no admite devolución, salvo que llegue con un defecto o un error nuestro: "
        "en ese caso la rehacemos.</p>")
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


if __name__ == "__main__":
    origen = pathlib.Path(sys.argv[1]); salida = pathlib.Path(__file__).resolve().parent / "collar-signe"
    salida.mkdir(exist_ok=True)
    rutas = []
    for n, (f, tipo, cx, _) in enumerate(FOTOS):
        im = crop45(Image.open(origen / f).convert("RGB"), cx, .5)
        im = niebla(im) if tipo == "prod" else im
        r = salida / f"{HANDLE}-{n + 1}.jpg"; im.save(r, quality=92); rutas.append(r)
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
