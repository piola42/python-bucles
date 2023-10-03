x = int (input("Ingrese el valor de x: "))
i = 1
e = 1
den = 1
num = x**i
den*=i
i+=1
e+=num/den
while (num/den>0.000001):
    num = x**i
    den*=i
    i+=1
    e+=num/den
print("e elevado al ",x," es: ",e)