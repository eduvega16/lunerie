"""Normaliza los productos importados con DSers (30-oct): variantes, opciones, textos, precio, fotos 4:5 e inventario.
Uso: python productos/normalizar_dsers.py <clave> ...  (claves de FICHAS). Necesita lote.json (datos y fotos
mNN.png de cada producto, bajados antes) en la carpeta del script. Hecho el 30-oct para Maille, Galet, Perle, aros y anillo."""
import json, os, subprocess, sys
from PIL import Image, ImageChops
from gql import gql, clave

LOC = "gid://shopify/Location/127723929939"
NIEBLA = (0xF2, 0xF4, 0xF2)
SP = os.path.dirname(os.path.abspath(__file__))

NO_SUMERGIBLE = "<li>No es sumergible.</li>"
FICHAS = {
    "maille": dict(
        titulo="Reloj Maille", handle="reloj-maille", tipo="Relojes", plantilla="reloj", precio="39.95",
        variantes={"WHITE / China Mainland": "Dorado", "Silver / China Mainland": "Plateado"},
        quitar_opciones=["Ships From"],
        desc="<p>Oval, con la esfera blanca y una correa de malla fina. De los relojes que se llevaban antes y vuelven "
             "ahora: pequeño, ligero y muy fácil de combinar.</p><ul>"
             "<li>Esfera de 20 × 22 mm, caja de aleación dorada o plateada y cristal mineral.</li>"
             "<li>Correa de malla de 7 mm de ancho y 21,5 cm de largo, con cierre ajustable.</li>"
             "<li>Movimiento de cuarzo, con la pila puesta. Pesa 28 g.</li>" + NO_SUMERGIBLE +
             "<li>En la esfera lleva la marca del fabricante, BS Bee Sister.</li></ul>",
        seo="Reloj pequeño oval con esfera blanca y correa de malla, dorado o plateado. Envío gratis a península y 3 años de garantía.",
        fotos=[(8, "vida", .5, "Reloj Maille dorado en la mano"), (2, "vida", .45, "Reloj Maille dorado en la muñeca"),
               (6, "vida", .5, "Reloj Maille plateado en la mano"), (1, "vida", .5, "Reloj Maille dorado, de cerca"),
               (3, "vida", .5, "Reloj Maille dorado con jersey blanco")],
        foto_variante={"Dorado": 8, "Plateado": 6}),
    "galet": dict(
        titulo="Reloj Galet", handle="reloj-galet", tipo="Relojes", plantilla="reloj", precio="34.95",
        variantes={"golden white": "Dorado", "silver": "Plateado"},
        desc="<p>Oval, con la caja gruesa y pulida como un canto rodado y números romanos. Se lleva solo o junto a una "
             "pulsera fina.</p><ul>"
             "<li>Esfera oval de 24 mm, caja de aleación dorada o plateada y cristal.</li>"
             "<li>Correa de eslabones de acero inoxidable, de 10 mm de ancho y 21,5 cm de largo, con cierre de "
             "pulsera. Si te queda grande, en cualquier relojería te quitan un eslabón al momento.</li>"
             "<li>Movimiento de cuarzo, con la pila puesta.</li>" + NO_SUMERGIBLE + "</ul>",
        seo="Reloj oval de caja gruesa con números romanos, dorado o plateado. Envío gratis a península y 3 años de garantía.",
        fotos=[(8, "vida", .5, "Reloj Galet dorado en la mano"), (0, "vida", .45, "Reloj Galet dorado, de perfil"),
               (6, "vida", .45, "Reloj Galet plateado en la mano")],
        foto_variante={"Dorado": 8, "Plateado": 6}),
    "perle": dict(
        titulo="Reloj Perle", handle="reloj-perle", tipo="Relojes", plantilla="reloj", precio="34.95",
        variantes={"1PC Without Box": None}, quitar_opciones=["Color"],
        desc="<p>Oval y dorado, con perlas entre los eslabones de la correa. Delicado, de los que se regalan.</p><ul>"
             "<li>Esfera de 20 × 24 mm, caja de aleación con acabado dorado.</li>"
             "<li>Correa de eslabones con perlas de imitación, de 12 mm de ancho y 20 cm de largo, con cierre de "
             "gancho.</li>"
             "<li>Movimiento de cuarzo, con la pila puesta. Pesa 36 g.</li>" + NO_SUMERGIBLE + "</ul>",
        seo="Reloj pequeño oval dorado con perlas en la correa. Envío gratis a península y 3 años de garantía.",
        fotos=[(3, "vida", .55, "Reloj Perle sobre un libro"), (1, "vida", .6, "Reloj Perle en la muñeca"),
               (2, "vida", .5, "Reloj Perle de cerca"), (4, "vida", .5, "Reloj Perle extendido")]),
    "aros": dict(
        titulo="Aros Boucle", handle="aros-boucle", tipo="Pendientes", plantilla="joya", precio="19.95",
        variantes={"Small-Gold": "Pequeño · 14 mm", "Medium-Gold": "Mediano · 18 mm"}, opcion="Tamaño",
        desc="<p>Aros en forma de U, lisos y dorados. Para llevarlos todos los días, solos o junto a otros.</p><ul>"
             "<li>Dos tamaños: pequeño (14 × 12 mm) y mediano (18 × 12 mm).</li>"
             "<li>Metal con acabado dorado y cierre de bisagra.</li>"
             "<li>Se venden por parejas.</li></ul>",
        seo="Aros dorados en forma de U, pequeños o medianos. Envío gratis a península y 3 años de garantía.",
        fotos=[(4, "prod", .5, "Aros Boucle medianos"), (1, "vida", .5, "Aros Boucle puestos en la oreja"),
               (5, "prod", .5, "Aros Boucle pequeños")],
        foto_variante={"Pequeño · 14 mm": 5, "Mediano · 18 mm": 4}),
    "anillo": dict(
        titulo="Anillo Duo", handle="anillo-duo", tipo="Anillos", plantilla="joya", precio="19.95",
        variantes={"01": None}, quitar_opciones=["Main Stone Color"],
        desc="<p>Dos piezas de esmalte, una azul y otra beige, sobre un aro dorado abierto. Se ajusta a casi cualquier "
             "dedo apretándolo o abriéndolo con suavidad.</p><ul>"
             "<li>Aleación con acabado dorado y esmalte.</li>"
             "<li>Abierto y ajustable, de unos 1,7 cm de diámetro. Pesa 7 g.</li></ul>",
        seo="Anillo dorado abierto con esmalte azul y beige, ajustable. Envío gratis a península y 3 años de garantía.",
        fotos=[(0, "vida", .5, "Anillo Duo sobre tela"), (1, "vida", .4, "Anillo Duo en la mano"),
               (3, "vida", .5, "Anillo Duo de lado"), (4, "vida", .45, "Anillo Duo con jersey azul")]),
}


