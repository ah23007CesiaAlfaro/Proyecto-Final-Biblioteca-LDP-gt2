from app.models.prestamo import Prestamo

LIMITE_PRESTAMOS = 3
DIAS_PERMITIDOS = 7
MULTA_POR_DIA = 0.50


class PrestamosServices:
    def __init__(self):
        self._prestamos = []
        self._contador = 1

    #  PRÉSTAMO 
    def realizar_prestamo(self, socio, libro):

        # Validar multa pendiente
        if socio.get_multa() > 0:
            return False, f"El socio tiene una multa pendiente de ${socio.get_multa():.2f}. Debe pagarla antes de pedir prestado."

        # Validar límite de préstamos
        if socio.get_libros_prestados() >= LIMITE_PRESTAMOS:
            return False, f"El socio ya tiene {LIMITE_PRESTAMOS} libros prestados (límite máximo)."

        # Validar stock disponible
        if libro.get_stock() <= 0:
            return False, "No hay ejemplares disponibles de ese libro."

        # Registrar préstamo
        id_prestamo = f"PRE{self._contador:02d}"
        nuevo = Prestamo(id_prestamo, socio.get_id(), libro.get_id())
        self._prestamos.append(nuevo)
        self._contador +=1
    


    

     
  