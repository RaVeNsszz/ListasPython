condicao = "inicio"
lista=[]
while condicao != "Fim":
    condicao = str(input("Editar tarefas(remover,adicionar), Fim para parar: ")).title()
    if condicao == "Adicionar":
        lista.append(str(input("Digite: ")))   
    elif condicao == "Remover":
        if lista == []:
            print("Lista vazia")
        else:
            x = lista.pop(0)
            print(x,"removido da fila")
    elif condicao == "Fim":
        print("Fila atual : ",lista)
    else:
        print("Comando Inválido")
