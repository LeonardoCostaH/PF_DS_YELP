import streamlit as st
import pandas as pd
import psycopg2
import numpy as np
import matplotlib
from connect import cursor, conn
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Proyecto Final Yelp")
st.markdown("***") # Línea de división 
st.markdown("## sub-título")
st.markdown("texto")

st.sidebar.markdown("texto en la barra lateral")

# Ejecutar una consulta SQL
# query = "SELECT * FROM usa_states;"
# cursor.execute(query)

# # Obtener los resultados y cargarlos en un DataFrame de pandas
# column_names = [desc[0] for desc in cursor.description]
# df = pd.DataFrame(cursor.fetchall(), columns=column_names)
