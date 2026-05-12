class Socio:
    def __init__(self, _id_socio, _nombre, _libros_prestados=0, _multas=0.0):
        self._id_socio = _id_socio
        self._nombre = _nombre
        self._libros_prestados = _libros_prestados
        self._multas = _multas

    # Getter
    def get_id(self):
        return self._id_socio

    def get_nombre(self):
        return self._nombre

    def get_libros_prestados(self):
        return self._libros_prestados

    def get_multas(self):
        return self._multas

    # Setter
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def set_libros_prestados(self, cantidad):
        self._libros_prestados = cantidad

    def set_multas(self, monto):
        self._multas = monto