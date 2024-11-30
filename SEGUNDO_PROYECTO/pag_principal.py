import pandas as pd
import streamlit as st

# Función para la página principal
def pagina_principal():
    # Inyectar los estilos CSS personalizados

    # Título de la aplicación con texto grande
    st.markdown("""
        <h1 style="font-size: 50px; text-align: center;">Recihome</h1>
    """, unsafe_allow_html=True)
    
    # Descripción de la aplicación con texto más grande
    st.markdown("""
        <p style="font-size: 20px; text-align: justify;">
            Una app centrada en la visualización, recolección y reciclaje de residuos en el hogar, 
            permitiendo monitorear en tiempo real los residuos generados por los hogares en todo el Perú mediante gráficos y promedios de cada vivienda.
        </p>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <p style="font-size: 18px; text-align: center;">
            Usa el menú de la izquierda para navegar entre páginas.
        </p>
    """, unsafe_allow_html=True)

    # Imagen en la esquina inferior derecha
    st.markdown("""
        <div style="position: fixed; bottom: 10px; right: 10px; z-index: 999;">
            <img src="https://raw.githubusercontent.com/Sawamurarebatta/Recihome-/main/SEGUNDO_PROYECTO/planeta.png" width="150">
        </div>
    """, unsafe_allow_html=True)
