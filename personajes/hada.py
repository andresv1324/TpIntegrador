import streamlit as st
from PIL import Image
from pathlib import Path

# Ruta absoluta de la carpeta principal del proyecto
RUTA_PROYECTO = Path(__file__).resolve().parent.parent

# Carpeta de imágenes
RUTA_IMG = RUTA_PROYECTO / "assets" / "hada" / "img"

# Carpeta de GIF
RUTA_GIF = RUTA_PROYECTO / "assets" / "hada" / "gif"

# Cargar imágenes
imgRioBravo = Image.open(RUTA_IMG / "hadaAnteElRioTempestuoso.png")
hadaGatAntCam = Image.open(RUTA_IMG / "hadaGatoAnteCamino.png")
hadaBajLlu = Image.open(RUTA_IMG / "gataBajoLaLluvia.png")
hadaCalva = Image.open(RUTA_IMG / "hadaCorte.png")
hadaSubSue = Image.open(RUTA_IMG / "hadaEnSubSuelo.png")
hadaCampana = Image.open(RUTA_IMG / "hadaCampanaGato.png")
hadaArdAntCam = Image.open(RUTA_IMG /"hadaArdiAnteCamino.png")
hadaFloresMag = Image.open(RUTA_IMG /"hadaEncuentroFlores.png")
hadaBosque = Image.open(RUTA_IMG / "hadaEnBosque.png")
hadaDentroBsque = Image.open (RUTA_IMG / "hadaDentroBosque.png")


