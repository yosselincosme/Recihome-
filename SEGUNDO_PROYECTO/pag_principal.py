import streamlit as st

# Configuración de la página
st.set_page_config(layout="wide", page_title="Recihome", page_icon="🌍")

# Función para la página principal
def pagina_principal():
    # URL del GIF de fondo
    gif_url = "https://github.com/Sawamurarebatta/Recihome-/blob/main/SEGUNDO_PROYECTO/appl.gif?raw=true"  # URL del GIF

    # Título de la aplicación con texto grande
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
            h1 {{
                font-size: 50px;
                text-align: center;
                font-family: 'Arial', sans-serif;
            }}
            p {{
                font-size: 20px;
                text-align: justify;
                font-family: 'Arial', sans-serif;
            }}
        </style>
        <h1>Recihome</h1>
        <p>
            Una app centrada en la visualización, recolección y reciclaje de residuos en el hogar, 
            permitiendo monitorear en tiempo real los residuos generados por los hogares en todo el Perú mediante gráficos y promedios de cada vivienda.
        </p>
        <p style="font-size: 18px; text-align: center;">
            Usa el menú de la izquierda para navegar entre páginas.
        </p>
    """, unsafe_allow_html=True)
    
    # Imagen interactiva en la esquina inferior derecha
    st.markdown("""
        <div style="position: fixed; bottom: 10px; right: 10px; z-index: 999;">
            <a href="#" id="interactive-logo">
                <img src="https://raw.githubusercontent.com/Sawamurarebatta/Recihome-/main/SEGUNDO_PROYECTO/planeta.png" width="150" style="cursor: pointer;">
            </a>
        </div>
        <script>
            document.getElementById('interactive-logo').onclick = function() {{
                alert('Equipo Recihome: \\n\\n- Yosselin Cosme \\n- Patricia Rebatta \\n- Andrea Jusytin');
            }};
        </script>
    """, unsafe_allow_html=True)

# Llamada a la función principal
pagina_principal()


