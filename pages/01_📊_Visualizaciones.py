import streamlit as st
import pandas as pd
import numpy as np
from connect import cursor, conn
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

# rutas yelp
ruta_yelp_hotel_business = "./datasets/yelp/yelp_hotel_business.csv"
ruta_yelp_hotel_reviews = "./datasets/yelp/yelp_hotel_reviews.csv"
ruta_yelp_tips = "./datasets/yelp/yelp_tips.csv"
ruta_yelp_users = "./datasets/yelp/yelp_users.csv"

# Dataframes yelp

yelp_hotel_business = pd.read_csv(ruta_yelp_hotel_business)
yelp_hotel_reviews = pd.read_csv(ruta_yelp_hotel_reviews)
yelp_tips = pd.read_csv(ruta_yelp_tips)
yelp_users = pd.read_csv(ruta_yelp_users)

df_yelp_hotel_business = pd.DataFrame(yelp_hotel_business)
df_yelp_hotel_reviews = pd.DataFrame(yelp_hotel_reviews)
df_yelp_tips = pd.DataFrame(yelp_tips)
df_yelp_users = pd.DataFrame(yelp_users)

if st.checkbox("mostrar dataframe"):
    st.dataframe(df_yelp_hotel_business)
if st.checkbox("vista de datos Head o Tail"):
    if st.button("Mostrar Head"):
        st.write(df_yelp_hotel_business.head())
    if st.button("Mostrar Tail"):
        st.write(df_yelp_hotel_business.tail())

dim = st.radio("Dimensión a mostrar:",("filas", "columnas"), horizontal=True)

if dim == "filas":
    st.write("Cantidad de filas:", df_yelp_hotel_business.shape[0])
if dim == "columnas":
    st.write("Cantidad de columnas: ", df_yelp_hotel_business.shape[1])


df = df_yelp_hotel_business

# Convert 'avg_rating' to numeric (if not already)
df['stars'] = pd.to_numeric(df['stars'], errors='coerce')

# Calculate the average of 'avg_rating' by 'state'
avg_ratings_by_state = df.groupby('city_id')['stars'].mean().reset_index()

# Set Seaborn theme
sns.set_theme(style="whitegrid")

# Bar plot of average ratings by state
fig = plt.figure(figsize=(10, 5))
sns.barplot(x='city_id', y='stars', data=avg_ratings_by_state, ci=None, color='purple')
plt.title('Average Ratings by state (Bar Plot)')
plt.xticks(rotation=45)
st.pyplot(fig)


