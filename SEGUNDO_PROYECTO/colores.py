# colores.py

# Paleta de colores para la aplicación
colores = {
    'fondo_principal': '#E9EFEC',
    'fondo_sidebar': '#C4DAD2',
    'encabezado': '#16423C',
    'boton': '#6A9C89',
    'texto_general': '#16423C',
    'grafico': ['#16423C', '#6A9C89', '#C4DAD2', '#E9EFEC']
}

# Función para inyectar los estilos CSS personalizados
def inyectar_estilos():
    return f"""
    <style>
    /* Fondo principal */
    .stApp {{
        background-color: {colores['fondo_principal']};
    }}
    
    /* Fondo del sidebar */
    [data-testid="stSidebar"] {{
        background-color: {colores['fondo_sidebar']};
    }}
    
    /* Encabezados */
    h1, h2, h3, h4 {{
        color: {colores['encabezado']};
    }}
    
    /* Botones y enlaces */
    .css-1q8dd3e, .css-1aumxhk, .st-cv {{
        background-color: {colores['boton']} !important;
        color: {colores['fondo_principal']} !important;
        border: 1px solid {colores['encabezado']} !important;
    }}
    
    /* Texto general */
    .css-16huue1 {{
        color: {colores['texto_general']} !important;
    }}
    </style>
    """
