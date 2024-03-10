def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

    
n = int(input("Informe a posição: "))
print("O valor na posição {} na sequência de Fibonacci é de {}".format(n,fib(n))) 
