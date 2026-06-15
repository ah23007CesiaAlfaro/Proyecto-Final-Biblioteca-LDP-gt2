def vista_actualizar_autor(service):
    print("\n--- ACTUALIZAR AUTOR ---")
    id_buscado = input("Ingrese el ID del autor a modificar (ej. AUT01): ").strip().upper()

    nuevo_nombre = input("Nuevo nombre (deje vacío para no cambiar): ").strip()
    nueva_nacionalidad = input("Nueva nacionalidad (deje vacío para no cambiar): ").strip()

   
    if not nuevo_nombre and not nueva_nacionalidad:
        print("\n! No se ingresaron cambios. Operación cancelada.")
        input("\nPresione Enter para continuar...")
        return

    # Si el usuario sí escribió algo, procesamos normalmente
    actualizado = service.actualizar_autor(
        id_buscado,
        nuevo_nombre if nuevo_nombre else None,
        nueva_nacionalidad if nueva_nacionalidad else None
    )

    if actualizado:
        print(f"\n¡Autor {id_buscado} actualizado correctamente!")
    else:
        print("\n!No se encontró ningún autor con ese ID.")
    input("\nPresione Enter para continuar...")