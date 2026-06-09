from app.ui.helpers import titulo, pausar


def vista_eliminar_libro(service):
    titulo("ELIMINAR LIBRO")
    id_libro = input("  ID del libro a eliminar: ").strip().upper()
    libro = service.eliminar_libro(id_libro)
    if libro:
        print(f"  Libro '{libro.get_titulo()}' eliminado.")
    else:
        print("  !No se encontró un libro con ese ID.")
    pausar()
