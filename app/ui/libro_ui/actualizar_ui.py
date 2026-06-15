from app.ui.helpers import titulo, pausar


def actualizar_libro(service):
    titulo("ACTUALIZAR LIBRO")
    id_libro = input("  ID del libro a actualizar: ").strip().upper()
    #Validacion de existencia mediante  el servicio
    libro = service.buscar_por_id(id_libro)
    if not libro:
        print("  ! No se encontró un libro con ese ID.")
        pausar()
        return

    print(f"\n  Libro actual: '{libro.get_titulo()}' | Stock: {libro.get_stock()}")
    #Captura los nuevos datos 
    nuevo_titulo = input("  Nuevo título (ENTER para no cambiar): ").strip()
    nuevo_stock_str = input("  Nuevo stock (ENTER para no cambiar): ").strip()

    nuevo_stock = None
    # Si el usuario escribió algo, intentamos procesarlo.
    #hacemos uso del try-exept como filtro contra datos erroneos
    if nuevo_stock_str:
        try:
            nuevo_stock = int(nuevo_stock_str)
            if nuevo_stock < 0:
                raise ValueError
        except ValueError:
            print("  [!] Stock inválido. No se modificó.")
            nuevo_stock = None

# Enviamos los datos al servicio. 
# # Usamos 'nuevo_titulo or None' para que, si el título está vacío, el servicio no haga cambios.
    service.actualizar_libro(id_libro, nuevo_titulo or None, nuevo_stock)
    print("   Libro actualizado correctamente.")
    pausar()
