import streamlit as st

from modulos.home import page_home
from modulos.ejercicio1 import page_ej1
from modulos.ejercicio2 import page_ej2
from modulos.ejercicio3 import page_ej3
from modulos.ejercicio4 import page_ej4

st.set_page_config(page_title="Proyecto", layout="wide")

st.markdown(
    """
    <style>
      .big-title { font-size: 38px; font-weight: 800; margin-bottom: 0.25rem; }
      .subtle { color: #666; margin-top: 0; }
      .card { padding: 14px; border: 1px solid #eee; border-radius: 12px; }
    </style>
    """,
    unsafe_allow_html=True
)

try:
    st.sidebar.image("logo.png")
except Exception:
    pass

st.sidebar.title("Menú")

opcion = st.sidebar.selectbox(
    "Seleccione una opción",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"],
)

if opcion == "Home":
    page_home()
elif opcion == "Ejercicio 1":
    page_ej1()
elif opcion == "Ejercicio 2":
    page_ej2()
elif opcion == "Ejercicio 3":
    page_ej3()
elif opcion == "Ejercicio 4":
    page_ej4()