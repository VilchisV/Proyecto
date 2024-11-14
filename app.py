import streamlit as st
import pandas as pd
import random
import os
from PIL import Image
from io import BytesIO
from ejecutivo import Ejecutivo  # Asegúrate de tener la clase Ejecutivo en este archivo
from ventas import Ventas
from inventario import Inventario
from producto import Producto
from cliente import Cliente

# Ruta de los archivos CSV
PATH_EJECUTIVOS = 'data/ejecutivos.csv'
PATH_VENTAS = 'data/ventas.csv'
PATH_INVENTARIO = 'data/inventario.csv'
PATH_CLIENTES = 'data/clientes.csv'

# Crear los directorios si no existen
if not os.path.exists('data'):
    os.makedirs('data')

# Cargar los DataFrames desde los CSV (si existen)
def cargar_datos():
    if os.path.exists(PATH_EJECUTIVOS):
        st.session_state.df_ejecutivos = pd.read_csv(PATH_EJECUTIVOS)
    else:
        st.session_state.df_ejecutivos = pd.DataFrame(columns=["Nombre", "Apellido", "Correo", "Contraseña"])

    if os.path.exists(PATH_VENTAS):
        st.session_state.df_ventas = pd.read_csv(PATH_VENTAS)
    else:
        st.session_state.df_ventas = pd.DataFrame(columns=["ID Venta", "Cliente", "Total", "Método de Pago"])

    if os.path.exists(PATH_INVENTARIO):
        st.session_state.df_inventario = pd.read_csv(PATH_INVENTARIO)
    else:
        st.session_state.df_inventario = pd.DataFrame(columns=["ID Producto", "Producto", "Cantidad", "Precio"])

    if os.path.exists(PATH_CLIENTES):
        st.session_state.df_clientes = pd.read_csv(PATH_CLIENTES)
    else:
        st.session_state.df_clientes = pd.DataFrame(columns=["Nombre", "Apellido", "Correo", "Preferencias", "Cita Agendada"])

# Guardar los DataFrames en CSV
def guardar_datos():
    st.session_state.df_ejecutivos.to_csv(PATH_EJECUTIVOS, index=False)
    st.session_state.df_ventas.to_csv(PATH_VENTAS, index=False)
    st.session_state.df_inventario.to_csv(PATH_INVENTARIO, index=False)
    st.session_state.df_clientes.to_csv(PATH_CLIENTES, index=False)

# Función para generar ID aleatorio
def generar_id_aleatorio():
    return random.randint(10000, 99999)

# Funciones de gestión de clientes
def gestionar_clientes():
    st.subheader("Gestión de Clientes")
    submenu = st.radio("Selecciona una opción:", ["Registrar Cliente", "Listar Clientes", "Agregar Preferencias", "Agendar Cita"])

    if submenu == "Registrar Cliente":
        nombre = st.text_input("Nombre del Cliente", key="nombre_cliente")
        apellido = st.text_input("Apellido del Cliente", key="apellido_cliente")
        correo = st.text_input("Correo del Cliente", key="correo_cliente")
        if st.button("Registrar Cliente"):
            nuevo_cliente = Cliente(nombre, apellido, correo, preferencias="")
            cliente_registro = pd.DataFrame([{
                "Nombre": nombre,
                "Apellido": apellido,
                "Correo": correo,
                "Preferencias": "",
                "Cita Agendada": ""
            }])
            st.session_state.df_clientes = pd.concat([st.session_state.df_clientes, cliente_registro], ignore_index=True)
            guardar_datos()  # Guardamos los datos en el archivo CSV
            st.success(f"Cliente {nombre} registrado correctamente.")

    elif submenu == "Listar Clientes":
        st.subheader("Lista de Clientes")
        if not st.session_state.df_clientes.empty:
            st.write(st.session_state.df_clientes)
        else:
            st.write("No hay clientes registrados.")

    elif submenu == "Agregar Preferencias":
        correo = st.text_input("Correo del Cliente para agregar preferencias", key="correo_preferencias")
        preferencias = st.text_area("Preferencias de Compra", key="preferencias_cliente")
        if st.button("Agregar Preferencias"):
            cliente = st.session_state.df_clientes[st.session_state.df_clientes['Correo'] == correo]
            if not cliente.empty:
                st.session_state.df_clientes.loc[st.session_state.df_clientes['Correo'] == correo, 'Preferencias'] = preferencias
                guardar_datos()  # Guardamos los datos en el archivo CSV
                st.success("Preferencias agregadas correctamente.")
            else:
                st.error("Cliente no encontrado.")

    elif submenu == "Agendar Cita":
        correo = st.text_input("Correo del Cliente para agendar cita", key="correo_agenda_cita")
        fecha_cita = st.date_input("Fecha de la cita", key="fecha_cita")
        if st.button("Agendar Cita"):
            cliente = st.session_state.df_clientes[st.session_state.df_clientes['Correo'] == correo]
            if not cliente.empty:
                st.session_state.df_clientes.loc[st.session_state.df_clientes['Correo'] == correo, 'Cita Agendada'] = str(fecha_cita)
                guardar_datos()  # Guardamos los datos en el archivo CSV
                st.success(f"Cita agendada para el {fecha_cita} exitosamente.")
            else:
                st.error("Cliente no encontrado.")

