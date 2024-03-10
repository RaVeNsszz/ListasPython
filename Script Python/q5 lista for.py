t = int(input("Quantos termos deseja ser mostrado na sequência de Fibonacci: "))
num = 0
t1 = 0
t2 = 1
print("0")
print("1")
for i in range(t-2):
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(t3)
    
