from app.ui.helpers import titulo, pausar


def pagar_multa(prestamos_service, socios_service):
    titulo("PAGO DE MULTA")

    id_socio = input("  ID del socio: ").strip().upper()
    socio = socios_service.buscar_por_id(id_socio)
    if not socio:
        print("  ¡ No se encontró un socio con ese ID.!")
        pausar()
        return

    multa = socio.get_multas()  
    if multa == 0:
        print(f"\n  El socio '{socio.get_nombre()}' no tiene multas pendientes.")
        pausar()
        return

    print(f"\n  Socio : {socio.get_nombre()}")
    print(f"  Multa : ${multa:.2f}")

    try:
        monto = float(input("\n  Ingrese el monto a pagar: $").strip())
    except ValueError:
        print("  ¡ Monto inválido.!")
        pausar()
        return

    exito, mensaje = prestamos_service.pagar_multa(socio, monto)

    if exito:
        print(f"\n  {mensaje}")
    else:
        print(f"\n  ! {mensaje}")

    pausar()