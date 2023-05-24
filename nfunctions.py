import re
import os
import json
import csv

path = "insumos.csv"


def menu():
    """
    Muestra el menú de opciones y solicita al usuario que ingrese una opción.

    Returns:
        str: Opción ingresada por el usuario.
    """
    print("""
        1. Cargar datos desde archivo.
        2. Listar cantidad por marca.
        3. Listar insumos por marca.
        4. Buscar insumo por característica.
        5. Listar insumos ordenados.
        6. Realizar compras.
        7. Guardar en formato JSON.
        8. Leer desde formato JSON.
        9. Actualizar precios.
        10. Salir del programa.
        """)
    opcion = input("Ingrese una opción: ")
    return opcion


def mostrar_datos_productos(datos: dict):
    for dato in datos:
        print(f"ID: {dato['id']}")
        print(f"Descripción: {dato['nombre']}")
        print(f"Marca: {dato['marca']}")
        print(f"Precio: ${dato['precio']}")
        print(f"Característica: {dato['caracteristicas']}")
        print("--------------------------------------------------------------------------")


# ----------------------------------------------------------------------------------------------------
# 1

def formatear_csv(path: str):
    """
    Lee un archivo CSV y retorna una lista de diccionarios con los datos formateados.

    Args:
        path (str): Ruta del archivo CSV.

    Returns:
        list: Lista de diccionarios con los datos formateados.
    """
    with open(path, encoding="utf8") as archivo:
        lista = []
        next(archivo)
        for linea in archivo:
            linea = linea.strip().split(',')
            diccionario_insumo = {
                'id': linea[0],
                'nombre': linea[1],
                'marca': linea[2],
                'precio': float(linea[3].replace('$', '')),
                'caracteristicas': linea[4]
            }
            lista.append(diccionario_insumo)
    return lista


# ----------------------------------------------------------------------------------------------------
# 2

def contar_cantidad_por_marca(lista: list, key: str):
    """
    Cuenta la cantidad de insumos por marca.

    Args:
        lista (list): Lista de insumos.
        key (str): Marca a contar.

    Returns:
        list: Lista de tuplas con la marca y la cantidad de insumos.
    """
    cantidad_por_marca = []
    for insumo in lista:
        marca = insumo[key]
        for item in cantidad_por_marca:
            if item[0] == marca:
                item[1] += 1
                break
        else:
            cantidad_por_marca.append([marca, 1])
    return cantidad_por_marca


# ----------------------------------------------------------------------------------------------------
# 3

def listar_insumos_por_marca(lista: list, key: str, key2: str, key3: str):
    """
    Lista los insumos agrupados por marca.

    Args:
        lista (list): Lista de insumos.
        key (str): Key de 'marca'.
        ket2 (str): Key de 'nombre'.
        key3 (str): Key de 'precio'.

    Returns:
        list: Lista de listas con la marca, el nombre y el precio de cada insumo.
    """
    insumos_por_marca = []
    for insumo in lista:
        marca = insumo[key]
        nombre = insumo[key2]
        precio = insumo[key3]
        insumos_por_marca.append([marca, nombre, precio])
    return insumos_por_marca


# ----------------------------------------------------------------------------------------------------
# 4

def buscar_insumo_por_caracteristica(lista: list, key: str):
    """
    Busca un insumo por una característica ingresada por el usuario.

    Args:
        lista (list): Lista de insumos.
        key (str): Key de característica.

    Returns:
        list: Lista de diccionarios con los insumos que coinciden con la característica buscada.
    """
    lista_caracteristicas = []
    caracteristica = input("Ingrese la caracteristica a buscar: ").capitalize()
    for insumo in lista:
        if key in insumo and re.search(caracteristica, insumo[key]):
            lista_caracteristicas.append(insumo)
    if not lista_caracteristicas:
        print("No se encontraron insumos con las características buscadas")
    return lista_caracteristicas


# ----------------------------------------------------------------------------------------------------
# 5

def ordenar_insumos(lista: list, key: str, key2: int, key3: str):
    """
    Ordena la lista de insumos por marca de forma ascendente y por precio de forma descendente.

    Args:
        lista (list): Lista de insumos.
        key (str): Key de marca.
        key2 (int): Key de precio.
        key3 (str): Key de caracteristicas.

    Returns:
        list: Lista de insumos ordenados.
    """
    for i in range(len(lista)):
        for j in range(len(lista) - 1 - i):
            if lista[j][key] > lista[j + 1][key]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
            elif lista[j][key] == lista[j + 1][key] and lista[j][key2] < lista[j + 1][key2]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    for insumo in lista:
        caracteristicas = insumo[key3].split("~")
        insumo[key3] = caracteristicas[0]

    return lista


# ----------------------------------------------------------------------------------------------------
# 6

def buscar_por_marca(lista: list, marca: str):
    """
    Busca insumos por marca.

    Args:
        lista (list): Lista de insumos.
        marca (str): Marca a buscar.

    Returns:
        list: Lista de insumos que coinciden con la marca buscada.
    """
    productos_encontrados = []
    for producto in lista:
        if producto['marca'] == marca:
            productos_encontrados.append(producto)
    return productos_encontrados


def mostrar_datos_tienda(producto: dict):
    """
    Muestra los datos de un insumo en el formato de tienda.

    Args:
        producto (dict): Datos del insumo.
    """
    print(f"ID: {producto['id']}")
    print(f"Descripción: {producto['nombre']}")
    print(f"Precio: ${producto['marca']}")
    print(f"Marca: {producto['precio']}")
    print(f"Característica: {producto['caracteristicas']}")
    print("--------------------------------------------------------------------------")


