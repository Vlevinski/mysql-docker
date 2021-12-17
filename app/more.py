import pymysql.cursors
import mysql.connector
from mysql.connector import errorcode
import sys

config = {
    'user': 'root',
    'password': 'root',
    'host': '0.0.0.0',
    'database': 'notes',
    'raise_on_warnings': True}


def dbs(sql):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    try:
        cursor.execute(sql)
    except Exception as err:
        sys.exit(err)
    resp = [i for i in cursor]
    cnx.close()
    return resp


dbase = dbs("show databases;")
print(dbase)

ver = dbs("select version();")
print(ver)
