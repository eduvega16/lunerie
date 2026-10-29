"""Publica en Instagram las piezas de la cola con estado «aprobado» (API oficial de publicación de contenido).

    python oficina/publicar.py                  lista lo aprobado y si está listo (no hace nada)
    python oficina/publicar.py ID               ensayo: enseña qué haría, sin red y sin publicar
    python oficina/publicar.py ID --confirmar   publica de verdad

Claves en .env.local (fuera de git): IG_TOKEN, IG_USER_ID y, si hace falta, IG_HOST (graph.instagram.com con Instagram Login,
graph.facebook.com con Facebook Login) e IG_VERSION. Nunca se imprimen.
La pieza necesita `publicacion` (ver cola/ESQUEMA.md): `archivos` (rutas locales, JPG/PNG o MP4) o `urls` (ya públicas, obligatorio para vídeo).
La API de Instagram no programa ni añade música: la hora la pone quien lanza este script.
"""
import glob, json, os, pathlib, subprocess, sys, tempfile, time, urllib.parse, urllib.request
from dotenv import load_dotenv
from PIL import Image

RAIZ = pathlib.Path(__file__).resolve().parent.parent
COLA = RAIZ / "oficina" / "cola"
SALIDA = RAIZ / "oficina" / "salida"
TIENDA = "qjxvnn-xq.myshopify.com"
load_dotenv(RAIZ / ".env.local")
HOST = os.environ.get("IG_HOST", "graph.instagram.com")
VERSION = os.environ.get("IG_VERSION", "v26.0")
TIPOS = {"foto": "IMAGE", "carrusel": "CAROUSEL", "reel": "REELS", "story": "STORIES"}


def piezas():
    for f in sorted(glob.glob(str(COLA / "20*.json"))):
        yield pathlib.Path(f), json.loads(pathlib.Path(f).read_text(encoding="utf-8"))


def revisar(p):
    """Lista de problemas que impiden publicar la pieza (vacía = lista)."""
    pub, fallos = p.get("publicacion") or {}, []
    if p.get("estado") != "aprobado":
        fallos.append(f"estado «{p.get('estado')}» (solo se publica «aprobado»)")
    if p.get("plataforma") != "instagram":
        fallos.append("la plataforma no es instagram")
    if p.get("formato") not in TIPOS:
        fallos.append(f"formato «{p.get('formato')}» no soportado")
    fuentes = pub.get("urls") or pub.get("archivos") or []
    if not fuentes:
        fallos.append("falta publicacion.archivos o publicacion.urls (sin material no hay qué publicar)")
    for a in pub.get("archivos") or []:
        if not (RAIZ / a).exists():
            fallos.append(f"no existe {a}")
    if p.get("formato") == "carrusel" and not 2 <= len(fuentes) <= 20:
        fallos.append("un carrusel lleva de 2 a 20 archivos")
    if p.get("formato") == "reel" and not pub.get("urls"):
        fallos.append("un reel necesita publicacion.urls con el MP4 ya público")
    return fallos


def a_jpeg(ruta):
    """Instagram solo acepta JPEG para imágenes: convierte a oficina/salida/ (carpeta que no va a git)."""
    SALIDA.mkdir(exist_ok=True)
    destino = SALIDA / (pathlib.Path(ruta).stem + ".jpg")
    im = Image.open(RAIZ / ruta).convert("RGB")
    ancho, alto = im.size
    if ancho / alto < 0.8:                                  # Instagram no admite fotos más estrechas que 4:5: recorte centrado
        nuevo = round(ancho / 0.8); arriba = (alto - nuevo) // 2
        im = im.crop((0, arriba, ancho, arriba + nuevo))
    im.save(destino, quality=92)
    return destino


def shopify(consulta, variables):
    with tempfile.TemporaryDirectory() as d:
        q, v = pathlib.Path(d, "q.graphql"), pathlib.Path(d, "v.json")
        q.write_text(consulta, encoding="utf-8"); v.write_text(json.dumps(variables), encoding="utf-8")
        r = subprocess.run(["shopify", "store", "execute", "-s", TIENDA, "--query-file", str(q), "--variable-file", str(v),
                            "--json", "--no-input", "--allow-mutations"], capture_output=True, text=True, shell=os.name == "nt")
    d = json.loads(r.stdout or "{}")
    if "error" in d or "errors" in d or r.returncode:
        raise RuntimeError(f"Shopify: {(r.stdout or r.stderr)[:400]}")
    return d.get("data", d)


def subir_publico(jpg):
    """Sube el JPG a Archivos de Shopify y devuelve su URL pública (Instagram la descarga con cURL)."""
    jpg = pathlib.Path(jpg)
    st = shopify("""mutation($i:[StagedUploadInput!]!){stagedUploadsCreate(input:$i){stagedTargets{url resourceUrl}
        userErrors{message}}}""", {"i": [{"filename": jpg.name, "mimeType": "image/jpeg", "httpMethod": "PUT", "resource": "FILE"}]})
    t = st["stagedUploadsCreate"]["stagedTargets"][0]
    subprocess.run(["curl", "-s", "-f", "-X", "PUT", "-H", "Content-Type: image/jpeg", "--data-binary", f"@{jpg}", t["url"]], check=True)
    fc = shopify("""mutation($f:[FileCreateInput!]!){fileCreate(files:$f){files{id} userErrors{message}}}""",
                 {"f": [{"originalSource": t["resourceUrl"], "contentType": "IMAGE", "filename": jpg.name}]})
    fid = fc["fileCreate"]["files"][0]["id"]
    for _ in range(30):
        n = shopify("""query($id:ID!){node(id:$id){... on MediaImage{fileStatus image{url}}}}""", {"id": fid})["node"]
        if n and n.get("image"):
            return n["image"]["url"], fid
        time.sleep(2)
    raise RuntimeError("Shopify tardó demasiado en procesar la imagen")


