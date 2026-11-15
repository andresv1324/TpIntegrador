import streamlit as st

def textoCruce():
    if st.session_state.destino == "Rio Bravo" and st.session_state.cruce =="Bordear el rio":
        if st.session_state.mostrarTextoComo==1:
            st.write("Elijes bordear el rio, dices que es mejor un trabajo duro que uno arriesgado, tu camino empieza complicado, te sientes observada y ansiosa, lo cual te hace tropezar y lastimarte, llegas a mitad de camino y sientes que no puedes más, de repente una manada de perros aparece en frente tuyo, gruñéndote y enfrentandote, tu miedo te ciega y tu cansancio actual no ayuda, pero")
            st.write("Desde lo más alto de los árboles a tu lado finos balines empiezan a dirigirse hacia los perros haciendo que se asusten y no sepan que hacer más que correr hacia diferentes direcciones, se olvidan de ti, pero debido a todo lo ocurrido te desmayas, momentos después te despiertas y sin entender mucho sigues el camino")

            if st.button("Continuar", key="textHadaBalsBorde"):
                st.session_state.mostrarTextoComo =2
                st.rerun()
        elif st.session_state.mostrarTextoComo ==2:
            st.write("Estás llegando al final de tu camino… Pero… espera un momento, ¿qué es ese ruido? *escuchas ruido de madera, empiezas a tener miedo…* de la nada te cae una nuez en la cabeza")
            st.write("Lejos de asustarte mirás hacia la dirección donde la viste venir, unos ojos redondos y brillosos te miran desde esa dirección, es una ardilla!! pero no cualquier ardilla, destellos dorados salen de su nariz y orejas cuando te ven, acaso esta será una conexión…?")
            st.write("Felicidades! un compañero te eligió para acompañarte en tu aventura")
            if st.button("Continuar", key="textHadaBalsBorde2"):
                st.session_state.mostrarTextoComo = 0
                st.rerun()
    elif st.session_state.destino == "Rio Bravo" and st.session_state.cruce =="Balsa por dentro":
        if st.session_state.mostrarTextoComo==1:
            st.write("eliges cruzar el río por dentro, tu instinto de venganza y de ira te hace ir por el lugar más peligroso a simple vista, donde estabas había una balsa medianamente decente, que en tu cabeza era buena idea, y de hecho, sí… El primer trayecto fue un poco turbulento, pero luego el rio desemboca y se calma haciendo de tu viaje hasta la mazmorra tranquilo. Pero de repente, casi llegando al final, el río se alborota y se vuelve incontrolable, intentas mantenerte a flote hasta llegar pero tu balsa se vuelca…")
            if st.button("Continuar", key="textHadaBalsDentr3"):
                st.session_state.mostrarTextoComo = 2
                st.rerun()
        elif st.session_state.mostrarTextoComo ==2:
            st.write(" justo antes de caer un gato tricolor callejero rondaba por ahí, vio la situación e hizo sonar su campana, no entiendes bien que pasó pero saliste ilesa y tu cuerpo no dolía, cuando logras despertar estabas en el suelo y sobre ti había un amigo felino tricolor mirándote fijo, crees ver destellos dorados salir de su collar pero dudas")
            st.write("Felicidades! un compañero te eligió para acompañarte en tu aventura")
            if st.button("Continuar", key="textHadaBalsDentr4"):
                st.session_state.mostrarTextoComo = 0
                st.rerun()



