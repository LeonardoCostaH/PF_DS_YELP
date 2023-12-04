import warnings
import streamlit as st
import pandas as pd
import numpy as np
from connect import cursor, conn
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import geopandas as gpd
from shapely.geometry import Point
from matplotlib.colors import LinearSegmentedColormap




warnings.filterwarnings("ignore")
warnings.filterwarnings("ignore", category=FutureWarning, module="seaborn._oldcore")
warnings.filterwarnings("ignore", category=FutureWarning, module="seaborn._core")


# Importar y transformar sig data
usa_states = pd.read_csv("data/usa_states.csv")
usa_cities = pd.read_csv("data/usa_cities.csv")
sig_states = gpd.read_file("data/sig/Estados/Estados_Unidos_Estados.shp")
sig_cities = gpd.read_file("data/sig/Ciudades/Estados_Unidos_Poblaciones.shp")
sig_routes = gpd.read_file("data/sig/Vialidad/Estados_Unidos_Vialidad.shp")
sig_hidrography = gpd.read_file("data/sig/Hidrografia/Estados_Unidos_Hidrografia.shp")
sig_california = sig_states[sig_states["STATE_NAME"] == "California"]
sig_florida = sig_states[sig_states["STATE_NAME"] == "Florida"]
sig_newyork = sig_states[sig_states["STATE_NAME"] == "New York"]
sig_utah = sig_states[sig_states["STATE_NAME"] == "Utah"]
utah_attractions = pd.read_csv("data/utah_attractions.csv")

# Supongamos que usa_cities es tu DataFrame con columnas 'latitude' y 'longitude'
usa_cities['geometry'] = usa_cities.apply(lambda row: Point(row.longitude, row.latitude), axis=1)

# Crea el GeoDataFrame usando la columna 'geometry'
usa_cities_gdf = gpd.GeoDataFrame(usa_cities, geometry='geometry')
usa_cities_gdf.crs = "EPSG:4326"
usa_cities = gpd.GeoDataFrame(usa_cities, geometry="geometry")

utah_hotels = pd.read_csv("data/booking_utah_hotels.csv")
count = utah_hotels.groupby("city")["name"].count()
utah_hotel_count = pd.DataFrame(count.reset_index())
utah_hotel_count.columns = ["city", "hotel_count"]
utah_hotel_count = pd.merge(utah_hotel_count, usa_cities[usa_cities["state_id"] == "UT"], on="city", how="left")
utah_hotel_count = gpd.GeoDataFrame(utah_hotel_count, geometry='geometry')
utah_hotel_count.crs = "EPSG:4326"
utah_hotel_count = gpd.GeoDataFrame(utah_hotel_count, geometry="geometry")


