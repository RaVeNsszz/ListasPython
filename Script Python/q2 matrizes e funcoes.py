matriz = []
maior = 0
for i in range(4):
    matriz.append([])
    for j in range(4):
        matriz[i].append(int(input("Digite valores inteiros: ")))
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i != j:
            maior = matriz[i][j]
            if maior < matriz[i][j]:
                maior = matriz[i][j]
print(maior)
                
            
        
