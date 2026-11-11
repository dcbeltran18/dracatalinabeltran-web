"""Constantes, estilos y bloques compartidos del sitio. Solo datos confirmados."""

DOMAIN = "https://dracatalinabeltran.com"
WA = "573203118517"
PHONE = "+57 320 311 8517"
EMAIL = "dc.beltran18@gmail.com"
ADDRESS = "Cra. 25 #12 Sur 59, El Poblado, Medellín"
UPDATED = "2026-11-10"
HOME_ES = "/"
HOME_EN = "/en/veneers-medellin/"
INSTAGRAM = "https://www.instagram.com/dracatalinabeltran/"
FACEBOOK = "https://www.facebook.com/cirugia.plastica.125"
ID_DENTIST = DOMAIN + "/#consultorio-medellin"
ID_PERSON = DOMAIN + "/dra-catalina-beltran/#dra"

MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
def fecha_es(d): y, m, dd = d.split("-"); return f"{int(dd)} de {MESES[int(m)-1]} de {y}"
def fecha_en(d): y, m, dd = d.split("-"); return f"{MONTHS[int(m)-1]} {int(dd)}, {y}"

DENTIST_SCHEMA = {
    "@type": "Dentist", "@id": ID_DENTIST,
    "name": "Dra. Catalina Beltrán - Diseño de Sonrisa en Medellín",
    "url": DOMAIN + "/", "image": DOMAIN + "/img/og.jpg", "logo": DOMAIN + "/icon-180.png",
    "telephone": PHONE, "email": EMAIL,
    "address": {"@type": "PostalAddress", "streetAddress": "Cra. 25 #12 Sur 59", "addressLocality": "Medellín",
                "addressRegion": "Antioquia", "addressCountry": "CO"},
    "areaServed": {"@type": "City", "name": "Medellín"},
    "priceRange": "USD 145 – USD 5.900", "currenciesAccepted": "USD, COP",
    "knowsLanguage": ["es", "en"],
    "employee": {"@id": ID_PERSON}, "founder": {"@id": ID_PERSON},
    "sameAs": [INSTAGRAM, FACEBOOK],
    "makesOffer": [
        {"@type": "Offer", "name": "Carilla de porcelana E-max (por diente)", "price": "380", "priceCurrency": "USD"},
        {"@type": "Offer", "name": "Carilla de resina (por diente)", "price": "145", "priceCurrency": "USD"},
        {"@type": "Offer", "name": "10 carillas de porcelana E-max", "price": "3800", "priceCurrency": "USD"},
        {"@type": "Offer", "name": "Sonrisa completa: 20 carillas de porcelana E-max", "price": "5900", "priceCurrency": "USD"},
    ],
}
PERSON_SCHEMA = {
    "@type": "Person", "@id": ID_PERSON, "name": "Catalina Beltrán", "honorificPrefix": "Dra.",
    "jobTitle": "Odontóloga estética", "url": DOMAIN + "/dra-catalina-beltran/",
    "image": DOMAIN + "/img/dra-catalina-beltran-odontologa-estetica-medellin.webp", "worksFor": {"@id": ID_DENTIST},
    "knowsLanguage": ["es", "en"],
    "alumniOf": [{"@type": "Organization", "name": "Colegio Odontológico Colombiano"},
                 {"@type": "Organization", "name": "Federación Odontológica Colombiana"},
                 {"@type": "CollegeOrUniversity", "name": "Universidad EAN"}],
    "hasCredential": [{"@type": "EducationalOccupationalCredential", "credentialCategory": "Registro profesional",
                       "name": "Odontóloga registrada en el RETHUS (Colombia) desde 2011"},
                      {"@type": "EducationalOccupationalCredential", "credentialCategory": "Especialización",
                       "name": "Especialista en Estética Dental, Federación Odontológica Colombiana"}],
    "sameAs": [INSTAGRAM],
}

