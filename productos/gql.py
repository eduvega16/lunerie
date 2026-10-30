"""Ayudante: GraphQL de Shopify (Admin) por la CLI, con variables. Uso: from gql import gql"""
import json, os, subprocess, tempfile, uuid

TIENDA = "qjxvnn-xq.myshopify.com"


def gql(query, variables=None, mutar=False):
    d = tempfile.mkdtemp()
    q = os.path.join(d, "q.graphql"); open(q, "w", encoding="utf8").write(query)
    cmd = ["shopify", "store", "execute", "-s", TIENDA, "--query-file", q, "--json", "--no-input"]
    if variables is not None:
        v = os.path.join(d, "v.json"); open(v, "w", encoding="utf8").write(json.dumps(variables))
        cmd += ["--variable-file", v]
    if mutar:
        cmd.append("--allow-mutations")
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf8", shell=os.name == "nt")
    try:
        data = json.loads(r.stdout)
    except Exception:
        raise RuntimeError(f"Sin JSON: {r.stdout[:500]} {r.stderr[-1500:]}")
    if isinstance(data, dict) and ("error" in data or "errors" in data):
        raise RuntimeError(json.dumps(data)[:1500])
    # userErrors en cualquier nivel
    def errores(x):
        if isinstance(x, dict):
            for k, val in x.items():
                if k == "userErrors" and val:
                    yield val
                else:
                    yield from errores(val)
        elif isinstance(x, list):
            for i in x:
                yield from errores(i)
    e = list(errores(data))
    if e:
        raise RuntimeError(f"userErrors: {e}")
    return data


def clave():
    return str(uuid.uuid4())
