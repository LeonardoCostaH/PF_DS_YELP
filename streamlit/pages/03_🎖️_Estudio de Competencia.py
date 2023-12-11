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
hotels = pd.read_csv("../files/data/usa_hotels.csv", index_col=0)

st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
    page_title="Tu Aplicación",
    page_icon=":chart_with_upwards_trend:"
)

selected_state = st.sidebar.selectbox('State', ["California", "Florida"])


california = usa_states[usa_states["state_id"] == "CA"]

cities_map = px.scatter_geo(
    clients,
    lat="latitude",
    lon="longitude",
    #size="hotel_count",
    color_discrete_sequence=["blue"],
    title="Geographic distribution:",
    width=1000,
    height=900,
    scope="usa")
cities_map.update_traces(marker=dict(line=dict(width=0)), opacity=0.7)  # Ajustar la opacidad
cities_map.update_layout(title_x=0.7)


col1, col2 = st.columns((2, 5))

with col1:
    ...
    #st.plotly_chart(bar_chart, use_container_width=True)
    #st.plotly_chart(top_cities, use_container_width=True)
    #st.plotly_chart(scatter_plot, use_container_width=True)
    
with col2:
    st.plotly_chart(cities_map, use_container_width=True)