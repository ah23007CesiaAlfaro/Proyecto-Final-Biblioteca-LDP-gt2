Algoritmo SistemaBiblioteca
	
	
	// 1. DEFINICION DE VARIABLES
	
	Definir menu_seleccion, i Como Entero
	Definir contador_libros, contador_socios, contador_prestamos Como Entero
	Definir id_libro_buscar, id_socio_buscar Como Texto
	Definir dia_actual Como Entero
	
	// Matrices: 
	// Libros: [1:ID, 2:Titulo, 3:Autor, 4:Fecha_Ing, 5:Stock, 6:Estado]
	// Socios: [1:ID, 2:Nombre, 3:Libros_Poseidos, 4:Multa]
	
	Definir libros, socios Como Texto
	Dimension libros[101, 7], socios[101, 5]
	
	contador_libros <- 0
	contador_socios<- 0
	menu_seleccion <- 0
	
	// 2.MENU PRINCIPAL
	
	Repetir
		Limpiar Pantalla
		Escribir "=========================================="
		Escribir "       SISTEMA DE GESTIÓN DE BIBLIOTECA"
		Escribir "=========================================="
		Escribir "1. Registrar nuevo libro (Completo)"
		Escribir "2. Registrar nuevo socio"
		Escribir "3. Realizar prestamo"
		Escribir "4. Devolver libro"
		Escribir "5. Ver Inventario Detallado"
		Escribir "6. Ver Lista de Socios"
		Escribir "7. Salir"
		Escribir "=========================================="
		Leer menu_seleccion
		
		Segun menu_seleccion Hacer
			1:
			2:
			3:
			4:
			5:
			6:
			
		FinSegun
		Si menu_seleccion <> 7 Entonces
			Escribir "Presione una tecla para continuar..."
			Esperar Tecla
		FinSi
		
	Hasta Que menu_seleccion =7
	
	
	
FinAlgoritmo
