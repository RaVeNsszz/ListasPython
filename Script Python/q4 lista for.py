qtd = int(input("Quantidade de pessoas: ")) # 1

soma = 0 #1
menoralt = 2 #1
count = 0 #1
pessoa = "" #1
for i in range(qtd): #n
    nome = str(input("Nome: "))
    alt = float(input("Altura: "))

    soma+=alt


    if alt > 1.85:
        count+=1
    
    if menoralt > alt :
        menoralt = alt
        pessoa  = nome
        
    else: 
        menoralt = alt

print("{} tem {}, potanto a menor pessoa no grupo.".format(pessoa,menoralt))
media = soma/qtd
print("Média do conjunto de alturas é: ",media)
print("Tem {} pessoa(s) acima de 1.85 no grupo".format(count))


 