def textoCruce():
    #CAMINO RIO BRAVO
    if st.session_state.destino == "Rio Bravo" and st.session_state.cruce =="Bordear el rio":
        if st.session_state.mostrarTextoComo==1:
            st.write("Elijes bordear el rio, dices que es mejor un trabajo duro que uno arriesgado, tu camino empieza complicado, te sientes observada y ansiosa, lo cual te hace tropezar y lastimarte, llegas a mitad de camino y sientes que no puedes más, de repente una manada de perros aparece en frente tuyo, gruñéndote y enfrentandote, tu miedo te ciega y tu cansancio actual no ayuda, pero")
            st.write("Desde lo más alto de los árboles a tu lado finos balines empiezan a dirigirse hacia los perros haciendo que se asusten y no sepan que hacer más que correr hacia diferentes direcciones, se olvidan de ti, pero debido a todo lo ocurrido te desmayas, momentos después te despiertas y sin entender mucho sigues el camino")
            st.image(RUTA_GIF / "hadaBordearRio.gif")

            if st.button("Continuar", key="textHadaBalsBorde"):
                st.session_state.mostrarTextoComo =2
                st.rerun()
        elif st.session_state.mostrarTextoComo ==2:
            st.write("Estás llegando al final de tu camino… Pero espera un momento, ¿qué es ese ruido? Escuchas un crujido de madera y empiezas a sentir miedo… De repente, una nuez cae sobre tu cabeza.")
            st.write("Lejos de asustarte, miras en la dirección de donde provino. Unos ojos redondos y brillantes te observan desde allí. ¡Es una ardilla! Pero no una ardilla cualquiera: destellos dorados brotan de su nariz y sus orejas al verte. ¿Acaso esto será el inicio de una conexión especial…? ")
            st.image(RUTA_GIF / "hadaArdilla.gif")
            st.write("Felicidades! un compañero te eligió para acompañarte en tu aventura")
            if st.button("Continuar", key="textHadaBalsBorde2"):
                st.session_state.mostrarTextoComo = 0
                st.rerun()
    elif st.session_state.destino == "Rio Bravo" and st.session_state.cruce =="Balsa por dentro":
        if st.session_state.mostrarTextoComo==1:
            st.write("Eliges cruzar el río por dentro, tu instinto de venganza y de ira te hace ir por el lugar más peligroso a simple vista, donde estabas había una balsa medianamente decente, que en tu cabeza era buena idea, y de hecho, sí… El primer trayecto fue un poco turbulento, pero luego el rio desemboca y se calma haciendo de tu viaje hasta la mazmorra tranquilo. Pero de repente, casi llegando al final, el río se alborota y se vuelve incontrolable, intentas mantenerte a flote hasta llegar pero tu balsa se vuelca…")
            st.image(RUTA_GIF / "hadaPelirrojaEnLosRapidos.gif")

            if st.button("Continuar", key="textHadaBalsDentr3"):
                st.session_state.mostrarTextoComo = 2
                st.rerun()
        elif st.session_state.mostrarTextoComo ==2:
            st.write("Justo antes de caer un gato tricolor callejero rondaba por ahí, vio la situación e hizo sonar su campana, no entiendes bien que pasó pero saliste ilesa y tu cuerpo no dolía, cuando logras despertar estabas en el suelo y sobre ti había un amigo felino tricolor mirándote fijo, crees ver destellos dorados salir de su collar pero dudas")
            st.write("Felicidades! un compañero te eligió para acompañarte en tu aventura")
            st.image(RUTA_GIF / "encuentroGatito.gif")
            if st.button("Continuar", key="textHadaBalsDentr4"):
                st.session_state.mostrarTextoComo = 0
                st.rerun()

    #CAMINO DEL BOSQUE
    elif st.session_state.destino =="Bosque Brumoso" and st.session_state.cruce =="Volar Sobre el bosque":
        if st.session_state.mostrarTextoComo==1:
            st.write("Creíste que atravesar el bosque por fuera sería la opción más lógica. Pensaste que el cielo sería tranquilo, pero estabas equivocada. Apenas comenzaste a volar, un grupo de pájaros chocó contra ti y te desestabilizó por un momento." \
            "Un tramo de silencio inquietante comenzó a ponerte nerviosa. No estabas equivocada: ese bosque es tierra de nadie. Hadas de diferentes reinos luchan constantemente por dominar esos cielos.")
            st.write("Al verte, creyeron que eras un hada exploradora que estaba investigando el terreno para detectar posibles amenazas o complicaciones futuras (al menos, desde su perspectiva). Decidieron atacarte y lograron hacerte caer." \
            "Sin embargo, fuiste tan rápida que conseguiste llegar bastante cerca del final del recorrido antes de perder el conocimiento por la caída")
            st.image(RUTA_GIF / "hadaCaidaBosque.gif")

            if st.button("Continuar", key="textHadaBalsBorde"):
                st.session_state.mostrarTextoComo =2
                st.rerun()
        elif st.session_state.mostrarTextoComo ==2:
            st.write("Justo antes de caer, un gato tricolor callejero que rondaba por la zona presenció la situación e hizo sonar su campana. No entiendes muy bien qué sucedió, pero, de alguna manera, lograste salir ilesa y tu cuerpo no sentía ningún dolor." \
            "Cuando finalmente despiertas, te encuentras en el suelo, con un nuevo amigo felino tricolor observándote fijamente desde arriba. Por un instante, crees ver unos destellos dorados salir de su collar, aunque no estás del todo segura…")
            st.write("Felicidades! tienes un nuevo amigo que te acompañará en esta travesía")
            st.image(RUTA_GIF /"hadaRescateBosque.gif")
            if st.button("Continuar", key="textHadaBalsBorde2"):
                st.session_state.mostrarTextoComo = 0
                st.rerun()

    elif st.session_state.destino =="Bosque Brumoso" and st.session_state.cruce =="Cruzar Por Dentro":
        if st.session_state.mostrarTextoComo==1:
            st.write("Elegiste la mejor opción para atravesar este camino. El bosque es horrible, oscuro y tenebroso, pero no representa ningún peligro, siempre y cuando no pises mal ni te caigas. Mientras tengas cuidado, tu viaje será tranquilo. Consejo: evita mirar hacia arriba")
            st.image(hadaDentroBsque)
            if st.button("Continuar", key="textHadaBosqueDentro"):
                st.session_state.mostrarTextoComo =2
                st.rerun()
        elif st.session_state.mostrarTextoComo ==2:
            st.write("Estás llegando al final de tu camino… Pero… espera un momento, ¿qué es ese ruido? *escuchas ruido de madera, empiezas a tener miedo…* de la nada te cae una nuez en la cabeza")
            st.write("Lejos de asustarte mirás hacia la dirección donde la viste venir, unos ojos redondos y brillosos te miran desde esa dirección, es una ardilla!! pero no cualquier ardilla, destellos dorados salen de su nariz y orejas cuando te ven, acaso esta será una conexión…?")
            st.write("Felicidades! un compañero te eligió para acompañarte en tu aventura")
            st.image(RUTA_GIF / "hadaArdilla.gif")
            if st.button("Continuar", key="textHadaBosqueDentro"):
                st.session_state.mostrarTextoComo = 0
                st.rerun()