CSS = """
@font-face{font-family:"Tenor Sans";src:url(/fonts/tenor-sans-400.woff2) format("woff2");font-weight:400;font-display:swap}
@font-face{font-family:"Jost";src:url(/fonts/jost-300.woff2) format("woff2");font-weight:300;font-display:swap}
@font-face{font-family:"Jost";src:url(/fonts/jost-400.woff2) format("woff2");font-weight:400;font-display:swap}
@font-face{font-family:"Jost";src:url(/fonts/jost-500.woff2) format("woff2");font-weight:500;font-display:swap}
:root{--ink:#0b0a09;--ink2:#15130f;--line:#2b271f;--text:#efe9df;--muted:#b9b0a2;--gold:#c9a96e;--wa:#25d366;--wa-ink:#062b14;
--display:"Tenor Sans","Optima",sans-serif;--body:"Jost",system-ui,-apple-system,"Segoe UI",sans-serif}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{margin:0;background:var(--ink);color:var(--text);font:300 18px/1.65 var(--body)}
a{color:var(--gold)}img,video{max-width:100%;height:auto;display:block}
.skip{position:absolute;left:-999px}.skip:focus{left:12px;top:12px;background:#fff;color:#000;padding:8px;z-index:20}
.wrap{max-width:880px;margin:0 auto;padding:0 20px}
header{border-bottom:1px solid var(--line);position:sticky;top:0;background:rgba(11,10,9,.95);backdrop-filter:blur(8px);z-index:5}
header .wrap{display:flex;align-items:center;justify-content:space-between;gap:12px;min-height:62px;max-width:1080px}
.brand{font-family:var(--display);color:var(--text);text-decoration:none;font-size:19px;white-space:nowrap}
.brand small{display:block;font:400 11px/1.2 var(--body);color:var(--muted);letter-spacing:.1em;text-transform:uppercase}
header nav{display:flex;flex-wrap:wrap;justify-content:flex-end;gap:4px 16px}
header nav a{color:var(--muted);text-decoration:none;font-size:14px;padding:12px 0;display:inline-block}header nav a:hover{color:var(--text)}
@media(max-width:760px){header nav .d{display:none}}
h1,h2,h3{font-family:var(--display);font-weight:400;line-height:1.2;color:#fff}
h1{font-size:clamp(30px,6vw,46px);margin:28px 0 14px}h2{font-size:clamp(23px,4.4vw,31px);margin:52px 0 12px}h3{font-size:21px;margin:28px 0 6px}
.lead{font-size:20px;color:var(--text)}.muted{color:var(--muted);font-size:15px}
.byline{display:flex;gap:10px;align-items:center;font-size:14px;color:var(--muted);margin:10px 0}
.byline img{width:40px;height:40px;border-radius:50%;object-fit:cover;object-position:top}
.btn{display:inline-flex;align-items:center;gap:10px;background:var(--wa);color:var(--wa-ink);font-weight:500;text-decoration:none;padding:14px 22px;border-radius:999px;font-size:17px}
.ctas{display:flex;flex-wrap:wrap;gap:12px;margin:20px 0 6px}
table{width:100%;border-collapse:collapse;margin:16px 0;font-size:16px}
th,td{text-align:left;padding:11px 10px;border-bottom:1px solid var(--line);vertical-align:top}th{color:var(--gold);font-weight:500}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:12px;margin:18px 0}
.card{background:var(--ink2);border:1px solid var(--line);border-radius:14px;padding:18px;color:var(--text);text-decoration:none}
a.card:hover{border-color:var(--gold)}
.card b{display:block;font-family:var(--display);font-weight:400;font-size:26px;color:var(--gold);line-height:1.2;margin-bottom:4px}
.card span{display:block;font-size:15px;color:var(--muted)}
.ba{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:14px 0}figure{margin:0}figcaption{font-size:13px;color:var(--muted);text-align:center;padding-top:4px}
.gallery{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:10px;margin:14px 0}.gallery img{border-radius:12px}
.doc{display:grid;grid-template-columns:200px 1fr;gap:22px;align-items:start}.doc img{border-radius:14px}
@media(max-width:640px){.doc{grid-template-columns:1fr}.doc img{max-width:220px}}
details{border-bottom:1px solid var(--line);padding:12px 0}summary{cursor:pointer;font-weight:500;color:#fff}details p{margin:8px 0 0}
.crumbs{font-size:13px;color:var(--muted);margin-top:18px;line-height:2.2}.crumbs a{color:var(--muted)}
.related{display:flex;flex-wrap:wrap;gap:10px;margin:14px 0}.related a{border:1px solid var(--line);border-radius:999px;padding:8px 14px;text-decoration:none;font-size:15px}
.note{border-left:3px solid var(--gold);padding:4px 0 4px 14px;color:var(--muted);font-size:16px}
.map{width:100%;height:320px;border:0;border-radius:14px;filter:grayscale(.3)}
.final{margin-top:56px;padding-top:8px;border-top:1px solid var(--line)}
footer{border-top:1px solid var(--line);margin-top:56px;padding:28px 0 96px;font-size:15px;color:var(--muted)}footer a{color:var(--muted)}
footer .cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:18px}footer b{color:var(--text);font-weight:500}
footer ul{list-style:none;padding:0;margin:6px 0}footer li{margin:4px 0}
.float{position:fixed;right:16px;bottom:16px;z-index:9;display:flex;gap:8px;align-items:center;background:var(--wa);color:var(--wa-ink);border-radius:999px;padding:12px 18px;font-weight:500;text-decoration:none;box-shadow:0 8px 24px rgba(0,0,0,.4)}
"""

