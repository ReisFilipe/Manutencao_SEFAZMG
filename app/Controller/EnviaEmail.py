import smtplib
from email.mime.text import MIMEText
import configparser
from Conexao import *
import json
import os


class EnviaEmail:

    def __init__(self):
        config =  configparser.ConfigParser()
        curdir = os.path.dirname(os.path.realpath(__file__))+'\config'
        conf = "\db.conf"

        config.read(curdir+conf)
        self.smtp_ssl_host = config.get("E-mail", "smtp")
        self.smtp_ssl_port = config.get("E-mail", "port") 
        self.username = config.get("E-mail", "username") 
        self.password = config.get("E-mail", "passwd") 

    def EnvioEmail(self):

        cDados = self.BuscaDados()

        for row in cDados:
            par_informacao = row['par_informacao']
            par_qtde_horas = row['par_qtde_horas']
            par_situacao = row['par_situacao']
            par_mes = row['par_mes']
            

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
        conn = Conexao()

        sql = '''select * from paralizacao limit 1 '''
        conn.execute(sql)
        result = conn.fetch(sql)

        return result
# Retirar depois de finalizar 
if __name__ == '__main__':
    '''
    mClass = EnviaEmail()
    result = mClass.BuscaDados()
    print(result)
    '''
config =  configparser.ConfigParser()
curdir = os.path.dirname(os.path.realpath(__file__))+'\config'
conf = "\db.conf"
