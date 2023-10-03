contador = 0
print("Ingrese 50 caracteres")
for i in range(1, 50):
    car = input()
    if car == "a":
        contador+=1
print("Hay ",contador," caracteres a")