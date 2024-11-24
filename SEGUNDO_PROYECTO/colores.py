colores = {
    'fondo_principal': '#16423C',  # Verde oscuro
    'fondo_sidebar': '#C4DAD2',    # Verde claro
    'encabezado': '#FFFFFF',       # Blanco
    'boton': '#6A9C89',            # Verde medio
    'texto_general': '#FFFFFF',    # Blanco
    'grafico': ['#16423C', '#6A9C89', '#C4DAD2', '#E9EFEC']  # Colores para gráficos
}

def inyectar_estilos():
    return f"""
    <style>
    /* Cargar la fuente TTF */
    @font-face {{
        font-family: 'CustomFont';
        src: url('custom_font.ttf') format('truetype');
    }}

    .stApp {{
        background-color: {colores['fondo_principal']};
    }}

    [data-testid="stSidebar"] {{
        background-color: {colores['fondo_sidebar']};
    }}

    h1, h2, h3, h4 {{
        color: {colores['encabezado']};
        font-family: 'CustomFont', sans-serif;
    }}

    .css-1q8dd3e, .css-1aumxhk, .st-cv {{
        background-color: {colores['boton']} !important;
        color: {colores['fondo_principal']} !important;
        border: 1px solid {colores['encabezado']} !important;
    }}

    .css-16huue1 {{
        color: {colores['texto_general']} !important;
        font-family: 'CustomFont', sans-serif;
    }}
    </style>
    """
