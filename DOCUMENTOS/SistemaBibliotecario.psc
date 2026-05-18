
Algoritmo SistemaBibliotecario
	
	Definir autores, libros, socios, prestamos Como Cadena
	Definir contadorAutores, contadorLibros, contadorSocios, contadorPrestamos Como Entero
	Definir opcionMenu Como Cadena
	//Matrices
	Dimensionar autores(101,3), libros(101,6), socios(101,5), prestamos(501,6)
	
	contadorAutores <- 0
	contadorLibros <- 0
	contadorSocios <- 0
	contadorPrestamos <- 0
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
		Leer opcionMenu
		
		Según opcionMenu Hacer
	"1": 
		RegistrarAutor(autores, contadorAutores)
	"2": 
		RegistrarLibro(libros, autores, contadorLibros, contadorAutores)
	"3": 
		RegistrarSocio(socios, contadorSocios)
	"4": 
		GestionarPrestamo(libros, contadorLibros, socios, contadorSocios, prestamos, contadorPrestamos)
	"5": 
		GestionarDevolucion(libros, contadorLibros, socios, contadorSocios, prestamos) //
	"6": 
		PagarMulta(socios, contadorSocios)
	"7": 
		VerInventario(libros, contadorLibros, autores, contadorAutores)
	"8": 
		VerSocios(socios, contadorSocios)
	"9":
		Escribir "Saliendo del sistema... ¡Que tenga un buen día!"
	De Otro Modo:
		Escribir ">>> ERROR: La opción ", opcionMenu, " no es válida"
FinSegún

Si opcionMenu <> "9" Entonces
Escribir ""
Escribir "Presione cualquier tecla para continuar..."
Esperar Tecla
FinSi

Hasta Que opcionMenu = "9"
FinAlgoritmo

// ==========================================
// MÓDULOS DE REGISTRO
// ==========================================

//CREACION DE FUNCION "REGISTRAR AUTORES" esta función registra un autor y le asigna un ID
//de manera autoomatica
Función RegistrarAutor(autores Por Referencia,contAutores Por Referencia)
contAutores <- contAutores+1
Escribir 'Nombre del autor:'
Leer autores[contAutores,2]
autores[contAutores,1]<-'AUT'+ConvertirATexto(contAutores)
Escribir 'Autor registrado con ID: ', autores[contAutores,1]
FinFunción


//  CREACION DE FUNCION REGISTRARLIBRO: Esta función solicita los datos de un nuevo libro (título, 
// autor y stock), le asigna un ID único automáticamente y marca su estado inicial.

Función RegistrarLibro(libros Por Referencia, autores, contLibros Por Referencia, contAutores)
Definir idAutor Como Cadena
contLibros <- contLibros + 1 // Incrementamos primero para usar la posición correcta
Escribir 'Título del libro:'
Leer libros[contLibros, 2]
Escribir 'ID del Autor:'
Leer idAutor
libros[contLibros, 1] <- 'LIB' + ConvertirATexto(contLibros)//asignacion de ID de libro 
libros[contLibros, 3] <- idAutor
Escribir 'Cantidad inicial:'
Leer libros[contLibros, 4]
libros[contLibros, 5] <- 'Disponible'
FinFunción

//CREACION DE FUNCION REGISTRARSOCIO: Registra un nuevo socio en el sistema, generando su ID 
		// único automáticamente e inicializando sus contadores de multas y libros 
		// prestados en cero.
		
		Función RegistrarSocio(socios Por Referencia,contSocio Por Referencia)
		contSocio <- contSocio+1
		Escribir 'Nombre del socio:'
		Leer socios[contSocio,2]
		socios[contSocio,1]<-'SOC'+ConvertirATexto(contSocio)
		socios[contSocio,3]<-'0'//inicializa las multas
		socios[contSocio,4]<-'0' // inicializa los Libros que el cliente posee 
		Escribir '>> Registro exitoso. El ID asignado es: ', socios[contSocio,1] 
FinFunción

// ==========================================
// MÓDULOS DE GESTIÓN 
// ==========================================

//Creación de  funcion:GESTIONARPRESTAMO:Registra un nuevo prestamo,evalua y valida los datos

Función GestionarPrestamo(libros Por Referencia,contLibros,socios Por Referencia,contSocio,prestamos Por Referencia,contPrestamo Por Referencia)
Definir idSocio, idLibro Como Cadena
Definir posicionSocio, posicionLibro, i, stock Como Entero
Escribir '--- PROCESAR PRÉSTAMO ---'
Escribir 'Ingrese ID del Socio:'
Leer idSocio
Escribir 'Ingrese ID del Libro:'
Leer idLibro

posicionSocio <- 0 //Inicializamos las posiciones en 0, lo que significa "no encontrado"
posicionLibro <- 0 // Esto sirve como bandera de control antes de realizar el recorrido


// 1. BUSCAR SOCIO Y LIBRO

