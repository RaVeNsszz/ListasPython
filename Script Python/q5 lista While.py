
pq = "Sim"
preco = 0
while pq != "N":

    print("-"*30)
    print("INGRESSOS AQUI")
    print("-"*30)
    print("CATEGORIAS\nCategoria A – R$40,00 /Categoria B – R$30,00 / Categoria C – R$25,00.")

    id = int(input("Idade: "))#provavelmente cada ingresso pode ser para pessoas distintas com idades diferentes
    cat = str(input("Categoria: ")).upper()

    if cat == "A" and id >= 60:
        dis = 40/2
        preco+=dis
    elif cat == "A" and id < 60:
        valor = 40
        preco += valor
    
    elif cat == "B" and id >= 60:
        dis = 30/2
        preco+=dis
    
    elif cat == "B" and id < 60:
        valor = 30
        preco += valor
    
    elif cat == "C" and id >= 60:
        dis = 25/2
        preco+=dis
    
    else:
        valor = 25
        preco += valor
    
    pq = str(input("Deseja continuar Sim(S) ou Não(N)?: ")).upper()
    ,
print("Valor total da compra: R${:.2f}".format(preco))





