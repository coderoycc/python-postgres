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
            sentencia='UPDATE Persona SET nombre = %s, apellido=%s, email=%s WHERE id_persona=%s;'
            valores=(
                ('Pablo Jaime', 'Fernandez', 'pajafer@mail.com', 6),
                ('Ramiro Celin', 'Collani', 'raco@mail.com', 7),
                ('Juan', 'Perez', 'jperez@mail.com', 1)
            )
            #ACTUALIZAMOS MUCHOS executemany
            cursor.executemany(sentencia, valores)
            #Al usar WITH el COMMIT es automático
            registros_insertados = cursor.rowcount
            print("los registros actualizados son: ", registros_insertados)
except Exception as e:
    print("Ocurrio un error: ",e)
finally:
    conexion.close()