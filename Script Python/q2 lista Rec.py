def funRec(nome):
    
    for i in range(len(nome)):
        count = 0
        if i == "a" or i == "A":
            count+=1
        else:
            return funRec(nome)
    print(count)

nome = input("Digite algo: ").upper()
funRec(nome)

def aaa(b):

    if b == " ":
        return 0

    else:
        x = b[0]
        if x == "a" or x == "A":
            return 1 + (aaa(b[1:]))

        else:

            return (aaa(b[1:]))

palavra = "abababaa"

print (aaa(palavra))