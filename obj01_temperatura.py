class Termometro():
    #función constructura:
    def __init__(self): #no tiene sentido poner unidad de Medida al principio
        self.__unidadM = 'C' #por defecto y privadas
        self.__temperatura = 0 #por defecto y privadas
    
    #Metodo, funcionalidad
    def __conversor(self, temperatura, unidad):
        if unidad == 'C':
            return "{} ºF".format((temperatura * 9/5) + 32)
        elif unidad == 'F':
            return "{} ºC".format((temperatura - 32) * 5/9)
        else:
            return "Unidad incorrecta"
    
    #Sobreescribir __str__ (print)
    def __str__(self):
        return "Mi Temperatura es: {} º{}".format(self.__temperatura, self.__unidadM)
    
    #Función setter y getter __unidadM
    def unidadMedida(self, uniM=None):
        if uniM == None:
            return self.__unidadM
        else:
            if uniM == 'F' or uniM == 'C':
                self.__unidadM = uniM
                
    #Función setter y getter __temperatura
    def temperatura(self, tempe = None):
        if tempe == None:
            return self.__temperatura
        else:
            if tempe > 0:
                self.__temperatura = tempe
    
    def mide(self, uniM = None):
        if uniM == None or uniM == self.__unidadM:
            return self.__str__()
        else:
            if uniM == 'F' or uniM == 'C':
                return self.__conversor(self.__temperatura, self.__unidadM)
            else:
                return self.__str__()
