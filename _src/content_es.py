"""Páginas en español.
Reglas: cada dato y cada pregunta vive en UNA sola página (sin canibalización);
la tabla completa de precios solo está en Precios; las demás enlazan.
Marcas [REVISAR] = afirmaciones clínicas que la doctora debe confirmar."""
from common import *

T = "/diseno-de-sonrisa/"
P_EMAX = T + "carillas-de-porcelana-emax/"
P_RES = T + "carillas-de-resina/"
P_MED = "/diseno-de-sonrisa-medellin/"
P_PRICE = "/precio-diseno-de-sonrisa-colombia/"
P_DRA = "/dra-catalina-beltran/"
P_BA = "/antes-y-despues/"
P_INT = "/pacientes-internacionales/"
P_CONT = "/contacto/"
P_MEJOR = "/mejor-diseno-de-sonrisa-medellin/"
P_MICRO = T + "microdiseno-de-sonrisa/"
P_BLANQ = "/blanqueamiento-dental-medellin/"

TRAT = ("Tratamientos", T)
def wa(t): return f"Hola Dra. Catalina 👋 Vi su página web ({t}) y tengo una pregunta. Mi nombre es: "
PRICE_LINE = f'Porcelana E-max USD 380 por diente · resina USD 145 por diente · sonrisa completa de 20 carillas de porcelana USD 5.900. <a href="{P_PRICE}">Ver precios y qué incluyen</a>.'

PAGES = []

# ---------------- INICIO ----------------
PAGES.append(dict(path="/", lang="es", byline=False,
    title="Dra. Catalina Beltrán | Odontóloga estética en Medellín",
    desc="Odontóloga estética en El Poblado, Medellín. Carillas sin desgaste en porcelana E-max y resina, con precio cerrado. 15 años de experiencia, 5,0 en Google.",
    h1="Dra. Catalina Beltrán, odontóloga estética en Medellín",
    lead=("La Dra. Catalina Beltrán es odontóloga estética en El Poblado, Medellín, con 15 años de experiencia y calificación de 5,0 en Google. "
          "Hace diseños de sonrisa con carillas de porcelana E-max y de resina sin desgaste dental, con precio cerrado antes de empezar: desde USD 145 por diente en resina y USD 5.900 por una sonrisa completa de 20 carillas de porcelana."),
    wa=wa("inicio"),
    body=f"""<div class="cards"><div class="card"><b>5,0</b><span>Calificación en Google</span></div><div class="card"><b>15 años</b><span>de experiencia</span></div>
<div class="card"><b>0 desgaste</b><span>Carillas sin desgastar tus dientes</span></div><div class="card"><b>USD 295</b><span>por diente en sonrisa completa de porcelana</span></div></div>
<section><h2>Tratamientos</h2>
<p>La Dra. Catalina Beltrán hace diseños de sonrisa con carillas de porcelana E-max y carillas de resina, sin desgaste dental.</p>
<div class="cards">
<a class="card" href="{P_EMAX}"><b>Porcelana E-max</b><span>Carillas de porcelana a la medida. USD 380 por diente.</span></a>
<a class="card" href="{P_RES}"><b>Resina</b><span>La forma más económica de un diseño completo. USD 145 por diente.</span></a>
<a class="card" href="{T}"><b>Guía de diseño de sonrisa</b><span>Tipos, microdiseño, blanqueamiento y cómo elegir.</span></a></div></section>
<section><h2>Precios</h2><p>{PRICE_LINE}</p></section>
<section><h2>Resultados</h2><p>Estos son resultados reales de diseño de sonrisa de la Dra. Catalina Beltrán en Medellín, publicados con autorización de los pacientes.</p>{ba("caso1")}<p><a href="{P_BA}">Ver más casos de antes y después</a></p></section>
<section><h2>Cómo funciona</h2><p>Todo empieza por WhatsApp: la doctora revisa tus fotos, te da un precio cerrado y luego haces el tratamiento en su consultorio de El Poblado.</p><ol>
<li><b>Escríbele por WhatsApp.</b> Cuéntale qué te gustaría cambiar y envía 3 fotos con tu celular; no necesitas radiografías.</li>
<li><b>Recibe tu valoración.</b> La doctora te dice qué opción te conviene, cuántos dientes tratar y el precio cerrado.</li>
<li><b>Haz tu tratamiento</b> en el <a href="{P_MED}">consultorio de El Poblado, Medellín</a>. Si vives fuera de Colombia: <a href="{P_INT}">un solo viaje de mínimo 4 días</a>.</li></ol></section>
<section><h2>Tu odontóloga</h2>{DOCTOR_ES}<p>¿Estás comparando opciones? Mira <a href="{P_MEJOR}">cómo elegir dónde hacerte el diseño de sonrisa en Medellín</a>.</p></section>
<section><h2>Pacientes</h2><p>Calificación de 5,0 en Google.</p>{PATIENTS_ES}</section>
<section><h2>Consultorio</h2><p>{ADDRESS}. <a href="{P_CONT}">Ver mapa y contacto</a>.</p></section>""",
    related=[("Diseño de sonrisa en Medellín", P_MED), ("Precios", P_PRICE), ("Pacientes internacionales", P_INT)]))

# ---------------- MEDELLÍN ----------------
MED_FAQS = [
    ("¿Atienden en inglés?", "Sí. La doctora atiende en español e inglés, por WhatsApp y en el consultorio."),
]
PAGES.append(dict(path=P_MED, lang="es", alt="/en/veneers-medellin/", crumb="Diseño de sonrisa en Medellín", schema_type="MedicalWebPage",
    title="Diseño de sonrisa en Medellín | Carillas sin desgaste",
    desc="Diseño de sonrisa en Medellín sin desgaste dental: porcelana E-max USD 380 y resina USD 145 por diente, en El Poblado. Precio cerrado y valoración gratis.",
    h1="Diseño de sonrisa en Medellín",
    lead=("En Medellín, la Dra. Catalina Beltrán hace diseños de sonrisa con carillas de porcelana E-max (USD 380 por diente) y de resina (USD 145 por diente), sin desgaste dental, en su consultorio de El Poblado. "
          "Recibes el plan y el precio cerrado antes de empezar, y la valoración es gratis por WhatsApp."),
    wa=wa("diseño de sonrisa Medellín"), faqs=MED_FAQS, image="/video/paciente-estados-unidos-se-ve-por-primera-vez-diseno-de-sonrisa-medellin.webp", video=True,
    body=f"""<section><p>Este paciente viajó desde Estados Unidos a Medellín para su diseño de sonrisa con la Dra. Catalina. El video lo muestra en el consultorio de El Poblado, al terminar el tratamiento, cuando se mira por primera vez.</p>
{VIDEO_ES}</section>
<section><h2>¿Cuánto cuesta un diseño de sonrisa en Medellín?</h2>
<p>Con la Dra. Catalina, una sonrisa completa de 20 carillas de porcelana E-max cuesta USD 5.900 (USD 295 por diente) y una sonrisa superior de 10 carillas, USD 3.800. En resina, cada diente cuesta USD 145. El precio incluye valoración y diseño digital, limpieza previa y control por videollamada. <a href="{P_PRICE}">Ver todos los precios</a>.</p></section>
<section><h2>¿Qué opciones de diseño de sonrisa hay en Medellín?</h2>
<p>Las dos formas de hacer un diseño completo son las <a href="{P_EMAX}">carillas de porcelana E-max</a>, más duraderas, y las <a href="{P_RES}">carillas de resina</a>, más económicas. Si solo quieres mejorar los bordes de tus dientes, el <a href="{P_MICRO}">microdiseño</a> es más rápido y económico; para aclarar el color, <a href="{T}">compara las opciones en la guía de diseño de sonrisa</a>.</p></section>
<section><h2>¿Cómo es el proceso en el consultorio?</h2>
<p>Le escribes a la doctora por WhatsApp y le envías 3 fotos con tu celular. Ella te dice qué opción te conviene, cuántos dientes tratar y el precio cerrado; si prefieres, por videollamada. Antes de tocar un diente, planifica tu diseño digital. En el consultorio hace la limpieza previa y el tratamiento, y el control posterior es por videollamada.</p></section>
<section><h2>Resultados en Medellín</h2>
<h3>Antes y después en el consultorio de El Poblado</h3>
<p>Un caso real de la Dra. Catalina en Medellín: 6 carillas superiores de porcelana E-max colocadas sin desgaste dental, en su consultorio de El Poblado. El paciente viajó desde Francia.</p>
{ba_page("caso2", "diseno-de-sonrisa-medellin-el-poblado-antes.webp", "diseno-de-sonrisa-medellin-el-poblado-despues-carillas-emax.webp",
 "Sonrisa antes del diseño de sonrisa en Medellín", "La misma sonrisa después del diseño de sonrisa con carillas E-max sin desgaste en El Poblado, Medellín",
 "Caso real en el consultorio de El Poblado, Medellín: 6 carillas superiores de porcelana E-max sin desgaste, paciente que viajó desde Francia.")}
<p>Mira el <a href="{P_EMAX}">mismo caso de frente y de perfil</a>, o <a href="{P_BA}">todos los casos de antes y después</a>.</p></section>
<section><h2>¿Por qué elegir a la Dra. Catalina?</h2>
<p>La Dra. Catalina Beltrán coloca las carillas sin desgaste dental, da un precio cerrado antes de empezar y atiende personalmente a cada paciente.</p>
<ul><li>Carillas sin desgaste dental: tus dientes naturales se conservan.</li><li>Precio cerrado antes de empezar, publicado en dólares.</li><li>Atención personal de la doctora, en español e inglés.</li>
<li>15 años de experiencia y registro en el RETHUS desde 2011.</li><li>Consultorio en El Poblado, una de las zonas de Medellín con más hoteles y restaurantes.</li></ul>
<p>Si estás comparando opciones, revisa <a href="{P_MEJOR}">cómo elegir el mejor diseño de sonrisa en Medellín</a>.</p>
{DOCTOR_ES}</section>
<section><h2>¿Dónde queda el consultorio?</h2><p><b>Dra. Catalina Beltrán - Diseño de Sonrisa en Medellín</b><br>Carrera 25 # 12 Sur 59, El Poblado, Medellín · WhatsApp <a href="{{WA}}">{PHONE}</a></p><p>Si vienes de otro país, el hotel Ibis Medellín está a 300 m.</p>{MAP}</section>""",
    related=[("Precios", P_PRICE), ("Guía de diseño de sonrisa", T), ("Pacientes internacionales", P_INT)]))

