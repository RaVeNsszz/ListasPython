#Cadastro de Clientes
def verificacao(n):
    nome = n.split()
    print(len(nome))
    if len(nome) >= 2:
        lista.append(nome[0]+" "+nome[1])
        
    
    else: 
        print("Nome Inválido")
        n = input("Nome: ")
        return verificacao(n)
    

def verificar(email):
    if "@" not in email:
        print("Email inválido")
        email = input("E-mail: ")
        return verificar(email)  

    else:
        print("Email válido")
        lista.append(email)
        
matriz = []
controle = 1

while controle != 0:
    lista = []
    n = input("Nome: ").strip()
    verificacao(n)

    email = input("E-mail: ")
    verificar(email)
    numero = int(input("Total de Compras Realizadas: "))
    lista.append(numero)
    
    cash = float(input("CashBack acumulado: "))
    lista.append(cash)
    matriz.append(lista)
    controle = int(input("Deseja Continuar Sim(1) ou Nâo(0): "))

print(matriz)
