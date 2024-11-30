import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from pag_principal import pagina_principal
from distribucion_general import distribucion_general, grafico_lineal_por_periodo
from filtros_avanzados import filtros_avanzados
from mapa import dashboard_residuos
from colores import obtener_css  # Importar la función para obtener el CSS

# Configurar la página
st.set_page_config(layout="wide")

# Colores para personalizar estilos
colores = {
    'none': '#024754',  # Fondo del menú
    'boton': '#FFFFFF'  # Color de los íconos
}

# Agregar CSS para personalizar la apariencia
st.markdown(obtener_css(), unsafe_allow_html=True)

# Cargar datos
url = "https://raw.githubusercontent.com/Sawamurarebatta/Recihome-/main/SEGUNDO_PROYECTO/residuos.csv"
try:
    archivo_cargado = pd.read_csv(url, sep=';', encoding='latin1')
except Exception as e:
    st.error(f"Error al cargar los datos: {e}")

# Crear el menú horizontal
selected = option_menu(
    menu_title="Menú Principal",
    options=["Página principal", "Distribución general", "Mapa", "Resumen", "Filtros Avanzados"],
    icons=["house", "bar-chart", "map", "clipboard", "filter"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "5px", "background-color": colores['none']},
        "icon": {"color": colores['boton'], "font-size": "20px"},
        "nav-link": {
            "font-size": "14px",
            "margin": "5px",
            "text-align": "center",
            "--hover-color": "#ddd"
        },
        "nav-link-selected": {"background-color": "#FF6347", "font-weight": "bold"},
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
    geojson_url = 'https://raw.githubusercontent.com/Sawamurarebatta/Recihome-/main/SEGUNDO_PROYECTO/peru_regions.geojson'
    # Asegúrate de que `depurar_geojson` esté implementada correctamente
    depurar_geojson(geojson_url)

elif selected == "Filtros Avanzados":
    filtros_avanzados(archivo_cargado)
