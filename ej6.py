num1=1
num2=0
num3=num1+(2*num2)
contador = 0

while num3<300:
    num2 = num1
    num1 = num3
    num3 = num1 + (2*num2)
    contador+=1
print("El rango es: ",contador)
print("El resultado es: ",num3)