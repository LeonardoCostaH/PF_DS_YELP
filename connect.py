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

def obtener_datos(cursor, tabla, *columnas):
    try:
        # Aquí ejecuta tu consulta SQL para obtener datos de Google
        cursor.execute(f"SELECT {', '.join(columnas)} FROM {tabla}")
        data = cursor.fetchall()
        # Convierte los resultados en un DataFrame de pandas
        df = pd.DataFrame(data, columns=columnas)
        return df
    except Exception as e:
        print(f"Error al obtener datos: {e}")
        # En lugar de cerrar el cursor aquí, lo cerraremos después de usarlo
    return None

def guardar_en_postgres(dataframe, tabla, conn):
    """
    Envía los datos de un DataFrame a una tabla en PostgreSQL.

    Parámetros:
    - dataframe: El DataFrame que se desea enviar.
    - tabla: El nombre de la tabla en PostgreSQL.
    - conn: La conexión a la base de datos PostgreSQL.

    Ejemplo de uso:
    conn = psycopg2.connect(dbname="nombre_base_de_datos", user="usuario", password="contraseña", host="localhost", port="5432")
    enviar_datos_a_postgres(df, 'nombre_de_tu_tabla', conn)
    conn.close()
    """
    # Crear un motor SQLAlchemy para utilizar el método to_sql
    engine = create_engine(f'postgresql+psycopg2://{conn.dsn}')
    
    # Enviar el DataFrame a la tabla
    dataframe.to_sql(tabla, engine, if_exists='append', index=False)

