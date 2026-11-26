import pandas as pd
from chamando_logging import logging

df_multas_sujas = pd.read_csv("multas_transito_bronze_2.csv")

print(df_multas_sujas)