import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from pag_principal import pagina_principal
from distribucion_general import distribucion_general
from colores import colores, inyectar_estilos  # Importar la función para inyectar los estilos
from PIL import ImageFont  # Usaremos PIL para cargar la fuente TrueType

# Inyectar los estilos CSS en la aplicación
st.markdown(inyectar_estilos(), unsafe_allow_html=True)

# Cargar el archivo CSV
url = "https://raw.githubusercontent.com/Sawamurarebatta/Recihome-/main/SEGUNDO_PROYECTO/residuos.csv"
archivo_cargado = pd.read_csv(url, sep=';', encoding='latin1')

# Subir y cargar la fuente .ttf
font_path = "custom_font.ttf"  # Reemplaza con la ruta correcta de tu archivo de fuente .ttf

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

    # Usar Plotly para crear el gráfico de barras
    fig = px.bar(
        datos_agrupados.melt(id_vars='DEPARTAMENTO', var_name='Residuos', value_name='Cantidad'),
        x='Residuos',
        y='Cantidad',
        color='DEPARTAMENTO',
        title=f"Distribución de Residuos por Departamento: {departamento}",
        color_discrete_sequence=colores['grafico']  # Usar los colores desde el archivo de configuración
    )

    # Configuración de la fuente en el gráfico
    fig.update_layout(
        title_font=dict(family="custom_font", size=24, color=colores['encabezado']),
        xaxis_title_font=dict(family="custom_font", size=18, color=colores['encabezado']),
        yaxis_title_font=dict(family="custom_font", size=18, color=colores['encabezado']),
        font=dict(family="custom_font", size=14, color=colores['texto_general'])
    )

    # Cargar la fuente en el gráfico
    fig.update_layout(
        font=dict(family="Arial, sans-serif")  # Usa "Arial" si la fuente no está disponible
    )
    
    # Mostrar el gráfico
    st.plotly_chart(fig)

