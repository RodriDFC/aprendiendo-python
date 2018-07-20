# una lista con 4 elementos 0-3
lista=["mauricio","rodri","fabiana","adriana"]
# imprimir toda la lista
print(lista[:])
# imprimir un elemento de la lista
print(lista[0])
print(lista[2])
# imprimir un elemento de la lista indice negativa...... ultimo elemento tiene indice -1
print(lista[-1])
print(lista[-3])
# ver los n primeros elementos....... resultado es un array..... print(lista[:n])
print(lista[:3])
# ver desde el elemento n hasta el final....... resultado es un array....... print(lista[n:])
print(lista[1:])
# agragar 1 elemento a una lista
lista.append("alejandro") # lo agrega al final
print(lista[:])
lista.insert(2,"sandra") # lo agraga en la posicion i....... lista.insert(i,"sandra")
print(lista[:])
# agragar varios elementos a una lista
lista.extend(["adrian","marcos","rodri"])
print(lista[:])
# saber el indice de un elemento
print(lista.index("fabiana"))
print(lista.index("rodri")) # si hay mas elementos iguales nos devuelve el primero empezando la busqueda en 0
# ver si un elemento esta o no en la lista true o false
print("marcos" in lista)
print("marco" in lista)
# remover un elemento de la lista
lista.remove("adrian")
print(lista[:])
# remover el ultimo elemento de una lista
lista.pop()
print(lista[:])
# suma de listas
lista1=["qwery","asdf","zxcv"]
lista2=lista+lista1
print(lista2[:])
# multiplicar lista con un entero
lista3=["pouiu","74rtr","er5er5"]*3
print(lista3[:])
# tamaño de la lista
print(len(lista))




