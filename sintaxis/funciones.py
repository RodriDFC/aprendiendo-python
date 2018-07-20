# declaracion
def mensajes():
    # cuerpo
    print("aprendiendo python")
    print("funciones")
# llamada
mensajes()
# funciones con parametros y sin return
print("funcion sin return")
def suma(n1, n2):
    print(n1 + n2)
suma(5, 2)
a = 10
b = 5
suma(a, b)
# funciones con parametros y con return
print("funcion con return")
def suma_r(n1, n2):
    res = n1 + n2
    return res
print(suma_r(5, 2))
a = 10
b = 5
resultado = suma_r(a, b)
print(resultado)
