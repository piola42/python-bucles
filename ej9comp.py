numeros = int(input("Ingrese la cantidad de numeros: "))
print("Ingrese los numeros: ")
num = int(input())
min = num
max = num
for i in range(1, numeros):
    num = int(input())
    if num<min:
        min=num
    if num>max:
        max=num
print("El numero mayor es ",max," y el menor ",min)