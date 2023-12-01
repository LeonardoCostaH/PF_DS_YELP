import streamlit as st
import pandas as pd
import numpy as np
from connect import cursor, conn
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import geopandas as gpd
from shapely.geometry import Point

utah_hotels = pd.read_csv("data/booking_utah_hotels.csv")

utah_hotels


