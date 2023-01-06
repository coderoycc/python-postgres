import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='carljr107',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)

try:
    with conexion:
        with conexion.cursor() as cursor: #Este bloque cierra el cursor
            sentencia='SELECT id_persona, nombre FROM persona where id_persona = %s'
            #%s es un parametro posicional
            parametro = 1
            #En el execute pasamos como una tupla por el id_persona %s
            cursor.execute(sentencia,(parametro,) )
            #registros = cursor.fetchall() #Obtiene todos los registros
            registros = cursor.fetchone()
            #recupera todos los registros una fila es una tupla y estan en una lista
            print(registros)
except Exception as e:
    print("Ocurrio un error: ",e)
finally:
    conexion.close()
