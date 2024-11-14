from inventario import Inventario
from cita import Cita
from ventas import Venta
from producto import Producto
class MenuEjecutivo:
    def __init__(self, ejecutivo, inventario, clientes, agenda, ventas):
        self.ejecutivo = ejecutivo
        self.inventario = inventario  # Aquí es una instancia de Inventario
        self.clientes = clientes
        self.agenda = agenda
        self.ventas = ventas

    def mostrar_menu(self):
        print("\n Menú Ejecutivo:")
        print("1. Ver inventario")
        print("2. Ver clientes")
        print("3. Agendar cita")
        print("4. Ver citas agendadas")
        print("5. Ver ventas")
        print("6. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            self.mostrar_submenu_inventario()  # Llama al submenú de inventario
        elif opcion == "2":
            self.mostrar_clientes()
        elif opcion == "3":
            self.agendar_cita()
        elif opcion == "4":
            self.listar_citas()
        elif opcion == "5":
            self.mostrar_ventas()
        elif opcion == "6":
            print("Saliendo...")
            exit()
        else:
            print("Opción no válida, intenta de nuevo.")

    def mostrar_submenu_inventario(self):
        print("\nSubmenú Inventario:")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Listar productos")
        print("4. Volver al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            self.agregar_producto()
        elif opcion == "2":
            self.eliminar_producto()
        elif opcion == "3":
            self.inventario.listar_productos()  # Llama al método de Inventario
        elif opcion == "4":
            self.mostrar_menu()  # Vuelve al menú principal
        else:
            print("Opción no válida, intenta de nuevo.")

    def agregar_producto(self):
        id_producto = input("Introduce el ID del producto: ")
        nombre = input("Introduce el nombre del producto: ")
        precio = float(input("Introduce el precio del producto: "))
        cantidad = int(input("Introduce la cantidad del producto: "))
        
        producto = Producto(id_producto, nombre, precio, cantidad)
        self.inventario.agregar_producto(producto)

    def eliminar_producto(self):
        id_producto = input("Introduce el ID del producto a eliminar: ")
        self.inventario.eliminar_producto(id_producto)

    def mostrar_clientes(self):
        print("Mostrando clientes...")
        for cliente in self.clientes:
            print(cliente)

    def agendar_cita(self):
        cliente = input("Introduce el nombre del cliente: ")
        fecha = input("Introduce la fecha de la cita: ")
        hora = input("Introduce la hora de la cita: ")
        cita = Cita(cliente, fecha, hora)
        self.agenda.agendar_cita(cita)
        print("Cita agendada correctamente.")

    def listar_citas(self):
        print("Listando citas...")
        self.agenda.listar_citas()

    def mostrar_ventas(self):
        print("Mostrando ventas...")
        for venta in self.ventas:
            print(venta)
