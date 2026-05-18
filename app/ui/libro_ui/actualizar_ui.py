def actualizar(service):
    print("\n--- ACTUALIZAR LIBRO ---")
    id_buscado = input("Ingrese el ID del libro a modificar: ")
    
    # Primero buscamos si existe para pedir los nuevos datos
    nuevo_titulo = input("Nuevo título (deje vacío para no cambiar): ")
    
    actualizado = service.actualizar_libro(id_buscado, nuevo_titulo)
    
    if actualizado:
        print(f"\n¡Libro {id_buscado} actualizado correctamente!")
    else:
        print("\n[!] No se encontró el libro o no se pudo actualizar.")
    input("\nPresione Enter para continuar...")
    