WA_ICON = '<svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2c-1.5 0-3-.4-4.3-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.6.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.8 11.9 11.9 0 0 0 4.6 4c1.7.7 2.4.8 3.2.7a2.8 2.8 0 0 0 1.8-1.3 2.3 2.3 0 0 0 .2-1.3c-.1-.1-.3-.2-.5-.3Z"/></svg>'

NAV_ES = ('<a href="/diseno-de-sonrisa/">Tratamientos</a><a href="/precio-diseno-de-sonrisa-colombia/">Precios</a>'
          '<a href="/antes-y-despues/" class="d">Resultados</a><a href="/dra-catalina-beltran/" class="d">La doctora</a>'
          '<a href="/pacientes-internacionales/" class="d">Pacientes internacionales</a><a href="{ALT}" hreflang="en">EN</a>')
NAV_EN = ('<a href="/en/veneers-medellin/">Veneers</a><a href="/en/cost-of-veneers-colombia/">Prices</a>'
          '<a href="/en/dr-catalina-beltran/" class="d">The doctor</a><a href="{ALT}" hreflang="es">ES</a>')

FOOTER_ES = f"""<div class="cols">
<div><b>Dra. Catalina Beltrán</b><br>Odontología estética<br>{ADDRESS}<br>
WhatsApp <a href="{{WA}}">{PHONE}</a><br><a href="{INSTAGRAM}">Instagram</a></div>
<div><b>Tratamientos</b><ul><li><a href="/diseno-de-sonrisa/">Diseño de sonrisa</a></li><li><a href="/diseno-de-sonrisa/carillas-de-porcelana-emax/">Carillas de porcelana E-max</a></li>
<li><a href="/diseno-de-sonrisa/carillas-de-resina/">Carillas de resina</a></li></ul></div>
<div><b>Pacientes</b><ul><li><a href="/diseno-de-sonrisa-medellin/">Diseño de sonrisa en Medellín</a></li><li><a href="/precio-diseno-de-sonrisa-colombia/">Precios</a></li>
<li><a href="/antes-y-despues/">Antes y después</a></li><li><a href="/pacientes-internacionales/">Pacientes internacionales</a></li>
<li><a href="/contacto/">Contacto</a></li><li><a href="/privacidad/">Privacidad</a></li></ul></div>
</div><p class="muted">Los precios publicados son de referencia; el precio exacto lo confirma la doctora tras revisar tu caso. La información de este sitio es orientativa y no reemplaza una valoración odontológica.</p>"""

FOOTER_EN = f"""<div class="cols">
<div><b>Dr. Catalina Beltrán</b><br>Cosmetic dentistry<br>{ADDRESS}, Colombia<br>
WhatsApp <a href="{{WA}}">{PHONE}</a><br><a href="{INSTAGRAM}">Instagram</a></div>
<div><b>Pages</b><ul><li><a href="/en/veneers-medellin/">Veneers in Medellín</a></li><li><a href="/en/cost-of-veneers-colombia/">Cost of veneers in Colombia</a></li>
<li><a href="/en/dr-catalina-beltran/">About Dr. Catalina</a></li><li><a href="/">Español</a></li></ul></div>
</div><p class="muted">Published prices are reference prices; your exact price is confirmed by the doctor after reviewing your case. This site is for information only and does not replace a dental assessment.</p>"""

CTA_ES = '<div class="ctas"><a class="btn" href="{WA}">{WAICON} Pregúntale tu precio a la doctora</a></div><p class="muted">Valoración gratis por WhatsApp · respuesta el mismo día · sin compromiso</p>'
CTA_EN = '<div class="ctas"><a class="btn" href="{WA}">{WAICON} Ask the doctor for your price</a></div><p class="muted">Free assessment on WhatsApp · same-day reply · no commitment</p>'

PRICE_TABLE_ES = """<table><thead><tr><th>Tratamiento</th><th>Precio de referencia</th></tr></thead><tbody>
<tr><td><a href="/diseno-de-sonrisa/carillas-de-porcelana-emax/">Carilla de porcelana E-max</a> (por diente)</td><td>USD 380</td></tr>
<tr><td><a href="/diseno-de-sonrisa/carillas-de-resina/">Carilla de resina</a> (por diente)</td><td>USD 145</td></tr>
<tr><td>10 carillas de porcelana E-max (sonrisa superior)</td><td>USD 3.800</td></tr>
<tr><td>Sonrisa completa: 20 carillas de porcelana E-max</td><td>USD 5.900 (USD 295 por diente)</td></tr></tbody></table>"""

