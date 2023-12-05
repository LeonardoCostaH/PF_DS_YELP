import streamlit as st
import pandas as pd
import numpy as np
from connect import cursor, conn
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
from wordcloud import WordCloud
import warnings

warnings.filterwarnings("ignore")

# Función para obtener datos desde la base de datos
def obtener_datos(cursor, tabla, *columnas):
    # Aquí ejecuta tu consulta SQL para obtener datos de Google
    cursor.execute(f"SELECT * FROM {tabla}")
    data = cursor.fetchall()
    # Convierte los resultados en un DataFrame de pandas
    df = pd.DataFrame(data, columns=list(columnas))
    return df

df_google_hotel_business = obtener_datos(cursor, "sources", 'source_id', 'source')
st.dataframe(df_google_hotel_business)

# Obtén datos de Google
google_data = obtener_datos(cursor, "google_hotel_business", "hotel_id", "name", "categories", "avg_rating", "num_of_reviews")

# Gráfico 1: Histograma de puntuaciones promedio
st.subheader("Gráfico 1: Histograma de puntuaciones promedio")
fig, ax = plt.subplots()
ax.hist(google_data["avg_rating"], bins=10, edgecolor="black")
ax.set_xlabel("Puntuación Promedio")
ax.set_ylabel("Frecuencia")
st.pyplot(fig)

google_data = obtener_datos(cursor, "google_hotel_reviews", "hotel_id", "reviews")

# Gráfico 2: Nube de palabras
st.subheader("Gráfico 2: Nube de palabras")
wordcloud_text = " ".join(review for review in google_data["reviews"])
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(wordcloud_text)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
st.pyplot(plt)

# Streamlit App
def main():
    # Configuración de la aplicación
    st.title('Análisis de Sentimientos y Predicción de Crecimiento')

    # Conexión a la base de datos (esto dependerá de cómo tengas configurada tu conexión)
    # cursor = ...

    # Obtener datos de Google y Yelp
    # df_google = obtener_datos(cursor)
    # df_yelp = obtener_datos(cursor, yelp_hotel_business, )

    # # Página 1
    # st.header('Página 1: Análisis de Google')
    # mostrar_histograma(df_google, 'Histograma de Puntuaciones Promedio Google', 'Puntuación Promedio', 'Frecuencia')

    # mostrar_nube_palabras(['Excelente lugar', 'Buen servicio', 'No me gustó'], 'Nube de Palabras en Reseñas Yelp')

# Ejecutar la aplicación
if __name__ == '__main__':
    main()