//USO DE CICLOS PARA: El programa no sabe donde estan guardados los datos asi que primero debe encontrarlos
//El objetivo es localizar que en la fila PosicionSocio para socio, posicionLibro para libros
//encuentren los datos dentro de las matrices.
Para i<-1 Hasta contSocio Hacer
	Si socios[i,1]=idSocio Entonces // verifica que el id que esta guardado en la columna 1 de la fila socios i,1 es igual 
		posicionSocio <- i // a la que el usuario escribio.
	FinSi
	
FinPara
Para i<-1 Hasta contLibros Hacer
	Si libros[i,1]=idLibro Entonces
		posicionLibro <- i
	FinSi
FinPara


// 2. VALIDACIONES Y SALIDA DE DATOS

Si posicionSocio>0 Y posicionLibro>0 Entonces   // (Si el valor es mayor a 0, significa que el ciclo 'Para' localizó el registro)
	stock <- ConvertirANumero(libros[posicionLibro,4]) // Transformamos el stock de texto a número 
	// para poder realizar operaciones matemáticas (como la resta de stock)
	
	// Verificamos stock, límite de 3 libros y que no tenga multas
	Si stock>0 Y ConvertirANumero(socios[posicionSocio,3])<3 Y socios[posicionSocio,4]='0' Entonces
		// Registrar el préstamo
		contPrestamo <- contPrestamo+1
		prestamos[contPrestamo,1]<-idSocio
		prestamos[contPrestamo,2]<-idLibro
		prestamos[contPrestamo,3]<-'Activo'
		
		// Actualizar matrices: Reduce la cantidad de libros disponibles en la base de datos
		libros[posicionLibro,4]<-ConvertirATexto(stock-1)
		
		// Si después de prestar el stock es 0, cambiar estado
		Si (stock - 1) = 0 Entonces
			libros[posicionLibro, 5] <- "Agotado"
		FinSi
		
		
		// Actualizamos el contador de libros prestados del socio (Columna 3)
		// Primero convertimos a número para sumar +1 y luego regresamos a texto
		socios[posicionSocio,3]<-ConvertirATexto(ConvertirANumero(socios[posicionSocio,3])+1)
		
		// ============================================================
		// SALIDA DE DATOS SOLICITADA
		// ============================================================
		Limpiar Pantalla
		Escribir '**********************************************'
		Escribir '          COMPROBANTE DE PRÉSTAMO             '
		Escribir '**********************************************'
		Escribir 'SOCIO: ', socios[posicionSocio,2]//muesta el nomnbre del socio
		Escribir 'LIBRO: ', libros[posicionLibro,2] // Muestra el titulo del libro
		Escribir '----------------------------------------------' 
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




// Devoluciones

Subproceso GestionarDevolucion(libros Por Referencia, contLibros, socios Por Referencia, contSocio, prestamos Por Referencia)
	Definir idLibro, idSocio Como Texto
	Definir i, j, dias Como Entero
	Definir cant_actual,libros_socio Como Entero
	Definir m, multa_actual Como Real
	Definir encontrado Como Logico
	
	Escribir "--- PROCESAR DEVOLUCIÓN ---"
	Escribir "Ingrese ID del Libro a devolver:"
	Leer idLibro
	Escribir "Ingrese ID del Socio que lo devuelve:" 
	Leer idSocio
	
	encontrado <- Falso
	
	Para i <- 1 Hasta 500 Hacer
		// Validamos ID Libro, ID Socio y que el prestamo este Activo
		Si prestamos[i, 2] = idLibro Y prestamos[i, 1] = idSocio Y prestamos[i, 3] = "Activo" Entonces
			Si encontrado = Falso Entonces 
				encontrado <- Verdadero 
				prestamos[i, 3] <- "Finalizado"
				Escribir "Libro: ", idLibro, " del Socio: ", idSocio, " identificado."
				Escribir "Días totales que tuvo el libro:"
				Leer dias
				
				// Lógica de Multas (Solo si pasa de 7 dias)
				Si dias > 7 Entonces
					m <- (dias - 7) * 0.50//calcula los dias de mora real aplicando la tarifa
					Para j <- 1 Hasta contSocio Hacer //busca en la matriz socios hasta encontrar el socio con el id
						Si socios[j, 1] = idSocio Entonces//que devolvio el libro.
							
							multa_actual <- ConvertirANumero(socios[j, 4]) //Recupera la deuda que el socio ya tenia acumulada
							socios[j, 4] <- ConvertirATexto(multa_actual + m)//Suma la nueva multa al saldo anterior 
							
							Limpiar Pantalla
							Escribir "**********************************************"
							Escribir "         ¡ALERTA DE RETRASO!                 "
							Escribir "**********************************************"
							Escribir "Socio: ", socios[j, 2]
							Escribir "Multa por este libro: $", m
							Escribir "Deuda total ahora: $", socios[j, 4]
							Escribir "----------------------------------------------"
							Escribir "AVISO: El socio debe pagar para prestar de nuevo."
							Escribir "**********************************************"
						FinSi
					FinPara
				Sino
					Escribir ">> Devolución a tiempo. Sin multas."
				FinSi
				
				
				// Actualizar Stock en la matriz de libros
				Para j <- 1 Hasta contLibros Hacer //El sistema busca el libro devuelto en la matriz de libros una por una
					Si libros[j, 1] = idLibro Entonces 
						// Incrementamos el stock numérico
						cant_actual <- ConvertirANumero(libros[j, 4])//Extrae la cantidad de libros que hay  y los convierte a num para poder sumar
						libros[j, 4] <- ConvertirATexto(cant_actual + 1)
						
						// REGLA DE ORO: Si ya hay 1 o más, el estado debe ser Disponible
						Si (cant_actual + 1) > 0 Entonces
							libros[j, 5] <- "Disponible"
						FinSi
					FinSi
				FinPara
				
				Para j <- 1 Hasta contSocio Hacer //Buscamoss el socio en la matriz socios
					Si socios[j, 1] = idSocio Entonces//cuando encontramos al socio actualizamos su cuenta
						libros_socio <- ConvertirANumero(socios[j, 3]) //Obtenemos cuantos libros tiene el socio prestados actualmente
						socios[j, 3] <- ConvertirATexto(libros_socio - 1) //se le resta 1 al total del socio porque ya entrego el libro
						Escribir "Libros restantes del socio: ", socios[j, 3] // le informamos al usuario cuantos libros le quedan al socio
					FinSi
				FinPara
			FinSi
		FinSi
	FinPara
	
	Si encontrado = Falso Entonces
		Escribir ">>> ERROR: No se encontro ese libro prestado a ese socio."
	FinSi
