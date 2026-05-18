from app.ui.socios_ui.crear_ui_soc import crear
from app.ui.socios_ui.eliminar_ui_soc import eliminar
from app.ui.socios_ui.leer_ui_soc import listar
from app.ui.socios_ui.actualizar_ui_soc import actualizar

def menu_socios(service):
    while True:
        print("\n" + "="*30)
        print("MODULO DE SOCIOS")
        print("1. Agregar Socio")
        print("2. Mostrar Socios")
        print("3. Actualizar Socio")
        print("4. Eliminar Socio")
        print("0. Salir")
        print("="*30)
        opcion = input("Seleccionar opcion: ")

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