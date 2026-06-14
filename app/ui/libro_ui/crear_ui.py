from app.ui.helpers import titulo, pausar

def crear_libro(libros_service, autores_service):
    titulo("REGISTRAR LIBRO")

    # 1. Mostrar autores disponibles
    autores = autores_service.mostrar_autores()
    if not autores:
        print("  ! No hay autores registrados. Registre un autor primero.")
        pausar()
        return

    print("  Autores disponibles:")
    for a in autores:
        print(f"    {a.get_id()} - {a.get_nombre()}")

    # 2. Captura y validación del ID
    id_autor = input("\n  ID del autor: ").strip().upper()
    autor = autores_service.buscar_por_id(id_autor)
    if not autor:
        print("  ! Error: No se encontró un autor con ese ID.")
        pausar()
        return

    # 3. Captura del Título
    titulo_libro = input("  Título del libro: ").strip()
    if not titulo_libro:
        print("  ! Error: El título no puede estar vacío.")
        pausar()
        return

    # 4. Captura del Stock
    try:
        stock = int(input("  Cantidad de ejemplares: ").strip())
        if stock <= 0:
            raise ValueError
    except ValueError:
        print("  ! Error: Ingrese una cantidad válida (número entero mayor a 0).")
        pausar()
        return

    # 5. Llamada al servicio.
    libro, es_nuevo = libros_service.crear_libro(titulo_libro, id_autor, stock)

    # Lógica de salida limpia y correcta
    if libro is None:
        # Esto solo pasará si el servicio falla internamente
        print("   ! Error: No se pudo registrar el libro en el sistema.")
    else:
        if es_nuevo:
            print(f"\n  ¡Libro registrado exitosamente con ID: {libro.get_id()}!")
        else:
            print(f"\n  ¡Libro actualizado! Nuevo stock total: {libro.get_stock()}")
    
    pausar()