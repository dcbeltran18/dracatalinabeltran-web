"""Páginas en español. Cada H2 es una pregunta real de Google respondida primero.
Marcas [REVISAR] en comentarios = afirmaciones clínicas que la doctora debe confirmar."""
from common import *

T = "/diseno-de-sonrisa/"
P_EMAX = T + "carillas-de-porcelana-emax/"
P_RES = T + "carillas-de-resina/"
P_MICRO = T + "microdiseno-de-sonrisa/"
P_BLANQ = T + "blanqueamiento-dental/"
P_MED = "/diseno-de-sonrisa-medellin/"
P_PRICE = "/precio-diseno-de-sonrisa-colombia/"
P_DRA = "/dra-catalina-beltran/"
P_BA = "/antes-y-despues/"
P_INT = "/pacientes-internacionales/"
P_FAQ = "/preguntas-frecuentes/"
P_CONT = "/contacto/"

TRAT = ("Tratamientos", T)
def wa(t): return f"Hola Dra. Catalina 👋 Vi su página web ({t}) y quiero saber el precio de mi caso."

PAGES = []

# ---------------- INICIO ----------------
HOME_FAQS = [
    ("¿Cuánto cuesta un diseño de sonrisa con la Dra. Catalina?",
     f'La carilla de porcelana E-max cuesta USD 380 por diente y la de resina USD 145. La sonrisa completa de 20 carillas de porcelana cuesta USD 5.900. <a href="{P_PRICE}">Ver todos los precios</a>.'),
    ("¿Dónde queda el consultorio?",
     f'En {ADDRESS}. La doctora también atiende en Bogotá. <a href="{P_CONT}">Ver mapa y contacto</a>.'),
    ("¿Las carillas desgastan los dientes?",
     f'La Dra. Catalina trabaja carillas sin desgaste dental. Si tu caso necesitara otra cosa, te lo explica antes de empezar. <a href="{P_EMAX}">Más sobre las carillas E-max</a>.'),
    ("¿Puedo hacerme el tratamiento si vivo en otro país?",
     f'Sí. Recibes la valoración y el precio cerrado por WhatsApp, y viajas una sola vez, mínimo 4 días. <a href="{P_INT}">Cómo funciona para pacientes internacionales</a>.'),
    ("¿Qué es mejor, porcelana o resina?",
     f'La porcelana E-max dura más y conserva su color; la resina es más económica. <a href="{T}">Comparar todos los tratamientos</a>.'),
]
PAGES.append(dict(path="/", lang="es", byline=False,
    title="Dra. Catalina Beltrán | Odontóloga estética y diseño de sonrisa en Medellín",
    desc="Diseño de sonrisa y carillas sin desgaste dental en El Poblado, Medellín. Porcelana E-max desde USD 380 por diente. 15 años de experiencia, 5,0 en Google. Valoración gratis por WhatsApp.",
    h1="Dra. Catalina Beltrán, odontóloga estética en Medellín",
    lead=("La Dra. Catalina Beltrán hace diseños de sonrisa con carillas de porcelana E-max y de resina, sin desgaste dental, en su consultorio de El Poblado, Medellín. "
          "Tiene 15 años de experiencia, calificación de 5,0 en Google y precios publicados en dólares: desde USD 145 por diente en resina y USD 5.900 por una sonrisa completa de 20 carillas de porcelana."),
    wa="Hola Dra. Catalina 👋 Vi su página web y quiero saber el precio de mi diseño de sonrisa.",
    faqs=HOME_FAQS,
    body=f"""<div class="cards"><div class="card"><b>5,0</b><span>Calificación en Google</span></div><div class="card"><b>15 años</b><span>de experiencia</span></div>
<div class="card"><b>2011</b><span>Registrada en el RETHUS</span></div><div class="card"><b>USD 295</b><span>por diente en sonrisa completa de porcelana</span></div></div>
<section><h2>Tratamientos de diseño de sonrisa</h2>
<p>La doctora te recomienda el tratamiento según lo que quieres cambiar, tu presupuesto y el estado de tus dientes. <a href="{T}">Ver la guía completa de diseño de sonrisa</a>.</p>
<div class="cards">
<a class="card" href="{P_EMAX}"><b>Porcelana E-max</b><span>La opción más duradera. USD 380 por diente.</span></a>
<a class="card" href="{P_RES}"><b>Resina</b><span>La opción más económica. USD 145 por diente.</span></a>
<a class="card" href="{P_MICRO}"><b>Microdiseño</b><span>Corrige detalles en pocos dientes.</span></a>
<a class="card" href="{P_BLANQ}"><b>Blanqueamiento</b><span>Aclara el color de tus dientes naturales.</span></a></div></section>
<section><h2>Precios de referencia</h2>{PRICE_TABLE_ES}
<p><a href="{P_PRICE}">Qué incluye cada precio y cómo se compara con Estados Unidos</a></p></section>
<section><h2>Resultados reales</h2>{ba("caso1")}
<p>Cada sonrisa se diseña según la cara, el tono de piel y la mordida de cada paciente. <a href="{P_BA}">Ver más casos de antes y después</a>.</p></section>
<section><h2>Cómo funciona</h2><ol>
<li><b>Escríbele por WhatsApp.</b> Cuéntale qué te gustaría cambiar. Para un precio exacto le envías 3 fotos con tu celular; no necesitas radiografías.</li>
<li><b>Recibe tu valoración.</b> La doctora te dice qué opción te conviene, cuántos dientes tratar y el precio cerrado. Si prefieres, por videollamada.</li>
<li><b>Haz tu tratamiento.</b> La doctora planifica tu diseño antes de empezar. Si vienes de otro país, viajas una sola vez, mínimo 4 días: <a href="{P_INT}">así funciona para pacientes internacionales</a>.</li></ol></section>
<section><h2>Tu odontóloga</h2>{DOCTOR_ES}</section>
<section><h2>Opiniones de pacientes</h2><p>La Dra. Catalina tiene una calificación de 5,0 en Google. Atiende pacientes de Colombia, Estados Unidos, Europa y Latinoamérica.</p>{PATIENTS_ES}</section>
<section><h2>Dónde atiende</h2><p>Consultorio en {ADDRESS}. La doctora también atiende en Bogotá.</p>
<p><a href="{P_MED}">Diseño de sonrisa en Medellín</a> · <a href="{P_CONT}">Contacto y mapa</a></p></section>""",
    related=[("Preguntas frecuentes", P_FAQ), ("Diseño de sonrisa en Medellín", P_MED), ("Precios", P_PRICE)]))

