# Definición de los colores personalizados
colores = {
    'fondo_principal': '#16423C',  # Verde oscuro
    'fondo_sidebar': '#C4DAD2',    # Verde claro
    'encabezado': '#FFFFFF',       # Blanco
    'boton': '#6A9C89',            # Verde medio
    'texto_general': '#FFFFFF',    # Blanco
    'grafico': ['#16423C', '#6A9C89', '#C4DAD2', '#E9EFEC']  # Colores para gráficos
}

# Estilos CSS
estilos_css = f"""
<style>
/* Cargar la fuente TTF */
@font-face {{
    font-family: 'CustomFont';
    src: url('custom_font.ttf') format('truetype');
}}

 /* Fondo principal */
.stApp {{
    background-color: {colores['fondo_principal']};
}}

 /* Fondo del sidebar */
[data-testid="stSidebar"] {{
    background-color: {colores['fondo_sidebar']};
}}

 /* Encabezados (titulo principal y subtítulos) */
h1, h2, h3, h4 {{
    color: {colores['encabezado']};
    font-family: 'CustomFont', sans-serif;  /* Usar la fuente personalizada */
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
    font-family: 'CustomFont', sans-serif;  /* Usar la fuente personalizada */
}}
</style>
"""


