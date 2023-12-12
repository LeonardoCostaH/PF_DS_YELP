import psycopg2
import pandas as pd
from sqlalchemy import create_engine

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


# def obtener_datos(cursor, tabla, *columnas):
#     try:
#         # Aquí ejecuta tu consulta SQL para obtener datos de Google
#         cursor.execute(f"SELECT {', '.join(columnas)} FROM {tabla}")
#         data = cursor.fetchall()
#         # Convierte los resultados en un DataFrame de pandas
#         df = pd.DataFrame(data, columns=columnas)
#         return df
#     finally:
#         # Cerrar el cursor en el bloque finally para garantizar que se cierre incluso en caso de excepción
#         cursor.close()

def obtener_datos(cursor, tabla):
    try:
        # Aquí ejecuta tu consulta SQL para obtener todos los datos de la tabla
        cursor.execute(f"SELECT * FROM {tabla}")
        data = cursor.fetchall()

        # Verificar si se obtuvieron datos
        if not data:
            # Retornar un DataFrame vacío o levantar una excepción según tus necesidades
            return pd.DataFrame()

        # Obtener los nombres de las columnas de la tabla
        column_names = [desc[0] for desc in cursor.description]

        # Convierte los resultados en un DataFrame de pandas
        df = pd.DataFrame(data, columns=column_names)
        return df
    except Exception as e:
        print(f"Error al obtener datos: {e}")
        # En lugar de cerrar el cursor aquí, lo cerraremos después de usarlo
    return None
