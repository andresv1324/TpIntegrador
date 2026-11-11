import streamlit as st
import pandas as pd
import numpy as np



def main():

    st.title("Aventura Interactiva")

    # =========================
    # INICIALIZAR VARIABLES
    # =========================

    if "etapa" not in st.session_state:
        st.session_state.etapa = 1

    if "personaje" not in st.session_state:
        st.session_state.personaje = None

    if "destino" not in st.session_state:
        st.session_state.destino = None

    if "cruce" not in st.session_state:
        st.session_state.cruce = None

    if "mascota" not in st.session_state:
        st.session_state.mascota = None

    # ETAPA 1: Selección del personaje
    if st.session_state.etapa == 1:
        st.subheader("Selecciona tu personaje")

        personaje = st.radio(
            "¿Con quién quieres comenzar?",
            ["🧚 Hada", "🧭 Explorador"]
        )

        if st.button("Elegir personaje"):
            st.session_state.personaje = personaje
            st.session_state.etapa = 2
            st.rerun()

    # ETAPA 2: Selección del camino
    elif st.session_state.etapa == 2:

        st.subheader(f"El camino del {st.session_state.personaje}")

        if st.session_state.personaje == "🧚 Hada":
            destino = st.radio(
                "¿A dónde quieres ir?",
                ["Río Bravo", "Bosque Brumoso"]
            )

        elif st.session_state.personaje == "🧭 Explorador":
            destino = st.radio(
                "¿A dónde quieres ir?",
                ["Tunel Con Trampas", "Montaña Con Laberintos"]
            )

        if st.button("Continuar"):

            st.session_state.cruce = destino
            st.session_state.etapa = 3
            st.rerun()

    # ETAPA 3: Pasar el camino
    elif st.session_state.etapa == 3:

        st.subheader("")

        if st.session_state.destino == "Rio Bravo":
            cruce = st.radio(
                "Encuentra una balsa",
                ["Usarla para ir por dentro del Rio","Ignorarla y bordear el rio"]
            )
        
        elif st.session_state.destino =="Bosque Brumoso":
            cruce = st.radio(
                "Ves un bosque el que deberas pasar",
                ["Volar Sobre el bosque","Ir por dentro del bosque"]
            )

        if st.button("Continuar"):
            st.session_state.cruce = cruce
            st.session_state.etapa = 4
            st.rerun()
        
    # ETAPA 4:
    elif st.session_state.etapa == 4:

        st.subheader(f"El camino del {st.session_state.personaje}")

        if st.session_state.cruce =="Usarla para ir por dentro del Rio" or st.session_state.cruce == "Ir por dentro del bosque":
            st.write("Encuentras una Ardilla mascota en el camino.")
            st.session.state.mascota = "Ardilla"

        elif st.select_slider.cruce == "Ignorarla y bordear el rio" or st.session_state.cruce == "Volar Sobre el bosque":
            st.write("Encontraste un Gato Tricolor mascota en el camino")
            st.session_state.mascota = "Gato Tricolor"

        if st.button("Continuar"):
            st.session_state.etapa = 5
            st.rerun()

if __name__ == '__main__':
    main()



# st.write(f"Personaje: {st.session_state.personaje}")
# st.write(f"Destino: {st.session_state.destino}")
