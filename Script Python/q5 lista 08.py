def LetrasRec(palavra):
    palavra = ''.join(palavra.strip().split()).upper() #t Tirando os espaços e quebrando
    if palavra == '':
        return palavra
    else:
        return LetrasRec(palavra[1:])


palavra = str(input("Digite algo: "))
print(LetrasRec(palavra))