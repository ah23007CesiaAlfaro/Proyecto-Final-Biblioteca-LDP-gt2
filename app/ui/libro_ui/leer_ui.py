from app.ui.helpers import titulo, pausar


def leer_libros(libros_service, autores_service):
    titulo("LISTA DE LIBROS")
    libros = libros_service.mostrar_libros()
    if not libros:
        print("  No hay libros registrados.")
    else:
        print(f"  {'ID':<8} {'Título':<28} {'Autor':<20} {'Stock'}")
        print("  " + "-" * 65)
        for l in libros:
            autor = autores_service.buscar_por_id(l.get_id_autor())
            nombre_autor = autor.get_nombre() if autor else l.get_id_autor()
            print(f"  {l.get_id():<8} {l.get_titulo():<28} {nombre_autor:<20} {l.get_stock()}")
    pausar()
