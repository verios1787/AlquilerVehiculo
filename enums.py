from enum import Enum

class EstadoVehiculo (Enum):
    DISPONIBLE = "disponible"
    RESERVADO = "reservado"
    EN_ALQUILER= "en_alquiler" 
    FUERA_SERVICIO = "fuera_servicio"



class EstadoReserva (Enum):
    SOLICITADA = "Solicitada"
    CONFIRMADA = "Confirmada"
    EN_CURSO = "En curso" 
    FINALIZADA = "Finalizada"
    CANCELADA = " Cancelada"
