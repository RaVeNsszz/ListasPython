#Exemplo 02
    
a = int(input("Imforme um numero inteiro positivo. Informe zero para parar: "))
maior = 0
while a != 0:#poderia usar o "AND", usar duas condições(n necessariamente so o and
    if a > maior:
        maior = a
    a = int(input("Imforme um numero inteiro positivo. Informe zero para parar: "))

print(maior)

#Exercicio 1
num = int(input("numero inteiro positivo. para parar numero negativo: "))
cont = 0 #contador
while num >= 0:  # ou not(num<0)
    if num >= 25 and num < 50:#25 <= num < 50 -> podia ser assi tbm # __se colocar o "OR" seria true se pelo menos uma for vrdd
        cont += 1

    num = int(input("numero inteiro positivo. para parar numero negativo: "))
#Exercicio 2

soma = 0
count = 0

n = int(input('Número. 0 para finalizar: '))

while n != 0:
	
    soma += n
    count += 1#toda vez q o codigo rodar vai contar +1
    n = int(input('Número. 0 para finalizar: '))

if (count==0):
    print("Média n pode ser calculada, pois n foi informada nenhum numero")
else:
    print("media: " soma/count)
	
#Exercicio 3
    ###
    
Entrada = idade e categoria
saida = valor do ingresso levando em consideração a idadde e categoria
outra entrada = se deseja continuar a compra

ler muuuitas vezes para interpretar bem

    ###    
    
    
    
    
    
       
        
   
