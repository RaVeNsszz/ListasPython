lista = []
for i in range (20):
    lista.append(int(input("Digite um valor inteiro: ")))
print("Lista =",lista)
pares = []
impares = []
for num in lista:
    if num % 2 == 0:
        pares.append(num)
    
    else:
        impares.append(num)

print("Pares =",pares)
print("Ímpares =",impares)

