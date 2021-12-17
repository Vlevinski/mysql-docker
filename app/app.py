from getpass import getpass
from mysql.connector import connect, Error

# settings
host = "0.0.0.0"

try:
    with connect(host,
                 user=input("Enter username: "),
                 password=getpass("Enter password: "),
                 ) as connection:
        print(connection)
except Error as e:
    print(e)