# ---------------- CÓMO ELEGIR (MEJOR) ----------------
MEJOR_FAQS = [
    ("¿Cómo verifico si una odontóloga está registrada?",
     "En la consulta pública del RETHUS (Registro Único Nacional del Talento Humano en Salud) del Ministerio de Salud de Colombia, buscando su nombre o su número de documento. La Dra. Catalina Beltrán está registrada desde 2011."),
    ("¿Puedo saber si soy candidato antes de ir al consultorio?",
     "Sí. La valoración es gratis por WhatsApp: envías 3 fotos con tu celular y la Dra. Catalina te dice qué opción te conviene y el precio cerrado de tu caso."),
]
PAGES.append(dict(path=P_MEJOR, lang="es", updated="2026-11-19", crumb="Cómo elegir diseño de sonrisa en Medellín", schema_type="MedicalWebPage",
    title="¿Cuál es el mejor diseño de sonrisa en Medellín? Cómo elegir",
    desc="Cómo elegir el mejor diseño de sonrisa y la odontóloga correcta en Medellín: 6 criterios verificables, preguntas para la consulta y señales de alerta.",
    h1="¿Cuál es el mejor diseño de sonrisa en Medellín?",
    lead=("No hay un diseño de sonrisa que sea el mejor para todos: el mejor es el que conserva tus dientes, se ve natural con tu cara y dura muchos años. "
          "Para elegir dónde hacértelo en Medellín, revisa seis criterios que puedes comprobar tú mismo: registro profesional, desgaste dental, casos reales, opiniones verificables, precio cerrado y material. "
          "Aquí te explicamos cómo comprobar cada uno y cómo los cumple la Dra. Catalina Beltrán."),
    wa=wa("cómo elegir diseño de sonrisa"), faqs=MEJOR_FAQS,
    body=f"""<section><h2>¿Qué hace que un diseño de sonrisa sea el mejor?</h2>
<p>Un buen diseño de sonrisa se planifica según tu cara, tu tono de piel y tu mordida, para que el resultado se vea natural y no exagerado. Conserva la mayor cantidad posible de diente natural, empieza por revisar la salud de dientes y encías, y usa un material que dure lo que esperas. Si un tratamiento solo promete dientes muy blancos y parejos, sin hablar de nada de esto, no es la mejor opción aunque sea la más rápida o la más barata.</p>
<p>Además, no todas las personas necesitan carillas. Si tus dientes tienen buena forma y solo quieres aclarar el color o mejorar los bordes, un <a href="{P_BLANQ}">blanqueamiento</a> o un <a href="{P_MICRO}">microdiseño</a> puede ser suficiente; <a href="{T}">compara las opciones en la guía de diseño de sonrisa</a>. Y si hay caries o encías inflamadas, se tratan primero: una buena odontóloga te lo dice en la valoración, aunque eso signifique no hacer carillas.</p></section>
<section><h2>6 criterios para elegir dónde hacerte el diseño de sonrisa en Medellín</h2>
<p>Estos son los puntos que conviene revisar con cualquier odontóloga antes de pagar, y lo que encontrarás con la Dra. Catalina Beltrán.</p>
<table><thead><tr><th>Criterio</th><th>Qué revisar</th><th>Con la Dra. Catalina Beltrán</th></tr></thead><tbody>
<tr><td><b>1. Registro profesional</b></td><td>Que esté registrada en el RETHUS y que tenga formación en estética dental.</td><td>Registrada en el RETHUS desde 2011, 15 años de experiencia y especialista en Estética Dental. <a href="{P_DRA}">Ver su formación</a>.</td></tr>
<tr><td><b>2. Que conserve tus dientes</b></td><td>Pregunta si las carillas requieren desgastar tus dientes y cuánto.</td><td>Carillas sin desgaste dental: tus dientes naturales se conservan.</td></tr>
<tr><td><b>3. Casos reales</b></td><td>Fotos de antes y después de pacientes reales, no imágenes de catálogo.</td><td>Casos publicados con autorización, entre ellos pacientes que viajaron desde Francia y Estados Unidos. <a href="{P_BA}">Ver antes y después</a>.</td></tr>
<tr><td><b>4. Opiniones verificables</b></td><td>Reseñas en Google con nombre, no testimonios anónimos.</td><td>Calificación de 5,0 en Google con 23 reseñas (noviembre de 2026). <a href="https://www.google.com/maps/search/?api=1&amp;query=Dra.%20Catalina%20Beltr%C3%A1n%20-%20Dise%C3%B1o%20de%20Sonrisa%20en%20Medellin&amp;query_place_id=ChIJ5UxszfqDRo4R-RxohnoXKdA" rel="noopener" target="_blank">Ver las opiniones en Google</a>.</td></tr>
<tr><td><b>5. Precio claro y cerrado</b></td><td>Que el precio esté publicado, que diga qué incluye y que no cambie después de empezar.</td><td>Porcelana E-max USD 380 por diente, resina USD 145 por diente y sonrisa completa de 20 carillas de porcelana USD 5.900, con precio cerrado antes de empezar. <a href="{P_PRICE}">Ver precios</a>. Si vives en Colombia, pide tu precio en pesos por WhatsApp.</td></tr>
<tr><td><b>6. Material y duración</b></td><td>Que te explique la diferencia entre porcelana y resina, y cuánto dura cada una.</td><td>Porcelana E-max: de 10 a 20 años o más con mantenimiento. Resina: de 5 a 7 años en promedio, hasta 10 con mantenimiento.</td></tr>
</tbody></table></section>
<section><h2>¿Cuál es la mejor doctora para diseño de sonrisa en Medellín?</h2>
<p>La mejor odontóloga para ti es la que cumple los seis criterios anteriores y te explica tu caso antes de cobrarte. Estas son las preguntas que conviene hacerle en la valoración:</p>
<ul><li>¿Mis dientes y encías están sanos para hacerme carillas, o hay que tratar algo antes?</li>
<li>¿Hay que desgastar mis dientes? ¿Cuánto y por qué?</li>
<li>¿Porcelana o resina en mi caso, y cuánto dura cada una?</li>
<li>¿Cuál es el precio cerrado y qué incluye: diseño digital, limpieza, controles?</li>
<li>¿Puedo ver casos reales parecidos al mío?</li>
<li>¿Quién me atiende en cada cita?</li></ul>
<p>La Dra. Catalina Beltrán responde estas preguntas en la valoración gratis por WhatsApp, antes de que tomes cualquier decisión, y atiende personalmente a cada paciente en su consultorio de El Poblado.</p>
{DOCTOR_ES}</section>
<section><h2>Señales de alerta antes de hacerte un diseño de sonrisa</h2>
<ul><li>Un precio que no dice qué incluye o que cambia una vez empezado el tratamiento.</li>
<li>Desgastar dientes sanos sin explicarte por qué es necesario en tu caso.</li>
<li>Empezar sin revisar la salud de tus dientes y encías.</li>
<li>Fotos de resultados que no son de pacientes de esa misma odontóloga.</li>
<li>Presión para pagar antes de recibir una valoración y un plan.</li></ul></section>
<section><h2>Pacientes de la Dra. Catalina</h2><p>Pacientes de Colombia y de otros países que se hicieron su diseño de sonrisa en el consultorio de El Poblado.</p>{PATIENTS_ES}</section>
<section><h2>¿Dónde queda el consultorio?</h2><p><b>Dra. Catalina Beltrán - Diseño de Sonrisa en Medellín</b><br>{ADDRESS} · WhatsApp <a href="{{WA}}">{PHONE}</a>. Si vives fuera de Colombia, el tratamiento se hace en <a href="{P_INT}">un solo viaje de mínimo 4 días</a>.</p></section>""",
    related=[("Diseño de sonrisa en Medellín", P_MED), ("Precios", P_PRICE), ("Antes y después", P_BA)]))

