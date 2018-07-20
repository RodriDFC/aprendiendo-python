# la sintaxis del ciclo es : ......   for <var> in <rango, lista, tupla....>
# el valor de la variable (var) sera el elemento de la tupla o lista .
# la variable puede ser numero o string
# el rango de for sera el tamaño de la lista o tupla (numero de elementos)
for i in [1,2,3,79488888888888888888888888888888888888888888888888888]:
    print("hola")
    print("el valor de i es:")
    print(i)
    print("--------------------")
for j in ("invierno","primavera","verano","otoño"):
    print("hola")
    print("el valor de j es:")
    print(j)
    print("--------------------")
# se puede recorrer un string,
# el rango de for sera el tamaño del string
for i in "hola-mundo":
    print("hola")
    print("el valor de i es:")
    print(i)
    print("--------------------")
# le podemos dar un rango al for,
# se repetira la cantidad de que el numero que se introduzca en .....  range(numero)
# los valores de i van del 0 a numero-1
rango=int(input("introduzca el rango de for: "))
for i in range(rango):
    print("hola")
    print("el valor de i es:")
    print(i)
    print("--------------------")

