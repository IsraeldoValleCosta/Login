# Controle de acesso v02
# Conexão com banco de dados
import sqlite3
import time
conn = sqlite3.connect("dbmercado.db")
#Entrada de Dados
vcpf = input("CPF:")
vnome =input("Nome:")   
vlogin = input("Login: ")
vsenha = input("Senha: ")
# Enviar instrução sql para ser executada
conn.execute("insert into usuario(cpf,nome,login,senha) values(?,?,?,?);", (vcpf, vnome, vlogin, vsenha))
conn.commit()
#Encerrar conexão
conn.close()
quit()