contador = 0
print("Ingrese 100 numeros enteros")
for i in range(1, 100+1):
    num = int(input())
    if num%2==0:
        contador+=1
print("Hay ",contador," numeros pares")