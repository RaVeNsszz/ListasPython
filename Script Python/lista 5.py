nota = float(input("Nota: Zero para parar"))
             
while nota != 0:
    if nota < 0 and nota > 10:
        print("Nota Inválida!")

    if nota >= 7.0:
        print("Aprovado na Matéria com: ",nota)
    else: 
        print("Reprovado na Matéria com: ",nota)
            
    nota = float(input("Nota: Zero para parar"))           
