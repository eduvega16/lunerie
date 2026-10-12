"""Sube los textos de legal/ a Shopify (políticas + páginas) con la Admin API de Shopify CLI.

Los datos personales NO se guardan en el repositorio: se pasan al ejecutar, por variables de entorno.
    LUNERIE_NOMBRE="…" LUNERIE_NIF="…" LUNERIE_DIRECCION="…" python legal/subir.py
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

datos = {k: os.environ.get(f"LUNERIE_{k}", "").strip() for k in ("NOMBRE", "NIF", "DIRECCION")}
if not all(datos.values()):
    sys.exit("Faltan LUNERIE_NOMBRE, LUNERIE_NIF o LUNERIE_DIRECCION")
HUECOS = {"[NOMBRE]": datos["NOMBRE"], "[NIF]": datos["NIF"], "[DIRECCIÓN]": datos["DIRECCION"],
          "[DIRECCIÓN DE DEVOLUCIONES]": datos["DIRECCION"]}


def html(fichero):
    """Devuelve (título, cuerpo HTML) con los huecos personales rellenos ([PLAZO] se queda visible a propósito)."""
    texto = (DIR / fichero).read_text(encoding="utf8")
    for hueco, valor in HUECOS.items():
        texto = texto.replace(hueco, valor)
    titulo, cuerpo = texto.split("\n", 1)
    # «**Pregunta**» sola en su línea: salto de línea antes de la respuesta
    cuerpo = re.sub(r"^(\*\*[^\n]+\*\*)$", r"\1  ", cuerpo, flags=re.M)
    return titulo.lstrip("# ").strip(), markdown.markdown(cuerpo.strip())


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
