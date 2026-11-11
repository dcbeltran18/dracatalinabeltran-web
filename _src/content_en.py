"""English pages, each paired with its Spanish version via hreflang."""
from common import *

E_VEN = "/en/veneers-medellin/"
E_COST = "/en/cost-of-veneers-colombia/"
E_DRA = "/en/dr-catalina-beltran/"

PAGES = []

VEN_FAQS = [
    ("How much do veneers cost in Medellín?",
     f'With Dr. Catalina Beltrán, an E-max porcelain veneer is USD 380 per tooth and a composite veneer USD 145. A full smile of 20 E-max porcelain veneers is USD 5,900. <a href="{E_COST}">See all prices</a>.'),
    ("How many days do I need in Medellín?", "One trip of at least 4 days. You know your fixed price before you book your flight."),
    ("Does the doctor speak English?", "Yes. Dr. Catalina treats patients in English and Spanish, on WhatsApp and in person."),
    ("Do I need X-rays to get a quote?", "No. For an exact price you send 3 photos taken with your phone, and the doctor shows you how."),
    ("Do veneers damage your teeth?", "Dr. Catalina places veneers with no tooth reduction. What damages a tooth is decay from poor hygiene, so daily brushing, flossing and check-ups keep it healthy."),
    ("Where is the office?", f"At {ADDRESS}, Colombia, in El Poblado. The Ibis Medellín hotel is 300 m away."),
]
PAGES.append(dict(path=E_VEN, lang="en", alt="/diseno-de-sonrisa-medellin/", crumb="Veneers in Medellín", schema_type="MedicalWebPage",
    title="Veneers in Medellín, Colombia | Dr. Catalina Beltrán, El Poblado",
    desc="Porcelain and composite veneers in Medellín with no tooth reduction. E-max veneers USD 380 per tooth, full smile of 20 for USD 5,900. Fixed price before you travel. English spoken.",
    h1="Veneers in Medellín, Colombia",
    lead=("Dr. Catalina Beltrán places E-max porcelain veneers (USD 380 per tooth) and composite veneers (USD 145 per tooth) with no tooth reduction at her office in El Poblado, Medellín. "
          "A full smile of 20 porcelain veneers is USD 5,900, and you get a fixed price in US dollars before you book your flight."),
    wa="Hi Dr. Catalina 👋 I saw your website and I'd like to know the price of my smile design.", faqs=VEN_FAQS, image="/img/caso1-despues-600.webp",
    body=f"""<div class="cards"><div class="card"><b>USD 295</b><span>per tooth on a 20-veneer porcelain smile</span></div><div class="card"><b>4 days</b><span>one trip to Medellín</span></div>
<div class="card"><b>5.0</b><span>Google rating</span></div><div class="card"><b>15 years</b><span>of experience</span></div></div>
<section><h2>How does it work?</h2><ol>
<li><b>Message us on WhatsApp.</b> Tell us what you'd like to change. For an exact price, send 3 photos with your phone. No X-rays needed.</li>
<li><b>Get your assessment and fixed price.</b> The doctor tells you which option fits and how many teeth to treat. By video call if you prefer.</li>
<li><b>Travel once.</b> Your design is planned before any work starts. Plan at least 4 days in Medellín.</li>
<li><b>Fly home smiling.</b> Follow-up is by video call.</li></ol></section>
<section><h2>How much do veneers cost?</h2>{PRICE_TABLE_EN}{INCLUDES_EN}<p><a href="{E_COST}">Full price details and US comparison</a></p></section>
<section><h2>Porcelain or composite veneers?</h2>
<table><thead><tr><th></th><th>Composite</th><th>E-max porcelain</th></tr></thead><tbody>
<tr><td>Price per tooth</td><td>USD 145</td><td>USD 380</td></tr><tr><td>Color over time</td><td>Can stain</td><td>Keeps its color</td></tr><tr><td>Durability</td><td>Lower</td><td>Higher</td></tr><tr><td>Repairs</td><td>Can be touched up</td><td>The piece is replaced</td></tr></tbody></table></section>
<section><h2>Real results</h2>{ba("caso1", False)}{VIDEO_EN}</section>
<section><h2>Patients who flew to Medellín</h2>{PATIENTS_EN}</section>
<section><h2>Your dentist</h2>{DOCTOR_EN}</section>
<section><h2>Where to stay</h2><p>The office is in El Poblado, one of the areas of Medellín with the most hotels and restaurants. We recommend the Ibis Medellín, 300 m from the office.</p></section>""",
    related=[("Cost of veneers in Colombia", E_COST), ("About Dr. Catalina", E_DRA), ("Español", "/diseno-de-sonrisa-medellin/")]))

