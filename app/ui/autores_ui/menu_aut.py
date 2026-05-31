from app.ui.autores_ui.crear_ui_aut import crear
from app.ui.autores_ui.eliminar_ui_aut import eliminar
from app.ui.autores_ui.leer_ui_aut import listar
from app.ui.autores_ui.actualizar_ui_aut import actualizar

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
            crear(service)
        elif opcion == "2":
            listar(service)
        elif opcion == "3":
            actualizar(service)
        elif opcion == "4":
            eliminar(service)
        elif opcion == "0":
            break
        else:
            print("Opción no válida")