def generar_mapa(estado_seleccionado):

    if estado_seleccionado == "Utah":

        # Calculate top cities with most hotels
        count = utah_hotels.groupby("city")["name"].count()
        utah_hotel_count = pd.DataFrame(count.reset_index())
        utah_hotel_count.columns = ["city", "hotel_count"]
        utah_hotel_count = pd.merge(utah_hotel_count, usa_cities[usa_cities["state_id"] == "UT"], on="city", how="left").dropna()
        top_10_cities_with_most_hotels = utah_hotel_count.sort_values(by="hotel_count", ascending=False).head(10)
        # Reescalate sizes
        min_size = top_10_cities_with_most_hotels['hotel_count'].min()
        max_size = top_10_cities_with_most_hotels['hotel_count'].max()
        size_range = (10, 500)  # Define the desired range of marker sizes
        normalized_sizes = (top_10_cities_with_most_hotels['hotel_count'] - min_size) / (max_size - min_size)
        top_10_cities_with_most_hotels['normalized_hotel_count'] = size_range[0] + normalized_sizes * (size_range[1] - size_range[0])


        title = "U T A H"
        fig, ax = plt.subplots(figsize=(8, 8))
        # Define a range of sizes for the markers
        fig.patch.set_facecolor('#0E1117')
        min_size = usa_cities['population'].min()
        max_size = usa_cities['population'].max()
        size_range = (10, 5000)  # Define the desired range of marker sizes
        normalized_sizes = (usa_cities['population'] - min_size) / (max_size - min_size)
        usa_cities['normalized_population'] = size_range[0] + normalized_sizes * (size_range[1] - size_range[0])

        # Plot
        sig_hidrography.plot(ax=ax, color="gray", edgecolor="none", alpha=0.25, markersize=10)
        sig_routes.plot(ax=ax, color="gray", edgecolor="none", alpha=0.5, markersize=10)
        sig_states.plot(ax=ax, color="white", edgecolor="gray", alpha=1, markersize=10)
        sig_utah.plot(ax=ax, color="white", edgecolor="#780109", alpha=1, markersize=10, linewidth=2)
        usa_cities[usa_cities["state_id"] != "UT"].plot(ax=ax, color="gray", edgecolor="none", alpha=0.5, markersize=usa_cities['normalized_population'])
        usa_cities[usa_cities["state_id"] == "UT"].plot(ax=ax, color="gray", edgecolor="none", alpha=0.1, markersize=usa_cities['normalized_population'])
        
        # Anotar el nombre de las ciudades con más de 100.000 habitantes
        for idx, row in usa_cities[usa_cities["population"] > 100000].iterrows():
            ax.annotate(row["city"], (row["geometry"].x, row["geometry"].y), color="black", fontsize=6, ha='center')
        for idx, row in usa_cities[(usa_cities["state_id"] == "UT") & (usa_cities["population"] > 100000)].iterrows():
            ax.annotate(row["city"], (row["geometry"].x, row["geometry"].y), color="white", fontsize=6, ha='center')

        # Añadir marcadores para las atracciones
        ax.scatter(utah_attractions['longitude_x'], utah_attractions['latitud_x'], color='#780109', marker='*', s=50, label='Attractions')
        # Plot top 10 cities
        ax.scatter(top_10_cities_with_most_hotels['longitude'], top_10_cities_with_most_hotels['latitude'], color='#780109', s=top_10_cities_with_most_hotels['normalized_hotel_count'], label='Attractions', alpha=0.5)

        ax.set_xlim([-116, -107]) # set latitud range
        ax.set_ylim([35, 44]) # set longnitud range
        plt.xticks(fontsize=6, color="white")
        plt.yticks(fontsize=6, color="white")
        plt.title(title, fontsize=14, loc='left', color="white", pad=10)
        # Asignar color a las líneas que delimitan el área del gráfico
        ax.spines['bottom'].set_color('white')
        ax.spines['top'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.spines['right'].set_color('white')

        return fig

    if estado_seleccionado == "California":
        title = "C A L I F O R N I A"
        fig, ax = plt.subplots(figsize=(10, 10))
        # Define a range of sizes for the markers
        min_size = usa_cities['population'].min()
        max_size = usa_cities['population'].max()
        size_range = (10, 5000)  # Define the desired range of marker sizes
        normalized_sizes = (usa_cities['population'] - min_size) / (max_size - min_size)
        usa_cities['normalized_population'] = size_range[0] + normalized_sizes * (size_range[1] - size_range[0])
        sig_california.plot(ax=ax, color="white", edgecolor="#780109", alpha=1, markersize=10, linewidth=1.5)
        sig_hidrography.plot(ax=ax, color="gray", edgecolor="none", alpha=0.25, markersize=10)
        sig_routes.plot(ax=ax, color="black", edgecolor="none", alpha=0.5, markersize=10)
        sig_states.plot(ax=ax, color="white", edgecolor="black", alpha=0.25, markersize=10)
        usa_cities.plot(ax=ax, color="gray", edgecolor="none", alpha=0.5, markersize=usa_cities['normalized_population'])
        usa_cities[usa_cities["state_id"] == "CA"].plot(ax=ax, color="black", edgecolor="none", alpha=0.25, markersize=usa_cities['normalized_population'])
        usa_cities[(usa_cities["state_id"] == "CA") & (usa_cities["population"] > 500000)].plot(ax=ax, color="red", edgecolor="none", alpha=0.25, markersize=usa_cities['normalized_population'])
        # Anotar el nombre de las ciudades con más de un millón de habitantes
        for idx, row in usa_cities[usa_cities["population"] > 500000].iterrows():
            ax.annotate(row["city"], (row["geometry"].x, row["geometry"].y), color="white", fontsize=6, ha='center')
        for idx, row in usa_cities[(usa_cities["state_id"] == "CA") & (usa_cities["population"] > 500000)].iterrows():
            ax.annotate(row["city"], (row["geometry"].x, row["geometry"].y), color="black", fontsize=6, ha='center')
        ax.set_xlim([-127, -111]) # set latitud range
        ax.set_ylim([30.5, 44]) # set longnitud range
        # Axis nomenclation
        plt.xticks(fontsize=8, color="gray")
        plt.yticks(fontsize=8, color="gray")
        plt.title(title, fontsize=14, loc='right', color="#780109", pad=10)
        # Border lines
        ax.spines['bottom'].set_color('black')
        ax.spines['top'].set_color('black')
        ax.spines['left'].set_color('black')
        ax.spines['right'].set_color('black')
        return fig



def top_10_population_cities(state):
    #
    state_id = usa_states["state_id"][usa_states["state"] == state].iloc[0]
    top_cities_state = usa_cities[usa_cities["state_id"] == state_id].sort_values(by="population", ascending=False).head(10)
    #
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(top_cities_state["city"], top_cities_state["population"], color='white')
    #
    fig.patch.set_facecolor('#0E1117')
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_title(f'Top 10 poluted cities in {state}     ', color="white", loc="right", fontsize=22)
    ax.set_facecolor('#0E1117')
    plt.xticks(rotation=90, ha="right")  # Rotar etiquetas del eje x para mayor claridad
    # Axis nomenclation
    plt.xticks(fontsize=18, color="gray")
    plt.yticks(fontsize=18, color="gray")
    plt.tight_layout()
    # Border lines
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('none')
    return fig

def top_10_population_cities_hotel_score_distribution(state):
    # Prepare data
    state_id = usa_states["state_id"][usa_states["state"] == state].iloc[0]
    top_10_cities = usa_cities[usa_cities["state_id"] == state_id].sort_values(by="population", ascending=False).head(10)
    filtered_data = utah_hotels[utah_hotels["city"].isin(top_10_cities["city"].to_list())]
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='city', y='avg_score', data=filtered_data, color="white")
    # Modificate Figure
    fig.patch.set_facecolor('#0E1117')
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_title(f'Score distribution in top 10 mos poluted cities in {state}', color="white", loc="right", fontsize=22)
    ax.set_facecolor('#0E1117')
    plt.xticks(rotation=90, ha="right")
    plt.xticks(fontsize=18, color="gray")
    plt.yticks(fontsize=18, color="gray")
    plt.tight_layout()
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('none')
    return fig

