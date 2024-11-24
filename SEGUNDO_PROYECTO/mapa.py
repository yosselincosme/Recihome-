import streamlit as st
import pandas as pd
import plotly.express as px
import geopandas as gpd
import plotly.graph_objects as go
import json

# Función para mostrar el mapa interactivo
def mostrar_mapa(archivo_cargado):
    # Cargar el archivo GeoJSON de Perú
    geojson_url = "https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/peru-departments.geojson"
    geojson_data = gpd.read_file(geojson_url)

    # Filtrar los datos del CSV para obtener los residuos por departamento
    residuos_por_departamento = archivo_cargado.groupby('DEPARTAMENTO').sum().reset_index()

    # Asegurarse de que las columnas para los residuos están presentes
    residuos_columnas = ['QRESIDUOS_DOM', 'QRESIDUOS_COM', 'QRESIDUOS_INDUSTRIAL']  # Ajusta según tus columnas

    # Crear un DataFrame para los residuos por departamento
    residuos_totales = residuos_por_departamento[["DEPARTAMENTO"] + residuos_columnas]
    residuos_totales = residuos_totales.set_index("DEPARTAMENTO")

    # Unir los datos del CSV con los datos geojson por el nombre del departamento
    geojson_data['properties']['name'] = geojson_data['properties'].apply(lambda x: x['name'])
    geojson_data = geojson_data.merge(residuos_totales, left_on='properties.name', right_index=True)

    # Crear un gráfico de mapa interactivo usando Plotly
    fig = go.Figure(go.Choroplethmapbox(
        geojson=geojson_data.geometry.__geo_interface__,
        locations=geojson_data.index,
        z=geojson_data['QRESIDUOS_DOM'],  # Puedes cambiar a la columna deseada
        colorscale="Viridis",
        colorbar_title="Cantidad de Residuos Domésticos",
    ))

    fig.update_layout(
        title="Distribución de Residuos en Perú por Departamento",
        mapbox_style="carto-positron",
        mapbox_zoom=4,
        mapbox_center={"lat": -9.19, "lon": -75.0152},  # Centrado aproximado de Perú
        margin={"r":0,"t":0,"l":0,"b":0},
    )

    st.plotly_chart(fig)

