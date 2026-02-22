import streamlit as st
import numpy as np

class Actividad:
    def __init__(self, nombre: str, tipo: str, presupuesto: float, gasto_real: float):
        self.nombre = nombre
        self.tipo = tipo
        self.presupuesto = float(presupuesto)
        self.gasto_real = float(gasto_real)

    def esta_en_presupuesto(self) -> bool:
        return self.gasto_real <= self.presupuesto

    def mostrar_info(self) -> str:
        return (
            f"Actividad: {self.nombre} | Tipo: {self.tipo} | "
            f"Presupuesto: {self.presupuesto:.2f} | Gasto real: {self.gasto_real:.2f}"
        )

def page_ej4():
    st.title("Ejercicio 4 - Programación Orientada a Objetos (POO)")

    # Conversion de los dicionarios en objetos
    if "actividades" not in st.session_state:
        st.session_state["actividades"] = []

    if len(st.session_state["actividades"]) == 0:
        st.write("No hay actividades registradas. Agrega actividades en el Ejercicio 2.")
        return

    objetos = [
        Actividad(
            nombre=a["nombre"],
            tipo=a["tipo"],
            presupuesto=a["presupuesto"],
            gasto_real=a["gasto_real"],
        )
        for a in st.session_state["actividades"]
    ]

    # Información de cada objeto
    for act in objetos:
        st.write(act.mostrar_info())

        if act.esta_en_presupuesto():
            st.success("Está dentro del presupuesto.")
        else:
            st.warning("Presupuesto excedido.")