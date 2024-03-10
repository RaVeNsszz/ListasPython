#Cadastro de produtos

def verificar(codigo):

    for num in range(len(codigo)):
        if len(codigo) >= 6:
            print("Código validado")
            
        
        else:
            print("Código inválido!!!")
            codigo = str(input("Código do produto: "))
            return verificar(codigo)

def validacao(estoque):
    if estoque > 0:
        print("Estoque Mínimo está ok!")
    
    else: 
        print("Estoque zerado, reposição urgente!")
        


num = int(input("Informe a qtd de produtos a serem cadastrados: "))
matriz = []
for i in range (num):

    linha = []
    produto = str(input("Produto: "))
    linha.append(produto)

    codigo = str(input("Código do produto: "))
    verificar(codigo)
    linha.append(codigo)

    descricao = str(input("Descrição do produto: "))
    linha.append(descricao)

    estoque = int(input("Estoque mínimo: "))
    linha.append(estoque)
        
    pc = float(input("Preço Compra: "))
    linha.append(pc)

    pv = float(input("Preço Venda: "))
    linha.append(pv)
    for j in range(1):
        matriz.append(linha)

print(matriz)
