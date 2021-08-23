"""Menu para el programa"""

import helpers
import manager

def loop():
    while True:
        helpers.clear()  #limpia el boofer
        
        print("=======================")
        print("BIENVENIDO AL GESTOR.")
        print("\n")
        print("[1] Listado de Clientes.")
        print("[2] Mostrar Cliente.")
        print("[3] Añadir Cliente.")
        print("[4] Modificar Cliente.")
        print("[5] Borrar Cliente.")
        print("[6] Salir.")

        option= int(input("Seleccione una opcion:\n> "))

        helpers.clear()

        if option == 1:
            print("Listando Clientes...\n")
            manager.show_all()
        if option == 2:
            print("Mostrando cliente...\n")
            manager.find()
        if option == 3:
            print("Añadiendo Cliente...\n")
            manager.agreagar()
        if option == 4:
            print("Modificando Cliente...\n")
            if manager.edit():
                print("El cliente se ha modificado exitosamente.")
            else:
                print("No se ha modificado ningun cliente.")
        if option == 5:
            print("Borrando Cliente... \n")
            if manager.delete():
                print("Cliente borrado exitosamente")
            else:
                print("No se ha borrado a ningun cliente")
        if option == 6:
            print("Saliendo... \n")
            break

        input("\nPresiona ENTER para continuar...")
