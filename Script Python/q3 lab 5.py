#Calcular porcentagem de cashback
#5 compras -> 1%
# 6 a 10 -> 1,5%
# +10 -> 2%
def cash(compras):
    if compras < 5:
        print("Você ainda não tem cashback!")
    
    else:
        if compras == 5:
            print("Você possue cashback de 1% na sua compra!!!")
        elif compras >= 6 and compras <=10:
            print("Você possue cashback de 1,5% na sua compra!!!")
        else:
            print("Você possue cashback de 2% na sua compra!!!")
        

compras = int(input("Número de Compras: "))
cash(compras)

