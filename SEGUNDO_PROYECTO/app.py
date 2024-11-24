import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from pag_principal import pagina_principal
from distribucion_general import distribucion_general

# Cargar el archivo CSV
archivo_cargado = pd.read_csv("residuos.csv", sep=';', encoding='latin1')

# Crear el menú horizontal
selected = option_menu(
    menu_title="Menú Principal",  # Título del menú
    options=["Página principal", "Distribución general", "Mapa", "Resumen", "Análisis por Departamento"],  # Nueva opción
    icons=["house", "bar-chart", "map", "clipboard", "filter"],  # Ícono para la nueva opción
    menu_icon="cast",  # Ícono general del menú
    default_index=0,  # Opción predeterminada al cargar
    orientation="horizontal",  # Menú horizontal
)

# Mostrar contenido según la opción seleccionada
if selected == "Página principal":
    pagina_principal()  # Llama a la función desde el archivo pag_principal.py

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

elif selected == "Análisis por Departamento":  # Nueva sección
    st.title("Análisis de Residuos por Departamento")
    
    # Agregar filtros en el sidebar para esta sección
    with st.sidebar:
        st.header("Filtros para el análisis por departamento")
        departamento = st.selectbox(
            "Selecciona un Departamento",
            archivo_cargado['DEPARTAMENTO'].unique()
        )
    
    # Filtrar datos por el departamento seleccionado
    datos_filtrados = archivo_cargado[archivo_cargado['DEPARTAMENTO'] == departamento]

    # Seleccionar columnas desde 'QRESIDUOS_DOM' hasta la penúltima
    columnas_residuos = archivo_cargado.loc[:, 'QRESIDUOS_DOM':archivo_cargado.columns[-2]].columns

    # Agrupar y sumar los datos por columnas
    datos_agrupados = datos_filtrados.groupby('DEPARTAMENTO')[columnas_residuos].sum().reset_index()

    # Crear gráfico de barras con Plotly
    fig = px.bar(
        datos_agrupados.melt(id_vars='DEPARTAMENTO', var_name='Residuos', value_name='Cantidad'),
        x='Residuos',
        y='Cantidad',
        color='DEPARTAMENTO',
        title=f"Distribución de Residuos por Departamento: {departamento}",
    )

    # Mostrar el gráfico
    st.plotly_chart(fig)
