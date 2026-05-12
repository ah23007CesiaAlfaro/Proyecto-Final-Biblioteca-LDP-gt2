def listar(service):
    socios = service.mostrar_socios()
    if not socios:
        print("\n[!] No hay socios registrados en el sistema.")
        input("\nPresione Enter para continuar...")
        return

    print("\n" + "=" * 80)
    print(f"{'ID':<8} | {'Nombre':<30} | {'Libros Prestados':<18} | {'Multas ($)':<10}")
    print("=" * 80)

    for s in socios:
        print(f"{s.get_id():<8} | {s.get_nombre():<30} | {s.get_libros_prestados():<18} | {s.get_multas():<10}")

    print("=" * 80)
    input("\nPresione Enter para continuar...")