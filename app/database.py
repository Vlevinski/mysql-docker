import pymysql


class DBHelper:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.cur = None
        self.con = None

    def __connect__(self):
        try:
            self.con = pymysql.connect(host=self.host,
                                       user=self.user,
                                       password=self.password,
                                       db=self.database,
                                       cursorclass=pymysql.cursors.DictCursor)
        except Exception as err:
            print("Error: ", err)
            exit(1)
        self.cur = self.con.cursor()

    def __disconnect__(self):
        self.con.close()

    def fetch(self, sql):
        self.__connect__()
        print("\n--> ", sql)
        try:
            self.cur.execute(sql)
        except Exception as err:
            print("Error: ", err)
            exit(1)
        result = self.cur.fetchall()
        self.__disconnect__()
        return result

    def execute(self, sql):
        self.__connect__()
        try:
            self.cur.execute(sql)
        except Exception as err:
            print("Error: ", err)
            exit(1)
        self.__disconnect__()