# ---------------- MEDELLÍN ----------------
MED_FAQS = [
    ("¿Cuál es el mejor lugar para hacerse un diseño de sonrisa en Medellín?",
     "Busca una odontóloga registrada en el RETHUS, que publique sus precios, muestre casos reales y te dé un plan cerrado antes de empezar. La Dra. Catalina Beltrán cumple esos cuatro puntos y tiene 5,0 en Google."),
    ("¿Se puede pagar a cuotas?",
     "Escríbele a la doctora por WhatsApp y te explica las formas de pago disponibles para tu caso."),
    ("¿Atienden en inglés?", "Sí. La doctora atiende en español e inglés, por WhatsApp y en el consultorio."),
]
PAGES.append(dict(path=P_MED, lang="es", alt="/en/veneers-medellin/", crumb="Diseño de sonrisa en Medellín", schema_type="MedicalWebPage",
    title="Diseño de sonrisa en Medellín | Carillas sin desgaste en El Poblado",
    desc="Diseño de sonrisa en Medellín con la Dra. Catalina Beltrán: carillas de porcelana E-max desde USD 380 y de resina desde USD 145, sin desgaste dental, en El Poblado. Valoración gratis.",
    h1="Diseño de sonrisa en Medellín",
    lead=("En Medellín, la Dra. Catalina Beltrán hace diseños de sonrisa con carillas de porcelana E-max (USD 380 por diente) y de resina (USD 145 por diente), sin desgaste dental, "
          "en su consultorio de El Poblado. Recibes el precio cerrado antes de empezar y la valoración es gratis por WhatsApp."),
    wa=wa("diseño de sonrisa Medellín"), faqs=MED_FAQS, image="/img/caso1-despues-600.webp",
    body=f"""<section><h2>¿Cuánto cuesta un diseño de sonrisa en Medellín?</h2>
<p>Con la Dra. Catalina, una sonrisa completa de 20 carillas de porcelana E-max cuesta USD 5.900, es decir, USD 295 por diente. Diez carillas de porcelana para la sonrisa superior cuestan USD 3.800. La carilla de resina cuesta USD 145 por diente.</p>
{PRICE_TABLE_ES}<p>Incluye valoración y diseño digital, limpieza previa y control por videollamada. <a href="{P_PRICE}">Ver el detalle de precios</a>.</p></section>
<section><h2>¿Qué tipos de diseño de sonrisa hay?</h2>
<table><thead><tr><th>Opción</th><th>Para qué sirve</th><th>Precio</th></tr></thead><tbody>
<tr><td><a href="{P_EMAX}">Carillas de porcelana E-max</a></td><td>Cambio completo, duradero y que conserva su color</td><td>USD 380 por diente</td></tr>
<tr><td><a href="{P_RES}">Carillas de resina</a></td><td>Cambio completo con menor inversión</td><td>USD 145 por diente</td></tr>
<tr><td><a href="{P_MICRO}">Microdiseño de sonrisa</a></td><td>Corregir detalles en pocos dientes</td><td>Según número de dientes</td></tr>
<tr><td><a href="{P_BLANQ}">Blanqueamiento dental</a></td><td>Aclarar el color de los dientes naturales</td><td>Por WhatsApp</td></tr></tbody></table></section>
<section><h2>¿Cómo es el proceso?</h2>
<p>Primero le escribes a la doctora por WhatsApp y le envías 3 fotos con tu celular. Ella te dice qué opción te conviene, cuántos dientes tratar y el precio cerrado; si prefieres, lo hacen por videollamada. Luego planifica tu diseño digital antes de tocar un diente, y en el consultorio hace la limpieza previa y el tratamiento. Al terminar, el control se hace por videollamada.</p></section>
<section><h2>Resultados en Medellín</h2>{ba("caso1")}{ba("caso2")}<p><a href="{P_BA}">Ver todos los casos</a></p></section>
<section><h2>¿Por qué elegir a la Dra. Catalina en Medellín?</h2>
<ul><li>Precio cerrado antes de empezar, publicado en dólares.</li><li>Carillas sin desgaste dental.</li><li>Atención personal de la doctora, en español e inglés.</li>
<li>15 años de experiencia y registro en el RETHUS desde 2011.</li><li>Consultorio en El Poblado, una de las zonas de Medellín con más hoteles y restaurantes.</li></ul>
{DOCTOR_ES}</section>
<section><h2>¿Dónde queda el consultorio?</h2><p>{ADDRESS}. Si vienes de otro país, el hotel Ibis Medellín está a 300 m del consultorio.</p>{MAP}</section>""",
    related=[("Precio del diseño de sonrisa en Colombia", P_PRICE), ("Qué es el diseño de sonrisa", T), ("Pacientes internacionales", P_INT)]))

