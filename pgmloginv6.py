# Controle de acesso v02
# Conexão com banco de dados
import sqlite3
from hashlib import sha256
conn = sqlite3.connect("dbmercado.db")

#Entrada de Dados
vcpf = input("CPF:")
vnome =input("Nome:")   
vlogin = input("Login: ")
vsenha = input("Senha: ")
senha_hash = sha256(vsenha.encode("utf-8")).hexdigest()
# Enviar instrução sql para ser executada
conn.execute("insert into usuario(cpf,nome,login,senha) values(?,?,?,?);", (vcpf, vnome, vlogin, vsenha))
conn.commit()
#Encerrar conexão
conn.close()
quit()