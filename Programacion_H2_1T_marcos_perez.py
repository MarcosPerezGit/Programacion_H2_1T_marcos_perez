import random

#Funcion para mostrar productos que se pueden comprar
def mostrar_productos():
    print("\nProductos disponibles:")
    print("1. Pan")
    print("2. Leche")
    print("3. Huevos")
    print("4. Macarrones")
    print("5. Atun")
    print("6. Salir")

#Funcion donde el usuario compra los productos
def menu_compras(nombre_usuario, dni):
    print("Bienvenido al menú de compras.")
    
    # Aqui se genera el numero de pedido aleatorio
    numero_pedido = random.randint(1,9999)
    print(f"Tu numero de pedido es: {numero_pedido}")

    while True:
        mostrar_productos() #Por aqui llamamos a la funcion para que imprima el menu de productos disponibles
        opcion = input("Seleccione un producto para comprar (o pulse '6' para terminar): ").strip().lower()

        if opcion == "1":
            realizar_compra(numero_pedido, nombre_usuario, dni, "Pan")
            print("Has comprado Pan.")
        elif opcion == "2":
            realizar_compra(numero_pedido, nombre_usuario, dni, "Leche")
            print("Has comprado Leche.")
        elif opcion == "3":
            realizar_compra(numero_pedido, nombre_usuario, dni, "Huevos")
            print("Has comprado Huevos.")
        elif opcion == "4":
            realizar_compra(numero_pedido, nombre_usuario, dni, "Macarrones")
            print("Has comprado Macarrones.")
        elif opcion == "5":
            realizar_compra(numero_pedido, nombre_usuario, dni, "Atun")
            print("Has comprado Atun.")
        elif opcion == "6":
            print("Compra finalizada.")
            break
        else:
            print("Seleccione una opcion valida.")

    # Aqui le damos la opcion al usuario por si quisiera ver el resumen de su compra
    consultar_opcion = input("¿Desea consultar los detalles de su compra? (si/no): ").strip().lower()
    if consultar_opcion == "si":
        consultar_compra(numero_pedido)
    elif consultar_opcion == "no":
        print("Gracias por la compra. Cerrando sesion...")

#Funcion para realizar la compra
def realizar_compra(numero_pedido, nombre_usuario, dni, producto):
    # Guardamos la compra en el archivo
    with open("compras.txt", "a") as archivo:
        archivo.write(f"{numero_pedido},{nombre_usuario},{dni},{producto}\n")

#Funcion para consultar las compras
def consultar_compra(numero_pedido):
    try:
        with open("compras.txt", "r") as archivo:
            compras_encontradas = True  
            for linea in archivo:
                pedido_id, nombre_usuario, dni, producto = linea.strip().split(",")
                if pedido_id == str(numero_pedido):
                    if compras_encontradas: 
                        print(f"\nDetalles de la compra para el numero de pedido: {pedido_id}")
                        print(f"Nombre de usuario: {nombre_usuario}")
                        print(f"DNI: {dni}")
                        compras_encontradas = False  # Cambiamos a False despues de encontrar un pedido
                    print(f"Producto comprado: {producto}")
            if compras_encontradas:  # Si sigue siendo True, significa que no se encontraron compras
                print("Error, no existen registros.")
    except FileNotFoundError:
        print("El numero de pedido solicitado no existe.")
#Funcion para registrar a los usuarios
def registrar_usuario():
    # Solicitamos al usuario que ingrese su nombre de usuario y DNI
    nombre_usuario = input("Ingrese su nombre de usuario: ").upper()
    dni = input("Ingrese su DNI: ").upper()

    # Abrimos el archivo y lo leemos
    try:
        with open("usuarios.txt", "r") as archivo:
            # Verificamos si el DNI ya está registrado
            for linea in archivo:
                usuario, dni_existente = linea.strip().split(",")
                if dni == dni_existente and nombre_usuario  !=usuario:
                    print("El DNI ya está registrado. Por favor, ingrese otro DNI diferente.")
                    return
                elif dni == dni_existente:
                    print("Has iniciado sesion. Accediendo al menu de compras...")
                    menu_compras(usuario, dni)  # Llamamos al menu de compras
                    return  # Si el DNI esta registrado, salimos de la funcion
    except FileNotFoundError:
        # Si el archivo no existe, creamos un archivo vacío
        with open("usuarios.txt", "w") as archivo:
            pass  # Creamos el archivo vacio

    # Si el DNI no está registrado, guardamos al nuevo usuario
    with open("usuarios.txt", "a") as archivo:
        archivo.write(f"{nombre_usuario},{dni}\n")
    
    print("Te has registrado!")
#Funcion que muestra el menu principal
def menu_principal():
    while True:
        print("\nMenu Principal:")
        print("1. Iniciar sesión")
        print("2. Consultar número de pedido")
        print("3. Salir")
        
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            numero_pedido_consulta = input("Por favor, ingrese un numero de pedido: ")
            consultar_compra(numero_pedido_consulta)
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Seleccione una opcion valida.")

# Llamamos a la funcion del menu principal para que ejecute el programa
menu_principal()