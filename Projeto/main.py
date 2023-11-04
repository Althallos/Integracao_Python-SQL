import pyodbc
import pandas as pd

dados_conexao = ("Driver={SQL Server};"
                 "Server=DESKTOP-B9JBA2I;"
                 "Database=ContosoRetailDW;")

conexao = pyodbc.connect(dados_conexao)
print('Conexão-Bem-Sucedida')

#   Tabela com as vendas dbo.FactSales
vendas_df = pd.read_sql("SELECT * FROM ContosoRetailDW.dbo.FactSales", conexao)

#       Calcular o lucro diário da empresa
#   Lucro ->  SalesAmount - TotalCost - DiscountAmount
vendas_df["Lucro"] = vendas_df["SalesAmount"] - vendas_df["TotalCost"] - vendas_df["DiscountAmount"]

#   Pode ter mais de 1 transação por dia na tabela, então uma opção é usar o método groupby do pandas
vendas_diarias_df = vendas_df.groupby(["DateKey"]).sum(numeric_only=True)   #   Tirando valores repetidos e somando linhas
print(vendas_diarias_df)

#   Plotar um gráfico do lucro diário
import matplotlib
import matplotlib.pyplot as plt

grafico = vendas_diarias_df["Lucro"].plot(figsize=(15, 5))
grafico.yaxis.set_major_formatter(matplotlib.ticker.StrMethodFormatter('${x:,.0f}'))
plt.show()
