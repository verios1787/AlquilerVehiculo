from auto import Auto
from camioneta import Camioneta
from moto import Moto

class Sucursal:
    def __init__(self, codigo,ciudad,direccion):
        self.codigo=codigo
        self.ciudad=ciudad
        self.direccion=direccion       
        self.vehiculos=[
            Auto("AE456FR", "Toyota", "Etios", 100000),        
            Auto("AE783SD", "Fiat", "Cronos", 95000),            
            Moto("AF457CX", "Honda", "Wave", 25000),
            Moto("AF749LS", "Yamaha", "FZ", 35000),          
            Camioneta("AH325LP", "Toyota", "Hilux", 220000),
            Camioneta("AI646QR", "Volkswagen", "Amarok", 210000)
        ]

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append (vehiculo)

    def quitar_vehiculos ( self,vehiculo):
        if vehiculo in self.vehiculos:
            self.vehiculos.remove(vehiculo)

    def listar_vehiculos(self):
        for vehiculo in self.vehiculos:
            print (vehiculo)
    