n = int( input("Ingrese el numero: "))
res = 0
for i in range(1, n+1):
    if i%2==0:
        res-=1/i
    else:
        res+=1/i
print("El resultado es: ",res)