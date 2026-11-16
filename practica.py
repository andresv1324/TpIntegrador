import streamlit as st
from pathlib import Path
import base64

from personajes.hada import main_hada
from personajes.explorador import main_explorador


st.set_page_config(
    page_title="Lo que aguarda en la profundidad",
    page_icon="🌒",
    layout="wide"
)


@st.cache_data
def cargaGifHada(nombre):
    ruta_proyecto = Path(__file__).parent
    ruta_gif = ruta_proyecto / "assets"/ "hada" / "gif" / nombre

    with open(ruta_gif, "rb") as archivo:
        gif = base64.b64encode(archivo.read()).decode("utf-8")

    return f"data:image/gif;base64,{gif}"

def cargaImgHada(nombre):
    ruta_proyecto = Path(__file__).parent
    ruta_gif = ruta_proyecto / "assets"/ "hada" / "img" / nombre

    with open(ruta_gif, "rb") as archivo:
        gif = base64.b64encode(archivo.read()).decode("utf-8")

    return f"data:image/gif;base64,{gif}"

def cargaGifPicaro(nombre):
    ruta_proyecto = Path(__file__).parent
    ruta_gif = ruta_proyecto / "assets"/ "picaro" / "gif" / nombre

    with open(ruta_gif, "rb") as archivo:
        gif = base64.b64encode(archivo.read()).decode("utf-8")

    return f"data:image/gif;base64,{gif}"

def cargaImgPicaro(nombre):
    ruta_proyecto = Path(__file__).parent
    ruta_gif = ruta_proyecto / "assets"/ "picaro" / "img" / nombre

    with open(ruta_gif, "rb") as archivo:
        gif = base64.b64encode(archivo.read()).decode("utf-8")

    return f"data:image/gif;base64,{gif}"


def cargar_estilos():
    ruta_proyecto = Path(__file__).parent
    ruta_css = ruta_proyecto / "css" / "estilos.css"

    with open(ruta_css, "r", encoding="utf-8") as archivo:
        css = archivo.read()

    gifHada = cargaGifHada("hadaSaludando.gif")
    gifPicaro = cargaGifPicaro("picaroSaludando.gif")
    css = css.replace("__HADA_GIF__", gifHada)
    css = css.replace("__PICARO_GIF__",gifPicaro)

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
        "textoSalaFinal": 1,
        "condicionSalida": None
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


def mostrar_portada():
    st.markdown(
        """
        <section class="landing-screen">
            <div class="landing-kicker">Una aventura de decisiones y misterio</div>
            <h1 class="landing-title">
                LO QUE AGUARDA
                <span>EN LA PROFUNDIDAD</span>
            </h1>
            <div class="landing-divider"></div>
            <p class="landing-description">
                Más allá de los senderos conocidos, algo antiguo despierta.
                Elegí tu camino, confiá en tu instinto y descubrí qué secretos
                se ocultan en la oscuridad.
            </p>
            <div class="landing-hint">Tu historia comienza aquí</div>
        </section>
        """,
        unsafe_allow_html=True
    )

    _, centro, _ = st.columns([1, 2, 1])
    with centro:
        if st.button("✦  Comenzar aventura  ✦", key="comenzar_aventura", use_container_width=True):
            st.session_state.etapa = 1
            st.rerun()


def main():
    cargar_estilos()
    inicializar_variables()

    if st.session_state.etapa == 0:
        mostrar_portada()

    # Etapa 1
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
        if st.session_state.personaje == "🧚 Hada":
            main_hada()
        elif st.session_state.personaje == "🧭 Explorador":
            main_explorador()

    elif st.session_state.etapa == 8:
        if st.session_state.personaje == "🧚 Hada":
            main_hada()
        elif st.session_state.personaje == "🧭 Explorador":
            main_explorador()

    elif st.session_state.etapa == 9:
        if st.session_state.personaje == "🧚 Hada":
            main_hada()
        elif st.session_state.personaje == "🧭 Explorador":
            main_explorador()

    elif st.session_state.etapa == 10:
        st.title("¡FIN DE LA AVENTURA!")
        if st.button("Volver al inicio"):
            st.session_state.clear()
            st.rerun()


if __name__ == "__main__":
    main()
