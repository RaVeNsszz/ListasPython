original = []
for i in range (5): 
    original.append(str(input("Livros da estante: ")))

fav = str(input("Favorito: "))
parametro = 1
while parametro != 0:
    for i in range (len(original)):
        if original[i] == fav:
            parametro = 0
        
        if i == len(original)-1:
            if parametro == 1:
                print("Você não possue esse livro!")
                fav = str(input("Digite novamente o Favorito: "))

invertida = [] 
final = []
for livro in range(len(original)-1,-1,-1):

    if original[livro] != fav:
        invertida.append(original[livro])

for livro in range(len(invertida)-1,-1,-1):
    final.append(invertida[livro])

print(final)

    
    