# ---------------- PILAR: DISEÑO DE SONRISA ----------------
PILAR_FAQS = [
    ("¿El diseño de sonrisa es bueno o malo?",
     "Es un tratamiento seguro cuando lo hace una odontóloga calificada, después de revisar la salud de tus dientes y encías. Los problemas suelen venir de tratamientos sin valoración previa o de desgastar dientes sanos sin necesidad."),
    ("¿Qué es mejor, diseño de sonrisa o microdiseño?",
     f'Depende de cuánto quieras cambiar. El microdiseño corrige pocos dientes; el diseño completo cambia toda la zona visible. <a href="{P_MICRO}">Ver microdiseño</a>.'),
    ("¿El diseño de sonrisa es lo mismo que las carillas?",
     "No exactamente. El diseño de sonrisa es el plan completo (forma, tamaño, color y proporción de los dientes según tu cara); las carillas son una de las formas de hacerlo realidad."),
]
PAGES.append(dict(path=T, lang="es", crumb="Diseño de sonrisa", schema_type="MedicalWebPage",
    title="¿Qué es el diseño de sonrisa? Tipos, precios y cuánto dura",
    desc="Qué es el diseño de sonrisa, qué tipos hay (porcelana E-max, resina, microdiseño, blanqueamiento), cuánto cuesta y cuánto dura. Guía de la Dra. Catalina Beltrán, odontóloga estética en Medellín.",
    h1="Diseño de sonrisa: qué es, tipos y precios",
    lead=("El diseño de sonrisa es un plan odontológico que define la forma, el tamaño, el color y la proporción de tus dientes según tu cara, y luego lo hace realidad con carillas de porcelana, carillas de resina, microdiseño o blanqueamiento. "
          "Con la Dra. Catalina Beltrán cuesta desde USD 145 por diente en resina y USD 380 en porcelana E-max."),
    wa=wa("diseño de sonrisa"), faqs=PILAR_FAQS,
    body=f"""<section><h2>¿Qué tipos de diseño de sonrisa hay?</h2>
<table><thead><tr><th></th><th><a href="{P_EMAX}">Porcelana E-max</a></th><th><a href="{P_RES}">Resina</a></th><th><a href="{P_MICRO}">Microdiseño</a></th><th><a href="{P_BLANQ}">Blanqueamiento</a></th></tr></thead><tbody>
<tr><td>Qué cambia</td><td>Forma, tamaño y color</td><td>Forma, tamaño y color</td><td>Detalles en pocos dientes</td><td>Solo el color</td></tr>
<tr><td>Precio</td><td>USD 380 por diente</td><td>USD 145 por diente</td><td>Según dientes</td><td>Por WhatsApp</td></tr>
<tr><td>Conserva el color</td><td>Sí</td><td>Puede pigmentarse con los años</td><td>Según material</td><td>El efecto baja con el tiempo</td></tr></tbody></table>
<p class="muted">Las diferencias de duración y color son generales; dependen de tus hábitos y cuidados. La doctora te explica qué esperar en tu caso.</p></section>
<section><h2>¿Cómo se hace un diseño de sonrisa?</h2>
<p>La doctora revisa tus fotos y la salud de tus dientes y encías. Después diseña digitalmente tu nueva sonrisa según tu cara, tu tono de piel y tu mordida, y te muestra el plan con el precio cerrado. Solo cuando lo apruebas se hace la limpieza previa y el tratamiento en el <a href="/diseno-de-sonrisa-medellin/">consultorio de El Poblado, Medellín</a>. El control posterior es por videollamada.</p></section>
<section><h2>¿Cuánto cuesta un diseño de sonrisa?</h2>
<p>Depende del material y del número de dientes. La sonrisa completa de 20 carillas de porcelana E-max cuesta USD 5.900; la sonrisa superior de 10 carillas, USD 3.800.</p>{PRICE_TABLE_ES}<p><a href="{P_PRICE}">Ver precios completos</a></p></section>
<section><h2>¿Cuánto dura un diseño de sonrisa?</h2>
<p>Depende del material: la porcelana E-max es la opción más duradera y conserva su color; la resina dura menos y puede necesitar pulido o retoques con los años. En los dos casos, la duración depende de tus cuidados: higiene diaria, controles y no morder objetos duros. La doctora te dice qué esperar según tu caso.</p></section>
<section><h2>¿Quién puede hacerse un diseño de sonrisa?</h2>
<p>Adultos con dientes y encías sanos, o que se tratan antes (por ejemplo, con la limpieza previa). Si tienes caries, enfermedad de las encías o bruxismo, la doctora lo evalúa primero y te dice si conviene tratarlo antes.</p></section>
<section><h2>Resultados</h2>{ba("caso2")}<p><a href="{P_BA}">Ver antes y después</a></p></section>""",
    related=[("Carillas de porcelana E-max", P_EMAX), ("Carillas de resina", P_RES), ("Microdiseño de sonrisa", P_MICRO), ("Blanqueamiento dental", P_BLANQ), ("Diseño de sonrisa en Medellín", P_MED)]))

