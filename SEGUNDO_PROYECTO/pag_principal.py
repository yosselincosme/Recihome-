import pandas as pd
import streamlit as st
from colores import estilos_css  # Importar los estilos desde colores.py

# Función para la página principal
def pagina_principal():
    # Inyectar los estilos CSS personalizados
    st.markdown(estilos_css, unsafe_allow_html=True)

    st.title("Recihome")
    st.write("Una app centrada en la visualización, recolección y reciclaje de residuos en el hogar, "
             "permitiendo monitorear en tiempo real los residuos generados por los hogares en todo el Perú mediante gráficos y promedios de cada vivienda.")
    st.write("Usa el menú de la izquierda para navegar entre páginas.")


