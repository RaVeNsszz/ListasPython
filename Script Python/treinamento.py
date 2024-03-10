a = [[1],[2],[3],
     [4],[5],[6],
     [7],[8],[9]]

b = [[1],[2],[3],
     [4],[5],[6],
     [7],[8],[9]]
soma = 0
ab = []
for i in range(len(a)):
     ab.append([])
     for j in range(len(a)):
          for k in range(len(b)):
               if a[i][j]:
                    soma = soma + (a[0][k]*b[k][k])
                    ab[i].append(soma)
     
print(ab)