#Determinar se o cliente já pode utilizar o cashback
def determina(cash):

     if cash < 25.00:
        print("Cashback não pode ser aplicado")
     else:
        print("Cashback já pode ser aplicado!")

cash = float(input("CashBack acumulado: "))
determina(cash)
