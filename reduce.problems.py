from functools import reduce

lista = [1, 3, -2, 15, 9]



sumatorio = reduce(lambda x, y: x + y, lista)

#para que funcione el reduce correctamente en sumaDoble, se debe añadir 0 al incio de la lista
#creo una copia de la lista
l=lista[:]

#añado el neutro para la suma en la posicion 0
l.insert(0,0)

sumaDoble = reduce(lambda x, y: x + y*2, l)

print(sumatorio)
print(sumaDoble)