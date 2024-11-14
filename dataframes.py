import pandas as pd
import os

def inicializar_dataframes():
    archivos = {
        "inventario.csv": ["ID", "Nombre", "Cantidad", "Precio"],
        "clientes.csv": ["ID", "Nombre", "Correo", "Teléfono"],
        "citas.csv": ["ID", "Cliente", "Fecha", "Hora"],
        "ventas.csv": ["ID Venta", "Cliente", "Total", "Método de Pago", "Fecha"],
        "ejecutivos.csv": ["Correo", "Nombre", "Apellido", "Contraseña"]
    }

    dataframes = {}
    
    for archivo, columnas in archivos.items():
        if os.path.exists(archivo):
            df = pd.read_csv(archivo)
        else:
            df = pd.DataFrame(columns=columnas)
            df.to_csv(archivo, index=False)
        dataframes[archivo] = df

    return (dataframes["inventario.csv"], dataframes["clientes.csv"],
            dataframes["citas.csv"], dataframes["ventas.csv"], dataframes["ejecutivos.csv"])
