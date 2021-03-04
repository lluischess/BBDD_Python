"""
 Python and PostgresSQL

"""
# 1. Instalar paquetes para trabajar con postgress y mysql
# 2. Conexion a Postgress


# -----------------------------------------------------------
# 1. Instalar paquetes para trabajar con postgress y mysql

# Primero actualizamos pip en cmd: python -m pip install --upgrade pip --no-warn-script-location
# Segundo instalamos el paquete postgress: pip install psycopg2
# O el de Mysql: pip install mysql-connector

# -----------------------------------------------------------
# 2. Conexion a Postgress

import psycopg2  # paquete para la conexcion

psycopg2.connect(user="postgres",
                 password="admin",
                 host="127.0.0.1")
