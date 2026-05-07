from app.services.libro_services import LibrosServices
from app.ui.libro_ui.menu_libro import menu_libros

def mostrar_menu():
    libros_service = LibrosServices()
    
    while True:
        print("\n" + "+" + "-"*32 + "+")
        print("| MENÚ PRINCIPAL |")
        print("+" + "-"*32 + "+")
        print("  1. Gestión de Libros")
        print("  2. Funciones Extra")
        print("  3. Salir")
        print("+" + "-"*32 + "+")
        
        opcion = input("Seleccione una opción (1-3): ")

        if opcion == "1":
             menu_libros(libros_service)
        elif opcion == "3":
            print("\nSaliendo del sistema informático...")
            break
        else:
            print("\n[!] Opción no válida.")