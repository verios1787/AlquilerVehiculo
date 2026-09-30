from enums import EstadoVehiculo

class Vehiculo:
    def __init__(self,patente,marca,modelo, tarifa_base, ):
        if tarifa_base <= 0:
                    raise ValueError ("La tarifa debe ser mayor que cero")
        self.patente= patente
        self.marca= marca
        self.modelo= modelo
        self.tarifa_base=tarifa_base
        self.estado = EstadoVehiculo.DISPONIBLE
        
    @property
    def tarifa_base(self):
        return self._tarifa_base
    
    @tarifa_base.setter
    def tarifa_base(self, valor):
        if valor <=0:
            raise ValueError("La tarifa base debe ser mayor que cero")
        self._tarifa_base = valor

    def calcular_costo(self, dias,costo):
        dias=(self.fecha_fin-self.fecha_inicializacion)
   
        if dias <=0:
            raise ValueError ("La cantidad de dias debe ser mayor que cero")
        return self.tarifa_base*dias
    
    def estado_disponible(self):
        return self.estado== EstadoVehiculo.DISPONIBLE

    def cambiar_estado (self, nuevo_estado):
        self.estado=nuevo_estado

    