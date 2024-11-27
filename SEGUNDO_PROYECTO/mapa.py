import pandas as pd
import streamlit as st
import plotly.express as px

def mostrar_mapa(archivo_cargado):
    """
    Genera un mapa interactivo que muestra la distribución de residuos por departamento.
    """
    st.title("Mapa de Residuos por Departamento")

    # Verifica que el archivo contenga las columnas necesarias
    if "DEPARTAMENTO" not in archivo_cargado.columns:
        st.error("El archivo no contiene la columna 'DEPARTAMENTO'.")
        return

    # Filtrar columnas de residuos
    columnas_residuos = archivo_cargado.loc[:, 'QRESIDUOS_DOM':archivo_cargado.columns[-2]].columns
    residuos_por_region = archivo_cargado.groupby('DEPARTAMENTO')[columnas_residuos].sum()
    residuos_por_region["Total Residuos"] = residuos_por_region.sum(axis=1)

    # Crear el mapa interactivo
    mapa_peru = px.choropleth(
        residuos_por_region.reset_index(),
        geojson="https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/peru-departments.geojson",
        locations="DEPARTAMENTO",
        featureidkey="properties.name",
        color="Total Residuos",
        color_continuous_scale="Viridis",
        labels={"Total Residuos": "Cantidad de Residuos (kg)"},
        title="Distribución de Residuos por Departamento"
    )
    mapa_peru.update_geos(fitbounds="locations", visible=False)

    # Mostrar el mapa en Streamlit
    st.plotly_chart(mapa_peru, use_container_width=True)
