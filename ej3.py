contador = 0
for i in range(1, 1000):
    primo = True
    j = 2
    while (i>j) and (primo==True):
        if i%j == 0:
            primo=False
            break
        else:
            j=j+1
    if primo==True:
        print(i, "Es primo")
        contador+=1
print("Entre 1 y 1000 hay ",contador," numeros primos ")