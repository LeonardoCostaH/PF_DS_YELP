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

# Agregar un título a la página
st.title("G L O B A L  A N A L Y S I S")

usa_states = pd.read_csv("files/data/usa_states.csv")
state_list = sorted(usa_states["state"].tolist()) # Crear una lista de opciones para el checklist
default_selection = ["Utah"]
selected_states = st.sidebar.multiselect('States:', state_list, default=default_selection)

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_us_cities.csv')
df.head()
df['text'] = df['name'] + '<br>Population ' + (df['pop']/1e6).astype(str)+' million'

limits = [(0,2),(3,10),(11,20),(21,50),(50,3000)]

colors = ["royalblue","crimson","lightseagreen","orange","lightgrey"]
cities = []
scale = 5000

map = go.Figure()

for i in range(len(limits)):

    lim = limits[i]
    df_sub = df[lim[0]:lim[1]]
    map.add_trace(go.Scattergeo(
        locationmode = 'USA-states',
        lon = df_sub['lon'],
        lat = df_sub['lat'],
        text = df_sub['text'],
        marker = dict(
            size = df_sub['pop']/scale,
            color = colors[i],
            line_color='rgb(40,40,40)',
            line_width=0.5,
            sizemode = 'area'
        ),
        name = '{0} - {1}'.format(lim[0],lim[1])))

map.update_layout(
    geo=dict(scope='usa', landcolor='#0E1117'),
    width=1500, height=1000,
    margin=dict(t=0, b=0, l=0, r=0),  # Ajusta el valor de t según tus necesidades
    showlegend=False
)







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
    st.plotly_chart(fig3)
with col2:
    st.plotly_chart(map)
    