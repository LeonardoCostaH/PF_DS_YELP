import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Cargar los datos
#utah_hotels = pd.read_csv("files/data/booking_utah_hotels.csv", index_col=0)
#utah_hotels_reviews = pd.read_csv("files/data/utah_hotels_reviews.csv", index_col=0)

# Establecer la configuración de la página
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
    page_title="Tu Aplicación",
    page_icon=":chart_with_upwards_trend:"
)

st.markdown(
    """
    <style>
        body {
            margin: 0;
            padding: 0;
        }
    </style>
    """,
    unsafe_allow_html=True
)


col1, col2 = st.columns((2, 5))

with col1:
    ...
with col2:
    ...
    