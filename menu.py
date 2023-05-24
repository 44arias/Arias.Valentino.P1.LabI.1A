import os
from nfunctions import *

path = "insumos.csv"
lista_insumos = []

lista_insumos = formatear_csv(path)


# ----------------------------------------------------------------------------------------------------
# Menú

flag_primero = False

while True:
    opcion = menu()
    os.system('cls')
    if opcion == '1':
        flag_primero = True
        mostrar_datos_productos(lista_insumos)
    elif flag_primero:
        if opcion == '2':
            cantidad_por_marca = contar_cantidad_por_marca(
                lista_insumos, 'marca')
            print("Cantidad por marca:")
            for marca, cantidad in cantidad_por_marca:
                print(f"Marca: {marca}")
                print(f"Cantidad: {cantidad}")
                print(
                    "--------------------------------------------------------------------------")
        elif opcion == '3':
            insumos_por_marca = listar_insumos_por_marca(
                lista_insumos, 'marca', 'nombre', 'precio')
            print("Insumos por marca:")
            for marca, nombre, precio in insumos_por_marca:
                print(f"Marca: {marca}")
                print(f"Nombre: {nombre}")
                print(f"Precio: ${precio}")
                print(
                    "--------------------------------------------------------------------------")
        elif opcion == '4':
            lista_caracteristicas = buscar_insumo_por_caracteristica(
                lista_insumos, 'caracteristicas')
            print("Insumos encontrados:")
            mostrar_datos_productos(lista_caracteristicas)
        elif opcion == '5':
            insumos_ordenados = ordenar_insumos(
                lista_insumos, 'marca', 'precio', 'caracteristicas')
            print("Insumos ordenados:")
            for producto in insumos_ordenados:
                id = producto['id']
                nombre = producto['nombre']
                precio = producto['precio']
                marca = producto['marca']
                p_caracteristica = producto['caracteristicas']
                print(f"ID: {id}")
                print(f"Nombre: {nombre}")
                print(f"Precio: ${precio}")
                print(f"Marca: {marca}")
                print(f"Primera Característica: {p_caracteristica}")
                print(
                    "--------------------------------------------------------------------------")
        elif opcion == '6':
            tienda(lista_insumos)
        elif opcion == '7':
            guardar_en_formato_json(lista_insumos)
            print("Datos guardados en formato JSON.")
        elif opcion == '8':
            lista_insumos = leer_desde_formato_json()
            print("Datos cargados desde el archivo JSON.")
        elif opcion == '9':
            actualizar_precios(lista_insumos)
            print("Precios actualizados.")
        elif opcion == '10':
            salir = input("Confirma salida? (s/n): ")
            if salir == 's':
                os.system('cls')
                print("Vuelva pronto!")
                break
            elif salir == 'n':
                continue
            else:
                print("Opción inválida. Por favor, ingrese una opción válida. (s/n): ")
                continue
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")
    elif opcion == '10':
        break
    else:
        print("Debe cargar los datos primeros...")
    os.system('pause')
