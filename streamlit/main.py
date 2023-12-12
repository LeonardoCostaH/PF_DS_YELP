import streamlit as st
import pandas as pd
import psycopg2
import numpy as np
import matplotlib
from connect import cursor, conn
import seaborn as sns
import matplotlib.pyplot as plt

img_logo = "img/Geogenesis_logo.png"
# Mostrar la imagen con tamaño y alineación personalizados
st.image(img_logo, use_column_width=True)
st.title("¡Bienvenido a Geogenesis Data Solutions!")
st.markdown("***") # Línea de división     
st.markdown("## Nuestra Misión:")
st.markdown("En Geogenesis, nos dedicamos a transformar datos en decisiones estratégicas para impulsar el crecimiento de la industria hotelera. Nuestra misión es ofrecer soluciones innovadoras que permitan a nuestros clientes mejorar sus servicios y tomar decisiones informadas.")

st.sidebar.markdown("## Principales Beneficios para Nuestros Clientes:")
st.sidebar.markdown("- *Optimización del Servicio:* Mejore la calidad del servicio basándose en la retroalimentación de los usuarios.")
st.sidebar.markdown("- *Predicciones Precisas:* Anticipe tendencias y tome decisiones informadas para el crecimiento del negocio.")
st.sidebar.markdown("- *Enfoque en la Experiencia del Cliente:* Alinee sus estrategias con las expectativas y preferencias de sus clientes.")

st.markdown("## ¿Por Qué Elegir Geogenesis?")
st.markdown("- *Experiencia en la Industria:* Conocemos la industria hotelera y entendemos sus desafíos.")
st.markdown("- *Innovación Tecnológica:* Utilizamos las últimas tecnologías para ofrecer soluciones avanzadas.")
st.markdown("- *Compromiso con el Éxito:* Estamos dedicados a impulsar el éxito y el crecimiento de nuestros clientes.")

st.markdown("***")
st.markdown("Descubra el poder de los datos con Geogenesis. ¡Estamos aquí para llevar su negocio hotelero al siguiente nivel!")

# Ejecutar una consulta SQL
# query = "SELECT * FROM usa_states;"
# cursor.execute(query)

# # Obtener los resultados y cargarlos en un DataFrame de pandas
# column_names = [desc[0] for desc in cursor.description]
# df = pd.DataFrame(cursor.fetchall(), columns=column_names)
