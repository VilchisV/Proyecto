import pandas as pd
import random
from datetime import datetime

class Ventas:
    def __init__(self, df_ventas):
        self.df_ventas = df_ventas

    def registrar_venta(self, cliente, total, metodo_pago):
        venta_id = f"V-{random.randint(1000, 9999)}"
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        nueva_venta = {
            'ID Venta': venta_id,
            'Cliente': cliente,
            'Total': total,
            'Método de Pago': metodo_pago,
            'Fecha': fecha
        }
        self.df_ventas = pd.concat([self.df_ventas, pd.DataFrame([nueva_venta])], ignore_index=True)
        self.guardar_en_csv()
        print(f"Venta registrada: {venta_id} y guardada en ventas.csv.")

    def mostrar_historial(self):
        print(self.df_ventas if not self.df_ventas.empty else "No hay ventas registradas.")

    def guardar_en_csv(self):
        self.df_ventas.to_csv('ventas.csv', index=False)
