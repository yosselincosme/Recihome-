
import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from pag_principal import pagina_principal
from distribucion_general import distribucion_general, grafico_lineal_por_periodo
from filtros_avanzados import filtros_avanzados
from mapa import dashboard_residuos
from resumen import depurar_geojson

# Configurar la página
st.set_page_config(layout="wide")  # Aquí se configura el layout de la página para usar el espacio completo


url = "https://raw.githubusercontent.com/Sawamurarebatta/Recihome-/main/SEGUNDO_PROYECTO/residuos.csv"
archivo_cargado = pd.read_csv(url, sep=';', encoding='latin1')
# Crear el menú horizontal
selected = option_menu(
    menu_title="Menú Principal",  # Título del menú
    options=["Página principal", "Distribución general", "Mapa", "Resumen", "Filtros Avanzados"],  # Nueva opción
    icons=["house", "bar-chart", "map", "clipboard", "filter"],  # Ícono para la nueva opción
    menu_icon="cast",  # Ícono general del menú
    default_index=0,  # Opción predeterminada al cargar
    orientation="horizontal",  # Menú horizontal
    styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "25px"}, 
            "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "blue"},
        }
)

# Mostrar contenido según la opción seleccionada
if selected == "Página principal":
    pagina_principal()  # Llama a la función desde el archivo pag_principal.py

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
    geojson_url = 'https://raw.githubusercontent.com/johan/world.geo.json/master/countries/PER.geo.json'
    depurar_geojson(geojson_url)

elif selected == "Filtros Avanzados":  # Nueva sección
    filtros_avanzados(archivo_cargado)







