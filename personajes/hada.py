import streamlit as st
from pathlib import Path

# Ruta absoluta de la carpeta principal del proyecto
RUTA_PROYECTO = Path(__file__).resolve().parent.parent

# Carpetas de recursos
RUTA_IMG = RUTA_PROYECTO / "assets" / "hada" / "img"
RUTA_GIF = RUTA_PROYECTO / "assets" / "hada" / "gif"


def mostrar_escena(parrafos, media, botones, clave_prefix=""):
    """Dibuja la imagen a la izquierda y la historia con botones directos a la derecha."""
    col_izq, col_der = st.columns([1, 1.15], gap="large")

    with col_izq:
        st.image(str(media), use_container_width=True)

    with col_der:
        with st.container(border=True):
            for p in parrafos:
                st.write(p)

            st.markdown("---")
            cols = st.columns(len(botones))
            for i, texto_btn in enumerate(botones):
                if cols[i].button(texto_btn, key=f"{clave_prefix}_{i}", use_container_width=True):
                    return texto_btn

    return None


def textoCruce():
    # CAMINO RIO BRAVO
    if st.session_state.destino == "Rio Bravo" and st.session_state.cruce == "Bordear el rio":
        if st.session_state.mostrarTextoComo == 1:
            if mostrar_escena(
                parrafos=[
                    "Eliges bordear el río. Piensas que es mejor realizar un trabajo duro que arriesgarte a tomar un camino peligroso. El recorrido comienza siendo complicado. Te sientes observada y ansiosa, lo que provoca que tropieces y termines lastimándote. Llegas a mitad de camino y sientes que ya no puedes continuar. De repente, una manada de perros aparece frente a ti, gruñendo y mostrándose amenazantes.",
                    "El miedo te invade y te impide reaccionar con claridad. El cansancio acumulado tampoco ayuda, pero… desde lo más alto de los árboles que te rodean, comienzan a salir disparados unos finos balines que se dirigen hacia los lobos. Estos se asustan, se desorientan y salen corriendo en distintas direcciones, olvidándose por completo de ti. Sin embargo, todo lo ocurrido termina pasándote factura y pierdes el conocimiento. Unos momentos después, despiertas sin entender muy bien qué sucedió. Aún confundida, decides continuar por el camino…"
                ],
                media=RUTA_GIF / "hadaBordearRio.gif",
                botones=["Continuar ➡️"],
                clave_prefix="textHadaBalsBorde"
            ):
                st.session_state.mostrarTextoComo = 2
                st.rerun()

        elif st.session_state.mostrarTextoComo == 2:
            if mostrar_escena(
                parrafos=[
                    "Estás llegando al final de tu camino… Pero espera un momento, ¿qué es ese ruido? Escuchas un crujido de madera y empiezas a sentir miedo… De repente, una nuez cae sobre tu cabeza.",
                    "Lejos de asustarte, miras en la dirección de donde provino. Unos ojos redondos y brillantes te observan desde allí. ¡Es una ardilla! Pero no una ardilla cualquiera: destellos dorados brotan de su nariz y sus orejas al verte. ¿Acaso esto será el inicio de una conexión especial…?",
                    "✨ ¡Felicidades! Un compañero te eligió para acompañarte en tu aventura."
                ],
                media=RUTA_GIF / "hadaArdilla.gif",
                botones=["Continuar ➡️"],
                clave_prefix="textHadaBalsBorde2"
            ):
                st.session_state.mostrarTextoComo = 0
                st.rerun()

    elif st.session_state.destino == "Rio Bravo" and st.session_state.cruce == "Balsa por dentro":
        if st.session_state.mostrarTextoComo == 1:
            if mostrar_escena(
                parrafos=[
                    "Eliges atravesar el río por dentro. Tu instinto de venganza y tu ira te impulsan a tomar el camino que, a simple vista, parece el más peligroso. En la orilla encuentras una balsa medianamente decente que, en ese momento, te parece una buena idea.",
                    "Y de hecho... ¡lo es! El primer tramo del recorrido resulta un poco turbulento, pero luego el río desemboca en una zona más tranquila, haciendo que tu viaje hacia la mazmorra sea mucho más llevadero.",
                    "Sin embargo, cuando estás a punto de llegar al final, el río vuelve a alborotarse y se vuelve completamente incontrolable. Intentas mantenerte a flote hasta alcanzar la orilla, pero, de repente, ¡tu balsa se vuelca…!"
                ],
                media=RUTA_GIF / "hadaPelirrojaEnLosRapidos.gif",
                botones=["Continuar ➡️"],
                clave_prefix="textHadaBalsDentr3"
            ):
                st.session_state.mostrarTextoComo = 2
                st.rerun()

        elif st.session_state.mostrarTextoComo == 2:
            if mostrar_escena(
                parrafos=[
                    "Justo antes de caer un gato tricolor callejero rondaba por ahí, vio la situación e hizo sonar su campana, no entiendes bien qué pasó pero saliste ilesa y tu cuerpo no dolía. Cuando logras despertar estabas en el suelo y sobre ti había un amigo felino tricolor mirándote fijo; crees ver destellos dorados salir de su collar pero dudas.",
                    "✨ ¡Felicidades! Un compañero te eligió para acompañarte en tu aventura."
                ],
                media=RUTA_GIF / "encuentroGatito.gif",
                botones=["Continuar ➡️"],
                clave_prefix="textHadaBalsDentr4"
            ):
                st.session_state.mostrarTextoComo = 0
                st.rerun()

    # CAMINO DEL BOSQUE
    elif st.session_state.destino == "Bosque Brumoso" and st.session_state.cruce == "Volar Sobre el bosque":
        if st.session_state.mostrarTextoComo == 1:
            if mostrar_escena(
                parrafos=[
                    "Creíste que atravesar el bosque por fuera sería la opción más lógica. Pensaste que el cielo sería tranquilo, pero estabas equivocada. Apenas comenzaste a volar, un grupo de pájaros chocó contra ti y te desestabilizó por un momento. Un tramo de silencio inquietante comenzó a ponerte nerviosa. No estabas equivocada: ese bosque es tierra de nadie. Hadas de diferentes reinos luchan constantemente por dominar esos cielos.",
                    "Al verte, creyeron que eras un hada exploradora que estaba investigando el terreno para detectar posibles amenazas o complicaciones futuras (al menos, desde su perspectiva). Decidieron atacarte y lograron hacerte caer. Sin embargo, fuiste tan rápida que conseguiste llegar bastante cerca del final del recorrido antes de perder el conocimiento por la caída."
                ],
                media=RUTA_GIF / "hadaCaidaBosque.gif",
                botones=["Continuar ➡️"],
                clave_prefix="textHadaBosqueVolar1"
            ):
                st.session_state.mostrarTextoComo = 2
                st.rerun()

        elif st.session_state.mostrarTextoComo == 2:
            if mostrar_escena(
                parrafos=[
                    "Justo antes de caer, un gato tricolor callejero que rondaba por la zona presenció la situación e hizo sonar su campana. No entiendes muy bien qué sucedió, pero, de alguna manera, lograste salir ilesa y tu cuerpo no sentía ningún dolor. Cuando finalmente despiertas, te encuentras en el suelo, con un nuevo amigo felino tricolor observándote fijamente desde arriba. Por un instante, crees ver unos destellos dorados salir de su collar, aunque no estás del todo segura…",
                    "✨ ¡Felicidades! Tienes un nuevo amigo que te acompañará en esta travesía."
                ],
                media=RUTA_GIF / "hadaRescateBosque.gif",
                botones=["Continuar ➡️"],
                clave_prefix="textHadaBosqueVolar2"
            ):
                st.session_state.mostrarTextoComo = 0
                st.rerun()

    elif st.session_state.destino == "Bosque Brumoso" and st.session_state.cruce == "Cruzar Por Dentro":
        if st.session_state.mostrarTextoComo == 1:
            if mostrar_escena(
                parrafos=[
                    "Elegiste la mejor opción para atravesar este camino. El bosque es horrible, oscuro y tenebroso, pero no representa ningún peligro, siempre y cuando no pises mal ni te caigas. Mientras tengas cuidado, tu viaje será tranquilo.",
                    "Consejo: evita mirar hacia arriba."
                ],
                media=RUTA_IMG / "hadaDentroBosque.png",
                botones=["Continuar ➡️"],
                clave_prefix="textHadaBosqueDentro1"
            ):
                st.session_state.mostrarTextoComo = 2
                st.rerun()

        elif st.session_state.mostrarTextoComo == 2:
            if mostrar_escena(
                parrafos=[
                    "Estás llegando al final de tu camino… Pero… espera un momento, ¿qué es ese ruido? *Escuchas ruido de madera, empiezas a tener miedo…* De la nada te cae una nuez en la cabeza.",
                    "Lejos de asustarte mirás hacia la dirección donde la viste venir: unos ojos redondos y brillosos te miran desde esa dirección. ¡Es una ardilla! Pero no cualquier ardilla: destellos dorados salen de su nariz y orejas cuando te ven. ¿Acaso esta será una conexión…?",
                    "✨ ¡Felicidades! Un compañero te eligió para acompañarte en tu aventura."
                ],
                media=RUTA_GIF / "hadaArdilla.gif",
                botones=["Continuar ➡️"],
                clave_prefix="textHadaBosqueDentro2"
            ):
                st.session_state.mostrarTextoComo = 0
                st.rerun()


