# todo lo que introducimos en consola es un texto (string)
notaEstudiante=input("ingrese nota del estudiante: ")
notaEstudiante=int(notaEstudiante)
def evaluacion(nota):
    valoracion="reprobado"
    if nota>=51:
        valoracion="aprobado"
    return valoracion
print(evaluacion(notaEstudiante))
