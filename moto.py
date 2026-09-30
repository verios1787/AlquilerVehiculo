from vehiculos import Vehiculo

class Moto(Vehiculo):

    def __init__(self, patente, marca, modelo, tarifa_base, ):
        super().__init__(patente, marca, modelo, tarifa_base, )


    def calcular_costo(self, dias):
        return self.tarifa_base * 0.85 * dias