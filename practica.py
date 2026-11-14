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

    if "opcionBatalla" not in st.session_state:
        st.session_state.opcionBatalla = None




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

        elif st.session_state.destino == "Tunel Con Trampas":
            cruce = st.radio(
                "Como superar el tunel",
                ["Trepar tunel","Cruzar el tunel"]
            )

        elif st.session_state.destino == "Montaña Con Laberintos":
            cruce = st.radio(
                "Como superar la montaña",
                ["Trepar montaña","Pasar por medio de la montaña"]
            )

        if st.button("Continuar"):
            st.session_state.cruce = cruce
            st.session_state.etapa = 4
            st.rerun()
        
    # ETAPA 4:
    elif st.session_state.etapa == 4:

        st.subheader(f"El camino del {st.session_state.personaje}")

        if st.session_state.cruce =="Usarla para ir por dentro del Rio" or st.session_state.cruce == "Ir por dentro del bosque" or st.session_state.cruce == "Trepar tunel" or st.session_state.cruce == "Pasar por medio de la montaña":
            st.write("Encuentras una Ardilla mascota en el camino.")
            st.session_state.mascota = "Ardilla"

        elif st.session_state.cruce == "Ignorarla y bordear el rio" or st.session_state.cruce == "Volar Sobre el bosque" or st.session_state.cruce == "Cruzar el tunel" or st.session_state.cruce == "Trepar montaña":
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

    #ETAPA 5
    elif st.session_state.etapa == 5:
        st.subheader(f"El camino del {st.session_state.personaje}")

        if st.session_state.mascota == "Ardilla" and st.session_state.personaje == "🧚 Hada":
            st.write("Al entras en la mazmorra vez un Tunel con una luz en el camino")
            st.write("Al fondo encuentras 2 salas que tendra que superar para poder continuar")
            salaInicial = st.radio(
                "¿Con quien vas a Luchar?",
                ["Fantasmas","Campo de Flores"]
            )

        elif st.session_state.mascota == "Gato Tricolor" and st.session_state.personaje == "🧚 Hada":
            st.write("Al entras en la mazmorra vez un Tunel oscuro donde se escuchan voces a lo lejos")
            st.write("Al fondo encuentras 2 salas que tendra que superar para poder continuar")

            salaInicial = st.radio(
                "Un Pasillo Izquierdo - donde se escucha el fluir del agua y pasillo Derecho - Donde se ve una caida a un cuerto oscuro con mucho ruido",
                ["Pasillo Izquierdo","Pasillo Derecho"]
            )
###################
        elif st.session_state.mascota == "Ardilla" and st.session_state.personaje == "🧭 Explorador":
            st.write("Al entar en la mazmorra sentis un aroma agradable")
            st.write("Vez 2 caminos ")
            salaInicial = st.radio(
                "¿Pasillo izquierdo - Vez una corriente de aire y pasillo Derecho - vez un pasillo oscuro",
                ["Corriente de aire","Pasillo oscuro"]
            )

        elif st.session_state.mascota == "Gato Tricolor" and st.session_state.personaje == "🧭 Explorador":
            st.write("Al entrar en la mazmorra sentis un fuerte aroma desagradable")
            st.write("Vez dos caminos ")

            salaInicial = st.radio(
                "Pasillo Izquierdo vez al fondo una reja metalica y Pasillo Derecho Una galeria con lodo en el piso ",
                ["Pasillo reja","Pasillo a la galeria"]
            )
