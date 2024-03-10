lista = []
count = 0
for i in range(0,15):
    
    lista.append(int(input("Digite um valor para posição {}: ".format(i+1))))
maior = 0
menor = 0
countmenor = 0
countmaior = 0
for i in range(len(lista)):

    if i == 0:
        maior = menor = lista[i]
        countmaior=i+1
        countmenor=i+1
    else:
        if lista[i] > maior:
            maior = lista[i]
            countmaior = i+1
            
        if lista[i] < menor:
            menor = lista[i]
            countmenor = i+1
    
print("Todos os numeros : ",lista)
print("Maior :",maior)
print("Menor :",menor)
print("Posição Maior :",countmaior)
print("Posição Menor :",countmenor)

