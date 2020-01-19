from Controller.Conexao import *


class ListaParalizacao:
    def Listar(self):
        conn = Conexao()

        sql = '''select par_informacao, par_qtde_horas, par_mes, par_situacao from paralizacao '''
        conn.execute(sql)
        result = conn.fetch(sql)

        return result
