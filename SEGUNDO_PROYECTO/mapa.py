import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import geopandas as gpd
import json
import requests

# Función para cargar y procesar el mapa con los datos de residuos
def mostrar_mapa(archivo_cargado):
    # Cargar el archivo GeoJSON de las regiones de Perú
    geojson_url = "https://raw.githubusercontent.com/Sawamurarebatta/Recihome-/main/SEGUNDO_PROYECTO/peru_regions.geojson"
    geojson_data = requests.get(geojson_url).json()  # Usamos requests para cargar el GeoJSON

    # Filtrar los datos del CSV para obtener los residuos por departamento
    residuos_por_departamento = archivo_cargado.groupby('DEPARTAMENTO').sum().reset_index()

    # Asegurarse de que las columnas de residuos están presentes
    residuos_columnas = ['QRESIDUOS_DOM', 'QRESIDUOS_COM', 'QRESIDUOS_INDUSTRIAL']  # Ajusta según tus columnas

    # Crear un DataFrame para los residuos por departamento
    residuos_totales = residuos_por_departamento[["DEPARTAMENTO"] + residuos_columnas]
    residuos_totales = residuos_totales.set_index("DEPARTAMENTO")

    # Procesar el GeoJSON y combinar con los datos de residuos
    for feature in geojson_data['features']:
        departamento_name = feature['properties']['name']  # Nombre del departamento en el GeoJSON
        if departamento_name in residuos_totales.index:
            feature['properties']['residuos_dom'] = residuos_totales.loc[departamento_name, 'QRESIDUOS_DOM']
            feature['properties']['residuos_com'] = residuos_totales.loc[departamento_name, 'QRESIDUOS_COM']
            feature['properties']['residuos_industrial'] = residuos_totales.loc[departamento_name, 'QRESIDUOS_INDUSTRIAL']
        else:
            feature['properties']['residuos_dom'] = 0
            feature['properties']['residuos_com'] = 0
            feature['properties']['residuos_industrial'] = 0

    # Crear el gráfico de mapa interactivo con Plotly
    fig = go.Figure(go.Choroplethmapbox(
        geojson=geojson_data,
        locations=[feature['properties']['name'] for feature in geojson_data['features']],
        z=[feature['properties']['residuos_dom'] for feature in geojson_data['features']],
        colorscale="Viridis",
        colorbar_title="Residuos Domésticos",
    ))

    fig.update_layout(
        title="Distribución de Residuos en Perú por Departamento",
        mapbox_style="carto-positron",
        mapbox_zoom=4,
        mapbox_center={"lat": -9.19, "lon": -75.0152},  # Centrado aproximado de Perú
        margin={"r":0,"t":0,"l":0,"b":0},
    )

    st.plotly_chart(fig)


