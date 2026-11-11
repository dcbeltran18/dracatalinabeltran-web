#!/usr/bin/env python3
"""Genera el sitio estático de dracatalinabeltran.com.

Uso (desde la raíz del repo):  python3 _src/build.py
- Contenido en _src/content_es.py y _src/content_en.py (lista PAGES).
- Este archivo arma el HTML común, los datos estructurados, sitemap y robots.
Reglas del plan SEO: respuesta primero, una pregunta por H2, autoría visible,
fecha de actualización, migas de pan, enlaces internos, schema conectado por @id.
"""
import json, os, re, sys, html
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from common import *  # noqa
import content_es, content_en

def wa_link(msg):
    return f"https://wa.me/{WA}?text={quote(msg)}"

def strip(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()

def schema_graph(p):
    es = p["lang"] == "es"
    url = DOMAIN + p["path"]
    g = [
        {"@type": "WebSite", "@id": DOMAIN + "/#website", "url": DOMAIN + "/", "name": "Dra. Catalina Beltrán",
         "inLanguage": ["es", "en"], "publisher": {"@id": ID_DENTIST}},
        DENTIST_SCHEMA, PERSON_SCHEMA,
    ]
    page = {"@type": p.get("schema_type", "WebPage"), "@id": url + "#webpage", "url": url, "name": p["title"],
            "description": p["desc"], "inLanguage": p["lang"], "isPartOf": {"@id": DOMAIN + "/#website"},
            "about": {"@id": ID_DENTIST}, "dateModified": p.get("updated", UPDATED)}
    if p.get("byline", True):
        page["author"] = {"@id": ID_PERSON}
        page["reviewedBy"] = {"@id": ID_PERSON}
        page["lastReviewed"] = p.get("updated", UPDATED)
    if p.get("image"):
        page["primaryImageOfPage"] = DOMAIN + p["image"]
    crumbs = [("Inicio" if es else "Veneers in Medellín", HOME_ES if es else HOME_EN)] + p.get("parents", []) + [(p["crumb"], p["path"])] if p.get("crumb") else None
    if crumbs:
        page["breadcrumb"] = {"@id": url + "#breadcrumb"}
        g.append({"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": DOMAIN + u} for i, (n, u) in enumerate(crumbs)]})
    g.append(page)
    if p.get("faqs"):
        g.append({"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in p["faqs"]]})
    return {"@context": "https://schema.org", "@graph": g}

def crumbs_html(p):
    if not p.get("crumb"):
        return ""
    es = p["lang"] == "es"
    items = [("Inicio" if es else "Veneers in Medellín", HOME_ES if es else HOME_EN)] + p.get("parents", [])
    links = " › ".join(f'<a href="{u}">{n}</a>' for n, u in items)
    return f'<nav class="crumbs" aria-label="breadcrumb">{links} › <span>{p["crumb"]}</span></nav>'

def byline_html(p):
    if not p.get("byline", True):
        return ""
    es = p["lang"] == "es"
    d = p.get("updated", UPDATED)
    if es:
        return (f'<p class="byline"><img src="/img/dra-catalina-480.webp" width="40" height="40" alt="" loading="lazy">'
                f'<span>Escrito y revisado por <a href="/dra-catalina-beltran/">Dra. Catalina Beltrán</a>, odontóloga estética, RETHUS desde 2011 · '
                f'Actualizado el <time datetime="{d}">{fecha_es(d)}</time></span></p>')
    return (f'<p class="byline"><img src="/img/dra-catalina-480.webp" width="40" height="40" alt="" loading="lazy">'
            f'<span>Written and reviewed by <a href="/en/dr-catalina-beltran/">Dr. Catalina Beltrán</a>, cosmetic dentist, licensed in Colombia since 2011 · '
            f'Updated <time datetime="{d}">{fecha_en(d)}</time></span></p>')

def faq_html(faqs, es):
    if not faqs:
        return ""
    h = "Preguntas frecuentes" if es else "Frequently asked questions"
    return f'<section><h2>{h}</h2>' + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs) + "</section>"

def related_html(rel, es):
    if not rel:
        return ""
    h = "Sigue leyendo" if es else "Keep reading"
    return f'<section><h2>{h}</h2><div class="related">' + "".join(f'<a href="{u}">{n}</a>' for n, u in rel) + "</div></section>"

def layout(p):
    es = p["lang"] == "es"
    wa = wa_link(p["wa"])
    alt = ""
    if p.get("alt"):
        es_url, en_url = (p["path"], p["alt"]) if es else (p["alt"], p["path"])
        alt = (f'<link rel="alternate" hreflang="es" href="{DOMAIN}{es_url}"><link rel="alternate" hreflang="en" href="{DOMAIN}{en_url}">'
               f'<link rel="alternate" hreflang="x-default" href="{DOMAIN}{es_url}">')
    robots = '<meta name="robots" content="noindex">' if p.get("noindex") else '<meta name="robots" content="index,follow,max-image-preview:large">'
    ld = json.dumps(schema_graph(p), ensure_ascii=False)
    nav = (NAV_ES if es else NAV_EN).replace("{ALT}", p.get("alt") or (HOME_EN if es else HOME_ES))
    foot = (FOOTER_ES if es else FOOTER_EN).replace("{WA}", wa)
    body = p["body"].replace("{WA}", wa).replace("{WAICON}", WA_ICON)
    cta = (CTA_ES if es else CTA_EN).replace("{WA}", wa).replace("{WAICON}", WA_ICON)
    lead = f'<p class="lead">{p["lead"]}</p>' if p.get("lead") else ""
    first_cta = "" if p.get("no_top_cta") else cta
    return f"""<!doctype html>
<html lang="{p["lang"]}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{p["title"]}</title><meta name="description" content="{p["desc"]}">{robots}
<link rel="canonical" href="{DOMAIN}{p["path"]}">{alt}
<meta property="og:title" content="{p["title"]}"><meta property="og:description" content="{p["desc"]}">
<meta property="og:image" content="{DOMAIN}/img/og.jpg"><meta property="og:url" content="{DOMAIN}{p["path"]}"><meta property="og:type" content="website">
<meta property="og:locale" content="{"es_CO" if es else "en_US"}"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico"><link rel="apple-touch-icon" href="/icon-180.png">
<link rel="preload" href="/fonts/jost-300.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/style.css">
<script type="application/ld+json">{ld}</script>
</head><body>
<a class="skip" href="#main">{"Saltar al contenido" if es else "Skip to content"}</a>
<header><div class="wrap"><a class="brand" href="{HOME_ES if es else HOME_EN}">Dra. Catalina Beltrán<small>{"Odontología estética · Medellín" if es else "Cosmetic dentistry · Medellín"}</small></a>
<nav aria-label="{"Principal" if es else "Main"}">{nav}</nav></div></header>
<main id="main" class="wrap"><article>{crumbs_html(p)}
<h1>{p["h1"]}</h1>{lead}{byline_html(p)}{first_cta}
{body}
{faq_html(p.get("faqs"), es)}
{related_html(p.get("related"), es)}
<section class="final">{cta}</section>
</article></main>
<footer><div class="wrap">{foot}</div></footer>
<a class="float" href="{wa}" aria-label="WhatsApp">{WA_ICON}<span>WhatsApp</span></a>
<script src="/site.js" defer></script>
</body></html>"""

def main():
    pages = content_es.PAGES + content_en.PAGES
    paths = {p["path"] for p in pages}
    with open(os.path.join(ROOT, "style.css"), "w", encoding="utf-8") as f:
        f.write(CSS.strip() + "\n")
    errors = []
    for p in pages:
        out = layout(p)
        # control de enlaces internos rotos
        for href in re.findall(r'href="(/[^"#?]*)"', out):
            if href.endswith("/") and href not in paths:
                errors.append(f"{p['path']} -> {href}")
        d = os.path.join(ROOT, p["path"].strip("/"))
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
            f.write(out)
    # enlaces entrantes por página (sin contar menú/pie)
    inbound = {p["path"]: 0 for p in pages}
    for p in pages:
        found = set(re.findall(r'href="(/[^"#?]*)"', p["body"] + "".join(a for _, a in p.get("faqs", []) or []))) | {u for _, u in p.get("related", []) or []}
        for href in found:
            if href in inbound and href != p["path"]:
                inbound[href] += 1
    sm = []
    for p in pages:
        if p.get("noindex"):
            continue
        sm.append(f'<url><loc>{DOMAIN}{p["path"]}</loc><lastmod>{p.get("updated", UPDATED)}</lastmod></url>')
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(sm) + "\n</urlset>\n")
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("User-agent: *\nAllow: /\nDisallow: /_src/\n\n"
                "User-agent: Googlebot\nAllow: /\n\nUser-agent: Bingbot\nAllow: /\n\n"
                "User-agent: OAI-SearchBot\nAllow: /\n\nUser-agent: PerplexityBot\nAllow: /\n\n"
                f"Sitemap: {DOMAIN}/sitemap.xml\n")
    nf = dict(path="/404.html", lang="es", title="Página no encontrada | Dra. Catalina Beltrán", desc="Página no encontrada.",
              h1="Esta página no existe", byline=False, noindex=True, no_top_cta=True,
              wa="Hola Dra. Catalina 👋 Vi su página web y quiero saber el precio de mi diseño de sonrisa.",
              body='<p><a href="/">Volver al inicio</a> · <a href="/diseno-de-sonrisa-medellin/">Diseño de sonrisa en Medellín</a> · <a href="/precio-diseno-de-sonrisa-colombia/">Precios</a></p>')
    with open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8") as f:
        f.write(layout(nf))
    print(f"OK: {len(pages)} páginas")
    for path, n in sorted(inbound.items(), key=lambda x: x[1]):
        print(f"  {n:2d} enlaces entrantes  {path}")
    if errors:
        print("ENLACES ROTOS:\n  " + "\n  ".join(sorted(set(errors))))
        sys.exit(1)

if __name__ == "__main__":
    main()
