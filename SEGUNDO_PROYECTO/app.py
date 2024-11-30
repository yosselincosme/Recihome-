import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from pag_principal import pagina_principal
from distribucion_general import distribucion_general, grafico_lineal_por_periodo
from filtros_avanzados import filtros_avanzados
from mapa import dashboard_residuos
from colores import colores  # Importar el diccionario de colores

# Configurar la página
st.set_page_config(layout="wide")

# Aplicar el fondo principal en toda la aplicación (sin usar CSS)
st.markdown(f"""
    <style>
        .stApp {{
            background-color: {colores['fondo_principal']};
        }}
    </style>
    """, unsafe_allow_html=True)

# Cargar datos
url = "https://raw.githubusercontent.com/Sawamurarebatta/Recihome-/main/SEGUNDO_PROYECTO/residuos.csv"
try:
    archivo_cargado = pd.read_csv(url, sep=';', encoding='latin1')
except Exception as e:
    st.error(f"Error al cargar los datos: {e}")

# Crear el menú horizontal
selected = option_menu(
    menu_title="",
    options=["Página principal", "Distribución general", "Mapa", "Filtros Avanzados"],
    icons=["house", "bar-chart", "map", "clipboard", "filter"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "5px", "background-color": colores['fondo_principal']},  # Fondo en RGB
        "icon": {"color": colores['encabezado'], "font-size": "20px"},  # Colores RGB
        "nav-link": {
            "font-size": "14px",
            "margin": "5px",
            "text-align": "center",
            "--hover-color": colores['fondo_sidebar']  # Color de hover en RGB
        },
        "nav-link-selected": {"background-color": "rgb(154, 140, 152)", "font-weight": "bold"},  # Color de selección
    }
)

# Mostrar contenido según la opción seleccionada
if selected == "Página principal":
    pagina_principal()

elif selected == "Distribución general":
    st.title("Distribución general")
    st.write("Aquí puedes analizar la distribución general de los datos.")
    distribucion_general(archivo_cargado)
    grafico_lineal_por_periodo(archivo_cargado)

elif selected == "Mapa":
    dashboard_residuos(archivo_cargado)

elif selected == "Resumen":
    st.title("Resumen")
    st.write("Aquí encontrarás un resumen general de la información.")

elif selected == "Filtros Avanzados":
    filtros_avanzados(archivo_cargado)

