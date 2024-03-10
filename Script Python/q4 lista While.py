count = 0
pares = 0
impares = 0
while count <= 9:
    num = int(input("Digite um número inteiro: "))
    if num > 0:
        count += 1
        if num % 2 == 0:
            pares += 1
        
        else:
            impares+=1
    else:
        print("Número inválido, tente novamente.")
        
print("Números Pares: ",pares)
print("Números Ímpares: ",impares)

