#importa reduce desde functools
from functools import reduce

#operador map
lista = [1, 3, -1, 15, 9, 8]

listaDoble = map(lambda x: x*2, lista)
listaPares = filter(lambda x: x%2 == 0,lista)

sumantorio = reduce(lambda  x, y: x + y, lista)
suma100 = reduce(lambda x,y: x + y, range(101))

#realizar list(listaDoble) para mostrar