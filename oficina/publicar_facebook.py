"""Publica una pieza de la cola en la PÁGINA de Facebook de Lunerie, como publicación con varias fotos (18-nov).

Uso: python oficina/publicar_facebook.py <id de la pieza>   (publica de verdad; solo con el OK de Edu)
Sube cada archivo de publicacion.archivos sin publicar (/photos published=false) y luego una sola publicación
(/feed con attached_media). Usa el token de página de .env.local (IG_TOKEN, con pages_manage_posts). Solo fotos;
los reels de Facebook van por otro sitio (/video_reels), sin hacer. No imprime claves."""
import json, sys, pathlib, subprocess
sys.stdout.reconfigure(encoding="utf-8")
RAIZ = pathlib.Path("D:/LUNERIE")
env = dict(l.split("=", 1) for l in (RAIZ / ".env.local").read_text(encoding="utf-8").splitlines()
           if "=" in l and not l.startswith("#"))
T = env["IG_TOKEN"].strip().strip('"')
PAGINA = "1376893392171782"
V = "v26.0"
pieza = json.loads((RAIZ / "oficina" / "cola" / f"{sys.argv[1]}.json").read_text(encoding="utf-8"))
texto = pieza["copy"].strip() + "\n\n" + " ".join(pieza.get("hashtags") or [])


def curl(args):
    r = subprocess.run(["curl", "-s"] + args, capture_output=True, text=True, encoding="utf-8")
    d = json.loads(r.stdout)
    if "error" in d:
        sys.exit("ERROR: " + d["error"].get("message", str(d["error"])))
    return d


ids = []
for a in pieza["publicacion"]["archivos"]:
    d = curl(["-X", "POST", f"https://graph.facebook.com/{V}/{PAGINA}/photos",
              "--form-string", "published=false", "--form-string", f"access_token={T}", "-F", f"source=@{RAIZ / a}"])
    ids.append(d["id"])
    print("foto subida", a.rsplit("/", 1)[-1])
campos = ["-X", "POST", f"https://graph.facebook.com/{V}/{PAGINA}/feed",
          "--form-string", f"message={texto}", "--form-string", f"access_token={T}"]
for i, fid in enumerate(ids):
    campos += ["--form-string", f"attached_media[{i}]=" + json.dumps({"media_fbid": fid})]
post = curl(campos)
print("Publicado en Facebook:", post["id"])
