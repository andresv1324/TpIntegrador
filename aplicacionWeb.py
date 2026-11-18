import streamlit as st
from pathlib import Path
import base64

from personajes.hada import main_hada
from personajes.explorador import main_explorador

# TRABAJO PRACTICO INTEGRADOR 2- Laboratorio de Computacion II
# AUTORES: MICAELA LANCIERI Y ANDRES VERGARA
# PROFESORA: MONICA HENCEK
# FECHA DE ENTREGA 17/11/2026


st.set_page_config(page_title="Lo que aguarda en la profundidad", layout="wide")

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
    
    # 1. Elige la imagen o GIF de fondo (puede ser de hada o de picaro)
    fondoPortada = cargaImgHada("portada.png") 

    css = css.replace("__HADA_GIF__", gifHada)
    css = css.replace("__PICARO_GIF__", gifPicaro)
    
    # 2. Reemplaza el marcador en el CSS
    css = css.replace("__FONDO_PORTADA__", fondoPortada)

    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

#agregado
def cargaPortada(ruta_relativa="assets/hada/img/portada.png"):
    ruta_proyecto = Path(__file__).parent
    ruta_img = ruta_proyecto / ruta_relativa

    with open(ruta_img, "rb") as archivo:
        img = base64.b64encode(archivo.read()).decode("utf-8")

    return f"data:image/jpeg;base64,{img}"



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
    st.markdown("<h2 style='text-align: center;'>Elige tu personaje</h2>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center; opacity: 0.85;'>Bienvenido a esta travesía, donde tu capacidad de intuición y sabiduría serán puestas a prueba.</p>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        if st.button("🧚 HADA EXILIADA\nMagia natural e intuición", key="elegir_hada", use_container_width=True):
            st.session_state.personaje = "🧚 Hada"
            st.session_state.informacion = 1
            st.session_state.etapa = 2
            st.rerun()

    with col2:
        if st.button("🧭 PÍCARO EXPLORADOR\nSigilo, astucia y supervivencia", key="elegir_explorador", use_container_width=True):
            st.session_state.personaje = "🧭 Explorador"
            st.session_state.informacion = 1
            st.session_state.etapa = 2
            st.rerun()


def main():
    cargar_estilos()
    inicializar_variables()

    if st.session_state.etapa == 0:
        fondo_jpg = cargaPortada("assets/hada/img/portada.png")

        st.markdown(f"""
            <style>
                header[data-testid="stHeader"] {{
                    display: none;
                }}
                .stApp {{
                    background-image: url("{fondo_jpg}") !important;
                    background-size: cover !important;
                    background-position: center center !important;
                    background-repeat: no-repeat !important;
                    background-attachment: fixed !important;
                }}
                .st-key-btn_comenzar {{
                    position: fixed !important;
                    bottom: 6vh !important;
                    left: 50% !important;
                    transform: translateX(-50%) !important;
                    width: 320px !important;
                    z-index: 999 !important;
                }}
            </style>
        """, unsafe_allow_html=True)

        _, col_centro, _ = st.columns([1.3, 1, 1.3])
        with col_centro:
            if st.button("⚔️ COMENZAR AVENTURA", key="btn_comenzar", use_container_width=True):
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

#    elif st.session_state.etapa == 10:
#        st.subheader("Continuación de la aventura")
#        st.write("Acá podés agregar la siguiente parte de tu historia.")


if __name__ == "__main__":
    main()