# ---------------- PILAR ----------------
PILAR_FAQS = [
    ("¿El diseño de sonrisa es bueno o malo?",
     "Es un tratamiento seguro cuando lo hace una odontóloga calificada después de revisar la salud de dientes y encías. Los problemas suelen venir de tratamientos sin valoración previa o de desgastar dientes sanos sin necesidad."),
    ("¿El diseño de sonrisa es lo mismo que las carillas?",
     "No exactamente. El diseño de sonrisa es el plan (forma, tamaño, color y proporción de los dientes según tu cara); las carillas son una de las formas de llevarlo a cabo."),
]
PAGES.append(dict(path=T, lang="es", crumb="Diseño de sonrisa", schema_type="MedicalWebPage",
    title="¿Qué es el diseño de sonrisa? Tipos, duración y cómo elegir",
    desc="Qué es el diseño de sonrisa, sus tipos (porcelana, resina, microdiseño, blanqueamiento), cuánto dura y quién puede hacérselo. Guía de una odontóloga.",
    h1="Diseño de sonrisa: qué es, tipos y cómo elegir",
    lead=("El diseño de sonrisa es un plan odontológico que define la forma, el tamaño, el color y la proporción de tus dientes según tu cara, y luego lo lleva a cabo con carillas de porcelana, carillas de resina, microdiseño o blanqueamiento. "
          "La opción correcta depende de cuánto quieres cambiar, de tu presupuesto y de la salud de tus dientes."),
    wa=wa("diseño de sonrisa"), faqs=PILAR_FAQS,
    body=f"""<section><h2>¿Qué tipos de diseño de sonrisa hay?</h2>
<p>Hay cuatro tipos de diseño de sonrisa: carillas de porcelana E-max, carillas de resina, microdiseño y blanqueamiento. Se diferencian en qué cambian y en cuándo conviene cada uno.</p>
<table><thead><tr><th>Opción</th><th>Qué cambia</th><th>Cuándo conviene</th></tr></thead><tbody>
<tr><td><a href="{P_EMAX}">Carillas de porcelana E-max</a></td><td>Forma, tamaño y color</td><td>Cambio completo y duradero</td></tr>
<tr><td><a href="{P_RES}">Carillas de resina</a></td><td>Forma, tamaño y color</td><td>Cambio completo con menor inversión</td></tr>
<tr><td><a href="{P_MICRO}">Microdiseño</a></td><td>Solo los bordes de los dientes, en resina</td><td>Mejorar bordes y textura con la menor inversión</td></tr>
<tr><td><a href="{P_BLANQ}">Blanqueamiento</a></td><td>Solo el color de dientes naturales</td><td>Dientes sanos con manchas</td></tr></tbody></table>
<p>Precios: {PRICE_LINE}</p></section>
<section><h2>¿Cómo se hacen las carillas de un diseño de sonrisa?</h2>
<p>Las carillas son láminas ultradelgadas que cubren el diente completo. Primero se toma un escáner 3D de tu boca y, con esa imagen, un laboratorio las fabrica con equipos CNC, en porcelana E-max (disilicato de litio) o en resina. Con la Dra. Catalina Beltrán se colocan sin desgastar tus dientes naturales.</p>
<p>El <a href="{P_MICRO}">microdiseño</a> se hace de otra forma: la doctora lo hace a mano, solo en los bordes de cada diente y siempre en resina. Por eso es más rápido y más económico que las carillas.</p></section>
<section><h2>¿Las carillas se manchan?</h2>
<p>Depende del material. Las carillas de resina pueden pigmentarse con los años, igual que el diente natural, sobre todo con bebidas oscuras como el café o el vino. Las <a href="{P_EMAX}">carillas de porcelana E-max</a>, hechas en disilicato de litio, no se manchan, son más resistentes y cuestan más: USD 380 por diente frente a USD 145 de las <a href="{P_RES}">carillas de resina</a>.</p></section>
<section><h2>¿Cómo se ve un diseño de sonrisa antes y después?</h2>
<p>Un diseño de sonrisa cambia la forma, el tamaño y el color de los dientes visibles, siempre en proporción con la cara. Estos son dos casos reales de la Dra. Catalina en Medellín.</p>
<h3>Diseño de sonrisa completo</h3>
{ba_page("caso1", "que-es-diseno-de-sonrisa-antes.webp", "que-es-diseno-de-sonrisa-despues.webp",
 "Dientes antes de un diseño de sonrisa, caso real en Medellín", "Los mismos dientes después del diseño de sonrisa: forma, tamaño y color en proporción con la cara",
 "Ejemplo de diseño de sonrisa: cambio de forma, tamaño y color de los dientes visibles.")}
<h3>Diseño de sonrisa con carillas de porcelana E-max</h3>
{ba_page("caso2", "tipos-de-diseno-de-sonrisa-carillas-emax-antes.webp", "tipos-de-diseno-de-sonrisa-carillas-emax-despues.webp",
 "Sonrisa antes de un diseño de sonrisa con carillas de porcelana", "La misma sonrisa después de un diseño de sonrisa con carillas de porcelana E-max sin desgaste",
 "Uno de los tipos de diseño de sonrisa: 6 carillas superiores de porcelana E-max, colocadas sin desgaste dental.")}
<p><a href="{P_BA}">Ver todos los casos de antes y después</a></p></section>
<section><h2>¿Qué es mejor, carillas o microdiseño?</h2>
<p>Depende de cuánto quieres cambiar: el microdiseño solo trabaja los bordes de cada diente, mientras que las carillas cubren el diente completo. Ordenadas de mayor a menor inversión: carillas de porcelana E-max (disilicato de litio), carillas de resina y microdiseño. En los tres casos se suelen tratar los 6 dientes de arriba y los 6 de abajo que se ven al sonreír. <a href="{P_MICRO}">Ver qué es el microdiseño</a>.</p></section>
<section><h2>¿Blanqueamiento o carillas?</h2>
<p>El blanqueamiento aclara el color de los dientes naturales, pero no cambia su forma ni se puede aplicar sobre una carilla. Si solo te molesta el color y tus dientes están sanos, empieza por un <a href="{P_BLANQ}">blanqueamiento dental</a>. Si vas a hacerte carillas, conviene blanquear antes para elegir el tono final. Mira el <a href="{P_BLANQ}">precio y cuánto dura el blanqueamiento</a>.</p></section>
<section><h2>¿Cómo se hace un diseño de sonrisa?</h2>
<p>La doctora revisa tus fotos y la salud de tus dientes y encías. Luego diseña digitalmente tu sonrisa según tu cara, tu tono de piel y tu mordida, y te muestra el plan con el precio cerrado. Solo cuando lo apruebas se hace la limpieza previa y el tratamiento en el <a href="{P_MED}">consultorio de El Poblado, Medellín</a>. El control posterior es por videollamada.</p></section>
<section><h2>¿Cuánto dura un diseño de sonrisa?</h2>
<p>Depende del material y de tus cuidados. La porcelana E-max es la opción más duradera: entre 10 y 20 años, e incluso más con un mantenimiento adecuado, y conserva su color. La resina dura en promedio de 5 a 7 años y, con mantenimiento, puede llegar hasta 10 años; con los años puede necesitar pulido o retoques. En ambos casos influyen la higiene diaria, los controles y hábitos como morder objetos duros o apretar los dientes.</p></section>
<section><h2>¿Quién puede hacerse un diseño de sonrisa?</h2>
<p>Adultos con dientes y encías sanos, o que los tratan antes. Si tienes caries, enfermedad de las encías o bruxismo, la doctora lo evalúa primero y te dice si conviene tratarlo antes de empezar.</p></section>""",
    related=[("Carillas de porcelana E-max", P_EMAX), ("Carillas de resina", P_RES), ("Diseño de sonrisa en Medellín", P_MED)]))

