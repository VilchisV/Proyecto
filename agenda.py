# agenda.py
from cita import Cita
import pandas as pd
class Agenda:
    def __init__(self, df_citas):
        self.df_citas = df_citas  # Solo recibe el DataFrame de citas

    def agendar_cita(self, cita):
        nuevo_cita = {
            "id": cita.id,
            "cliente": cita.cliente,
            "fecha": cita.fecha,
            "hora": cita.hora,
            "motivo": cita.motivo
        }
        self.df_citas = pd.concat([self.df_citas, pd.DataFrame([nuevo_cita])], ignore_index=True)

    def listar_citas(self):
        print(self.df_citas)

    def buscar_cita(self, id_cita):
        cita = self.df_citas[self.df_citas["id"] == id_cita]
        if not cita.empty:
            print(cita)
        else:
            print(f"Cita con ID {id_cita} no encontrada.")