def informacion_hada():
    st.image(RUTA_GIF / "hadaDesterrada.gif")
    st.text(
        "Eres un hada que fue exiliada de su hogar, de su familia y de su aldea."
        "Luchaste por quedarte y te defendiste, pero la reina no te creyó, a pesar"
        "de que todo haya sido una confusión y el verdadero culpable sea otra persona. "
        "Tu exilio solo podrá ser redimido si enfrentas esta aventura. Si logras superarla,"
        "serás declarada inocente y podrás regresar a tu aldea. De lo contrario, "
        "tu peor destino será no volver a salir de la mazmorra… Te deseamos suerte"
    )

    if st.button("Continuar", key="continuar_historia_hada"):
        st.session_state.informacion = 0
        st.rerun()


def elegir_camino_hada():
    st.subheader(
        "Hiciste la elección de personaje, tu rumbo ha comenzado, elige tu camino"
    )

    destino = st.radio(
        "¿A dónde quieres ir?",
        ["Rio Bravo", "Bosque Brumoso"],
        key="destino_hada"
    )

    if st.button("Continuar", key="continuar_camino_hada"):
        st.session_state.destino = destino
        st.session_state.etapa = 3
        st.rerun()

#OPCION CRUZAR CAMINO
def etapa_3_hada():
    if st.session_state.destino == "Rio Bravo":
        st.header(
            "Empiezas tu recorrido por un río turbulento que intimida, "
            "rompe olas contra piedras filosas y hay muchísimo viento. "
            "¿Por dónde eliges ir?"
        )
        st.image(imgRioBravo, width=500)
        cruce = st.radio(
            "",
            ["Balsa por dentro", "Bordear el rio"],
            key="cruce_hada_rio"
        )

    elif st.session_state.destino == "Bosque Brumoso":
        st.subheader(
            "Inicias tu recorrido por un bosque cubierto de niebla,"
            "donde se respira un ambiente tenso y sombrío."
        )
        st.image(hadaBosque)
        cruce = st.radio(
            "",
            ["Volar Sobre el bosque", "Cruzar Por Dentro"],
            key="cruce_hada_bosque"
        )
    else:
        return

    if st.button("Continuar", key="continuar_cruce_hada"):
        st.session_state.cruce = cruce
        st.session_state.etapa = 4
        st.rerun()

#OPCION TENER MASCOTA
def etapa_4_hada():
    if st.session_state.cruce in [
        "Bordear el rio",
        "Cruzar Por Dentro"
    ]:
        st.session_state.mascota = "Ardilla"

    elif st.session_state.cruce in [
        "Balsa por dentro",
        "Volar Sobre el bosque"
    ]:
        st.session_state.mascota = "Gato Tricolor"

    st.session_state.etapa = "MAZMORRA"
    st.rerun()


