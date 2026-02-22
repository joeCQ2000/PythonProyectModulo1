import streamlit as st
import pandas as pd

def page_ej2():
    st.title("Ejercicio 2 - Listas y Diccionarios")

    if "actividades" not in st.session_state:
        st.session_state["actividades"] = []

    nombre = st.text_input("Nombre de la actividad")
    tipo = st.selectbox("Tipo de actividad", ["Ingreso", "Gasto", "Ahorro", "Otro"])
    presupuesto = st.number_input("Presupuesto", min_value=0.0, step=1.0)
    gasto_real = st.number_input("Gasto real", min_value=0.0, step=1.0)

    # Botón para agregar
    if st.button("Agregar actividad"):
        actividad = {
            "nombre": nombre,
            "tipo": tipo,
            "presupuesto": presupuesto,
            "gasto_real": gasto_real
        }
        st.session_state["actividades"].append(actividad)
        st.success("Actividad agregada.")

    st.write("### Actividades registradas")
    if len(st.session_state["actividades"]) == 0:
        st.write("Aún no hay actividades registradas.")
        return

    df = pd.DataFrame(st.session_state["actividades"])
    st.dataframe(df, use_container_width=True)

    st.write("### Estado de cada actividad")
    for i, act in enumerate(st.session_state["actividades"], start=1):
        if act["gasto_real"] <= act["presupuesto"]:
            estado = "Dentro del presupuesto "
        else:
            estado = "Presupuesto excedido "

        st.write(
            f"{i}. **{act['nombre']}** ({act['tipo']}) -> "
            f"Presupuesto: {act['presupuesto']:.2f} | "
            f"Gasto real: {act['gasto_real']:.2f} | "
            f"Estado: {estado}"
        )