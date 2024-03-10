lista1 = []
count = 15
while count != 0:
    num = int(input("Número: "))
    if num != len(lista1):
        count-=1
        lista1.append(num)
    else:
        print("O Número ",num," já foi adicionado a lista 1, informe outro.")

lista2 = []
count = 15
print("Incremente a segunda lista")
while count != 0:
    num = int(input("Número: "))
    if num != len(lista2):
        count-=1
        lista2.append(num)
        
    else:
        print("O Número",num," já foi adicionado a lista 2, informe outro.")
    

intersecao = []
for i in range(len(lista1)):
    num = lista1[i]
    for numer in lista2:
        if num == numer:
            intersecao.append(num)
print("Interseção =",intersecao)
