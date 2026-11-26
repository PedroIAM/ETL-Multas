from chamando_logging  import logging
import pandas as pd

nome_arquivo = "multas_transito_bronze.csv"
logging.info("Iniciando Pipeline")


try:
    logging.info("Iniciando Etapa: Leitura CSV - Bronze")
    df_multas = pd.read_csv(nome_arquivo, sep=";", dtype=str, encoding="utf-8")
    df_multas.to_csv("multas_transito_bronze_2.csv")
    logging.info("Etapa Leitura CSV Finalizada com Sucesso!")
except Exception as error:
    logging.exception(f"Erro na leitura do CSV - {error}")
    raise