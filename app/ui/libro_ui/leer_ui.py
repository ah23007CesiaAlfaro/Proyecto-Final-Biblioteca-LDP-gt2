def listar(service):
    libros = service.mostrar_libros()
    if not libros:
        print("\n[!] No hay libros registrados en el sistema.")
        input("\nPresione Enter para continuar...")
        return

    print("\n" + "="*80)
    print(f"{'ID':<8} | {'Título':<25} | {'Autor':<15} | {'Stock':<8} | {'Estado':<8}")
    print("="*80)
    for l in libros:
        print(f"{l.get_id():<8} | {l.get_titulo():<25} | {l.get_id_autor():<15} | {l.get_stock():<8} | {l.get_estado():<8}")
    print("="*80)
    input("\nPresione Enter para continuar...")