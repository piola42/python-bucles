num = int( input("Ingrese un numero: "))
resultado = 0
while num>0:
    resto = num%10
    resultado = resultado*10+resto
    num = num//10
print("El resultado es: ",resultado)