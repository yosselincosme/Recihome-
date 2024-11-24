# Definir los colores en un diccionario
colores = {
    'fondo_principal': '#16423C',  # Verde oscuro
    'fondo_sidebar': '#C4DAD2',    # Verde claro
    'encabezado': '#FFFFFF',       # Blanco
    'boton': '#6A9C89',            # Verde medio
    'texto_general': '#FFFFFF',    # Blanco
    'grafico': ['#16423C', '#6A9C89', '#C4DAD2', '#E9EFEC']  # Colores para gráficos
}

# Función para inyectar los estilos CSS
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

    /* Estilos personalizados para el menú */
    .css-1d391kg {{  # Esta clase es para los íconos del menú
        font-size: 12px !important;  # Reducir el tamaño de los íconos
    }}
    .css-1v0mbdj {{  # Esta clase es para el texto de los íconos
        font-size: 10px !important;  # Reducir el tamaño del texto
    }}
    .css-1d391kg, .css-1v0mbdj {{
        padding:  20px;  # Rediseñar el espaciado alrededor de los íconos
    }}
    .stMenu {{  # Clase general para el menú
        font-size: 6px !important;  # Hacer la fuente del menú más pequeña
        padding: 5000px;  # Espaciado para que sea más largo horizontalmente
        display: flex;
        justify-content: center;
        background-color: {colores['fondo_principal']};  # Color de fondo del menú
        width: 100%;  # Asegurarse de que el menú abarque toda la página
        position: fixed;  # Fijar el menú en la parte superior
        top: 0;
        left: 0;
        z-index: 1000;  # Asegurarse de que el menú esté sobre otros elementos
    }}
    .stMenu a {{
        color: {colores['encabezado']} !important;  # Texto blanco
        transition: background-color 0.3s ease;
    }}
    .stMenu a:hover {{
        background-color: #E57B29;  # Color de fondo del texto cuando se pasa el ratón
    }}
    .main {{  # Ajustar el contenido principal para que no quede cubierto por el menú
        margin-top: 60px;  # Dejar espacio en la parte superior para el menú fijo
    }}
    </style>
    """