# ---------------- E-MAX ----------------
EMAX_FAQS = [
    ("¿Las carillas E-max requieren desgastar los dientes?", "Con la Dra. Catalina, no. Coloca las carillas sin desgaste dental, de modo que tus dientes naturales se conservan."),
    ("¿Las carillas E-max se manchan?", "No. La porcelana E-max no absorbe pigmentos como el café o el vino, por eso conserva su color."),  # [REVISAR]
    ("¿Las carillas pudren los dientes?", "No. Lo que daña un diente es la caries por mala higiene debajo o alrededor de la carilla. Con higiene diaria y controles, el diente se mantiene sano."),
    ("¿Cuándo no se pueden poner carillas?", "Cuando hay caries o enfermedad de encías sin tratar, o un bruxismo fuerte sin control. La doctora lo revisa en la valoración y, si hace falta, lo trata antes."),
]
PAGES.append(dict(path=P_EMAX, lang="es", crumb="Carillas de porcelana E-max", parents=[TRAT], schema_type="MedicalWebPage",
    title="Carillas de porcelana E-max en Medellín: precio y duración",
    desc="Carillas E-max sin desgaste en Medellín: USD 380 por diente, 20 carillas por USD 5.900 y una duración de 10 a 20 años. Ventajas, desventajas y cuidados.",
    h1="Carillas de porcelana E-max",
    lead=("Las carillas E-max son láminas delgadas de porcelana de disilicato de litio que se adhieren al frente de los dientes para cambiar su forma, tamaño y color. "
          "Con la Dra. Catalina Beltrán en Medellín se colocan sin desgaste dental y cuestan USD 380 por diente; la sonrisa completa de 20 carillas cuesta USD 5.900."),
    wa=wa("carillas E-max"), faqs=EMAX_FAQS, image="/img/carillas-emax-sin-desgaste-despues-caso-2.webp",
    body=f"""<section><h2>¿Qué son las carillas E-max?</h2>
<p>E-max es una marca de porcelana de disilicato de litio. Es resistente y deja pasar la luz de forma parecida al esmalte natural, por eso se ve real de cerca. Cada carilla se fabrica a la medida según el diseño digital de tu sonrisa.</p></section>
<section><h2>Resultados con carillas E-max</h2>
<p>Este es un caso real de la Dra. Catalina: 6 carillas superiores de porcelana E-max colocadas sin desgaste dental, en su consultorio de El Poblado, Medellín, a un paciente que viajó desde Francia. Arriba, la sonrisa de frente; abajo, el mismo paciente de perfil.</p>
{ba("caso2")}{ba("caso2b")}<p><a href="{P_BA}">Ver más casos de antes y después</a></p></section>
<section><h2>¿Cuánto cuestan las carillas E-max en Medellín?</h2>
<p>Las carillas E-max cuestan USD 380 por diente con la Dra. Catalina Beltrán en Medellín. Diez carillas para la sonrisa superior cuestan USD 3.800 y la sonrisa completa de 20 carillas, USD 5.900, es decir, USD 295 por diente. <a href="{P_PRICE}">Ver qué incluye y la comparación con Estados Unidos</a>.</p></section>
<section><h2>¿Para quién son las carillas E-max?</h2>
<p>Las carillas E-max son para quien quiere un cambio completo y duradero: dientes manchados que no mejoran con blanqueamiento, desgastados, con espacios, de formas irregulares o pequeños. También para quien tiene carillas viejas de resina y quiere pasar a porcelana.</p></section>
<section><h2>¿Cuánto duran las carillas E-max?</h2>
<p>Las carillas de porcelana E-max duran entre 10 y 20 años, e incluso más con un mantenimiento adecuado: higiene diaria, controles, no morder objetos duros y usar placa nocturna si aprietas los dientes. Son la opción más duradera del diseño de sonrisa.</p></section>
<section><h2>Ventajas y desventajas de las carillas E-max</h2>
<p>La principal ventaja de las carillas E-max es que conservan su color y duran más que la resina; la principal desventaja es que cuestan más.</p>
<table><thead><tr><th>Ventajas</th><th>Desventajas</th></tr></thead><tbody>
<tr><td>Conservan su color</td><td>Cuestan más que la resina</td></tr><tr><td>Aspecto natural de cerca</td><td>Se fabrican en laboratorio: no se hacen en una sola cita</td></tr>
<tr><td>Más duraderas que la resina</td><td>Si una se fractura, se reemplaza la pieza</td></tr><tr><td>Sin desgaste dental con la doctora</td><td>Necesitan higiene y controles como cualquier diente</td></tr></tbody></table></section>
<section><h2>¿Cuánto tiempo toma el tratamiento con carillas E-max?</h2>
<p>Si vives fuera de Colombia, las carillas E-max se hacen en un solo viaje de mínimo 4 días a Medellín, en el <a href="{P_MED}">consultorio de El Poblado</a>. Antes de viajar ya tienes la valoración, el diseño y el precio cerrado. <a href="{P_INT}">Ver cómo funciona el viaje</a>.</p></section>
<section><h2>¿Cómo se cuidan las carillas E-max?</h2><p>Las carillas E-max se cuidan con higiene diaria y controles, como los dientes naturales:</p><ul><li>Cepillado y seda dental todos los días.</li><li>Controles con la doctora (el primero, por videollamada).</li><li>No morder objetos duros ni abrir paquetes con los dientes.</li><li>Placa nocturna si aprietas o rechinas los dientes.</li></ul></section>
<section><h2>¿Qué alternativas hay?</h2><p>Si buscas menor inversión, las <a href="{P_RES}">carillas de resina</a> cuestan USD 145 por diente. Si solo quieres mejorar los bordes de tus dientes, el <a href="{P_MICRO}">microdiseño</a> es la opción más económica; para aclarar el color, revisa el <a href="{P_BLANQ}">blanqueamiento dental</a>.</p></section>""",
    related=[("Carillas de resina", P_RES), ("Antes y después", P_BA), ("Precios", P_PRICE)]))

# ---------------- RESINA ----------------
RES_FAQS = [
    ("¿Las carillas de resina se manchan?", "Pueden pigmentarse con los años, sobre todo con bebidas oscuras como el café o el vino. Un pulido en el control ayuda a mantener el brillo."),
    ("¿Se pueden cambiar después a porcelana?", "Sí. Muchas personas empiezan con resina y luego pasan a porcelana E-max. La doctora te dice cuándo conviene."),
]
PAGES.append(dict(path=P_RES, lang="es", crumb="Carillas de resina", updated="2026-11-13", og="/img/og-diseno-de-sonrisa-en-resina-caso-3.jpg", og_alt="Sonrisa después del diseño de sonrisa en resina en 12 dientes con la Dra. Catalina Beltrán en Medellín", image_obj=("/img/diseno-de-sonrisa-en-resina-despues-caso-3-910.webp", 910, 556, "Diseño de sonrisa en resina en 12 dientes de un paciente de Estados Unidos, hecho por la Dra. Catalina Beltrán en Medellín"), parents=[TRAT], schema_type="MedicalWebPage",
    title="Carillas de resina en Medellín: precio y duración",
    desc="Diseño de sonrisa en resina en Medellín: USD 145 por diente y una duración de 5 a 7 años, hasta 10 con mantenimiento. Diferencias con la porcelana E-max.",
    h1="Carillas de resina",
    lead=("Las carillas de resina son láminas ultradelgadas del color del diente que cubren cada pieza completa para cambiar su forma, tamaño y color. Las fabrica un laboratorio con equipos CNC a partir de un escáner 3D de tu boca. "
          f"Con la Dra. Catalina Beltrán en <a href='{P_MED}'>Medellín</a> cuestan USD 145 por diente, sin desgaste dental, y son la forma más económica de hacer un diseño de sonrisa completo."),
    wa=wa("carillas de resina"), faqs=RES_FAQS,
    body=f"""<section><h2>Un caso real en resina</h2><p>Este paciente viajó desde Estados Unidos para su diseño de sonrisa en resina con la Dra. Catalina Beltrán: 12 dientes, 6 superiores y 6 inferiores.</p>{ba_slider("caso3")}<p><a href="{P_BA}">Ver todos los casos de antes y después</a></p></section>
<section><h2>¿Cuánto cuesta un diseño de sonrisa en resina?</h2>
<p>El diseño de sonrisa en resina cuesta USD 145 por diente con la Dra. Catalina Beltrán en Medellín. El total depende de cuántos dientes necesitas; la doctora te lo confirma gratis por WhatsApp. <a href="{P_PRICE}">Ver todos los precios</a>.</p></section>
<section><h2>¿Qué es mejor, resina o porcelana?</h2>
<p>La porcelana E-max dura más (entre 10 y 20 años, e incluso más con buen mantenimiento) y conserva su color; la resina cuesta menos de la mitad y se puede retocar. Si buscas el resultado más duradero, conviene porcelana; si quieres un cambio completo con menor inversión, o probar un diseño, conviene resina.</p>
<table><thead><tr><th></th><th>Resina</th><th><a href="{P_EMAX}">Porcelana E-max</a></th></tr></thead><tbody>
<tr><td>Precio por diente</td><td>USD 145</td><td>USD 380</td></tr><tr><td>Color con los años</td><td>Puede pigmentarse</td><td>Lo conserva</td></tr>
<tr><td>Duración</td><td>De 5 a 7 años en promedio, hasta 10 con mantenimiento</td><td>Entre 10 y 20 años, o más</td></tr><tr><td>Si se daña</td><td>Se puede retocar</td><td>Se reemplaza la pieza</td></tr></tbody></table></section>
<section><h2>¿Cuánto dura un diseño de sonrisa en resina?</h2>
<p>Un diseño de sonrisa en resina dura en promedio de 5 a 7 años y, con un buen mantenimiento, puede llegar hasta los 10 años. Dura menos que la porcelana y con los años puede necesitar pulido o retoques. La duración depende sobre todo de la higiene, los controles y hábitos como el café o el cigarrillo. La doctora te dice qué esperar en tu caso.</p></section>
<section><h2>¿Para quién es el diseño de sonrisa en resina?</h2><p>El diseño de sonrisa en resina es para quien quiere un cambio completo con menor inversión, o quiere probar un diseño antes de pasar a porcelana. Si solo quieres mejorar los bordes de tus dientes, el <a href="{P_MICRO}">microdiseño</a> cuesta menos porque no cubre el diente completo.</p></section>
<section><h2>¿Cómo se cuidan las carillas de resina?</h2><p>Las carillas de resina se cuidan con higiene diaria, controles y pulidos cuando la doctora los indique:</p><ul><li>Cepillado y seda dental todos los días.</li><li>Pulido en los controles.</li><li>Moderar café, vino y cigarrillo.</li><li>No morder objetos duros.</li></ul></section>""",
    related=[("Carillas de porcelana E-max", P_EMAX), ("Guía de diseño de sonrisa", T), ("Precios", P_PRICE)]))

