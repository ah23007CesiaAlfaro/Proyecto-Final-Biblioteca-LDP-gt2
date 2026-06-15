class Prestamo:
    def __init__(self, id_prestamo, id_socio, id_libro):  # ¡Corregido el __init__ con doble guion!
        self._id_prestamo = id_prestamo
        self._id_socio = id_socio
        self._id_libro = id_libro

    def get_id(self):
        return self._id_prestamo

    def get_id_socio(self):
        return self._id_socio
        
    def get_id_libro(self):
        return self._id_libro