FinSubproceso

//FUNCION PAGO DE MULTAS 

//CREACION DE FUNCION PAGAR MULTAS: Realiza la transaccion de pago de multas: identifica el socio,verifica que tenga deuda y realiza el pago
Función PagarMulta(socios Por Referencia,contSocio)
Definir idSocio Como Cadena
Definir i, posicionSocio Como Entero
Definir monto, deuda Como Real
Escribir 'ID Socio:'
Leer idSocio
posicionSocio <- 0

Para i<-1 Hasta contSocio Hacer //El sistema busca pide el id del socio al uauario
	Si socios[i,1]=idSocio Entonces  //Se usa la variables PSocio como marcador inicial en 0.
		posicionSocio <- i // si encuentra el que el id coincide con la matriz socio permite recordar el socio sin perderlo de vista
	FinSi
FinPara

Si posicionSocio>0 Entonces //Si despues de recorrer la lista  P.Socios sigue siendo 0 significa que el socio no existe
	deuda <- ConvertirANumero(socios[posicionSocio,4]) //Este si evita que el programa  realize calculos a un socio inexistente
	Escribir 'Deuda: $', deuda
	
	Si deuda>0 Entonces
		Escribir 'Monto a pagar:'
		Leer monto
		
		socios[posicionSocio,4]<-ConvertirATexto(deuda-monto) //se toma la deuda,se resta el monto y se guarda el resoltado
		Escribir 'Pago realizado.'
	FinSi
FinSi
FinFunción

//FUNCION PARA VISUALIZAR EL INVENTARIO
Función VerInventario(libros, contLibros, autores, contAutores) //Define la funcion y recibe las matrices necesarias como parametros
Definir i, j Como Entero // crea los contadores  i para recorrer los libros y j para buscar autores
Definir nombreAutor Como Cadena //reserva el espacio en memoria para el nombre que vamos a encontrar

Escribir "======================================================================"
Escribir "ID | TÍTULO  | AUTOR | STOCK | ESTADO"
Escribir "----------------------------------------------------------------------"

Para i <- 1 Hasta contLibros Hacer //recorre 1 por 1 todos los libros
	nombreAutor <- "Desconocido" // Valor por si no se encuentra el ID
	
	// BÚSQUEDA CRUZADA: Buscamos el ID del autor en la matriz de autores
	Para j <- 1 Hasta contAutores Hacer 
		Si autores[j, 1] = libros[i, 3] Entonces //Compara el ID del autor del libro actual con id que esta en la tabla autores
			nombreAutor <- autores[j, 2] // si los ids coinciden tomamos el nombre de la columna 2 y lo guardamos en la variable nombreAutor
		FinSi
	FinPara
	
	// Imprimimos la línea completa con el nombre del autor ya localizado
	Escribir libros[i, 1], " | ", libros[i, 2], " | ", nombreAutor, " | ", libros[i, 4], " | ", libros[i, 5]
FinPara
Escribir "======================================================================"
FinFunción

//FUNCION PARA VER LOS SOCIOS Y SUS HISTORIALES
Función VerSocios(socios, contSocio) //Define la funcion que recibe la matriz  de datos de los socios y el contador de registros
Definir i Como Entero // declara un contador para recorrer la lista
Escribir "ID | NOMBRE | LIBROS | MULTA"
Escribir "--------------------------------"
Para i <- 1 Hasta contSocio Hacer //inicia el recorrido viendo cada socio
	Escribir socios[i,1], " | ", socios[i,2], " | Posee: ", socios[i,3], " | Deuda: $", socios[i,4]
FinPara
FinFunción
