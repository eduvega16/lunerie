"""Monta el vídeo UGC del Collar Signé (5-nov): clips de Kling + voz en off (edge-tts, voz neuronal gratuita) + subtítulos
de la voz y tarjeta final. ffmpeg, sin créditos.
    python marca/ugc_montaje.py [Elvira|Ximena]   → marca/fotos-ia/ugc-collar/collar-ugc-<voz>-9x16.mp4
Orden de planos en PLANOS; subtítulos sacados del .srt de la voz (voz/voz-<voz>.srt).
"""
import pathlib, re, subprocess, sys, tempfile
from PIL import Image, ImageDraw, ImageFilter, ImageFont

RAIZ = pathlib.Path(__file__).resolve().parent.parent
CARPETA = RAIZ / "marca" / "fotos-ia" / "ugc-collar"
FUENTES = RAIZ / "marca" / "fuentes"
PLANOS = ["ancla-1", "nombre-1", "cuello-1", "mirada-1"]   # 4 s cada uno
SEG = 4.0
# altura del subtítulo según el plano que se ve (entre la barbilla y el nombre, sin tapar el collar; zona libre hasta 1248)
Y_PLANO = {"ancla": 960, "nombre": 860, "cuello": 760, "mirada": 860,
           "colgando": 1130, "palma": 330, "cierre": 960, "espejo": 1000}
VOZ = RAIZ / "marca" / "fotos-ia" / "ugc-collar" / "voz"
INICIO_VOZ = 0.2
W, H = 1080, 1920


def jost(tam, peso="Medium"):
    f = ImageFont.truetype(str(FUENTES / "Jost.ttf"), tam)
    try:
        f.set_variation_by_name(peso)
    except Exception:
        pass
    return f


def subtitulo(texto, destino):
    """Texto blanco con sombra suave, centrado, partido en líneas de ~26 caracteres."""
    f = jost(62, "SemiBold")
    palabras, lineas, actual = texto.split(), [], ""
    for p in palabras:
        if len(actual) + len(p) + 1 > 26 and actual:
            lineas.append(actual); actual = p
        else:
            actual = (actual + " " + p).strip()
    lineas.append(actual)
    im = Image.new("RGBA", (W, 90 * len(lineas) + 40), (0, 0, 0, 0))
    sombra = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ds, d = ImageDraw.Draw(sombra), ImageDraw.Draw(im)
    for i, l in enumerate(lineas):
        x = (W - d.textlength(l, font=f)) / 2
        ds.text((x, 20 + i * 90), l, font=f, fill=(0, 0, 0, 170))
        d.text((x, 20 + i * 90), l, font=f, fill=(255, 255, 255, 255))
    sombra = sombra.filter(ImageFilter.GaussianBlur(6))
    Image.alpha_composite(sombra, im).save(destino)


def tarjeta(destino):
    """Tarjeta final: panel niebla con el nombre de la pieza, precio y web."""
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    x0, y0, x1, y1 = 170, 880, 910, 1240
    d.rounded_rectangle((x0, y0, x1, y1), 36, fill=(249, 249, 249, 238))
    serif = ImageFont.truetype(str(FUENTES / "Cormorant.ttf"), 110)
    try:
        serif.set_variation_by_name("Regular")
    except Exception:
        pass
    tinta, oro = (22, 32, 27, 255), (166, 131, 74, 255)
    def centro(t, f, y, c):
        d.text(((W - d.textlength(t, font=f)) / 2, y), t, font=f, fill=c)
    centro("Collar Signé", serif, y0 + 30, tinta)
    centro("49,95 €", jost(56, "Regular"), y0 + 170, tinta)
    centro("DORADO · PLATEADO", jost(32, "Regular"), y0 + 250, oro)
    centro("lunerie.es", jost(40, "Medium"), y0 + 300, tinta)
    im.save(destino)


def trozos(subs, maximo=22):
    """Parte cada frase en trozos cortos de una línea (estilo UGC), repartiendo el tiempo por letras."""
    out = []
    for a, b, txt in subs:
        palabras, grupos, g = txt.split(), [], ""
        for p in palabras:
            if g and len(g) + len(p) + 1 > maximo:
                grupos.append(g); g = p
            else:
                g = (g + " " + p).strip()
        grupos.append(g)
        total, t = sum(len(x) for x in grupos), a
        for x in grupos:
            d = (b - a) * len(x) / total
            out.append((t, t + d, x)); t += d
    return out


