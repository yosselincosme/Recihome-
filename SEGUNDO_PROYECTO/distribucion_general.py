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

def grafico_lineal_por_periodo(archivo_cargado):
    st.title("Evolución de residuos en el tiempo")

    # Filtrar las columnas de residuos (desde QRESIDUOS_DOM hasta la penúltima columna)
    columnas_residuos = archivo_cargado.columns[10:-1]
    
    # Sumar los residuos por año (PERIODO)
    residuos_por_anio = archivo_cargado.groupby('PERIODO')[columnas_residuos].sum()
    
    # Sumar los valores por fila para obtener los totales por año
    residuos_por_anio['Total Residuos'] = residuos_por_anio.sum(axis=1)
    
    # Resetear índice para que sea compatible con Plotly
    residuos_por_anio = residuos_por_anio.reset_index()
    
    # Crear el gráfico de líneas
    fig = px.line(
        residuos_por_anio,
        x='PERIODO',
        y='Total Residuos',
        title="Distribución de Residuos por Año",
        labels={'PERIODO': 'Año', 'Total Residuos': 'Cantidad de Residuos (kg)'},
        markers=True
    )

    # Ajustar los ejes y formato del gráfico
    fig.update_layout(
        xaxis=dict(title="Año"),
        yaxis=dict(title="Cantidad de Residuos (kg)"),
        title=dict(x=0.5),
    )

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig)


