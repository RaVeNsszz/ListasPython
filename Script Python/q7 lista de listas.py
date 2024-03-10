parametro = 0
while parametro != 1:
    p = str(input("Digite algo: ")) 
    if len(p) >= 4:
        parametro = 1
    else:

        print("Número mínimo de caracteres não atingido!")
meio = len(p)//2
pmetade =""
smetade = ""
for i in range(0,meio):
    pmetade = pmetade + p[i]
for i in range(meio,len(p)):
    smetade = smetade + p[i]
print("Primeira metade: ",pmetade)
print("Segunda metade: ",smetade)
print("Segunda metade antes da primeira metade: ",p[meio:]+p[:meio])
vogais = ""
consoantes = ""
for i in range(len(p)):
    if p[i] == "a" or p[i] == "e" or p[i] == "i" or p[i] == "o" or p[i] == "u":
        vogais= vogais + p[i]   
    else :
        consoantes = consoantes + p[i]
print("Vogais antes das consoantes: ",vogais+consoantes)
inversa = ""
for i in range(len(p)-1,-1,-1):
    inversa = inversa + p[i]
print("Invertida: ",inversa)
zigzag = ""
for i in range(meio):
    zigzag = zigzag + pmetade[i] + smetade[i]
print("Metades Intecaladas: ",zigzag)


