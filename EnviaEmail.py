import smtplib
from email.mime.text import MIMEText
import configparser
from ConexaoDB import *

class EnviaEmail:

    def __init__(self):
        config =  configparser.ConfigParser()
        config.read("C:/Users/Filipe/Documents/Projetos/Manutencao_sefaz/config/db.conf")
        self.smtp_ssl_host = config.get("E-mail", "smtp")
        self.smtp_ssl_port = config.get("E-mail", "port") 
        self.username = config.get("E-mail", "username") 
        self.password = config.get("E-mail", "passwd") 

    def EnvioEmail(self):

        from_addr = self.username
        to_addrs = ['destiny@gmail.com']

        # a biblioteca email possuí vários templates
        # para diferentes formatos de mensagem
        # neste caso usaremos MIMEText para enviar
        # somente texto
        message = MIMEText('Hello World')
        message['subject'] = 'Hello'
        message['from'] = from_addr
        message['to'] = ', '.join(to_addrs)

        # conectaremos de forma segura usando SSL
        server = smtplib.SMTP_SSL(self.smtp_ssl_host, self.smtp_ssl_port)
        # para interagir com um servidor externo precisaremos
        # fazer login nele
        server.login(self.username, self.password)
        server.sendmail(from_addr, to_addrs, message.as_string())
        server.quit()

    def BuscaDados(self):
        conn = ConexaoDB()

        sql = '''select * from paralizacao '''
        conn.execute(sql)

        result = conn.fetch(sql)
        #print(result)
        return result
# Retirar depois de finalizar 
if __name__ == '__main__':
    mClass = EnviaEmail()
    result = mClass.BuscaDados()
    print(result)