# Funciones de gestión de inventario y ventas
def gestionar_inventario():
    st.subheader("Gestión de Inventario")
    submenu = st.radio("Selecciona una opción:", ["Agregar Producto", "Eliminar Producto", "Listar Productos"])
    
    if submenu == "Agregar Producto":
        nombre = st.text_input("Nombre del producto", key="nombre_producto")
        precio = st.number_input("Precio", min_value=0.0, key="precio_producto")
        cantidad = st.number_input("Cantidad", min_value=0, step=1, key="cantidad_producto")
        if st.button("Agregar Producto"):
            id_producto = generar_id_aleatorio()  # Generar ID aleatorio
            nuevo_producto = {
                "ID Producto": id_producto,
                "Producto": nombre,
                "Cantidad": cantidad,
                "Precio": precio
            }
            st.session_state.df_inventario = pd.concat([st.session_state.df_inventario, pd.DataFrame([nuevo_producto])], ignore_index=True)
            guardar_datos()  # Guardamos los datos en el archivo CSV
            st.success("Producto agregado correctamente.")

    elif submenu == "Eliminar Producto":
        id_producto = st.number_input("ID del producto a eliminar", min_value=10000, step=1, key="id_producto_eliminar")
        if st.button("Eliminar Producto"):
            if id_producto in st.session_state.df_inventario['ID Producto'].values:
                st.session_state.df_inventario = st.session_state.df_inventario[st.session_state.df_inventario['ID Producto'] != id_producto]
                guardar_datos()  # Guardamos los datos en el archivo CSV
                st.success("Producto eliminado correctamente.")
            else:
                st.error("ID de producto no encontrado.")

    elif submenu == "Listar Productos":
        st.subheader("Lista de Productos")
        if not st.session_state.df_inventario.empty:
            st.write(st.session_state.df_inventario)
        else:
            st.write("No hay productos en el inventario.")

def registrar_venta():
    st.title("Registrar Venta")
    cliente = st.text_input("Nombre del cliente", key="cliente_venta")
    total = st.number_input("Total de la venta", min_value=0.0, key="total_venta")
    metodo_pago = st.selectbox("Método de Pago", ["Efectivo", "Tarjeta"], key="metodo_pago")
    if st.button("Registrar Venta"):
        id_venta = generar_id_aleatorio()  # Generar ID aleatorio
        nueva_venta = {
            "ID Venta": id_venta,
            "Cliente": cliente,
            "Total": total,
            "Método de Pago": metodo_pago
        }
        st.session_state.df_ventas = pd.concat([st.session_state.df_ventas, pd.DataFrame([nueva_venta])], ignore_index=True)
        guardar_datos()  # Guardamos los datos en el archivo CSV
        st.success("Venta registrada correctamente.")

def historial_ventas():
    st.title("Historial de Ventas")
    if not st.session_state.df_ventas.empty:
        st.write(st.session_state.df_ventas)
    else:
        st.write("No hay ventas registradas.")

