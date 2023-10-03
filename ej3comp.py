contador = 0
for i in range(2, 30):
    primo = True
    j = 2
    while (i>j) and (primo==True):
        if i%j == 0:
            primo=False
            break
        else:
            j+=1
    if primo==True:
        print("El cubo de ",i," es ",i**3)
        contador+=1