# ---------------- E-MAX ----------------
EMAX_FAQS = [
    ("¿Las carillas E-max se manchan?", "No. La porcelana E-max no absorbe pigmentos como el café o el vino, por eso conserva su color."),  # [REVISAR]
    ("¿Las carillas pudren los dientes?", "No. Lo que daña un diente es la caries por mala higiene debajo o alrededor de la carilla. Con higiene diaria y controles, el diente se mantiene sano."),
    ("¿Cuándo no se pueden poner carillas?", "Cuando hay caries o enfermedad de encías sin tratar, o un bruxismo fuerte sin control. La doctora lo revisa en la valoración y, si hace falta, lo trata antes."),
]
PAGES.append(dict(path=P_EMAX, lang="es", crumb="Carillas de porcelana E-max", parents=[TRAT], schema_type="MedicalWebPage",
    title="Carillas de porcelana E-max en Medellín: precio, duración y ventajas",
    desc="Carillas de porcelana E-max sin desgaste dental en Medellín: USD 380 por diente, 20 carillas por USD 5.900. Qué son, cuánto duran, ventajas y desventajas, cuidados.",
    h1="Carillas de porcelana E-max",
    lead=("Las carillas E-max son láminas delgadas de porcelana de disilicato de litio que se adhieren al frente de los dientes para cambiar su forma, tamaño y color. "
          "Con la Dra. Catalina Beltrán en Medellín cuestan USD 380 por diente, sin desgaste dental, y la sonrisa completa de 20 carillas cuesta USD 5.900."),
    wa=wa("carillas E-max"), faqs=EMAX_FAQS, image="/img/caso1-despues-600.webp",
    body=f"""<section><h2>¿Qué son las carillas E-max?</h2>
<p>E-max es una marca de porcelana de disilicato de litio. Es resistente y deja pasar la luz de forma parecida al esmalte natural, por eso se ve real de cerca. Cada carilla se fabrica a la medida según el diseño digital de tu sonrisa.</p></section>
<section><h2>¿Cuánto cuestan las carillas E-max en Medellín?</h2>
<table><thead><tr><th>Cantidad</th><th>Precio</th></tr></thead><tbody><tr><td>1 carilla</td><td>USD 380</td></tr><tr><td>10 carillas (sonrisa superior)</td><td>USD 3.800</td></tr><tr><td>20 carillas (sonrisa completa)</td><td>USD 5.900 (USD 295 por diente)</td></tr></tbody></table>
<p>En Estados Unidos se publican rangos de USD 1.000 a 2.500 por carilla de porcelana. <a href="{P_PRICE}">Ver comparación de precios</a>.</p></section>
<section><h2>¿Para quién son?</h2>
<p>Para quien quiere un cambio completo y duradero: dientes manchados que no mejoran con blanqueamiento, desgastados, con espacios, de formas irregulares o pequeños. También para quien tiene carillas viejas de resina y quiere cambiarlas por porcelana.</p></section>
<section><h2>¿Cuánto duran las carillas E-max?</h2>
<p>Son la opción más duradera del diseño de sonrisa. Su duración depende de tus cuidados: higiene diaria, controles, no morder objetos duros y usar placa nocturna si aprietas los dientes. La doctora te explica qué esperar en tu caso.</p></section>
<section><h2>Ventajas y desventajas de las carillas E-max</h2>
<table><thead><tr><th>Ventajas</th><th>Desventajas</th></tr></thead><tbody>
<tr><td>Conservan su color</td><td>Cuestan más que la resina</td></tr><tr><td>Aspecto natural de cerca</td><td>Requieren laboratorio: no se hacen en una sola cita</td></tr>
<tr><td>Más duraderas que la resina</td><td>Si una se fractura, se reemplaza la pieza</td></tr><tr><td>Sin desgaste dental con la doctora</td><td>Necesitan higiene y controles como cualquier diente</td></tr></tbody></table></section>
<section><h2>¿Cuánto tiempo toma el tratamiento?</h2>
<p>El tratamiento se hace en el <a href="/diseno-de-sonrisa-medellin/">consultorio de Medellín</a>, en El Poblado. Si vienes de otro país, un solo viaje de mínimo 4 días. Antes del viaje ya tienes la valoración, el diseño y el precio cerrado. <a href="{P_INT}">Ver cómo funciona el viaje</a>.</p></section>
<section><h2>¿Cómo se cuidan?</h2><ul><li>Cepillado y seda dental todos los días.</li><li>Controles con la doctora (el primero, por videollamada).</li><li>No morder objetos duros ni abrir paquetes con los dientes.</li><li>Placa nocturna si aprietas o rechinas los dientes.</li></ul></section>
<section><h2>Alternativas</h2><p>Si buscas menor inversión, las <a href="{P_RES}">carillas de resina</a> cuestan USD 145 por diente. Si solo quieres corregir pocos dientes, mira el <a href="{P_MICRO}">microdiseño de sonrisa</a>. Si solo te molesta el color, empieza por el <a href="{P_BLANQ}">blanqueamiento</a>.</p></section>
<section><h2>Resultados</h2>{ba("caso1")}</section>""",
    related=[("Diseño de sonrisa: guía completa", T), ("Carillas de resina", P_RES), ("Diseño de sonrisa en Medellín", P_MED), ("Precios", P_PRICE)]))

