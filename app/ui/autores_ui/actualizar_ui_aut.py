def actualizar(service):
    print("\n--- ACTUALIZAR AUTOR ---")
    id_buscado = input("Ingrese el ID del autor a modificar (ej. AUT01): ")

    nuevo_nombre = input("Nuevo nombre (deje vacío para no cambiar): ")
    nueva_nacionalidad = input("Nueva nacionalidad (deje vacío para no cambiar): ")

    actualizado = service.actualizar_autor(
        id_buscado,
        nuevo_nombre if nuevo_nombre.strip() else None,
        nueva_nacionalidad if nueva_nacionalidad.strip() else None
    )

    if actualizado:
        print(f"\n¡Autor {id_buscado} actualizado correctamente!")
    else:
        print("\n[!] No se encontró ningún autor con ese ID.")
    input("\nPresione Enter para continuar...")