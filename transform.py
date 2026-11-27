import pandas as pd
from chamando_logging import logging

#Leitura CSV
df_multas_sujas = pd.read_csv("multas_transito_bronze_2.csv")

#Filtrando Colunas Validas e Invalidas
try:
    logging.info("Iniciando Etapa: Filtrando colunas  ")
    tratamento = (
    df_multas_sujas['id_multa'].isnull() |
    df_multas_sujas['id_multa'].duplicated() |
    df_multas_sujas['placa_veiculo'].isnull() |
    df_multas_sujas['tipo_veiculo'].isnull() |
    df_multas_sujas['cpf_proprietario'].isnull() |
    df_multas_sujas['cpf_proprietario'].duplicated() |
    df_multas_sujas['data_multa'].isnull() |
    df_multas_sujas['status_pagamento'].isnull() |
    df_multas_sujas['hora_multa'].isnull() |
    df_multas_sujas['motivo_multa'].isnull() |
    df_multas_sujas['valor_multa'].isnull() |
    df_multas_sujas['gravidade'].isnull() |
    df_multas_sujas['orgao_autuador'].isnull() |
    df_multas_sujas['estado'].isnull()      
    )


    #Variavel pra guardar DF valido & invalido
    df_multas_valido = df_multas_sujas[~tratamento]
    df_multas_invalido = df_multas_sujas[tratamento]
    logging.info("Etapa: Filtrando Colunas Concluída")
except Exception as error:
    logging.exception("Erro na etapa: Filtrando colunas válidas")
    raise

qtd_registros = len(df_multas_sujas)
qtd_df_validos = len(df_multas_valido)
qtd_df_invalidos = len(df_multas_invalido)

logging.info(f"Registros inicial: {qtd_registros}")
logging.info(f"Registros Válidos: {qtd_df_validos}")
logging.info(f"Registros Inválidos: {qtd_df_invalidos}")

#Criando Função Organização de formatos Etapa
def organizando_formatacao(df):
    df.columns = df.columns.str.lower().str.strip()
    colunas_formatar = ['modelo_veiculo','tipo_veiculo','status_pagamento','motivo_multa','gravidade','orgao_autuador']
    df['estado'] = df['estado'].str.upper().str.strip()
    for coluna in colunas_formatar:
        df[coluna] = df[coluna].str.lower().str.strip() 
    return df

#Criando Função Definindo Tipo da coluna


#Definindo Função Principal de Etapas
def proxima_etapa(etapa,funcao,*args):
    logging.info(f"Iniciando Etapa: {etapa}")

    try:
        resultado = funcao(*args)
        logging.info(f"Etapa: {etapa} Concluída!")
        return resultado

    except Exception as erro:
        logging.exception(f"Erro na etapa: {funcao} - {erro}")
        raise


#Declarando Parametros para funções
etapa_tratando_formatacao = proxima_etapa('Formatação de colunas',organizando_formatacao,df_multas_sujas)
print(df_multas_valido.info())
print(df_multas_valido.columns)

