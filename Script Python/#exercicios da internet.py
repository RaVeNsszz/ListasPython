#exercicios da internet 
correcao = ["a","c","b","d","a","c","d","a","c","d"]
matriz = [
["c","a","b","c","d","b","a","d","c","d"],
["a","c","b","a","d","c","a","b","c","d"],
["d","b","a","c","d","a","c","b","a","c"],
["b","c","b","d","a","b","d","c","b","c"],
["c","d","a","b","a","c","b","a","b","c"]
]
count = 0
situacao = []
for i in range(len(matriz)):
    situacao.append([])
    for j in range(len(matriz)):
        resposta = matriz[i][j]
        if correcao[j][i] == resposta:
            count+1
        else:
            count+=0
    situacao[i].append(count)
           
print(situacao)