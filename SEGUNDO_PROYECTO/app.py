import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from pag_principal import pagina_principal
from distribucion_general import distribucion_general

# Inyectar estilos CSS personalizados
st.markdown(
    """
    <style>
    /* Fondo principal */
    .stApp {
        background-color: #E9EFEC;
    }
    
    /* Fondo del sidebar */
    [data-testid="stSidebar"] {
        background-color: #C4DAD2;
    }
    
    /* Encabezados */
    h1, h2, h3, h4 {
        color: #16423C;
    }
    
    /* Botones y enlaces */
    .css-1q8dd3e, .css-1aumxhk, .st-cv {
        background-color: #6A9C89 !important;
        color: #E9EFEC !important;
        border: 1px solid #16423C !important;
    }
    
    /* Texto general */
    .css-16huue1 {
        color: #16423C !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Cargar el archivo CSV
url = "https://raw.githubusercontent.com/Sawamurarebatta/Recihome-/main/SEGUNDO_PROYECTO/residuos.csv"
archivo_cargado = pd.read_csv(url, sep=';', encoding='latin1')

# Crear el menú horizontal
selected = option_menu(
    menu_title=None,
    options=["Página principal", "Distribución general", "Mapa", "Resumen", "Análisis por Departamento"],
    icons=["house", "bar-chart", "map", "clipboard", "filter"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

# Mostrar contenido según la opción seleccionada
if selected == "Página principal":
    pagina_principal()

elif selected == "Distribución general":
    st.title("Distribución general")
    st.write("Aquí puedes analizar la distribución general de los datos.")
    distribucion_general(archivo_cargado)

elif selected == "Mapa":
    st.title("Mapa")
    st.write("Esta sección muestra un mapa interactivo.")

elif selected == "Resumen":
    st.title("Resumen")
    st.write("Aquí encontrarás un resumen general de la información.")

elif selected == "Análisis por Departamento":
    st.title("Análisis de Residuos por Departamento")
    
    with st.sidebar:
        st.header("Filtros para el análisis por departamento")
        departamento = st.selectbox(
            "Selecciona un Departamento",
            archivo_cargado['DEPARTAMENTO'].unique()
        )
    
    datos_filtrados = archivo_cargado[archivo_cargado['DEPARTAMENTO'] == departamento]
    columnas_residuos = archivo_cargado.loc[:, 'QRESIDUOS_DOM':archivo_cargado.columns[-2]].columns
    datos_agrupados = datos_filtrados.groupby('DEPARTAMENTO')[columnas_residuos].sum().reset_index()

    fig = px.bar(
        datos_agrupados.melt(id_vars='DEPARTAMENTO', var_name='Residuos', value_name='Cantidad'),
        x='Residuos',
        y='Cantidad',
        color='DEPARTAMENTO',
        title=f"Distribución de Residuos por Departamento: {departamento}",
        color_discrete_sequence=['#16423C', '#6A9C89', '#C4DAD2', '#E9EFEC']
    )

    st.plotly_chart(fig)
