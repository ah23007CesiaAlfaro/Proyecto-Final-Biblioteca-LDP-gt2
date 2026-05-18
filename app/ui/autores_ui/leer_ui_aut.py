def listar(service):
    autores = service.mostrar_autores()
    if not autores:
        print("\n[!] No hay autores registrados en el sistema.")
        input("\nPresione Enter para continuar...")
        return

    print("\n" + "="*50)
    print(f"{'ID':<8} | {'Nombre':<25} | {'Nacionalidad':<15}")
    print("="*50)
    for a in autores:
        print(f"{a.get_id():<8} | {a.get_nombre():<25} | {a.get_nacionalidad():<15}")
    print("="*50)
    input("\nPresione Enter para continuar...")