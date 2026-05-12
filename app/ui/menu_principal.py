from app.services.libro_services import LibrosServices
from app.ui.libro_ui.menu_libro import menu_libros
from app.ui.socios_ui.menu_soc import menu_socios
from app.services.socios_services import SociosServices
def mostrar_menu():
    libros_service = LibrosServices()
    socios_Services = SociosServices()
    while True:
        print("\n" + "+" + "-"*32 + "+")
        print("| MENÚ PRINCIPAL |")
        print("+" + "-"*32 + "+")
        print("  1. Gestión de Libros")
        print("  2. Gestión de Socios")
        print("  3. Funciones Extra")
        print("  4. Salir")
        print("+" + "-"*32 + "+")
        
        opcion = input("Seleccione una opción (1-3): ")

        if opcion == "1":
             menu_libros(libros_service)
        elif opcion == "2":
             menu_socios(socios_Services)
        elif opcion == "4":
            print("\nSaliendo del sistema informático...")
            break
        else:
            print("\n[!] Opción no válida.")