def informacion_hada():
    st.image("assets/gif/hadaDesterrada.gif")
    st.text(
        "Eres un hada que fue exiliada de su lugar, de su casa, de su familia, "
        "luchaste por quedarte y te defendiste, pero la reina no te creyó a pesar "
        "de que todo haya sido una confusión y el culpable sea otro, tu exiliación "
        "solo puede ser redimida enfrentando esta aventura. Si logras superar, "
        "serás inocente y podrás volver a tu aldea; si no, tu peor destino será "
        "no salir de la mazmorra. Te deseamos suerte."
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
        cruce = st.radio(
            "",
            ["Balsa por dentro", "Bordear el rio"],
            key="cruce_hada_rio"
        )

    elif st.session_state.destino == "Bosque Brumoso":
        st.subheader(
            "Inicias tu recorrido por el bosque brumoso, está todo lleno de "
            "niebla y hay un ambiente tenso y sombrío."
        )
        cruce = st.radio(
            "",
            ["Volar Sobre el bosque", "Ir por dentro del bosque"],
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
        "Ir por dentro del bosque"
    ]:
        st.write("Encuentras una Ardilla mascota en el camino.")
        st.session_state.mascota = "Ardilla"
        st.session_state.mostrarTextoComo =3

    elif st.session_state.cruce in [
        "Balsa por dentro",
        "Volar Sobre el bosque"
    ]:
        st.write("Encontraste un Gato Tricolor mascota en el camino.")
        st.session_state.mascota = "Gato Tricolor"



    if st.button("Continuar", key="continuar_mascota_hada"):
        st.session_state.etapa = "MAZMORRA"
        st.rerun()


def etapa_5_hada():
    if st.session_state.mascota == "Ardilla":
        st.write("Encuentras y entras a la mazmorra")
        st.write("pasas por un tunel que te dirige hacia el este (izquierda) y te encuentras con dos opciones de camino, el primero tiene un aspecto tranquilo, calmo e inquietante, el segundo se ve más familiar, como tu hogar, algunas flores salen de la puerta y se ve vida…")
        sala = st.radio(
            "¿Con quién vas a luchar?",
            ["Pasillo Tranquilo", "Pasillo Familiar"],
            key="sala_hada_ardilla"
        )

    elif st.session_state.mascota == "Gato Tricolor":
        st.write("Llegas a la entrada de la mazmorra pasas por un túnel que te dirige hacia el este")
        st.write("Está oscuro y hay muchos ruidos, pero crees que es la mejor entrada y que es un engaño el aspecto para que los exploradores como vos no pasen, más adelante te encuentras con dos pasillos ¿cuál eliges?")
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
        st.write("entras a una habitación en penumbras, tras pasar la entrada tus ojos no pueden creer lo que ven, entidades, personas, espíritus, toda clase de fantasmas que te puedas imaginar, deambulando por todo el lugar… te encuentras frente a fantasmas que buscan oro y cosas brillantes, sino te raptan y no te dejan salir")
        st.write("¿qué decides hacer? ")
        opciones = ["Polvo De Hadas", "¡snif snif!"]

    elif sala == "Pasillo Familiar":
        st.write(" entras a la puerta de tu eleccion y te encuentras con un campo de flores hermoso, las flores más bellas que jamás hayas visto, tu amigo roedor se emociona porque jamás creyó que existiera algo así, empiezas tu camino pero a medida que avanzas te das cuenta que las flores largan un olor extraño, casi nauseabundo, malas noticias… las flores son venenosas, largan un hedor parecido al ácido y te asfixian")
        st.write("¿qué hacés?")
        opciones = ["Polvo De Hadas", "¡snif snif!"]

    elif sala == "Pasillo Izquierdo":
        st.write("Entras a una habitación llena de humedad.")
        st.write("Es un espacio donde cae agua por doquier y su piso está inundado de barro, sientes como tus alas empiezan a pesar por el agua que cae y no te permite seguir volando, inevitablemente debes caminar, el barro te llegaba hasta por debajo de la rodilla, pero de repente sientes que este te tira un poco, frente a ti se eleva una montaña de barro, es un espiritu que usa el barro como cuerpo")
        opcion = st.radio(
            "¿Que haces?",
            ["Tintineo De Campana", "Cortar Mechon Del Cabello"]
        ) 

    elif sala == "Pasillo Derecho":
        st.write("este pasillo está oscuro, haces 5 pasos y el piso se pierde")
        st.write("caes por un túnel y al caer te encuentras con una habitación completamente a oscuras donde hay mucho ruido, sabes que si sigues 5 minutos así no resistiras")
        opcion = st.radio(
            "Que haces?",
            ["Tinteno De Campana", "Correr"]
        ) 
    else:
        return

    if st.button("Continuar", key="continuar_batalla_hada"):
        st.session_state.opcionBatalla = opcion
        st.session_state.etapa = 7
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

#python -m streamlit run practica.py