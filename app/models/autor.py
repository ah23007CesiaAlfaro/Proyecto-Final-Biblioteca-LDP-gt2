class Autor:
    def __init__(self, _id_autor, _nombre, _nacionalidad):
        self._id_autor = _id_autor
        self._nombre = _nombre
        self._nacionalidad = _nacionalidad

    # Getters
    def get_id(self):
        return self._id_autor
    def get_nombre(self):
        return self._nombre
    def get_nacionalidad(self):
        return self._nacionalidad

    # Setters
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    def set_nacionalidad(self, nueva_nacionalidad):
        self._nacionalidad = nueva_nacionalidad