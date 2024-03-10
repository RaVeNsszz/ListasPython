def aaa(b):

    if b == " ":
        return 0

    else:
        x = b[0]
        if x == "a" or x == "A":
            return 1 + (aaa(b[1:]))

        else:

            return (aaa(b[1:]))


palavra = str(input("Digite uma palavra: "))
print(aaa(palavra))