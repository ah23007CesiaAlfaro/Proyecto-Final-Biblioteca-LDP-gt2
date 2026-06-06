from app.services.autores_services import AutoresServices
from app.services.libro_services import LibrosServices
from app.services.socios_services import SociosServices
from app.services.prestamos_services import PrestamosServices

from app.ui.autores_ui.menu_aut import menu_autores
from app.ui.libro_ui.menu_libro import menu_libros
from app.ui.socios_ui.menu_soc import menu_socios
from app.ui.prestamo_ui.prestamo_ui import realizar_prestamo
from app.ui.prestamo_ui.devolucion_ui import realizar_devolucion
from app.ui.prestamo_ui.pago_multa_ui import pagar_multa


def mostrar_menu():
    # Servicios compartidos entre todos los módulos
    autores_service = AutoresServices()
    libros_service = LibrosServices()
    socios_service = SociosServices()
    prestamos_service = PrestamosServices()

    while True:
        print("\n+" + "=" * 38 + "+")
        print("|      SISTEMA DE BIBLIOTECA           |")
        print("+" + "=" * 38 + "+")
        print("  1. Gestión de Autores")
        print("  2. Gestión de Libros")
        print("  3. Gestión de Socios")
        print("  4. Realizar Préstamo")
        print("  5. Realizar Devolución")
        print("  6. Pago de Multa")
        print("  7. Salir")
        print("+" + "-" * 38 + "+")

        op = input("  Seleccione una opción (1-7): ").strip()

        if op == "1":
            menu_autores(autores_service)
        elif op == "2":
            menu_libros(libros_service, autores_service)
        elif op == "3":
            menu_socios(socios_service)
        elif op == "4":
            realizar_prestamo(prestamos_service, socios_service, libros_service)
        elif op == "5":
            realizar_devolucion(prestamos_service, socios_service, libros_service)
        elif op == "6":
            pagar_multa(prestamos_service, socios_service)
        elif op == "7":
            print("\n  ¡Hasta luego! Cerrando el sistema de biblioteca...\n")
            break
        else:
            print("  [!] Opción no válida. Ingrese un número del 1 al 7.")
