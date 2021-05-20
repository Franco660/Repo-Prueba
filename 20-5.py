class vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas


class Coche(vehiculo):
    def __init__(self, velocidad, cilindrada, color, ruedas):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada


class Camioneta(Coche):
    def __init__(self, carga, velocidad, cilindrada, color, ruedas):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga


class Bicicleta(vehiculo):
    def __init__(self, tipo, color, ruedas):
        super().__init__(color, ruedas)
        self.tipo = tipo


class motocicleta(Bicicleta):
    def __init__(self, velocidad, cilindrada, tipo, color, ruedas):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
