print("Vamos usar os operadores do python, na comparação de strings!")
p1 = str(input("Digite aqui sua Primeira palavra ou frase: "))
p2 = str(input("Digite aqui sua Segunda palavra ou frase: "))
maior = p1 > p2
menor = p1 < p2
igual = p1 == p2 
maior_igual = p1 >= p2
menor_igual = p1 <= p2
print(""" True ou False
A palavra {} é maior que a palavra {}? {}
A palavra {} é menor que a palavra {}? {}
A palavra {} é igual a palavra {}? {}
A palavra {} é maior ou igual a palavra {}? {}
A palavra {} é menor ou igual a palavra {}? {}
""".format(p1,p2,maior,p1,p2,menor,p1,p2,igual,p1,p2,maior_igual,p1,p2,menor_igual))