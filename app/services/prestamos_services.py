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

        # DEVOLUCIÓN 
    def realizar_devolucion(self, socio, libro, dias):
        """
        Busca el préstamo activo, lo elimina y aplica multa si corresponde.
        Retorna (exito: bool, multa_generada: float, mensaje: str)
        """
        prestamo = self._buscar_prestamo(socio.get_id(), libro.get_id())
        if not prestamo:
            return False, 0.0, "No se encontró un préstamo activo para ese socio y libro."

        # Eliminar préstamo
        self._prestamos.remove(prestamo)

        # Devolver stock y reducir contador del socio
        libro.set_stock(libro.get_stock() + 1)
        socio.set_libros_prestados(socio.get_libros_prestados() - 1)

        # Calcular multa
        dias_atrasados = int(dias) - DIAS_PERMITIDOS
        if dias_atrasados > 0:
            multa = round(dias_atrasados * MULTA_POR_DIA, 2)
            socio.set_multa(socio.get_multa() + multa)
            return True, multa, f"Devolución con {dias_atrasados} día(s) de retraso."

        return True, 0.0, "Devolución a tiempo. Sin multa."

    


    

     
  