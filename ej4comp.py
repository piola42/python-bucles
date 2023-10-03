nterminos = int( input("Ingrese el numero de terminos: "))
termino = 5
serie = 0

for i in range(1, nterminos+1):
    termino+=5
    serie+=termino
print("La suma de la serie es: ",serie)