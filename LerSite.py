import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime

class ConsultaSefazMG:

    def Consulta(self):
        req = requests.get('http://www.sped.fazenda.mg.gov.br/spedmg/paralisacoes-programadas/')
        if req.status_code == 200:
            print('Requisição bem sucedida!')
            content = req.content

        soup = BeautifulSoup(content, 'html.parser')
        table = soup.find(name='table')

        data_e_hora_atuais = datetime.now()
        dDataAtual = data_e_hora_atuais.strftime('%d/%m')

        table_str = str(table)
        df = (pd.read_html(table_str))[0]

        for x in range(1,len(df)):
            cMensagem = df[0][x]
            cHoras = df[1][x]
            cSituacao = df[2][x]
            
            #print('---------------------------      ------------------------')
            #print(cMensagem)
            #print(cHoras)
            print(cSituacao)
            cInicio = cMensagem.find("dia")
            cData = cMensagem[cInicio+4:cInicio+10]
            #print(cData)

            if cData[3:5] == dDataAtual[3:5]: # and cSituacao == 'Agendada':
                cAlerta = 'Paralização programada '+cMensagem +' com duração de '+ cHoras
                #print(cAlerta)

        return cAlerta

if __name__ == '__main__':
    mClass = ConsultaSefazMG()
    cResult = mClass.Consulta()
    print(cResult)