# ---------------- MICRODISEÑO ----------------
MICRO_FAQS = [
    ("¿El microdiseño desgasta los dientes?", "No. El microdiseño de sonrisa no requiere ningún tipo de desgaste dental: la resina se agrega sobre los bordes de tus dientes naturales."),
    ("¿Se puede hacer el microdiseño en porcelana?", "No. El microdiseño solo se hace en resina de alta estética, porque la doctora lo hace a mano directamente sobre tus dientes. Las carillas, en cambio, las fabrica un laboratorio."),
    ("¿Quién no es candidato para un microdiseño?", "Las personas con dientes muy desalineados. Las manchas, en cambio, se pueden corregir. La doctora te dice si eres candidato al ver 3 fotos de tu sonrisa."),
    ("¿Cuánto tiempo toma el microdiseño?", "Dos sesiones, es decir, dos días de consulta y tratamiento."),
]
PAGES.append(dict(path=P_MICRO, lang="es", crumb="Microdiseño de sonrisa", updated="2026-11-21", parents=[TRAT], schema_type="MedicalWebPage",
    title="Microdiseño de sonrisa en Medellín: sin desgaste, en 2 citas",
    desc="Microdiseño de sonrisa en Medellín con la Dra. Catalina Beltrán: resina en los bordes, sin desgaste, 6 dientes arriba y 6 abajo, en 2 citas.",
    h1="Microdiseño de sonrisa en Medellín",
    lead=("El microdiseño de sonrisa (también llamado micro diseño) mejora solo los bordes de tus dientes con resina de alta estética, sin cubrir el diente completo y sin ningún tipo de desgaste. "
          "Lo habitual es tratar los 6 dientes de arriba y los 6 de abajo que se ven al sonreír, y se hace en 2 sesiones. "
          "Con la Dra. Catalina Beltrán en Medellín es más rápido y más económico que las carillas."),
    wa=wa("microdiseño de sonrisa"), faqs=MICRO_FAQS,
    body=f"""<section><h2>¿Qué es el microdiseño de sonrisa?</h2>
<p>El microdiseño de sonrisa es un tratamiento en el que la doctora agrega resina de alta estética solo en los bordes de cada diente, a mano y directamente en el consultorio. A diferencia de las carillas, no cubre el diente completo. Con la resina se logran texturas muy naturales y, si lo deseas, un borde translúcido como el de un diente natural.</p></section>
<section><h2>¿Cuántos dientes incluye un microdiseño?</h2>
<p>Lo ideal es tratar 6 dientes arriba y 6 abajo, que son los que se ven cuando sonríes. Si tu sonrisa es más amplia y muestra más dientes, la doctora puede incluir algunos más. Te lo dice en la valoración gratis por WhatsApp.</p></section>
<section><h2>¿El microdiseño desgasta los dientes?</h2>
<p>No. El microdiseño no requiere ningún tipo de desgaste: la resina se agrega sobre tus dientes naturales, que se conservan. Es el mismo principio que sigue la Dra. Catalina en sus carillas sin desgaste dental.</p></section>
<section><h2>¿Cuánto tiempo toma el microdiseño?</h2>
<p>El microdiseño se hace en 2 sesiones, es decir, dos días de consulta y tratamiento en el <a href="{P_MED}">consultorio de El Poblado, Medellín</a>. Si vienes de otro país, escríbele por WhatsApp para organizar las 2 citas dentro de tu viaje. <a href="{P_INT}">Ver cómo funciona para pacientes internacionales</a>.</p></section>
<section><h2>¿Cuál es la diferencia entre microdiseño y carillas?</h2>
<p>Las carillas son láminas ultradelgadas que cubren el diente completo y las fabrica un laboratorio con equipos CNC a partir de un escáner 3D de tu boca. El microdiseño solo trabaja los bordes y lo hace la doctora a mano, por eso es más rápido y más económico.</p>
<table><thead><tr><th></th><th>Microdiseño</th><th><a href="{P_RES}">Carillas de resina</a></th><th><a href="{P_EMAX}">Carillas de porcelana E-max</a></th></tr></thead><tbody>
<tr><td>Qué cubre</td><td>Solo los bordes de cada diente</td><td>El diente completo</td><td>El diente completo</td></tr>
<tr><td>Cómo se hace</td><td>A mano, por la doctora</td><td>En laboratorio, con escáner 3D</td><td>En laboratorio, con escáner 3D</td></tr>
<tr><td>Material</td><td>Resina de alta estética</td><td>Resina</td><td>Disilicato de litio</td></tr>
<tr><td>Manchas</td><td>Es resina: puede pigmentarse con bebidas oscuras, como el diente natural</td><td>Puede pigmentarse, como el diente natural</td><td>No se mancha</td></tr>
<tr><td>Precio</td><td>El más económico; te lo confirma la doctora</td><td>USD 145 por diente</td><td>USD 380 por diente</td></tr>
</tbody></table>
<p>Ordenados de mayor a menor inversión: carillas de porcelana E-max, carillas de resina y microdiseño. Si quieres cambiar por completo la forma, el tamaño y el color de tus dientes, conviene una carilla; si solo quieres mejorar los bordes, el microdiseño puede ser suficiente.</p></section>
<section><h2>¿Quién puede hacerse un microdiseño?</h2>
<p>El microdiseño es para quien quiere mejorar los bordes, la forma y la textura de sus dientes sin cubrirlos por completo. No es una opción si los dientes están muy desalineados. Las manchas no son un impedimento, porque se pueden corregir. La doctora te dice si eres candidato después de ver 3 fotos de tu sonrisa por WhatsApp.</p></section>
<section><h2>¿Cuánto cuesta un microdiseño de sonrisa?</h2>
<p>El microdiseño cuesta menos que las carillas de resina, que valen USD 145 por diente. El precio depende de cada paciente; la Dra. Catalina te lo confirma gratis por WhatsApp después de ver 3 fotos de tu sonrisa. Si vives en Colombia, pide tu precio en pesos. <a href="{P_PRICE}">Ver todos los precios</a>.</p></section>
<section><h2>¿Quién hace el microdiseño?</h2>
<p>La Dra. Catalina Beltrán, odontóloga estética con 15 años de experiencia, hace personalmente cada microdiseño en su consultorio de El Poblado.</p>
{DOCTOR_ES}</section>""",
    related=[("Carillas de resina", P_RES), ("Guía de diseño de sonrisa", T), ("Precios", P_PRICE)]))

