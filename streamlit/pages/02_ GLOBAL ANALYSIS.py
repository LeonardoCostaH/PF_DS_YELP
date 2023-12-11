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
usa_attractions = pd.read_csv("../files/data/usa_attractions.csv", index_col=0)
usa_attractions["n_reviews"].fillna(usa_attractions["n_reviews"].mean() ,inplace=True)


hotels = pd.read_csv("../files/data/usa_hotels.csv", index_col=0)

hotel_count_by_city = hotels.groupby(['city', 'state']).size().reset_index(name='hotel_count')
hotel_count_by_city = pd.merge(hotel_count_by_city, usa_states[['state', 'state_id']], on='state', how="left")
hotel_count_by_city = pd.merge(hotel_count_by_city, usa_cities[['city', 'state_id', 'latitude', 'longitude', 'population']], on=['state_id', 'city'], how='left')
hotel_count_by_city = hotel_count_by_city.sort_values(by=['hotel_count'], ascending=False)


st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
    page_title="Tu Aplicación",
    page_icon=":chart_with_upwards_trend:"
)


# FILTER

# Create hotel filters
st.sidebar.markdown("### Filters")


all_regions = usa_attractions["region"].unique()  # Utiliza unique() en lugar de is_unique()
selected_regions = st.sidebar.multiselect('Region', all_regions, default=all_regions)


all_categories = usa_attractions['new_categories'].unique()
selected_attractions_categories = st.sidebar.multiselect('Attraction categories', all_categories, default=all_categories)

filtered_attractions = usa_attractions[(usa_attractions["new_categories"].isin(selected_attractions_categories) & (usa_attractions["region"].isin(selected_regions)))]



# GRAFICOS

# Crear el mapa de ciudades primero
cities_map = px.scatter_geo(
    hotel_count_by_city,
    lat="latitude",
    lon="longitude",
    size="hotel_count",
    color_discrete_sequence=["blue"],
    width=850,
    height=700,
    scope="usa")
cities_map.update_traces(marker=dict(line=dict(width=0)), opacity=0.7)  # Ajustar la opacidad


# Crear el mapa de atracciones después
attractions_map = px.scatter_geo(
    filtered_attractions,
    lat="latitud",
    lon="longitude",
    size="n_reviews",
    color_discrete_sequence=["red"],
    width=850,
    height=700,
    scope="usa")
attractions_map.update_traces(marker=dict(line=dict(width=0)))  # Esto elimina la línea de borde

# Agregar las trazas del primer grupo al mapa existente
for trace in attractions_map.data:
    cities_map.add_trace(trace)




# Gráfico de barras de las 10 atracciones más frecuentes con Plotly
top_attractions = filtered_attractions['new_categories'].value_counts().nlargest(10)
bar_chart = px.bar(
    y=top_attractions.values,
    x=top_attractions.index,
    orientation='v',
    color_discrete_sequence=["red"],
    width=300,
    height=200,
    #text=top_attractions.index
)
bar_chart.update_layout(margin=dict(b=1)) 
#bar_chart.update_xaxes(showticklabels=False)


top_cities = px.bar(hotel_count_by_city.head(10), x='city', y='hotel_count', height=200, width=300)
#top_cities.update_xaxes(showticklabels=False)






col1, col2 = st.columns((2, 5))

with col1:
    st.plotly_chart(bar_chart, use_container_width=True)
    st.plotly_chart(top_cities, use_container_width=True)

with col2:
    st.plotly_chart(cities_map)