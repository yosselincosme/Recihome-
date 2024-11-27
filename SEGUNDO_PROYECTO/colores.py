# colores.py

colores = {
    'fondo_principal': '#16423C',  # Verde oscuro
    'fondo_sidebar': '#C4DAD2',    # Verde claro
    'encabezado': '#FFFFFF',       # Blanco
    'boton': '#6A9C89',            # Verde medio
    'texto_general': '#FFFFFF',    # Blanco
    'grafico': ['#16423C', '#6A9C89', '#C4DAD2', '#E9EFEC']  # Colores para gráficos
}

# Función para generar el CSS
def obtener_css():
    return f"""
    <style>
        /* Fondo principal */
        .stApp {{
            background-color: {colores['fondo_principal']};
        }}
        
        /* Fondo del sidebar */
        .css-1d391kg {{
            background-color: {colores['fondo_sidebar']} !important;
        }}
        
        /* Encabezados */
        h1, h2, h3, h4, h5, h6 {{
            color: {colores['encabezado']};
        }}
        
        /* Texto general */
        .stText, .stMarkdown {{
            color: {colores['texto_general']};
        }}
        
        /* Estilo de botones */
        .css-1lcbm7d button {{
            background-color: {colores['boton']} !important;
            color: {colores['encabezado']} !important;
        }}
    </style>
    """
