funcionarios = int(input("Funcionários no setor: "))

for nome in range(1,funcionarios+1):
    
    nome = str(input("Nome: "))
    covid = str(input("Tomou Vacina S/N: "))
    aux = nome
    
    if(covid == "S"):
        
        vacina = str(input("Qual vacina tomou: "))
        listas_vacinas =['Astrazeneca' , 'Coronavac' ,
'Jansen' , 'Pfizer']
        print("Nome: {} Vacina: {} Tipo: {}".format(aux,covid,listas_vacinas[0],[2],[3],[4]))
               
    else:
        negativo = "N"
        print("Nome: {} Vacina: {} Tipo: {}".format(aux,covid,negativo))
        
        
    print("Funcionarios do setor: {} \n Total de vacinados: {}\n Total de NÃO vacinados: {}".format(funcionarios,"S","N"))
    
