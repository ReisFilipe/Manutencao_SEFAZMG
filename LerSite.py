import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from ConexaoDB import *

class ConsultaSefazMG:

    def Consulta(self):
        req = requests.get('http://www.sped.fazenda.mg.gov.br/spedmg/paralisacoes-programadas/')
        if req.status_code == 200:
            print('Requisição bem sucedida!')
            content = req.content


            conn = ConexaoDB()

            soup = BeautifulSoup(content, 'html.parser')
            table = soup.find(name='table')

            date = datetime.now()
            dDataAtual = date.strftime('%d/%m')

            table_str = str(table)
            df = (pd.read_html(table_str))[0]

            for x in range(1,len(df)):
                #print(df)
                cMes = df[0][x]
                cMensagem = df[1][x]
                cHoras = df[2][x]
                cSituacao = df[3][x]
  
                cInicio = cMensagem.find("dia")
                cData = cMensagem[cInicio+4:cInicio+10]

                sql = ("select * from paralizacao where par_informacao = '{0}' ").format(cMensagem)
                conn.execute(sql)

                result = conn.fetchone(sql)

                if result != None:
                    sql = ('''update paralizacao set par_situacao = '{0}', par_qtde_horas = '{1}', par_atualizacao = '{4}'  
                            where par_mes = '{2}' and par_informacao = '{3}' 
                            ''').format(cSituacao, cHoras, cMes, cMensagem, datetime.now())
                    conn.execute(sql)
                else:
                    sql = ('''INSERT INTO manutencao_sefaz.paralizacao
                            (par_informacao, par_qtde_horas, par_situacao, par_atualizacao, par_mes)
                            VALUES('{0}', '{1}', '{2}', '{3}', '{4}'); 
                            ''').format(cMensagem, cHoras, cSituacao, datetime.now(), cMes )
                    conn.execute(sql)

                if ((cSituacao != 'Cancelada') and (cSituacao != 'Agendada')):
                    sql = ('''update paralizacao set par_alerta = 'S'  
                            where par_mes = '{0}' and par_informacao = '{1}' 
                            ''').format( cMes, cMensagem)
                    conn.execute(sql)
        return 'Fim'

if __name__ == '__main__':
    mClass = ConsultaSefazMG()
    result = mClass.Consulta()
    print(result)