"""Voz en off con ElevenLabs (5-nov; plan Free de Edu: API + licencia comercial de voz, 10.000 caracteres al mes).
La clave va en .env.local como ELEVENLABS_KEY=… (fuera de git; nunca en el chat). Nunca se imprime.
    python marca/voz_elevenlabs.py buscar [n]          → baja GRATIS las muestras de n voces femeninas de España a
                                                        marca/fotos-ia/ugc-collar/voz/muestras/ (escucharlas y elegir)
    python marca/voz_elevenlabs.py generar <voice_id> <nombre> [texto]
                                                     → voz/voz-<nombre>.mp3 + .srt (tiempos exactos por frase)
    luego: python marca/ugc_montaje.py <nombre>
Cada «generar» gasta ~1 crédito por carácter del texto (el guion son ~210).
"""
import base64, json, os, pathlib, re, sys, urllib.parse, urllib.request
from dotenv import load_dotenv

RAIZ = pathlib.Path(__file__).resolve().parent.parent
load_dotenv(RAIZ / ".env.local")
CLAVE = os.environ.get("ELEVENLABS_KEY", "")
API = "https://api.elevenlabs.io"
VOZ = RAIZ / "marca" / "fotos-ia" / "ugc-collar" / "voz"
GUION = ("¿No sabes qué regalarle? Mira esto. Lleva su nombre, escrito como una firma. Y una lágrima del color de su "
         "mes: esta azul es diciembre. En dorado o en plateado. Es el Collar Signé, y lo tienes en lunerie punto es.")


def pedir(ruta, datos=None):
    req = urllib.request.Request(API + ruta, data=json.dumps(datos).encode() if datos is not None else None,
                                 headers={"xi-api-key": CLAVE, "Content-Type": "application/json"},
                                 method="POST" if datos is not None else "GET")
    try:
        return json.load(urllib.request.urlopen(req, timeout=120))
    except urllib.error.HTTPError as e:
        sys.exit(f"ElevenLabs {e.code}: {e.read()[:400].decode(errors='ignore')}")


def limpio(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:40]


def buscar(n=8):
    q = urllib.parse.urlencode({"page_size": 40, "language": "es", "gender": "female", "sort": "usage_character_count_1y"})
    voces = pedir(f"/v1/shared-voices?{q}")["voices"]
    espana = [v for v in voces if "spain" in (v.get("accent") or "").lower() or (v.get("locale") or "").startswith("es-ES")]
    destino = VOZ / "muestras"; destino.mkdir(parents=True, exist_ok=True)
    elegidas = (espana or voces)[:n]
    for v in elegidas:
        nombre = limpio(v["name"])
        if v.get("preview_url"):
            urllib.request.urlretrieve(v["preview_url"], destino / f"{nombre}.mp3")
        print(f"{nombre:30} voice_id={v['voice_id']} owner={v['public_owner_id']} · {v.get('accent')} · "
              f"{v.get('age')} · {(v.get('description') or '')[:80]}")
    (destino / "voces.json").write_text(json.dumps(elegidas, ensure_ascii=False, indent=1), encoding="utf8")


def modelo():
    ms = [m for m in pedir("/v1/models") if m.get("can_do_text_to_speech")]
    for prefer in ("eleven_v4", "eleven_v3", "eleven_multilingual_v2"):
        for m in ms:
            if m["model_id"] == prefer:
                return prefer
    return ms[0]["model_id"]


def asegurar_voz(voice_id):
    """Las voces de la biblioteca pública hay que añadirlas a «Mis voces» antes de usarlas (el Free tiene 3 huecos)."""
    mias = {v["voice_id"] for v in pedir("/v1/voices")["voices"]}
    if voice_id in mias:
        return
    f = VOZ / "muestras" / "voces.json"
    info = next((v for v in json.loads(f.read_text(encoding="utf8")) if v["voice_id"] == voice_id), None) if f.exists() else None
    if not info:
        sys.exit("No encuentro esa voz en muestras/voces.json: ejecuta antes «buscar».")
    pedir(f"/v1/voices/add/{info['public_owner_id']}/{voice_id}", {"new_name": f"Lunerie · {info['name']}"[:50]})


