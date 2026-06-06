from app.ui.helpers import titulo, pausar


def realizar_prestamo(prestamos_service, socios_service, libros_service):
    titulo("REALIZAR PRÉSTAMO")

    id_socio = input("  ID del socio: ").strip().upper()
    socio = socios_service.buscar_por_id(id_socio)
    if not socio:
        print("  ¡No se encontró un socio con ese ID.!")
        pausar()
        return

    id_libro = input("  ID del libro: ").strip().upper()
    libro = libros_service.buscar_por_id(id_libro)
    if not libro:
        print("  ¡No se encontró un libro con ese ID.!")
        pausar()
        return

    exito, resultado = prestamos_service.realizar_prestamo(socio, libro)

    if exito:
        print("\n╔══════════════════════════════════════╗")
        print("  ║          PRÉSTAMO EXITOSO            ║")
        print("  ╚══════════════════════════════════════╝")
        print(f"\n  Socio  : {socio.get_nombre()} ({socio.get_id()})")
        print(f"  Libro  : {libro.get_titulo()} ({libro.get_id()})")
        print(f"  ID Pré.: {resultado}")
        print(f"\n   Debe devolver el libro  en 7 días.")
        print("     Pasado ese plazo generara una  multa de $0.50 por día de retraso.")
    else:
        print(f"\n  Préstamo no autorizado: {resultado}")

    pausar()
