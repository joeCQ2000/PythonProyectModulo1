import streamlit as st

def page_ej1():
    st.title("Ejercicio 1 – Variables y Condicionales")

    presupuesto = st.number_input("Ingrese el presupuesto", min_value=0.0, step=1.0)
    gasto = st.number_input("Ingrese el gasto", min_value=0.0, step=1.0)

    if st.button("Evaluar"):
        diferencia = presupuesto - gasto

        if gasto <= presupuesto:
            st.success(" El gasto está dentro del presupuesto.")
        else:
            st.warning("El gasto excede el presupuesto.")

        st.write(f"Diferencia (presupuesto - gasto): {diferencia:.2f}")