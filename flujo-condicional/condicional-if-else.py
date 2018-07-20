# un else biene con el if mas cercano y en la misma sangria
# if-elif-else funciona com una unidad
edad_p=input("ingrese su edad: ")
edad_p=int(edad_p)
def evaluacion(edad):
    if edad<18:
        acceso="no puedes acceder"
    elif edad>100:
        acceso="edad incorrecta"
    else:
        acceso="puedes acceder"
    return acceso
print(evaluacion(edad_p))