def srt_desde(al, inicio=0.0):
    chars, ini, fin = al["characters"], al["character_start_times_seconds"], al["character_end_times_seconds"]
    frases, actual, t0 = [], "", None
    for c, a, b in zip(chars, ini, fin):
        if t0 is None and c.strip():
            t0 = a
        actual += c
        if c in ".?!":
            frases.append((t0, b, actual.strip())); actual, t0 = "", None
    if actual.strip():
        frases.append((t0, fin[-1], actual.strip()))
    ts = lambda s: f"{int(s // 3600):02d}:{int(s % 3600 // 60):02d}:{int(s % 60):02d},{int(round(s % 1 * 1000)):03d}"
    return "\n".join(f"{i}\n{ts(a)} --> {ts(b)}\n{t}\n" for i, (a, b, t) in enumerate(frases, 1))


def generar(voice_id, nombre, texto=GUION):
    asegurar_voz(voice_id)
    m = modelo()
    r = pedir(f"/v1/text-to-speech/{voice_id}/with-timestamps?output_format=mp3_44100_128",
              {"text": texto, "model_id": m, "language_code": "es",
               "voice_settings": {"stability": 0.45, "similarity_boost": 0.8, "style": 0.3, "use_speaker_boost": True}})
    VOZ.mkdir(parents=True, exist_ok=True)
    (VOZ / f"voz-{nombre}.mp3").write_bytes(base64.b64decode(r["audio_base64"]))
    (VOZ / f"voz-{nombre}.srt").write_text(srt_desde(r["alignment"]), encoding="utf8")
    print(f"voz-{nombre}.mp3 ({m}, {len(texto)} caracteres)")


DESCRIPCION = ("Mujer joven de unos 27 años de Madrid, España, con acento castellano peninsular. Voz cálida, natural y "
               "cercana, como una amiga grabando una story de Instagram con el móvil: tono relajado, sonriente y sin "
               "exagerar. Calidad de audio limpia, de micrófono de móvil cerca.")


def disenar(descripcion=DESCRIPCION, texto=GUION):
    """Voz propia diseñada por descripción (el plan Free no deja usar por API las voces de la biblioteca).
    Guarda 3 propuestas leyendo el guion en voz/diseno-<n>.mp3 con su generated_voice_id en diseno.json."""
    r = None
    for ruta, cuerpo in (("/v1/text-to-voice/design", {"voice_description": descripcion, "text": texto,
                                                         "model_id": "eleven_ttv_v3"}),
                         ("/v1/text-to-voice/create-previews", {"voice_description": descripcion, "text": texto})):
        try:
            req = urllib.request.Request(API + ruta, data=json.dumps(cuerpo).encode(), method="POST",
                                         headers={"xi-api-key": CLAVE, "Content-Type": "application/json"})
            r = json.load(urllib.request.urlopen(req, timeout=180)); break
        except urllib.error.HTTPError as e:
            print(ruta, e.code, e.read()[:300].decode(errors="ignore"))
    if not r:
        sys.exit("No se pudo diseñar la voz")
    VOZ.mkdir(parents=True, exist_ok=True)
    info = []
    for i, pv in enumerate(r["previews"], 1):
        audio = pv.get("audio_base_64") or pv.get("audio_base64")
        (VOZ / f"diseno-{i}.mp3").write_bytes(base64.b64decode(audio))
        info.append({"n": i, "generated_voice_id": pv["generated_voice_id"], "duracion": pv.get("duration_secs")})
        print(f"diseno-{i}.mp3  generated_voice_id={pv['generated_voice_id']}")
    (VOZ / "diseno.json").write_text(json.dumps({"descripcion": descripcion, "previews": info}, indent=1,
                                                ensure_ascii=False), encoding="utf8")


def guardar(n, nombre):
    """Guarda la propuesta n de disenar() como voz propia y devuelve su voice_id."""
    d = json.loads((VOZ / "diseno.json").read_text(encoding="utf8"))
    gid = next(p["generated_voice_id"] for p in d["previews"] if p["n"] == int(n))
    v = pedir("/v1/text-to-voice", {"voice_name": f"Lunerie {nombre}", "voice_description": d["descripcion"],
                                    "generated_voice_id": gid})
    print("voice_id", v["voice_id"])
    return v["voice_id"]


if __name__ == "__main__":
    if not CLAVE:
        sys.exit("Falta ELEVENLABS_KEY en .env.local")
    a = sys.argv[1:]
    if a and a[0] == "buscar":
        buscar(int(a[1]) if len(a) > 1 else 8)
    elif a and a[0] == "disenar":
        disenar()
    elif a and a[0] == "guardar" and len(a) >= 3:
        guardar(a[1], a[2])
    elif a and a[0] == "generar" and len(a) >= 3:
        generar(a[1], a[2], a[3] if len(a) > 3 else GUION)
    else:
        print(__doc__)
