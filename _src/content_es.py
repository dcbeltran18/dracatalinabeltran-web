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

TRAT = ("Tratamientos", T)
def wa(t): return f"Hola Dra. Catalina 👋 Vi su página web ({t}) y quiero saber el precio de mi caso."
PRICE_LINE = f'Porcelana E-max USD 380 por diente · resina USD 145 por diente · sonrisa completa de 20 carillas de porcelana USD 5.900. <a href="{P_PRICE}">Ver precios y qué incluyen</a>.'

PAGES = []

# ---------------- INICIO ----------------
PAGES.append(dict(path="/", lang="es", byline=False,
    title="Dra. Catalina Beltrán | Odontóloga estética en Medellín",
    desc="Odontóloga estética en El Poblado, Medellín. Carillas sin desgaste dental en porcelana E-max y resina, con precio cerrado. 15 años de experiencia, 5,0 en Google.",
    h1="Dra. Catalina Beltrán, odontóloga estética en Medellín",
    lead=("La Dra. Catalina Beltrán es odontóloga estética en El Poblado, Medellín, con 15 años de experiencia y calificación de 5,0 en Google. "
          "Hace diseños de sonrisa con carillas de porcelana E-max y de resina sin desgaste dental, con precio cerrado antes de empezar: desde USD 145 por diente en resina y USD 5.900 por una sonrisa completa de 20 carillas de porcelana."),
    wa="Hola Dra. Catalina 👋 Vi su página web y quiero saber el precio de mi diseño de sonrisa.",
    body=f"""<div class="cards"><div class="card"><b>5,0</b><span>Calificación en Google</span></div><div class="card"><b>15 años</b><span>de experiencia</span></div>
<div class="card"><b>0 desgaste</b><span>Carillas sin desgastar tus dientes</span></div><div class="card"><b>USD 295</b><span>por diente en sonrisa completa de porcelana</span></div></div>
<section><h2>Tratamientos</h2>
<div class="cards">
<a class="card" href="{P_EMAX}"><b>Porcelana E-max</b><span>Carillas de porcelana a la medida. USD 380 por diente.</span></a>
<a class="card" href="{P_RES}"><b>Resina</b><span>La forma más económica de un diseño completo. USD 145 por diente.</span></a>
<a class="card" href="{T}"><b>Guía de diseño de sonrisa</b><span>Tipos, microdiseño, blanqueamiento y cómo elegir.</span></a></div></section>
<section><h2>Precios</h2><p>{PRICE_LINE}</p></section>
<section><h2>Resultados</h2>{ba("caso1")}<p><a href="{P_BA}">Ver más casos de antes y después</a></p></section>
<section><h2>Cómo funciona</h2><ol>
<li><b>Escríbele por WhatsApp.</b> Cuéntale qué te gustaría cambiar y envía 3 fotos con tu celular; no necesitas radiografías.</li>
<li><b>Recibe tu valoración.</b> La doctora te dice qué opción te conviene, cuántos dientes tratar y el precio cerrado.</li>
<li><b>Haz tu tratamiento</b> en el <a href="{P_MED}">consultorio de El Poblado, Medellín</a>. Si vives fuera de Colombia: <a href="{P_INT}">un solo viaje de mínimo 4 días</a>.</li></ol></section>
<section><h2>Tu odontóloga</h2>{DOCTOR_ES}</section>
<section><h2>Pacientes</h2><p>Calificación de 5,0 en Google.</p>{PATIENTS_ES}</section>
<section><h2>Consultorio</h2><p>{ADDRESS}. <a href="{P_CONT}">Ver mapa y contacto</a>.</p></section>""",
    related=[("Diseño de sonrisa en Medellín", P_MED), ("Precios", P_PRICE), ("Pacientes internacionales", P_INT)]))

