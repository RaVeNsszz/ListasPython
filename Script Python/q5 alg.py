cotacao = float(input("Informe a cotação do dolar atual: "))
qtd = float(input("Quantos reais deseja converter em dolares: "))
conversao = qtd/cotacao
print("A conversão de R$ {:.2f} daria US$ {:.2f}" .format(qtd,conversao))