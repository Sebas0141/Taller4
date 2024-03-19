class Vehiculo:
    def __init__(self, matricula):
        self.matricula = matricula
        self.velocidad = 0

    def mostrar_informacion(self):
        print(f"Matrícula: {self.matricula}, Velocidad: {self.velocidad} km/h")

    def acelerar(self, cantidad):
        self.velocidad += cantidad
        print(f"Acelerando. Nueva velocidad: {self.velocidad} km/h")


class Coche(Vehiculo):
    def __init__(self, matricula, num_puertas):
        super().__init__(matricula)
        self.num_puertas = num_puertas

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Número de Puertas: {self.num_puertas}")


class Camion(Vehiculo):
    def __init__(self, matricula, carga_maxima):
        super().__init__(matricula)
        self.carga_maxima = carga_maxima

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Carga Máxima: {self.carga_maxima} toneladas")


coche = Coche("ABC123", 4)
camion = Camion("XYZ456", 10)

coche.mostrar_informacion()
camion.mostrar_informacion()

coche.acelerar(50)
camion.acelerar(30)