PRICE_TABLE_EN = """<table><thead><tr><th>Treatment</th><th>Reference price</th></tr></thead><tbody>
<tr><td>E-max porcelain veneer (per tooth)</td><td>USD 380</td></tr>
<tr><td>Composite veneer (per tooth)</td><td>USD 145</td></tr>
<tr><td>10 E-max porcelain veneers (upper smile)</td><td>USD 3,800</td></tr>
<tr><td>Full smile: 20 E-max porcelain veneers</td><td>USD 5,900 (USD 295 per tooth)</td></tr></tbody></table>"""

INCLUDES_ES = "<ul><li>Valoración y diseño digital</li><li>Carillas sin desgaste dental</li><li>Limpieza previa</li><li>Control por videollamada</li></ul><p>No incluye vuelos ni hotel.</p>"
INCLUDES_EN = "<ul><li>Assessment and digital design</li><li>No tooth reduction</li><li>Cleaning beforehand</li><li>Video follow-up at home</li></ul><p>Flights and hotel are not included.</p>"

CASES = {
    # archivo antes, archivo después, ancho, alto, alt antes ES, alt después ES, alt antes EN, alt después EN
    "caso1": ("diseno-de-sonrisa-medellin-antes-caso-1.webp", "diseno-de-sonrisa-medellin-despues-caso-1.webp", 600, 367,
              "Sonrisa antes del diseño de sonrisa, caso 1",
              "La misma sonrisa después del diseño de sonrisa con la Dra. Catalina Beltrán en Medellín",
              "Smile before smile design, case 1", "The same smile after smile design with Dr. Catalina Beltrán in Medellín"),
    "caso2": ("carillas-emax-antes-caso-2.webp", "carillas-emax-sin-desgaste-despues-caso-2.webp", 600, 367,
              "Dientes antes de las carillas de porcelana E-max, caso 2",
              "Los mismos dientes después de carillas de porcelana E-max sin desgaste, Dra. Catalina Beltrán, Medellín",
              "Teeth before E-max porcelain veneers, case 2", "The same teeth after no-prep E-max porcelain veneers, Dr. Catalina Beltrán, Medellín"),
    "caso2b": ("carillas-emax-antes-perfil-caso-2.webp", "carillas-emax-sin-desgaste-despues-perfil-caso-2.webp", 400, 600,
               "Perfil de la sonrisa antes de las carillas de porcelana E-max, caso 2",
               "Perfil de la misma sonrisa después de carillas de porcelana E-max sin desgaste, Dra. Catalina Beltrán, Medellín",
               "Side view of the smile before E-max porcelain veneers, case 2",
               "Side view of the same smile after no-prep E-max porcelain veneers, Dr. Catalina Beltrán, Medellín"),
}
CAPTIONS = {"caso2b": ("Mismo paciente, vista de perfil, antes y después de sus carillas E-max.",
                       "Same patient, side view, before and after his E-max veneers."),
            "caso2": ("Caso real de carillas de porcelana E-max, sin desgaste dental, de la Dra. Catalina Beltrán en Medellín.",
                      "Real case of no-prep E-max porcelain veneers by Dr. Catalina Beltrán in Medellín.")}

def ba(n, es=True):
    fa, fd, w, h, aa, ad, ea, ed = CASES[n]
    a, d = ("Antes", "Después") if es else ("Before", "After")
    alt_a, alt_d = (aa, ad) if es else (ea, ed)
    cap = CAPTIONS.get(n)
    capt = f'<p class="muted">{cap[0] if es else cap[1]}</p>' if cap else ""
    return (f'<div class="ba"><figure><img src="/img/{fa}" width="{w}" height="{h}" alt="{alt_a}" loading="lazy" decoding="async"><figcaption>{a}</figcaption></figure>'
            f'<figure><img src="/img/{fd}" width="{w}" height="{h}" alt="{alt_d}" loading="lazy" decoding="async"><figcaption>{d}</figcaption></figure></div>{capt}')

