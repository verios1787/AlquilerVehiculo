class ServicioNotificaciones:
    def notificar (self, cliente, mensaje):
        self.cliente=cliente
        self.mensaje=mensaje
        print (f"Notifiacion para {cliente.email} : {mensaje} ")