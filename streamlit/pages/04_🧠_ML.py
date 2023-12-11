
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


st.set_page_config(
    #page_title="Tu Aplicación",
    #page_icon=":chart_with_upwards_trend:",
    layout="wide",
    initial_sidebar_state="expanded"
)



usa_states = pd.read_csv("../files/data/usa_states.csv")
state_list = sorted(usa_states["state"].tolist()) # Crear una lista de opciones para el checklist
default_selection = ["Utah"]
selected_states = st.sidebar.multiselect('States:', state_list, default=default_selection)

utah_hotels = pd.read_csv("../files/data/usa_hotels.csv")
utah_hotels.dropna(inplace=True)
utah_hotels.isna().sum()
utah_hotels['scores'] = utah_hotels['scores'].apply(literal_eval)

def lista_diccionarios_a_diccionario(lista_diccionarios):
    resultado = {}
    for diccionario in lista_diccionarios:
        resultado.update(diccionario)
    return resultado

utah_hotels["personal_score"] = None
utah_hotels["ammenities_score"] = None
utah_hotels["cleanning_score"] = None
utah_hotels["confort_score"] = None
utah_hotels["price_cuality_score"] = None
utah_hotels["location"] = None
utah_hotels["wifi_score"] = None

for i, row in utah_hotels.iterrows():
    dict_scores = lista_diccionarios_a_diccionario(row["scores"])
    utah_hotels.at[i, "personal_score"] = dict_scores.get("Personal", 0)
    utah_hotels.at[i, "ammenities_score"] = dict_scores.get("Instalaciones y servicios", 0)
    utah_hotels.at[i, "cleanning_score"] = dict_scores.get("Limpieza", 0)
    utah_hotels.at[i, "confort_score"] = dict_scores.get("Confort", 0)
    utah_hotels.at[i, "price_cuality_score"] = dict_scores.get("Relación calidad-precio", 0)
    utah_hotels.at[i, "location"] = dict_scores.get("Ubicación", 0)
    utah_hotels.at[i, "wifi_score"] = dict_scores.get("WiFi gratis", 0)
utah_hotels.drop(columns=["scores"], inplace=True)

hotels = utah_hotels.copy()
client_list = sorted(hotels["name"].tolist())
selected_clients = st.sidebar.multiselect('Clients:', client_list) # Crear el checklist desplegable
hotels['is_client'] = hotels['name'].apply(lambda x: 1 if x in selected_clients else 0)

mi_gradiente_invertida = ['#9D1E27', '#FFFFFF']

score_categories = ["personal_score", "amenities_score", "cleaning_score", "comfort_score", "price_quality_score", "location", "wifi_score"]
default_selection = ["personal_score"]
selected_categories = st.sidebar.multiselect('Categorías:', score_categories, default=default_selection)

fig = px.scatter_3d(hotels, x='price', y='state', z="avg_score", color='is_client',
                    color_continuous_scale=mi_gradiente_invertida)

fig.update_layout(scene=dict(xaxis=dict(autorange="reversed")))
fig.update_traces(marker=dict(size=3, sizemode='diameter'))
fig.update_layout(width=1500, height=800, margin=dict(t=5))  # Ajustar el margen superior
fig.update(layout_coloraxis_showscale=False)

st.plotly_chart(fig)