# ---------------- MEDELLÍN ----------------
MED_FAQS = [
    ("¿Cómo elegir dónde hacerse un diseño de sonrisa en Medellín?",
     "Verifica que la odontóloga esté registrada en el RETHUS, que publique sus precios, que muestre casos reales y que te entregue un plan con precio cerrado antes de empezar."),
    ("¿Atienden en inglés?", "Sí. La doctora atiende en español e inglés, por WhatsApp y en el consultorio."),
]
PAGES.append(dict(path=P_MED, lang="es", alt="/en/veneers-medellin/", crumb="Diseño de sonrisa en Medellín", schema_type="MedicalWebPage",
    title="Diseño de sonrisa en Medellín | Carillas sin desgaste",
    desc="Diseño de sonrisa en Medellín sin desgaste dental: porcelana E-max USD 380 y resina USD 145 por diente, en El Poblado. Precio cerrado y valoración gratis.",
    h1="Diseño de sonrisa en Medellín",
    lead=("En Medellín, la Dra. Catalina Beltrán hace diseños de sonrisa con carillas de porcelana E-max (USD 380 por diente) y de resina (USD 145 por diente), sin desgaste dental, en su consultorio de El Poblado. "
          "Recibes el plan y el precio cerrado antes de empezar, y la valoración es gratis por WhatsApp."),
    wa=wa("diseño de sonrisa Medellín"), faqs=MED_FAQS, image="/video/paciente-estados-unidos-se-ve-por-primera-vez-diseno-de-sonrisa-medellin.webp", video=True,
    body=f"""<section><h2>¿Cuánto cuesta un diseño de sonrisa en Medellín?</h2>
<p>Con la Dra. Catalina, una sonrisa completa de 20 carillas de porcelana E-max cuesta USD 5.900 (USD 295 por diente) y una sonrisa superior de 10 carillas, USD 3.800. En resina, cada diente cuesta USD 145. El precio incluye valoración y diseño digital, limpieza previa y control por videollamada. <a href="{P_PRICE}">Ver todos los precios</a>.</p></section>
<section><h2>¿Qué opciones hay?</h2>
<p>Las dos formas de hacer un diseño completo son las <a href="{P_EMAX}">carillas de porcelana E-max</a>, más duraderas, y las <a href="{P_RES}">carillas de resina</a>, más económicas. Si solo quieres corregir pocos dientes o aclarar el color, hay opciones más pequeñas: <a href="{T}">compáralas en la guía de diseño de sonrisa</a>.</p></section>
<section><h2>¿Cómo es el proceso en el consultorio?</h2>
<p>Le escribes a la doctora por WhatsApp y le envías 3 fotos con tu celular. Ella te dice qué opción te conviene, cuántos dientes tratar y el precio cerrado; si prefieres, por videollamada. Antes de tocar un diente, planifica tu diseño digital. En el consultorio hace la limpieza previa y el tratamiento, y el control posterior es por videollamada.</p></section>
<section><h2>Resultados en Medellín</h2>
<h3>El momento en que se ve por primera vez</h3>
<p>Este paciente viajó desde Estados Unidos a Medellín para su diseño de sonrisa con la Dra. Catalina. El video lo muestra en el consultorio de El Poblado, al terminar el tratamiento, cuando se mira por primera vez.</p>
{VIDEO_ES}
<h3>Antes y después en el consultorio de El Poblado</h3>
<p>Un caso real de la Dra. Catalina en Medellín: carillas de porcelana E-max colocadas sin desgaste dental, en su consultorio de El Poblado.</p>
{ba_page("caso2", "diseno-de-sonrisa-medellin-el-poblado-antes.webp", "diseno-de-sonrisa-medellin-el-poblado-despues-carillas-emax.webp",
 "Sonrisa antes del diseño de sonrisa en Medellín", "La misma sonrisa después del diseño de sonrisa con carillas E-max sin desgaste en El Poblado, Medellín",
 "Caso real en el consultorio de El Poblado, Medellín: carillas de porcelana E-max sin desgaste.")}
<p>Mira el <a href="{P_EMAX}">mismo caso de frente y de perfil</a>, o <a href="{P_BA}">todos los casos de antes y después</a>.</p></section>
<section><h2>¿Por qué elegir a la Dra. Catalina?</h2>
<ul><li>Carillas sin desgaste dental: tus dientes naturales se conservan.</li><li>Precio cerrado antes de empezar, publicado en dólares.</li><li>Atención personal de la doctora, en español e inglés.</li>
<li>15 años de experiencia y registro en el RETHUS desde 2011.</li><li>Consultorio en El Poblado, una de las zonas de Medellín con más hoteles y restaurantes.</li></ul>
{DOCTOR_ES}</section>
<section><h2>¿Dónde queda el consultorio?</h2><p>{ADDRESS}. Si vienes de otro país, el hotel Ibis Medellín está a 300 m.</p>{MAP}</section>""",
    related=[("Precios", P_PRICE), ("Guía de diseño de sonrisa", T), ("Pacientes internacionales", P_INT)]))

