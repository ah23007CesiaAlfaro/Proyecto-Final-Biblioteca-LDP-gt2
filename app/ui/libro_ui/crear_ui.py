def crear(service):
    print("\n" + "="*30)
    print("   REGISTRO DE LIBRO")
    print("="*30)

    while True:
        titulo = input("Ingrese el titulo: ")
        if titulo.strip():
            break
        print("El titulo no puede estar vacio.")

    while True:
        id_aut = input("Ingrese el ID del Autor: ")
        if id_aut.strip():
            break
        print("El ID del autor no puede estar vacío.")
        
    while True:
        stock_input = input("Ingrese la cantidad: ")
        if stock_input.isdigit():
            stock = int(stock_input)
            break
        print("El stock debe ser un número entero válido.")

    libro_obj, es_nuevo=service.crear_libro(titulo,id_aut,stock) 
    if es_nuevo:
        print(f"\n[+] ¡ÉXITO! Nuevo libro registrado con ID: {libro_obj.get_id()}")
    else:
        print(f"\n[*] AVISO: El libro ya existía.")
        print(f"    Se han sumado {stock} unidades al stock actual.")
        print(f"    Stock total de '{libro_obj.get_titulo()}': {libro_obj.get_stock()}")

    input("\nPresione Enter para continuar...")
 
