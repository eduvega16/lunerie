"""Sube a Archivos de Shopify las creatividades de la campaña (fotos y vídeos de marca/fotos-ia/campana-bf/) y guarda
sus URL públicas en anuncios/creatividades-urls.json, para dárselas a Meta (el conector de Meta solo sube por URL).
    python anuncios/subir_creatividades.py [fichero ...]     (sin ficheros: todos los de la campaña)
Si un fichero ya está en el JSON, no se vuelve a subir (borrar su línea para forzarlo).
"""
import json, pathlib, subprocess, sys, time

RAIZ = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "productos"))
from gql import gql  # noqa: E402

CARPETA = RAIZ / "marca" / "fotos-ia" / "campana-bf"
SALIDA = RAIZ / "anuncios" / "creatividades-urls.json"
FICHEROS = (["1-oferta-telefono-4x5.jpg", "1-oferta-telefono-9x16.jpg", "2-pack-a-juego-4x5.jpg", "2-pack-a-juego-9x16.jpg",
             "3-carrusel-1-izquierda.jpg", "3-carrusel-2-centro.jpg", "3-carrusel-3-derecha.jpg", "3-carrusel-4-oferta.jpg",
             "4-solo-da-la-hora-4x5.jpg", "4-solo-da-la-hora-9x16.mp4", "5-para-ti-4x5.jpg", "5-para-ti-9x16.jpg",
             "6-menos-de-40-4x5.jpg", "6-menos-de-40-9x16.jpg", "8-oferta-navidad-9x16.mp4"]
            + [f"7-para-tu-{q}-{f}.jpg" for q in ("madre", "hermana", "pareja") for f in ("4x5", "9x16")]
            + [f"{n}-{f}.mp4" for n in ("9-bloqueo", "10-notas", "11-lo-sentimos", "12-piezas-cayendo", "13-pack-a-juego")
               for f in ("9x16", "4x5")])


def subir(ruta):
    video = ruta.suffix == ".mp4"
    mime = "video/mp4" if video else ("image/png" if ruta.suffix == ".png" else "image/jpeg")
    t = gql("""mutation($i:[StagedUploadInput!]!){stagedUploadsCreate(input:$i){stagedTargets{url resourceUrl parameters{name value}}
               userErrors{message}}}""",
            {"i": [{"filename": ruta.name, "mimeType": mime, "resource": "VIDEO" if video else "FILE",
                    "httpMethod": "POST", **({"fileSize": str(ruta.stat().st_size)} if video else {})}]},
            True)["stagedUploadsCreate"]["stagedTargets"][0]
    campos = sum([["-F", f"{p['name']}={p['value']}"] for p in t["parameters"]], [])
    r = subprocess.run(["curl", "-s", "-o", "NUL" if sys.platform == "win32" else "/dev/null", "-w", "%{http_code}",
                        *campos, "-F", f"file=@{ruta}", t["url"]], capture_output=True, text=True)
    assert r.stdout.strip() in ("200", "201", "204"), (ruta.name, r.stdout, r.stderr[-300:])
    f = gql("""mutation($f:[FileCreateInput!]!){fileCreate(files:$f){files{id} userErrors{message}}}""",
            {"f": [{"originalSource": t["resourceUrl"], "contentType": "VIDEO" if video else "IMAGE",
                    "filename": ruta.name}]}, True)["fileCreate"]["files"][0]["id"]
    for _ in range(90):
        n = gql("""query($id:ID!){node(id:$id){... on MediaImage{fileStatus image{url}}
                   ... on Video{fileStatus originalSource{url} sources{url mimeType height}}}}""", {"id": f})["node"]
        if video and n.get("fileStatus") == "READY" and n.get("sources"):
            mp4 = sorted((s for s in n["sources"] if s["mimeType"] == "video/mp4"), key=lambda s: -(s["height"] or 0))
            return (mp4[0] if mp4 else n["originalSource"])["url"]
        if not video and n.get("image"):
            return n["image"]["url"]
        if n.get("fileStatus") == "FAILED":
            raise RuntimeError(f"Shopify no pudo procesar {ruta.name}")
        time.sleep(4)
    raise RuntimeError(f"Shopify tardó demasiado con {ruta.name}")


if __name__ == "__main__":
    urls = json.loads(SALIDA.read_text(encoding="utf8")) if SALIDA.exists() else {}
    for nombre in sys.argv[1:] or FICHEROS:
        if nombre in urls:
            continue
        urls[nombre] = subir(CARPETA / nombre)
        SALIDA.write_text(json.dumps(urls, ensure_ascii=False, indent=1) + "\n", encoding="utf8")
        print(nombre, "->", urls[nombre][:90], flush=True)
    print("listo:", len(urls), "ficheros")
