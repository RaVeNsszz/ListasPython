def string(palavra,count):
    if len(palavra) == 0:
        return count
    return string(palavra[1:],count+1)


p = str(input("Digite um nome: "))
print("Essa palavra têm {} letras.".format(string(p,0)))