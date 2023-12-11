import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Cargar los datos
clients = pd.read_csv("../files/data/usa_clients.csv", index_col=0)
clients_reviews = pd.read_csv("../files/data/usa_clients_reviews.csv", index_col=0)
clients_reviews['date'] = pd.to_datetime(clients_reviews['date'])

# Establecer la configuración de la página
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
    page_title="Tu Aplicación",
    page_icon=":chart_with_upwards_trend:"
)

# Create hotel filters
st.sidebar.markdown("### Filters")
date_range = st.sidebar.date_input("Date Range", 
                                   min_value=clients_reviews['date'].min(), 
                                   max_value=clients_reviews['date'].max(), 
                                   value=(clients_reviews['date'].min(), clients_reviews['date'].max()))
selected_state = st.sidebar.selectbox('State', clients['state'].unique())
selected_cities = st.sidebar.multiselect('City', clients['city'][clients["state"] == selected_state].unique())
selected_hotels = st.sidebar.multiselect('Hotel', 
                                         clients['name'][clients["city"].isin(selected_cities)].unique(),
                                         default=clients['name'][clients["city"].isin(selected_cities)].unique())

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
    ...
    #st.plotly_chart(fig1)
    #st.plotly_chart(fig2)
    
with col2:
    ...
    #st.plotly_chart(map)
    