def etapa_5_hada():
    if st.session_state.mascota == "Ardilla":
        st.write("Encuentras y entras a la mazmorra")
        st.write("Avanzas por un túnel que te conduce hacia el este (izquierda). Al llegar al final, te encuentras con dos posibles caminos. El primero tiene un aspecto tranquilo, sereno e inquietante. El segundo, en cambio, te resulta más familiar, casi como estar en tu propio hogar: algunas flores brotan de la entrada y todo parece rebosar de vida… ")
        st.image(hadaArdAntCam)
        sala = st.radio(
            "¿Con quién vas a luchar?",
            ["Pasillo Tranquilo", "Pasillo Familiar"],
            key="sala_hada_ardilla"
        )

    elif st.session_state.mascota == "Gato Tricolor":
        st.write("Avanzas por un túnel que te conduce hacia el este (izquierda). El lugar está oscuro y se escuchan muchos ruidos, pero crees que es la mejor entrada. Piensas que su aspecto tenebroso es solo un engaño para evitar que exploradores como tú se atrevan a entrar.")
        st.write("Más adelante, te encuentras con dos pasillos… ¿Cuál eliges?")
        st.image(hadaGatAntCam)
        sala = st.radio(
            "",
            ["Pasillo Izquierdo", "Pasillo Derecho"],
            key="sala_hada_gato"
        )
    else:
        return

    if st.button("Continuar", key="continuar_sala_hada"):
        st.session_state.salaInicial = sala
        st.session_state.etapa = 6
        st.rerun()


def etapa_6_hada():
    sala = st.session_state.salaInicial

    if sala == "Pasillo Tranquilo":
        st.write("Entras a una habitación en penumbras. Apenas cruzas la entrada, tus ojos no pueden creer lo que ven: entidades, personas, espíritus y toda clase de fantasmas que puedas imaginar deambulando por el lugar…" \
        "Te encuentras rodeado de fantasmas que buscan oro y objetos brillantes. Si no les das lo que quieren, podrían raptarte y no dejarte salir jamás.")
        st.image(RUTA_GIF /"hadaSalaFantasma.gif")
        opcion = st.radio(
            "¿qué hacés?",
            ["Polvo De Hadas", "¡snif snif!"],
            key="opcionPasilloTranquilo"
        )

    elif sala == "Pasillo Familiar":
        st.write("Entras por la puerta que elegiste y te encuentras con un hermoso campo de flores. Son las flores más bellas que jamás hayas visto. Tu pequeño amigo roedor está emocionado, pues nunca creyó que pudiera existir un lugar así." \
        "Comienzas a avanzar, pero, a medida que te adentras en el campo, notas que las flores desprenden un olor extraño, casi nauseabundo. ¡Malas noticias! Las flores son venenosas y liberan un hedor ácido que dificulta la respiración.")
        st.image(RUTA_GIF / "hadaFlores.gif")
        opcion = st.radio(
            "¿qué hacés?",
            ["Polvo De Hadas", "¡snif snif!"],
            key="opcionPasilloFamiliar"
        )

    elif sala == "Pasillo Izquierdo":
        st.write("Entras a una habitación llena de humedad.")
        st.write("El agua cae por todas partes y el suelo está completamente inundado de barro. Sientes cómo tus alas comienzan a volverse cada vez más pesadas debido al agua, impidiéndote seguir volando. Inevitablemente, no te queda otra opción que avanzar caminando." \
        "El barro te llega por debajo de las rodillas, pero, de repente, sientes que algo tira de tus piernas y dificulta tu avance. Frente a ti, una enorme montaña de barro comienza a elevarse. ¡Es un espíritu que utiliza el barro como cuerpo!")
        st.image(RUTA_GIF / "hadaAnteBarro.gif")
        opcion = st.radio(
            "¿qué haces?",
            ["Tintineo De Campana", "Cortar Mechon Del Cabello"],
            key="opcionPasilloIzquierdo"
        )

    elif sala == "Pasillo Derecho":
        st.write("Este pasillo está completamente oscuro. Apenas logras dar cinco pasos cuando, de repente, ¡el suelo desaparece bajo tus pies! Caes por un túnel y terminas en una habitación sumida en la oscuridad, donde se escuchan ruidos por todas partes." \
        "No sabes qué se esconde allí, pero tienes la certeza de que, si permaneces en ese lugar durante cinco minutos más, no podrás resistirlo.")
        st.image(hadaSubSue)
        opcion = st.radio(
            "¿que haces?",
            ["Tintineo De Campana", "Correr"],
            key="opcionPasilloDerecho"
        )

    else:
        return

    if st.button("Continuar", key="continuarBatallaHada"):
        st.session_state.opcionBatalla = opcion
        st.session_state.etapa = 7
        st.rerun()

