for i in "python":
    print(f"estamos en la letra: {i}")
print("--------------")
# cuando se esta ejecutando en bucle for o while, y se encuentra con la intruccion continue
# ingnora el codigo que esta debajo y salta con la siguiente iteracion
for i in "python":
    if i=="h":
        continue
    print(f"estamos en la letra: {i}")
print("--------------")
# despues de ejecutar el while o for ejecuta el else
j=0
numero=2
while j<20:
    if numero>200:
        j=40
    else:
        numero = numero + numero
    j+=1
else:
    print(numero)
    numero=numero//5
    print(numero)

