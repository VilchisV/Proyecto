import pandas as pd

class Usuario:
    def __init__(self, df_usuarios: pd.DataFrame):
        self.df_usuarios = df_usuarios

    def agregar_usuario(self, nombre, apellido, fecha_nac, correo, telefono):
        nuevo_usuario = {
            "Nombre": nombre,
            "Apellido": apellido,
            "Fecha de Nacimiento": fecha_nac,
            "Correo": correo,
            "Teléfono": telefono
        }
        self.df_usuarios = pd.concat([self.df_usuarios, pd.DataFrame([nuevo_usuario])], ignore_index=True)
        return "Usuario agregado con éxito"

    def obtener_usuarios(self):
        return self.df_usuarios
