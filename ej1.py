capital = float(0)
interes = int(0)
tiempo = int(0)
while (capital<0) or (interes<=0) or (interes>=100) or (tiempo<=0):
    capital = float( input("Ingrese el capital: "))
    interes = int( input("Ingrese el interes: "))
    tiempo = int( input("Ingrese el tiempo en años: "))

for i in range(tiempo):
    capital = capital*(1+interes/100)
print("Resultado: ", capital)