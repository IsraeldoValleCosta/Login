# Controle de acesso v02
# Conexão com banco de dados
import sqlite3
import time

conn = sqlite3.connect("dbmercado.db")

# Mecanismo para enviar instrução SELECT para ser executada
cursor = conn.cursor()

tentativas = 0

while tentativas < 3:

    vlogin = input("Login: ")
    vsenha = input("Senha: ")

    # Verifica se login e senha foram preenchidos
    if vlogin and vsenha:

        sql = "Select count(*) from usuario where login = "
        sql = sql + '"' + vlogin + '"'
        sql = sql + " and senha = " + '"' + vsenha + '"'

        # Enviar comando SQL para ser executado
        cursor.execute(sql)

        # Receber conjunto de dados
        dados = cursor.fetchone()

        if dados[0] > 0:
            print("Acesso permitido!")
            break

        else:
            tentativas = tentativas + 1
            print("Login ou senha incorretos!")
            print("Tentativas restantes:", 3 - tentativas)

            if tentativas == 2:
                print("Ultima Tentativa!!!!!")
                
if tentativas == 3:
    print("Você excedeu o número de tentativas")


# Encerrar conexão
time.sleep(5)
conn.close()
quit()






