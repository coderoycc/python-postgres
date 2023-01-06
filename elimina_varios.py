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
            sentencia='DELETE FROM persona WHERE id_persona IN %s;'
            cadena = input('Inserte ID\'s Separados por comas')
            valores=(tuple(cadena.split(',')),) #TUPLA DE TUPLAS
            #ELIMINAMOS MUCHOS
            cursor.execute(sentencia, valores)
            #Al usar WITH el COMMIT es automático
            registros_insertados = cursor.rowcount
            print("los registros eliminados son: ", registros_insertados)
except Exception as e:
    print("Ocurrio un error: ",e)
finally:
    conexion.close()