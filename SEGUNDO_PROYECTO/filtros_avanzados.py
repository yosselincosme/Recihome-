import streamlit as st
import plotly.express as px
import pandas as pd

def filtros_avanzados(archivo_cargado):
    
    # Filtros en el sidebar
    with st.sidebar:
        st.header("Filtros para el análisis avanzado")
        
        # Selector para determinar qué filtro usar
        filtro_activo = st.radio(
            "Selecciona qué filtro deseas usar:",
            options=["Por Departamento", "Por Tipo de Residuo"],
            index=0
        )
        
        # Filtro por Departamento
        if filtro_activo == "Por Departamento":
            departamento = st.selectbox(
                "Selecciona un Departamento",
                options=archivo_cargado['DEPARTAMENTO'].unique()
            )
        
        # Filtro por Tipo de Residuo
        elif filtro_activo == "Por Tipo de Residuo":
            columnas_residuos = archivo_cargado.loc[:, 'QRESIDUOS_DOM':archivo_cargado.columns[-2]].columns
            tipo_residuo = st.selectbox(
                "Selecciona un Tipo de Residuo",
                options=columnas_residuos
            )
    
    # Mostrar gráfico basado en el filtro activo
    if filtro_activo == "Por Departamento":
        # Filtrar por Departamento
        datos_filtrados = archivo_cargado[archivo_cargado['DEPARTAMENTO'] == departamento]
        
        # Sumar las columnas de residuos
        columnas_residuos = archivo_cargado.loc[:, 'QRESIDUOS_DOM':archivo_cargado.columns[-2]].columns
        datos_agrupados = datos_filtrados.groupby('DEPARTAMENTO')[columnas_residuos].sum().reset_index()
        
        # Ordenar residuos por suma total para determinar las columnas más frecuentes
        total_residuos = datos_agrupados[columnas_residuos].sum().sort_values(ascending=False)
        top_9_residuos = total_residuos.head(9).index
        otros_residuos = total_residuos.index.difference(top_9_residuos)
        
        # Crear una columna "Otros" que sume los residuos restantes
        datos_agrupados['Otros'] = datos_agrupados[otros_residuos].sum(axis=1)
        datos_agrupados = datos_agrupados[['DEPARTAMENTO'] + list(top_9_residuos) + ['Otros']]

        # Transformar datos para graficar
        melted_data = datos_agrupados.melt(
            id_vars='DEPARTAMENTO', var_name='Residuos', value_name='Cantidad'
        )
        
        # Crear gráfico
        fig = px.bar(
            melted_data,
            x='Residuos',
            y='Cantidad',
            color='DEPARTAMENTO',
            title=f"Distribución de Residuos en el Departamento: {departamento}",
            color_discrete_sequence=px.colors.qualitative.Prism  # Colores más variados
        )
    
    elif filtro_activo == "Por Tipo de Residuo":
        # Agrupar datos por Departamento para el residuo seleccionado
        datos_agrupados = archivo_cargado.groupby('DEPARTAMENTO')[[tipo_residuo]].sum().reset_index()
        
        # Crear gráfico
        fig = px.bar(
            datos_agrupados,
            x='DEPARTAMENTO',
            y=tipo_residuo,
            title=f"Cantidad de {tipo_residuo} por Departamento",
            labels={tipo_residuo: "Cantidad (kg)", "DEPARTAMENTO": "Departamento"},
            color_discrete_sequence=px.colors.qualitative.T10  # Colores más variados
        )
    
    # Personalizar el fondo del gráfico
    fig.update_layout(
        paper_bgcolor='rgba(0, 51, 51, 1)',  # Fondo del gráfico
        plot_bgcolor='rgba(255, 255, 255, 1)',  # Fondo del área de trazado
        font=dict(color='white'),  # Texto blanco para contraste
    )
    
    # Mostrar el gráfico
    st.plotly_chart(fig)


