# sintaxis .... nombreTupla=(elemento, elemento.....)
# no se puede modificar la lista añadir,eliminar
tupla=("juan","rodri",5, 5)
print(tupla)
print(tupla[1])
print(tupla[2])
print("---------")
# convertir tupla en lista
lista=list(tupla)
print(lista)
print("---------")
# convertir lista en tupla
lista1=[12,14,84]
tupla1=tuple(lista1)
print(lista1)
print(tupla1)
print("---------")
# buscar un elemento en la tupla
print("marco" in tupla)
print("rodri" in tupla)
print("---------")
# cuantos veces se repiten un elemento en la tupla
print(tupla.count("rodri"))
print(tupla.count(5))
print("---------")
# tamaño de una tupla
print(len(lista))
print("---------")
# una tupla se la puede definir sin parantesis
otra_tupla="juan", 4, 9,1994
print(otra_tupla)
print("---------")
# desempaquetado de tuplas...... se asigna en el mismo orden que la tupla
nombre, dia, mes, año=otra_tupla
print(nombre)
print(dia)
print(mes)
print(año)
print("---------")
# saber el indice de un elemento
print(tupla.index("rodri"))
