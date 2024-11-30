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

    # Configurar los colores por región usando formato hexadecimal
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

    # Personalizar el fondo y las líneas del gráfico con colores en formato hexadecimal
    fig.update_layout(
        paper_bgcolor='#223D5B',  # Fondo del gráfico (color hexadecimal)
        plot_bgcolor='#223D5B',  # Fondo del área de trazado también en hexadecimal
        font_color='white',  # Texto de los títulos y etiquetas en blanco
        xaxis=dict(
            showgrid=True,  # Mostrar las líneas de cuadrícula
            gridcolor='white',  # Color de las líneas de cuadrícula
            title=dict(font=dict(color='white')),  # Título del eje X
            tickfont=dict(color='white')  # Color de los valores en el eje X
        ),
        yaxis=dict(
            showgrid=False,  # No mostrar las líneas de cuadrícula en el eje Y
            title=dict(font=dict(color='white')),  # Título del eje Y
            tickfont=dict(color='white')  # Color de los valores en el eje Y
        )
    )

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

    # Colores para el gráfico de barras
    colores_barras = ['#640D5F', '#D91656', '#EB5B00', '#FFB200']

    # Crear el gráfico de barras por año
    fig = px.bar(
        residuos_por_anio,
        x='PERIODO',
        y='Total Residuos',
        title="Distribución de Residuos por Año",
        labels={'PERIODO': 'Año', 'Total Residuos': 'Cantidad de Residuos (kg)'},
        color='PERIODO',
        color_discrete_sequence=colores_barras
    )

    # Ajustar el fondo y las líneas con colores en formato hexadecimal
    fig.update_layout(
        paper_bgcolor='#223D5B',  # Fondo del gráfico (color crema en formato hexadecimal)
        plot_bgcolor='#223D5B',  # Fondo del área de trazado también en formato hexadecimal
        font_color='white',  # Texto en blanco
        xaxis=dict(
            showgrid=True,
            gridcolor='white',
            title=dict(font=dict(color='white')),
            tickfont=dict(color='white')
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='white',
            title=dict(font=dict(color='white')),
            tickfont=dict(color='white')
        )
    )

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig)

    # Ahora crear una gráfica del departamento que genera más basura en total
    residuos_por_departamento = archivo_cargado.groupby('DEPARTAMENTO')[columnas_residuos].sum()
    residuos_totales_departamento = residuos_por_departamento.sum(axis=1)
    
    # Crear un DataFrame con los resultados
    df_departamento = residuos_totales_departamento.reset_index()
    df_departamento.columns = ['Departamento', 'Cantidad de Residuos']

    # Encontrar el departamento que genera más residuos
    departamento_max_residuos = df_departamento.loc[df_departamento['Cantidad de Residuos'].idxmax()]

    # Crear una gráfica de barras del departamento con más residuos
    fig_departamento = px.bar(
        df_departamento,
        x='Departamento',
        y='Cantidad de Residuos',
        title=f"Departamento con más residuos: {departamento_max_residuos['Departamento']}",
        labels={'Cantidad de Residuos': 'Cantidad de Residuos (kg)', 'Departamento': 'Departamento'},
        color='Departamento'
    )

    # Personalizar el gráfico con el fondo
    fig_departamento.update_layout(
        paper_bgcolor='#223D5B',
        plot_bgcolor='#223D5B',
        font_color='white',
        xaxis=dict(
            showgrid=True,
            gridcolor='white',
            title=dict(font=dict(color='white')),
            tickfont=dict(color='white')
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='white',
            title=dict(font=dict(color='white')),
            tickfont=dict(color='white')
        )
    )

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig_departamento)