# ---------------- BLANQUEAMIENTO (BORRADOR) ----------------
BLANQ_FAQS = [
    ("¿El blanqueamiento funciona sobre carillas o coronas?", "No. El blanqueamiento solo aclara dientes naturales libres de otros materiales; no cambia el color de coronas, carillas, lentes ni otras restauraciones."),
    ("¿Puedo blanquearme los dientes en casa sin supervisión?", "No es recomendable. Usado de forma inadecuada, el producto puede causar hipersensibilidad y dañar el esmalte; por eso la Dra. Catalina hace una valoración previa y acompaña el proceso antes, durante y después."),
    ("¿Sirve para manchas por medicamentos o de origen genético?", "No. El blanqueamiento no tiene efecto en manchas de origen genético ni en las causadas por medicamentos."),
]
PAGES.append(dict(path=P_BLANQ, lang="es", crumb="Blanqueamiento dental", updated="2026-11-21", parents=[TRAT], schema_type="MedicalWebPage",
    title="Blanqueamiento dental en Medellín: precio y cuánto dura",
    desc="Blanqueamiento dental en Medellín con la Dra. Catalina Beltrán: COP 650.000 con limpieza, 2 sesiones el mismo día. Cuántos tonos aclara y cuánto dura.",
    h1="Blanqueamiento dental en Medellín",
    lead=("El blanqueamiento dental en consultorio, o aclaramiento dental, aclara el color de tus dientes naturales con supervisión profesional. "
          "El resultado depende del color de base: en los dientes amarillos es muy probable un resultado excelente, en los marrones el cambio es menor y los grisáceos rara vez mejoran. "
          "Con la Dra. Catalina Beltrán en El Poblado, Medellín, se hace en 2 sesiones el mismo día, incluye limpieza y cuesta COP 650.000."),
    wa=wa("blanqueamiento dental"), faqs=BLANQ_FAQS,
    body=f"""<section><h2>¿Qué es el blanqueamiento dental en consultorio?</h2>
<p>Es un tratamiento que rompe las manchas del diente en fragmentos más pequeños, de modo que el color se ve más claro. La Dra. Catalina lo llama aclaramiento dental. Se hace con diagnóstico previo y con acompañamiento antes, durante y después.</p>
<div class="video"><iframe src="https://www.youtube-nocookie.com/embed/bUBDaLC4lJk?rel=0" title="Blanqueamiento dental en consultorio con la Dra. Catalina Beltrán" width="560" height="315" loading="lazy" allow="encrypted-media; picture-in-picture" allowfullscreen></iframe></div></section>
<section><h2>¿Cuántos tonos se aclaran con un blanqueamiento?</h2>
<p>Depende del color de base de tus dientes. En los dientes amarillos es muy probable un resultado excelente; en los marrones el cambio es algo menos notorio, de uno a uno y medio tonos; y en los grisáceos es muy poco frecuente que mejoren.</p>
<table><thead><tr><th>Color de base</th><th>Qué esperar</th></tr></thead><tbody>
<tr><td>Amarillo</td><td>Es muy probable un resultado excelente</td></tr>
<tr><td>Marrón</td><td>Cambio algo menos notorio: de uno a uno y medio tonos</td></tr>
<tr><td>Gris</td><td>Es muy poco frecuente que mejore</td></tr>
<tr><td>Manchas genéticas o por medicamentos</td><td>El blanqueamiento no tiene efecto</td></tr>
</tbody></table></section>
<section><h2>¿Cómo es el procedimiento y cuánto tiempo toma?</h2>
<p>El blanqueamiento se hace en 2 sesiones el mismo día en el consultorio de El Poblado, e incluye una limpieza dental. Antes, la doctora hace la valoración para confirmar que eres candidato y qué resultado puedes esperar según el color de tus dientes.</p></section>
<section><h2>¿Cuánto dura un blanqueamiento dental?</h2>
<p>El resultado de un blanqueamiento dura en promedio entre 1 y 3 años. No es un tratamiento permanente: cuánto se mantiene depende de tus hábitos.</p></section>
<section><h2>¿Quién puede hacerse un blanqueamiento dental?</h2>
<p>No todas las personas son candidatas, por eso siempre hay una valoración previa. El blanqueamiento solo funciona en dientes naturales libres de otros materiales: no aclara coronas, carillas, lentes ni restauraciones.</p></section>
<section><h2>¿El blanqueamiento da sensibilidad?</h2>
<p>Puede darla. El producto, usado de forma inadecuada, puede causar hipersensibilidad y dañar el esmalte; por eso se usan productos desensibilizantes antes, durante y después del tratamiento. En algunos casos la sensibilidad obliga a suspender el aclaramiento, aunque en ciertas situaciones se puede tratar.</p></section>
<section><h2>¿Qué cuidados hay después del blanqueamiento?</h2>
<ul><li>No tomar bebidas oscuras.</li>
<li>Evitar alimentos que te causen sensibilidad justo después del procedimiento.</li>
<li>Seguir usando el desensibilizante que te indique la doctora.</li>
<li>No hacer ningún blanqueamiento por tu cuenta sin supervisión profesional.</li></ul></section>
<section><h2>¿Blanqueamiento o carillas?</h2>
<p>El blanqueamiento aclara el color pero no cambia la forma ni el tamaño de los dientes. Si además quieres cambiar la forma, conviene un diseño de sonrisa con <a href="{P_RES}">carillas de resina</a> o <a href="{P_EMAX}">carillas de porcelana E-max</a>; y si vas a hacerte carillas, conviene blanquear antes para elegir el tono final. <a href="{T}">Compara todas las opciones en la guía de diseño de sonrisa</a>.</p></section>
<section><h2>¿Cuánto cuesta un blanqueamiento dental en Medellín?</h2>
<p>El blanqueamiento dental con la Dra. Catalina Beltrán cuesta COP 650.000 e incluye la limpieza y las 2 sesiones. Antes de agendar, envía 3 fotos de tu sonrisa por WhatsApp: la doctora revisa si eres candidato y qué resultado puedes esperar. Puedes pagar en efectivo, por transferencia o con tarjeta. <a href="{P_PRICE}">Ver los precios de carillas y diseño de sonrisa</a>.</p></section>
<section><h2>¿Quién hace el blanqueamiento?</h2>
<p>La Dra. Catalina Beltrán, odontóloga estética, en su consultorio de El Poblado, Medellín.</p>
{DOCTOR_ES}</section>""",
    related=[("Guía de diseño de sonrisa", T), ("Carillas de resina", P_RES), ("Precios", P_PRICE)]))

