distancia_colegio=int(input("introduce su  distancia al colegio en km: "))
print(distancia_colegio)
num_hermanos=int(input("introduce el numero de hermanos: "))
print(num_hermanos)
salario_familiar=int(input("introduce el salario familiar mensual: "))
print(salario_familiar)
# el operador and da verdadero si todas sus condiciones son verdad
# el operador or da verdad si alguna de ellas es verdad
if distancia_colegio>=10 and num_hermanos>2 or salario_familiar<=3500:
    print("si tiene derecho a beca")
else:
    print("no tiene derecho beca")
print("----------------------------")
def eleccecion_materias():
    print("materias disponibles: Introduccion a la programacion, Fisica, Algebra")
    opcion=input("escriba la materia escogida: ")
    materia=opcion.lower()
    if materia in ("introduccion a la programacion", "fisica", "algebra"):
        print("eligio la materia: "+materia)
    else:
        print("la materia selecionada no coincide con las materias disponibles")
        return
print(eleccecion_materias())

