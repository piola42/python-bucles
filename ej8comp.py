numeros = int(input("Ingrese la cantidad de numeros: "))
contador = 0
print("Ingrese los numeros")
for i in range(1, numeros+1):
    num = int(input())
    if num==0:
        contador+=1
print("Hay ",contador," ceros")