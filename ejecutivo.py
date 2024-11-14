# ejecutivo.py

class Ejecutivo:
    def __init__(self, nombre, apellido, correo, contrasenia):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contrasenia = contrasenia

    def validar_contrasenia(self, contrasenia):
        # Aquí podrías agregar la lógica para validar la contraseña
        return self.contrasenia == contrasenia
