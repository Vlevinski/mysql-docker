from database import DBHelper
from sql import customer

config ={
    "host":"0.0.0.0",
    "user":"root",
    "password":"root",
    "database":"notes"
}

db = DBHelper(**config)

qrt = db.fetch("SELECT version();")
[print(item) for item in qrt]

qrt = db.fetch("SHOW DATABASES;")
[print(item) for item in qrt]

qrt = db.fetch("SHOW TABLES;")
[print(item) for item in qrt]

qrt = db.fetch("SELECT * FROM user;")
[print(item) for item in qrt]




