contador = 0
print("Ingrese 100 numeros")
for i in range(100):
    num = int( input("Ingrese un numero: "))
    if num%2==0:
        contador+=1
print("Numeros pares: ", contador)