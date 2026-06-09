from app.ui.helpers import titulo, pausar


def crear_libro(libros_service, autores_service):
    titulo("REGISTRAR LIBRO")

    # Mostrar autores disponibles
    autores = autores_service.mostrar_autores()
    if not autores:
        print("  ! No hay autores registrados. Registre un autor primero.")
        pausar()
        return

    print("  Autores disponibles:")
    for a in autores:
        print(f"    {a.get_id()} - {a.get_nombre()}")

    id_autor = input("\n  ID del autor: ").strip().upper()
    autor = autores_service.buscar_por_id(id_autor)
    if not autor:
        print("  !No se encontró un autor con ese ID.")
        pausar()
        return

    titulo_libro = input("  Título del libro: ").strip()
    if not titulo_libro:
        print("  !El título no puede estar vacío.")
        pausar()
        return

    try:
        stock = int(input(" Cantidad de ejemplares: ").strip())
        if stock <= 0:
            raise ValueError
    except ValueError:
        print(" ! Ingrese una cantidad válida (número entero mayor a 0).")
        pausar()
        return

    libro, es_nuevo = libros_service.crear_libro(titulo_libro, id_autor, stock)

    if es_nuevo:
        print(f"\n Libro registrado con ID: {libro.get_id()}")
    else:
        print(f"\n El libro ya existía. Stock actualizado a: {libro.get_stock()}")
    pausar()
