def eliminar(service):
    print("\n--- ELIMINAR AUTOR ---")
    id_autor = input("Ingrese el ID del autor a eliminar (ej. AUT01): ")
    eliminado = service.eliminar_autor(id_autor)
    if eliminado:
        print(f"\n¡Autor '{eliminado.get_nombre()}' eliminado correctamente!")
    else:
        print("\n No se encontró ningún autor con ese ID.")
    input("\nPresione Enter para continuar...")