from getpass import getpass
from mysql.connector import connect, Error

# settings
host = "0.0.0.0"
port = 3306

try:
    with connect(host=host,
                 port=port,
                 user=input("Enter username: "),
                 password=getpass("Enter password: "),
                 ) as connection:
        print("Connector --> ", connection)
except Error as e:
    print(e)
