#!/usr/bin/env python3
"""Genera la imagen para compartir (og:image, 1200x630) de cada página, con el estilo de img/og.jpg.

Uso (desde la raíz del repo):  python3 _src/og_images.py
Solo usa fotos y datos que ya están publicados en cada página.
"""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "img")
W, H = 1200, 630
BG = (10, 9, 8)
GOLD = (198, 164, 107)
TXT = (242, 237, 230)
MUTED = (200, 194, 186)

def font(name, size):
    return ImageFont.truetype(os.path.join(ROOT, "fonts", name), size)

F_EYE = font("jost-500.woff2", 22)
F_SUB = font("jost-300.woff2", 30)
F_TAG = font("jost-500.woff2", 17)

def wrap(draw, text, f, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=f) <= maxw:
            cur = t
        else:
            lines.append(cur)
            cur = w
    lines.append(cur)
    return lines

def spaced(draw, xy, text, f, fill, track=3):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=f, fill=fill)
        x += draw.textlength(ch, font=f) + track

def cover(im, w, h, top=False):
    r = max(w / im.width, h / im.height)
    im = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
    x = (im.width - w) // 2
    y = 0 if top else (im.height - h) // 2
    return im.crop((x, y, x + w, y + h))

def make(out, eyebrow, title, sub, pair=None, portrait=None, labels=("ANTES", "DESPUÉS")):
    c = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(c)
    textw = 560
    if pair:
        iw, ih, gap = 480, 294, 12
        x = W - 48 - iw
        y0 = (H - (2 * ih + gap)) // 2
        for i, (f, lab) in enumerate(zip(pair, labels)):
            ph = cover(Image.open(os.path.join(IMG, f)).convert("RGB"), iw, ih)
            y = y0 + i * (ih + gap)
            c.paste(ph, (x, y))
            tw = d.textlength(lab, font=F_TAG) + 3 * len(lab) + 24
            d.rectangle((x + 12, y + 12, x + 12 + tw, y + 44), fill=BG)
            spaced(d, (x + 24, y + 18), lab, F_TAG, GOLD, 3)
    if portrait:
        pw = 470
        ph = cover(Image.open(os.path.join(IMG, portrait)).convert("RGB"), pw, H, top=True)
        c.paste(ph, (W - pw, 0))
        grad = Image.linear_gradient("L").rotate(-90).resize((160, H))  # 255 a la izquierda, 0 a la derecha
        c.paste(Image.new("RGB", (160, H), BG), (W - pw, 0), grad)
        textw = 600
    x, y = 72, 70
    spaced(d, (x, y), eyebrow, F_EYE, GOLD, 4)
    size = 62
    while True:
        ft = font("tenor-sans-400.woff2", size)
        lines = wrap(d, title.upper(), ft, textw)
        if len(lines) <= 3 or size <= 44:
            break
        size -= 4
    y += 62
    for ln in lines:
        d.text((x, y), ln, font=ft, fill=TXT)
        y += int(size * 1.15)
    y += 26
    for ln in wrap(d, sub, F_SUB, textw):
        d.text((x, y), ln, font=F_SUB, fill=MUTED)
        y += 42
    d.line((x, H - 100, x + 172, H - 100), fill=GOLD, width=2)
    d.text((x, H - 84), "dracatalinabeltran.com", font=F_TAG, fill=MUTED)
    c.save(os.path.join(IMG, out), "JPEG", quality=86, optimize=True, progressive=True)
    return out

ES_EYE = "DRA. CATALINA BELTRÁN · MEDELLÍN"
EN_EYE = "DR. CATALINA BELTRÁN · MEDELLÍN"
OG = [
    ("og-diseno-de-sonrisa-medellin.jpg", ES_EYE, "Diseño de sonrisa en Medellín",
     "Carillas sin desgaste dental en El Poblado. Valoración gratis por WhatsApp.",
     dict(pair=("diseno-de-sonrisa-medellin-el-poblado-antes.webp", "diseno-de-sonrisa-medellin-el-poblado-despues-carillas-emax.webp"))),
    ("og-que-es-diseno-de-sonrisa.jpg", ES_EYE, "Qué es el diseño de sonrisa",
     "Tipos, materiales y cómo es el proceso.",
     dict(pair=("que-es-diseno-de-sonrisa-antes.webp", "que-es-diseno-de-sonrisa-despues.webp"))),
    ("og-carillas-de-porcelana-emax.jpg", ES_EYE, "Carillas de porcelana E-max",
     "Sin desgaste dental. USD 380 por diente.",
     dict(pair=("carillas-emax-antes-caso-2.webp", "carillas-emax-sin-desgaste-despues-caso-2.webp"))),
    ("og-precio-diseno-de-sonrisa-colombia.jpg", ES_EYE, "Precio del diseño de sonrisa en Colombia",
     "20 carillas de porcelana E-max por USD 5.900.",
     dict(pair=("precio-carillas-emax-colombia-antes.webp", "precio-carillas-emax-colombia-despues.webp"))),
    ("og-antes-y-despues-diseno-de-sonrisa.jpg", ES_EYE, "Antes y después",
     "Casos reales de diseño de sonrisa de la Dra. Catalina Beltrán.",
     dict(pair=("diseno-de-sonrisa-medellin-antes-caso-1.webp", "diseno-de-sonrisa-medellin-despues-caso-1.webp"))),
    ("og-dra-catalina-beltran.jpg", "ODONTOLOGÍA ESTÉTICA · MEDELLÍN", "Dra. Catalina Beltrán",
     "Odontóloga estética con 15 años de experiencia. RETHUS desde 2011.",
     dict(portrait="dra-catalina-beltran-odontologa-estetica-medellin.webp")),
    ("og-pacientes-internacionales.jpg", ES_EYE, "Pacientes internacionales",
     "Un solo viaje de al menos 4 días a Medellín. Precio fijo en dólares antes de viajar.",
     dict(portrait="paciente-estados-unidos-con-la-dra-catalina-beltran-medellin.webp")),
    ("og-contacto-dra-catalina-beltran.jpg", ES_EYE, "Contacto",
     "Cra. 25 #12 Sur 59, El Poblado, Medellín. WhatsApp +57 320 311 8517.",
     dict(portrait="dra-catalina-beltran-odontologa-estetica-medellin.webp")),
    ("og-veneers-medellin.jpg", EN_EYE, "Veneers in Medellín, Colombia",
     "No tooth reduction. 20 porcelain veneers for USD 5,900.",
     dict(pair=("veneers-medellin-before-case-1.webp", "veneers-medellin-after-case-1.webp"), labels=("BEFORE", "AFTER"))),
    ("og-cost-of-veneers-colombia.jpg", EN_EYE, "Cost of veneers in Colombia",
     "E-max porcelain USD 380 per tooth. Fixed price before you travel.",
     dict(pair=("precio-carillas-emax-colombia-antes.webp", "precio-carillas-emax-colombia-despues.webp"), labels=("BEFORE", "AFTER"))),
    ("og-dr-catalina-beltran.jpg", "COSMETIC DENTISTRY · MEDELLÍN", "Dr. Catalina Beltrán",
     "Cosmetic dentist with 15 years of experience. English spoken.",
     dict(portrait="dr-catalina-beltran-cosmetic-dentist-medellin.webp")),
]

if __name__ == "__main__":
    for out, eye, title, sub, kw in OG:
        print(make(out, eye, title, sub, **kw))
