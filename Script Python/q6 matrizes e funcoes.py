def primos(n):       
    count = 0
    for i in range(1,n+1):
        if n%i == 0:
            count+=1
    if count > 2:
        return False
            
    else:
        return True
          
            
n = int(input("Num: "))
resp = primos(n)
print(resp)




