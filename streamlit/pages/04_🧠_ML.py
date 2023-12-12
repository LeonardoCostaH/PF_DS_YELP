
import numpy as np
import pandas as pd
import streamlit as st

import matplotlib
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

import time
import numpy as np
import pandas as pd
import geopandas as gpd
import plotly.express as px
from ast import literal_eval
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from connect import cursor, conn


california_hotels = pd.read_csv("../files/data/booking/california_hotels.csv", index_col=0)
matrix = pd.read_csv("../files/data/booking/california_hotels_similarity_matrix.csv", index_col=0)
california_hotels = california_hotels[california_hotels["avg_score"] > 10]



st.set_page_config(
    #page_title="Tu Aplicación",
    #page_icon=":chart_with_upwards_trend:",
    layout="wide",
    initial_sidebar_state="expanded"
)





# FILTERS

selected_client = st.sidebar.selectbox('Client hotel', california_hotels['name'].unique())

filtered_hotel = california_hotels.loc[california_hotels['name'] == selected_client]
california_hotels['similarity'] = matrix[f"{filtered_hotel.index[0]}"]

california_hotels = california_hotels.sort_values(by='similarity', ascending=False)




# Define color mapping for the top 25 and the rest
color_map = {
    True: 'red',  # Top 25 hotels
    False: 'lightblue'  # Rest of the hotels
}

# Create a boolean column indicating whether the hotel is in the top 25
california_hotels['top_25'] = california_hotels.index.isin(california_hotels.head(100).index)

# Plot the 3D scatter plot with color mapping
fig = px.scatter_3d(california_hotels, x='price', y='stars', z="avg_score",
                    color="top_25", color_discrete_map=color_map)

fig.update_layout(scene=dict(xaxis=dict(autorange="reversed")))
fig.update_traces(marker=dict(size=3, sizemode='diameter'))
fig.update_layout(width=1500, height=800, margin=dict(t=5))  # Adjust the top margin
fig.update(layout_coloraxis_showscale=False)




col1, col2= st.columns((2, 2))
with col1:

    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("Similar hotels")
    st.text("")
    st.text("")
    california_hotels[["city", "name", "stars", "avg_score", "similarity"]][california_hotels['top_25'] == True]
with col2:
    st.plotly_chart(fig, use_container_width=True)