# Funciones de creación e inicio de sesión
def crear_cuenta(nombre, apellido, correo, contrasenia):
    # Verificar si el correo ya está registrado
    if correo in st.session_state.df_ejecutivos['Correo'].values:
        return "El correo ya está registrado."
    
    nuevo_ejecutivo = {
        "Nombre": nombre,
        "Apellido": apellido,
        "Correo": correo,
        "Contraseña": contrasenia
    }
    
    st.session_state.df_ejecutivos = pd.concat([st.session_state.df_ejecutivos, pd.DataFrame([nuevo_ejecutivo])], ignore_index=True)
    guardar_datos()
    return "Cuenta creada exitosamente."

def iniciar_sesion(correo, contrasenia):
    # Buscar al usuario en el DataFrame
    usuario = st.session_state.df_ejecutivos[st.session_state.df_ejecutivos['Correo'] == correo]
    
    if not usuario.empty and usuario.iloc[0]['Contraseña'] == contrasenia:
        st.session_state.usuario_logueado = usuario.iloc[0]
        return True
    else:
        return False

# Streamlit App
st.sidebar.title("Menú Principal")
st.markdown("<h1 style='text-align: center;'>Universidad Nacional Autónoma de México</h1>", unsafe_allow_html=True)
st.write("\t ## Matemáticas Aplicadas y Computación")
# URLs de las imágenes en formato raw de GitHub
image_url1 = "https://raw.githubusercontent.com/VilchisV/Proyecto/main/Logo.png"
image_url2 = "https://raw.githubusercontent.com/VilchisV/Proyecto/main/UNAM.png"

# Definir las columnas con diferentes anchos
col_uno, col_dos = st.columns([1, 2], gap="small")

# Contenido de la primera columna
with col_uno:
# Agregar una imagen en la primera columna desde una URL
    st.image(image_url1)

# Agregar el texto en la primera columna
st.write("## CAPYCODE ")

# Contenido de la segunda columna
with col_dos:
# Agregar una imagen en la segunda columna desde una URL
    st.image(image_url2, width=170, caption=None)

# Agregar el texto en la segunda columna
st.info(
    "### Desarrolladores:\n"
    "- Alcantar Hernandez Jessica Esmeralda \n"
    "- Vilchis López Víctor Manuel\n"
    "- Guevara Moysen Jorge Isaac\n"
    "- Enríquez Sánchez Joshua Antonio",
    icon="ℹ️"
)




if 'usuario_logueado' in st.session_state:
    submenu_opcion = st.sidebar.radio("Selecciona una opción:", ["Gestionar Inventario", "Registrar Venta", "Historial de Ventas", "Gestionar Clientes", "Cerrar Sesión"])
    
    if submenu_opcion == "Gestionar Inventario":
        gestionar_inventario()
    elif submenu_opcion == "Registrar Venta":
        registrar_venta()
    elif submenu_opcion == "Historial de Ventas":
        historial_ventas()
    elif submenu_opcion == "Gestionar Clientes":
        gestionar_clientes()
    elif submenu_opcion == "Cerrar Sesión":
        del st.session_state['usuario_logueado']
        st.success("Has cerrado sesión correctamente.")
else:
    st.title("Iniciar Sesión")
    correo = st.text_input("Correo electrónico", key="correo_login")
    contrasenia = st.text_input("Contraseña", type="password", key="contrasenia_login")
    if st.button("Iniciar Sesión"):
        if iniciar_sesion(correo, contrasenia):
            st.success("Inicio de sesión exitoso.")
        else:
            st.error("Correo o contraseña incorrectos.")
    
    st.title("Crear Cuenta")
    nombre = st.text_input("Nombre", key="nombre_registro")
    apellido = st.text_input("Apellido", key="apellido_registro")
    correo_registro = st.text_input("Correo electrónico", key="correo_registro")
    contrasenia_registro = st.text_input("Contraseña", type="password", key="contrasenia_registro")
    if st.button("Crear Cuenta"):
        respuesta = crear_cuenta(nombre, apellido, correo_registro, contrasenia_registro)
        st.success(respuesta)

cargar_datos()