# ---------------- RESINA ----------------
RES_FAQS = [
    ("¿Las carillas de resina se manchan?", "Pueden pigmentarse con los años, sobre todo con café, vino o cigarrillo. Un pulido en el control ayuda a mantener el brillo."),  # [REVISAR]
    ("¿Se pueden cambiar después a porcelana?", "Sí. Muchas personas empiezan con resina y luego pasan a porcelana E-max. La doctora te dice cuándo conviene."),
    ("¿El diseño de sonrisa en resina es bueno?", "Sí, cuando está bien planificado. Es una forma de lograr un cambio completo con menor inversión, aceptando que dura menos que la porcelana."),
]
PAGES.append(dict(path=P_RES, lang="es", crumb="Carillas de resina", parents=[TRAT], schema_type="MedicalWebPage",
    title="Carillas de resina en Medellín: precio, duración y diferencias",
    desc="Diseño de sonrisa en resina en Medellín: USD 145 por diente, sin desgaste dental. Cuánto dura, si se mancha, ventajas y desventajas frente a la porcelana E-max.",
    h1="Carillas de resina",
    lead=("Las carillas de resina se hacen con un material del color del diente que la doctora moldea sobre cada pieza para cambiar su forma, tamaño y color. "
          "Con la Dra. Catalina Beltrán en <a href='/diseno-de-sonrisa-medellin/'>Medellín</a> cuestan USD 145 por diente, sin desgaste dental. Son la forma más económica de hacer un diseño de sonrisa completo."),
    wa=wa("carillas de resina"), faqs=RES_FAQS,
    body=f"""<section><h2>¿Cuánto cuesta un diseño de sonrisa en resina?</h2>
<p>USD 145 por diente. El precio total depende de cuántos dientes necesitas; la doctora te lo confirma gratis por WhatsApp. <a href="{P_PRICE}">Ver todos los precios</a>.</p></section>
<section><h2>Resina o porcelana: ¿cuál conviene?</h2>
<table><thead><tr><th></th><th>Resina</th><th><a href="{P_EMAX}">Porcelana E-max</a></th></tr></thead><tbody>
<tr><td>Precio por diente</td><td>USD 145</td><td>USD 380</td></tr><tr><td>Color con los años</td><td>Puede pigmentarse</td><td>Lo conserva</td></tr>
<tr><td>Duración</td><td>Menor</td><td>Mayor</td></tr><tr><td>Reparación</td><td>Se puede retocar</td><td>Se reemplaza la pieza</td></tr></tbody></table></section>
<section><h2>¿Cuánto dura un diseño de sonrisa en resina?</h2>
<p>Dura menos que la porcelana y con los años puede necesitar pulido o retoques. La duración depende sobre todo de la higiene, los controles y hábitos como el café o el cigarrillo. La doctora te dice qué esperar en tu caso.</p></section>
<section><h2>¿Para quién es?</h2><p>Para quien quiere un cambio completo con menor inversión, o quiere probar un diseño antes de pasar a porcelana. También es útil para corregir pocos dientes en un <a href="{P_MICRO}">microdiseño</a>.</p></section>
<section><h2>¿Cómo se cuidan?</h2><ul><li>Cepillado y seda dental todos los días.</li><li>Pulido en los controles.</li><li>Moderar café, vino y cigarrillo.</li><li>No morder objetos duros.</li></ul></section>
<section><h2>Resultados</h2>{ba("caso2")}</section>""",
    related=[("Carillas de porcelana E-max", P_EMAX), ("Microdiseño de sonrisa", P_MICRO), ("Diseño de sonrisa: guía completa", T), ("Precios", P_PRICE)]))

# ---------------- MICRODISEÑO ----------------
MICRO_FAQS = [
    ("¿Qué es mejor, diseño de sonrisa o microdiseño?", "Si solo te molestan uno o pocos dientes, el microdiseño basta. Si quieres cambiar forma, tamaño y color de toda la zona visible, conviene el diseño completo."),
    ("¿Cuánto cuesta un microdiseño de sonrisa?", "Depende de cuántos dientes se tratan y del material. En resina, cada diente cuesta USD 145. La doctora te da el precio exacto por WhatsApp."),
]
PAGES.append(dict(path=P_MICRO, lang="es", crumb="Microdiseño de sonrisa", parents=[TRAT], schema_type="MedicalWebPage",
    title="Microdiseño de sonrisa en Medellín: qué es, precio y diferencias",
    desc="Microdiseño de sonrisa en Medellín: corrige bordes, espacios o formas en pocos dientes. Precio según número de dientes (resina desde USD 145 por diente). Diferencias con el diseño completo.",
    h1="Microdiseño de sonrisa",
    lead=("El microdiseño de sonrisa corrige detalles en pocos dientes, como un borde desgastado, un espacio o un diente más pequeño, sin cambiar toda la sonrisa. "
          "Con la Dra. Catalina Beltrán en Medellín, el precio depende de cuántos dientes se tratan; en resina cuesta USD 145 por diente."),
    wa=wa("microdiseño"), faqs=MICRO_FAQS,
    body=f"""<section><h2>¿Para qué sirve el microdiseño?</h2><ul><li>Cerrar espacios pequeños entre dientes.</li><li>Corregir bordes desgastados o astillados.</li><li>Igualar el tamaño de uno o dos dientes.</li><li>Mejorar detalles de forma sin tocar el resto.</li></ul></section>
<section><h2>Microdiseño o diseño completo: ¿cuál necesito?</h2>
<table><thead><tr><th></th><th>Microdiseño</th><th><a href="{T}">Diseño completo</a></th></tr></thead><tbody>
<tr><td>Dientes tratados</td><td>Pocos</td><td>Toda la zona visible</td></tr><tr><td>Cambia el color general</td><td>No</td><td>Sí</td></tr><tr><td>Inversión</td><td>Menor</td><td>Mayor</td></tr></tbody></table>
<p>Si además te molesta el color, puedes combinarlo con un <a href="{P_BLANQ}">blanqueamiento</a>.</p></section>
<section><h2>¿Cuánto dura?</h2><p>Depende del material: en resina dura menos que en porcelana y puede necesitar pulido o retoques. La doctora te dice qué material conviene en tu caso.</p></section>""",
    related=[("Carillas de resina", P_RES), ("Carillas de porcelana E-max", P_EMAX), ("Diseño de sonrisa: guía completa", T)]))

