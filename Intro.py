import os
import streamlit as st
from PIL import Image

# Configuración para usar todo el ancho de la pantalla
st.set_page_config(layout="wide")

# --- ENCABEZADO Y SIDEBAR ---
st.title("Aplicaciones de Streamlit")

with st.sidebar:
    st.subheader("Aplicaciones con Inteligencia Artificial")
    st.write(
        "Los aprendizajes realizados en computación avanzada se pueden ver "
        "reflejados en las apps que se encuentran en esta página."
    )

url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")

st.write("---")

# Función para cargar imagen sin romper la app si el archivo no existe
def mostrar_imagen(nombre_archivo, ancho=200):
    if os.path.exists(nombre_archivo):
        img = Image.open(nombre_archivo)
        st.image(img, width=ancho)
    else:
        st.image("https://via.placeholder.com/200x120.png?text=Streamlit+App", width=ancho)

# Lista de las 11 aplicaciones con sus datos
apps_data = [
    {
        "titulo": "App 1",
        "link": "https://temphum1409.streamlit.app/",
        "desc": "Monitoreo y análisis de datos de temperatura y humedad en tiempo real.",
        "img": "txt_to_audio2.png"
    },
    {
        "titulo": "App 2",
        "link": "https://serietiempo0709.streamlit.app/",
        "desc": "Análisis, modelado y pronóstico basado en series de tiempo.",
        "img": "txt_to_audio.png"
    },
    {
        "titulo": "App 3",
        "link": "https://snsorapp.streamlit.app/",
        "desc": "Visualización e interacción con lecturas de datos de sensores.",
        "img": "OIG5.jpg"
    },
    {
        "titulo": "App 4",
        "link": "https://pronostico0909.streamlit.app/",
        "desc": "Herramienta interactiva para predicción y estimación de tendencias.",
        "img": "OIG8.jpg"
    },
    {
        "titulo": "App 5",
        "link": "https://paralelismo1910.streamlit.app/",
        "desc": "Demostración de procesamiento en paralelo y optimización de cómputo.",
        "img": "data_analisis.png"
    },
    {
        "titulo": "App 6",
        "link": "https://geoappd.streamlit.app/",
        "desc": "Aplicación de análisis y visualización de datos geoespaciales.",
        "img": "OIG3.jpg"
    },
    {
        "titulo": "App 7",
        "link": "https://clasfruta-mrcstca7buxaq7yff7ctul.streamlit.app/",
        "desc": "Modelo de visión por computador para clasificación automática de frutas.",
        "img": "Chat_pdf.png"
    },
    {
        "titulo": "App 8",
        "link": "https://appstream2026.streamlit.app/",
        "desc": "Dashboard interactivo para análisis de flujos de datos.",
        "img": "OIG4.jpg"
    },
    {
        "titulo": "App 9",
        "link": "https://app2309.streamlit.app/",
        "desc": "Plataforma interactiva para desarrollo de ejercicios prácticos.",
        "img": "OIG6.jpg"
    },
    {
        "titulo": "App 10",
        "link": "https://app0209.streamlit.app/",
        "desc": "Prototipo interactivo para evaluación y pruebas de modelos.",
        "img": "txt_to_audio2.png"
    },
    {
        "titulo": "App 11",
        "link": "https://zd9tc9af9m7qp9rrwhc4cb.streamlit.app/",
        "desc": "Herramienta avanzada de procesamiento y análisis interactivo.",
        "img": "txt_to_audio.png"
    }
]

# --- ORGANIZACIÓN DE LAS 11 APPS EN COLUMNAS ---
cols = st.columns(3)

for idx, app in enumerate(apps_data):
    col = cols[idx % 3]  # Distribución cíclica en 3 columnas
    with col:
        st.subheader(app["titulo"])
        mostrar_imagen(app["img"], ancho=200)
        st.write(app["desc"])
        st.markdown(f"{app['titulo']}: [Enlace]({app['link']})")
        st.write("")  # Espaciado vertical entre tarjetas
