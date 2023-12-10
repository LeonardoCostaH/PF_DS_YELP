import psycopg2
import pandas as pd

# datos de conexión
dbname = 'postgres'
user = 'postgres'
password = 'ozZpSSXJxNiYbBo6KiLM'
host = 'pfyeld.csogvboudl4p.us-east-2.rds.amazonaws.com'  # endpoint de la base de datos en AWS
port = '5432'  



# Conexión a la base de datos
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)

# Crear un cursor
cursor = conn.cursor()


def guardar_en_postgres(dataframe, nombre_tabla, conn):
    # Crear la tabla si no existe
    dataframe.head(0).to_sql(nombre_tabla, conn, if_exists='replace', index=False)
    
    # Guardar el DataFrame en la tabla
    dataframe.to_sql(nombre_tabla, conn, if_exists='append', index=False)

def obtener_datos(cursor, tabla, *columnas):
    # Aquí ejecuta tu consulta SQL para obtener datos de Google
    cursor.execute(f"SELECT * FROM {tabla}")
    data = cursor.fetchall()
    # Convierte los resultados en un DataFrame de pandas
    df = pd.DataFrame(data, columns=list(columnas))
    return df