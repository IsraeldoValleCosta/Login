# Controle de acesso v02
# Conexão com banco de dados
import sqlite3
import time
conn = sqlite3.connect("dbmercado.db")
# Mecanismo para enviar instrução SELECT para ser executada
cursor = conn.cursor()   
vlogin = input("Login: ")
vsenha = input("Senha: ")
sql = "Select count(*) from usuario where login = "
sql = sql +  '"' + vlogin + '"'
sql = sql + " and senha = "  + '"' + vsenha + '"'
#Enviar comando sql para ser executado
cursor.execute(sql)
# receber conjunto de dados
dados = cursor.fetchone()
if dados[0] > 0:
    print("Acesso permitido!")
else:
    print("Acesso negado!")
#encerrar conexão
time.sleep(5)
conn.close()
quit()

