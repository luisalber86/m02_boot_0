def normal(x):
    return x

def cuadrado(y):
    return y * y

def cubo(x):
    return x**3 #operador de potencia ** (al cubo)

#funciones de primer nivel: admite funciones como parametro de entrada
def sumaTodos(limitTo, f):
    resultado = 0
    for i in range(limitTo+1):
        resultado += f(i)
    
    return resultado

#Para que no lo haga cuando importo funciones
#Y solo se ejecuta cuando lo realice desde este archivo
if __name__ == '__main__':
    print(sumaTodos(100, normal))
    print(sumaTodos(3,cuadrado))
    print(sumaTodos(3,cubo))
