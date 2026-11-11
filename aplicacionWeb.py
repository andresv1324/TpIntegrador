import streamlit as st

st.title("Aventura interactiva")

st.write("Te encuentras frente a dos caminos.")

# Seleccionar una opcion
opcion = st.radio(
    "¿Qué camino quieres tomar?",
    ["Ir al bosque 🌳", "Ir a la montaña 🏔️"]
)

# Confirmar eleccion
if st.button("Aceptar"):

    if opcion == "Ir al bosque 🌳":
        st.success("Elegiste ir al bosque.")
        st.write("Encuentras un río y un puente.")

    elif opcion == "Ir a la montaña 🏔️":
        st.success("Elegiste ir a la montaña.")
        st.write("Encuentras una cueva misteriosa.")
