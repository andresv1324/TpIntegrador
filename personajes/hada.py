import streamlit as st

def textoComo():
    if st.session_state.cruce =="Balsa por dentro":
        st.write("Eliges cruzar el río por dentro, tu instinto de venganza y de ira te hace ir por el lugar más peligroso a simple vista, donde estabas había una balsa medianamente decente, que en tu cabeza era buena idea, y de hecho, sí… El primer trayecto fue un poco turbulento, pero luego el rio desemboca y se calma haciendo de tu viaje hasta la mazmorra tranquilo. Pero de repente, casi llegando al final, el río se alborota y se vuelve incontrolable, intentas mantenerte a flote hasta llegar pero tu balsa se vuelca…")
        if st.button("Continuar", key="textHadaBalsDentr"):
            st.session_state.mostrarTextoComo =2
            st.rerun()

def textoComo1():
    if st.session_state.cruce =="Balsa por dentro":
        st.write(" justo antes de caer un gato tricolor callejero rondaba por ahí, vio la situación e hizo sonar su campana, no entiendes bien que pasó pero saliste ilesa y tu cuerpo no dolía, cuando logras despertar estabas en el suelo y sobre ti había un amigo felino tricolor mirándote fijo, crees ver destellos dorados salir de su collar pero dudas")
        st.write("Felicidades! un compañero te eligió para acompañarte en tu aventura")
        if st.button("Continuar", key="textHadaBalsDentr2"):
            st.session_state.mostrarTextoComo = False
            st.rerun()

def textoComo2():
    st.write(" aaaaaaaaaaaaaaaaaaaaaaaaaajusto antes de caer un gato tricolor callejero rondaba por ahí, vio la situación e hizo sonar su campana, no entiendes bien que pasó pero saliste ilesa y tu cuerpo no dolía, cuando logras despertar estabas en el suelo y sobre ti había un amigo felino tricolor mirándote fijo, crees ver destellos dorados salir de su collar pero dudas")
    st.write("Felicidades! un compañero te eligió para acompañarte en tu aventura")
    if st.button("Continuar", key="textHadaBalsDentr3"):
        st.session_state.mostrarTextoComo = 4
        st.rerun()

def textoComo3():
    st.write(" aeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeaaaaaaaaaaaaaaaaaaaaaaajusto antes de caer un gato tricolor callejero rondaba por ahí, vio la situación e hizo sonar su campana, no entiendes bien que pasó pero saliste ilesa y tu cuerpo no dolía, cuando logras despertar estabas en el suelo y sobre ti había un amigo felino tricolor mirándote fijo, crees ver destellos dorados salir de su collar pero dudas")
    st.write("Felicidades! un compañero te eligió para acompañarte en tu aventura")
    if st.button("Continuar", key="textHadaBalsDentr4"):
        st.session_state.mostrarTextoComo = False
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
        st.session_state.mostrarTextoComo=3
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
        st.write("Al entrar en la mazmorra ves un túnel oscuro donde se escuchan voces a lo lejos.")
        st.write("Al fondo encuentras 2 salas que tendrás que superar para continuar.")
        sala = st.radio(
            "Un pasillo izquierdo donde se escucha el fluir del agua y "
            "un pasillo derecho donde se ve una caída a un cuarto oscuro con mucho ruido.",
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
    st.subheader(f"El camino del {st.session_state.personaje}")
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
        st.write(f"Usas a tu {st.session_state.mascota}, que genera una fuerte luz que seca a los espíritus.")
        st.write("Cortarse un mechón del cabello: este genera una onda de luz.")
        opciones = ["Habilidad de tu mascota", "Cortar el cabello"]

    elif sala == "Pasillo Derecho":
        st.write(f"Usar a tu {st.session_state.mascota} junto a tu polvo de hadas.")
        st.write("tun tun tun")
        opciones = [f"Usar a tu {st.session_state.mascota} junto a tu polvo de hada", "tun tun tun"]
    else:
        return

    opcion = st.radio("¿Cómo vas a superar la sala?", opciones, key="batalla_hada")

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
        if st.session_state.mostrarTextoComo==1:
            textoComo()
        elif st.session_state.mostrarTextoComo==2:
            textoComo1()
        elif st.session_state.mostrarTextoComo==3:
            textoComo2()
        elif st.session_state.mostrarTextoComo==4:
            textoComo3()
        else:
            etapa_4_hada()
    elif etapa == 5:
        etapa_5_hada()
    elif etapa == 6:
        etapa_6_hada()

#python -m streamlit run practica.py