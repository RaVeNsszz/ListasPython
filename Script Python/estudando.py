def inversa(p):
    inversa = ""
    for i in range(len(p)-1,-1,-1):
        inversa = inversa + p[i]
    return inversa

def pmetade(p):
    pmetade = ""
    for i in range(0,len(p)//2):
        pmetade = pmetade + p[i]
    return pmetade

def smetade(p): #ta bugadinho
    smetade = ""
    num = len(p)//2
    for i in range(num,len(p)):
        smetade = smetade + p[i]
        return smetade

def ultimaprimeira(p):
    return smetade(p) + pmetade(p)


def vogais_consoantes(p):
    vogais = ""
    consoantes = ""
    for i in range(len(p)):
        if p[i]== "a" or p[i]=="e"or p[i]=="i"or p[i]=="o"or p[i]=="u":
            vogais = vogais + p[i]
        
        else:
            consoantes = consoantes + p[i]
    return vogais + consoantes

def intercaladas(p,pm,sm): # não deu certo, deve ser por  causa da primeira metade q ta errada 
    intercaladas = ""
    for i in range(len(p)//2):
        intercaladas = intercaladas + pm[i] + sm[i]
    return intercaladas 


palavra = "banana"
resp1 = inversa(palavra)
resp2 = pmetade(palavra)
resp3 = smetade(palavra)
resp4 = ultimaprimeira(palavra)
resp5 = vogais_consoantes(palavra)
#resp6 = intercaladas(palavra,resp2,resp3)
print(resp1,resp2,resp3,resp4,resp5)