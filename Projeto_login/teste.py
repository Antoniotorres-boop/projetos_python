import sqlite3

# Isso cria um arquivo de banco de dados na sua pasta
conexao = sqlite3.connect('usuarios.db')
print("Banco de dados criado com sucesso no Windows!")
conexao.close()