def etapa_7_hada():

    if st.session_state.salaInicial =="Pasillo Derecho" and st.session_state.opcionBatalla=="Tintineo De Campana":
        st.write("De repente, escuchas un tintineo familiar: ¡es el mismo sonido que habías oído antes! Tu amigo felino está a tu lado, intentando llamar tu atención mientras mueve la pequeña campana de su collar. La campana comienza a brillar y te inclinas para tocarla.")
        st.image(hadaCampana)
        if st.button("Continuar"):
            st.session_state.condicionSalida = 1
            st.session_state.etapa = 8
            st.rerun()
    elif st.session_state.salaInicial =="Pasillo Derecho" and st.session_state.opcionBatalla=="Correr":
        st.write("Los ruidos no te permiten escuchar nada y la oscuridad te impide ver lo que tienes delante. Dos de tus sentidos están completamente bloqueados. Tu corazón comienza a acelerarse y tu mente se nubla por el miedo.")
        st.image(RUTA_GIF / "hadaGatitoLocos.gif")
        if st.button("Continuar"):
            st.session_state.condicionSalida = 2
            st.session_state.etapa = 8
            st.rerun()
    elif st.session_state.salaInicial =="Pasillo Izquierdo" and st.session_state.opcionBatalla=="Tintineo De Campana":
        st.write("Tu compañero intenta llamar tu atención y comienza a moverse inquieto. De pronto, ves una pequeña luz tenue. Recuerdas la caída en el bosque y aquellos destellos dorados. Intentas enfocar la vista y descubres que la luz proviene del collar de tu compañero. ")
        st.image(hadaBajLlu)
        if st.button("Continuar"):
            st.session_state.condicionSalida = 1
            st.session_state.etapa = 8
            st.rerun()
    elif st.session_state.salaInicial =="Pasillo Izquierdo" and st.session_state.opcionBatalla=="Cortar Mechon Del Cabello":
        st.write("Durante tus épocas de estudio, formaste parte de un grupo secreto dedicado a investigar magia prohibida, cuyos hechizos requieren utilizar partes de uno mismo como fuente de poder." \
        "Recuerdas uno de esos hechizos y decides ponerlo en práctica. Tomas un mechón de tu largo cabello y lo cortas. Según las enseñanzas, cuando un hada realiza este ritual, su cabello comienza a brillar y libera la luz mágica que lleva encerrada en su interior.")
        st.image(hadaCalva)
        if st.button("Continuar"):
            st.session_state.condicionSalida = 2
            st.session_state.etapa = 8
            st.rerun()
    elif st.session_state.salaInicial =="Pasillo Tranquilo" and st.session_state.opcionBatalla=="Polvo De Hadas":
        st.write("Eliges el polvo de hada y lo lanzas al aire como si fuera una lluvia. Al entrar en contacto con el ambiente, este crea una nube de humo acompañada de pequeñas explosiones que ciegan a los fantasmas. Aprovechas la confusión para escabullirte entre los rincones del lugar y desaparecer de su vista, evitando que puedan percibir tu presencia")
        st.write("Lamentablemente, tu hechizo no estaba lo suficientemente estudiado ni practicado. El polvo de hada funciona durante la primera mitad del recorrido, pero luego sus efectos comienzan a disiparse. Logras llegar hasta la puerta, pero, justo antes de cruzarla, un fantasma te agarra de los pies y comienza a arrastrarte hacia el interior.")
        st.image(RUTA_GIF /"hadaFantasmaMal.gif")
        if st.button("Continuar"):
            st.session_state.condicionSalida = 2
            st.session_state.etapa = 8
            st.rerun()
    elif st.session_state.salaInicial =="Pasillo Tranquilo" and st.session_state.opcionBatalla=="¡snif snif!":
        st.write("Eliges a tu ardilla. ¿Recuerdas los destellos dorados que salían de ella? Pues… ¡resulta que tiene poderes! Si permites que se suba a tu cabeza, podrá volverte invisible y ayudarte a pasar desapercibida entre los fantasmas.")
        st.image(RUTA_GIF/"hadaInvisible.gif")
        if st.button("Continuar"):
            st.session_state.condicionSalida = 1
            st.session_state.etapa = 8
            st.rerun()
    elif st.session_state.salaInicial =="Pasillo Familiar" and st.session_state.opcionBatalla=="Polvo De Hadas":
        st.write("Comienzas a buscar una solución y recuerdas tus clases de magia, aquellas que recibías antes de ser exiliada. De pronto, un hechizo viene a tu memoria. Lo combinas con tu polvo de hada y logras neutralizar el veneno que desprenden las flores.")
        st.image(RUTA_GIF / "hadaSinNiebla.gif")
        if st.button("Continuar"):
            st.session_state.condicionSalida = 2
            st.session_state.etapa = 8
            st.rerun()
    elif st.session_state.salaInicial =="Pasillo Familiar" and st.session_state.opcionBatalla=="¡snif snif!":
        st.write("En medio de la desesperación, tu pequeño amigo roedor llama tu atención. Al mirarlo, notas que su pelaje comienza a brillar. ¡Lo que viste en el bosque no era mentira! ¡Él también tiene poderes!")
        st.write(hadaFloresMag)
        if st.button("Continuar"):
            st.session_state.condicionSalida = 1
            st.session_state.etapa = 8
            st.rerun()
    else:
        st.error("No se encontró una combinación válida")
        st.write("Sala recibida:", repr(st.session_state.salaInicial))
        st.write("Opción recibida:", repr(st.session_state.opcionBatalla))

