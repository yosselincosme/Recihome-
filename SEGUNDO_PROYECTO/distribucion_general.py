import pandas as pd
import plotly.express as px
import streamlit as st

def distribucion_general(archivo_cargado):
    # Filtrar y sumar los residuos por región natural (sin incluir la columna 'PERIODO')
    columnas_residuos = archivo_cargado.columns[10:-1]  # Desde QRESIDUOS_DOM hasta la penúltima columna
    residuos_por_region = archivo_cargado.groupby('REG_NAT')[columnas_residuos].sum()

    # Sumar todos los tipos de residuos por región
    residuos_totales = residuos_por_region.sum(axis=1)

    # Crear un DataFrame para plotly
    df_residuos = residuos_totales.reset_index()
    df_residuos.columns = ['Región Natural', 'Cantidad de Residuos']

    # Configurar los colores por región
    colores = {'COSTA': '#4CAF50', 'SIERRA': '#FF6347', 'SELVA': '#FFEB3B'}

    # Crear el gráfico de barras horizontal
    fig = px.bar(df_residuos,
                 x='Cantidad de Residuos', 
                 y='Región Natural', 
                 orientation='h',
                 color='Región Natural', 
                 color_discrete_map=colores,
                 labels={'Cantidad de Residuos': 'Cantidad de Residuos', 'Región Natural': 'Región Natural'},
                 title='Distribución Acumulada de Residuos por Región Natural')

    # Añadir las etiquetas dentro de las barras
    fig.update_traces(text=df_residuos['Cantidad de Residuos'], textposition='inside', textfont_color='black')

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig)

