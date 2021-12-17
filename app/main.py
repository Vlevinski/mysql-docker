import pymysql.cursors

# Connect 
con = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='notes',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)


def new_table():
    sql = """CREATE TABLE `users` ( 
                `id` int(11) NOT NULL AUTO_INCREMENT, 
                `email` varchar(255) COLLATE utf8_bin NOT NULL,
                `password` varchar(255) COLLATE utf8_bin NOT NULL,
                PRIMARY KEY (`id`)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
                AUTO_INCREMENT=1 ;"""
    cur = con.cursor()
    cur.execute(sql)
    return [i for i in cur]


def all_tables():
    sql = "SHOW tables;"
    cur = con.cursor()
    cur.execute(sql)
    return [i for i in cur]


def insert_one():
    sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
    cur = con.cursor()
    cur.execute(sql)
    con.commit()


def read_one():
    sql = "SELECT * FROM `user`;"
    cur = con.cursor()
    cur.execute(sql)
    return cur.fetchone()


def read_many():
    sql = "SELECT * FROM `user`;"
    cur = con.cursor()
    cur.execute(sql)
    return cur.fetchall()


print(all_tables())
