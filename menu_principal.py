from ejecutivo import Ejecutivo
import pandas as pd

def crear_cuenta(df_ejecutivos):
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    correo = input("Correo: ")
    contrasenia = input("Contraseña: ")
    ejecutivo = Ejecutivo(nombre, apellido, correo, contrasenia, df_ejecutivos)
    ejecutivo.guardar_en_csv()
    print("Cuenta creada exitosamente.")

def iniciar_sesion(df_ejecutivos):
    correo = input("Correo: ")
    contrasenia = input("Contraseña: ")
    ejecutivo = df_ejecutivos[df_ejecutivos["Correo"] == correo]
    if not ejecutivo.empty and ejecutivo.iloc[0]["Contraseña"] == contrasenia:
        print(f"Bienvenido {ejecutivo.iloc[0]['Nombre']} {ejecutivo.iloc[0]['Apellido']}")
    else:
        print("Correo o contraseña incorrectos.")
