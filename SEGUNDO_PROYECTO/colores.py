colores = {
    'fondo_principal': 'rgb(255, 221, 210)',  # Fondo de la pantalla principal
    'fondo_sidebar': 'rgb(196, 218, 210)',  # Fondo del sidebar (menú)
    'fondo_menu': 'rgb(255, 255, 255)',  # Fondo específico para el menú
    'encabezado': 'rgb(255, 255, 255)',  # Blanco
    'boton': 'rgb(106, 156, 137)',  # Verde medio
    'texto_general': 'rgb(255, 255, 255)',  # Blanco
    'grafico': [
        'rgb(22, 66, 60)',
        'rgb(106, 156, 137)',
        'rgb(196, 218, 210)',
        'rgb(233, 239, 236)',
    ]  # Colores para gráficos
}

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
        
        /* Fondo específico para el menú */
        .css-1lcbm7d {{
            background-color: {colores['fondo_menu']} !important;
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

