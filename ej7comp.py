num = int( input("Ingrese un numero: "))
primo = True
j = 1
for i in range(2, num):
    if num%i == 0:
        primo = False
        print("No es primo")
        break
if primo==True:
    print("Es primo")