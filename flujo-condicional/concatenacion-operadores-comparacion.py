edad_p=input("ingrese su edad: ")
edad_p=int(edad_p)
def evaluacion(edad):
    # primero evalua 0<edad.... si se cumple pasa a evaluar edad<100... si se cumple  accede al if
    # si no se cumple algunas de las condiciones anteriores va directo al else
    if 0<edad<=100:
        acceso="edad correcta"
    else:
        acceso="edad incorrecta"
    return acceso
print(evaluacion(edad_p))
