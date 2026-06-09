from app.ui.helpers import titulo, pausar


def actualizar_libro(service):
    titulo("ACTUALIZAR LIBRO")
    id_libro = input("  ID del libro a actualizar: ").strip().upper()
    libro = service.buscar_por_id(id_libro)
    if not libro:
        print("  ! No se encontró un libro con ese ID.")
        pausar()
        return

    print(f"\n  Libro actual: '{libro.get_titulo()}' | Stock: {libro.get_stock()}")
    nuevo_titulo = input("  Nuevo título (ENTER para no cambiar): ").strip()
    nuevo_stock_str = input("  Nuevo stock (ENTER para no cambiar): ").strip()

    nuevo_stock = None
    if nuevo_stock_str:
        try:
            nuevo_stock = int(nuevo_stock_str)
            if nuevo_stock < 0:
                raise ValueError
        except ValueError:
            print("  [!] Stock inválido. No se modificó.")
            nuevo_stock = None

    service.actualizar_libro(id_libro, nuevo_titulo or None, nuevo_stock)
    print("   Libro actualizado correctamente.")
    pausar()
