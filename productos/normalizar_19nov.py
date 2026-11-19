"""Normaliza los 7 productos personalizables importados con DSers el 19-nov (en BORRADOR).

Como normalizar_dsers.py, pero con varias opciones por producto: quita variantes y opciones sobrantes, cambia nombres
y valores al español y los ordena, textos, precio, «Frase corta», fotos 4:5 (sustituidas en su sitio, así cada
variante conserva su foto), inventario fuera del «almacén» de DSers y foto de variante si cambia.
Uso: python productos/normalizar_19nov.py <carpeta con lote.json y las fotos mNN.png> <clave> ...
"""
import json, os, subprocess, sys
from PIL import Image, ImageChops
from gql import gql, clave

sys.stdout.reconfigure(encoding="utf-8")
LOC = "gid://shopify/Location/127723929939"
NIEBLA = (0xF2, 0xF4, 0xF2)
MESES = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
         "Noviembre", "Diciembre"]
EN = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
MES_NUM = {str(i + 1): m for i, m in enumerate(MESES)}               # «1» → Enero
MES_EN = {f"{i + 1}-{e}": m for i, (e, m) in enumerate(zip(EN, MESES))}  # «1-Jan» → Enero
LETRAS = [chr(c) for c in range(ord("A"), ord("Z") + 1)]
TALLAS = "<p><strong>Tallas:</strong> 12 (52 mm de contorno), 14-15 (54,5 mm) y 17 (57 mm). Para acertar, rodea el " \
         "dedo con un hilo y mide el contorno; si dudas entre dos tallas, elige la mayor.</p>"

