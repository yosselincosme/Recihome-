import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from mapa import mostrar_mapa  # Importar la función mostrar_mapa desde mapa.py
from distribucion_general import distribucion_general  # Importar la función de distribución general
from pag_principal import pagina_principal  # Página principal
from resumen import dashboard_residuos  # Resumen de residuos (basado en tu segundo código)

# Cargar archivo CSV
url = "https://raw.githubusercontent.com/Sawamurarebatta/Recihome-/main/SEGUNDO_PROYECTO/residuos.csv"
archivo_cargado = pd.read_csv(url, sep=';', encoding='latin1')

# Crear el menú horizontal
selected = option_menu(
    menu_title="Menú Principal",  # Título del menú
    options=["Página principal", "Distribución general", "Mapa", "Resumen", "Filtros Avanzados"],  # Opciones del menú
    icons=["house", "bar-chart", "map", "clipboard", "filter"],  # Íconos para cada opción
    menu_icon="cast",  # Ícono general del menú
    default_index=0,  # Opción predeterminada al cargar
    orientation="horizontal",  # Menú horizontal
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "11px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "blue"},
    }
)  # Estilo del menú

# Mostrar contenido según la opción seleccionada
if selected == "Página principal":
    pagina_principal()

elif selected == "Distribución general":
    st.title("Distribución general")
    st.write("Aquí puedes analizar la distribución general de los datos.")
    distribucion_general(archivo_cargado)

elif selected == "Mapa":
    st.title("Mapa")
    st.write("Esta sección muestra un mapa interactivo de residuos.")
    
    # Llamar a la función que genera el mapa desde mapa.py
    mostrar_mapa(archivo_cargado)

elif selected == "Resumen":
    st.title("Resumen General")
    dashboard_residuos(archivo_cargado)

elif selected == "Filtros Avanzados":
    st.title("Análisis de Residuos por Departamento")
    
    # Filtros de selección en la barra lateral
    with st.sidebar:
        st.header("Filtros para el análisis por departamento")
        departamento = st.selectbox(
            "Selecciona un Departamento",
            archivo_cargado['DEPARTAMENTO'].unique()
        )
    
    # Filtrar y graficar datos
    datos_filtrados = archivo_cargado[archivo_cargado['DEPARTAMENTO'] == departamento]
    columnas_residuos = archivo_cargado.loc[:, 'QRESIDUOS_DOM':archivo_cargado.columns[-2]].columns
    datos_agrupados = datos_filtrados.groupby('DEPARTAMENTO')[columnas_residuos].sum().reset_index()

    # Crear gráfico con Plotly
    fig = px.bar(
        datos_agrupados.melt(id_vars='DEPARTAMENTO', var_name='Residuos', value_name='Cantidad'),
        x='Residuos',
        y='Cantidad',
        color='DEPARTAMENTO',
        title=f"Distribución de Residuos por Departamento: {departamento}",
        color_discrete_sequence=["#636EFA", "#EF553B", "#00CC96"]  # Colores personalizados
    )

    # Configuración del gráfico
    fig.update_layout(
        title_font=dict(size=24, color="#333"),  # Fuente personalizada
        xaxis_title_font=dict(size=18, color="#333"),
        yaxis_title_font=dict(size=18, color="#333"),
        font=dict(size=14, color="#333")  # Fuente predeterminada
    )

    # Mostrar el gráfico
    st.plotly_chart(fig)

