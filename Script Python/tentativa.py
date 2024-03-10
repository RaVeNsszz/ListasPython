prioritario = []
normal = []

pq = str(input("Adicionar a fila s/n: ")).upper()
while pq == "S":

    nome = str(input("Nome: ")).title
    pq2 = str(input("Têm prioridade s/n: ")).upper()
    pq = str(input("Adicionar mais um fila s/n: ")).upper()

    if pq2 == "S":
        prioritario.append(nome)

    else:
        normal.append(nome)

lista = []
for i in range(len(prioritario)):
    x = prioritario[i]
    lista.append(x)
    

    for j in range(len(normal)):
        x = normal[j]
        lista.append(x)
        

print(lista)
