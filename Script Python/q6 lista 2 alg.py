num1 = int(input("Digite um valor: "))
num2 = int(input("Digite outro valor: "))
num3 = int(input("Digite mais um valor: "))

if num1 > num2 and num2 > num3:
    print("Maiores valores: {} e {}".format(num1,num2))
    print("Produto da soma: {}".format(num1+num2))

elif num2 > num1 and num1 > num3:
    print("Maiores valores: {} e {}".format(num2,num1))
    print("Produto da soma: {}".format(num2+num1))

elif num2 > num3 and num3>num1:
    print("Maiores valores: {} e {}".format(num2,num3))
    print("Produto da soma: {}".format(num2+num3))

elif num3 > num2 and num2> num1:
    print("Maiores valores: {} e {}".format(num3,num2))
    print("Produto da soma: {}".format(num3+num2))

elif num1 > num3 and num3 > num2:
    print("Maiores valores: {} e {}".format(num1,num3))
    print("Produto da soma: {}".format(num1+num3))

else:
    print("Maiores valores: {} e {}".format(num3,num1))
    print("Produto da soma: {}".format(num3+num1))