def informacion_hada():
    if mostrar_escena(
        parrafos=[
            "Eres un hada que fue exiliada de su hogar, de su familia y de su aldea. Luchaste por quedarte y te defendiste, pero la reina no te creyó, a pesar de que todo haya sido una confusión y el verdadero culpable sea otra persona.",
            "Tu exilio solo podrá ser redimido si enfrentas esta aventura. Si logras superarla, serás declarada inocente y podrás regresar a tu aldea. De lo contrario, tu peor destino será no volver a salir de la mazmorra…",
            "Te deseamos suerte."
        ],
        media=RUTA_GIF / "hadaDesterrada.gif",
        botones=["Comenzar mi travesía ➡️"],
        clave_prefix="continuar_historia_hada"
    ):
        st.session_state.informacion = 0
        st.rerun()


def elegir_camino_hada():
    st.markdown("<h3 style='text-align: center;'>Hiciste la elección de personaje, tu rumbo ha comenzado</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>¿A dónde quieres ir?</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")
    with col1:
        with st.container(border=True):
            st.image(str(RUTA_IMG / "hadaAnteElRioTempestuoso.png"), use_container_width=True)
            if st.button("🌊 Rio Bravo", key="btn_destino_rio", use_container_width=True):
                st.session_state.destino = "Rio Bravo"
                st.session_state.etapa = 3
                st.rerun()

    with col2:
        with st.container(border=True):
            st.image(str(RUTA_IMG / "hadaEnBosque.png"), use_container_width=True)
            if st.button("🌲 Bosque Brumoso", key="btn_destino_bosque", use_container_width=True):
                st.session_state.destino = "Bosque Brumoso"
                st.session_state.etapa = 3
                st.rerun()


