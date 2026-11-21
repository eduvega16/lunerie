"""Publica piezas de la cola en la PÁGINA de Facebook de Lunerie (18-nov; reels y automático, 21-nov).

    python oficina/publicar_facebook.py --pendientes        lista lo publicado en Instagram que falta en Facebook
    python oficina/publicar_facebook.py ID                  ensayo: enseña qué haría, sin publicar
    python oficina/publicar_facebook.py ID --confirmar      publica de verdad

`oficina/publicar.py` llama a `publicar_fb()` justo después de publicar en Instagram (21-nov, Edu: «sube todo el
contenido a Facebook»), así que lo programado sale en los dos sitios. Si Facebook falla, Instagram ya está publicado y el
error queda en el registro: se repite a mano con este script.

- foto / carrusel: cada archivo se sube sin publicar (/photos published=false) y luego una sola publicación (/feed con
  attached_media). Si la pieza solo tiene `urls`, se suben por URL.
- reel: /video_reels en tres pasos (start → rupload con el archivo, que se baja de `publicacion.urls` → finish).
- story: no se publica (en Facebook duran 24 h y no aportan a la página).
Deja `publicacion.facebook = {post_id, fecha}` en la pieza: lo que ya lo tiene no se vuelve a subir.
Usa el token de página de .env.local (IG_TOKEN, con pages_manage_posts). No imprime claves."""
import json, os, pathlib, subprocess, sys, tempfile, time, urllib.request

RAIZ = pathlib.Path(__file__).resolve().parent.parent
COLA = RAIZ / "oficina" / "cola"
PAGINA = "1376893392171782"
V = "v26.0"


def _token():
    env = dict(l.split("=", 1) for l in (RAIZ / ".env.local").read_text(encoding="utf-8").splitlines()
               if "=" in l and not l.startswith("#"))
    return env["IG_TOKEN"].strip().strip('"')


def _curl(args):
    r = subprocess.run(["curl", "-s", "-m", "300"] + args, capture_output=True, text=True, encoding="utf-8",
                       errors="replace")
    try:
        d = json.loads(r.stdout)
    except json.JSONDecodeError:
        raise RuntimeError(f"Facebook: respuesta rara: {(r.stdout or r.stderr)[:300]}")
    if isinstance(d, dict) and "error" in d:
        e = d["error"]
        raise RuntimeError(f"Facebook: {e.get('message', e)}")
    return d


def texto(p):
    return p["copy"].strip() + "\n\n" + " ".join(p.get("hashtags") or [])


def que_hace(p):
    """None si se puede publicar en Facebook; si no, el motivo."""
    pub = p.get("publicacion") or {}
    if (pub.get("facebook") or {}).get("omitida"):
        return "no se sube: " + pub["facebook"]["omitida"]
    if pub.get("facebook"):
        return "ya está en Facebook"
    if p.get("formato") == "story":
        return "las stories no se suben a Facebook"
    if p.get("formato") == "reel" and not pub.get("urls"):
        return "el reel no tiene la URL pública del MP4"
    if p.get("formato") in ("foto", "carrusel"):
        if not (pub.get("archivos") or pub.get("urls")):
            return "sin material"
        falta = [a for a in pub.get("archivos") or [] if not (RAIZ / a).exists()]
        if falta and not pub.get("urls"):
            return f"faltan archivos en este PC: {', '.join(falta)}"
        return None
    if p.get("formato") == "reel":
        return None
    return f"formato «{p.get('formato')}» no soportado"


def publicar_fb(fichero, p, confirmar=True):
    """Publica la pieza en la página. Devuelve el id de la publicación (o None si no toca o es ensayo)."""
    motivo = que_hace(p)
    if motivo:
        print(f"  Facebook: no se publica ({motivo})")
        return None
    pub, T = p["publicacion"], _token()
    if not confirmar:
        print(f"  Facebook (ensayo): {p['formato']} con {len(pub.get('archivos') or pub.get('urls'))} archivo(s)")
        return None
    if p["formato"] == "reel":
        url = pub["urls"][0]
        d = _curl(["-X", "POST", f"https://graph.facebook.com/{V}/{PAGINA}/video_reels",
                   "--form-string", "upload_phase=start", "--form-string", f"access_token={T}"])
        vid = d["video_id"]
        # 21-nov: con «file_url» Facebook no consigue bajar los MP4 del CDN de Shopify («There was a problem uploading
        # your video file»); bajándolo aquí y subiendo el archivo, sí.
        with tempfile.TemporaryDirectory() as tmp:
            mp4 = pathlib.Path(tmp, "reel.mp4")
            urllib.request.urlretrieve(url, mp4)
            _curl(["-X", "POST", f"https://rupload.facebook.com/video-upload/{V}/{vid}",
                   "-H", f"Authorization: OAuth {T}", "-H", "offset: 0", "-H", f"file_size: {mp4.stat().st_size}",
                   "--data-binary", f"@{mp4}"])
        _curl(["-X", "POST", f"https://graph.facebook.com/{V}/{PAGINA}/video_reels",
               "--form-string", "upload_phase=finish", "--form-string", f"video_id={vid}",
               "--form-string", "video_state=PUBLISHED", "--form-string", f"description={texto(p)}",
               "--form-string", f"access_token={T}"])
        post = vid
    else:
        ids = []
        locales = [RAIZ / a for a in pub.get("archivos") or []]
        if locales and all(f.exists() for f in locales):
            fuentes = [("-F", f"source=@{f}") for f in locales]
        else:
            fuentes = [("--form-string", f"url={u}") for u in pub["urls"]]
        for flag, valor in fuentes:
            d = _curl(["-X", "POST", f"https://graph.facebook.com/{V}/{PAGINA}/photos",
                       "--form-string", "published=false", "--form-string", f"access_token={T}", flag, valor])
            ids.append(d["id"])
        campos = ["-X", "POST", f"https://graph.facebook.com/{V}/{PAGINA}/feed",
                  "--form-string", f"message={texto(p)}", "--form-string", f"access_token={T}"]
        for i, fid in enumerate(ids):
            campos += ["--form-string", f"attached_media[{i}]=" + json.dumps({"media_fbid": fid})]
        post = _curl(campos)["id"]
    pub["facebook"] = {"post_id": post, "fecha": time.strftime("%Y-%m-%dT%H:%M:%S%z")}
    fichero.write_text(json.dumps(p, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"  Publicado en Facebook: {post}")
    return post


def _piezas():
    for f in sorted(COLA.glob("20*.json")):
        yield f, json.loads(f.read_text(encoding="utf-8"))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--pendientes" in sys.argv:
        for f, p in _piezas():
            if p.get("estado") == "publicado":
                m = que_hace(p)
                print(f"{p['id']}: " + ("FALTA en Facebook" if not m else m))
        sys.exit()
    if not args:
        sys.exit(__doc__)
    for f, p in _piezas():
        if p["id"].startswith(args[0]):
            print(p["id"])
            publicar_fb(f, p, "--confirmar" in sys.argv)
            break
    else:
        sys.exit(f"No hay ninguna pieza que empiece por {args[0]}")
