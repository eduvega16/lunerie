"""Sube ficheros de tema/tienda/ a un tema de Shopify por la Admin API (themeFilesUpsert), sin `shopify theme push`.

Sirve cuando la sesión de la CLI de temas falla («you don't have access to this dev store») pero `shopify store
execute` funciona (2-nov). Uso:
    python tema/subir_api.py <id del tema> snippets/lunerie-inicio.liquid templates/index.json ...
Para el tema publicado Shopify puede negarse (pide exención); en los temas sin publicar funciona.
"""
import pathlib, sys, time

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "productos"))
from gql import gql  # noqa: E402

TIENDA = pathlib.Path(__file__).resolve().parent / "tienda"

SUBIR = """mutation($tema: ID!, $files: [OnlineStoreThemeFilesUpsertFileInput!]!) {
  themeFilesUpsert(themeId: $tema, files: $files) {
    upsertedThemeFiles { filename }
    job { id }
    userErrors { filename code message }
  }
}"""

TRABAJO = "query($id: ID!) { job(id: $id) { done } }"


def subir(tema, nombres):
    files = [{"filename": n, "body": {"type": "TEXT", "value": (TIENDA / n).read_text(encoding="utf8")}}
             for n in nombres]
    r = gql(SUBIR, {"tema": f"gid://shopify/OnlineStoreTheme/{tema}", "files": files}, mutar=True)
    res = r["themeFilesUpsert"]
    job = (res.get("job") or {}).get("id")
    while job and not gql(TRABAJO, {"id": job})["job"]["done"]:
        time.sleep(1)
    return [f["filename"] for f in res["upsertedThemeFiles"]]


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    print("Subidos:", ", ".join(subir(sys.argv[1], sys.argv[2:])))
