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
            sentencia='INSERT INTO Persona(nombre, apellido, email) VALUES(%s, %s, %s);'
            valores=(
                ('Pablo', 'Fernandez', 'pafer@mail.com'),
                ('Ramiro', 'Collane', 'raco@mail.com'),
                ('Elsa', 'Badazo', 'elba@mail.com'),
                ('Alan', 'Brito', 'alaB@mail.com'),
                ('Horacio', 'Nelmin', 'horanel@mail.com')
            )
            #INSERTAR MUCHOS executemany
            cursor.executemany(sentencia, valores)
            #Al usar WITH el COMMIT es automático
            registros_insertados = cursor.rowcount
            print("los registros insertados son: ", registros_insertados)
except Exception as e:
    print("Ocurrio un error: ",e)
finally:
    conexion.close()