import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from pag_principal import pagina_principal
from distribucion_general import distribucion_general
from colores import colores, inyectar_estilos  # Importar los colores y la función para inyectar los estilos

# Inyectar los estilos CSS globalmente
st.markdown(inyectar_estilos(), unsafe_allow_html=True)

# Cargar el archivo CSV
url = "https://raw.githubusercontent.com/Sawamurarebatta/Recihome-/main/SEGUNDO_PROYECTO/residuos.csv"
archivo_cargado = pd.read_csv(url, sep=';', encoding='latin1')

# Inyectar estilo CSS personalizado para el menú
st.markdown("""
    <style>
        .css-1d391kg {  # Esta clase es para los íconos del menú
            font-size: 12px !important;  # Reducir el tamaño de los íconos
        }
        .css-1v0mbdj {  # Esta clase es para el texto de los íconos
            font-size: 10px !important;  # Reducir el tamaño del texto
        }
        .css-1d391kg, .css-1v0mbdj {
            padding: 10px 20px;  # Rediseñar el espaciado alrededor de los íconos
        }
        .stMenu {  # Clase general para el menú
            font-size: 10px !important;  # Hacer la fuente del menú más pequeña
            padding: 10px 20px;  # Espaciado para que sea más largo horizontalmente
            display: flex;
            justify-content: center;
            background-color: #16423C;  # Color de fondo del menú
            width: 300%;  # Asegurarse de que el menú abarque toda la página
            position: fixed;  # Fijar el menú en la parte superior
            top: 0;
            left: 0;
            z-index: 1000;  # Asegurarse de que el menú esté sobre otros elementos
        }
        .stMenu a {
            color: #FFFFFF;  # Texto blanco
            transition: background-color 0.3s ease;
        }
        .stMenu a:hover {
            background-color: #E57B29;  # Color de fondo del texto cuando se pasa el ratón
        }
        .main {  # Ajustar el contenido principal para que no quede cubierto por el menú
            margin-top: 60px;  # Dejar espacio en la parte superior para el menú fijo
        }
    </style>
""", unsafe_allow_html=True)

# Crear el menú horizontal
selected = option_menu(
    menu_title=None,
    options=["Página principal", "Distribución general", "Mapa", "Resumen", "Análisis por Departamento"],
    icons=["house", "bar-chart", "map", "clipboard", "filter"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={"container": {"max-width": "300%", "padding": "10px 0"}},  # Hacer el menú más largo para abarcar toda la página
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
    
    # Filtros de selección en la barra lateral
    with st.sidebar:
        st.header("Filtros para el análisis por departamento")
        departamento = st.selectbox(
            "Selecciona un Departamento",
            archivo_cargado['DEPARTAMENTO'].unique()
        )
    
    # Filtrado de datos
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

    # Configuración del gráfico
    fig.update_layout(
        title_font=dict(size=24, color=colores['encabezado']),  # Usar la fuente predeterminada
        xaxis_title_font=dict(size=18, color=colores['encabezado']),
        yaxis_title_font=dict(size=18, color=colores['encabezado']),
        font=dict(size=14, color=colores['texto_general'])  # Fuente predeterminada para el cuerpo
    )

    # Mostrar el gráfico
    st.plotly_chart(fig)



