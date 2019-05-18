class Vehiculo():
    def __init__(self, pasajeros, velocidadM):
        self.pasajeros = pasajeros
        self.velocidadM = velocidadM
        

class Moto():
    def __init__(self, ruedas, maletero):
        Vehiculo.__init__(self, pasajeros, veloridadM)
        self.ruedas = ruedas
        self.maletero = maletero
    
class Coche():
    def __init__(self, puertas, maletero):
        Vehiculo.__init__(self, pasajeros, velocidadM)
        self.puertas = puertas
        self.maletero = maletero