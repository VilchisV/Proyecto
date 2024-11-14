class Cita:
    def __init__(self, cliente, fecha, hora):
        self.cliente = cliente
        self.fecha = fecha
        self.hora = hora

    def __str__(self):
        return f"Cliente: {self.cliente}, Fecha: {self.fecha}, Hora: {self.hora}"
