import configparser
import pymysql

class ConexaoDB:

    def Conexao(self):
        config =  configparser.ConfigParser()
        config.read("C:/Users/Filipe/Documents/Projetos/Manutencao_sefaz/config/db.conf")

        try:
            conn = pymysql.connect(host=config.get("MariaDB", "host"), 
                                    db=config.get("MariaDB", "db"),
                                    user=config.get("MariaDB", "user"), 
                                    passwd=config.get("MariaDB", "passwd"))
            
        except Exception as e:
            print('Erro favor entrar em contato com o suporte：{}'.format(e))

        return conn