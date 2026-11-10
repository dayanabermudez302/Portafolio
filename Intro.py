import os
import streamlit as st
from PIL import Image

# Configuración de ancho completo
st.set_page_config(layout="wide")

# Título principal
st.title("Aplicaciones de Inteligencia Artificial.")

# --- BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    st.subheader("Aplicaciones con Inteligencia Artificial.")
    parrafo = (
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
        "resulta en una mayor eficiencia y precisión en diversos campos."
    )
    st.write(parrafo)

# --- ENLACE GENERAL ---
url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")

st.write("---")  # Línea divisoria

# Función auxiliar para cargar imagen de forma segura sin romper la App
def cargar_imagen(nombre_archivo, width_size=200):
    if os.path.exists(nombre_archivo):
        img = Image.open(nombre_archivo)
        st.image(img, width=width_size)
    else:
        # Muestra una imagen genérica si el archivo no existe en el repo
        st.image("https://via.placeholder.com/200x120.png?text=IA+App", width=width_size)

# --- MATRIZ DE COLUMNAS (3 COLUMNAS) ---
col1, col2, col3 = st.columns(3)

# ----------------- COLUMNA 1 -----------------
with col1:
    st.subheader("Conversión de texto a voz")
    cargar_imagen('txt_to_audio2.png', width_size=190)
    st.write("En la siguiente enlace usaremos una de las aplicaciones de Inteligencia Artificial") 
    url1 = "https://imultimod.streamlit.app/"
    st.write(f"Texto a voz: [Enlace]({url1})")

    st.subheader("Reconocimiento de Objetos")
    cargar_imagen('txt_to_audio.png', width_size=200)
    st.write("En la siguiente enlace veremos como se detectan objetos en Imágenes.") 
    url2 = "https://yolov5cmc.streamlit.app/"
    st.write(f"YOLO: [Enlace]({url2})")

    st.subheader("Entrenando Modelos")
    cargar_imagen('OIG5.jpg', width_size=200)
    st.write("En la siguiente enlace veremos como puedes usar tu modelo entrenado.") 
    url3 = "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"
    st.write(f"YOLO: [Enlace]({url3})")

# ----------------- COLUMNA 2 -----------------
with col2: 
    st.subheader("Conversión de voz a texto")
    cargar_imagen('OIG8.jpg', width_size=200)
    st.write("En la siguiente veremos una aplicación que usa la conversión de voz a texto.") 
    url4 = "https://traductorw.streamlit.app/"
    st.write(f"Voz a texto: [Enlace]({url4})")

    st.subheader("Análisis de Datos")
    cargar_imagen('data_analisis.png', width_size=190)
    st.write("En la siguiente enlace veremos como se pueden analizar datos usando agentes.") 
    url5 = "https://dataagente.streamlit.app/"
    st.write(f"Datos: [Enlace]({url5})")

    st.subheader("Transcriptor Audio y Video")
    cargar_imagen('OIG3.jpg', width_size=200)
    st.write("En la siguiente enlace veremos como realizamos transcripciones de audio/video.") 
    url6 = "https://transcript-whisper.streamlit.app/"
    st.write(f"Transcriptor: [Enlace]({url6})")

# ----------------- COLUMNA 3 -----------------
with col3: 
    st.subheader("Generación en Contexto")
    cargar_imagen('Chat_pdf.png', width_size=190)
    st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
    url7 = "https://chatpdf-cc.streamlit.app/"
    st.write(f"RAG: [Enlace]({url7})")

    st.subheader("Análisis de Imagen")
    cargar_imagen('OIG4.jpg', width_size=200)
    st.write("En la siguiente enlace veremos la capacidad de análisis en Imágenes.") 
    url8 = "https://vision2-gpt4o.streamlit.app/"
    st.write(f"Vision: [Enlace]({url8})")

    st.subheader("Sistema Ciberfísico")
    cargar_imagen('OIG6.jpg', width_size=200)
    st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
    url9 = "https://vision2-gpt4o.streamlit.app/"
    st.write(f"Vision: [Enlace]({url9})")
