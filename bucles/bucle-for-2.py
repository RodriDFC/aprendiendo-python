# para usar la funcion print cuando se quiere imprimir mensajes y el valor de las variables hacer
# print(f"mensaje de la variable: {variable}")
for i in range(7):
    print(f"mensaje de la variable: {i}")
print("-------------")
# con range(n,m)..... empieza en n y termina en m-1..... teniendo una longitud de m-n
for j in range(3,9):
    print(f"mensaje de la variable: {j}")
print("-------------")
# con range(n,m,p)..... empieza en n, cuenta en multiplos de p
# termina en m-1 o en algun valor segun p
for k in range(10,30,3):
    print(f"mensaje de la variable: {k}")
print("-------------")