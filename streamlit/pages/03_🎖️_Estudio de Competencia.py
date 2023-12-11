import streamlit as st
from connect import cursor, conn
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import warnings
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

warnings.filterwarnings("ignore")

usa_states = pd.read_csv("../files/data/usa_states.csv")
usa_cities = pd.read_csv("../files/data/usa_cities.csv")
clients = pd.read_csv("../files/data/usa_clients.csv", index_col=0)
california_hotels = pd.read_csv("../files/data/booking/california_hotels.csv", index_col=0)


st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
    page_title="Tu Aplicación",
    page_icon=":chart_with_upwards_trend:"
)


# FILTERS

selected_state = st.sidebar.selectbox('State', ["California", "Florida"])
california = usa_states[usa_states["state_id"] == "CA"]

selected_client = st.sidebar.selectbox('Client hotel', clients['name'].unique())




# VISUALZIATION

default_center = {"lat": 36.7783, "lon": -119.4179}  # Example center for California
california_bbox = {"lon_min": -124.55, "lon_max": -114.13, "lat_min": 32.53, "lat_max": 42.0,}

cities_map = px.scatter_geo(
    california_hotels,
    lat="latitude",
    lon="longitude",
    color_discrete_sequence=["blue"],
    title="Geographic distribution:",
    width=600,
    height=500,
    scope="usa",
    center=default_center,
    size='avg_score')
cities_map.update_traces(marker=dict(line=dict(width=0)), opacity=0.25)  # Ajustar la opacidad

cities_map.update_layout(title_x=0.7)
cities_map.update_geos(
    center_lon=default_center["lon"],
    center_lat=default_center["lat"],
    lonaxis_range=[california_bbox["lon_min"], california_bbox["lon_max"]],
    lataxis_range=[california_bbox["lat_min"], california_bbox["lat_max"]],)


scatter_plot = px.scatter(
    california_hotels,
    x="price",  # Replace with the actual column you want on the x-axis
    y="avg_score",  # Replace with the actual column you want on the y-axis
    title="Price/Score relation:",
    width=300,
    height=500,
    opacity=0.25)









score_columns = [
    'Personal', 'Instalaciones y servicios', 'Limpieza', 'Confort',
    'Relación calidad-precio', 'Ubicación', 'WiFi Gratis'
]


hotel_name = 'Hyatt Regency San Francisco'
hotel_data = california_hotels[california_hotels['name'] == hotel_name][score_columns].transpose()
hotel_data.columns = ['Hotel Score']
hotel_data['Categoria'] = hotel_data.index


state_avg_scores = california_hotels[score_columns].mean().reset_index()
state_avg_scores.columns = ['Categoria', 'State Average Score']

combined_data = pd.merge(hotel_data, state_avg_scores, on='Categoria')


fig = px.bar(combined_data, x='Categoria', y=['Hotel Score', 'State Average Score'],
             labels={'value': 'Puntuación', 'variable': 'Categoría'},
             title=f'Comparación de Puntuaciones para el Hotel {hotel_name} y Promedios Estatales',
             height=400,
             template='plotly_white',
             barmode='group')  # Utilizar 'group' para agrupar las barras












col1, col2, col3 = st.columns((2, 2, 4))

with col1:
    st.plotly_chart(cities_map, use_container_width=True)
    

with col2:
    st.plotly_chart(fig, use_container_width=True)



with col3:
    st.plotly_chart(scatter_plot, use_container_width=True)