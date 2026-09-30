class Cliente:
    def __init__(self, nombre,apellido, dni, telefono,email, reservas):
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.telefono=telefono
        self.email=email
        self.reservas=reservas
        self.reservas=[]

    def agregar_reservas(self, reservas):
        self.reservas.append(reservas)
     
    