# ---------------- BLANQUEAMIENTO ----------------
BLANQ_FAQS = [
    ("¿El blanqueamiento daña los dientes?", "Hecho por una odontóloga y con el producto adecuado, no daña el esmalte. Puede dar sensibilidad temporal, que pasa en pocos días."),  # [REVISAR]
    ("¿Se puede blanquear una carilla?", "No. El blanqueamiento solo aclara dientes naturales. Por eso, si vas a hacerte carillas, conviene blanquear antes para elegir el color."),
]
PAGES.append(dict(path=P_BLANQ, lang="es", crumb="Blanqueamiento dental", parents=[TRAT], schema_type="MedicalWebPage",
    title="Blanqueamiento dental en Medellín | Dra. Catalina Beltrán",
    desc="Blanqueamiento dental en consultorio en Medellín con la Dra. Catalina Beltrán. Para quién sirve, sensibilidad, cuánto dura el efecto y cuándo hacerlo antes de un diseño de sonrisa.",
    h1="Blanqueamiento dental",
    lead=("El blanqueamiento dental aclara el color de tus dientes naturales sin cambiar su forma. La Dra. Catalina Beltrán lo hace en su consultorio de El Poblado, Medellín, "
          "y te confirma el precio por WhatsApp. Es la mejor opción si solo te molesta el color."),
    wa=wa("blanqueamiento"), faqs=BLANQ_FAQS,
    body=f"""<section><h2>¿Para quién es el blanqueamiento?</h2><p>Para quien tiene dientes sanos con manchas por café, té, vino, cigarrillo o el paso de los años. Si las manchas no mejoran con blanqueamiento, o también quieres cambiar la forma, conviene un <a href="{T}">diseño de sonrisa</a>.</p></section>
<section><h2>¿Cuánto dura el efecto?</h2><p>El resultado se mantiene más tiempo si moderas café, vino y cigarrillo y tienes buena higiene. La doctora te indica cómo mantenerlo.</p></section>
<section><h2>¿Blanqueamiento o carillas?</h2>
<table><thead><tr><th></th><th>Blanqueamiento</th><th><a href="{P_EMAX}">Carillas</a></th></tr></thead><tbody>
<tr><td>Cambia el color</td><td>Sí, en dientes naturales</td><td>Sí</td></tr><tr><td>Cambia la forma</td><td>No</td><td>Sí</td></tr><tr><td>Inversión</td><td>Menor</td><td>Mayor</td></tr></tbody></table></section>
<section><h2>¿Cuánto cuesta?</h2><p>La doctora te confirma el precio y las promociones vigentes por WhatsApp.</p></section>""",
    related=[("Diseño de sonrisa: guía completa", T), ("Microdiseño de sonrisa", P_MICRO), ("Carillas de porcelana E-max", P_EMAX)]))

# ---------------- PRECIOS ----------------
PRICE_FAQS = [
    ("¿Cuánto vale un diseño de sonrisa en dólares?", "Una sonrisa superior de 10 carillas de porcelana E-max cuesta USD 3.800 y la sonrisa completa de 20 carillas USD 5.900, que equivale a USD 295 por diente."),
    ("¿Qué incluye el precio?", "Valoración y diseño digital, carillas sin desgaste dental, limpieza previa y control por videollamada. No incluye vuelos ni hotel."),
    ("¿Por qué es más barato que en Estados Unidos?", "En EE. UU. se publican rangos de USD 1.000 a 2.500 por carilla de porcelana. En Medellín el costo de operación es menor, con el mismo material E-max."),
    ("¿Puedo pagar en pesos colombianos?", "Sí. La doctora te confirma el valor en pesos y las formas de pago por WhatsApp."),
]
PAGES.append(dict(path=P_PRICE, lang="es", alt="/en/cost-of-veneers-colombia/", crumb="Precios", schema_type="WebPage",
    title="¿Cuánto cuesta un diseño de sonrisa en Colombia? Precios 2026",
    desc="Precios reales de diseño de sonrisa en Colombia: carilla de porcelana E-max USD 380, resina USD 145, 20 carillas USD 5.900. Qué incluye y comparación con Estados Unidos.",
    h1="¿Cuánto cuesta un diseño de sonrisa en Colombia?",
    lead=("Con la Dra. Catalina Beltrán, en Medellín, una sonrisa completa de 20 carillas de porcelana E-max cuesta USD 5.900, es decir, USD 295 por diente. "
          "La carilla de porcelana suelta cuesta USD 380 y la de resina USD 145. El precio es cerrado y lo sabes antes de empezar."),
    wa=wa("precios"), faqs=PRICE_FAQS,
    body=f"""<section><h2>Precios de referencia 2026</h2>{PRICE_TABLE_ES}
<p class="muted">Precios vigentes al {fecha_es(UPDATED)}. Tu precio exacto depende de cuántos dientes necesitas: la doctora te lo confirma gratis por WhatsApp.</p></section>
<section><h2>¿Qué incluye el precio?</h2>{INCLUDES_ES}<p>Si vienes de otro país, el hotel Ibis Medellín está a 300 m del consultorio. <a href="{P_INT}">Ver cómo funciona el viaje</a>.</p></section>
<section><h2>¿Resina o porcelana?</h2>
<table><thead><tr><th></th><th><a href="{P_RES}">Resina</a></th><th><a href="{P_EMAX}">Porcelana E-max</a></th></tr></thead><tbody>
<tr><td>Precio por diente</td><td>USD 145</td><td>USD 380</td></tr><tr><td>Color con los años</td><td>Puede pigmentarse</td><td>Lo conserva</td></tr><tr><td>Duración</td><td>Menor</td><td>Mayor</td></tr></tbody></table></section>
<section><h2>¿Cuánto cuesta en Colombia frente a Estados Unidos?</h2>
<table><thead><tr><th>Tratamiento</th><th>EE. UU. (rango publicado)</th><th>Dra. Catalina, Medellín</th></tr></thead><tbody>
<tr><td>Carilla de porcelana</td><td>USD 1.000–2.500</td><td>USD 380</td></tr><tr><td>Carilla de resina</td><td>USD 400–1.500</td><td>USD 145</td></tr><tr><td>10 carillas de porcelana</td><td>USD 10.000+</td><td>USD 3.800</td></tr></tbody></table></section>
<section><h2>¿Por qué varía tanto el precio de una clínica a otra?</h2>
<p>Cambia según el material (resina o porcelana), la marca de la porcelana, cuántos dientes se tratan, si hay que tratar caries o encías antes y si incluye diseño digital y controles. Al comparar, pregunta siempre qué incluye el precio y si es cerrado.</p></section>""",
    related=[("Diseño de sonrisa en Medellín", P_MED), ("Carillas de porcelana E-max", P_EMAX), ("Carillas de resina", P_RES)]))

