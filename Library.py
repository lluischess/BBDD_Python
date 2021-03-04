"""
 Python and PostgresSQL

"""
# 1. Instalar paquetes para trabajar con postgress y mysql
# 2. Conexion a Postgress


# -----------------------------------------------------------
# 1. Instalar paquetes para trabajar con postgress y mysql

# Primero actualizamos pip en cmd: python -m pip install --upgrade pip --no-warn-script-location
# Segundo instalamos el paquete postgress: pip install psycopg2
# Para arreglar el problema en visual code: python -m pip install psycopg2-binary
# O el de Mysql: pip install mysql-connector

# -----------------------------------------------------------
# 2. Conexion a Postgress

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
sql_select = "SELECT * FROM persona"

# Ejecutar sentencia
cursor_test_db.execute(sql_select)

# fetchall devuelve el resultado 
resultado = cursor_test_db.fetchall()
print(resultado)

# Cerrar conexion y cursor
cursor_test_db.close()
conexion_test_db.close()