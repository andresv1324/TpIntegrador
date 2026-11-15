import streamlit as st


def informacion_explorador():
    st.text(
        "Eres un pícaro explorador, en busca de su camino… engañaste a gente, "
        "mentiste y robaste para sobrevivir, pero jamás te descubrieron. Eres ágil "
        "y con encantos de envidiar; convences hasta a la persona más desconfiada "
        "del planeta. Posees una fuerza mental increíble y una supervivencia "
        "irrevocable. En tu cotidianidad tus pensamientos dicen: “entre más "
        "obstáculos superados, más sabiduría”. Obviamente eres un aprendiz de "
        "la vida misma. Un día viste en un cartel tu siguiente obstáculo: salir "
        "de una mazmorra, y pensaste… ¿por qué no?"
    )

    if st.button("Continuar", key="continuar_historia_explorador"):
        st.session_state.informacion = 0
        st.rerun()

#OPCION DE CAMINO
def elegir_camino_explorador():
    st.subheader(
        "Hiciste la elección de personaje, tu rumbo ha comenzado, elige tu camino"
    )

    destino = st.radio(
        "¿A dónde quieres ir?",
        ["Tunel Con Trampas", "Montaña Con Laberintos"],
        key="destino_explorador"
    )

    if st.button("Continuar", key="continuar_camino_explorador"):
        st.session_state.destino = destino
        st.session_state.etapa = 3
        st.rerun()

#OPCION DE CRUZAR PRIMER CAMINO
def etapa_3_explorador():
    if st.session_state.destino == "Tunel Con Trampas":
        st.subheader(
            "Te encuentras con un túnel bastante gigante para tu tamaño. "
            "Piensas y piensas; solo se te ocurren dos formas de cruzar. ¿Cuál eliges?"
        )
        cruce = st.radio(
            "",
            ["Trepar tunel", "Cruzar el tunel"],
            key="cruce_explorador_tunel"
        )

    elif st.session_state.destino == "Montaña Con Laberintos":
        st.subheader("te encuentras con la inmensidad de la naturaleza frente a tus ojos,un bosque gigante frente a ti," 
                    "tus caminos son limitados pero para un Pícaro como vos, piensas “nada es imposible”... por donde decides ir?")
        cruce = st.radio(
            "",
            ["Trepar montaña", "Pasar por medio de la montaña"],
            key="cruce_explorador_montana"
        )
    else:
        return

    if st.button("Continuar", key="continuar_cruce_explorador"):
        st.session_state.cruce = cruce
        st.session_state.etapa = 4
        st.rerun()


def etapa_4_explorador():
    st.subheader(f"El camino del {st.session_state.personaje}")

    if st.session_state.cruce in [
        "Trepar tunel",
        "Pasar por medio de la montaña"
    ]:
        st.write("Encuentras una Ardilla mascota en el camino.")
        st.session_state.mascota = "Ardilla"

    elif st.session_state.cruce in [
        "Cruzar el tunel",
        "Trepar montaña"
    ]:
        st.write("Encontraste un Gato Tricolor mascota en el camino.")
        st.session_state.mascota = "Gato Tricolor"

    if st.button("Continuar", key="continuar_mascota_explorador"):
        st.session_state.etapa = "MAZMORRA"
        st.rerun()


def etapa_5_explorador():
    st.subheader(f"El camino del {st.session_state.personaje}")

    if st.session_state.mascota == "Ardilla":
        st.write("Al entrar en la mazmorra sentís un aroma agradable.")
        st.write("Ves 2 caminos.")
        sala = st.radio(
            "Pasillo izquierdo: ves una corriente de aire. Pasillo derecho: ves un pasillo oscuro.",
            ["Corriente de aire", "Pasillo oscuro"],
            key="sala_explorador_ardilla"
        )

    elif st.session_state.mascota == "Gato Tricolor":
        st.write("Al entrar en la mazmorra sentís un fuerte aroma desagradable.")
        st.write("Ves dos caminos.")
        sala = st.radio(
            "Pasillo izquierdo: al fondo ves una reja metálica. "
            "Pasillo derecho: una galería con lodo en el piso.",
            ["Pasillo reja", "Pasillo a la galeria"],
            key="sala_explorador_gato"
        )
    else:
        return

    if st.button("Continuar", key="continuar_sala_explorador"):
        st.session_state.salaInicial = sala
        st.session_state.etapa = 6
        st.rerun()


def etapa_6_explorador():
    st.subheader(f"El camino del {st.session_state.personaje}")
    sala = st.session_state.salaInicial

    if sala == "Corriente de aire":
        st.write(f"Puedes usar la habilidad de {st.session_state.mascota}.")
        st.write("Tomar a tu compañero y huir con él en brazos.")
        opciones = [
            f"Usar la habilidad de tu compañero {st.session_state.mascota}",
            "Escapar con tu compañero"
        ]

    elif sala == "Pasillo oscuro":
        st.write("Tu compañero extiende las patas hacia ti.")
        st.write("Crack Crack")
        opciones = [
            f"Sostener las patitas de tu compañero {st.session_state.mascota}",
            "Crack Crack Crack"
        ]

    elif sala == "Pasillo reja":
        st.write("Intentar forzar cerrojo con la ganzúa.")
        st.write("Explotar bisagras con un trozo de pedernal.")
        opciones = ["Forzar Cerrojo", "Explotar Bisagra"]

    elif sala == "Pasillo a la galeria":
        st.write("Salto acrobático.")
        st.write("Cubrirte con la capa y pasar la sala.")
        opciones = ["Salto Acrobatico", "Uso De La Capa"]
    else:
        return

    opcion = st.radio("¿Cómo vas a superar la sala?", opciones, key="batalla_explorador")

    if st.button("Continuar", key="continuar_batalla_explorador"):
        st.session_state.opcionBatalla = opcion
        st.session_state.etapa = 7
        st.rerun()


def main_explorador():
    etapa = st.session_state.etapa

    if etapa == 2:
        if st.session_state.informacion == 1:
            informacion_explorador()
        else:
            elegir_camino_explorador()
    elif etapa == 3:
        etapa_3_explorador()
    elif etapa == 4:
        etapa_4_explorador()
    elif etapa == 5:
        etapa_5_explorador()
    elif etapa == 6:
        etapa_6_explorador()
