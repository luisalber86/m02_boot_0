#definición de objetos, siempre empieza por Mayus.
class Perro():
    #función constructora
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
    
    def ladrar(self): #debemos poner un parametro siempre
        if self.peso >= 8:
            print("GUAU, GUAU")
        else:
            print("guau, guau")
            
    #funcion standard por si hacemos print, no nos devuelva el lugar de memoria
    def __str__(self):
        return "- Mi Nombre es {}, tengo: {} años y un peso de {} Kg".format(self.nombre, self.edad, self.peso)
 
 
 
#Subclase de Perro, hereda de Perro
class PerroAsistencia(Perro):
    def __init__(self, nombre, edad, peso, amo):
        Perro.__init__(self, nombre, edad, peso)
        self.amo = amo
        self.__trabajando = False 
        
    #sobreescribir metodo __str__ (print)
    def __str__(self):
        return "- Mi Nombre es {}, tengo: {} años y un peso de {} Kg. Soy un perro de asistencia de {}. Estoy Trabajando?".format(self.nombre, self.edad, self.peso, self.amo, self.__trabajando)

    def pasear(self):
        print("ayudo a pasear a mi amo {}".format(self.amo))

    def ladrar(self):
        if self.__trabajando: #__ significa privados
            print("No puedo ladrar")
        else:
            Perro.ladrar(self) #necesario meter la instancia, ivocar metodo padre

    #definir funcion(metodo) para cambiar self.__trabajando
    def trabajando(self, valor = None):
        if valor == None:
            return self.__trabajando
        else:
            self.__trabajando = valor


class Timido():
    def __init__(self, nombre):
        self.__nombre = nombre

    def preguntarNombreConCuidado(self):
        return self.__nombre
        
salchicho = Perro('Salchicho', 3, 40)
juno = Perro('Juno', 8, 17)
lola = Perro('Lola', 2, 3)
perroguia = PerroAsistencia ('Perroguia', 4, 9, 'Luis')


print(juno)
print(perroguia)