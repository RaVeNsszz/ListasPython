#Faça um programa que leia 5 números e informe a soma e a média a cada número lido.
media = 0
num = 0
for num in range(5):
    media+=1
    num = int(input("Num: "))
    num+=num
    num/=media
    
    print("Média: ",media)
print("Soma: ",num)