def tienda(lista_insumos: list):
    """
    Simula una tienda donde se pueden realizar compras de insumos.

    Args:
        lista_insumos (list): Lista de insumos.
    """
    lista_productos = []
    lista_precios = []

    os.system('cls')

    while True:
        marca_buscada = input(
            "Ingrese la marca que busca (o 'x' para finalizar): ").capitalize()
        if marca_buscada == 'X':
            break

        productos_encontrados = buscar_por_marca(
            lista_insumos, marca_buscada)

        if productos_encontrados:
            print("Productos encontrados:")
            for producto in productos_encontrados:
                mostrar_datos_tienda(producto)

            id_seleccion = input(
                "Ingrese el ID del producto que desea (o 'x' para finalizar): ").capitalize()
            if id_seleccion == 'X':
                break

            producto_seleccionado = None
            for producto in productos_encontrados:
                if producto['id'] == id_seleccion:
                    producto_seleccionado = producto
                    break

            if producto_seleccionado is None:
                print("ID de producto inválido. Inténtelo nuevamente.")
                continue

            try:
                os.system('cls')
                cantidad_buscada = int(
                    input("Ingrese la cantidad que desea comprar: "))
                if cantidad_buscada < 0:
                    print("Cantidad inválida. Inténtelo nuevamente.")
                    continue

                subtotal = int(
                    producto_seleccionado['precio']) * cantidad_buscada

                lista_productos.append({
                    'producto': producto_seleccionado['nombre'],
                    'cantidad': cantidad_buscada,
                    'subtotal': subtotal
                })
                lista_precios.append(subtotal)

                print("Producto agregado al carrito.")

            except ValueError:
                print("Entrada inválida. Inténtelo nuevamente.")
                continue

    if len(lista_productos) > 0:
        print("Carrito de compras:")
        total_compra = sum(lista_precios)
        print(f"Total: ${total_compra}")

        generar_factura(lista_productos, total_compra)
    else:
        print("No se agregaron productos al carrito. La compra ha sido cancelada.")


def generar_factura(lista_productos: list, total_compra: float):
    """
    Genera una factura de compra con los productos seleccionados.

    Args:
        lista_productos (list): Lista de productos seleccionados.
        total_compra (float): Total de la compra.
    """
    factura = "FACTURA DE COMPRA\n"
    factura += "--------------------------------------------------------------------------\n"

    for producto in lista_productos:
        factura += f"Producto: {producto['producto']}\n"
        factura += f"Cantidad: {producto['cantidad']}\n"
        factura += f"Subtotal: ${producto['subtotal']}\n"
        factura += "--------------------------------------------------------------------------\n"

    nombre_archivo = input("Ingrese el nombre para guardar la factura: ")
    if nombre_archivo.strip() == "":
        print("Debe ingresar al menos un caracter para el nombre de la factura. La factura no será generada.")
        return

    nombre_archivo += ".txt"

    with open(nombre_archivo, 'w') as archivo:
        archivo.write(factura)

    print(
        f"La factura se ha guardado correctamente en el archivo: {nombre_archivo}")


# ----------------------------------------------------------------------------------------------------
# 7

def guardar_en_formato_json(lista_insumos: list):
    """
    Guarda los productos de alimento de la lista en un archivo JSON.

    Args:
        lista_insumos (list): Lista de insumos.
    """
    productos_alimento = []
    for insumo in lista_insumos:
        if "Alimento" in insumo["nombre"]:
            productos_alimento.append(insumo)

    if len(productos_alimento) > 0:
        nombre_archivo = "productos_alimento.json"
        with open(nombre_archivo, "w") as archivo:
            json.dump(productos_alimento, archivo, indent=4)
        print(
            f"Se ha generado el archivo JSON con los productos de alimento: {nombre_archivo}")
    else:
        print("No se encontraron productos de alimento.")


# ----------------------------------------------------------------------------------------------------
# 8

def leer_desde_formato_json():
    """
    Lee los productos de alimento desde un archivo JSON y los muestra en la consola.
    """
    nombre_archivo = "productos_alimento.json"

    try:
        with open(nombre_archivo, "r") as archivo:
            productos_alimento = json.load(archivo)

        print("Productos de alimento:")
        for producto in productos_alimento:
            print(f"ID: {producto['id']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Marca: {producto['marca']}")
            print(f"Precio: {producto['precio']}")
            print(f"Características: {producto['caracteristicas']}")
            print("--------------------------------------------------------------------------")

    except FileNotFoundError:
        print("No se encontró el archivo JSON. Primero debe generar el archivo utilizando la opción 7.")


# ----------------------------------------------------------------------------------------------------
# 9

def actualizar_precios(lista_insumos: list):
    """
    Actualiza los precios de los productos de acuerdo a un porcentaje (8.4%) y guarda los productos actualizados en un archivo CSV.

    Args:
        lista_insumos (list): Lista de insumos.

    """
    porcentaje = 8.4

    def actualizar_precio(insumo: dict):
        """
        Actualiza el precio de un insumo según el porcentaje proporcionado.

        Args:
            insumo (dict): Diccionario que contiene los datos del insumo.

        Returns:
            dict: Diccionario con el insumo actualizado.

        """
        insumo['precio'] = round(
            insumo['precio'] + (insumo['precio'] * porcentaje / 100), 2)
        return insumo

    lista_insumos_actualizados = list(map(actualizar_precio, lista_insumos))

    with open('insumos_actualizados.csv', 'w', newline='') as archivo_csv:
        writer = csv.DictWriter(
            archivo_csv, fieldnames=lista_insumos_actualizados[0].keys())
        writer.writeheader()
        writer.writerows(lista_insumos_actualizados)

    print("Los precios se han actualizado correctamente y se han guardado en el archivo 'Insumos.csv'.")
