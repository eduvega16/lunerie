"""Renueva la clave de Instagram (IG_TOKEN) sin pasar nunca el token por el chat (4-nov: Meta cortó el acceso,
«API access blocked» / error 190 al publicar).

Pasos de Edu (el inicio de sesión en Meta lo hace él):
  1. developers.facebook.com → Mis apps → «Lunerie Vega» (2676185462837815): si hay un aviso (app restringida,
     comprobación del uso de datos, verificación), resolverlo primero.
  2. Herramientas → Explorador de la API Graph → app «Lunerie Vega» → «Generar token de acceso» con los permisos
     instagram_basic, instagram_content_publish, pages_show_list, pages_read_engagement, business_management
     y pages_manage_posts (8-nov: para publicar también en la página de Facebook).
  3. Pegar ese token en D:\\LUNERIE\\.env.local en una línea  IG_TOKEN_USUARIO=...   (NO en el chat).
Después:  python oficina/renovar_token.py
  → lo cambia por uno largo, saca el token de la página «L U N E R I E» (no caduca), lo guarda como IG_TOKEN,
    borra IG_TOKEN_USUARIO de .env.local y comprueba que ve la cuenta de Instagram. Nunca imprime los tokens.
"""
import json, pathlib, sys, urllib.error, urllib.parse, urllib.request
from dotenv import dotenv_values

RAIZ = pathlib.Path(__file__).resolve().parent.parent
ENV = RAIZ / ".env.local"
API = "https://graph.facebook.com/v21.0"


def get(ruta, **q):
    try:
        return json.load(urllib.request.urlopen(f"{API}/{ruta}?{urllib.parse.urlencode(q)}"))
    except urllib.error.HTTPError as e:
        sys.exit(f"Meta {e.code}: {e.read().decode()[:400]}")


def guardar(clave, valor, quitar=()):
    lineas = [l for l in ENV.read_text(encoding="utf8").splitlines()
              if not l.startswith(f"{clave}=") and not any(l.startswith(f"{q}=") for q in quitar)]
    lineas.append(f"{clave}={valor}")
    ENV.write_text("\n".join(lineas) + "\n", encoding="utf8")


if __name__ == "__main__":
    e = dotenv_values(ENV)
    corto = e.get("IG_TOKEN_USUARIO")
    if not corto:
        sys.exit("Falta IG_TOKEN_USUARIO en .env.local (ver los pasos al principio de este fichero).")
    largo = get("oauth/access_token", grant_type="fb_exchange_token", client_id=e["META_APP_ID"],
                client_secret=e["META_APP_SECRET"], fb_exchange_token=corto)["access_token"]
    paginas = get("me/accounts", fields="id,name,access_token,instagram_business_account", access_token=largo)["data"]
    pagina = next((p for p in paginas if (p.get("instagram_business_account") or {}).get("id") == e["IG_USER_ID"]), None)
    if not pagina:
        sys.exit("Ninguna página de este usuario tiene enlazada la cuenta de Instagram " + e["IG_USER_ID"] +
                 ". Páginas vistas: " + ", ".join(p["name"] for p in paginas))
    yo = get(e["IG_USER_ID"], fields="username", access_token=pagina["access_token"])
    guardar("IG_TOKEN", pagina["access_token"], quitar=("IG_TOKEN_USUARIO",))
    print(f"Listo: token de la página «{pagina['name']}» guardado en .env.local; ve a @{yo['username']}.")
