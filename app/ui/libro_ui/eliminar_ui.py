def eliminar(service):
    print("\n--- ELIMINAR LIBRO ---")
    id_libro = input("Ingrese el ID del libro a eliminar (ej. LIB01): ")
    eliminado = service.eliminar_libro(id_libro)
    if eliminado:
        print(f"\n¡Libro '{eliminado.get_titulo()}' eliminado correctamente!")
    else:
        print("\n[!] No se encontró ningún libro con ese ID.")
    input("\nPresione Enter para continuar...")