# ---------------- PILAR ----------------
PILAR_FAQS = [
    ("¿El diseño de sonrisa es bueno o malo?",
     "Es un tratamiento seguro cuando lo hace una odontóloga calificada después de revisar la salud de dientes y encías. Los problemas suelen venir de tratamientos sin valoración previa o de desgastar dientes sanos sin necesidad."),
    ("¿El diseño de sonrisa es lo mismo que las carillas?",
     "No exactamente. El diseño de sonrisa es el plan (forma, tamaño, color y proporción de los dientes según tu cara); las carillas son una de las formas de llevarlo a cabo."),
]
PAGES.append(dict(path=T, lang="es", crumb="Diseño de sonrisa", schema_type="MedicalWebPage",
    title="¿Qué es el diseño de sonrisa? Tipos, duración y cómo elegir",
    desc="Qué es el diseño de sonrisa, qué tipos hay (porcelana, resina, microdiseño, blanqueamiento), cuánto dura y quién puede hacérselo. Guía de una odontóloga estética.",
    h1="Diseño de sonrisa: qué es, tipos y cómo elegir",
    lead=("El diseño de sonrisa es un plan odontológico que define la forma, el tamaño, el color y la proporción de tus dientes según tu cara, y luego lo lleva a cabo con carillas de porcelana, carillas de resina, microdiseño o blanqueamiento. "
          "La opción correcta depende de cuánto quieres cambiar, de tu presupuesto y de la salud de tus dientes."),
    wa=wa("diseño de sonrisa"), faqs=PILAR_FAQS,
    body=f"""<section><h2>¿Qué tipos de diseño de sonrisa hay?</h2>
<table><thead><tr><th>Opción</th><th>Qué cambia</th><th>Cuándo conviene</th></tr></thead><tbody>
<tr><td><a href="{P_EMAX}">Carillas de porcelana E-max</a></td><td>Forma, tamaño y color</td><td>Cambio completo y duradero</td></tr>
<tr><td><a href="{P_RES}">Carillas de resina</a></td><td>Forma, tamaño y color</td><td>Cambio completo con menor inversión</td></tr>
<tr><td>Microdiseño</td><td>Detalles en pocos dientes</td><td>Corregir un borde, un espacio o un diente</td></tr>
<tr><td>Blanqueamiento</td><td>Solo el color de dientes naturales</td><td>Dientes sanos con manchas</td></tr></tbody></table>
<p>Precios: {PRICE_LINE}</p></section>
<section><h2>¿Cómo se ve un diseño de sonrisa antes y después?</h2>
<p>Un diseño de sonrisa cambia la forma, el tamaño y el color de los dientes visibles, siempre en proporción con la cara. Estos son dos casos reales de la Dra. Catalina en Medellín.</p>
<h3>Diseño de sonrisa completo</h3>
{ba_page("caso1", "que-es-diseno-de-sonrisa-antes.webp", "que-es-diseno-de-sonrisa-despues.webp",
 "Dientes antes de un diseño de sonrisa, caso real en Medellín", "Los mismos dientes después del diseño de sonrisa: forma, tamaño y color en proporción con la cara",
 "Ejemplo de diseño de sonrisa: cambio de forma, tamaño y color de los dientes visibles.")}
<h3>Diseño de sonrisa con carillas de porcelana E-max</h3>
{ba_page("caso2", "tipos-de-diseno-de-sonrisa-carillas-emax-antes.webp", "tipos-de-diseno-de-sonrisa-carillas-emax-despues.webp",
 "Sonrisa antes de un diseño de sonrisa con carillas de porcelana", "La misma sonrisa después de un diseño de sonrisa con carillas de porcelana E-max sin desgaste",
 "Uno de los tipos de diseño de sonrisa: carillas de porcelana E-max, colocadas sin desgaste dental.")}
<p><a href="{P_BA}">Ver todos los casos de antes y después</a></p></section>
<section><h2>¿Qué es mejor, diseño de sonrisa o microdiseño?</h2>
<p>Si solo te molestan uno o pocos dientes (un borde desgastado, un espacio pequeño, un diente más corto), un microdiseño basta y la inversión es menor. Si quieres cambiar forma, tamaño y color de toda la zona visible al sonreír, conviene un diseño completo con carillas. El microdiseño se cobra según el número de dientes tratados.</p></section>
<section><h2>¿Blanqueamiento o carillas?</h2>
<p>El blanqueamiento aclara el color de los dientes naturales, pero no cambia su forma ni se puede aplicar sobre una carilla. Si solo te molesta el color y tus dientes están sanos, empieza por blanqueamiento. Si vas a hacerte carillas, conviene blanquear antes para elegir el tono final. La doctora te confirma el precio del blanqueamiento por WhatsApp.</p></section>
<section><h2>¿Cómo se hace un diseño de sonrisa?</h2>
<p>La doctora revisa tus fotos y la salud de tus dientes y encías. Luego diseña digitalmente tu sonrisa según tu cara, tu tono de piel y tu mordida, y te muestra el plan con el precio cerrado. Solo cuando lo apruebas se hace la limpieza previa y el tratamiento en el <a href="{P_MED}">consultorio de El Poblado, Medellín</a>. El control posterior es por videollamada.</p></section>
<section><h2>¿Cuánto dura un diseño de sonrisa?</h2>
<p>Depende del material y de tus cuidados. La porcelana E-max es la opción más duradera y conserva su color; la resina dura menos y con los años puede necesitar pulido o retoques. En ambos casos influyen la higiene diaria, los controles y hábitos como morder objetos duros o apretar los dientes.</p></section>
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
    desc="Carillas E-max sin desgaste dental en Medellín: USD 380 por diente y 20 carillas por USD 5.900. Qué son, cuánto duran, ventajas, desventajas y cuidados.",
    h1="Carillas de porcelana E-max",
    lead=("Las carillas E-max son láminas delgadas de porcelana de disilicato de litio que se adhieren al frente de los dientes para cambiar su forma, tamaño y color. "
          "Con la Dra. Catalina Beltrán en Medellín se colocan sin desgaste dental y cuestan USD 380 por diente; la sonrisa completa de 20 carillas cuesta USD 5.900."),
    wa=wa("carillas E-max"), faqs=EMAX_FAQS, image="/img/carillas-emax-sin-desgaste-despues-caso-2.webp",
    body=f"""<section><h2>¿Qué son las carillas E-max?</h2>
<p>E-max es una marca de porcelana de disilicato de litio. Es resistente y deja pasar la luz de forma parecida al esmalte natural, por eso se ve real de cerca. Cada carilla se fabrica a la medida según el diseño digital de tu sonrisa.</p></section>
<section><h2>Resultados con carillas E-max</h2>
<p>Este es un caso real de la Dra. Catalina: carillas de porcelana E-max colocadas sin desgaste dental, en su consultorio de El Poblado, Medellín. Arriba, la sonrisa de frente; abajo, el mismo paciente de perfil.</p>
{ba("caso2")}{ba("caso2b")}<p><a href="{P_BA}">Ver más casos de antes y después</a></p></section>
<section><h2>¿Cuánto cuestan las carillas E-max en Medellín?</h2>
<p>USD 380 por diente. Diez carillas para la sonrisa superior cuestan USD 3.800 y la sonrisa completa de 20 carillas, USD 5.900, es decir, USD 295 por diente. <a href="{P_PRICE}">Ver qué incluye y la comparación con Estados Unidos</a>.</p></section>
<section><h2>¿Para quién son?</h2>
<p>Para quien quiere un cambio completo y duradero: dientes manchados que no mejoran con blanqueamiento, desgastados, con espacios, de formas irregulares o pequeños. También para quien tiene carillas viejas de resina y quiere pasar a porcelana.</p></section>
<section><h2>¿Cuánto duran las carillas E-max?</h2>
<p>Son la opción más duradera del diseño de sonrisa. Su duración depende de tus cuidados: higiene diaria, controles, no morder objetos duros y usar placa nocturna si aprietas los dientes. La doctora te explica qué esperar en tu caso.</p></section>
<section><h2>Ventajas y desventajas de las carillas E-max</h2>
<table><thead><tr><th>Ventajas</th><th>Desventajas</th></tr></thead><tbody>
<tr><td>Conservan su color</td><td>Cuestan más que la resina</td></tr><tr><td>Aspecto natural de cerca</td><td>Se fabrican en laboratorio: no se hacen en una sola cita</td></tr>
<tr><td>Más duraderas que la resina</td><td>Si una se fractura, se reemplaza la pieza</td></tr><tr><td>Sin desgaste dental con la doctora</td><td>Necesitan higiene y controles como cualquier diente</td></tr></tbody></table></section>
<section><h2>¿Cuánto tiempo toma el tratamiento?</h2>
<p>Se hace en el <a href="{P_MED}">consultorio de El Poblado, Medellín</a>. Si vives fuera de Colombia, en un solo viaje de mínimo 4 días; antes de viajar ya tienes la valoración, el diseño y el precio cerrado. <a href="{P_INT}">Ver cómo funciona el viaje</a>.</p></section>
<section><h2>¿Cómo se cuidan las carillas E-max?</h2><ul><li>Cepillado y seda dental todos los días.</li><li>Controles con la doctora (el primero, por videollamada).</li><li>No morder objetos duros ni abrir paquetes con los dientes.</li><li>Placa nocturna si aprietas o rechinas los dientes.</li></ul></section>
<section><h2>¿Qué alternativas hay?</h2><p>Si buscas menor inversión, las <a href="{P_RES}">carillas de resina</a> cuestan USD 145 por diente. Si solo quieres corregir pocos dientes o aclarar el color, revisa el microdiseño y el blanqueamiento en la <a href="{T}">guía de diseño de sonrisa</a>.</p></section>""",
    related=[("Carillas de resina", P_RES), ("Antes y después", P_BA), ("Precios", P_PRICE)]))

# ---------------- RESINA ----------------
RES_FAQS = [
    ("¿Las carillas de resina se manchan?", "Pueden pigmentarse con los años, sobre todo con café, vino o cigarrillo. Un pulido en el control ayuda a mantener el brillo."),  # [REVISAR]
    ("¿Se pueden cambiar después a porcelana?", "Sí. Muchas personas empiezan con resina y luego pasan a porcelana E-max. La doctora te dice cuándo conviene."),
]
PAGES.append(dict(path=P_RES, lang="es", crumb="Carillas de resina", parents=[TRAT], schema_type="MedicalWebPage",
    title="Carillas de resina en Medellín: precio, duración y diferencias",
    desc="Diseño de sonrisa en resina en Medellín: USD 145 por diente. Cuánto dura, si se mancha y en qué se diferencia de la porcelana E-max. Tabla comparativa.",
    h1="Carillas de resina",
    lead=("Las carillas de resina se hacen con un material del color del diente que la doctora moldea sobre cada pieza para cambiar su forma, tamaño y color. "
          f"Con la Dra. Catalina Beltrán en <a href='{P_MED}'>Medellín</a> cuestan USD 145 por diente, sin desgaste dental, y son la forma más económica de hacer un diseño de sonrisa completo."),
    wa=wa("carillas de resina"), faqs=RES_FAQS,
    body=f"""<section><h2>Un caso real en resina</h2><p>Así cambió esta sonrisa con un diseño en resina hecho por la Dra. Catalina Beltrán.</p>{ba("caso3")}<p><a href="{P_BA}">Ver todos los casos de antes y después</a></p></section>
<section><h2>¿Cuánto cuesta un diseño de sonrisa en resina?</h2>
<p>USD 145 por diente. El total depende de cuántos dientes necesitas; la doctora te lo confirma gratis por WhatsApp. <a href="{P_PRICE}">Ver todos los precios</a>.</p></section>
<section><h2>¿Qué es mejor, resina o porcelana?</h2>
<p>La porcelana E-max dura más y conserva su color; la resina cuesta menos de la mitad y se puede retocar. Si buscas el resultado más duradero, conviene porcelana; si quieres un cambio completo con menor inversión, o probar un diseño, conviene resina.</p>
<table><thead><tr><th></th><th>Resina</th><th><a href="{P_EMAX}">Porcelana E-max</a></th></tr></thead><tbody>
<tr><td>Precio por diente</td><td>USD 145</td><td>USD 380</td></tr><tr><td>Color con los años</td><td>Puede pigmentarse</td><td>Lo conserva</td></tr>
<tr><td>Duración</td><td>Menor</td><td>Mayor</td></tr><tr><td>Si se daña</td><td>Se puede retocar</td><td>Se reemplaza la pieza</td></tr></tbody></table></section>
<section><h2>¿Cuánto dura un diseño de sonrisa en resina?</h2>
<p>Dura menos que la porcelana y con los años puede necesitar pulido o retoques. La duración depende sobre todo de la higiene, los controles y hábitos como el café o el cigarrillo. La doctora te dice qué esperar en tu caso.</p></section>
<section><h2>¿Para quién es?</h2><p>Para quien quiere un cambio completo con menor inversión, o quiere probar un diseño antes de pasar a porcelana. También se usa para corregir pocos dientes en un microdiseño.</p></section>
<section><h2>¿Cómo se cuidan las carillas de resina?</h2><ul><li>Cepillado y seda dental todos los días.</li><li>Pulido en los controles.</li><li>Moderar café, vino y cigarrillo.</li><li>No morder objetos duros.</li></ul></section>""",
    related=[("Carillas de porcelana E-max", P_EMAX), ("Guía de diseño de sonrisa", T), ("Precios", P_PRICE)]))

# ---------------- PRECIOS ----------------
PRICE_FAQS = [
    ("¿Cuánto vale un diseño de sonrisa en dólares?", "Una sonrisa superior de 10 carillas de porcelana E-max cuesta USD 3.800 y la sonrisa completa de 20 carillas, USD 5.900, que equivale a USD 295 por diente."),
    ("¿Puedo pagar en pesos colombianos?", "Sí. La doctora te confirma el valor en pesos por WhatsApp."),
]
PAGES.append(dict(path=P_PRICE, lang="es", alt="/en/cost-of-veneers-colombia/", crumb="Precios", schema_type="WebPage",
    title="¿Cuánto cuesta un diseño de sonrisa en Colombia? Precios 2026",
    desc="Precios reales de diseño de sonrisa en Colombia: porcelana E-max USD 380, resina USD 145, 20 carillas USD 5.900. Qué incluye y comparación con EE. UU.",
    h1="¿Cuánto cuesta un diseño de sonrisa en Colombia?",
    lead=("Con la Dra. Catalina Beltrán, en Medellín, una sonrisa completa de 20 carillas de porcelana E-max cuesta USD 5.900, es decir, USD 295 por diente. "
          "La carilla de porcelana suelta cuesta USD 380 y la de resina USD 145. El precio es cerrado y lo sabes antes de empezar."),
    wa=wa("precios"), faqs=PRICE_FAQS,
    body=f"""<section><h2>Precios de referencia 2026</h2>{PRICE_TABLE_ES}
<p class="muted">Precios vigentes al {fecha_es(UPDATED)}. Tu precio exacto depende de cuántos dientes necesitas: la doctora te lo confirma gratis por WhatsApp.</p></section>
<section><h2>¿Qué incluye el precio?</h2>{INCLUDES_ES}<p>Si vives fuera de Colombia, <a href="{P_INT}">así funciona el viaje</a>.</p></section>
<section><h2>¿Qué resultado obtienes por ese precio?</h2>
<p>Este es un caso real de carillas de porcelana E-max de la Dra. Catalina, del tipo de tratamiento que se cotiza con precio cerrado en dólares. El precio exacto de tu caso depende de cuántos dientes necesitas.</p>
{ba_page("caso2", "precio-carillas-emax-colombia-antes.webp", "precio-carillas-emax-colombia-despues.webp",
 "Sonrisa antes de carillas de porcelana E-max cotizadas con precio cerrado", "Resultado de carillas de porcelana E-max sin desgaste con precio cerrado en dólares, Medellín, Colombia",
 "Resultado real de carillas E-max sin desgaste en Medellín, con precio cerrado antes de empezar.")}</section>
<section><h2>¿Cuánto cuesta en Colombia frente a Estados Unidos?</h2>
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
    wa="Hola Dra. Catalina 👋 Vi su página web y quiero saber el precio de mi diseño de sonrisa.", image="/img/dra-catalina-beltran-odontologa-estetica-medellin.webp",
    body=f"""<img src="/img/dra-catalina-beltran-odontologa-estetica-medellin.webp" width="900" height="1200" alt="Dra. Catalina Beltrán, odontóloga estética" style="max-width:360px;border-radius:16px;margin:18px 0">
<section><h2>Formación</h2><table><tbody>
<tr><td>Odontóloga con énfasis en ciencias quirúrgicas</td><td>Colegio Odontológico Colombiano</td></tr>
<tr><td>Especialista en Estética Dental</td><td>Federación Odontológica Colombiana</td></tr>
<tr><td>Especialización en Auditoría y Garantía de Calidad en Salud</td><td>Universidad EAN</td></tr>
<tr><td>Registro profesional</td><td>RETHUS, desde 2011</td></tr></tbody></table></section>
<section><h2>Cómo trabaja</h2><p>Revisa personalmente las fotos de cada paciente, diseña la sonrisa según la cara, el tono de piel y la mordida, y da un precio cerrado antes de empezar. Trabaja carillas sin desgaste dental y atiende en español e inglés.</p></section>
<section><h2>Pacientes</h2><p>Calificación de 5,0 en Google.</p>{PATIENTS_ES}</section>
<section><h2>Tratamientos</h2><div class="related"><a href="{P_EMAX}">Carillas de porcelana E-max</a><a href="{P_RES}">Carillas de resina</a><a href="{T}">Guía de diseño de sonrisa</a></div></section>
<section><h2>Consultorio</h2><p>{ADDRESS}. <a href="{P_CONT}">Contacto y mapa</a> · <a href="{INSTAGRAM}">Instagram</a></p></section>""",
    related=[("Diseño de sonrisa en Medellín", P_MED), ("Antes y después", P_BA)]))

