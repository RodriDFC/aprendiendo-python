import math
# la condicion del while es como una condicion de un if
i = 1
while i <= 10:
    print(f"Ejecucion numero {i}. El valor de i es: {i}")
    i += 1
print("final de la ejecuacion")
print("-----------------------")
edad=int(input("introduce tu edad: "))
while edad < 0 or edad > 100:
    print("la edad es incorrecta. vuelva introducir su edad")
    edad = int(input("introduce tu edad: "))
print(f"termino el bucle while su edad es {edad}")
print("-----------------------")
numero=int(input("introduce un numero: "))
intentos=0
while numero<0 and intentos<2:
    print("el numero es negativo. vuelva introducir un numero")
    numero = int(input("introduce tu edad: "))
    intentos+=1
if intentos<2:
    solucion=math.sqrt(numero)
    print("la raiz cuadrada es: "+str(solucion))
else:
    print("los intentos que tenia se agotaron")
