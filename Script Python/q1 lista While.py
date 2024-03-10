n = 1
while n != 0:
    nota = float(input("Nota: "))

    if nota > 0 and nota <= 10:
        
        if nota >= 7.0:
            situacao = "APROVADO"
            n = 0

        else:
            situacao = "REPROVADO"
            n = 0
           
    else:
        print("Nota Inválida!")
        nota = float(input("Nota: "))
        n = 1
print("Nota: {}\nSituação: {}".format(nota,situacao))