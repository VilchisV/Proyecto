# optica.py
from inventario import Inventario
from agenda import Agenda

class Optica:
    def __init__(self):
        self.inventario = Inventario()
        self.agenda = Agenda()

    def gestionar_inventario(self):
        print("Gestionando Inventario")
        self.inventario.listar_productos()

    def gestionar_agenda(self):
        print("Gestionando Agenda")
        self.agenda.listar_citas()
