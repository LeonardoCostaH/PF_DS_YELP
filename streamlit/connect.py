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