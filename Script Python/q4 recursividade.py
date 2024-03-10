def concatenacao(frase):
    if len(frase) == 1:
        return frase[0]
    return frase[0] + concatenacao(frase[1:])

frase = ["Rayane","da","Silva","Rodrigues"]
print(concatenacao(frase))

