import pandas as pd
import streamlit as st
import plotly.express as px

def mostrar_mapa(archivo_cargado):
    """
    Muestra un mapa interactivo y gráficos relacionados con residuos por región y tipo.
    """
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

    # Crear fila para el mapa y el gráfico de barras
    row1_col1, row1_col2 = st.columns([2, 1])  # Columna ancha para el mapa y una más estrecha para el gráfico

    with row1_col1:
        st.subheader("Mapa de Generación de Residuos por Departamento")
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
        st.plotly_chart(top_chart, use_container_width=True)

    # Crear un gráfico circular
    st.subheader("Distribución de Tipos de Residuos")
    residuos_totales_tipos = archivo_cargado[columnas_residuos].sum().reset_index()
    residuos_totales_tipos.columns = ["Tipo de Residuo", "Cantidad"]
    pie_chart = px.pie(
        residuos_totales_tipos,
        names="Tipo de Residuo",
        values="Cantidad",
        title="Distribución Total de Residuos por Tipo",
        color_discrete_sequence=px.colors.sequential.Viridis
    )
    st.plotly_chart(pie_chart, use_container_width=True)

    # Nota al pie
    st.info("Datos basados en el archivo proporcionado. La información puede ser explorada de manera interactiva.")
