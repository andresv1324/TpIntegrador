import streamlit as st
from pathlib import Path
import base64

from personajes.hada import main_hada
from personajes.explorador import main_explorador


@st.cache_data
def cargar_gif(nombre):
    ruta_proyecto = Path(__file__).parent
    ruta_gif = ruta_proyecto / "assets" / "gif" / nombre

    with open(ruta_gif, "rb") as archivo:
        gif = base64.b64encode(archivo.read()).decode("utf-8")

    return f"data:image/gif;base64,{gif}"


def cargar_estilos():
    ruta_proyecto = Path(__file__).parent
    ruta_css = ruta_proyecto / "css" / "estilos.css"

    with open(ruta_css, "r", encoding="utf-8") as archivo:
        css = archivo.read()

    gif_hada = cargar_gif("hadaSaludando.gif")
    css = css.replace("__HADA_GIF__", gif_hada)

    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def inicializar_variables():
    valores_iniciales = {
        "etapa": 0,
        "personaje": None,
        "destino": None,
        "cruce": None,
        "mascota": None,
        "salaInicial": None,
        "opcionBatalla": None,
        "informacion": 1,
        "mostrarTextoComo": 1,
        "textoSalaFinal": 1
    }

    for variable, valor in valores_iniciales.items():
        if variable not in st.session_state:
            st.session_state[variable] = valor


def seleccionar_personaje():
    st.subheader(
        "Bienvenido a esta travesía, donde tu capacidad de intuición "
        "y sabiduría serán puestas a prueba. Elige tu personaje:"
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("", key="elegir_hada", use_container_width=True):
            st.session_state.personaje = "🧚 Hada"
            st.session_state.informacion = 1
            st.session_state.etapa = 2
            st.rerun()

    with col2:
        if st.button("", key="elegir_explorador", use_container_width=True):
            st.session_state.personaje = "🧭 Explorador"
            st.session_state.informacion = 1
            st.session_state.etapa = 2
            st.rerun()


def main():
    cargar_estilos()
    inicializar_variables()

    if st.session_state.etapa == 0:
        st.title("LO QUE AGUARDA EN LA PROFUNDIDAD")

        if st.button("Comenzar Aventura"):
            st.session_state.etapa = 1
            st.rerun()

    #Etapa 1
    elif st.session_state.etapa == 1:
        seleccionar_personaje()

    elif st.session_state.etapa == 2:
        if st.session_state.personaje == "🧚 Hada":
            main_hada()
        elif st.session_state.personaje == "🧭 Explorador":
            main_explorador()

    # La etapa 3 en adelante queda a cargo del personaje seleccionado.
    elif st.session_state.etapa == "MAZMORRA":
        st.header("ENTRASTE EN LA MAZMORRA")
        st.session_state.etapa = 5
        st.rerun()

    elif st.session_state.etapa == 5:
        if st.session_state.personaje == "🧚 Hada":
            main_hada()
        elif st.session_state.personaje == "🧭 Explorador":
            main_explorador()

    elif st.session_state.etapa == 6:
        if st.session_state.personaje == "🧚 Hada":
            main_hada()
        elif st.session_state.personaje == "🧭 Explorador":
            main_explorador()

    elif st.session_state.etapa == 3 or st.session_state.etapa == 4:
        if st.session_state.personaje == "🧚 Hada":
            main_hada()
        elif st.session_state.personaje == "🧭 Explorador":
            main_explorador()

    elif st.session_state.etapa == 7:
        st.subheader("Continuación de la aventura")
        st.write("Acá podés agregar la siguiente parte de tu historia.")


if __name__ == "__main__":
    main()