def etapa_3_hada():
    if st.session_state.destino == "Rio Bravo":
        eleccion = mostrar_escena(
            parrafos=[
                "Comienzas tu recorrido junto a un río turbulento e intimidante. Las olas rompen violentamente contra las piedras afiladas de la orilla, mientras fuertes ráfagas de viento azotan todo a tu alrededor.",
                "El camino no parece nada sencillo… ¿Por dónde eliges ir?"
            ],
            media=RUTA_IMG / "hadaAnteElRioTempestuoso.png",
            botones=["Balsa por dentro", "Bordear el rio"],
            clave_prefix="cruce_hada_rio"
        )
    elif st.session_state.destino == "Bosque Brumoso":
        eleccion = mostrar_escena(
            parrafos=[
                "Inicias tu recorrido por un bosque cubierto de niebla, donde se respira un ambiente tenso y sombrío.",
                "¿Cómo decides cruzarlo?"
            ],
            media=RUTA_IMG / "hadaEnBosque.png",
            botones=["Volar Sobre el bosque", "Cruzar Por Dentro"],
            clave_prefix="cruce_hada_bosque"
        )
    else:
        return

    if eleccion:
        st.session_state.cruce = eleccion
        st.session_state.etapa = 4
        st.rerun()


def etapa_4_hada():
    if st.session_state.cruce in ["Bordear el rio", "Cruzar Por Dentro"]:
        st.session_state.mascota = "Ardilla"
    elif st.session_state.cruce in ["Balsa por dentro", "Volar Sobre el bosque"]:
        st.session_state.mascota = "Gato Tricolor"

    st.session_state.etapa = "MAZMORRA"
    st.rerun()


