import configparser
import pymysql

class Conexao:

    def __init__(self):
        config =  configparser.ConfigParser()
        config.read("C:/Users/filip/Documents/Projetos/Manutencao_SEFAZMG/app/Controller/config/db.conf")
        self.host = config.get("MariaDB", "host")
        self.user = config.get("MariaDB", "user")
        self.password = config.get("MariaDB", "passwd")
        self.db = config.get("MariaDB", "db")

    def __connect__(self):
        try:
            self.con = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db, cursorclass=pymysql.cursors.
                                    DictCursor,autocommit=True)
            self.cur = self.con.cursor()
        except Exception as e:
            print('Erro favor entrar em contato com o suporte：{}'.format(e))

    def __disconnect__(self):
        self.con.close()

    def fetch(self, sql):
        self.__connect__()
        self.cur.execute(sql)
        result = self.cur.fetchall()
        self.__disconnect__()
        return result

    def fetchone(self, sql):
        self.__connect__()
        self.cur.execute(sql)
        result = self.cur.fetchone()
        self.__disconnect__()
        return result

    def execute(self, sql):
        self.__connect__()
        self.cur.execute(sql)
        self.__disconnect__()
