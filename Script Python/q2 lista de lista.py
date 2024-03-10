lista = []
for i in range(10):
    lista.append(int(input("Informe números aleatórios: ")))

for num in lista:

    x = lista.pop(0)
    lista.append(x)
    
    print(lista)
    

