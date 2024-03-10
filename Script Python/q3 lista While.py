num1 = int(input("Base: "))
num2 = int(input("Expoente: "))
n = 1
while n != 0:

    if num1 > 0 and num2 > 0:
        print("Resultado: ")
        print(pow(num1,num2))
        n = 0
    
    else: 
        print("Os números informados não são naturais")
        num1 = int(input("Base: "))
        num2 = int(input("Expoente: "))
