def crear(service):
    print("\n" + "=" * 30)
    print("  REGISTRO DE SOCIO")
    print("=" * 30)

    while True:
        nombre = input("Ingrese el nombre del socio: ")
        if nombre.strip():
            break
        print("El nombre no puede estar vacío.")

    # Llamamos al servicio
    nuevo_socio = service.crear_socio(nombre)

    print(f"\n[+] ¡ÉXITO! Nuevo socio registrado con ID: {nuevo_socio.get_id()}")

    input("\nPresione Enter para continuar...")