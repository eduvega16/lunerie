"""Puente radar → oficina: saca de la base de datos del radar (05_producto_ganador) los anuncios de joyería y relojes
de la competencia y las tendencias de TikTok, y los deja en oficina/referencias/ para el estratega creativo.

    python oficina/radar_a_oficina.py [--db RUTA_A_productos.db] [--max 150]

- Solo LEE el radar (SQLite en modo solo lectura): no lo modifica, no lo ejecuta y no toca sus claves.
- Solo guarda anuncios públicos de la Biblioteca de anuncios de Meta (texto, titular, botón, formato, días activo,
  variantes y enlace a la propia biblioteca). No guarda URLs de vídeo ni de imagen de Meta (caducan).
- El radar se ejecuta aparte (uv run python cli.py pipeline --tiktok en 05_producto_ganador); aquí solo se lee lo último.
"""
import argparse, json, pathlib, re, sqlite3, sys
from datetime import datetime, timezone

RAIZ = pathlib.Path(__file__).resolve().parent
SALIDA = RAIZ / "referencias"
DB_DEFECTO = pathlib.Path(r"D:\aura-ai-portfolio\projects\05_producto_ganador\data\productos.db")
CLAVES = ("collar", "joya", "pendiente", "reloj", "pulsera", "anillo", "bisuter", "gargantilla", "colgante")
NO_TIENDA = ("reader", "novel", "drama", "pocketfm")   # apps de lectura que se cuelan en las búsquedas


def limpio(t):
    return re.sub(r"\s+", " ", (t or "").replace("\u200d", "")).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DB_DEFECTO))
    ap.add_argument("--max", type=int, default=150)
    a = ap.parse_args()
    ruta = pathlib.Path(a.db)
    if not ruta.exists():
        sys.exit(f"No encuentro la base del radar en {ruta}. Pasa la ruta con --db.")
    c = sqlite3.connect(f"file:{ruta.as_posix()}?mode=ro", uri=True)
    c.row_factory = sqlite3.Row
    q = lambda s, *p: [dict(r) for r in c.execute(s, p).fetchall()]

    texto = "lower(coalesce(texto,'') || ' ' || coalesce(titulo,''))"
    cond = " or ".join(f"{texto} like '%{k}%'" for k in CLAVES)
    filas = q(f"""SELECT id, anunciante, dominio, dias_activo, variantes, rank_cuenta, formato, cta, titulo, texto, inicio, visto_en
                  FROM ads WHERE fuente='meta' AND ({cond})
                  ORDER BY COALESCE(dias_activo,0) * COALESCE(variantes,1) DESC""")
    filas = [f for f in filas if not any(n in (f["dominio"] or "") for n in NO_TIENDA)]

    anuncios = []
    for f in filas[: a.max]:
        aid = f["id"].split(":")[-1]
        anuncios.append({
            "biblioteca": f"https://www.facebook.com/ads/library/?id={aid}",
            "anunciante": f["anunciante"], "dominio": f["dominio"], "dias_activo": f["dias_activo"],
            "variantes": f["variantes"], "puesto_en_su_cuenta": f["rank_cuenta"], "formato": f["formato"],
            "boton": f["cta"], "titulo": limpio(f["titulo"]), "texto": limpio(f["texto"]), "inicio": f["inicio"]})

    por_tienda = {}
    for f in filas:
        t = por_tienda.setdefault(f["dominio"], {"anunciante": f["anunciante"], "dominio": f["dominio"], "anuncios": 0,
                                                 "max_dias": 0, "formatos": {}})
        t["anuncios"] += 1
        t["max_dias"] = max(t["max_dias"], f["dias_activo"] or 0)
        t["formatos"][f["formato"]] = t["formatos"].get(f["formato"], 0) + 1
    tiendas = sorted(por_tienda.values(), key=lambda t: -t["anuncios"])[:25]

    ultima = max((f["visto_en"] or "" for f in filas), default="")
    meta = {"generado": datetime.now(timezone.utc).isoformat(timespec="seconds"), "datos_del_radar_de": ultima[:10],
            "anuncios_de_joyeria_y_relojes": len(filas), "tiendas": len(por_tienda), "origen": str(ruta)}
    SALIDA.mkdir(exist_ok=True)
    (SALIDA / "radar-joyeria.json").write_text(json.dumps(
        {"meta": meta, "aviso": "Anuncios de la competencia: sirven de inspiración de FORMA (estructura, formato, gancho). "
                                "Lunerie no copia textos ni usa su urgencia falsa, emojis ni contrareembolso.",
         "tiendas": tiendas, "anuncios": anuncios}, ensure_ascii=False, indent=1), encoding="utf-8")

    tend = q("""SELECT nombre, industria, crecimiento, publicaciones, vistas FROM tendencias
                WHERE crecimiento IS NOT NULL ORDER BY crecimiento DESC LIMIT 20""")
    (SALIDA / "radar-tendencias-tiktok.json").write_text(json.dumps(
        {"meta": meta, "tendencias": tend}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(anuncios)} anuncios de {len(por_tienda)} tiendas · {len(tend)} tendencias · datos del radar de {ultima[:10]}")


if __name__ == "__main__":
    main()
