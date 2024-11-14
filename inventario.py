import pandas as pd

class Inventario:
    def __init__(self, df_inventario):
        self.df_inventario = df_inventario

    def agregar_producto(self, producto):
        nuevo_producto = {
            "ID": producto.id,
            "Nombre": producto.nombre,
            "Precio": producto.precio,
            "Cantidad": producto.cantidad
        }
        self.df_inventario = pd.concat([self.df_inventario, pd.DataFrame([nuevo_producto])], ignore_index=True)
        self.guardar_en_csv()
        print("Producto agregado y guardado en inventario.csv.")

    def eliminar_producto(self, id_producto):
        self.df_inventario = self.df_inventario[self.df_inventario["ID"] != id_producto]
        self.guardar_en_csv()
        print("Producto eliminado y guardado en inventario.csv.")

    def listar_productos(self):
        print(self.df_inventario if not self.df_inventario.empty else "Inventario vacío.")

    def guardar_en_csv(self):
        self.df_inventario.to_csv('inventario.csv', index=False)
