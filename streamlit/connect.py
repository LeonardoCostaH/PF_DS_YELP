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


def obtener_datos(cursor, tabla, *columnas):
    try:
        # Aquí ejecuta tu consulta SQL para obtener datos de Google
        cursor.execute(f"SELECT {', '.join(columnas)} FROM {tabla}")
        data = cursor.fetchall()
        # Convierte los resultados en un DataFrame de pandas
        df = pd.DataFrame(data, columns=columnas)
        return df
    finally:
        # Cerrar el cursor en el bloque finally para garantizar que se cierre incluso en caso de excepción
        cursor.close()