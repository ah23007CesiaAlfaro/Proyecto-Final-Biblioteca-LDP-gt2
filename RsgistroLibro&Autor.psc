// FUNCIÓN: RegistrarAutor
Funcion RegistrarAutor(autores Por Referencia, contadorAutores Por Referencia)
	
	Definir nombreAutor Como Caracter
	Definir i Como Entero
	Definir espacioEncontrado Como Logico
	
	// VALIDACIÓN: NO VACÍO
	Repetir
		Escribir "Ingrese el nombre del autor:"
		Leer nombreAutor
	Hasta Que nombreAutor <> ""
	
	espacioEncontrado <- Falso
	i <- 1
	
	Mientras i <= 100 Y espacioEncontrado = Falso Hacer
		
		Si autores[i,1] = "" Entonces
			
			autores[i,1] <- "AUTOR" + ConvertirATexto(contadorAutores)
			autores[i,2] <- nombreAutor
			
			Escribir "Autor registrado:"
			Escribir autores[i,1] + " - " + nombreAutor
			
			contadorAutores <- contadorAutores + 1
			espacioEncontrado <- Verdadero
			
		FinSi
		
		i <- i + 1
		
	FinMientras
	
	Si espacioEncontrado = Falso Entonces
		Escribir "No hay espacio para más autores."
	FinSi
	
FinFuncion


// FUNCIÓN: BuscarAutor
Funcion idAutor <- BuscarAutor(autores)
	
	Definir nombreBuscado, idAutor Como Caracter
	Definir i Como Entero
	Definir encontrado Como Logico
	
	// VALIDACIÓN: NO VACÍO
	Repetir
		Escribir "Ingrese el nombre del autor:"
		Leer nombreBuscado
	Hasta Que nombreBuscado <> ""
	
	encontrado <- Falso
	i <- 1
	
	Mientras i <= 100 Y encontrado = Falso Hacer
		
		Si autores[i,2] = nombreBuscado Entonces
			idAutor <- autores[i,1]
			encontrado <- Verdadero
		FinSi
		
		i <- i + 1
		
	FinMientras
	
	Si encontrado = Falso Entonces
		Escribir "Autor no encontrado."
		idAutor <- ""
	FinSi
	
FinFuncion

// FUNCIÓN: RegistrarLibro
Funcion RegistrarLibro(libros Por Referencia, autores, contadorLibros Por Referencia)
	
	Definir tituloLibro Como Caracter
	Definir cantidadEjemplares, i Como Entero
	Definir idAutor Como Caracter
	Definir espacioEncontrado Como Logico
	
	// VALIDACIÓN: NO VACÍO
	Repetir
		Escribir "Ingrese el título del libro:"
		Leer tituloLibro
	Hasta Que tituloLibro <> ""
	
	idAutor <- BuscarAutor(autores)
	
	Si idAutor <> "" Entonces
		
		// VALIDACIÓN: CANTIDAD CORRECTA
		Repetir
			Escribir "Ingrese la cantidad de ejemplares:"
			Leer cantidadEjemplares
		Hasta Que cantidadEjemplares > 0
		
		espacioEncontrado <- Falso
		i <- 1
		
		Mientras i <= 100 Y espacioEncontrado = Falso Hacer
			
			Si libros[i,1] = "" Entonces
				
				libros[i,1] <- "LIB" + ConvertirATexto(contadorLibros)
				libros[i,2] <- tituloLibro
				libros[i,3] <- idAutor
				libros[i,4] <- ConvertirATexto(cantidadEjemplares)
				libros[i,5] <- "Disponible"
				
				Escribir "Libro registrado:"
				Escribir libros[i,1] + " - " + tituloLibro
				
				contadorLibros <- contadorLibros + 1
				espacioEncontrado <- Verdadero
				
			FinSi
			
			i <- i + 1
			
		FinMientras
		
		Si espacioEncontrado = Falso Entonces
			Escribir "No hay espacio para más libros."
		FinSi
		
	Sino
		Escribir "No se puede registrar el libro sin autor."
	FinSi
	
FinFuncion


// ALGORITMO PRINCIPAL
Algoritmo SistemaBiblioteca
	
	Dimension autores[100,2]
	Dimension libros[100,5]
	
	Definir contadorAutores, contadorLibros Como Entero
	Definir opcion Como Caracter
	
	contadorAutores <- 1
	contadorLibros <- 1
	
	Repetir
		
		Escribir "===== SISTEMA DE BIBLIOTECA ====="
		Escribir "1. Registrar Autor"
		Escribir "2. Registrar Libro"
		Escribir "3. Salir"
		
		// VALIDACIÓN DEL MENÚ
		Repetir
			Leer opcion
		Hasta Que opcion = "1" O opcion = "2" O opcion = "3"
		
		Segun opcion Hacer
			
			"1":
				RegistrarAutor(autores, contadorAutores)
				
			"2":
				RegistrarLibro(libros, autores, contadorLibros)
				
		FinSegun
		
	Hasta Que opcion = "3"
	
	Escribir "Fin del sistema"
	
FinAlgoritmo