VIDEO_FILE = "/video/paciente-estados-unidos-se-ve-por-primera-vez-diseno-de-sonrisa-medellin"
VIDEO_SCHEMA = {
    "@type": "VideoObject", "@id": DOMAIN + "/#video-paciente-eeuu",
    "name": "Paciente de Estados Unidos se ve por primera vez después de su diseño de sonrisa en Medellín",
    "description": "Un paciente de Estados Unidos se mira por primera vez al terminar su diseño de sonrisa con la Dra. Catalina Beltrán, odontóloga estética en El Poblado, Medellín.",
    "thumbnailUrl": DOMAIN + VIDEO_FILE + ".webp", "contentUrl": DOMAIN + VIDEO_FILE + ".mp4",
    "uploadDate": "2026-11-07", "duration": "PT19S", "inLanguage": "en",
    "creator": {"@id": ID_PERSON}, "publisher": {"@id": ID_DENTIST},
}
VIDEO_ES = ('<figure><video controls title="Paciente de Estados Unidos se ve por primera vez después de su diseño de sonrisa en Medellín" playsinline preload="none" poster="/video/paciente-estados-unidos-se-ve-por-primera-vez-diseno-de-sonrisa-medellin.webp" width="720" height="720">'
            '<source src="/video/paciente-estados-unidos-se-ve-por-primera-vez-diseno-de-sonrisa-medellin.mp4" type="video/mp4"></video>'
            '<figcaption>Paciente de Estados Unidos al verse por primera vez, al terminar su tratamiento en Medellín.</figcaption></figure>')
VIDEO_EN = VIDEO_ES.replace("Paciente de Estados Unidos al verse por primera vez, al terminar su tratamiento en Medellín.",
                            "A patient from the United States seeing his new smile for the first time, right after treatment in Medellín.")

PATIENTS_ES = """<div class="gallery">
<figure><img src="/img/paciente-1.webp" width="600" height="800" alt="Paciente de Estados Unidos junto a la Dra. Catalina en el consultorio" loading="lazy"><figcaption>Paciente de Estados Unidos</figcaption></figure>
<figure><img src="/img/paciente-2.webp" width="600" height="800" alt="Paciente de Italia con su nueva sonrisa en Medellín" loading="lazy"><figcaption>Paciente de Italia</figcaption></figure>
<figure><img src="/img/paciente-3.webp" width="600" height="800" alt="Paciente de Manizales en el consultorio después de su tratamiento" loading="lazy"><figcaption>Paciente de Manizales, Colombia</figcaption></figure>
<figure><img src="/img/paciente-4.webp" width="600" height="800" alt="Paciente de Estados Unidos junto a la doctora en el consultorio" loading="lazy"><figcaption>Paciente de Estados Unidos</figcaption></figure></div>"""
PATIENTS_EN = (PATIENTS_ES.replace("Paciente de Estados Unidos junto a la Dra. Catalina en el consultorio", "Patient from the United States with Dr. Catalina at the office")
               .replace("Paciente de Italia con su nueva sonrisa en Medellín", "Patient from Italy with her new smile in Medellín")
               .replace("Paciente de Manizales en el consultorio después de su tratamiento", "Patient from Manizales after treatment")
               .replace("Paciente de Estados Unidos junto a la doctora en el consultorio", "Patient from the United States with the doctor")
               .replace(">Paciente de Estados Unidos<", ">Patient from the United States<").replace(">Paciente de Italia<", ">Patient from Italy<")
               .replace(">Paciente de Manizales, Colombia<", ">Patient from Manizales, Colombia<"))

DOCTOR_ES = """<div class="doc"><img src="/img/dra-catalina-beltran-odontologa-estetica-medellin-480.webp" width="480" height="640" alt="Dra. Catalina Beltrán, odontóloga estética en Medellín" loading="lazy">
<div><h3>Dra. Catalina Beltrán</h3><p>Odontóloga con 15 años de experiencia, registrada en el RETHUS desde 2011 y especialista en Estética Dental. Revisa personalmente tus fotos, diseña tu sonrisa y te atiende en su consultorio de El Poblado, en español o en inglés.</p>
<p><a href="/dra-catalina-beltran/">Conoce su formación y experiencia</a></p></div></div>"""
DOCTOR_EN = """<div class="doc"><img src="/img/dra-catalina-beltran-odontologa-estetica-medellin-480.webp" width="480" height="640" alt="Dr. Catalina Beltrán, cosmetic dentist in Medellín" loading="lazy">
<div><h3>Dr. Catalina Beltrán</h3><p>A dentist with 15 years of experience, licensed in Colombia's national health registry (RETHUS) since 2011 and a specialist in Cosmetic Dentistry. She reviews your photos herself, designs your smile and treats you personally at her office in El Poblado, in English or Spanish.</p>
<p><a href="/en/dr-catalina-beltran/">Her training and experience</a></p></div></div>"""

MAP = '<iframe class="map" title="Mapa del consultorio" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://maps.google.com/maps?q=Dra.%20Catalina%20Beltr%C3%A1n%20Cra.%2025%20%2312%20Sur%2059%20Medell%C3%ADn&output=embed"></iframe>'