# ---------------- DRA ----------------
PAGES.append(dict(path=P_DRA, lang="es", alt="/en/dr-catalina-beltran/", crumb="Dra. Catalina Beltrán", schema_type="ProfilePage", byline=False,
    title="Dra. Catalina Beltrán | Odontóloga estética en Medellín, RETHUS 2011",
    desc="Conoce a la Dra. Catalina Beltrán: odontóloga con 15 años de experiencia, especialista en Estética Dental, registrada en el RETHUS desde 2011. Consultorio en El Poblado, Medellín.",
    h1="Dra. Catalina Beltrán",
    lead=("La Dra. Catalina Beltrán es odontóloga con 15 años de experiencia, registrada en el RETHUS desde 2011 y especialista en Estética Dental. "
          "Atiende personalmente a cada paciente en su consultorio de El Poblado, Medellín, y también en Bogotá."),
    wa="Hola Dra. Catalina 👋 Vi su página web y quiero saber el precio de mi diseño de sonrisa.", image="/img/dra-catalina-900.webp",
    body=f"""<img src="/img/dra-catalina-900.webp" width="900" height="1200" alt="Dra. Catalina Beltrán, odontóloga estética" style="max-width:360px;border-radius:16px;margin:18px 0">
<section><h2>Formación</h2><table><tbody>
<tr><td>Odontóloga con énfasis en ciencias quirúrgicas</td><td>Colegio Odontológico Colombiano</td></tr>
<tr><td>Especialista en Estética Dental</td><td>Federación Odontológica Colombiana</td></tr>
<tr><td>Especialización en Auditoría y Garantía de Calidad en Salud</td><td>Universidad EAN</td></tr>
<tr><td>Registro profesional</td><td>RETHUS, desde 2011</td></tr></tbody></table></section>
<section><h2>Cómo trabaja</h2><p>Revisa personalmente las fotos de cada paciente, diseña la sonrisa según la cara, el tono de piel y la mordida, y da un precio cerrado antes de empezar. Trabaja carillas sin desgaste dental y atiende en español e inglés.</p></section>
<section><h2>Pacientes</h2><p>Atiende pacientes de Colombia, Estados Unidos, Europa y Latinoamérica. Tiene una calificación de 5,0 en Google.</p>{PATIENTS_ES}</section>
<section><h2>Tratamientos</h2><div class="related"><a href="{P_EMAX}">Carillas de porcelana E-max</a><a href="{P_RES}">Carillas de resina</a><a href="{P_MICRO}">Microdiseño</a><a href="{P_BLANQ}">Blanqueamiento</a></div></section>
<section><h2>Consultorio</h2><p>{ADDRESS}. También atiende en Bogotá. <a href="{P_CONT}">Contacto y mapa</a>. <a href="{INSTAGRAM}">Instagram</a>.</p></section>""",
    related=[("Diseño de sonrisa en Medellín", P_MED), ("Antes y después", P_BA)]))

# ---------------- ANTES Y DESPUÉS ----------------
PAGES.append(dict(path=P_BA, lang="es", crumb="Antes y después", schema_type="WebPage",
    title="Diseño de sonrisa antes y después | Casos reales en Medellín",
    desc="Fotos reales de antes y después de diseño de sonrisa con la Dra. Catalina Beltrán en Medellín: carillas de porcelana E-max y resina. Pacientes de Colombia y del exterior.",
    h1="Diseño de sonrisa: antes y después",
    lead="Estos son casos reales de pacientes de la Dra. Catalina Beltrán en Medellín, publicados con su autorización. Cada sonrisa se diseñó según la cara, el tono de piel y la mordida de cada persona.",
    wa=wa("antes y después"),
    body=f"""<section><h2>Caso 1</h2>{ba("caso1")}</section>
<section><h2>Caso 2</h2>{ba("caso2")}{ba("caso2b")}</section>
<section><h2>El momento en que se ve por primera vez</h2>{VIDEO_ES}</section>
<section><h2>Pacientes que viajaron a Medellín por su sonrisa</h2>{PATIENTS_ES}</section>
<p class="note">Los resultados varían según cada caso. La doctora te dice qué es posible en tu caso después de ver tus fotos.</p>""",
    related=[("Carillas de porcelana E-max", P_EMAX), ("Precios", P_PRICE), ("Diseño de sonrisa en Medellín", P_MED)]))

# ---------------- INTERNACIONALES ----------------
INT_FAQS = [
    ("¿Cuántos días necesito en Medellín?", "Mínimo 4 días, en un solo viaje."),
    ("¿Necesito radiografías para la cotización?", "No. Para el precio exacto basta con 3 fotos tomadas con tu celular; la doctora te indica cómo."),
    ("¿Qué pasa después de regresar a mi país?", "El control se hace por videollamada."),
    ("¿El precio puede cambiar al llegar?", "El precio es cerrado y lo conoces antes de comprar el vuelo."),
]
PAGES.append(dict(path=P_INT, lang="es", crumb="Pacientes internacionales", schema_type="WebPage",
    title="Diseño de sonrisa en Colombia para extranjeros | Un viaje de 4 días",
    desc="Diseño de sonrisa en Medellín para pacientes del exterior: precio cerrado en dólares antes de viajar, un solo viaje de mínimo 4 días, valoración gratis por WhatsApp y control por videollamada.",
    h1="Diseño de sonrisa para pacientes internacionales",
    lead=("Si vives fuera de Colombia, recibes la valoración y el precio cerrado en dólares por WhatsApp antes de comprar el vuelo, y haces tu diseño de sonrisa en un solo viaje de mínimo 4 días a Medellín. "
          "El control posterior es por videollamada."),
    wa="Hola Dra. Catalina 👋 Vi su página web (pacientes internacionales) y quiero saber el precio de mi caso.", faqs=INT_FAQS,
    body=f"""<section><h2>¿Cómo funciona?</h2><ol>
<li><b>Escríbele por WhatsApp</b> desde tu país. Cuéntale qué quieres cambiar y envía 3 fotos con tu celular.</li>
<li><b>Recibe tu valoración y tu precio cerrado</b> en dólares. Si prefieres, por videollamada.</li>
<li><b>Compra tu vuelo</b> sabiendo exactamente cuánto vas a pagar.</li>
<li><b>Viaja a Medellín</b> mínimo 4 días. La doctora ya tiene tu diseño planificado.</li>
<li><b>Vuelve a casa</b> con tu sonrisa terminada. El control es por videollamada.</li></ol></section>
<section><h2>¿Cuánto cuesta?</h2>{PRICE_TABLE_ES}{INCLUDES_ES}</section>
<section><h2>¿Dónde me hospedo?</h2><p>El consultorio queda en El Poblado. Recomendamos el hotel Ibis Medellín, a 300 m del consultorio.</p></section>
<section><h2>¿En qué idioma me atienden?</h2><p>En español o inglés, por WhatsApp y en el consultorio.</p></section>
<section><h2>Pacientes del exterior</h2>{PATIENTS_ES}{VIDEO_ES}</section>""",
    related=[("Precios", P_PRICE), ("Diseño de sonrisa en Medellín", P_MED), ("Veneers in Medellín (English)", "/en/veneers-medellin/")]))

