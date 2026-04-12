
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

// ==========================================
// MÓDULOS DE GESTIÓN 
// ==========================================
Función GestionarPrestamo(libros Por Referencia,cL,socios Por Referencia,cS,prestamos Por Referencia,cP Por Referencia)
Definir idS, idL Como Cadena
Definir pS, pL, i, stk Como Entero
Escribir '--- PROCESAR PRÉSTAMO ---'
Escribir 'Ingrese ID del Socio:'
Leer idS
Escribir 'Ingrese ID del Libro:'
Leer idL
pS <- 0
pL <- 0
// 1. BUSCAR SOCIO Y LIBRO
Para i<-1 Hasta cS Hacer
	Si socios[i,1]=idS Entonces
		pS <- i
	FinSi
FinPara
Para i<-1 Hasta cL Hacer
	Si libros[i,1]=idL Entonces
		pL <- i
	FinSi
FinPara

// 2. VALIDACIONES Y SALIDA DE DATOS
Si pS>0 Y pL>0 Entonces
	stk <- ConvertirANumero(libros[pL,4])
	// Verificamos stock, límite de 3 libros y que no tenga multas
	Si stk>0 Y ConvertirANumero(socios[pS,3])<3 Y socios[pS,4]='0' Entonces
		// Registrar el préstamo
		cP <- cP+1
		prestamos[cP,1]<-idS
		prestamos[cP,2]<-idL
		prestamos[cP,3]<-'Activo'
		// Actualizar matrices
		libros[pL,4]<-ConvertirATexto(stk-1)
		
		// Si después de prestar el stock es 0, cambiar estado
		Si (stk - 1) = 0 Entonces
			libros[pL, 5] <- "Agotado"
		FinSi
		
		
		socios[pS,3]<-ConvertirATexto(ConvertirANumero(socios[pS,3])+1)
		// ============================================================
		// SALIDA DE DATOS SOLICITADA
		// ============================================================
		Limpiar Pantalla
		Escribir '**********************************************'
		Escribir '          COMPROBANTE DE PRÉSTAMO             '
		Escribir '**********************************************'
		Escribir 'SOCIO: ', socios[pS,2]
		Escribir 'LIBRO: ', libros[pL,2] // Muestra el nombre del socio
		Escribir '----------------------------------------------' // Muestra el título del libro
		Escribir '¡PRÉSTAMO REALIZADO CON ÉXITO!'
		Escribir ''
		Escribir 'AVISO IMPORTANTE:'
		Escribir 'Tiene un plazo de 7 DÍAS para devolver el libro.'
		Escribir 'De lo contrario, se aplicará una multa de $0.50'
		Escribir 'por cada día de retraso.'
		Escribir '**********************************************'
	SiNo
		Escribir '>>> ERROR: El socio tiene multas, alcanzó el límite de 3 libros o no hay stock.'
	FinSi
SiNo
	Escribir '>>> ERROR: ID de Socio o Libro no encontrado.'
FinSi
FinFunción
