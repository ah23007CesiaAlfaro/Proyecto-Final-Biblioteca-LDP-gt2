Algoritmo SistemaBibliotecarioFinal
	// 1. DIMENSIÓN DE MATRICES
	Definir autores, libros, socios, prestamos Como Cadena
	Dimensionar autores(101,3), libros(101,6), socios(101,5), prestamos(501,6)
	Definir cAutores, cLibros, cSocios, cPrestamos Como Entero
	Definir opcion_menu Como Cadena
	cAutores <- 0
	cLibros <- 0
	cSocios <- 0
	cPrestamos <- 0
	Repetir
		Limpiar Pantalla
		Escribir '========= MENÚ BIBLIOTECA ========='
		Escribir '1. Registrar Autor'
		Escribir '2. Registrar Libro'
		Escribir '3. Registrar Socio'
		Escribir '4. Gestionar Préstamo'
		Escribir '5. Gestionar Devolución'
		Escribir '6. Pagar Multa'
		Escribir '7. Ver Inventario'
		Escribir '8. Ver Socios'
		Escribir '9. Salir'
		Escribir 'Seleccione una opción:'
		Leer opcion_menu
		Según opcion_menu Hacer
	"1": 
		RegistrarAutor(autores, cAutores)
	"2": 
		RegistrarLibro(libros, autores, cLibros, cAutores)
	"3": 
		RegistrarSocio(socios, cSocios)
	"4": 
		GestionarPrestamo(libros, cLibros, socios, cSocios, prestamos, cPrestamos)
	"5": 
		GestionarDevolucion(libros, cLibros, socios, cSocios, prestamos)
	"6": 
		PagarMulta(socios, cSocios)
	"7": 
		VerInventario(libros, cLibros, autores, cAutores)
	"8": 
		VerSocios(socios, cSocios)
	"9":
		Escribir "Saliendo del sistema... ¡Que tenga un buen día!"
	De Otro Modo:
		Escribir ">>> ERROR: La opción ", opcion_menu, " no es válida"
FinSegún

i opcion_menu <> "9" Entonces
Escribir ""
Escribir "Presione cualquier tecla para continuar..."
Esperar Tecla
FinSi

Hasta Que opcion_menu = "9"
FinAlgoritmo
		