import psycopg2
conexion = psycopg2.connect(
    user='postgres',
    password='carljr107',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)
try:
    with conexion: #Iniciamos conexion
        with conexion.cursor() as cursor: #Este bloque cierra el cursor
            sentencia='DELETE FROM Persona WHERE id_persona=%s;'
            valores=(10,)
            cursor.execute(sentencia, valores)
            #Al usar WITH el COMMIT es automático
            registros_eliminados = cursor.rowcount
            print("los registros eliminados son: ", registros_eliminados)
except Exception as e:
    print("Ocurrio un error: ",e)
finally:
    conexion.close()