def etapa_5_hada():
    if st.session_state.mascota == "Ardilla":
        eleccion = mostrar_escena(
            parrafos=[
                "Encuentras y entras a la mazmorra.",
                "Avanzas por un túnel que te conduce hacia el este (izquierda). Al llegar al final, te encuentras con dos posibles caminos. El primero tiene un aspecto tranquilo, sereno e inquietante. El segundo, en cambio, te resulta más familiar, casi como estar en tu propio hogar: algunas flores brotan de la entrada y todo parece rebosar de vida…",
                "¿Qué camino tomas?"
            ],
            media=RUTA_IMG / "hadaArdiAnteCamino.png",
            botones=["Pasillo Tranquilo", "Pasillo Familiar"],
            clave_prefix="sala_hada_ardilla"
        )
    elif st.session_state.mascota == "Gato Tricolor":
        eleccion = mostrar_escena(
            parrafos=[
                "Avanzas por un túnel que te conduce hacia el este. El lugar está oscuro y se escuchan muchos ruidos, pero crees que es la mejor entrada. Piensas que su aspecto tenebroso es solo un engaño para evitar que exploradores como tú se atrevan a entrar.",
                "Más adelante, te encuentras con dos pasillos… ¿Cuál eliges?"
            ],
            media=RUTA_IMG / "hadaGatoAnteCamino.png",
            botones=["Pasillo Izquierdo", "Pasillo Derecho"],
            clave_prefix="sala_hada_gato"
        )
    else:
        return

    if eleccion:
        st.session_state.salaInicial = eleccion
        st.session_state.etapa = 6
        st.rerun()


def etapa_6_hada():
    sala = st.session_state.salaInicial

    if sala == "Pasillo Tranquilo":
        eleccion = mostrar_escena(
            parrafos=[
                "Entras a una habitación en penumbras. Apenas cruzas la entrada, tus ojos no pueden creer lo que ven: entidades, personas, espíritus y toda clase de fantasmas que puedas imaginar deambulando por el lugar…",
                "Te encuentras rodeada de fantasmas que buscan oro y objetos brillantes. Si no les das lo que quieren, podrían raptarte y no dejarte salir jamás. ¿Qué hacés?"
            ],
            media=RUTA_GIF / "hadaSalaFantasma.gif",
            botones=["Polvo De Hadas", "¡snif snif!"],
            clave_prefix="opcionPasilloTranquilo"
        )
    elif sala == "Pasillo Familiar":
        eleccion = mostrar_escena(
            parrafos=[
                "Entras por la puerta que elegiste y te encuentras con un hermoso campo de flores. Son las flores más bellas que jamás hayas visto. Tu pequeño amigo roedor está emocionado, pues nunca creyó que pudiera existir un lugar así.",
                "Comienzas a avanzar, pero, a medida que te adentras en el campo, notas que las flores desprenden un olor extraño, casi nauseabundo. ¡Malas noticias! Las flores son venenosas y liberan un hedor ácido que dificulta la respiración. ¿Qué hacés?"
            ],
            media=RUTA_GIF / "hadaFlores.gif",
            botones=["Polvo De Hadas", "¡snif snif!"],
            clave_prefix="opcionPasilloFamiliar"
        )
    elif sala == "Pasillo Izquierdo":
        eleccion = mostrar_escena(
            parrafos=[
                "Entras a una habitación llena de humedad. El agua cae por todas partes y el suelo está completamente inundado de barro. Sientes cómo tus alas comienzan a volverse cada vez más pesadas debido al agua, impidiéndote seguir volando.",
                "El barro te llega por debajo de las rodillas, pero, de repente, sientes que algo tira de tus piernas y dificulta tu avance. Frente a ti, una enorme montaña de barro comienza a elevarse. ¡Es un espíritu que utiliza el barro como cuerpo! ¿Qué haces?"
            ],
            media=RUTA_GIF / "hadaAnteBarro.gif",
            botones=["Tintineo De Campana", "Cortar Mechon Del Cabello"],
            clave_prefix="opcionPasilloIzquierdo"
        )
    elif sala == "Pasillo Derecho":
        eleccion = mostrar_escena(
            parrafos=[
                "Este pasillo está completamente oscuro. Apenas logras dar cinco pasos cuando, de repente, ¡el suelo desaparece bajo tus pies! Caes por un túnel y terminas en una habitación sumida en la oscuridad, donde se escuchan ruidos por todas partes.",
                "No sabes qué se esconde allí, pero tienes la certeza de que, si permaneces en ese lugar durante cinco minutos más, no podrás resistirlo. ¿Qué haces?"
            ],
            media=RUTA_IMG / "hadaEnSubSuelo.png",
            botones=["Tintineo De Campana", "Correr"],
            clave_prefix="opcionPasilloDerecho"
        )
    else:
        return

    if eleccion:
        st.session_state.opcionBatalla = eleccion
        st.session_state.etapa = 7
        st.rerun()


