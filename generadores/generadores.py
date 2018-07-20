def pares(limite):
    num=1
    lista=[]
    while num<limite:
        lista.append(num*2)
        num+=1
    return lista
li=pares(10)
print(li)
print("acceder al 1er elemento")
print(li[0])
print("acceder al 2do elemento")
print(li[1])
print("--------------")
# un generador es similar a una funcion con la diferencia que usa yield
# es usada para devolver valores de una lista sin necesidad de tener la lista completa
def pares1(limite):
    num=1
    while num<limite:
        yield num*2
        num+=1
num_pares=pares1(10)
print("acceder al 1er elemento")
print(next(num_pares))
print("acceder al 2do elemento")
print(next(num_pares))