def top_10_population_cities_hotel_price_distribution(state):
    # Prepare data
    state_id = usa_states["state_id"][usa_states["state"] == state].iloc[0]
    top_10_cities = usa_cities[usa_cities["state_id"] == state_id].sort_values(by="population", ascending=False).head(10)
    filtered_data = utah_hotels[utah_hotels["city"].isin(top_10_cities["city"].to_list())]
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='city', y='price', data=filtered_data, color="white")
    # Modificate Figure
    fig.patch.set_facecolor('#0E1117')
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_title(f'Price distribution in top 10 most poluted cities in {state}', color="white", loc="right", fontsize=22)
    ax.set_facecolor('#0E1117')
    plt.xticks(rotation=90, ha="right")
    plt.xticks(fontsize=18, color="gray")
    plt.yticks(fontsize=18, color="gray")
    plt.tight_layout()
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('none')
    return fig



st.set_page_config(
    #page_title="Tu Aplicación",
    #page_icon=":chart_with_upwards_trend:",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Add list to select state
states = ["Utah", "California", "Florida", "New Yorl"]
selected_state = st.sidebar.selectbox("Selecciona una opción", states)

figura_mapa = generar_mapa(selected_state)





col1, col2, col3 = st.columns((4, 2, 2))  # Col1 toma el 33% y col2 el 66% del ancho total

with col1:
    st.pyplot(figura_mapa)
with col2:
    st.text("")
    st.text("")
    st.pyplot(top_10_population_cities(selected_state))
    st.text("")
    st.text("")
    top_hotels = utah_hotels[["city", "name", "avg_score"]].sort_values(by="avg_score").head(5)
    top_hotels
    st.text("")
    st.text("")
    st.pyplot(top_10_population_cities_hotel_score_distribution(selected_state))
with col3:
    st.text("")
    st.text("")
    st.pyplot(top_10_population_cities(selected_state))
    st.text("")
    st.text("")
    top_hotels = utah_hotels[["city", "name", "avg_score"]].sort_values(by="avg_score").head(5)
    top_hotels
    st.text("")
    st.text("")
    st.pyplot(top_10_population_cities_hotel_price_distribution(selected_state))



    
    


    
    




