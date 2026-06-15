from app.ui.helpers import titulo, pausar


def realizar_devolucion(prestamos_service, socios_service, libros_service):
    titulo("REALIZAR DEVOLUCIÓN")

    id_socio = input("  ID del socio: ").strip().upper()
    socio = socios_service.buscar_por_id(id_socio)
    if not socio:
        print("  ¡No se encontró un socio con ese ID!.")
        pausar()
        return

    id_libro = input("  ID del libro a devolver: ").strip().upper()
    libro = libros_service.buscar_por_id(id_libro)
    if not libro:
        print(" ¡No se encontró un libro con ese ID.!")
        pausar()
        return

    try:
        dias = int(input("  ¿Cuántos días tuvo el libro? ").strip())
        if dias < 0:
            raise ValueError
    except ValueError:
        print("  Ingrese un número de días válido.")
        pausar()
        return

    exito, multa, mensaje = prestamos_service.realizar_devolucion(socio, libro, dias)

    if not exito:
        print(f"\n  {mensaje}")
        pausar()
        return

    print(f"\n   Devolución registrada. {mensaje}")

    if multa > 0:
        print("\n ╔══════════════════════════════════════╗")
        print(f"  ║   MULTA GENERADA: ${multa:.2f}       ║")
        print("   ╚══════════════════════════════════════╝")
        print(f"\n  El socio debe pagar ${multa:.2f} antes de realizar un nuevo préstamo.")
    else:
        print("  Sin multa. ¡Gracias por devolver a tiempo!")

    pausar()