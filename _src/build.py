#!/usr/bin/env python3
"""Genera el sitio estático de dracatalinabeltran.com.
Uso: python3 _src/build.py   (desde la raíz del repo)
Cada página se define en PAGES; el HTML común está en layout()."""
import json, os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://dracatalinabeltran.com"
WA = "573203118517"
ADDRESS = "Cra. 25 #12 Sur 59, El Poblado, Medellín"
TODAY = "2026-11-10"

def wa_link(msg):
    from urllib.parse import quote
    return f"https://wa.me/{WA}?text={quote(msg)}"

CSS = """
:root{--ink:#0b0a09;--ink2:#15130f;--line:#2b271f;--text:#efe9df;--muted:#b9b0a2;--gold:#c9a96e;--wa:#25d366;--wa-ink:#062b14;
--display:"Tenor Sans","Optima",sans-serif;--body:"Jost",system-ui,-apple-system,"Segoe UI",sans-serif}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--ink);color:var(--text);font:300 18px/1.65 var(--body)}
a{color:var(--gold)}img{max-width:100%;height:auto;display:block}
.wrap{max-width:860px;margin:0 auto;padding:0 20px}
header{border-bottom:1px solid var(--line);position:sticky;top:0;background:rgba(11,10,9,.94);backdrop-filter:blur(8px);z-index:5}
header .wrap{display:flex;align-items:center;justify-content:space-between;gap:12px;min-height:60px}
.brand{font-family:var(--display);color:var(--text);text-decoration:none;font-size:19px;letter-spacing:.02em}
.brand small{display:block;font:400 11px/1.2 var(--body);color:var(--muted);letter-spacing:.12em;text-transform:uppercase}
nav a{color:var(--muted);text-decoration:none;font-size:14px;margin-left:14px}nav a:hover{color:var(--text)}
@media(max-width:640px){nav .hide-m{display:none}}
h1,h2,h3{font-family:var(--display);font-weight:400;line-height:1.2;color:#fff}
h1{font-size:clamp(30px,6vw,46px);margin:44px 0 14px}h2{font-size:clamp(24px,4.5vw,32px);margin:48px 0 12px}h3{font-size:21px;margin:28px 0 6px}
.lead{font-size:20px;color:var(--text)}
.muted{color:var(--muted);font-size:15px}
.btn{display:inline-flex;align-items:center;gap:10px;background:var(--wa);color:var(--wa-ink);font-weight:500;text-decoration:none;padding:14px 22px;border-radius:999px;font-size:17px}
.btn.ghost{background:transparent;color:var(--gold);border:1px solid var(--gold)}
.ctas{display:flex;flex-wrap:wrap;gap:12px;margin:22px 0}
table{width:100%;border-collapse:collapse;margin:16px 0;font-size:16px}
th,td{text-align:left;padding:11px 10px;border-bottom:1px solid var(--line);vertical-align:top}th{color:var(--gold);font-weight:500}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin:18px 0}
.card{background:var(--ink2);border:1px solid var(--line);border-radius:14px;padding:18px}
.card b{display:block;font-family:var(--display);font-weight:400;font-size:28px;color:var(--gold)}
.ba{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:14px 0}.ba figure{margin:0}.ba figcaption{font-size:13px;color:var(--muted);text-align:center;padding-top:4px}
.doc{display:grid;grid-template-columns:200px 1fr;gap:22px;align-items:start}.doc img{border-radius:14px}
@media(max-width:640px){.doc{grid-template-columns:1fr}.doc img{max-width:240px}}
details{border-bottom:1px solid var(--line);padding:12px 0}summary{cursor:pointer;font-weight:500;color:#fff}details p{margin:8px 0 0}
.crumbs{font-size:13px;color:var(--muted);margin-top:18px}.crumbs a{color:var(--muted)}
footer{border-top:1px solid var(--line);margin-top:64px;padding:28px 0 90px;font-size:15px;color:var(--muted)}
footer a{color:var(--muted)}
.float{position:fixed;right:16px;bottom:16px;z-index:9;background:var(--wa);color:var(--wa-ink);border-radius:999px;padding:13px 18px;font-weight:500;text-decoration:none;box-shadow:0 8px 24px rgba(0,0,0,.4)}
.related{display:flex;flex-wrap:wrap;gap:10px;margin:14px 0}.related a{border:1px solid var(--line);border-radius:999px;padding:8px 14px;text-decoration:none;font-size:15px}
"""

