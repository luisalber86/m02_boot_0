#operador map
lista = [1, 3, -1, 15, 9, 8]

listaDoble = map(lambda x: x*2, lista)
listaPares = filter(lambda x: x%2 == 0,lista)

#realizar list(listaDoble) para mostrar