def etapa_7_hada():
    sala = st.session_state.salaInicial
    opcion = st.session_state.opcionBatalla

    if sala == "Pasillo Derecho" and opcion == "Tintineo De Campana":
        if mostrar_escena(
            parrafos=[
                "De repente, escuchas un tintineo familiar: ¡es el mismo sonido que habías oído antes! Tu amigo felino está a tu lado, intentando llamar tu atención mientras mueve la pequeña campana de su collar. La campana comienza a brillar y te inclinas para tocarla."
            ],
            media=RUTA_IMG / "hadaCampanaGato.png",
            botones=["Continuar ➡️"],
            clave_prefix="et7_hada_1"
        ):
            st.session_state.condicionSalida = 1
            st.session_state.etapa = 8
            st.rerun()

    elif sala == "Pasillo Derecho" and opcion == "Correr":
        if mostrar_escena(
            parrafos=[
                "Los ruidos no te permiten escuchar nada y la oscuridad te impide ver lo que tienes delante. Dos de tus sentidos están completamente bloqueados. Tu corazón comienza a acelerarse y tu mente se nubla por el miedo."
            ],
            media=RUTA_GIF / "hadaGatitoLocos.gif",
            botones=["Continuar ➡️"],
            clave_prefix="et7_hada_2"
        ):
            st.session_state.condicionSalida = 2
            st.session_state.etapa = 8
            st.rerun()

    elif sala == "Pasillo Izquierdo" and opcion == "Tintineo De Campana":
        if mostrar_escena(
            parrafos=[
                "Tu compañero intenta llamar tu atención y comienza a moverse inquieto. De pronto, ves una pequeña luz tenue. Recuerdas la caída en el bosque y aquellos destellos dorados. Intentas enfocar la vista y descubres que la luz proviene del collar de tu compañero."
            ],
            media=RUTA_IMG / "gataBajoLaLluvia.png",
            botones=["Continuar ➡️"],
            clave_prefix="et7_hada_3"
        ):
            st.session_state.condicionSalida = 1
            st.session_state.etapa = 8
            st.rerun()

    elif sala == "Pasillo Izquierdo" and opcion == "Cortar Mechon Del Cabello":
        if mostrar_escena(
            parrafos=[
                "Durante tus épocas de estudio, formaste parte de un grupo secreto dedicado a investigar magia prohibida, cuyos hechizos requieren utilizar partes de uno mismo como fuente de poder.",
                "Recuerdas uno de esos hechizos y decides ponerlo en práctica. Tomas un mechón de tu largo cabello y lo cortas. Según las enseñanzas, cuando un hada realiza este ritual, su cabello comienza a brillar y libera la luz mágica que lleva encerrada en su interior."
            ],
            media=RUTA_IMG / "hadaCorte.png",
            botones=["Continuar ➡️"],
            clave_prefix="et7_hada_4"
        ):
            st.session_state.condicionSalida = 2
            st.session_state.etapa = 8
            st.rerun()

    elif sala == "Pasillo Tranquilo" and opcion == "Polvo De Hadas":
        if mostrar_escena(
            parrafos=[
                "Eliges el polvo de hada y lo lanzas al aire como si fuera una lluvia. Al entrar en contacto con el ambiente, este crea una nube de humo acompañada de pequeñas explosiones que ciegan a los fantasmas. Aprovechas la confusión para escabullirte entre los rincones del lugar y desaparecer de su vista.",
                "Lamentablemente, tu hechizo no estaba lo suficientemente estudiado ni practicado. El polvo de hada funciona durante la primera mitad del recorrido, pero luego sus efectos comienzan a disiparse. Logras llegar hasta la puerta, pero, justo antes de cruzarla, un fantasma te agarra de los pies y comienza a arrastrarte hacia el interior."
            ],
            media=RUTA_GIF / "hadaFantasmaMal.gif",
            botones=["Continuar ➡️"],
            clave_prefix="et7_hada_5"
        ):
            st.session_state.condicionSalida = 2
            st.session_state.etapa = 8
            st.rerun()

    elif sala == "Pasillo Tranquilo" and opcion == "¡snif snif!":
        if mostrar_escena(
            parrafos=[
                "Eliges a tu ardilla. ¿Recuerdas los destellos dorados que salían de ella? Pues… ¡resulta que tiene poderes! Si permites que se suba a tu cabeza, podrá volverte invisible y ayudarte a pasar desapercibida entre los fantasmas."
            ],
            media=RUTA_GIF / "hadaInvisible.gif",
            botones=["Continuar ➡️"],
            clave_prefix="et7_hada_6"
        ):
            st.session_state.condicionSalida = 1
            st.session_state.etapa = 8
            st.rerun()

    elif sala == "Pasillo Familiar" and opcion == "Polvo De Hadas":
        if mostrar_escena(
            parrafos=[
                "Comienzas a buscar una solución y recuerdas tus clases de magia, aquellas que recibías antes de ser exiliada. De pronto, un hechizo viene a tu memoria. Lo combinas con tu polvo de hada y logras neutralizar el veneno que desprenden las flores."
            ],
            media=RUTA_GIF / "hadaSinNiebla.gif",
            botones=["Continuar ➡️"],
            clave_prefix="et7_hada_7"
        ):
            st.session_state.condicionSalida = 2
            st.session_state.etapa = 8
            st.rerun()

    elif sala == "Pasillo Familiar" and opcion == "¡snif snif!":
        if mostrar_escena(
            parrafos=[
                "En medio de la desesperación, tu pequeño amigo roedor llama tu atención. Al mirarlo, notas que su pelaje comienza a brillar. ¡Lo que viste en el bosque no era mentira! ¡Él también tiene poderes!"
            ],
            media=RUTA_IMG / "hadaEncuentroFlores.png",
            botones=["Continuar ➡️"],
            clave_prefix="et7_hada_8"
        ):
            st.session_state.condicionSalida = 1
            st.session_state.etapa = 8
            st.rerun()


