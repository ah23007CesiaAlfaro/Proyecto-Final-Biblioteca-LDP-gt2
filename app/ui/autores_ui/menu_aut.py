from app.ui.autores_ui.crear_ui_aut import vista_crear_autor
from app.ui.autores_ui.eliminar_ui_aut import vista_eliminar_autor
from app.ui.autores_ui.leer_ui_aut import vista_listar_autores
from app.ui.autores_ui.actualizar_ui_aut import vista_actualizar_autor

def menu_autores(service):
    while True:
        print("\n" + "="*30)
        print("   MODULO DE AUTORES")
        print("1. Agregar Autor")
        print("2. Mostrar Autores")
        print("3. Actualizar Autor")
        print("4. Eliminar Autor")
        print("0. Salir")
        print("="*30)
        opcion = input("Seleccionar opción: ")

        if opcion == "1":
            vista_crear_autor(service)
        elif opcion == "2":
            vista_listar_autores(service)
        elif opcion == "3":
            vista_actualizar_autor(service)
        elif opcion == "4":
            vista_eliminar_autor(service)
        elif opcion == "0":
            break
        else:
            print("Opción no válida")