
	// ==========================================
	// Modulo 3
	// ==========================================
	Escribir "ID del Socio que solicita:"
	Leer idSocioBusq
	Escribir "ID del Libro a prestar:"
	Leer idLibroBusq
	
	posSocio <- 0
	posLibro <- 0
	
	// Buscar Socio 
	Para i <- 1 Hasta 100 Hacer
		Si socios[i,1] = idSocioBusq Entonces
			posSocio <- i
		FinSi
	FinPara
	
	// Buscar Libro 
	Para i <- 1 Hasta 100 Hacer
		Si libros[i,1] = idLibroBusq Entonces
			posLibro <- i
		FinSi
	FinPara
	
	Si posSocio > 0 Y posLibro > 0 Entonces
		// VALIDACIÓN 
		Si libros[posLibro, 5] = "Disponible" Entonces
			Si ConvertirANumero(socios[posSocio, 3]) < 3 Y socios[posSocio, 4] = "0" Entonces
				
				// CONTROL DE ESTADO 
				prestamos[contadorPrestamos, 1] <- idSocioBusq
				prestamos[contadorPrestamos, 2] <- idLibroBusq
				prestamos[contadorPrestamos, 3] <- "Activo"
				prestamos[contadorPrestamos, 4] <- "0"
				
			    // ACTUALIZAR
				libros[posLibro, 5] <- "Prestado"
				socios[posSocio, 3] <- ConvertirATexto(ConvertirANumero(socios[posSocio, 3]) + 1)
				
				contadorPrestamos <- contadorPrestamos + 1
				Escribir "Préstamo generado con éxito."
			Sino
				Escribir "El socio no cumple los requisitos (Límite de libros o multas pendientes)."
			FinSi
		Sino
			Escribir "El libro no está disponible actualmente."
		FinSi
	Sino
		Escribir "Error: ID de socio o libro no encontrado."
	FinSi
	
	
	// ==========================================
	// PROCESAR DEVOLUCIÓN 
	// ==========================================
	Escribir "Ingrese ID del Libro a devolver:"
	Leer idLibroDev
	
	encontrado <- Falso
	Para i <- 1 Hasta 100 Hacer
		Si prestamos[i, 2] = idLibroDev Y prestamos[i, 3] = "Activo" Entonces
			
			idSocioDev <- prestamos[i, 1]
			prestamos[i, 3] <- "Finalizado"
			
			// Cálculo de Multas
			Escribir "¿Días de retraso? (0 si entregó a tiempo):"
			Leer dias
			Si dias > 0 Entonces
				valorMulta <- dias * 5.0 //cambiar por el valor real
				prestamos[i, 4] <- ConvertirATexto(valorMulta)
				
				// Actualizar multas 
				Para k <- 1 Hasta 100 Hacer
					Si socios[k, 1] = idSocioDev Entonces
						socios[k, 4] <- ConvertirATexto(ConvertirANumero(socios[k, 4]) + valorMulta)
					FinSi
				FinPara
				Escribir "Multa generada: $", valorMulta
			FinSi
			
			// Liberar Libro 
			Para j <- 1 Hasta 100 Hacer
				Si libros[j, 1] = idLibroDev Entonces
					libros[j, 5] <- "Disponible"
				FinSi
			FinPara
			
			// Actualizar Socio 
			Para j <- 1 Hasta 100 Hacer
				Si socios[j, 1] = idSocioDev Entonces
					socios[j, 3] <- ConvertirATexto(ConvertirANumero(socios[j, 3]) - 1)
				FinSi
			FinPara
			
			Escribir "Libro devuelto y sistema actualizado."
			encontrado <- Verdadero
		FinSi
	FinPara
	
	Si No encontrado Entonces Escribir "No existe un préstamo activo para este libro." 
	FinSi
	
	// ==========================================
	// HISTORIAL DE PRÉSTAMOS
	// ==========================================
	
	Escribir "--- HISTORIAL COMPLETO ---"
	Para i <- 1 Hasta contadorPrestamos - 1 Hacer
		Escribir "Socio: ", prestamos[i,1], " | Libro: ", prestamos[i,2], " | Estado: ", prestamos[i,3], " | Multa: $", prestamos[i,4]
FinPara

