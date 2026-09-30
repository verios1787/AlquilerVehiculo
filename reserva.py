
from enums import EstadoReserva
from historial import HistorialEstado

class Reserva:
    def __init__ (self, id,cliente,vehiculo, fecha,  fecha_inicio, fecha_fin, historial):
        self.id=id
        self.cliente=cliente
        self.vehiculo=vehiculo
        self.fecha=fecha

        self.__fecha_inicio=None
        self.fecha_inicio= fecha_inicio
        self.__fecha_fin=None
        self.fecha_fin=fecha_fin
        self.historial=historial
        self.historial=[]
        self.estado=EstadoReserva.SOLICITADA
        self.registrar_historial("Reserva creada")

    def registrar_historial(self,descripcion):
            descripcion=HistorialEstado(self,descripcion)

   
    def cambiar_estado(self, nuevo_estado):
          if (self.estado==EstadoReserva.SOLICITADA and nuevo_estado==EstadoReserva.FINALIZADA):
            raise ValueError("Una reserva solicitada no puede" "pasar directamente a finalizada")
          self.estado=nuevo_estado

    @property
    def fecha_inicio(self):
            return self.__fecha_inicio
    
    @fecha_inicio.setter
    def fecha_inicio(self, fecha):
         if self.__fecha_fin and fecha > self.__fecha_fin:
            raise ValueError ("la fecha de inicio debe ser anterior o igual a la de finalizacion. ")
         else:
              self.__fecha_inicio= fecha
    

    @property
    def fecha_fin(self):
            return self.__fecha_fin

    @fecha_fin.setter
    def fecha_fin(self, fecha):
            if fecha <=self.__fecha_inicio:
                raise ValueError("La fecha de finalizacion debe ser posterior a la fecha de inicio ")
            else:
                self.__fecha_fin= fecha



    
          
