import sqlite3

conn = sqlite3.connect("dbmercado.db")

while True:
    vcpf = input("CPF: ")
    vnome = input("Nome: ")
    vlogin = input("Login: ")
    vsenha = input("Senha: ")

    conn.execute(
        "INSERT INTO usuario(cpf, nome, login, senha) VALUES (?, ?, ?, ?);",
        (vcpf, vnome, vlogin, vsenha)
    )
    conn.commit()

    print("Usuário cadastrado!")

    continua = input("Digite N para encerrar: ")

    if continua.upper() == "N":
        break

conn.close()
quit()