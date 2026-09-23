from vehiculos import Vehiculos

class Auto(Vehiculos):

    def __init__(self, patente, marca, modelo, tarifa_base, estado):
        super().__init__(patente, marca, modelo, tarifa_base, estado)