# opciones: nombre viejo → None (se quita; tiene que quedar con un solo valor) o (nombre nuevo, {viejo: nuevo}, orden)
# quedan: {opción vieja: [valores que se quedan]} · fotos: (índice, «prod» = fondo niebla | «vida», cx, cy, alto, alt)
# foto_variante: (opción nueva, {valor nuevo: índice de foto}) solo cuando hay que cambiarla
FICHAS = {
    "initiale": dict(
        id="11147313348947", titulo="Collar Initiale", handle="collar-initiale", tipo="Collares", plantilla="joya",
        precio="44.95", frase="Tu inicial, entre perlas.",
        opciones={"Metal Color": ("Color", {"XNL0092-Gold Color": "Dorado", "XNL0092-Silver Color": "Plateado"},
                                  ["Dorado", "Plateado"]),
                  "Length": None,
                  "Main Stone Color": ("Inicial", {}, LETRAS)},
        desc="<p>Un collar de perlas con tu inicial, o la suya, y una circonita cuadrada que brilla al lado. Las dos "
             "cuelgan de una anilla con brillantes.</p><ul>"
             "<li>Acero inoxidable con acabado dorado o plateado.</li>"
             "<li>Perlas de imitación.</li>"
             "<li>Inicial de 8-10 mm y circonita de 5,5 mm.</li>"
             "<li>Largo: 40 cm, más 5 cm de alargador.</li></ul>",
        seo=("Collar Initiale · collar de perlas con inicial",
             "Collar de perlas con tu inicial y una circonita, dorado o plateado. Envío gratis a península y 3 años de garantía."),
        # 1, 6 y 7: antes se les borra el texto de eManco de abajo (OpenCV, inpaint)
        fotos=[(7, "vida", .5, .5, 1, "Collar Initiale dorado con la letra a"),
               (0, "vida", .47, .43, .86, "Collar Initiale dorado con la letra m"),
               (1, "vida", .55, .5, 1, "Collar Initiale dorado con la letra k"),
               (3, "vida", .5, .5, 1, "Collar Initiale dorado con la letra j"),
               (2, "vida", .5, .5, 1, "Collar Initiale dorado con la letra g, de cerca"),
               (5, "vida", .6, .5, 1, "Las 26 iniciales del Collar Initiale"),
               (6, "vida", .5, .5, 1, "Collar Initiale plateado con la letra a")]),
    "croix": dict(
        id="11147313414483", titulo="Collar Croix", handle="collar-croix", tipo="Collares", plantilla="joya",
        precio="24.95", frase="Una cruz de piedras de colores.",
        quedan={"Metal Color": ["xl303e", "xl303f"]},
        opciones={"Metal Color": ("Color", {"xl303e": "Dorado", "xl303f": "Plateado"}, ["Dorado", "Plateado"])},
        desc="<p>Una cruz de piedras de colores, cada una de un tono, en una cadena fina. Para llevarla sola o junto a "
             "otros collares.</p><ul>"
             "<li>Acero inoxidable con acabado dorado o plateado.</li>"
             "<li>Circonitas ovaladas de colores.</li></ul>",
        seo=("Collar Croix · cruz de piedras de colores",
             "Collar con una cruz de circonitas de colores, dorado o plateado. Envío gratis a península y 3 años de garantía."),
        fotos=[(7, "vida", .5, .5, 1, "Collar Croix dorado"),
               (1, "vida", .5, .5, 1, "La cruz del Collar Croix, de cerca"),
               (4, "vida", .5, .5, 1, "Collar Croix plateado")]),
    "baroque": dict(
        id="11147319214419", titulo="Pendientes Baroque", handle="pendientes-baroque", tipo="Pendientes",
        plantilla="joya", precio="24.95", frase="Una perla irregular en un aro pequeño.",
        quedan={"Metal Color": ["Gold a", "Silver a"]},
        opciones={"Metal Color": ("Color", {"Gold a": "Dorado", "Silver a": "Plateado"}, ["Dorado", "Plateado"])},
        desc="<p>Una perla de forma irregular que cuelga de un aro pequeño. Sencillos, para llevar todos los días.</p><ul>"
             "<li>Acero inoxidable con acabado dorado o plateado.</li>"
             "<li>Aro pequeño con cierre de bisagra.</li>"
             "<li>Se venden por pares.</li></ul>",
        seo=("Pendientes Baroque · aros con perla irregular",
             "Aros pequeños con una perla de forma irregular, dorados o plateados. Envío gratis a península y 3 años de garantía."),
        fotos=[(0, "vida", .45, .5, 1, "Pendientes Baroque dorados"),
               (2, "vida", .5, .5, 1, "Pendiente Baroque puesto en la oreja"),
               (1, "vida", .5, .5, 1, "Pendientes Baroque dorados y plateados"),
               (5, "vida", .5, .5, 1, "Pendientes Baroque plateados")]),
    "toi-moi": dict(
        id="11147318329683", titulo="Anillo Toi & Moi", handle="anillo-toi-et-moi", tipo="Anillos", plantilla="anillo",
        precio="29.95", frase="Tu piedra y la suya.",
        quedan={"Ring Size": ["6", "7", "8"]},
        opciones={"Main Stone Color": ("Color", {"Golden Color": "Dorado", "Silvery Color": "Plateado"},
                                       ["Dorado", "Plateado"]),
                  "Ring Size": ("Talla", {"6": "12", "7": "14-15", "8": "17"}, ["12", "14-15", "17"])},
        desc="<p>Dos piedras juntas en un anillo fino: la tuya y la de alguien a quien quieres. Elige el color de cada "
             "una, el de vuestro mes o el que más os guste.</p><ul>"
             "<li>Acabado dorado o plateado.</li>"
             "<li>Dos circonitas, cada una del color que elijas.</li>"
             "<li>Se hace para ti, con las dos piedras que elijas.</li></ul>" + TALLAS,
        seo=("Anillo Toi & Moi · anillo con dos piedras",
             "Anillo fino con dos piedras del color que elijas, dorado o plateado. Envío gratis a península y 3 años de garantía."),
        fotos=[(4, "vida", .5, .5, 1, "Tres anillos Toi & Moi dorados con piedras de colores"),
               (1, "vida", .5, .5, 1, "Anillo Toi & Moi dorado en la mano"),
               (2, "vida", .5, .5, 1, "Anillo Toi & Moi dorado puesto"),
               (3, "vida", .5, .5, 1, "Anillo Toi & Moi plateado puesto")],
        foto_variante=("Color", {"Dorado": 2, "Plateado": 3})),
    "fil": dict(
        id="11147313381715", titulo="Anillo Fil", handle="anillo-fil", tipo="Anillos", plantilla="joya",
        precio="19.95", frase="Fino, abierto y con su piedra.",
        opciones={"Ships From": None, "Ring Size": None,
                  "Main Stone Color": ("Mes", MES_NUM, MESES)},
        desc="<p>Un anillo muy fino y abierto, con una piedra rectangular del color de su mes. Se ajusta al dedo "
             "apretándolo o abriéndolo con suavidad.</p><ul>"
             "<li>Acero inoxidable con acabado dorado.</li>"
             "<li>Circonita rectangular de 4 × 8 mm.</li>"
             "<li>Abierto y ajustable, de 18 mm de diámetro por dentro.</li></ul>"
             "<p><strong>Los colores:</strong> enero, granate · febrero, lavanda · marzo, azul agua · abril, blanco · "
             "mayo, verde · junio, lila claro · julio, rojo · agosto, verde oliva · septiembre, azul grisáceo · "
             "octubre, rosa · noviembre, champán · diciembre, verde azulado.</p>",
        seo=("Anillo Fil · anillo fino con la piedra de su mes",
             "Anillo fino, abierto y dorado con una piedra del color de su mes. Envío gratis a península y 3 años de garantía."),
        fotos=[(14, "prod", .52, .52, .85, "Anillo Fil con la piedra verde de mayo"),
               (1, "vida", .5, .5, 1, "Anillos Fil puestos en la mano"),
               (0, "vida", .5, .5, 1, "Dos anillos Fil en el dedo"),
               (4, "vida", .5, .5, 1, "Anillo Fil de cerca"),
               (2, "vida", .5, .5, 1, "Anillos Fil de todos los meses"),
               (3, "vida", .5, .5, 1, "Doce anillos Fil, uno por mes")]
              + [(i, "prod", .52, .52, .85, f"Anillo Fil de {m.lower()}") for i, m in
                 [(17, "Enero"), (7, "Febrero"), (6, "Marzo"), (15, "Abril"), (10, "Junio"), (9, "Julio"),
                  (16, "Agosto"), (8, "Septiembre"), (13, "Octubre"), (12, "Noviembre"), (11, "Diciembre")]]),
    "gravee": dict(
        id="11147793170771", titulo="Pulsera Gravée", handle="pulsera-gravee", tipo="Pulseras", plantilla="joya",
        precio="34.95", frase="Su nombre grabado y su piedra.",
        quedan={"Metal Color": ["Gold with OPP Bag"]},
        opciones={"Metal Color": None, "Main Stone Color|Ships From": None,
                  "Length": ("Mes", MES_EN, MESES)},
        desc="<p>Una barra fina con el nombre grabado y, al lado, una piedra del color de su mes. Para llevar el tuyo "
             "o el de quien quieres.</p><ul>"
             "<li>Acero inoxidable con acabado dorado.</li>"
             "<li>Barra de 20 × 3 mm con el nombre que elijas, grabado tal cual lo escribes.</li>"
             "<li>Circonita redonda del color de su mes.</li>"
             "<li>Cadena ajustable con cierre de mosquetón.</li></ul>"
             "<p><strong>Los colores:</strong> enero, rojo oscuro · febrero, morado · marzo, azul claro · abril, "
             "blanco · mayo, verde · junio, rosa claro · julio, rojo · agosto, verde claro · septiembre, azul oscuro · "
             "octubre, rosa · noviembre, champán · diciembre, turquesa.</p><p>En las fotos, nombre de ejemplo.</p>",
        seo=("Pulsera Gravée · pulsera con nombre grabado y piedra",
             "Pulsera dorada con el nombre grabado en una barra y la piedra de su mes. Envío gratis a península y 3 años de garantía."),
        fotos=[(0, "vida", .5, .5, 1, "Pulsera Gravée puesta, con nombre de ejemplo"),
               (2, "vida", .5, .5, 1, "Pulsera Gravée de cerca"),
               (1, "vida", .5, .5, 1, "Pulsera Gravée en la muñeca"),
               (3, "vida", .5, .5, 1, "Pulsera Gravée con camisa blanca")]),
    "charme": dict(
        id="11147793269075", titulo="Pulsera Charme", handle="pulsera-charme", tipo="Pulseras", plantilla="joya",
        precio="29.95", frase="Una cruz y la piedra de su mes.",
        opciones={"Ships From": None, "Metal Color": ("Mes", MES_EN, MESES)},
        desc="<p>Una pulsera de bolitas doradas con dos colgantes: una cruz de brillantes y una piedra rectangular del "
             "color de su mes.</p><ul>"
             "<li>Acero inoxidable con acabado dorado.</li>"
             "<li>18 cm de largo.</li>"
             "<li>Cruz de 1,5 × 0,8 cm y piedra de 0,7 × 0,3 cm, de circonita.</li></ul>"
             "<p><strong>Los colores:</strong> enero, rojo · febrero, morado oscuro · marzo, azul agua · abril, "
             "blanco · mayo, verde · junio, lavanda · julio, fucsia · agosto, verde claro · septiembre, azul intenso · "
             "octubre, rosa · noviembre, champán · diciembre, turquesa.</p>",
        seo=("Pulsera Charme · pulsera de bolitas con cruz y piedra",
             "Pulsera dorada de bolitas con una cruz y la piedra de su mes. Envío gratis a península y 3 años de garantía."),
        fotos=[(9, "prod", .5, .5, 1, "Pulsera Charme con la piedra verde de mayo"),
               (0, "vida", .5, .5, 1, "Pulsera Charme puesta"),
               (2, "vida", .5, .5, 1, "Pulsera Charme en la muñeca con jersey negro"),
               (4, "vida", .5, .5, 1, "Pulsera Charme con chaqueta negra"),
               (1, "vida", .5, .5, 1, "Pulsera Charme: 18 cm de largo")]
              + [(i, "prod", .5, .5, 1, f"Pulsera Charme de {m.lower()}") for i, m in
                 [(12, "Enero"), (13, "Febrero"), (14, "Marzo"), (8, "Abril"), (10, "Junio"), (15, "Julio"),
                  (16, "Agosto"), (11, "Septiembre"), (17, "Octubre"), (6, "Noviembre"), (7, "Diciembre")]]),
}