def srt(ruta):
    t = ruta.read_text(encoding="utf8")
    seg = lambda s: (lambda h, m, x: int(h) * 3600 + int(m) * 60 + float(x.replace(",", ".")))(*s.split(":"))
    arregla = lambda x: ("¿" + x if x.endswith("?") and not x.startswith("¿") else x).replace("lunerie punto es", "lunerie.es")
    return [(seg(a), seg(b), arregla(txt.strip()))
            for a, b, txt in re.findall(r"(\S+) --> (\S+)\n(.+?)(?:\n\n|\Z)", t, re.S)]


def montar(voz):
    mp3, subs = VOZ / f"voz-{voz}.mp3", trozos(srt(VOZ / f"voz-{voz}.srt"))
    dur_voz = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                                    str(mp3)], capture_output=True, text=True).stdout)
    planos = [(x.split(":")[0], float(x.split(":")[1]) if ":" in x else SEG) for x in PLANOS]   # «plano:segundos»
    inicios = [sum(d for _, d in planos[:i]) for i in range(len(planos))]
    total = max(sum(d for _, d in planos), INICIO_VOZ + dur_voz + 0.8)
    extra = total - sum(d for _, d in planos)
    tmp = pathlib.Path(tempfile.mkdtemp())
    entradas, filtros = [], []
    for i, (p, dur) in enumerate(planos):
        entradas += ["-i", str(CARPETA / "clips" / f"{p}.mp4")]
        pad = f",tpad=stop_mode=clone:stop_duration={extra:.2f}" if i == len(planos) - 1 else ""
        filtros.append(f"[{i}:v]trim=0:{dur},setpts=PTS-STARTPTS,scale={W}:{H},fps=30,setsar=1{pad}[v{i}]")
    filtros.append("".join(f"[v{i}]" for i in range(len(PLANOS))) + f"concat=n={len(PLANOS)}:v=1:a=0[base]")
    n = len(PLANOS)
    entradas += ["-i", str(mp3)]
    ultimo, k = "base", n + 1
    t_card = total - 2.2
    subs = [(a, min(b, t_card - INICIO_VOZ), t) for a, b, t in subs if a + INICIO_VOZ < t_card]   # no asomar tras la tarjeta
    for j, (a, b, txt) in enumerate(subs):
        png = tmp / f"s{j}.png"; subtitulo(txt, png)
        entradas += ["-i", str(png)]
        visible = max(i for i, t0 in enumerate(inicios) if t0 <= a + INICIO_VOZ)
        y = Y_PLANO[planos[visible][0].rsplit("-", 1)[0]]
        filtros.append(f"[{ultimo}][{k}:v]overlay=0:{y}:enable='between(t,{a + INICIO_VOZ:.2f},{b + INICIO_VOZ:.2f})'[o{j}]")
        ultimo, k = f"o{j}", k + 1
    card = tmp / "tarjeta.png"; tarjeta(card)
    entradas += ["-loop", "1", "-t", f"{total:.2f}", "-i", str(card)]
    filtros.append(f"[{k}:v]format=rgba,fade=in:st={t_card:.2f}:d=0.4:alpha=1[card]")
    filtros.append(f"[{ultimo}][card]overlay=0:0[final]")
    filtros.append(f"[{n}:a]adelay={int(INICIO_VOZ * 1000)}|{int(INICIO_VOZ * 1000)},apad[aud]")
    salida = CARPETA / f"collar-ugc-{voz.lower()}-9x16.mp4"
    cmd = ["ffmpeg", "-v", "error", "-y", *entradas, "-filter_complex", ";".join(filtros), "-map", "[final]",
           "-map", "[aud]", "-t", f"{total:.2f}", "-c:v", "libx264", "-crf", "18", "-preset", "medium",
           "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(salida)]
    subprocess.run(cmd, check=True)
    print(salida, f"{total:.1f} s")


if __name__ == "__main__":
    a = sys.argv[1:]
    if "--carpeta" in a:
        CARPETA = RAIZ / "marca" / "fotos-ia" / a[a.index("--carpeta") + 1]
    if "--planos" in a:
        PLANOS = a[a.index("--planos") + 1].split(",")
    montar(a[0] if a and not a[0].startswith("--") else "sarah")
