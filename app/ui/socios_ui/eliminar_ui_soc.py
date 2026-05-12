from app.services.socios_services import SociosServices

def eliminar(service):
    print("\n--- ELIMINAR SOCIO ---")
    id_socio = input("Ingrese el ID del socio a eliminar: ")

    eliminado = service.eliminar_socio(id_socio)

    if eliminado:
        print(f"\n¡Socio '{eliminado.get_nombre()}' eliminado correctamente!")
    else:
        print("\n[!] No se encontró ningún socio con ese ID.")

    input("\nPresione Enter para continuar...")