def fib(n):
    if n > 1:
        return fib(n-1) + fib(n-2)
    return n

x = int(input("Digite um valor: "))

for i in range(x):
    print(fib(i))