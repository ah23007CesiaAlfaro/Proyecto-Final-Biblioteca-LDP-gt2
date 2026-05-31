from app.models.prestamo import prestamo

LIMITE_PRESTAMOS = 3
DIAS_PERMITIDOS = 7
MULTA_POR_DIA = 0.50

class PrestamosServices:
    def __init__(self):
        self._prestamos=[]
        self._contador=1

   #validacion de multa
    def realizar_prestamo(self,socio,libro):
     if socio.get_multa()>0:
        return False, f"El socio tiene una multa pendiente de ${socio.get_multa():.2f}. Debe pagarla antes de realizar otro prestamo."
     
     
       # validacion de Limite de prestamos
     if socio.get_libros_prestados()>= LIMITE_PRESTAMOS:
        return False, f"El socio ya tiene {LIMITE_PRESTAMOS} libros prestados."
     
    # validacion stock disponible
     if libro.get_stock()<=0:
          return False,"No hay ejemplares disponibles de ese libro."
     
     # Registrar préstamo
    id_prestamo = f"PRE{self._contador:02d}"
    nuevo = Prestamo(id_prestamo, socio.get_id(), libro.get_id())
    self._prestamos.append(nuevo)
    self._contador += 1

 # Actualizar stock y contador del socio
    libro.set_stock(libro.get_stock() - 1)
    socio.set_libros_prestados(socio.get_libros_prestados() + 1)

    

     
  