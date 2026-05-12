from app.services.socios_services import SociosServices

def actualizar(service):
    print("\n--- ACTUALIZAR SOCIO ---")
    id_buscado = input("Ingrese el ID del socio a modificar: ")

    nuevo_nombre = input("Nuevo nombre (deje vacío para cancelar): ")

    if nuevo_nombre.strip():
        actualizado = service.actualizar_socio(id_buscado, nuevo_nombre)
        if actualizado:
            print(f"\n¡Socio {id_buscado} actualizado correctamente!")
        else:
            print("\n[!] No se encontró el socio o no se pudo actualizar.")
    else:
        print("\nOperación cancelada. No se realizaron cambios.")

    input("\nPresione Enter para continuar...")