import streamlit as st


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


def etapa_3_hada():
    if st.session_state.destino == "Rio Bravo":
        st.header(
            "Empiezas tu recorrido por un río turbulento que intimida, "
            "rompe olas contra piedras filosas y hay muchísimo viento. "
            "¿Por dónde eliges ir?"
        )
        cruce = st.radio(
            "",
            ["Usarla para ir por dentro del Rio", "Ignorarla y bordear el rio"],
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


def etapa_4_hada():
    st.subheader(f"El camino del {st.session_state.personaje}")

    if st.session_state.cruce in [
        "Usarla para ir por dentro del Rio",
        "Ir por dentro del bosque"
    ]:
        st.write("Encuentras una Ardilla mascota en el camino.")
        st.session_state.mascota = "Ardilla"

    elif st.session_state.cruce in [
        "Ignorarla y bordear el rio",
        "Volar Sobre el bosque"
    ]:
        st.write("Encontraste un Gato Tricolor mascota en el camino.")
        st.session_state.mascota = "Gato Tricolor"

    if st.button("Continuar", key="continuar_mascota_hada"):
        st.session_state.etapa = "MAZMORRA"
        st.rerun()


def etapa_5_hada():
    st.subheader(f"El camino del {st.session_state.personaje}")

    if st.session_state.mascota == "Ardilla":
        st.write("Al entrar en la mazmorra ves un túnel con una luz en el camino.")
        st.write("Al fondo encuentras 2 salas que tendrás que superar para continuar.")
        sala = st.radio(
            "¿Con quién vas a luchar?",
            ["Fantasmas", "Campo de Flores"],
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

    if sala == "Fantasmas":
        st.write("Puedes luchar usando Polvo de Hadas, que genera explosiones que te ayudan a esconderte en la habitación.")
        st.write(f"Puedes usar a tu mascota: {st.session_state.mascota}, que puede hacerte invisible para pasar la sala.")
        opciones = ["Polvo De Hadas", f"Habilidad de la {st.session_state.mascota}"]

    elif sala == "Campo de Flores":
        st.write("Puedes luchar usando Polvo de Hadas, que anula el veneno de las flores.")
        st.write(f"Puedes usar a tu mascota: {st.session_state.mascota}, que genera una burbuja protectora que repele los gases.")
        opciones = ["Polvo De Hadas", f"Habilidad de la {st.session_state.mascota}"]

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
        etapa_4_hada()
    elif etapa == 5:
        etapa_5_hada()
    elif etapa == 6:
        etapa_6_hada()
