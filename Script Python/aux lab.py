def verificar(email):
    if "@" not in email:
        print("Email inválido")
        
    else:
        print("Email válido")
        

nomes = []
controle = 1

while controle != 0:
    nomes.append(str(input("Nome: ")))
    controle = int(input("Continuar Sim(1) ou Nâo(0): "))

matriz = []
for linha in range(len(nomes)):
    print(linha)
    linha = []
    for coluna in range(len(nomes)): 
        print(coluna)  
        email =str(input("E-mail: "))
        verificar(email)
        
        linha.append(int(input("Número de Compras Realizadas: ")))
        linha.append(float(input("CashBack acumulado: ")))

    matriz.append(linha)       

print(matriz)
