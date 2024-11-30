import pandas as pd
import streamlit as st
import plotly.express as px
import requests

def dashboard_residuos(archivo_cargado):
    st.title("Resumen General: Residuos por Región y Tipo")

    # Preprocesamiento
    columnas_residuos = archivo_cargado.loc[:, 'QRESIDUOS_DOM':archivo_cargado.columns[-2]].columns

    # Sumar residuos por departamento
    residuos_por_region = archivo_cargado.groupby('DEPARTAMENTO')[columnas_residuos].sum()
    residuos_por_region["Total Residuos"] = residuos_por_region.sum(axis=1)
    residuos_totales = residuos_por_region["Total Residuos"].sum()

    # Crear una fila de dos columnas para las métricas clave
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Residuos Totales Generados", value=f"{residuos_totales/1_000_000:.2f} M")
    with col2:
        region_max = residuos_por_region["Total Residuos"].idxmax()
        max_residuos = residuos_por_region["Total Residuos"].max()
        st.metric(label=f"Mayor Generación: {region_max}", value=f"{max_residuos/1_000_000:.2f} M")

    # Descargar GeoJSON desde GitHub
    geojson_url = "https://raw.githubusercontent.com/Sawamurarebatta/Recihome-/main/SEGUNDO_PROYECTO/peru_regions.geojson"
    geojson_response = requests.get(geojson_url)

    if geojson_response.status_code == 200:
        peru_geojson = geojson_response.json()
    else:
        st.error("No se pudo cargar el archivo GeoJSON desde GitHub.")
        return

    # Verificar que los nombres coincidan entre los datos y el GeoJSON
    nombres_departamentos_datos = set(residuos_por_region.index.str.upper())
    nombres_departamentos_geojson = {
        feature["properties"]["name"].upper() for feature in peru_geojson["features"]
    }
    coincidencias = nombres_departamentos_datos.intersection(nombres_departamentos_geojson)
    no_coincidencias = nombres_departamentos_datos.difference(nombres_departamentos_geojson)

    if no_coincidencias:
        st.warning(f"Los siguientes departamentos en tus datos no coinciden con el GeoJSON: {', '.join(no_coincidencias)}")

    # Crear una fila para el mapa y el gráfico de barras
    row1_col1, row1_col2 = st.columns([2, 1])  # Columna ancha para el mapa y una columna más estrecha para el gráfico

    with row1_col1:
        st.subheader("Mapa de Generación de Residuos por Departamento")
        mapa_peru = px.choropleth(
            residuos_por_region.reset_index(),
            geojson=peru_geojson,
            locations="DEPARTAMENTO",
            featureidkey="properties.name",
            color="Total Residuos",
            color_continuous_scale="Viridis",
            labels={"Total Residuos": "Cantidad de Residuos (kg)"},
            title="Distribución de Residuos por Departamento"
        )
        # Cambiar el color de fondo
        mapa_peru.update_layout(
            paper_bgcolor='rgba(0, 51, 51, 1)',  # Fondo del gráfico
            plot_bgcolor='rgba(240, 240, 240, 1)',  # Fondo del área de trazado
        )
        mapa_peru.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(mapa_peru, use_container_width=True)

    with row1_col2:
        st.subheader("Top Departamentos por Generación de Residuos")
        top_departamentos = residuos_por_region.nlargest(5, "Total Residuos").reset_index()
        top_chart = px.bar(
            top_departamentos,
            x="Total Residuos",
            y="DEPARTAMENTO",
            orientation="h",
            text="Total Residuos",
            color="DEPARTAMENTO",
            labels={"Total Residuos": "Cantidad de Residuos (kg)", "DEPARTAMENTO": "Departamento"},
            title="Top 5 Departamentos Generadores de Residuos"
        )
        # Cambiar el color de fondo
        top_chart.update_layout(
            paper_bgcolor='rgba(0, 51, 51, 1)',  # Fondo del gráfico
            plot_bgcolor='rgba(240, 240, 240, 1)',  # Fondo del área de trazado
        )
        st.plotly_chart(top_chart, use_container_width=True)