def crop45(im, cx=0.5, cy=0.5, w=None):
    W, H = im.size
    w = w or min(W, int(H * 4 / 5)); h = int(w * 5 / 4)
    if h > H: h = H; w = int(h * 4 / 5)
    x = int(min(max(cx * W - w / 2, 0), W - w)); y = int(min(max(cy * H - h / 2, 0), H - h))
    return im.crop((x, y, x + w, y + h))


def niebla(im):
    fondo = max(im.getpixel((5, 5)))  # fondo gris claro del proveedor → blanco → niebla
    im = im.point(lambda v: min(255, round(v * 255 / max(fondo, 1))))
    return ImageChops.multiply(im, Image.new("RGB", im.size, NIEBLA))


def hacer(k, p):
    f = FICHAS[k]; PID = p["id"]; M = [m["id"] for m in p["media"]["nodes"]]
    V = {v["title"]: v for v in p["variants"]["nodes"]}
    quitar = [v["id"] for t, v in V.items() if t not in f["variantes"]]
    if quitar:
        gql("""mutation($p:ID!,$v:[ID!]!){ productVariantsBulkDelete(productId:$p, variantsIds:$v){ userErrors{ field message } } }""",
            {"p": PID, "v": quitar}, True)
    for nombre in f.get("quitar_opciones", []):
        o = next(o for o in p["options"] if o["name"] == nombre)
        gql("""mutation($p:ID!,$o:[ID!]!){ productOptionsDelete(productId:$p, options:$o){ userErrors{ field message } } }""",
            {"p": PID, "o": [o["id"]]}, True)
    restantes = [o for o in p["options"] if o["name"] not in f.get("quitar_opciones", [])]
    if restantes:
        o = restantes[0]; ov = {x["name"]: x["id"] for x in o["optionValues"]}
        vals = []
        for viejo, nuevo in f["variantes"].items():
            nombre_valor = viejo.split(" / ")[0]
            if nuevo and nombre_valor in ov:
                vals.append({"id": ov[nombre_valor], "name": nuevo})
        opt = {"id": o["id"]}
        if f.get("opcion"): opt["name"] = f["opcion"]
        gql("""mutation($p:ID!,$o:OptionUpdateInput!,$vals:[OptionValueUpdateInput!]){ productOptionUpdate(productId:$p, option:$o, optionValuesToUpdate:$vals){ userErrors{ field message } } }""",
            {"p": PID, "o": opt, "vals": vals}, True)
    gql("""mutation($i:ProductUpdateInput!){ productUpdate(product:$i){ userErrors{ field message } } }""",
        {"i": {"id": PID, "title": f["titulo"], "handle": f["handle"], "vendor": "Lunerie", "productType": f["tipo"],
               "templateSuffix": f["plantilla"], "descriptionHtml": f["desc"], "status": "DRAFT",
               "seo": {"title": f"{f['titulo']} | Lunerie", "description": f["seo"]}}}, True)
    # fotos: procesar, subir y sustituir en su sitio (conserva el id y el enlace con la variante)
    os.makedirs(os.path.join(SP, k), exist_ok=True)
    rutas = []
    for i, tipo, cx, alt in f["fotos"]:
        im = Image.open(os.path.join(SP, k, f"m{i:02d}.png")).convert("RGB")
        out = niebla(crop45(im, cx, .5)) if tipo == "prod" else crop45(im, cx, .5)
        r = os.path.join(SP, k, f"m{i:02d}-final.jpg"); out.save(r, quality=92); rutas.append(r)
    ins = [{"filename": f"{f['handle']}-{n+1}.jpg", "mimeType": "image/jpeg", "resource": "IMAGE", "httpMethod": "PUT"}
           for n in range(len(rutas))]
    T = gql("""mutation($i:[StagedUploadInput!]!){ stagedUploadsCreate(input:$i){ stagedTargets{ url resourceUrl parameters{ name value } } userErrors{ field message } } }""",
            {"i": ins}, True)["stagedUploadsCreate"]["stagedTargets"]
    files = []
    for (i, _, _, alt), r, t in zip(f["fotos"], rutas, T):
        hdr = []
        for prm in t["parameters"]: hdr += ["-H", f"{prm['name']}: {prm['value']}"]
        code = subprocess.run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "-X", "PUT", "-H",
                               "Content-Type: image/jpeg", *hdr, "--data-binary", "@" + r, t["url"]],
                              capture_output=True, text=True).stdout
        assert code == "200", (k, i, code)
        files.append({"id": M[i], "originalSource": t["resourceUrl"], "alt": alt})
    gql("""mutation($f:[FileUpdateInput!]!){ fileUpdate(files:$f){ userErrors{ field message } } }""", {"f": files}, True)
    # variantes: precio, sin tachado, sin control de stock y su foto
    q = gql("""query($h:String!){ productByHandle(handle:$h){ variants(first:10){ nodes{ id title inventoryItem{ id inventoryLevels(first:5){ nodes{ id location{ id } } } } } } } }""",
            {"h": f["handle"]})["productByHandle"]["variants"]["nodes"]
    vs = []
    for v in q:
        d = {"id": v["id"], "price": f["precio"], "compareAtPrice": None, "inventoryItem": {"tracked": False}}
        fv = f.get("foto_variante", {}).get(v["title"])
        if fv is not None: d["mediaId"] = M[fv]
        vs.append(d)
    gql("""mutation($p:ID!,$v:[ProductVariantsBulkInput!]!){ productVariantsBulkUpdate(productId:$p, variants:$v){ userErrors{ field message } } }""",
        {"p": PID, "v": vs}, True)
    # quitar las fotos que sobran y ordenar
    usadas = {M[i] for i, *_ in f["fotos"]}
    sobran = [m for m in M if m not in usadas]
    if sobran:
        gql("""mutation($p:ID!,$m:[ID!]!){ productDeleteMedia(productId:$p, mediaIds:$m){ mediaUserErrors{ field message } } }""",
            {"p": PID, "m": sobran}, True)
    gql("""mutation($p:ID!,$m:[MoveInput!]!){ productReorderMedia(id:$p, moves:$m){ mediaUserErrors{ field message } } }""",
        {"p": PID, "m": [{"id": M[i], "newPosition": str(n)} for n, (i, *_) in enumerate(f["fotos"])]}, True)
    # inventario: fuera del «almacén» de DSers, dentro del de la tienda (si no, sale «no disponible»)
    for v in q:
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
    todo = json.load(open(os.path.join(SP, "lote.json"), encoding="utf8"))
    for k in sys.argv[1:]:
        hacer(k, todo[k])
