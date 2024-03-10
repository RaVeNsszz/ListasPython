def LetrasRec(frase):
    frase = ''.join(frase.strip().split()) #t Tirando os espaços e quebrando
    if frase == '':
        return 0
    else:
        return 1 + LetrasRec(frase[1:])

frase = str(input("Digite algo: "))
print(LetrasRec(frase))