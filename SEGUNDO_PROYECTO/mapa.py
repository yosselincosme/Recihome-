import pandas as pd
import streamlit as st
import plotly.express as px

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

    # 2. Crear una fila para el mapa y el gráfico de barras
    row1_col1, row1_col2 = st.columns([2, 1])  # Columna ancha para el mapa y una columna más estrecha para el gráfico

    with row1_col1:
        st.subheader("Mapa de Generación de Residuos por Departamento")
        mapa_peru = px.choropleth(
            residuos_por_region.reset_index(),
            geojson="https://raw.githubusercontent.com/Sawamurarebatta/Recihome-/main/SEGUNDO_PROYECTO/peru_regions.geojson",  # GeoJSON del Perú
            locations="DEPARTAMENTO",  # Asegúrate de que esta columna coincida con los nombres en el GeoJSON
            featureidkey="properties.name",  # Asegúrate de que coincidan los nombres de departamentos
            color="Total Residuos",
            color_continuous_scale="Viridis",
            labels={"Total Residuos": "Cantidad de Residuos (kg)"},
            title="Distribución de Residuos por Departamento"
        )
        # Cambiar solo el color de fondo
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
        # Cambiar solo el color de fondo
        top_chart.update_layout(
            paper_bgcolor='rgba(0, 51, 51, 1)',  # Fondo del gráfico
            plot_bgcolor='rgba(240, 240, 240, 1)',  # Fondo del área de trazado
        )
        st.plotly_chart(top_chart, use_container_width=True)

    # Nota al pie
    st.info("Datos basados en el archivo proporcionado. La información puede ser explorada de manera interactiva.")

# Ejemplo de uso
if __name__ == "__main__":
    st.title("Análisis de Residuos por Región")
    
    # Subida de archivo
    archivo = st.file_uploader("Sube tu archivo CSV", type="csv")
    
    if archivo:
        # Cargar datos
        datos = pd.read_csv(archivo)
        dashboard_residuos(datos)