# ---------------- FAQ INDEX ----------------
def qa(q, a, link, label): return (q, f'{a} <a href="{link}">{label}</a>.')
ALL_FAQS = [
    qa("¿Cuánto cuesta un diseño de sonrisa en Colombia?", "Con la Dra. Catalina en Medellín, desde USD 145 por diente en resina y USD 380 en porcelana E-max; la sonrisa completa de 20 carillas, USD 5.900.", P_PRICE, "Ver precios"),
    qa("¿Qué es un diseño de sonrisa?", "Un plan que define forma, tamaño, color y proporción de tus dientes según tu cara, y se hace realidad con carillas, microdiseño o blanqueamiento.", T, "Guía completa"),
    qa("¿Qué es mejor, resina o porcelana?", "La porcelana E-max dura más y conserva su color; la resina es más económica.", P_RES, "Comparar"),
    qa("¿Cuánto duran las carillas E-max?", "Son la opción más duradera; su duración depende de tus cuidados y controles.", P_EMAX, "Carillas E-max"),
    qa("¿Las carillas pudren los dientes?", "No. Lo que daña el diente es la caries por mala higiene; con higiene y controles se mantiene sano.", P_EMAX, "Más información"),
    qa("¿Qué es mejor, diseño de sonrisa o microdiseño?", "El microdiseño corrige pocos dientes; el diseño completo cambia toda la zona visible.", P_MICRO, "Microdiseño"),
    qa("¿El blanqueamiento daña los dientes?", "Hecho por una odontóloga, no daña el esmalte; puede dar sensibilidad temporal.", P_BLANQ, "Blanqueamiento"),
    qa("¿Cuántos días necesito si vengo de otro país?", "Un solo viaje de mínimo 4 días, con precio cerrado antes de viajar.", P_INT, "Pacientes internacionales"),
    qa("¿Dónde queda el consultorio?", f"En {ADDRESS}. La doctora también atiende en Bogotá.", P_CONT, "Contacto"),
    qa("¿Quién es la Dra. Catalina Beltrán?", "Odontóloga con 15 años de experiencia, especialista en Estética Dental, registrada en el RETHUS desde 2011.", P_DRA, "Conócela"),
]
PAGES.append(dict(path=P_FAQ, lang="es", crumb="Preguntas frecuentes", schema_type="WebPage",
    title="Preguntas frecuentes sobre diseño de sonrisa | Dra. Catalina",
    desc="Respuestas de la Dra. Catalina Beltrán a las preguntas más buscadas sobre diseño de sonrisa: precio, resina o porcelana, duración, riesgos, microdiseño y viaje a Medellín.",
    h1="Preguntas frecuentes sobre diseño de sonrisa",
    lead="Estas son las preguntas que más hacen los pacientes antes de un diseño de sonrisa, respondidas por la Dra. Catalina Beltrán. Cada respuesta enlaza a la página con el detalle.",
    wa=wa("preguntas frecuentes"), faqs=ALL_FAQS, body="",
    related=[("Diseño de sonrisa: guía completa", T), ("Precios", P_PRICE)]))

# ---------------- CONTACTO ----------------
PAGES.append(dict(path=P_CONT, lang="es", crumb="Contacto", schema_type="ContactPage", byline=False,
    title="Contacto | Dra. Catalina Beltrán, El Poblado, Medellín",
    desc=f"Consultorio de la Dra. Catalina Beltrán: {ADDRESS}. WhatsApp {PHONE}. También atiende en Bogotá.",
    h1="Contacto", lead=f"Escríbele a la Dra. Catalina por WhatsApp al {PHONE}. El consultorio queda en {ADDRESS}. La doctora también atiende en Bogotá.",
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
<h2>Qué datos recogemos</h2><p>Este sitio no pide nombre, teléfono ni correo. Si nos escribes por WhatsApp, recibimos los datos que tú decides enviarnos, como tu nombre, número o fotos de tu sonrisa.</p>
<h2>Para qué los usamos</h2><p>Para responder tu solicitud, hacer tu valoración, darte un presupuesto y hacer seguimiento a tu caso. No vendemos ni compartimos tus datos con terceros para fines comerciales. Tus fotos y datos de salud solo los ve el equipo del consultorio y no se usan en publicidad sin tu autorización expresa y por escrito.</p>
<h2>Tus derechos</h2><p>De acuerdo con la Ley 1581 de 2012 y el Decreto 1377 de 2013 de Colombia, puedes conocer, actualizar, rectificar y pedir que eliminemos tus datos, así como revocar tu autorización. Escríbenos por WhatsApp o al correo indicado y te respondemos en un máximo de 15 días hábiles.</p>
<h2>Cuánto tiempo los guardamos</h2><p>Mientras sean necesarios para tu atención y por el tiempo que exige la normatividad colombiana para historias clínicas.</p>"""))
