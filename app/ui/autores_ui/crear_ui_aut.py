def vista_crear_autor(service):
    print("\n" + "="*30)
    print("   REGISTRO DE AUTOR")
    print("="*30)

    while True:
        nombre = input("Ingrese el nombre del autor: ")
        if nombre.strip():
            break
        print("El nombre no puede estar vacío.")

    while True:
        nacionalidad = input("Ingrese la nacionalidad: ")
        if nacionalidad.strip():
            break
        print("La nacionalidad no puede estar vacía.")

    autor_obj, es_nuevo = service.crear_autor(nombre, nacionalidad)
    if es_nuevo:
        print(f"\n¡ÉXITO! Nuevo autor registrado con ID: {autor_obj.get_id()}")
    else:
        print(f"\n AVISO: El autor '{autor_obj.get_nombre()}' ya existe con ID: {autor_obj.get_id()}")

    input("\nPresione Enter para continuar...")