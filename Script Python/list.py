lista = []
lista2 = []
qtd = int(input("Total de clientes: "))

for i in range(qtd):
    lista.append(str(input("Nome do cliente: ")))
maior = 0
menor = 0
for j in range(len(lista)):
    if lista[j] > lista[j]:
        maior = lista[j]
        lista2.insert(maior)

print(lista2)    
   
    
        
    

    
    