COST_FAQS = [
    ("How much is 20 veneers in Colombia?", "With Dr. Catalina Beltrán in Medellín, a full smile of 20 E-max porcelain veneers is USD 5,900, about USD 295 per tooth. Bought one by one, 20 veneers would be USD 7,600."),
    ("Is it cheaper to get veneers in Colombia?", "Yes. Published US ranges are USD 1,000–2,500 per porcelain veneer; in Medellín with Dr. Catalina it is USD 380, using the same E-max material."),
    ("Can I get veneers for $5,000?", "Yes. 10 E-max porcelain veneers for the upper smile are USD 3,800. A full smile of 20 porcelain veneers is USD 5,900."),
    ("What is included in the price?", "Assessment and digital design, veneers with no tooth reduction, a cleaning beforehand and video follow-up once you are home. Flights and hotel are not included."),
    ("Why do veneer prices vary so much between clinics?", "Material (composite or porcelain), porcelain brand, number of teeth, any treatment needed beforehand, and whether design and follow-up are included. Always ask what the price includes and whether it is fixed."),
]
PAGES.append(dict(path=E_COST, lang="en", alt="/precio-diseno-de-sonrisa-colombia/", crumb="Cost of veneers in Colombia", parents=[("Veneers in Medellín", E_VEN)],
    title="Cost of Veneers in Colombia (2026): Real Prices in Medellín",
    desc="How much do veneers cost in Colombia? E-max porcelain USD 380 per tooth, composite USD 145, 20 veneers USD 5,900. What's included and how it compares with the US.",
    h1="Cost of veneers in Colombia",
    lead=("In Medellín, with Dr. Catalina Beltrán, a full smile of 20 E-max porcelain veneers costs USD 5,900, about USD 295 per tooth. "
          "A single porcelain veneer is USD 380 and a composite veneer USD 145, with a fixed price before you travel."),
    wa="Hi Dr. Catalina 👋 I saw your website (prices) and I'd like to know the exact price of my case.", faqs=COST_FAQS,
    body=f"""<section><h2>2026 reference prices</h2>{PRICE_TABLE_EN}<p class="muted">Prices as of {fecha_en(UPDATED)}. Your exact price depends on how many teeth you need; the doctor confirms it for free on WhatsApp.</p></section>
<section><h2>How do prices in Colombia compare with the US?</h2>
<table><thead><tr><th>Treatment</th><th>US (published range)</th><th>Dr. Catalina, Medellín</th></tr></thead><tbody>
<tr><td>Porcelain veneer</td><td>USD 1,000–2,500</td><td>USD 380</td></tr><tr><td>Composite veneer</td><td>USD 400–1,500</td><td>USD 145</td></tr><tr><td>10 porcelain veneers</td><td>USD 10,000+</td><td>USD 3,800</td></tr></tbody></table></section>
<section><h2>What's included?</h2>{INCLUDES_EN}<p>We recommend the Ibis Medellín, 300 m from the office.</p></section>
<section><h2>How long does the trip take?</h2><p>One trip of at least 4 days. <a href="{E_VEN}">See how the process works</a>.</p></section>""",
    related=[("Veneers in Medellín", E_VEN), ("About Dr. Catalina", E_DRA), ("Español", "/precio-diseno-de-sonrisa-colombia/")]))

PAGES.append(dict(path=E_DRA, lang="en", alt="/dra-catalina-beltran/", crumb="Dr. Catalina Beltrán", schema_type="ProfilePage", byline=False,
    title="Dr. Catalina Beltrán | Cosmetic Dentist in Medellín, Colombia",
    desc="Meet Dr. Catalina Beltrán: a dentist with 15 years of experience, specialist in Cosmetic Dentistry, licensed in Colombia since 2011. Office in El Poblado, Medellín. English spoken.",
    h1="Dr. Catalina Beltrán",
    lead="Dr. Catalina Beltrán is a dentist with 15 years of experience, licensed in Colombia's national health registry (RETHUS) since 2011 and a specialist in Cosmetic Dentistry. She treats every patient personally at her office in El Poblado, Medellín.",
    wa="Hi Dr. Catalina 👋 I saw your website and I'd like to know the price of my smile design.", image="/img/dra-catalina-900.webp",
    body=f"""<img src="/img/dra-catalina-900.webp" width="900" height="1200" alt="Dr. Catalina Beltrán, cosmetic dentist" style="max-width:360px;border-radius:16px;margin:18px 0">
<section><h2>Training</h2><table><tbody>
<tr><td>Dentist with an emphasis in surgical sciences</td><td>Colegio Odontológico Colombiano</td></tr>
<tr><td>Specialist in Cosmetic Dentistry</td><td>Federación Odontológica Colombiana</td></tr>
<tr><td>Postgraduate degree in Healthcare Auditing and Quality Assurance</td><td>Universidad EAN</td></tr>
<tr><td>License</td><td>RETHUS (Colombia), since 2011</td></tr></tbody></table></section>
<section><h2>How she works</h2><p>She reviews each patient's photos herself, designs the smile around the face, skin tone and bite, and gives a fixed price before any work starts. She places veneers with no tooth reduction and speaks English and Spanish.</p></section>
<section><h2>Patients</h2>{PATIENTS_EN}</section>""",
    related=[("Veneers in Medellín", E_VEN), ("Cost of veneers in Colombia", E_COST)]))
