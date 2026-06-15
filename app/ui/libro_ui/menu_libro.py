from app.ui.helpers import titulo
from app.ui.libro_ui.crear_ui import crear_libro
from app.ui.libro_ui.leer_ui import leer_libros
from app.ui.libro_ui.actualizar_ui import actualizar_libro
from app.ui.libro_ui.eliminar_ui import vista_eliminar_libro 

def menu_libros(libros_service, autores_service):
    while True:
        titulo("GESTIÓN DE LIBROS")
        print("  1. Registrar libro")
        print("  2. Ver libros")
        print("  3. Actualizar libro")
        print("  4. Eliminar libro")
        print("  5. Volver al menú principal")

        op = input("\n  Opción: ").strip()

        if op == "1":
            crear_libro(libros_service, autores_service)
        elif op == "2":
            leer_libros(libros_service, autores_service)
        elif op == "3":
            actualizar_libro(libros_service)
        elif op == "4":
            vista_eliminar_libro(libros_service) 
        elif op == "5":
            break
        else:
            print("  ! Opción no válida.")