# ---------------- ANTES Y DESPUÉS ----------------
PAGES.append(dict(path=P_BA, lang="es", crumb="Antes y después", schema_type="WebPage",
    title="Diseño de sonrisa antes y después | Casos reales en Medellín",
    desc="Fotos reales de antes y después de diseño de sonrisa en Medellín con la Dra. Catalina Beltrán, y el video de un paciente al ver su nueva sonrisa.",
    h1="Diseño de sonrisa: antes y después",
    lead="Estos son casos reales de pacientes de la Dra. Catalina Beltrán en Medellín, publicados con su autorización. Cada sonrisa se diseñó según la cara, el tono de piel y la mordida de cada persona.",
    wa=wa("antes y después"), video=True,
    body=f"""<section><h2>Caso 1: diseño de sonrisa</h2>{ba("caso1")}</section>
<section><h2>Caso 2: carillas de porcelana E-max sin desgaste</h2>{ba("caso2")}{ba("caso2b")}<p><a href="{P_EMAX}">Qué son las carillas E-max y cuánto cuestan</a></p></section>
<section><h2>Caso 3: diseño de sonrisa en resina</h2>{ba("caso3")}<p><a href="{P_RES}">Qué es el diseño de sonrisa en resina y cuánto cuesta</a></p></section>
<section><h2>El momento en que se ve por primera vez</h2>{VIDEO_ES}</section>
<section><h2>Pacientes que viajaron a Medellín por su sonrisa</h2>{PATIENTS_ES}</section>
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
    wa="Hola Dra. Catalina 👋 Vi su página web (pacientes internacionales) y quiero saber el precio de mi caso.", faqs=INT_FAQS, video=True,
    body=f"""<section><h2>¿Cómo funciona?</h2><ol>
<li><b>Escríbele por WhatsApp</b> desde tu país. Cuéntale qué quieres cambiar y envía 3 fotos con tu celular.</li>
<li><b>Recibe tu valoración y tu precio cerrado</b> en dólares. Si prefieres, por videollamada.</li>
<li><b>Compra tu vuelo</b> sabiendo exactamente cuánto vas a pagar.</li>
<li><b>Viaja a Medellín</b> mínimo 4 días. La doctora ya tiene tu diseño planificado.</li>
<li><b>Vuelve a casa</b> con tu sonrisa terminada. El control es por videollamada.</li></ol></section>
<section><h2>¿Cuánto cuesta?</h2><p>{PRICE_LINE}</p>{INCLUDES_ES}</section>
<section><h2>¿Dónde me hospedo?</h2><p>El consultorio queda en El Poblado. Recomendamos el hotel Ibis Medellín, a 300 m del consultorio.</p></section>
<section><h2>¿Después de volver a mi país?</h2><p>El control se hace por videollamada con la doctora.</p></section>
<section><h2>Pacientes del exterior</h2>{VIDEO_ES}</section>""",
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