WA_ICON = '<svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2c-1.5 0-3-.4-4.3-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.6.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.8 11.9 11.9 0 0 0 4.6 4c1.7.7 2.4.8 3.2.7a2.8 2.8 0 0 0 1.8-1.3 2.3 2.3 0 0 0 .2-1.3c-.1-.1-.3-.2-.5-.3Z"/></svg>'

def dentist_schema():
    return {
        "@context": "https://schema.org", "@type": "Dentist",
        "name": "Dra. Catalina Beltrán - Diseño de Sonrisa en Medellín",
        "url": DOMAIN + "/", "image": DOMAIN + "/img/dra-catalina-900.webp",
        "telephone": "+57 320 311 8517",
        "address": {"@type": "PostalAddress", "streetAddress": "Cra. 25 #12 Sur 59", "addressLocality": "Medellín",
                    "addressRegion": "Antioquia", "addressCountry": "CO"},
        "areaServed": ["Medellín", "Bogotá", "Colombia"],
        "priceRange": "USD 145 – USD 5.900",
        "sameAs": ["https://www.instagram.com/dracatalinabeltran/"],
    }

def faq_schema(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": html.unescape(_strip(a))}} for q, a in faqs]}

def _strip(s):
    import re
    return re.sub(r"<[^>]+>", "", s)

def faq_html(faqs):
    return "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

def layout(p):
    lang = p["lang"]
    es = lang == "es"
    alt = ""
    if p.get("alt"):
        other = "en" if es else "es"
        alt = (f'<link rel="alternate" hreflang="{lang}" href="{DOMAIN}{p["path"]}">'
               f'<link rel="alternate" hreflang="{other}" href="{DOMAIN}{p["alt"]}">')
    schemas = [dentist_schema()]
    if p.get("faqs"):
        schemas.append(faq_schema(p["faqs"]))
    if p.get("crumb"):
        schemas.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio" if es else "Home", "item": DOMAIN + ("/" if es else "/en/veneers-medellin/")},
            {"@type": "ListItem", "position": 2, "name": p["crumb"], "item": DOMAIN + p["path"]}]})
    ld = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schemas)
    wa = wa_link(p["wa"])
    if es:
        nav = ('<a href="/diseno-de-sonrisa-medellin/" class="hide-m">Medellín</a>'
               '<a href="/precio-diseno-de-sonrisa-colombia/">Precios</a><a href="/en/veneers-medellin/">EN</a>')
        foot = (f'<p><b>Dra. Catalina Beltrán</b> · Odontología estética · {ADDRESS}. También atiende en Bogotá.<br>'
                f'WhatsApp <a href="{wa}">+57 320 311 8517</a> · <a href="https://www.instagram.com/dracatalinabeltran/">Instagram</a></p>'
                '<p><a href="/">Inicio</a> · <a href="/diseno-de-sonrisa-medellin/">Diseño de sonrisa Medellín</a> · '
                '<a href="/precio-diseno-de-sonrisa-colombia/">Precio diseño de sonrisa Colombia</a> · '
                '<a href="/en/veneers-medellin/">Veneers in Medellín (English)</a> · '
                '<a href="https://valoracion.dracatalinabeltran.com/privacidad.html">Privacidad</a></p>'
                '<p class="muted">Los precios publicados son de referencia. El precio exacto lo confirma la doctora tras revisar tu caso. '
                'La información de este sitio no reemplaza una valoración odontológica.</p>')
        float_t = "WhatsApp"
    else:
        nav = ('<a href="/en/veneers-medellin/" class="hide-m">Veneers</a>'
               '<a href="/en/cost-of-veneers-colombia/">Prices</a><a href="/">ES</a>')
        foot = (f'<p><b>Dr. Catalina Beltrán</b> · Cosmetic dentistry · {ADDRESS}, Colombia. Also sees patients in Bogotá.<br>'
                f'WhatsApp <a href="{wa}">+57 320 311 8517</a> · <a href="https://www.instagram.com/dracatalinabeltran/">Instagram</a></p>'
                '<p><a href="/en/veneers-medellin/">Veneers in Medellín</a> · <a href="/en/cost-of-veneers-colombia/">Cost of veneers in Colombia</a> · '
                '<a href="/">Español</a></p>'
                '<p class="muted">Published prices are reference prices. Your exact price is confirmed by the doctor after reviewing your case. '
                'This site does not replace a dental assessment.</p>')
        float_t = "WhatsApp"
    crumbs = ""
    if p.get("crumb"):
        crumbs = f'<div class="crumbs"><a href="{"/" if es else "/en/veneers-medellin/"}">{"Inicio" if es else "Home"}</a> › {p["crumb"]}</div>'
    return f"""<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{p["title"]}</title><meta name="description" content="{p["desc"]}">
<link rel="canonical" href="{DOMAIN}{p["path"]}">{alt}
<meta property="og:title" content="{p["title"]}"><meta property="og:description" content="{p["desc"]}">
<meta property="og:image" content="{DOMAIN}/img/og.jpg"><meta property="og:url" content="{DOMAIN}{p["path"]}"><meta property="og:type" content="website">
<link rel="icon" href="/favicon.ico"><link rel="apple-touch-icon" href="/icon-180.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Tenor+Sans&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css">{ld}
</head><body>
<header><div class="wrap"><a class="brand" href="{"/" if es else "/en/veneers-medellin/"}">Dra. Catalina Beltrán<small>{"Odontología estética" if es else "Cosmetic dentistry"}</small></a><nav>{nav}</nav></div></header>
<main class="wrap">{crumbs}{p["body"].replace("{WA}", wa).replace("{WAICON}", WA_ICON)}</main>
<footer><div class="wrap">{foot}</div></footer>
<a class="float" href="{wa}" aria-label="WhatsApp">{float_t}</a>
</body></html>"""

