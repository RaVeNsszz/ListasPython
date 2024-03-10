def soma(string):
    if len(string)==1:
        return string [0]
    
    return int(string[0]) + int(soma (string[1:]))


string = input("Informe um valor positivo: ")
print(soma(string))
