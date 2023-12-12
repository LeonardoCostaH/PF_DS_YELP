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
matrix = pd.read_csv("../files/data/booking/california_hotels_similarity_matrix.csv", index_col=0)
df_reviews = pd.read_csv("../files/data/usa_clients_reviews.csv")
df_reviews['date'] = pd.to_datetime(df_reviews['date'])


st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
    page_title="Tu Aplicación",
    page_icon=":chart_with_upwards_trend:"
)










df_positive_reviews = df_reviews[df_reviews['sentiment'] > 0]

grouped_data = df_reviews.groupby(pd.Grouper(key='date', freq='3M')).agg(
    total_reviews=('sentiment', 'count'),
    positive_reviews=('sentiment', lambda x: (x > 0).sum())
)

grouped_data['PRP'] = (grouped_data['positive_reviews'] / grouped_data['total_reviews']) * 100

growth_rate = 0.02
target_percentage = 90
quarters_to_target = (target_percentage - grouped_data['PRP'].iloc[-1]) / (growth_rate * 100)
date_range = pd.date_range(start=grouped_data.index[-1], periods=int(quarters_to_target * 4) + 1, freq='M')
projected_data = pd.DataFrame(index=date_range)
projected_data['PRP'] = [min(grouped_data['PRP'].iloc[-1] + (growth_rate * 100 * i), target_percentage) for i in range(1, len(projected_data) + 1)]


fig = px.line(grouped_data, x=grouped_data.index, y='PRP',
              labels={'PRP': 'Porcentaje de Reseñas Positivas (%)'},
              title='Porcentaje de Reseñas Positivas (PRP) cada 3 meses',
              markers=True)


fig.add_scatter(x=projected_data.index, y=projected_data['PRP'], mode='lines', line=dict(dash='dash'),
                #name=f'Proyección ({growth_rate*100}% Crecimiento por Trimestre hasta {target_percentage}%)'
                )












negative_reviews = df_reviews[df_reviews['sentiment'] < 0]


threshold_95 = negative_reviews.shape[0] * 0.95


fig_reviews = px.bar(
    x=['Total de Reseñas', 'Reseñas Negativas'],
    y=[df_reviews.shape[0], negative_reviews.shape[0]],
    labels={'y': 'Cantidad de Reseñas', 'x': 'Tipo de Reseña'},
    title='Total de Reseñas y Reseñas Negativas',
)


fig_reviews.add_shape(
    type='line',
    x0=-0.5,
    y0=threshold_95,
    x1=1.5,
    y1=threshold_95,
    line=dict(color='red', dash='dash'),
    name='Umbral del 95% para Reseñas Negativas'
)







family_reviews = df_reviews[df_reviews['company'] == 'En familia']


family_reviews.set_index('date', inplace=True)


average_sentiment_by_month = family_reviews['sentiment'].resample('M').mean()


fig_sent = px.line(average_sentiment_by_month, x=average_sentiment_by_month.index, y=average_sentiment_by_month.values,
              labels={'y': 'Promedio de Sentimiento'},
              title='Promedio Mensual de Sentimiento para Reseñas de Familias')






positive_usa_reviews = df_reviews[(df_reviews['sentiment'] > 0) & (df_reviews['nationality'] == 'Estados Unidos')]


positive_usa_reviews['quarter'] = positive_usa_reviews['date'].dt.to_period("Q")
df_reviews['quarter'] = df_reviews['date'].dt.to_period("Q")


percentage_positive_usa_by_quarter = (
    positive_usa_reviews.groupby('quarter').size() / df_reviews[df_reviews['nationality'] == 'Estados Unidos'].groupby('quarter').size()
) * 100


projected_data_usa_six_months = pd.DataFrame(index=pd.date_range(start=percentage_positive_usa_by_quarter.index[-1].to_timestamp(), periods=7, freq='M'))

growth_rate_usa_six_months = 0.07  # 7% de crecimiento en 6 meses
target_percentage_usa_six_months = round(percentage_positive_usa_by_quarter.iloc[-1] + growth_rate_usa_six_months * 100, 2)


projected_data_usa_six_months['Satisfaction Index'] = (
    percentage_positive_usa_by_quarter.iloc[-1] +
    np.arange(1, len(projected_data_usa_six_months) + 1) * growth_rate_usa_six_months * 100
)


projected_data_usa_six_months['Satisfaction Index'] = np.minimum(
    projected_data_usa_six_months['Satisfaction Index'], target_percentage_usa_six_months
)

fig_usa_six_months = px.line(
    x=percentage_positive_usa_by_quarter.index.to_timestamp(),
    y=percentage_positive_usa_by_quarter.values,
    labels={'y': 'Porcentaje de Reseñas Positivas', 'x': 'Año'},
    title='Porcentaje de Reseñas Positivas para Huéspedes Estadounidenses por Cuatrimestre con Proyección a 6 Meses'
)

fig_usa_six_months.add_scatter(
    x=[projected_data_usa_six_months.index[0], projected_data_usa_six_months.index[-1]],
    y=[percentage_positive_usa_by_quarter.iloc[-1], target_percentage_usa_six_months],
    mode='lines',
    line=dict(color='red', dash='dash'),
    name=f'Proyección (7% Crecimiento por 6 Meses hasta {target_percentage_usa_six_months}%)'
)








col1, col2 = st.columns((2, 2))
with col1:
    st.plotly_chart(fig, use_container_width=True)
    st.text("Kpi1: Aumentar el porcentaje de reseñas positivas (PRP) en un 2% cada 3 meses hasta alcanzar 90%.")
    st.plotly_chart(fig_reviews, use_container_width=True)
    st.text("Kpi3: Mantener el índice de Respuestas a Reseñas Negativas (IRRN) por encima del 95%.")

    

with col2:
    st.plotly_chart(fig_usa_six_months, use_container_width=True)
    st.text("KPI 2: Aumentar el índice de satisfacción de huéspedes de EEUU en los próximos 6 meses en un 7%.")
    st.plotly_chart(fig_sent, use_container_width=True)
    st.text("KPI4: Mantener el promedio mensual de sentimiento para huéspedes que vienen en familia por encima de 0.25.")
