cantidad = int(input("Ingrese la cantidad de empleados: "))
mayor = 0
print("Ingrese los sueldos")
for i in range(1, cantidad+1):
    print("Sueldo empleado ",i)
    sueldo = float(input())
    if sueldo>mayor:
        mayor=sueldo
        empmayor = i
print("El empleado ",empmayor," tiene el mayor sueldo de ",mayor)