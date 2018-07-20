# un diccionario es un conjunto de elementos... cada elemento tiene una clave y un valor
# la clave como el valor puede ser cualquier tipo de dato
diccionario={"Bolivia":"Sucre", "Peru":"Lima", "Venezuela":"Bolivar"}
print(diccionario)
print("---------------")
# acceder al valor de los elementos... se una la clave del elemento..... diccionario[clave]
print(diccionario["Bolivia"])
print(diccionario["Peru"])
print("---------------")
# agregar mas elementos al diccionario ......diccionario[nuevaClave]=valor
diccionario["Argentina"]="fgfgdfg"
print(diccionario)
print("---------------")
# modificar el valor de una clave ........ diccionario[Clave]=nuevoValor
diccionario["Argentina"]="Buenos Aires"
print(diccionario)
print("---------------")
# eliminar un elemento
del diccionario["Peru"]
print(diccionario)
print("---------------")
# se puede mesclar tipos de datos
diccionario1={"Bolivia":"Sucre", 4:"hola", "mosqueteros":3, 9:5.66}
print(diccionario1)
print("---------------")
# se pueden guardar tuplas
mi_diccionario={"equipo":"wilterman", "estrellas":6, "copas":(2008,2010,2015,2018)}
print(mi_diccionario)
print(mi_diccionario["equipo"])
print(mi_diccionario["copas"])
print("---------------")
# tambien se puede guardar otros diccionarios
mi_diccionario1={"equipo":"wilterman", "estrellas":6, "copas":{"torneos":(2008,2010,2015,2018)}}
print(mi_diccionario1)
print(mi_diccionario1["equipo"])
print(mi_diccionario1["copas"])
print("---------------")
# metodos utiles cuando trabajamos con diccionarios
print(mi_diccionario1.keys())
print(mi_diccionario1.values())
print(len(mi_diccionario1))

