from dataframes import inicializar_dataframes
from menu_principal import crear_cuenta, iniciar_sesion

if __name__ == "__main__":
    df_inventario, df_clientes, df_citas, df_ventas, df_ejecutivos = inicializar_dataframes()
    
    while True:
        print("\n--- Menú Principal ---")
        print("1. Iniciar sesión")
        print("2. Crear cuenta")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            iniciar_sesion(df_ejecutivos)
        elif opcion == "2":
            crear_cuenta(df_ejecutivos)
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")