###################
        if st.button("Continuar"):
            st.session_state.salaInicial = salaInicial
            st.session_state.etapa = 6
            st.rerun()


    #ETAPA 6
    elif st.session_state.etapa == 6:
        st.subheader(f"El camino del {st.session_state.personaje}")

        if st.session_state.salaInicial == "Fantasmas" and st.session_state.personaje == "🧚 Hada":
            st.write("Podes luchar Usando Polvo de Hadas que genera explosiones que te ayudan a esconderte en la habitacion")
            st.write(f"Puedes usar a tu mascota: {st.session_state.mascota}, que puede hacerte invisible para pasar la sala")

            opcionBatalla = st.radio(
                "Como vas a superar la sala?",
                [
                    "Polvo De Hadas",
                    f"Habilidad de la {st.session_state.mascota}"
                ]
            )

        elif st.session_state.salaInicial == "Campo de Flores" and st.session_state.personaje == "🧚 Hada":
            st.write("Podes luchar Usando Polvo de Hadas que anula el veneno de las flores")
            st.write(f"Puedes usar a tu mascota: {st.session_state.mascota}, que genera una burbuja protectora que repele los gases")
            opcionBatalla = st.radio(
                "Como vas a superar la sala?",
                [
                    "Polvo De Hadas",
                    f"Habilidad de la {st.session_state.mascota}"
                ]
            )

        elif st.session_state.salaInicial == "Pasillo Izquierdo" and st.session_state.personaje == "🧚 Hada":
            st.write(f"Usas a tu {st.session_state.mascota}, que genera una fuerte luz que seca a los espiritus")
            st.write("Cortarse un mechon del cabello - Este genera un onda de luz")
            opcionBatalla = st.radio(
                "Como vas a superar la sala",
                ["Habilad de tu mascota","Cortar el cabello"]
            )

        elif st.session_state.salaInicial == "Pasillo Derecho"and st.session_state.personaje == "🧚 Hada":
            st.write(f"Usar a tu {st.session_state.mascota}, junto tu polvo de hadas")
            st.write("tun tun tun")
            opcionBatalla = st.radio(
                "Como vas a superar la sala",
                [
                    f"Usar a tu {st.session_state.mascota} junto a tu polvo de hada",
                "tun tun tun"
                ]
            )

        elif st.session_state.salaInicial == "Corriente de aire" and st.session_state.personaje == "🧭 Explorador":
            st.subheader(f"El camino del {st.session_state.personaje}")

            st.write(f"Puedes usar habilidad de {st.session_state.mascota}")
            st.write(f"Tomar a tu compañero y huyes con el en brazos")

            opcionBatalla = st.radio(
                "Como vas a superar la sala",
                [
                    f"Usar la habilidad de tu compañero {st.session_state.mascota}"
                    "Escapar con tu compañero"
                ]
            )

        elif st.session_state.salaInicial == "Pasillo oscuro" and st.session_state.personaje == "🧭 Explorador":
            st.subheader(f"El camino del {st.session_state.personaje}")

            st.write("Tu compañero extiende las patas hacia ti")
            st.write("Crack Crack")

            opcionBatalla = st.radio(
                "Como vas a superar la sala",
                [
                    f"Sostener las patitas de tu compañero {st.session_state.mascota}"
                    "Crack Crack Crack"
                ]
            )

        elif st.session_state.salaInicial == "Pasillo reja" and st.session_state.personaje == "🧭 Explorador":
            st.subheader(f"El camino del {st.session_state.personaje}")

            st.write("Intentar forzar cerrrojo con la ganzua")
            st.write("Explotar bisagras con un trozo de pedernal")

            opcionBatalla = st.radio(
                "Como vas a superar la sala",
                ["Forzar Cerrojo","Explotar Bisagra"]
            )

        elif st.session_state.salaInicial == "Pasillo a la galeria" and st.session_state.personaje == "🧭 Explorador":
            st.subheader(f"El camino del {st.session_state.personaje}")

            st.write("Salto acrobatico")
            st.write("Cubrirte con la capa y pasar la sala")

            opcionBatalla = st.radio(
                "Como vas a superar la sala",
                ["Salto Acrobatico","Uso De La Capa"]
            )



        if st.button("Continuar"):
            st.session_state.opcionBatalla = opcionBatalla
            st.session_state.etapa = 7
            st.rerun()








if __name__ == '__main__':
    main()



# st.write(f"Personaje: {st.session_state.personaje}")
# st.write(f"Destino: {st.session_state.destino}")
