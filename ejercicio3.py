import streamlit as st
import numpy as np

import streamlit as st

def calcular_retorno(actividad: dict, tasa: float, meses: int) -> float:
    # Retorno = presupuesto × tasa × meses
    return float(actividad["presupuesto"]) * float(tasa) * int(meses)

def page_ej3():
    st.title("Ejercicio 3 – Funciones y Programación Funcional")

    # Verificación de la existencia de la lista
    if "actividades" not in st.session_state:
        st.session_state["actividades"] = []

    # Inputs
    tasa_pct = st.slider("Tasa (%)", min_value=0.0, max_value=100.0, value=10.0, step=0.5)
    meses = st.number_input("Meses", min_value=1, max_value=360, value=12, step=1)

    # Botón
    if st.button("Calcular retorno"):
        actividades = st.session_state["actividades"]

        if len(actividades) == 0:
            st.write("No hay actividades registradas. Agrega actividades en el Ejercicio 2.")
            return

        tasa = tasa_pct / 100.0

        # Programación funcional
        retornos = list(
            map(
                lambda act: {
                    "nombre": act["nombre"],
                    "tipo": act["tipo"],
                    "retorno": calcular_retorno(act, tasa, meses),
                },
                actividades,
            )
        )

        # Mostrar resultados (obligatorio: st.write)
        st.write("Resultados por actividad:")
        for r in retornos:
            st.write(
                f"- {r['nombre']} ({r['tipo']}): retorno esperado = {r['retorno']:.2f}"
            )