# ---------- contenido compartido ----------
DOCTOR_ES = """<div class="doc"><img src="/img/dra-catalina-480.webp" width="480" height="640" alt="Dra. Catalina Beltrán, odontóloga estética en Medellín" loading="lazy">
<div><h3>Dra. Catalina Beltrán</h3><p>Odontóloga con 15 años de experiencia, registrada en el RETHUS desde 2011. Especialista en Estética Dental (Federación Odontológica Colombiana), odontóloga con énfasis en ciencias quirúrgicas (Colegio Odontológico Colombiano) y especialista en Auditoría y Garantía de Calidad en Salud (Universidad EAN).</p>
<p>Revisa personalmente tus fotos, diseña tu sonrisa y te atiende en su consultorio de El Poblado. Calificación de 5,0 en Google.</p></div></div>"""

DOCTOR_EN = """<div class="doc"><img src="/img/dra-catalina-480.webp" width="480" height="640" alt="Dr. Catalina Beltrán, cosmetic dentist in Medellín" loading="lazy">
<div><h3>Dr. Catalina Beltrán</h3><p>A dentist with 15 years of experience, licensed in Colombia's national health registry (RETHUS) since 2011. Specialist in Cosmetic Dentistry (Federación Odontológica Colombiana) and dentist with an emphasis in surgical sciences (Colegio Odontológico Colombiano).</p>
<p>She reviews your photos herself, designs your smile and treats you personally at her office in El Poblado, Medellín. Rated 5.0 on Google.</p></div></div>"""

BA_ES = """<div class="ba"><figure><img src="/img/caso1-antes-600.webp" width="600" height="367" alt="Antes del diseño de sonrisa" loading="lazy"><figcaption>Antes</figcaption></figure>
<figure><img src="/img/caso1-despues-600.webp" width="600" height="367" alt="Después del diseño de sonrisa con carillas" loading="lazy"><figcaption>Después</figcaption></figure></div>"""
BA_EN = BA_ES.replace("Antes del diseño de sonrisa", "Before smile design").replace("Después del diseño de sonrisa con carillas", "After smile design with veneers").replace(">Antes<", ">Before<").replace(">Después<", ">After<")

