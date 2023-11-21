import warnings
import pandas as pd
import seaborn as sns
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Importar y transformar sig data
sig_provincias = gpd.read_file("data/sig/provincia.shp")
sig_localidades = gpd.read_file("data/sig/localidad_bahra.shp")
sig_provincias["nam"] = sig_provincias["nam"].str.replace("Ciudad Autónoma de Buenos Aires", "Capital Federal")
sig_provincias["nam"] = sig_provincias["nam"].str.replace("Tierra del Fuego, Antártida e Islas del Atlántico Sur", "Tierra Del Fuego")
sig_provincias["nam"] = sig_provincias["nam"].str.replace("Santiago del Estero", "Santiago Del Estero")
sig_provincias.drop(columns=["gid", "entidad", "fna", "gna", "in1", "fdc", "sag"], inplace=True)
sig_provincias.rename(columns={"nam": "Provincia"}, inplace=True)

# Color palete
white = "#FFFFFF"
black = "#000000"

sns.set_theme(style="whitegrid")

def map_technology(prov_data, loc_data, technology, max_color, min_color):
    cmap = LinearSegmentedColormap.from_list('custom_colormap', [max_color, min_color], N=256)
    vmin = prov_data[technology].min()
    vmax = prov_data[technology].max()
    fig, ax = plt.subplots(figsize=(8, 8))
    prov_data.plot(column=technology, legend=False, ax=ax, edgecolor='black', linewidth=0.5, cmap=cmap, vmin=vmin, vmax=vmax)
    loc_data[f"scaled_{technology}"] = (loc_data[technology] - loc_data[technology].min()) / (loc_data[technology].max() - loc_data[technology].min()) * (50 - 5) + 5
    loc_data.plot(ax=ax, color="white", edgecolor="black", alpha=0.5, markersize=loc_data[f"scaled_{technology}"])
    plt.gcf().set_facecolor("white") # Background
    plt.gca().set_facecolor("white") # Background
    plt.title(f"{technology}", fontsize=12, color="black", loc='center')
    ax.set_xlim([-85, -45])
    ax.set_ylim([-57, -20])
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.set_facecolor('white')
    cax = plt.axes([0.3, 0.1, 0.4, 0.03])
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=vmin, vmax=vmax))
    sm._A = []
    cbar = plt.colorbar(sm, cax=cax, orientation='horizontal')
    plt.show()


# 
def missing_values_heatmap(dataframe, title):
    # Create and configurate heatmap
    sns.heatmap(data=dataframe.isnull().T, cbar=False, annot_kws={"color": "red"}, cmap=sns.color_palette(["#0D1117", white]))
    plt.gcf().set_facecolor("#0D1117") # Background
    plt.gca().set_facecolor("#0D1117") # Background
    plt.title(f"{title} missing values", fontsize=10, loc='left', color=white) # Title
    plt.yticks(fontsize=9, color=white) # Y axis
    plt.xticks([]) # X axis
    # Save and show
    plt.savefig(f"gallery/ETL/{title}.png", format='png', dpi=300, bbox_inches='tight')
    plt.show()

#
def histogram(column, title):
    # Create histogram
    plt.figure(figsize=(10, 6))
    plt.gcf().set_facecolor("#0D1117") # Background
    plt.gca().set_facecolor("#0D1117") # Background
    plt.hist(column, bins=len(column.value_counts()), color=white, edgecolor=white)
    # Title
    plt.title(title, fontsize=10, loc='right', color=white)
    # X axis
    plt.xticks(fontsize=9, color=white) 
    plt.xlabel('')
    # Y axis
    plt.yticks(fontsize=9, color=white)
    plt.ylabel('')
    # Grid
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(color='darkgrey', linewidth=0.25)
    # Annotate the bars with their respective counts
    #for p in ax.patches:
    #    ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()), 
    #                ha='center', va='center', rotation=90, fontsize=9, color=back_color, xytext=(0, -20), textcoords='offset points')
    # Muestra el histograma
    plt.savefig(f"gallery/EDA/{title}.png", format='png', dpi=300, bbox_inches='tight')
    plt.show()

#
def barplot(data, title):
    plt.figure(figsize=(10, 6))
    plt.gcf().set_facecolor("#0D1117") # Background
    plt.gca().set_facecolor("#0D1117") # Background
    data.plot(kind='bar', color=white, edgecolor=white)
    # Title
    plt.title(title, fontsize=10, loc='right', color=white)
    # X axis
    plt.xticks(fontsize=9, color=white) 
    plt.xlabel('')
    # Y axis
    plt.yticks(fontsize=9, color=white)
    plt.ylabel('')
    # Grid
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(True)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(True)
    ax.grid(color='darkgrey', linewidth=0.25)
    # Annotate the bars with their respective counts
    #for p in ax.patches:
    #    ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()), 
    #                ha='center', va='center', rotation=90, fontsize=9, color=back_color, xytext=(0, -20), textcoords='offset points')
    # Muestra el histograma
    plt.savefig(f"gallery/EDA/{title}.png", format='png', dpi=300, bbox_inches='tight')
    plt.show()
    

def scatter_plot(data, title):

    red_color = "#E63946"
    back_color = "#0D1117"

    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))
    plt.gca().set_facecolor(back_color)
    sns.scatterplot(x='date', y='price', data=data, color="white", size="score", legend=False, edgecolor='none', alpha=0.4, sizes=(5,250))
    #sns.scatterplot(x='date', y='price', data=edata_white, color=red_color, size='count', legend=False, edgecolor='none', alpha=0.4, sizes=(5,250))

    plt.xlabel('')


    plt.ylabel('')
    #title = plt.title(f"{price}                ", loc='right')
    #title.set_color(red_color)

    # Quitar el borde de la grilla en los ejes
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    plt.xticks(rotation=90)
    plt.tick_params(axis='x', colors='grey')  
    plt.tick_params(axis='y', colors='grey')  
    plt.yticks(fontsize=6)
    plt.xticks(fontsize=6)

    # Cambia el color de la grilla de fondo a gris
    ax.grid(color='darkgrey', linewidth=0.25)

    # Guardar el gráfico como un archivo JPEG
    plt.savefig(f"gallery/EDA/{title}scatter_plot.jpg", format='jpg', dpi=300, bbox_inches='tight', facecolor=back_color)