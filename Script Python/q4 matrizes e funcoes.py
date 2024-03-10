def multM(a, b): #'''essa foi a função que eu tentei fazer'''
    if len(a) == len(b[0]):
        r = []
        for i in range(len(a)):
            r.append([])
            for j in range(len(b[0])):
                for k in range(len(a)):
                    val = a[i][j] * b[k][i]
                r[-1].append(val)
        return print(r)



a = [[1],[2],[3],
     [4],[5],[6],
     [7],[8],[9]]

b = [[1],[2],[3],
     [4],[5],[6],
     [7],[8],[9]]

print(multM(a,b))        
