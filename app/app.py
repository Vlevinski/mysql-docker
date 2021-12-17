from mysql.connector import connect, Error
import sys

# settings
host = "0.0.0.0"
port = 3306
database = "online_movie_rating"
user = "root"
password = "root"


def conn():
    return connect(host=host,
                   port=port,
                   user=user,
                   password=password, )


def conn_db(data_base):
    return connect(host=host,
                   port=port,
                   user=user,
                   password=password,
                   database=data_base, )


# connection
def open_connect():
    try:
        connection = conn()
    except Error as e:
        sys.exit(e)
    return connection


def create_db():
    try:
        connection = conn()
        create_db_query = "CREATE DATABASE online_movie_rating"
        cursor = connection.cursor()
        cursor.execute(create_db_query)
    except Error as e:
        sys.exit(e)


def execute_db(qrs, data_base):
    try:
        connection = conn_db(data_base)
        create_db_query = qrs
        cursor = connection.cursor()
        cursor.execute(create_db_query)
        [print(item) for item in cursor]
    except Error as e:
        sys.exit(e)


# show db query
def show_db():
    try:
        connection = conn()
        show_db_query = "SHOW DATABASES;"
        cursor = connection.cursor()
        cursor.execute(show_db_query)
        [print(item) for item in cursor]
    except Error as e:
        sys.exit(e)


def select_db(data_base):
    try:
        connection = conn_db(data_base)
        print(connection)
    except Error as e:
        sys.exit(e)


print("Databases: ")
show_db()

print("\nUser rows: ")
db = "notes"
query = "SELECT * from user;"
execute_db(query, db)

print("\nMySQL version: ")
query = "SELECT version();"
execute_db(query, db)
