import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from pag_principal import pagina_principal
from distribucion_general import distribucion_general, grafico_lineal_por_periodo
from filtros_avanzados import filtros_avanzados
from mapa import dashboard_residuos
from colores import obtener_css  # Importar la función para obtener el CSS

# Configurar la página
st.set_page_config(layout="wide")

# Agregar CSS para personalizar la apariencia
st.markdown(obtener_css(), unsafe_allow_html=True)

# Cargar datos
url = "https://raw.githubusercontent.com/Sawamurarebatta/Recihome-/main/SEGUNDO_PROYECTO/residuos.csv"
archivo_cargado = pd.read_csv(url, sep=';', encoding='latin1')

# Crear el menú horizontal
selected = option_menu(
    menu_title="Menú Principal",
    options=["Página principal", "Distribución general", "Mapa", "Resumen", "Filtros Avanzados"],
    icons=["house", "bar-chart", "map", "clipboard", "filter"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": colores['fondo_sidebar']},
        "icon": {"color": colores['boton'], "font-size": "25px"},
        "nav-link": {"font-size": "10px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "blue"},
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
    geojson_url = 'https://github.com/Sawamurarebatta/Recihome-/blob/main/SEGUNDO_PROYECTO/peru_regions.geojson'
    depurar_geojson(geojson_url)

elif selected == "Filtros Avanzados":
    filtros_avanzados(archivo_cargado)





