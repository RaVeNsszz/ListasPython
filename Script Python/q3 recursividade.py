def letra(string, count = 0):
    if len(string) == 0:
        return count
    if  string[0] in "Aa":
        count+=1
    return letra(string[1:],count)


string = str(input("Digite uma palavra: "))
print("A palavra: {} possue {} letras a.".format(string,letra(string,0)))