import pandas as pd
from chamando_logging import logging

#Leitura CSV
df_multas_sujas = pd.read_csv("multas_transito_bronze_2.csv")

#Criando Função Etapa
def organizando_formatacao(df):
    df.columns = df.columns.str.lower().str.strip()
    colunas_formatar = ['modelo_veiculo','tipo_veiculo','status_pagamento','motivo_multa','gravidade','orgao_autuador']
    df['estado'] = df['estado'].str.upper().str.strip()
    for coluna in colunas_formatar:
        df[coluna] = df[coluna].str.lower().str.strip() 
    return df



def proxima_etapa(etapa,funcao,*args):
    logging.info(f"Iniciando Etapa: {etapa}")

    try:
        resultado = funcao(*args)
        logging.info(f"Etapa: {etapa} Concluída!")
        return resultado

    except Exception as erro:
        logging.exception(f"Erro na etapa: {funcao} - {erro}")
        raise




etapa_tratando_formatacao = proxima_etapa('Formatação de colunas',organizando_formatacao,df_multas_sujas)
print(df_multas_sujas)