PRICE_TABLE_ES = """<table><tr><th>Tratamiento</th><th>Precio de referencia</th></tr>
<tr><td>Carilla de porcelana E-max (por diente)</td><td>USD 380</td></tr>
<tr><td>Carilla de resina (por diente)</td><td>USD 145</td></tr>
<tr><td>10 carillas de porcelana E-max (sonrisa superior)</td><td>USD 3.800</td></tr>
<tr><td>Sonrisa completa: 20 carillas de porcelana E-max</td><td>USD 5.900 (USD 295 por diente)</td></tr></table>"""

PRICE_TABLE_EN = """<table><tr><th>Treatment</th><th>Reference price</th></tr>
<tr><td>E-max porcelain veneer (per tooth)</td><td>USD 380</td></tr>
<tr><td>Composite veneer (per tooth)</td><td>USD 145</td></tr>
<tr><td>10 E-max porcelain veneers (upper smile)</td><td>USD 3,800</td></tr>
<tr><td>Full smile: 20 E-max porcelain veneers</td><td>USD 5,900 (USD 295 per tooth)</td></tr></table>"""

CTA_ES = '<div class="ctas"><a class="btn" href="{WA}">{WAICON} Pregúntale tu precio a la doctora</a></div><p class="muted">Valoración gratis por WhatsApp · respuesta el mismo día · sin compromiso</p>'
CTA_EN = '<div class="ctas"><a class="btn" href="{WA}">{WAICON} Ask the doctor for your price</a></div><p class="muted">Free assessment on WhatsApp · same-day reply · no commitment</p>'

# ---------- páginas ----------
PAGES = []

PAGES.append(dict(path="/", lang="es", alt="/en/veneers-medellin/",
    title="Dra. Catalina Beltrán | Diseño de sonrisa en Medellín y Bogotá",
    desc="Odontóloga estética con 15 años de experiencia. Diseño de sonrisa y carillas sin desgaste dental en El Poblado, Medellín. Precios en dólares y valoración gratis por WhatsApp.",
    wa="Hola Dra. Catalina 👋 Vi su página web y quiero saber el precio de mi diseño de sonrisa.",
    body=f"""<h1>Diseño de sonrisa en Medellín con la Dra. Catalina Beltrán</h1>
<p class="lead">Carillas sin desgaste dental en El Poblado, Medellín, con precio cerrado antes de empezar. La doctora también atiende en Bogotá.</p>
{CTA_ES}
<div class="cards"><div class="card"><b>5,0</b>Calificación en Google</div><div class="card"><b>15 años</b>de experiencia</div><div class="card"><b>USD 295</b>por diente en sonrisa completa de porcelana</div></div>
<h2>Cómo funciona</h2>
<ol><li><b>Escríbele por WhatsApp.</b> Cuéntale qué te gustaría cambiar. Para un precio exacto le envías 3 fotos con tu celular; no necesitas radiografías.</li>
<li><b>Recibe tu valoración.</b> La doctora te dice qué opción te conviene, cuántos dientes tratar y el precio cerrado. Si prefieres, por videollamada.</li>
<li><b>Haz tu tratamiento.</b> La doctora planifica tu diseño antes de empezar. Si vienes de otro país, viajas una sola vez, mínimo 4 días.</li></ol>
<h2>Resultados reales</h2>{BA_ES}
<p>Cada sonrisa se diseña según la cara, el tono de piel y la mordida de cada paciente.</p>
<h2>Precios de referencia</h2>{PRICE_TABLE_ES}
<p><a href="/precio-diseno-de-sonrisa-colombia/">Ver qué incluye cada precio y cómo se compara</a></p>
<h2>Tu odontóloga</h2>{DOCTOR_ES}
<h2>Más información</h2><div class="related"><a href="/diseno-de-sonrisa-medellin/">Diseño de sonrisa en Medellín</a><a href="/precio-diseno-de-sonrisa-colombia/">¿Cuánto cuesta un diseño de sonrisa en Colombia?</a><a href="/en/veneers-medellin/">Veneers in Medellín (English)</a></div>
{CTA_ES}"""))