def infoSalia():
    if st.session_state.condicionSalida == 2:
        st.error("💀 No lograste escapar de la mazmorra")
        if st.button("Continuar ➡️", key="fin_malo_hada"):
            st.session_state.etapa = 10
            st.rerun()
    elif st.session_state.condicionSalida == 1:
        st.success("🏆 ¡Felicidades! Lograste escapar de la mazmorra")
        if st.button("Continuar ➡️", key="fin_bueno_hada"):
            st.session_state.etapa = 10
            st.rerun()


def finalAventura():
    sala = st.session_state.salaInicial
    opcion = st.session_state.opcionBatalla

    if sala == "Pasillo Izquierdo" and opcion == "Tintineo De Campana":
        if mostrar_escena(
            parrafos=[
                "En ese instante, su brillo se fusiona con el tuyo y ambos generan una luz tan intensa que encandila al espíritu y lo seca en cuestión de segundos, dejando todo el barro completamente seco y al espíritu atrapado en su interior."
            ],
            media=RUTA_GIF / "hadaEscapaBarro.gif",
            botones=["Continuar ➡️"],
            clave_prefix="fin_hada_1"
        ):
            st.session_state.etapa = 9
            st.rerun()

    elif sala == "Pasillo Izquierdo" and opcion == "Cortar Mechon Del Cabello":
        if mostrar_escena(
            parrafos=[
                "Lamentablemente, el brillo no es lo suficientemente intenso como para secar al espíritu ni todo el barro que lo rodea. El poder se consume rápidamente y el espíritu recupera sus fuerzas."
            ],
            media=RUTA_GIF / "hadaMostroFallo.gif",
            botones=["Continuar ➡️"],
            clave_prefix="fin_hada_2"
        ):
            st.session_state.etapa = 9
            st.rerun()

    elif sala == "Pasillo Derecho" and opcion == "Tintineo De Campana":
        if mostrar_escena(
            parrafos=[
                "Acercas tu mano para tocar la campana y, al instante, esta comienza a brillar e ilumina toda la habitación. Finalmente, descubres que los ruidos no eran más que unos cuantos insectos chocando contra objetos metálicos. Se trata de insectos comunes, aunque parecen estar sumidos en una extraña locura.",
                "Tu amigo felino y tú deciden avanzar apartándolos del camino. No representan ningún peligro para ustedes y, al quedar iluminados por la campana, los insectos comienzan a tranquilizarse."
            ],
            media=RUTA_GIF / "hadaGatitoLuz.gif",
            botones=["Continuar ➡️"],
            clave_prefix="fin_hada_3"
        ):
            st.session_state.etapa = 9
            st.rerun()

    elif sala == "Pasillo Derecho" and opcion == "Correr":
        if mostrar_escena(
            parrafos=[
                "Solo alcanzas a sentir cómo tu compañero felino se altera, lo que te pone aún más nerviosa. Lo tomas entre tus brazos y comienzas a correr sin rumbo, intentando escapar de lo que sea que se encuentre en ese lugar. Pero, en medio de la desesperación, terminas chocando contra una pared…"
            ],
            media=RUTA_GIF / "hadaContraPared.gif",
            botones=["Continuar ➡️"],
            clave_prefix="fin_hada_4"
        ):
            st.session_state.etapa = 9
            st.rerun()

    elif sala == "Pasillo Tranquilo" and opcion == "Polvo De Hadas":
        st.session_state.etapa = 9
        st.rerun()

    elif sala == "Pasillo Tranquilo" and opcion == "¡snif snif!":
        if mostrar_escena(
            parrafos=[
                "¡Muy bien! Ahora debes ser cuidadosa: no hagas ruido y continúa avanzando. Como eres un hada, puedes volar lentamente para hacer el menor ruido posible y evitar tocar a cualquiera de los fantasmas."
            ],
            media=RUTA_GIF / "hadaArdillaEscape.gif",
            botones=["Continuar ➡️"],
            clave_prefix="fin_hada_5"
        ):
            st.session_state.etapa = 9
            st.rerun()

    elif sala == "Pasillo Familiar" and opcion == "Polvo De Hadas":
        if mostrar_escena(
            parrafos=[
                "Continúas avanzando lo más rápido posible para conseguir salir del campo, pero hay un pequeño detalle que no habías tenido en cuenta: sin el veneno que liberan, las plantas se vuelven agresivas. Logras protegerte de sus toxinas, ¡pero no consigues escapar de sus rasguños!",
                "Los rasguños de las plantas comienzan a lastimarte y debilitarte cada vez más a medida que intentas encontrar la salida. A pesar de tus esfuerzos, no consigues atravesar el campo de flores."
            ],
            media=RUTA_GIF / "hadaEspinas.gif",
            botones=["Continuar ➡️"],
            clave_prefix="fin_hada_6"
        ):
            st.session_state.etapa = 9
            st.rerun()

    elif sala == "Pasillo Familiar" and opcion == "¡snif snif!":
        if mostrar_escena(
            parrafos=[
                "Tu ardilla comienza a trepar por tu cuerpo hasta llegar a tu cabeza. Allí, su brillo se intensifica cada vez más hasta generar una burbuja protectora que te mantiene a salvo de todos los gases venenosos.",
                "Como no necesitas combatir ni neutralizar los gases, las flores permanecen dormidas. Aprovechas la oportunidad para avanzar de manera sigilosa y tranquila, sin despertarlas. Las flores no llegaron a despertarse y conseguiste llegar hasta el final."
            ],
            media=RUTA_GIF / "hadaEscudo.gif",
            botones=["Continuar ➡️"],
            clave_prefix="fin_hada_7"
        ):
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
        if st.session_state.mostrarTextoComo in [1, 2]:
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
    elif etapa == 9:
        infoSalia()