# ---------------- PRECIOS ----------------
PRICE_FAQS = [
    ("¿Cuánto vale un diseño de sonrisa en dólares?", "Una sonrisa superior de 10 carillas de porcelana E-max cuesta USD 3.800 y la sonrisa completa de 20 carillas, USD 5.900, que equivale a USD 295 por diente."),
    ("¿Puedo pagar en pesos colombianos?", "Sí. La doctora te confirma el valor en pesos por WhatsApp. Puedes pagar en efectivo, por transferencia bancaria o con tarjeta."),
]
PAGES.append(dict(path=P_PRICE, lang="es", alt="/en/cost-of-veneers-colombia/", crumb="Precios", schema_type="WebPage",
    title="¿Cuánto cuesta un diseño de sonrisa en Colombia? Precio 2026",
    desc="Precios reales de diseño de sonrisa en Colombia: porcelana E-max USD 380, resina USD 145, 20 carillas USD 5.900. Qué incluye y comparación con EE. UU.",
    h1="¿Cuánto cuesta un diseño de sonrisa en Colombia?",
    lead=("Con la Dra. Catalina Beltrán, en Medellín, una sonrisa completa de 20 carillas de porcelana E-max cuesta USD 5.900, es decir, USD 295 por diente. "
          "La carilla de porcelana suelta cuesta USD 380 y la de resina USD 145. El precio es cerrado y lo sabes antes de empezar."),
    wa=wa("precios"), faqs=PRICE_FAQS,
    body=f"""<section><h2>Precios de referencia 2026</h2><p>En 2026, con la Dra. Catalina Beltrán en Medellín, la carilla de porcelana E-max cuesta USD 380 por diente, la de resina USD 145 y la sonrisa completa de 20 carillas de porcelana USD 5.900.</p>{PRICE_TABLE_ES}
<p class="muted">Precios vigentes al {fecha_es(UPDATED)}. Tu precio exacto depende de cuántos dientes necesitas: la doctora te lo confirma gratis por WhatsApp.</p></section>
<section><h2>¿Qué incluye el precio?</h2><p>El precio incluye la valoración y el diseño digital, las carillas sin desgaste dental, la limpieza previa y el control por videollamada. No incluye vuelos ni hotel.</p>{INCLUDES_ES}<p>Si vives fuera de Colombia, <a href="{P_INT}">así funciona el viaje</a>.</p></section>
<section><h2>¿Qué resultado obtienes por ese precio?</h2>
<p>Este es un caso real de 6 carillas superiores de porcelana E-max de la Dra. Catalina, del tipo de tratamiento que se cotiza con precio cerrado en dólares. El precio exacto de tu caso depende de cuántos dientes necesitas.</p>
{ba_page("caso2", "precio-carillas-emax-colombia-antes.webp", "precio-carillas-emax-colombia-despues.webp",
 "Sonrisa antes de carillas de porcelana E-max cotizadas con precio cerrado", "Resultado de carillas de porcelana E-max sin desgaste con precio cerrado en dólares, Medellín, Colombia",
 "Resultado real de carillas E-max sin desgaste en Medellín, con precio cerrado antes de empezar.")}</section>
<section><h2>¿Cuánto cuesta en Colombia frente a Estados Unidos?</h2>
<p>Una carilla de porcelana cuesta USD 380 con la Dra. Catalina en Medellín, frente a USD 925 a 2.500 en Estados Unidos según MedicineNet. La de resina cuesta USD 145, frente a USD 250 a 1.500.</p>
<table><thead><tr><th>Tratamiento</th><th>EE. UU. (rango publicado)</th><th>Dra. Catalina, Medellín</th></tr></thead><tbody>
<tr><td>Carilla de porcelana</td><td>USD 925–2.500</td><td>USD 380</td></tr><tr><td>Carilla de resina</td><td>USD 250–1.500</td><td>USD 145</td></tr></tbody></table>
<p class="muted">Rangos de Estados Unidos: <a href="https://www.medicinenet.com/how_much_do_teeth_veneers_cost/article.htm" rel="noopener">MedicineNet, “How Much Do Teeth Veneers Cost?”</a>, consultado el {fecha_es(UPDATED)}.</p></section>
<section><h2>¿Por qué varía tanto el precio de una clínica a otra?</h2>
<p>Cambia según el material (resina o porcelana), la marca de la porcelana, cuántos dientes se tratan, si hay que tratar caries o encías antes y si incluye diseño digital y controles. Al comparar, pregunta siempre qué incluye el precio y si es cerrado. Para elegir material, mira <a href="{P_RES}">resina o porcelana: cuál conviene</a>.</p></section>""",
    related=[("Diseño de sonrisa en Medellín", P_MED), ("Carillas de porcelana E-max", P_EMAX), ("Carillas de resina", P_RES)]))

# ---------------- DRA ----------------
PAGES.append(dict(path=P_DRA, lang="es", alt="/en/dr-catalina-beltran/", crumb="Dra. Catalina Beltrán", schema_type="ProfilePage", byline=False,
    title="Dra. Catalina Beltrán | Odontóloga estética, RETHUS 2011",
    desc="Dra. Catalina Beltrán: odontóloga con 15 años de experiencia, especialista en Estética Dental, RETHUS desde 2011. Consultorio en El Poblado, Medellín.",
    h1="Dra. Catalina Beltrán",
    lead=("La Dra. Catalina Beltrán es odontóloga con 15 años de experiencia, registrada en el RETHUS desde 2011 y especialista en Estética Dental. "
          "Atiende personalmente a cada paciente en su consultorio de El Poblado, Medellín."),
    wa=wa("perfil de la Dra."), image="/img/dra-catalina-beltran-odontologa-estetica-medellin.webp",
    body=f"""<img src="/img/dra-catalina-beltran-odontologa-estetica-medellin.webp" width="900" height="1200" alt="Dra. Catalina Beltrán, odontóloga estética" style="max-width:360px;border-radius:16px;margin:18px 0">
<section><h2>Formación</h2><p>La Dra. Catalina Beltrán es odontóloga con énfasis en ciencias quirúrgicas, especialista en Estética Dental y registrada en el RETHUS desde 2011.</p><table><tbody>
<tr><td>Odontóloga con énfasis en ciencias quirúrgicas</td><td>Colegio Odontológico Colombiano</td></tr>
<tr><td>Especialista en Estética Dental</td><td>Federación Odontológica Colombiana</td></tr>
<tr><td>Especialización en Auditoría y Garantía de Calidad en Salud</td><td>Universidad EAN</td></tr>
<tr><td>Registro profesional</td><td>RETHUS, desde 2011</td></tr></tbody></table></section>
<p>Si estás eligiendo odontóloga, revisa <a href="{P_MEJOR}">qué conviene verificar antes de un diseño de sonrisa en Medellín</a>.</p>
<section><h2>Cómo trabaja</h2><p>Revisa personalmente las fotos de cada paciente, diseña la sonrisa según la cara, el tono de piel y la mordida, y da un precio cerrado antes de empezar. Trabaja carillas sin desgaste dental y atiende en español e inglés.</p></section>
<section><h2>Pacientes</h2><p>Calificación de 5,0 en Google.</p>{PATIENTS_ES}</section>
<section><h2>Tratamientos</h2><p>La Dra. Catalina Beltrán hace diseños de sonrisa con carillas de porcelana E-max y carillas de resina, sin desgaste dental.</p><div class="related"><a href="{P_EMAX}">Carillas de porcelana E-max</a><a href="{P_RES}">Carillas de resina</a><a href="{T}">Guía de diseño de sonrisa</a></div></section>
<section><h2>Consultorio</h2><p>{ADDRESS}. <a href="{P_CONT}">Contacto y mapa</a> · <a href="{INSTAGRAM}">Instagram</a></p></section>""",
    related=[("Diseño de sonrisa en Medellín", P_MED), ("Antes y después", P_BA)]))

# ---------------- ANTES Y DESPUÉS ----------------
PAGES.append(dict(path=P_BA, lang="es", crumb="Antes y después", schema_type="WebPage",
    title="Diseño de sonrisa antes y después | Casos reales en Medellín",
    desc="Fotos reales de antes y después de diseño de sonrisa en Medellín con la Dra. Catalina Beltrán, y el video de un paciente al ver su nueva sonrisa.",
    h1="Diseño de sonrisa: antes y después",
    lead="Estos son casos reales de pacientes de la Dra. Catalina Beltrán en Medellín, publicados con su autorización. Cada sonrisa se diseñó según la cara, el tono de piel y la mordida de cada persona.",
    wa=wa("antes y después"), video=True,
    body=f"""<section><h2>Caso 1: diseño de sonrisa</h2><p>Caso real de diseño de sonrisa de la Dra. Catalina Beltrán en Medellín: la forma, el tamaño y el color de los dientes cambian en proporción con la cara del paciente.</p>{ba("caso1")}</section>
<section><h2>Caso 2: carillas de porcelana E-max sin desgaste</h2><p>Caso real de 6 carillas superiores de porcelana E-max sin desgaste dental de la Dra. Catalina Beltrán, visto de frente y de perfil. El paciente viajó desde Francia.</p>{ba("caso2")}{ba("caso2b")}<p><a href="{P_EMAX}">Qué son las carillas E-max y cuánto cuestan</a></p></section>
<section><h2>El momento en que se ve por primera vez</h2><p>Este paciente viajó desde Estados Unidos a Medellín para su diseño de sonrisa con la Dra. Catalina. El video lo muestra en el consultorio de El Poblado, al terminar el tratamiento, cuando se mira por primera vez.</p>{VIDEO_ES}</section>
<section><h2>Pacientes que viajaron a Medellín por su sonrisa</h2><p>Pacientes de Estados Unidos, Italia y otras ciudades de Colombia se han hecho su diseño de sonrisa con la Dra. Catalina Beltrán en Medellín.</p>{PATIENTS_ES}</section>
<p class="note">Los resultados varían según cada caso. La doctora te dice qué es posible en el tuyo después de ver tus fotos.</p>""",
    related=[("Carillas de porcelana E-max", P_EMAX), ("Precios", P_PRICE), ("Diseño de sonrisa en Medellín", P_MED)]))