MED_FAQS = [
    ("¿Cuánto cuesta un diseño de sonrisa en Medellín?",
     "Con la Dra. Catalina, la carilla de porcelana E-max cuesta USD 380 por diente y la de resina USD 145 por diente. La sonrisa completa de 20 carillas de porcelana E-max cuesta USD 5.900. Son precios de referencia: el precio exacto depende de cuántos dientes necesitas y la doctora te lo confirma gratis por WhatsApp."),
    ("¿Qué es mejor, diseño de sonrisa o microdiseño?",
     "Depende de cuánto quieras cambiar. Un microdiseño corrige detalles en pocos dientes; un diseño de sonrisa completo cambia forma, tamaño y color de toda la zona visible. La doctora te dice cuál te conviene después de ver tus fotos."),
    ("¿Las carillas desgastan los dientes?",
     "La Dra. Catalina trabaja carillas sin desgaste dental. Si tu caso necesitara algo distinto, te lo explica en la valoración antes de empezar."),
    ("¿Dónde queda el consultorio?",
     f"En {ADDRESS}. La doctora también atiende en Bogotá."),
    ("¿Cuánto tiempo necesito si vengo de otro país?",
     "Un solo viaje de mínimo 4 días. Antes de comprar el vuelo ya sabes el precio cerrado de tu tratamiento."),
]
PAGES.append(dict(path="/diseno-de-sonrisa-medellin/", lang="es", alt="/en/veneers-medellin/", crumb="Diseño de sonrisa en Medellín",
    title="Diseño de sonrisa en Medellín | Carillas sin desgaste en El Poblado",
    desc="Diseño de sonrisa en Medellín con la Dra. Catalina Beltrán: carillas de porcelana E-max y resina sin desgaste dental en El Poblado. Precio cerrado y valoración gratis.",
    wa="Hola Dra. Catalina 👋 Vi su página web (diseño de sonrisa Medellín) y quiero saber el precio de mi caso.",
    faqs=MED_FAQS,
    body=f"""<h1>Diseño de sonrisa en Medellín</h1>
<p class="lead">La Dra. Catalina Beltrán hace diseños de sonrisa con carillas de porcelana E-max y de resina, sin desgaste dental, en su consultorio de El Poblado.</p>
{CTA_ES}
<h2>Tipos de diseño de sonrisa</h2>
<h3>Carillas de porcelana E-max (cerámica)</h3><p>Es la opción más estética y duradera. La porcelana E-max (disilicato de litio) refleja la luz como un diente natural y no se mancha. Precio de referencia: USD 380 por diente.</p>
<h3>Carillas de resina</h3><p>Es la opción más económica. Se trabaja directamente en el consultorio. Precio de referencia: USD 145 por diente.</p>
<h3>Microdiseño de sonrisa</h3><p>Corrige detalles en pocos dientes: un borde, un espacio o el color de algunos dientes. Es una buena entrada si no quieres un cambio completo.</p>
<h2>Resultados</h2>{BA_ES}
<h2>Precios en Medellín</h2>{PRICE_TABLE_ES}
<p>Incluye valoración y diseño digital, limpieza previa y control por videollamada. <a href="/precio-diseno-de-sonrisa-colombia/">Ver el detalle de precios</a>.</p>
<h2>Por qué elegir a la Dra. Catalina</h2>
<ul><li>Precio cerrado antes de empezar, publicado en dólares.</li><li>Carillas sin desgaste dental.</li><li>Atención personal de la doctora, en español e inglés.</li><li>Consultorio en El Poblado, una de las zonas de Medellín con más hoteles y restaurantes.</li></ul>
{DOCTOR_ES}
<h2>Preguntas frecuentes</h2>{faq_html(MED_FAQS)}
<div class="related"><a href="/precio-diseno-de-sonrisa-colombia/">Precio del diseño de sonrisa en Colombia</a><a href="/">Inicio</a></div>
{CTA_ES}"""))