def url_lista(url, intentos=8):
    """Espera a que el CDN sirva la imagen (200 + image/jpeg) antes de dársela a Instagram, que la descarga nada más recibirla."""
    for _ in range(intentos):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, method="HEAD"), timeout=20) as r:
                if r.status == 200 and "image" in r.headers.get("Content-Type", ""):
                    time.sleep(5)
                    return
        except Exception:
            pass
        time.sleep(5)
    raise RuntimeError(f"La URL pública no responde como imagen: {url}")


def crear(ruta, intentos=4, **params):
    """POST a /media con reintentos: Instagram a veces no consigue bajar la imagen a la primera (error 2207052)."""
    for i in range(intentos):
        try:
            return api("POST", ruta, **params)["id"]
        except RuntimeError as e:
            if "2207052" not in str(e) or i == intentos - 1:
                raise
            time.sleep(20)


def api(metodo, ruta, **params):
    token = os.environ["IG_TOKEN"]
    url = f"https://{HOST}/{VERSION}/{ruta}"
    datos = urllib.parse.urlencode(params).encode() if metodo == "POST" else None
    if metodo == "GET" and params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, data=datos, method=metodo, headers={"Authorization": f"Bearer {token}"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"Instagram {e.code}: {e.read().decode()[:500]}") from None


def esperar(contenedor, video):
    for _ in range(5 if video else 2):
        estado = api("GET", contenedor, fields="status_code").get("status_code")
        if estado == "FINISHED":
            return
        if estado in ("ERROR", "EXPIRED"):
            raise RuntimeError(f"El contenedor {contenedor} quedó en {estado}")
        time.sleep(60 if video else 5)
    raise RuntimeError(f"El contenedor {contenedor} no terminó a tiempo")


def pie(p):
    return p["copy"].strip() + "\n\n" + " ".join(p.get("hashtags") or [])


def publicar(fichero, p, confirmar):
    pub, tipo, ia = p["publicacion"], TIPOS[p["formato"]], p["publicacion"].get("ia", True)
    ig = os.environ.get("IG_USER_ID", "<IG_USER_ID>")
    if pub.get("urls"):
        urls = list(pub["urls"])
    elif confirmar:
        urls = [subir_publico(a_jpeg(a))[0] for a in pub["archivos"]]
        for u in urls:
            url_lista(u)
    else:
        urls = [f"<URL pública de {a} (JPEG)>" for a in pub["archivos"]]
    video = tipo in ("REELS", "STORIES") and urls[0].lower().split("?")[0].endswith((".mp4", ".mov"))
    alt = pub.get("alt_text")
    pasos = []                                              # (descripción, params) de cada petición a /media
    if tipo == "CAROUSEL":
        for u in urls:
            pasos.append(("hijo", dict(image_url=u, is_carousel_item="true")))
        raiz = dict(media_type="CAROUSEL", caption=pie(p))
    elif tipo == "IMAGE":
        raiz = dict(image_url=urls[0], caption=pie(p), **({"alt_text": alt} if alt else {}))
    elif tipo == "REELS":
        raiz = dict(media_type=tipo, video_url=urls[0], caption=pie(p))
    else:                                                   # STORIES: foto o vídeo, sin pie
        raiz = dict(media_type=tipo, video_url=urls[0]) if video else dict(media_type=tipo, image_url=urls[0])
    if ia:
        raiz["is_ai_generated"] = "true"                    # autoetiqueta de IA (solo en el contenedor raíz del carrusel)
    print(f"\n{p['id']} · {tipo} · {len(urls)} archivo(s) · IA={'sí' if ia else 'no'}")
    if not confirmar:
        for d, par in pasos:
            print(f"  POST /{ig}/media {par}")
        print(f"  POST /{ig}/media {raiz}" + ("  (children = los de arriba)" if pasos else ""))
        print(f"  POST /{ig}/media_publish creation_id=<contenedor>\n  (ensayo: no se ha publicado nada)")
        return
    if tipo == "CAROUSEL":
        hijos = [crear(f"{ig}/media", **par) for _, par in pasos]
        for h in hijos:
            esperar(h, False)
        raiz["children"] = ",".join(hijos)
    cont = crear(f"{ig}/media", **raiz)
    esperar(cont, video)
    media = api("POST", f"{ig}/media_publish", creation_id=cont)["id"]
    p["estado"] = "publicado"
    p["publicacion"]["resultado"] = {"media_id": media, "fecha": time.strftime("%Y-%m-%dT%H:%M:%S%z")}
    fichero.write_text(json.dumps(p, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"  Publicado. media_id={media}")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    confirmar = "--confirmar" in sys.argv
    if not args:
        for f, p in piezas():
            if p.get("estado") == "aprobado":
                fallos = revisar(p)
                print(f"{p['id']}: " + ("LISTA para publicar" if not fallos else "NO lista · " + " · ".join(fallos)))
        sys.exit()
    for f, p in piezas():
        if p["id"].startswith(args[0]):
            fallos = revisar(p)
            if fallos:
                sys.exit(f"{p['id']} no se puede publicar: " + " · ".join(fallos))
            if confirmar and not all(os.environ.get(k) for k in ("IG_TOKEN", "IG_USER_ID")):
                sys.exit("Faltan IG_TOKEN o IG_USER_ID en .env.local")
            publicar(f, p, confirmar)
            break
    else:
        sys.exit(f"No hay ninguna pieza que empiece por {args[0]}")
