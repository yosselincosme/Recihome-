import pandas as pd
import streamlit as st
from colores import colores  # Importa el diccionario de colores

def pagina_principal():
    st.title("Recihome")
    st.write("Una app centrada en la visualización, recolección y reciclaje de residuos en el hogar, "
             "permitiendo monitorear en tiempo real los residuos generados por los hogares en todo el Perú mediante gráficos y promedios de cada vivienda.")
    st.write("Usa el menú de la izquierda para navegar entre páginas.")

# Función para inyectar los estilos CSS personalizados
def inyectar_estilos():
    return f"""
    <style>
    /* Fondo principal */
    .stApp {{
        background-color: {colores['fondo_principal']};
    }}
    
    /* Fondo del sidebar */
    [data-testid="stSidebar"] {{
        background-color: {colores['fondo_sidebar']};
    }}
    
    /* Encabezados */
    h1, h2, h3, h4 {{
        color: {colores['encabezado']};
    }}
    
    /* Botones y enlaces */
    .css-1q8dd3e, .css-1aumxhk, .st-cv {{
        background-color: {colores['boton']} !important;
        color: {colores['fondo_principal']} !important;
        border: 1px solid {colores['encabezado']} !important;
    }}
    
    /* Texto general */
    .css-16huue1 {{
        color: {colores['texto_general']} !important;
    }}
    </style>
    """
    
# Inyectar los estilos en la app
st.markdown(inyectar_estilos(), unsafe_allow_html=True)

   