PRICE_FAQS = [
    ("¿Cuánto cuesta un diseño de sonrisa en Colombia?",
     "Depende del material y del número de dientes. Con la Dra. Catalina Beltrán en Medellín, la carilla de resina cuesta USD 145 por diente, la de porcelana E-max USD 380 por diente, y la sonrisa completa de 20 carillas de porcelana USD 5.900."),
    ("¿Cuánto vale un diseño de sonrisa en dólares?",
     "Una sonrisa superior de 10 carillas de porcelana E-max cuesta USD 3.800 y la sonrisa completa de 20 carillas USD 5.900, que equivale a USD 295 por diente."),
    ("¿Qué es más barato, resina o porcelana?",
     "La resina es más barata (USD 145 por diente frente a USD 380 en porcelana E-max), pero la porcelana dura más y no se mancha. La doctora te ayuda a elegir según tu presupuesto y lo que esperas."),
    ("¿Qué incluye el precio?",
     "Valoración y diseño digital, carillas sin desgaste dental, limpieza previa y control por videollamada. No incluye vuelos ni hotel."),
    ("¿Por qué es más barato que en Estados Unidos?",
     "En EE. UU. se publican rangos de USD 1.000 a 2.500 por carilla de porcelana. En Medellín el costo de operación es menor, con el mismo material E-max."),
]
PAGES.append(dict(path="/precio-diseno-de-sonrisa-colombia/", lang="es", alt="/en/cost-of-veneers-colombia/", crumb="Precio del diseño de sonrisa en Colombia",
    title="¿Cuánto cuesta un diseño de sonrisa en Colombia? Precios 2026",
    desc="Precios reales de diseño de sonrisa en Colombia: carilla de porcelana E-max USD 380, resina USD 145, sonrisa completa de 20 carillas USD 5.900. Qué incluye y cómo se compara.",
    wa="Hola Dra. Catalina 👋 Vi su página web (precios) y quiero saber el precio exacto de mi caso.",
    faqs=PRICE_FAQS,
    body=f"""<h1>¿Cuánto cuesta un diseño de sonrisa en Colombia?</h1>
<p class="lead">Con la Dra. Catalina Beltrán, en Medellín, una sonrisa completa de 20 carillas de porcelana E-max cuesta USD 5.900: USD 295 por diente, con precio cerrado antes de empezar.</p>
{CTA_ES}
<h2>Precios de referencia 2026</h2>{PRICE_TABLE_ES}
<p class="muted">Precios actualizados al {TODAY[8:]}/{TODAY[5:7]}/{TODAY[:4]}. Tu precio exacto depende de cuántos dientes necesitas: la doctora te lo confirma gratis por WhatsApp.</p>
<h2>Qué incluye</h2><ul><li>Valoración y diseño digital</li><li>Carillas sin desgaste dental</li><li>Limpieza previa</li><li>Control por videollamada</li></ul>
<p>No incluye vuelos ni hotel. Si vienes de otro país, recomendamos el Ibis Medellín, a 300 m del consultorio.</p>
<h2>Resina o porcelana: ¿cuál conviene?</h2>
<table><tr><th></th><th>Resina</th><th>Porcelana E-max</th></tr>
<tr><td>Precio por diente</td><td>USD 145</td><td>USD 380</td></tr>
<tr><td>Se mancha con el tiempo</td><td>Puede mancharse</td><td>No se mancha</td></tr>
<tr><td>Dónde se hace</td><td>Directo en el consultorio</td><td>En laboratorio, a la medida</td></tr></table>
<h2>Comparación con Estados Unidos</h2>
<table><tr><th>Tratamiento</th><th>EE. UU. (rango publicado)</th><th>Dra. Catalina, Medellín</th></tr>
<tr><td>Carilla de porcelana</td><td>USD 1.000–2.500</td><td>USD 380</td></tr>
<tr><td>Carilla de resina</td><td>USD 400–1.500</td><td>USD 145</td></tr>
<tr><td>10 carillas de porcelana</td><td>USD 10.000+</td><td>USD 3.800</td></tr></table>
<h2>Preguntas frecuentes</h2>{faq_html(PRICE_FAQS)}
<div class="related"><a href="/diseno-de-sonrisa-medellin/">Diseño de sonrisa en Medellín</a><a href="/">Inicio</a></div>
{CTA_ES}"""))

