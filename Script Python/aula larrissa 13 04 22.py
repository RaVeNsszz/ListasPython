gambiarra = ""
for num in range(1,31):
    #print(num)
    gambiarra += str(num) + ", "
print(gambiarra+"30")

resultado = 0
for num in range(1,6):
    print(num)
#soma de int de 1 a 5    
resultado = 0
for num in range(1,6):
    resultado += num
    print(resultado)
print(resultado)    
#ler 10 num inteiros positivos e determine o maior deles
maior = 0
for i in range(10):
    num = int(inout("Digite um número positivo: "))

    if num > maior:
        maior = num
print(maior)
#faça um prog em py q some os numeros pares de 0 a 9
soma = 0
for num in range(0,9,2):
    print("num", num)
    soma+=num
    print("soma", soma)

print("soma final",soma)    
   #multiplicação
soma = 1
for num in range(0,9,2):
    print("num", num)
    soma*=num
    print("soma", soma)

print("soma final",soma)    
