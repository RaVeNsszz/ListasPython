#Calcular qual valor máximo do cashback o usuário pode usar para abater na nova venda

def calcular(cash,total):
    porcentagem = cash/100
    #se o cash for  igual 45% do total
    if porcentagem == 45/total:
        conta = total * 0.55
        print("valor descontado: %.2f " %(conta))
    
    if porcentagem > 45/total: 
        conta = total * 0.55
        print("Seu cashback acumulado é superior a 45% do valor do produto! Portanto, só podemos da o disconto de 45% na compra!")
        print("valor descontado: %.2f" %(conta))
    
    if porcentagem < 45/total:
        conta = total*(1-porcentagem)
        print("valor descontado: %.2f" %(conta))

        
        
cash = float(input("Cashback acumulado: "))
total = float(input("Valor da Venda: "))
calcular(cash,total)

