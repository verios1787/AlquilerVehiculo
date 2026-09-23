
from sucursal import Sucursal
class Vehiculos(Sucursal):
    def __init__(self,patente,marca,modelo, tarifa_base, estado):
        self.patente= patente
        self.marca= marca
        self.modelo= modelo
        self.tarifa_base=tarifa_base
        self.estado=estado

   