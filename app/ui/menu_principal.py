from app.services.libro_services import LibrosServices
from app.ui.libro_ui.menu_libro import menu_libros
from app.ui.socios_ui.menu_soc import menu_socios
from app.services.socios_services import SociosServices
from app.ui.autores_ui.menu_aut import menu_autores
from app.services.autores_services import AutoresServices

def mostrar_menu():
    libros_service = LibrosServices()
    socios_service = SociosServices()
    autores_service = AutoresServices()

    while True:
        print("\n" + "+" + "-"*32 + "+")
        print("| MENÚ PRINCIPAL |")
        print("+" + "-"*32 + "+")
        print("  1. Gestión de Libros")
        print("  2. Gestión de Socios")
        print("  3. Gestión de Autores")
        print("  4. Salir")
        print("+" + "-"*32 + "+")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            menu_libros(libros_service)
        elif opcion == "2":
            menu_socios(socios_service)
        elif opcion == "3":
            menu_autores(autores_service)
        elif opcion == "4":
            print("\nSaliendo del sistema informático...")
            break
        else:
            print("\n[!] Opción no válida.")