VEN_FAQS = [
    ("How much do veneers cost in Medellín?",
     "With Dr. Catalina Beltrán, an E-max porcelain veneer is USD 380 per tooth and a composite veneer USD 145 per tooth. A full smile of 20 E-max porcelain veneers is USD 5,900. These are reference prices; the doctor confirms your exact price for free on WhatsApp."),
    ("How many days do I need in Medellín?",
     "One trip of at least 4 days. You know your fixed price before you book your flight."),
    ("Does the doctor speak English?",
     "Yes. Dr. Catalina treats patients in English and Spanish, on WhatsApp and in person."),
    ("Do I need X-rays to get a quote?",
     "No. For an exact price you send 3 photos taken with your phone, and the doctor shows you how."),
    ("Where is the office?",
     f"At {ADDRESS}, Colombia, in El Poblado, one of the areas of Medellín with the most hotels and restaurants."),
]
PAGES.append(dict(path="/en/veneers-medellin/", lang="en", alt="/diseno-de-sonrisa-medellin/", crumb="Veneers in Medellín",
    title="Veneers in Medellín, Colombia | Dr. Catalina Beltrán, El Poblado",
    desc="Porcelain and composite veneers in Medellín with no tooth reduction. E-max veneers from USD 380 per tooth, full smile USD 5,900. Free assessment on WhatsApp, English spoken.",
    wa="Hi Dr. Catalina 👋 I saw your website and I'd like to know the price of my smile design.",
    faqs=VEN_FAQS,
    body=f"""<h1>Veneers in Medellín, Colombia</h1>
<p class="lead">Dr. Catalina Beltrán places E-max porcelain and composite veneers with no tooth reduction at her office in El Poblado, Medellín. Fixed price in US dollars before you travel.</p>
{CTA_EN}
<div class="cards"><div class="card"><b>USD 295</b>per tooth on a 20-veneer porcelain smile</div><div class="card"><b>4 days</b>one trip to Medellín</div><div class="card"><b>5.0</b>Google rating</div></div>
<h2>How it works</h2>
<ol><li><b>Message us on WhatsApp.</b> Tell us what you'd like to change. For an exact price, send 3 photos with your phone. No X-rays needed.</li>
<li><b>Get your assessment.</b> The doctor tells you which option fits, how many teeth to treat and your fixed price. By video call if you prefer.</li>
<li><b>Travel once and fly home smiling.</b> Your design is planned before any work starts. Plan at least 4 days in Medellín.</li></ol>
<h2>Real results</h2>{BA_EN}
<h2>Prices</h2>{PRICE_TABLE_EN}
<p>Included: assessment and digital design, no tooth reduction, cleaning beforehand and video follow-up at home. Not included: flights and hotel. <a href="/en/cost-of-veneers-colombia/">See full price details</a>.</p>
<h2>Your dentist</h2>{DOCTOR_EN}
<h2>Frequently asked questions</h2>{faq_html(VEN_FAQS)}
<div class="related"><a href="/en/cost-of-veneers-colombia/">Cost of veneers in Colombia</a><a href="/diseno-de-sonrisa-medellin/">Español</a></div>
{CTA_EN}"""))

