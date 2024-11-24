import plotly.graph_objects as go

def mostrar_mapa(archivo_cargado):
    # Agrupar por departamento y calcular residuos totales
    residuos_por_departamento = archivo_cargado.groupby('DEPARTAMENTO').sum().reset_index()

    # Cargar el GeoJSON
    geojson_url = "https://raw.githubusercontent.com/Sawamurarebatta/Recihome-/main/SEGUNDO_PROYECTO/peru_regions.geojson"
    geojson_data = requests.get(geojson_url).json()

    # Vincular residuos al GeoJSON
    for feature in geojson_data['features']:
        depto = feature['properties']['name']
        if depto in residuos_por_departamento['DEPARTAMENTO'].values:
            total_residuos = residuos_por_departamento.loc[
                residuos_por_departamento['DEPARTAMENTO'] == depto, 
                ['QRESIDUOS_DOM', 'QRESIDUOS_COM', 'QRESIDUOS_INDUSTRIAL']
            ].sum(axis=1).values[0]
            feature['properties']['total_residuos'] = total_residuos
        else:
            feature['properties']['total_residuos'] = 0

    # Crear el mapa
    fig = go.Figure(go.Choroplethmapbox(
        geojson=geojson_data,
        locations=[f['properties']['name'] for f in geojson_data['features']],
        z=[f['properties']['total_residuos'] for f in geojson_data['features']],
        colorscale="Viridis",
        colorbar_title="Total Residuos",
        marker_opacity=0.7,
        marker_line_width=0
    ))

    # Configurar diseño del mapa
    fig.update_layout(
        mapbox=dict(
            style="carto-positron",
            center={"lat": -9.19, "lon": -75.0152},
            zoom=4
        ),
        margin={"r": 0, "t": 0, "l": 0, "b": 0}
    )

    st.plotly_chart(fig)


