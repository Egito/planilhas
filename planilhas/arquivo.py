import pandas as pd
from IPython.display import display


def anterior():
   # ler dados e gerar coluna de saldo anterior
   return 0

def entradas():
   # ler dados e gerar coluna de entradas
   return 0

def saidas():
   # ler dados e gerar coluna de saidas
   return 0

#wb = '2024_RO-57_4600672688 - Locacao ROTINA Ago24 Rev00.xlsx'
wb = "C:/Users/N0C3/Downloads/python-nb/planilhas/Petrobras - Historico de Radios DMR.xlsx"
#wb = "Petrobras - Historico de Radios DMR.xlsx"


df = pd.read_excel(wb, sheet_name=0)
# print(df)
# print(df.columns)
# df.dtypes
# df.size
df.info()
df
