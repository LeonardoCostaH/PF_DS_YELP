import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Cargar los datos
#utah_hotels = pd.read_csv("../../files/data/booking_utah_hotels.csv", index_col=0)
#utah_hotels_reviews = pd.read_csv("../../files/data/utah_hotels_reviews.csv", index_col=0)

# Establecer la configuración de la página
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
    page_title="Tu Aplicación",
    page_icon=":chart_with_upwards_trend:"
)

st.title("G L O B A L  A N A L Y S I S")

# Map

# Datos
categorias = ['Categoria 1', 'Categoria 2', 'Categoria 3', 'Categoria 4', 'Categoria 5']
valores = [20, 35, 25, 40, 15]
colores = ["royalblue","crimson","lightseagreen","orange","lightgrey"]
fig1 = go.Figure(data=[go.Bar(x=valores, y=categorias, orientation='h', marker=dict(color=colores))])
fig1.update_layout(
    title='Top populated 5 cities',
    xaxis_title='Valores',
    yaxis_title='Categorías',
    height=300, 
    width=600)

# Datos
categorias = ['Categoria 1', 'Categoria 2', 'Categoria 3', 'Categoria 4', 'Categoria 5']
valores = [20, 35, 25, 40, 15]
colores = ["royalblue","crimson","lightseagreen","orange","lightgrey"]
fig2 = go.Figure(data=[go.Bar(x=valores, y=categorias, orientation='h', marker=dict(color=colores))])
fig2.update_layout(
    title='Top cities with most hotels',
    xaxis_title='Valores',
    yaxis_title='Categorías',
    height=300, 
    width=600)

# Datos
categorias = ['Categoria 1', 'Categoria 2', 'Categoria 3', 'Categoria 4', 'Categoria 5']
valores = [20, 35, 25, 40, 15]
colores = ["royalblue","crimson","lightseagreen","orange","lightgrey"]
fig3 = go.Figure(data=[go.Bar(x=valores, y=categorias, orientation='h', marker=dict(color=colores))])
fig3.update_layout(
    title='Top 5 popular touristic attractions categories',
    xaxis_title='Valores',
    yaxis_title='Categorías',
    height=300, 
    width=600)


col1, col2 = st.columns((2, 5))

with col1:
    st.plotly_chart(fig1)
    st.plotly_chart(fig2)
    
with col2:
    st.plotly_chart(map)
    