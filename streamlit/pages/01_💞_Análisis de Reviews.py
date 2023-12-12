import streamlit as st
import pandas as pd
import numpy as np
from connect import cursor, conn
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
from wordcloud import WordCloud
import warnings
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

warnings.filterwarnings("ignore")

clients = pd.read_csv("../files/data/usa_clients.csv", index_col=0)
clients_reviews = pd.read_csv("../files/data/usa_clients_reviews.csv", index_col=0)

clients_reviews['date'] = pd.to_datetime(clients_reviews['date'])

st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
    page_title="Tu Aplicación",
    page_icon=":chart_with_upwards_trend:"
)

# FILTER

# Create hotel filters
st.sidebar.markdown("### Filters")
date_range = st.sidebar.date_input("Date Range", 
                                   min_value=clients_reviews['date'].min(), 
                                   max_value=clients_reviews['date'].max(), 
                                   value=(clients_reviews['date'].min(), clients_reviews['date'].max()))

selected_state = st.sidebar.selectbox('State', clients['state'].unique())

#cities_to_filter_by = clients['city'][clients["state"] == selected_state].unique()
#selected_cities = st.sidebar.multiselect('City', cities_to_filter_by, default=cities_to_filter_by)



# Create user filters
all_company= clients_reviews['company'].unique()
selected_company = st.sidebar.multiselect('Company', all_company, default=all_company)

all_acommodation=clients_reviews['acommodation'].unique()
selected_acommodation = st.sidebar.multiselect('Accommodation', all_acommodation,default=all_acommodation)

all_stay = list(clients_reviews['stay'].unique())
selected_stay = st.sidebar.multiselect('Stay length', all_stay, default=all_stay)

all_nationality=clients_reviews['is_american'].unique()
selected_nationality = st.sidebar.multiselect('Nationality', all_nationality,default=all_nationality)



# Filter data and calculate


filtered_clients_reviews = clients_reviews[clients_reviews["company"].isin(selected_company)]

filtered_clients_reviews['company'].dropna(inplace=True)
average_sentiment = filtered_clients_reviews['sentiment'].mean()
filtered_clients_reviews['useful'] = 0.1


# GRAFICAR
average_sentiment = 0.55
# Crear el gráfico de torta con la paleta de colores específica
if average_sentiment > 0.5:
    lista_de_colores = ["#689F38", "#8BC34A", "#9CCC65", "#AED581", "#C5E1A5"]
elif 0.5 > average_sentiment > 0:
    lista_de_colores = ["#FFB300", "#FFCA28", "#FFD54F", "#FFE082", "#FFFFFF"]
elif average_sentiment < 0:
    lista_de_colores = ["#3C0000", "#670010", "#960018", "#CB4C46", "#FF8478"]


# Group by month and calculate the average sentiment for each month
filtered_clients_reviews['month'] = filtered_clients_reviews['date'].dt.to_period('M').astype(str)
monthly_average_sentiment = filtered_clients_reviews.groupby('month')['sentiment'].mean().reset_index()

# Create the scatter plot
custom_color_scale = ['#D30F02', '#F7C20E', '#648813']
scatter_plot = px.scatter(filtered_clients_reviews, x="date", y="sentiment",
                          title='Booking reviews analysis:',
                          color='sentiment',
                          color_continuous_scale=custom_color_scale,
                          size='useful',  # Add the column you want to use for bubble size
                          opacity=0.75,
                          height=900,
                          size_max=10)

max_porciones = 5
counts = filtered_clients_reviews['acommodation'].value_counts()
categorias_principales = counts.head(max_porciones).index
filtered_clients_reviews['acommodation_agrupado'] = filtered_clients_reviews['acommodation'].where(filtered_clients_reviews['acommodation'].isin(categorias_principales), 'Otros')
torta_acommodation = px.pie(filtered_clients_reviews, names="acommodation_agrupado", height=400, hole=.5, title='Acommodation:',
                    color_discrete_sequence=lista_de_colores)
torta_acommodation.update_layout(showlegend=False)
torta_acommodation.update_traces(textinfo='label')

torta_company = px.pie(filtered_clients_reviews, names="company", height=400, hole=.5, title='Company:',
                       color_discrete_sequence=lista_de_colores)
torta_company.update_layout(showlegend=False)
torta_company.update_traces(textinfo='label')

torta_isamerican = px.pie(filtered_clients_reviews, names="is_american", height=400, hole=.5, title='Nationality:',
                       color_discrete_sequence=lista_de_colores)
torta_isamerican.update_layout(showlegend=False)
torta_isamerican.update_traces(textinfo='label')

max_porciones = 5
counts = filtered_clients_reviews['stay'].value_counts()
categorias_principales = counts.head(max_porciones).index
filtered_clients_reviews['stay_agrupado'] = filtered_clients_reviews['stay'].where(filtered_clients_reviews['stay'].isin(categorias_principales), 'Otros')
torta_stay = px.pie(filtered_clients_reviews, names="stay_agrupado", height=400, hole=.5, title='Stay lenght:',
                    color_discrete_sequence=lista_de_colores)
torta_stay.update_layout(showlegend=False)
torta_stay.update_traces(textinfo='label')


# STRUCTURE

col1, col2, col3 = st.columns((3, 1, 1))
with col3:
    st.text("")
    st.plotly_chart(torta_acommodation, use_container_width=True)
    st.plotly_chart(torta_stay, use_container_width=True)
with col2:
    st.text("")
    st.plotly_chart(torta_company, use_container_width=True)
    st.plotly_chart(torta_isamerican, use_container_width=True)
with col1:
    st.plotly_chart(scatter_plot, use_container_width=True)



col1, col2 = st.columns((3, 3))
with col1:
    st.text("")
    st.text("")
    st.text("")
    df_copy = filtered_clients_reviews.copy()
    resumenes_texto = ' '.join(df_copy['review'][df_copy['sentiment'] > 0.25].dropna())
    wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='Greens').generate(resumenes_texto)
    wordcloud_image = wordcloud.to_image()
    st.image(wordcloud_image)
with col2:
    st.text("")
    st.text("")
    st.text("")
    df_copy = filtered_clients_reviews.copy()
    resumenes_texto = ' '.join(df_copy['review'][df_copy['sentiment'] < 0.25].dropna())
    wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='Reds').generate(resumenes_texto)
    wordcloud_image = wordcloud.to_image()
    st.image(wordcloud_image)