def infoSalia():
    if st.session_state.condicionSalida == 2:
        st.error("No lograste Escapar De La Mazmorra")
        if st.button("Continuar"):
            st.session_state.etapa = 10
            st.rerun()
    elif st.session_state.condicionSalida == 1:
        st.success("Felicidades! lograste Escapar De La Mazmorra")
        if st.button("Continuar"):
            st.session_state.etapa = 10
            st.rerun()


def finalAventura():
    if st.session_state.salaInicial =="Pasillo Izquierdo" and st.session_state.opcionBatalla=="Tintineo De Campana":
        st.write("En ese instante, su brillo se fusiona con el tuyo y ambos generan una luz tan intensa que encandila al espíritu y lo seca en cuestión de segundos, dejando todo el barro completamente seco y al espíritu atrapado en su interior.")
        st.image(RUTA_GIF / "hadaEscapaBarro.gif")
        if st.button("Continuar"):
            st.session_state.etapa = 9
            st.rerun()
    elif st.session_state.salaInicial =="Pasillo Izquierdo" and st.session_state.opcionBatalla=="Cortar Mechon Del Cabello":
        st.write("Lamentablemente, el brillo no es lo suficientemente intenso como para secar al espíritu ni todo el barro que lo rodea. El poder se consume rápidamente y el espíritu recupera sus fuerzas.")
        st.image(RUTA_GIF/ "hadaMostroFallo.gif")
        if st.button("Continuar"):
            st.session_state.etapa = 9
            st.rerun()
    elif st.session_state.salaInicial =="Pasillo Derecho" and st.session_state.opcionBatalla=="Tintineo De Campana":
        st.write("Acercas tu mano para tocar la campana y, al instante, esta comienza a brillar e ilumina toda la habitación. Finalmente, descubres que los ruidos no eran más que unos cuantos insectos chocando contra objetos metálicos. Se trata de insectos comunes, aunque parecen estar sumidos en una extraña locura.")
        st.write("Tu amigo felino y tú deciden avanzar apartándolos del camino. No representan ningún peligro para ustedes y, al quedar iluminados por la campana, los insectos comienzan a tranquilizarse.")
        st.image(RUTA_GIF/ "hadaGatitoLuz.gif")
        if st.button("Continuar"):
            st.session_state.etapa = 9
            st.rerun()
    elif st.session_state.salaInicial =="Pasillo Derecho" and st.session_state.opcionBatalla=="Correr":
        st.write("Solo alcanzas a sentir cómo tu compañero felino se altera, lo que te pone aún más nerviosa. Lo tomas entre tus brazos y comienzas a correr sin rumbo, intentando escapar de lo que sea que se encuentre en ese lugar. Pero, en medio de la desesperación, terminas chocando contra una pared…")
        st.image(RUTA_GIF / "hadaContraPared.gif")
        if st.button("Continuar"):
            st.session_state.etapa = 9
            st.rerun()
    elif st.session_state.salaInicial =="Pasillo Tranquilo" and st.session_state.opcionBatalla=="Polvo De Hadas":
        st.session_state.etapa = 9
        st.rerun()
    elif st.session_state.salaInicial =="Pasillo Tranquilo" and st.session_state.opcionBatalla=="¡snif snif!":
        st.write("¡Muy bien! Ahora debes ser cuidadosa: no hagas ruido y continúa avanzando. Como eres un hada, puedes volar lentamente para hacer el menor ruido posible y evitar tocar a cualquiera de los fantasmas.")
        st.image(RUTA_GIF / "hadaArdillaEscape.gif")
        if st.button("Continuar"):
            st.session_state.etapa = 9
            st.rerun()
    elif st.session_state.salaInicial =="Pasillo Familiar" and st.session_state.opcionBatalla=="Polvo De Hadas":
        st.write("Continúas avanzando lo más rápido posible para conseguir salir del campo, pero hay un pequeño detalle que no habías tenido en cuenta: sin el veneno que liberan, las plantas se vuelven agresivas. Logras protegerte de sus toxinas, ¡pero no consigues escapar de sus rasguños!")
        st.write("Los rasguños de las plantas comienzan a lastimarte y debilitarte cada vez más a medida que intentas encontrar la salida. A pesar de tus esfuerzos, no consigues atravesar el campo de flores.")
        st.image(RUTA_GIF / "hadaEspinas.gif")
        if st.button("Continuar"):
            st.session_state.etapa = 9
            st.rerun()
    elif st.session_state.salaInicial =="Pasillo Familiar" and st.session_state.opcionBatalla=="¡snif snif!":
        st.write("Tu ardilla comienza a trepar por tu cuerpo hasta llegar a tu cabeza. Allí, su brillo se intensifica cada vez más hasta generar una burbuja protectora que te mantiene a salvo de todos los gases venenosos.")
        st.write("Como no necesitas combatir ni neutralizar los gases, las flores permanecen dormidas. Aprovechas la oportunidad para avanzar de manera sigilosa y tranquila, sin despertarlas.Las flores no llegaron a despertarse y conseguiste llegar hasta el final. ")
        st.image(RUTA_GIF / "hadaEscudo.gif")
        if st.button("Continuar"):
            st.session_state.etapa = 9
            st.rerun()

def main_hada():
    etapa = st.session_state.etapa

    if etapa == 2:
        if st.session_state.informacion == 1:
            informacion_hada()
        else:
            elegir_camino_hada()
    elif etapa == 3:
        etapa_3_hada()
    elif etapa == 4:
        if st.session_state.mostrarTextoComo==1 or st.session_state.mostrarTextoComo==2:
            textoCruce()
        else:
            etapa_4_hada()
    elif etapa == 5:
        etapa_5_hada()
    elif etapa == 6:
        etapa_6_hada()
    elif etapa == 7:
        etapa_7_hada()
    elif etapa == 8:
        finalAventura()
    elif etapa ==9:
        infoSalia()


#python -m streamlit run practica.py
