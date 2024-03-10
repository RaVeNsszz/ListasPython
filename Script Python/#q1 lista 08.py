# lista 08

#1 Implemente a função recursiva que recebe uma posição e retorna o valor
#fibonacci daquela posição (ex.: Fib(1)=1, Fib(2)=1, Fib(3)=2). Crie um
#programa que use essa função.

#fib(n) = fib(n-1_+fib(n-2)
#casos base: fib(0)=0 e fib(1)=1
#solução de cleb
def fib(n):
    if n > 1:
        return fib(n-1) + fib(n-2)
    return n

x = int(input("Digite um valor: "))

for i in range(x):
    print(fib(i))


#resolução da professora da solução de Clebson
#n =3 
#1° chamada =  fib(3)
#   fib(n-1)+fib(n-2)--> fib(2) + fib(1)
#2° chamada = fib(2) = 1
#   fib(1) + fib(0)  --> 1+0
#3° chamada = fib(1) -- retorna 1
#4° chamada = fib(0) -- retorna 0
#5° chamada = fib(1) -- retorna 1

#q2
#Implemente uma função recursiva que receba uma string e diga quantas
#letras ele tem. Crie um programa que use essa função.
def LetrasRec(frase):
    frase = ''.join(frase.strip().split()) #t Tirando os espaços e quebrando
    if frase == '':
        return 0
    else:
        return 1 + LetrasRec(frase[1:])


print(LetrasRec('   f l a v i n  '))

#explicação
# casa --> tam(str casa)=1+tam(str asa)
# 1° chamada --- "casa"
#   1 + LetrasRec(asa)   -- 1 + 3 = 4
#2° chamada ---"asa"
#   1 + LetrasRec("sa") -- 1 + 2 = 3
#3° chamada --- "a"
#   1 + LetrasRec("") == 
#TIREI PRINT


#3) Escreva uma função recursiva que recebe uma string e conta quantos “A”
#aparece nele. Crie o programa que chame a função e mostre a resposta.

def aaa(b):

    if b == " ":
        return 0

    else:
        x = b[0]
        if x == "a" or x == "A":
            return 1 + (aaa(b[1:]))

        else:
            return (aaa(b[1:]))


palavra =str(input("Digite uma palavra: "))

print (aaa(palavra))
