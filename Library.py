"""
 Python and PostgresSQL

"""
# 1. Instalar paquetes para trabajar con postgress y mysql
# 2. Conexion a Postgress y Select
# 3. Insert
# 4. Update
# 5. Delete


# -----------------------------------------------------------
# 1. Instalar paquetes para trabajar con postgress y mysql

# Primero actualizamos pip en cmd: python -m pip install --upgrade pip --no-warn-script-location
# Segundo instalamos el paquete postgress: pip install psycopg2
# Para arreglar el problema en visual code: python -m pip install psycopg2-binary
# O el de Mysql: pip install mysql-connector

# -----------------------------------------------------------
# 2. Conexion a Postgress y Select

import psycopg2  # paquete para la conexcion

# Assignamos la conexion de la BBDD a una variable
conexion_test_db = psycopg2.connect(user="postgres",
                 password="admin",
                 host="127.0.0.1",
                 port="5432",
                 database="test_db")

# Un cursor nos permite ejecutar sentencia en la bbdd
cursor_test_db = conexion_test_db.cursor()

# Asignamos sentencia SQL a una variable
#sql_select = "SELECT * FROM persona WHERE id_persona = %s" 1 valor
sql_select = "SELECT * FROM persona WHERE id_persona IN %s" # varios valores

entrada = input("Proporciona las Ids: (separado por comas)")
tupla = tuple(entrada.split(","))
#id_persona = input("Añade el Id de la persona:")
tupla_ids = ((tupla),) #tupla de tuplas
#llave_primeria = (id_persona,)#tuppla

# Ejecutar sentenc1ia
cursor_test_db.execute(sql_select,tupla_ids) # segundo parametro de sustitución de la id_persona

# fetchall devuelve el resultado 
resultado = cursor_test_db.fetchall() #devuelve todos los registros
for resul in resultado:
    print(resul)

# fetchone devuelve 1 registro
#resultado2 = cursor_test_db.fetchone()
#print(resultado2)

# Cerrar conexion y cursor
#cursor_test_db.close()
#conexion_test_db.close()

#--------------------------------------------------------------------------------
# 3. Insert

sql_insert = "INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)" # %s comodin

valores = (
    ("Marcos","mendez","lol3@lol.com"),
    ("Maria","mendez","lol2@lol.com"),
    ("Marta","mendez","lol1@lol.com")
    ) #tupla

#cursor_test_db.execute(sql_insert,valores) para insertar 1 registro

# Para insertar varios registros a la vez
#cursor_test_db.executemany(sql_insert,valores)

# Guardar informacion en la BBDD
#conexion_test_db.commit() # hasta que no se ejecute el commit no se guarda la información

#resultado = cursor_test_db.rowcount
#print(f"Registros insertados: {resultado}")

# Cerrar conexion y cursors
#cursor_test_db.close()
#conexion_test_db.close()

#--------------------------------------------------------------------------------
# 4. Update

sql_update = "UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s"

#donde = input("Que id modificamos? ")

#valores = (
#    ("Juan","Perez","jperez@gmail.com",input("Que id modificamos? ")),
#    ("Juan2","Perez","jperez@gmail.com",input("Que id modificamos? ")),
#    ("Juan3","Perez","jperez@gmail.com",input("Que id modificamos? "))
#    )

#cursor_test_db.execute(sql_update,valores)
#cursor_test_db.executemany(sql_update,valores)
#conexion_test_db.commit()
#resultado = cursor_test_db.rowcount
#print(f"Registros actualizados: {resultado}")
# Cerrar conexion y cursors
#cursor_test_db.close()
#conexion_test_db.close()

#--------------------------------------------------------------------------------
# 5. Delete

sql_delete = "DELETE FROM persona WHERE id_persona = %s" 

valores = (input("Que id Eliminamos? "),)

cursor_test_db.execute(sql_delete,valores)
#cursor_test_db.executemany(sql_update,valores)
conexion_test_db.commit()
resultado = cursor_test_db.rowcount
print(f"Registros Eliminados: {resultado}")
# Cerrar
# Cerrar conexion y cursors
cursor_test_db.close()
conexion_test_db.close()