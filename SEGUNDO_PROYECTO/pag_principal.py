import pandas as pd
import streamlit as st

def pagina_principal():
    st.title("Recihome")
    st.write("Una app centrada en la visualización, recolección y reciclaje de residuos en el hogar, "
             "permitiendo monitorear en tiempo real los residuos generados por los hogares en todo el Perú mediante gráficos y promedios de cada vivienda.")
    st.write("Usa el menú de la izquierda para navegar entre páginas.")

    # Cargar el archivo CSV con el delimitador correcto
    try:
        df = pd.read_csv(r"C:\Users\Yosselin\Desktop\SEGUNDO_PROYECTO\residuos.csv", sep=';', encoding='latin1')
        st.write("### Datos de residuos:")
        st.dataframe(df)
    except FileNotFoundError:
        st.error("No se encontró el archivo `residuos.csv`. Asegúrate de que la ruta sea correcta.")
    except UnicodeDecodeError:
        st.error("No se pudo decodificar el archivo. Intenta usar otra codificación como 'latin1' o 'ISO-8859-1'.")
