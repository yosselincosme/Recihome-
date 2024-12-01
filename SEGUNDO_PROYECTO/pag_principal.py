import streamlit as st

# Configuración de la página (debe ser la primera llamada a Streamlit)
st.set_page_config(layout="wide")  # Asegúrate de que esta sea la primera instrucción de Streamlit

# Función para la página principal
def pagina_principal():
    # URL del GIF de fondo
    gif_url = "https://github.com/Sawamurarebatta/Recihome-/blob/main/SEGUNDO_PROYECTO/appl.gif?raw=true"

    # URL del logo
    logo_url = "https://github.com/Sawamurarebatta/Recihome-/blob/main/SEGUNDO_PROYECTO/logo.png?raw=true"

    # Variable de estado para mostrar/ocultar nombres
    if "mostrar_nombres" not in st.session_state:
        st.session_state.mostrar_nombres = False

    # Diseño de la página
    st.markdown(f"""
        <style>
            .stApp {{
                background-image: url("{gif_url}");
                background-repeat: no-repeat;
                background-size: cover;
                background-position: center;
                height: 100vh;
                color: white;  /* Cambia el color de texto para hacerlo visible sobre el GIF */
            }}
            .logo-container {{
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 80vh;  /* Ajustar la altura para centrar verticalmente */
            }}
            p {{
                font-size: 20px;
                text-align: justify;
                font-family: 'Arial', sans-serif;
            }}
        </style>
        <div class="logo-container">
            <img src="{logo_url}" alt="Logo" style="max-width: 300px; height: auto;">
        </div>
        <p style="font-size: 18px; text-align: center;">
            Usa el menú de la izquierda para navegar entre páginas.
        </p>
    """, unsafe_allow_html=True)

    # Botón para alternar mostrar/ocultar nombres
    if st.button("Mostrar/Ocultar nombres"):
        st.session_state.mostrar_nombres = not st.session_state.mostrar_nombres

    # Mostrar u ocultar nombres según el estado
    if st.session_state.mostrar_nombres:
        st.markdown("""
            <div style="text-align: center; margin-top: 20px;">
                <p style="font-size: 18px; font-weight: bold;">Yosselin, Patricia, Justin y Andrea</p>
            </div>
        """, unsafe_allow_html=True)

    # Imagen en la esquina inferior derecha
    st.markdown("""
        <div style="position: fixed; bottom: 10px; right: 10px; z-index: 999;">
            <img src="https://raw.githubusercontent.com/Sawamurarebatta/Recihome-/main/SEGUNDO_PROYECTO/planeta.png" width="150">
        </div>
    """, unsafe_allow_html=True)

# Llamar a la función principal
pagina_principal()