Q_PROD = """query($id:ID!){ product(id:$id){ id options{ id name optionValues{ id name } }
  media(first:50){ nodes{ id } }
  variants(first:250){ nodes{ id title selectedOptions{ name value } media(first:1){ nodes{ id } }
    inventoryItem{ id inventoryLevels(first:5){ nodes{ id location{ id } } } } } } } }"""


def leer(pid):
    return gql(Q_PROD, {"id": pid})["product"]


def recorte(im, cx, cy, alto):
    W, H = im.size
    h = int(H * alto); w = int(h * 4 / 5)
    if w > W: w = W; h = int(w * 5 / 4)
    x = int(min(max(cx * W - w / 2, 0), W - w)); y = int(min(max(cy * H - h / 2, 0), H - h))
    return im.crop((x, y, x + w, y + h))


def niebla(im):
    fondo = max(im.getpixel((5, 5)))  # fondo blanco o gris claro del proveedor → blanco → niebla
    im = im.point(lambda v: min(255, round(v * 255 / max(fondo, 1))))
    return ImageChops.multiply(im, Image.new("RGB", im.size, NIEBLA))


def hacer(carpeta, k):
    f = FICHAS[k]; PID = f"gid://shopify/Product/{f['id']}"
    p = leer(PID); M = [m["id"] for m in p["media"]["nodes"]]
    # 1. variantes que sobran
    if f.get("quedan"):
        quitar = [v["id"] for v in p["variants"]["nodes"]
                  if any(o["name"] in f["quedan"] and o["value"] not in f["quedan"][o["name"]] for o in v["selectedOptions"])]
        if quitar:
            gql("""mutation($p:ID!,$v:[ID!]!){ productVariantsBulkDelete(productId:$p, variantsIds:$v){ userErrors{ field message } } }""",
                {"p": PID, "v": quitar}, True)
            p = leer(PID)
    # 2. opciones que sobran (con un solo valor)
    fuera = [o["id"] for o in p["options"] if o["name"] in f["opciones"] and f["opciones"][o["name"]] is None]
    if fuera:
        gql("""mutation($p:ID!,$o:[ID!]!){ productOptionsDelete(productId:$p, options:$o){ userErrors{ field message } } }""",
            {"p": PID, "o": fuera}, True)
        p = leer(PID)
    # 3. nombres y valores en español, y su orden
    orden = []
    for o in p["options"]:
        nuevo, valores, lista = f["opciones"][o["name"]]
        vals = [{"id": x["id"], "name": valores[x["name"]]} for x in o["optionValues"] if x["name"] in valores]
        gql("""mutation($p:ID!,$o:OptionUpdateInput!,$v:[OptionValueUpdateInput!]){ productOptionUpdate(productId:$p, option:$o, optionValuesToUpdate:$v){ userErrors{ field message } } }""",
            {"p": PID, "o": {"id": o["id"], "name": nuevo}, "v": vals}, True)
        orden.append({"name": nuevo, "values": [{"name": n} for n in lista]})
    gql("""mutation($p:ID!,$o:[OptionReorderInput!]!){ productOptionsReorder(productId:$p, options:$o){ userErrors{ field message } } }""",
        {"p": PID, "o": orden}, True)
    # 4. ficha
    gql("""mutation($i:ProductUpdateInput!){ productUpdate(product:$i){ userErrors{ field message } } }""",
        {"i": {"id": PID, "title": f["titulo"], "handle": f["handle"], "vendor": "Lunerie", "productType": f["tipo"],
               "templateSuffix": f["plantilla"], "descriptionHtml": f["desc"], "status": "DRAFT",
               "seo": {"title": f["seo"][0], "description": f["seo"][1]},
               "metafields": [{"namespace": "custom", "key": "frase", "type": "single_line_text_field",
                               "value": f["frase"]}]}}, True)
    # 5. fotos: recorte 4:5 (y fondo niebla), JPEG 97 sin submuestreo, sustituidas en su sitio
    rutas = []
    for i, tipo, cx, cy, alto, alt in f["fotos"]:
        im = Image.open(os.path.join(carpeta, f["id"], f"m{i:02d}.png")).convert("RGB")
        if tipo == "prod":
            im = niebla(im)
        out = recorte(im, cx, cy, alto)
        r = os.path.join(carpeta, f["id"], f"m{i:02d}-final.jpg"); out.save(r, quality=97, subsampling=0); rutas.append(r)
    ins = [{"filename": f"{f['handle']}-{n + 1}.jpg", "mimeType": "image/jpeg", "resource": "IMAGE", "httpMethod": "PUT"}
           for n in range(len(rutas))]
    T = gql("""mutation($i:[StagedUploadInput!]!){ stagedUploadsCreate(input:$i){ stagedTargets{ url resourceUrl parameters{ name value } } userErrors{ field message } } }""",
            {"i": ins}, True)["stagedUploadsCreate"]["stagedTargets"]
    files = []
    for (i, *_, alt), r, t in zip(f["fotos"], rutas, T):
        hdr = []
        for prm in t["parameters"]: hdr += ["-H", f"{prm['name']}: {prm['value']}"]
        code = subprocess.run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "-X", "PUT", "-H",
                               "Content-Type: image/jpeg", *hdr, "--data-binary", "@" + r, t["url"]],
                              capture_output=True, text=True).stdout
        assert code == "200", (k, i, code)
        files.append({"id": M[i], "originalSource": t["resourceUrl"], "alt": alt})
    gql("""mutation($f:[FileUpdateInput!]!){ fileUpdate(files:$f){ userErrors{ field message } } }""", {"f": files}, True)
    # 6. fotos que sobran fuera y orden
    usadas = [M[i] for i, *_ in f["fotos"]]
    sobran = [m for m in M if m not in usadas]
    if sobran:
        gql("""mutation($p:ID!,$m:[ID!]!){ productDeleteMedia(productId:$p, mediaIds:$m){ mediaUserErrors{ field message } } }""",
            {"p": PID, "m": sobran}, True)
    gql("""mutation($p:ID!,$m:[MoveInput!]!){ productReorderMedia(id:$p, moves:$m){ mediaUserErrors{ field message } } }""",
        {"p": PID, "m": [{"id": m, "newPosition": str(n)} for n, m in enumerate(usadas)]}, True)
    # 7. variantes: precio, sin tachado, sin control de stock; foto de variante si cambia
    p = leer(PID)
    vs = [{"id": v["id"], "price": f["precio"], "compareAtPrice": None, "inventoryItem": {"tracked": False}}
          for v in p["variants"]["nodes"]]
    for n in range(0, len(vs), 100):
        gql("""mutation($p:ID!,$v:[ProductVariantsBulkInput!]!){ productVariantsBulkUpdate(productId:$p, variants:$v){ userErrors{ field message } } }""",
            {"p": PID, "v": vs[n:n + 100]}, True)
    if f.get("foto_variante"):
        opcion, mapa = f["foto_variante"]
        unir = []
        for v in p["variants"]["nodes"]:
            valor = next(o["value"] for o in v["selectedOptions"] if o["name"] == opcion)
            if not v["media"]["nodes"]:
                unir.append({"variantId": v["id"], "mediaIds": [M[mapa[valor]]]})
        if unir:
            gql("""mutation($p:ID!,$v:[ProductVariantAppendMediaInput!]!){ productVariantAppendMedia(productId:$p, variantMedia:$v){ userErrors{ field message } } }""",
                {"p": PID, "v": unir}, True)
    # 8. inventario: fuera del «almacén» de DSers, dentro del de la tienda (si no, sale «no disponible»)
    for v in p["variants"]["nodes"]:
        it = v["inventoryItem"]; locs = {l["location"]["id"]: l["id"] for l in it["inventoryLevels"]["nodes"]}
        if LOC not in locs:
            gql("""mutation($i:ID!,$l:ID!){ inventoryActivate(inventoryItemId:$i, locationId:$l) @idempotent(key:"%s"){ userErrors{ field message } } }""" % clave(),
                {"i": it["id"], "l": LOC}, True)
        for lid, lvl in locs.items():
            if lid != LOC:
                gql("""mutation($l:ID!){ inventoryDeactivate(inventoryLevelId:$l) @idempotent(key:"%s"){ userErrors{ field message } } }""" % clave(),
                    {"l": lvl}, True)
    print(k, "ok")


if __name__ == "__main__":
    for k in sys.argv[2:]:
        hacer(sys.argv[1], k)