# ---------------- INTERNACIONALES ----------------
INT_FAQS = [
    ("¿Cuántos días necesito en Medellín?", "Mínimo 4 días, en un solo viaje."),
    ("¿Necesito radiografías para la cotización?", "No. Para el precio exacto bastan 3 fotos tomadas con tu celular; la doctora te indica cómo."),
    ("¿El precio puede cambiar al llegar?", "No. El precio es cerrado y lo conoces antes de comprar el vuelo."),
]
PAGES.append(dict(path=P_INT, lang="es", crumb="Pacientes internacionales", schema_type="WebPage",
    title="Diseño de sonrisa en Colombia para extranjeros | 4 días",
    desc="Diseño de sonrisa en Medellín para pacientes del exterior: precio cerrado en dólares antes de viajar, un solo viaje de 4 días y control por videollamada.",
    h1="Diseño de sonrisa para pacientes internacionales",
    lead=("Si vives fuera de Colombia, recibes la valoración y el precio cerrado en dólares por WhatsApp antes de comprar el vuelo, y haces tu diseño de sonrisa en un solo viaje de mínimo 4 días a Medellín. "
          "El control posterior es por videollamada."),
    wa=wa("pacientes internacionales"), faqs=INT_FAQS, video=True,
    body=f"""<section><h2>¿Cómo funciona el diseño de sonrisa si vives fuera de Colombia?</h2><p>Todo se coordina por WhatsApp antes de viajar, y el tratamiento se hace en un solo viaje de mínimo 4 días a Medellín.</p><ol>
<li><b>Escríbele por WhatsApp</b> desde tu país. Cuéntale qué quieres cambiar y envía 3 fotos con tu celular.</li>
<li><b>Recibe tu valoración y tu precio cerrado</b> en dólares. Si prefieres, por videollamada.</li>
<li><b>Compra tu vuelo</b> sabiendo exactamente cuánto vas a pagar.</li>
<li><b>Viaja a Medellín</b> mínimo 4 días. La doctora ya tiene tu diseño planificado.</li>
<li><b>Vuelve a casa</b> con tu sonrisa terminada. El control es por videollamada.</li></ol></section>
<section><h2>¿Cuánto cuesta un diseño de sonrisa para pacientes del exterior?</h2><p>Con la Dra. Catalina Beltrán, el precio es cerrado y en dólares. {PRICE_LINE}</p>{INCLUDES_ES}</section>
<section><h2>¿Dónde hospedarse en Medellín durante el tratamiento?</h2><p>Lo más práctico es hospedarse en El Poblado, donde queda el consultorio. Recomendamos el hotel Ibis Medellín, a 300 m del consultorio.</p></section>
<section><h2>¿Cómo es el control después de volver a tu país?</h2><p>El control posterior se hace por videollamada con la Dra. Catalina Beltrán.</p></section>
<section><h2>Un paciente de Estados Unidos al ver su nueva sonrisa</h2><p>Este paciente viajó desde Estados Unidos a Medellín para su diseño de sonrisa con la Dra. Catalina. El video lo muestra en el consultorio de El Poblado, al terminar el tratamiento, cuando se mira por primera vez.</p>{VIDEO_ES}</section>""",
    related=[("Precios", P_PRICE), ("Diseño de sonrisa en Medellín", P_MED), ("Veneers in Medellín (English)", "/en/veneers-medellin/")]))

# ---------------- CONTACTO ----------------
PAGES.append(dict(path=P_CONT, lang="es", crumb="Contacto", schema_type="ContactPage", byline=False,
    title="Contacto | Dra. Catalina Beltrán, El Poblado, Medellín",
    desc=f"Consultorio de la Dra. Catalina Beltrán: {ADDRESS}. WhatsApp {PHONE}.",
    h1="Contacto", lead=f"Escríbele a la Dra. Catalina por WhatsApp al {PHONE}. El consultorio queda en {ADDRESS}.",
    wa=wa("contacto"),
    body=f"""<section><h2>Consultorio en Medellín</h2><p>{ADDRESS}, Antioquia, Colombia.</p>{MAP}</section>
<section><h2>Otros canales</h2><ul><li>WhatsApp: <a href="{{WA}}">{PHONE}</a></li><li>Correo: <a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="{INSTAGRAM}">Instagram @dracatalinabeltran</a></li></ul></section>""",
    related=[("Diseño de sonrisa en Medellín", P_MED), ("Pacientes internacionales", P_INT)]))

# ---------------- PRIVACIDAD ----------------
PAGES.append(dict(path="/privacidad/", lang="es", crumb="Privacidad", byline=False, no_top_cta=True,
    title="Política de privacidad | Dra. Catalina Beltrán", desc="Política de privacidad y tratamiento de datos del sitio de la Dra. Catalina Beltrán.",
    h1="Política de privacidad y tratamiento de datos", wa=wa("privacidad"),
    body=f"""<p class="muted">Última actualización: {fecha_es(UPDATED)}</p>
<h2>Responsable</h2><p>Dra. Catalina Beltrán, consultorio de odontología estética. {ADDRESS}, Colombia. WhatsApp: {PHONE}. Correo: {EMAIL}.</p>
<h2>Qué datos recogemos</h2><p>Este sitio no pide nombre, teléfono ni correo. Para saber qué páginas son útiles, registra datos técnicos anónimos de la visita (página, país aproximado por zona horaria, tipo de dispositivo, tiempo en la página) y un código de referencia que viaja en tu mensaje si haces clic en WhatsApp. Si nos escribes por WhatsApp, recibimos los datos que tú decides enviarnos, como tu nombre, número o fotos de tu sonrisa.</p>
<h2>Para qué los usamos</h2><p>Para responder tu solicitud, hacer tu valoración, darte un presupuesto, hacer seguimiento a tu caso y mejorar este sitio. No vendemos ni compartimos tus datos con terceros para fines comerciales. Tus fotos y datos de salud solo los ve el equipo del consultorio y no se usan en publicidad sin tu autorización expresa y por escrito.</p>
<h2>Tus derechos</h2><p>De acuerdo con la Ley 1581 de 2012 y el Decreto 1377 de 2013 de Colombia, puedes conocer, actualizar, rectificar y pedir que eliminemos tus datos, así como revocar tu autorización. Escríbenos por WhatsApp o al correo indicado y te respondemos en un máximo de 15 días hábiles.</p>
<h2>Cuánto tiempo los guardamos</h2><p>Mientras sean necesarios para tu atención y por el tiempo que exige la normatividad colombiana para historias clínicas.</p>"""))

# Imagen para compartir (og:image) y foto principal de cada página (la convierte en ImageObject build.py)
OG_ES = {
    "/": dict(image="/img/diseno-de-sonrisa-medellin-despues-caso-1.webp"),
    P_MED: dict(updated="2026-11-16", og="/img/og-diseno-de-sonrisa-medellin.jpg",
                og_alt="Antes y después de carillas de porcelana E-max sin desgaste con la Dra. Catalina Beltrán en El Poblado, Medellín",
                image_caption="Paciente de Estados Unidos se ve por primera vez después de su diseño de sonrisa en Medellín"),
    T: dict(updated="2026-11-21", og="/img/og-que-es-diseno-de-sonrisa.jpg", image="/img/que-es-diseno-de-sonrisa-despues.webp",
            og_alt="Antes y después de un diseño de sonrisa hecho por la Dra. Catalina Beltrán en Medellín"),
    P_EMAX: dict(og="/img/og-carillas-de-porcelana-emax.jpg",
                 og_alt="Antes y después de carillas de porcelana E-max sin desgaste, caso real de la Dra. Catalina Beltrán"),
    P_PRICE: dict(updated="2026-11-16", og="/img/og-precio-diseno-de-sonrisa-colombia.jpg", image="/img/precio-carillas-emax-colombia-despues.webp",
                  og_alt="Antes y después de carillas de porcelana E-max y el precio de 20 carillas por USD 5.900"),
    P_DRA: dict(og="/img/og-dra-catalina-beltran.jpg", og_alt="Dra. Catalina Beltrán, odontóloga estética en Medellín"),
    P_BA: dict(updated="2026-11-16", og="/img/og-antes-y-despues-diseno-de-sonrisa.jpg", image="/img/diseno-de-sonrisa-medellin-despues-caso-1.webp",
               og_alt="Antes y después de un diseño de sonrisa, caso real de la Dra. Catalina Beltrán en Medellín"),
    P_INT: dict(updated="2026-11-16", og="/img/og-pacientes-internacionales.jpg",
                og_alt="Paciente de Estados Unidos junto a la Dra. Catalina Beltrán en su consultorio de Medellín"),
    P_CONT: dict(og="/img/og-contacto-dra-catalina-beltran.jpg",
                 og_alt="Dra. Catalina Beltrán, odontóloga estética, consultorio en El Poblado, Medellín",
                 image_caption="Dra. Catalina Beltrán, odontóloga estética en Medellín"),
}
for _p in PAGES:
    _p.update(OG_ES.get(_p["path"], {}))

for _p in PAGES:
    if _p["path"] in (P_EMAX, P_RES):
        _p["updated"] = "2026-11-16"

for _p in PAGES:
    if _p["path"] in ("/", P_DRA):
        _p["updated"] = "2026-11-16"
