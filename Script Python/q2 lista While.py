var = 1
nome = str(input("Nome: "))
senha = str(input("Senha: "))

while var != 0:

    if nome != senha: 
        print("Cadastro Finalizado com sucesso.")
        var = 0
    
    else:
        print("Inválido")
        nome = str(input("Nome: "))
        senha = str(input("Senha: "))

