num = int( input("Ingrese un numero, y para acabar uno negativo: "))
while num>0:
    suma = 0
    for i in range(1, num+1):
        if num%i==0:
            suma = suma+i
    print("Resultado: ", suma)
    num = int( input("Ingrese otro numero, y para acabar uno negativo: "))