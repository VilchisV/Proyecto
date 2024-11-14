class Cliente:
    def __init__(self, nombre, apellido, correo, preferencias, cita_agendada=None):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.preferencias = preferencias
        self.cita_agendada = cita_agendada