COST_FAQS = [
    ("How much is 20 veneers in Colombia?",
     "With Dr. Catalina Beltrán in Medellín, a full smile of 20 E-max porcelain veneers is USD 5,900, about USD 295 per tooth. Bought one by one, 20 veneers would be USD 7,600."),
    ("Is it cheaper to get veneers in Colombia?",
     "Yes. Published US ranges are USD 1,000–2,500 per porcelain veneer; in Medellín with Dr. Catalina it is USD 380, using the same E-max material."),
    ("Can I get veneers for $5,000?",
     "Yes. 10 E-max porcelain veneers for the upper smile are USD 3,800. A full smile of 20 porcelain veneers is USD 5,900."),
    ("What is included in the price?",
     "Assessment and digital design, veneers with no tooth reduction, a cleaning beforehand and video follow-up once you are home. Flights and hotel are not included."),
    ("Composite or porcelain veneers?",
     "Composite veneers are cheaper (USD 145 per tooth) and done chairside. Porcelain E-max veneers (USD 380) last longer and do not stain. The doctor helps you choose."),
]
PAGES.append(dict(path="/en/cost-of-veneers-colombia/", lang="en", alt="/precio-diseno-de-sonrisa-colombia/", crumb="Cost of veneers in Colombia",
    title="Cost of Veneers in Colombia (2026): Real Prices in Medellín",
    desc="How much do veneers cost in Colombia? E-max porcelain USD 380 per tooth, composite USD 145, 20 veneers USD 5,900. What's included and how it compares with the US.",
    wa="Hi Dr. Catalina 👋 I saw your website (prices) and I'd like to know the exact price of my case.",
    faqs=COST_FAQS,
    body=f"""<h1>Cost of veneers in Colombia</h1>
<p class="lead">In Medellín, with Dr. Catalina Beltrán, a full smile of 20 E-max porcelain veneers costs USD 5,900, about USD 295 per tooth, with a fixed price before you travel.</p>
{CTA_EN}
<h2>2026 reference prices</h2>{PRICE_TABLE_EN}
<p class="muted">Prices as of {TODAY}. Your exact price depends on how many teeth you need; the doctor confirms it for free on WhatsApp.</p>
<h2>Colombia vs. the United States</h2>
<table><tr><th>Treatment</th><th>US (published range)</th><th>Dr. Catalina, Medellín</th></tr>
<tr><td>Porcelain veneer</td><td>USD 1,000–2,500</td><td>USD 380</td></tr>
<tr><td>Composite veneer</td><td>USD 400–1,500</td><td>USD 145</td></tr>
<tr><td>10 porcelain veneers</td><td>USD 10,000+</td><td>USD 3,800</td></tr></table>
<h2>What's included</h2><ul><li>Assessment and digital design</li><li>No tooth reduction</li><li>Cleaning beforehand</li><li>Video follow-up at home</li></ul>
<p>Not included: flights and hotel. We recommend the Ibis Medellín, 300 m from the office.</p>
<h2>Frequently asked questions</h2>{faq_html(COST_FAQS)}
<div class="related"><a href="/en/veneers-medellin/">Veneers in Medellín</a><a href="/precio-diseno-de-sonrisa-colombia/">Español</a></div>
{CTA_EN}"""))

def main():
    with open(os.path.join(ROOT, "style.css"), "w", encoding="utf-8") as f:
        f.write(CSS.strip() + "\n")
    urls = []
    for p in PAGES:
        d = os.path.join(ROOT, p["path"].strip("/"))
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
            f.write(layout(p))
        urls.append(p["path"])
    sm = "".join(f"<url><loc>{DOMAIN}{u}</loc><lastmod>{TODAY}</lastmod></url>" for u in urls)
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sm}</urlset>\n')
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\nDisallow: /_src/\nSitemap: {DOMAIN}/sitemap.xml\n")
    nf = dict(path="/404.html", lang="es", title="Página no encontrada | Dra. Catalina Beltrán", desc="Página no encontrada.",
              wa="Hola Dra. Catalina 👋 Vi su página web y quiero saber el precio de mi diseño de sonrisa.",
              body='<h1>Esta página no existe</h1><p><a href="/">Volver al inicio</a></p>' + CTA_ES)
    with open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8") as f:
        f.write(layout(nf).replace('<link rel="canonical"', '<meta name="robots" content="noindex"><link rel="canonical"'))
    print("OK:", ", ".join(urls))

if __name__ == "__main__":
    main()
