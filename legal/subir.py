"""Sube los textos de legal/ a Shopify (políticas + páginas) con la Admin API de Shopify CLI.

Los datos personales NO se guardan en el repositorio: se pasan al ejecutar, por variables de entorno.
    LUNERIE_NOMBRE="…" LUNERIE_NIF="…" LUNERIE_DIRECCION="…" python legal/subir.py
Sin esas variables, se leen de la política de privacidad que ya está en Shopify (línea «Responsable»).
Con nombres de fichero, sube solo esos:  python legal/subir.py privacidad.md
Requiere `shopify store auth` hecho para la tienda (ver CLAUDE.md, apartado 6).
"""
import json, os, pathlib, re, subprocess, sys, tempfile
import markdown

STORE = "qjxvnn-xq.myshopify.com"
DIR = pathlib.Path(__file__).parent
POLITICAS = {  # fichero → tipo de política de Shopify (Configuración → Políticas)
    "aviso-legal.md": "LEGAL_NOTICE",
    "devoluciones.md": "REFUND_POLICY",
    "envios.md": "SHIPPING_POLICY",
    "privacidad.md": "PRIVACY_POLICY",
    "terminos.md": "TERMS_OF_SERVICE",
    "contacto.md": "CONTACT_INFORMATION",
}
PAGINAS = {"envios.md": "envios", "preguntas-frecuentes.md": "preguntas-frecuentes"}  # fichero → handle
SOLO = set(sys.argv[1:])  # vacío = todo
if SOLO - set(POLITICAS) - set(PAGINAS):
    sys.exit(f"No conozco: {', '.join(sorted(SOLO - set(POLITICAS) - set(PAGINAS)))}")
if SOLO:
    POLITICAS = {f: t for f, t in POLITICAS.items() if f in SOLO}
    PAGINAS = {f: h for f, h in PAGINAS.items() if f in SOLO}


def html(fichero):
    """Devuelve (título, cuerpo HTML) con los huecos personales rellenos ([PLAZO] se queda visible a propósito)."""
    texto = (DIR / fichero).read_text(encoding="utf8")
    for hueco, valor in HUECOS.items():
        texto = texto.replace(hueco, valor)
    titulo, cuerpo = texto.split("\n", 1)
    # «**Pregunta**» sola en su línea: salto de línea antes de la respuesta
    cuerpo = re.sub(r"^(\*\*[^\n]+\*\*)$", r"\1  ", cuerpo, flags=re.M)
    return titulo.lstrip("# ").strip(), markdown.markdown(cuerpo.strip(), extensions=["tables"])


def gql(query, variables):
    with tempfile.TemporaryDirectory() as tmp:
        q, v = pathlib.Path(tmp, "q.graphql"), pathlib.Path(tmp, "v.json")
        q.write_text(query, encoding="utf8")
        v.write_text(json.dumps(variables, ensure_ascii=False), encoding="utf8")
        r = subprocess.run(f'shopify store execute -s {STORE} --query-file "{q}" --variable-file "{v}" '
                           "--allow-mutations --json --no-input", shell=True, capture_output=True, text=True,
                           encoding="utf8")
    salida = "\n".join(l for l in r.stdout.splitlines() if '"type":"progress"' not in l)
    try:
        return json.loads(salida)
    except json.JSONDecodeError:
        sys.exit(f"Error de Shopify CLI:\n{salida}\n{r.stderr}")


datos = {k: os.environ.get(f"LUNERIE_{k}", "").strip() for k in ("NOMBRE", "NIF", "DIRECCION")}
if not all(datos.values()):
    # Los mismos que ya están publicados: «Responsable: [NOMBRE] · NIF [NIF] · [DIRECCIÓN]» (no se imprimen)
    politicas = gql("query { shop { shopPolicies { type body } } }", {})["shop"]["shopPolicies"]
    privacidad = next((p["body"] for p in politicas if p["type"] == "PRIVACY_POLICY"), "")
    m = re.search(r"Responsable:</strong>\s*(.+?)\s*·\s*NIF\s*(.+?)\s*·\s*(.+?)\s*</li>", privacidad, re.S)
    if not m:
        sys.exit("Faltan LUNERIE_NOMBRE, LUNERIE_NIF o LUNERIE_DIRECCION (y no están en la política publicada)")
    datos = dict(zip(("NOMBRE", "NIF", "DIRECCION"), m.groups()))
HUECOS = {"[NOMBRE]": datos["NOMBRE"], "[NIF]": datos["NIF"], "[DIRECCIÓN]": datos["DIRECCION"],
          "[DIRECCIÓN DE DEVOLUCIONES]": datos["DIRECCION"]}


for fichero, tipo in POLITICAS.items():
    _, body = html(fichero)
    r = gql("mutation($p: ShopPolicyInput!) { shopPolicyUpdate(shopPolicy: $p) { shopPolicy { type url } "
            "userErrors { field message } } }", {"p": {"type": tipo, "body": body}})
    res = r["shopPolicyUpdate"]
    print(tipo, "→", res["userErrors"] or res["shopPolicy"]["url"])

for fichero, handle in PAGINAS.items():
    titulo, body = html(fichero)
    existe = gql("query($q: String!) { pages(first: 1, query: $q) { nodes { id } } }",
                 {"q": f"handle:{handle}"})["pages"]["nodes"]
    if existe:
        r = gql("mutation($id: ID!, $p: PageUpdateInput!) { pageUpdate(id: $id, page: $p) { page { handle } "
                "userErrors { field message } } }", {"id": existe[0]["id"], "p": {"title": titulo, "body": body}})
        res = r["pageUpdate"]
    else:
        r = gql("mutation($p: PageCreateInput!) { pageCreate(page: $p) { page { handle } "
                "userErrors { field message } } }",
                {"p": {"title": titulo, "handle": handle, "body": body, "isPublished": True}})
        res = r["pageCreate"]
    print("página", handle, "→", res["userErrors"] or "ok")
