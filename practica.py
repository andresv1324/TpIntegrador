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

    if "salaInicial" not in st.session_state:
        st.session_state.salaInicial = None

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
                ["Rio Bravo", "Bosque Brumoso"]
            )

        elif st.session_state.personaje == "🧭 Explorador":
            destino = st.radio(
                "¿A dónde quieres ir?",
                ["Tunel Con Trampas", "Montaña Con Laberintos"]
            )

        if st.button("Continuar"):

            st.session_state.destino = destino
            st.session_state.etapa = 3
            st.rerun()

    # ETAPA 3: Pasar el camino
    elif st.session_state.etapa == 3:

        st.subheader(f"El camino del {st.session_state.destino}")

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
            st.session_state.mascota = "Ardilla"

        elif st.session_state.cruce == "Ignorarla y bordear el rio" or st.session_state.cruce == "Volar Sobre el bosque":
            st.write("Encontraste un Gato Tricolor mascota en el camino")
            st.session_state.mascota = "Gato Tricolor"

        if st.button("Continuar"):
            st.session_state.etapa = "MAZMORRA"
            st.rerun()

    #ENTRADA A LA MAZMORRA
    elif st.session_state.etapa == "MAZMORRA":
        st.header("ENTRASTE EN LA MAZMORRA")
        st.session_state.etapa= 5
        st.rerun()

    elif st.session_state.etapa == 5:

        st.subheader(f"El camino del {st.session_state.personaje}")

        if st.session_state.mascota == "Ardilla":
            st.write("Al entras en la mazmorra vez un Tunel con una luz en el camino")
            st.write("Al fondo encuentras 2 salas que tendra que superar para poder continuar")
            salaInicial = st.radio(
                "¿Con quien vas a Luchar?",
                ["Fantasmas","Campo de Flores"]
            )

        elif st.session_state.mascota == "Gato Tricolor":
            st.write("Al entras en la mazmorra vez un Tunel oscuro donde se escuchan voces a lo lejos")
            st.write("Al fondo encuentras 2 salas que tendra que superar para poder continuar")

            salaInicial = st.radio(
                "Un Pasillo Izquierdo - donde se escucha el fluir del agua y pasillo Derecho - Donde se ve una caida a un cuerto oscuro con mucho ruido",
                ["Pasillo Izquierdo","Pasillo Derecho"]
            )

        if st.button("Continuar"):
            st.session_state.salaInicial = salaInicial
            st.session_state.etapa = 6
            st.rerun()




if __name__ == '__main__':
    main()



# st.write(f"Personaje: {st.session_state.personaje}")
# st.write(f"Destino: {st.session_state.destino}")
