#def fatorial(numero):
#    if numero == 1:
#       return 1
#    
#    return numero * fatorial(numero-1)

#print(fatorial(5))

def mult(lista):
    if len(lista) == 0:    #n
        return #1
    else:   #n
        return lista[0] * mult(lista[1:]) #n^2


print(mult(1,2,3,4,5))#1

