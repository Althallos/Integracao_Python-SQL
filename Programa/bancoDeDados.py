import pyodbc

#       Fazendo a conexão

#   Se estiver usando outro sistema de banco de dados, o driver mudaria. Para saber em outros casos, execute:
#pyodbc.drivers()   ->  Caso não encontre seu driver ali, basta pesquisar por "driver MeuBancoDeDados for pyodbc" e baixar

dados_conexao = ("Driver={SQL Server};"
                 "Server=SeuServidor;"      #Para pegar o nome do seu servidor colocar no CMD(Prompt de comando): hostname
                 "Database=ContosoRetailDW;")       #Nome da Base de Dados

conexao = pyodbc.connect(dados_conexao)
print('Conexão-Bem-Sucedida')

#   Caso Precisasse de Login e Senha:
#dados_conexão = ("Driver={SQL Server};"
#                 "Server=SeuServidor;"
#                 "Database=NomeBaseDeDados;"
#                 "UID=LOGIN";
#                 "PWD=Senha")

#   Criando o que o pyodbc chama de Cursor (Quem irá executar os códigos SQL)
cursor = conexao.cursor()

#   Opção 1: Apenas executar um comando no banco de dados
#cursor.execute("SELECT * FROM BaseDeDados.Tabela")
#   Caso a operação não seja para criar uma consulta e sim um UPDATE, DELETE ou CREATE, você precisará fazer um commit 
#   da sua operação no banco de dados para implementar (Não aconselhável se você não tem certeza que pode fazer isso)
#conexao.commit()


import pandas as pd

produtos_df = pd.read_sql("SELECT * FROM ContosoRetailDW.dbo.DimProduct", conexao)
print(produtos_df)