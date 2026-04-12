
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

// ==========================================
// MÓDULOS DE REGISTRO
// ==========================================

//CREACION DE FUNCION "REGISTRAR AUTORES" esta función registra un autor y le asigna un ID
//de manera autoomatica
Función RegistrarAutor(autores Por Referencia,cA Por Referencia)
cA <- cA+1
Escribir 'Nombre del autor:'
Leer autores[cA,2]
autores[cA,1]<-'AUT'+ConvertirATexto(cA)
Escribir 'Autor registrado con ID: ', autores[cA,1]
FinFunción

//  CREACION DE FUNCION REGISTRARLIBRO: Esta función solicita los datos de un nuevo libro (título, 
// autor y stock), le asigna un ID único automáticamente y marca su estado inicial.

Función RegistrarLibro(libros Por Referencia, autores, cL Por Referencia, cA)
Definir idA Como Cadena
cL <- cL + 1 // Incrementamos primero para usar la posición correcta
Escribir 'Título del libro:'
Leer libros[cL, 2]
Escribir 'ID del Autor:'
Leer idA
libros[cL, 1] <- 'LIB' + ConvertirATexto(cL)
libros[cL, 3] <- idA
Escribir 'Cantidad inicial:'
Leer libros[cL, 4]
libros[cL, 5] <- 'Disponible'
FinFunción

//CREACION DE FUNCION REGISTRARSOCIO: Registra un nuevo socio en el sistema, generando su ID 
		// único automáticamente e inicializando sus contadores de multas y libros 
		// prestados en cero.
		
		Función RegistrarSocio(socios Por Referencia,cS Por Referencia)
		cS <- cS+1
		Escribir 'Nombre del socio:'
		Leer socios[cS,2]
		socios[cS,1]<-'SOC'+ConvertirATexto(cS)
		socios[cS,3]<-'0'//inicializa las multas
		socios[cS,4]<-'0' // inicializa los Libros poseidos
		Escribir '>> Registro exitoso. El ID asignado es: ', socios[cS,1] 
FinFunción
