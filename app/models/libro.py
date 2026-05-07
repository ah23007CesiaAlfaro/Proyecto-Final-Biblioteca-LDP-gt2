class Libro:
    def __init__ (self, _id_libro, _titulo,  _id_autor, _stock, _estado ='Disponible' ) :
        self._id_libro = _id_libro
        self._titulo =_titulo
        self._id_autor =_id_autor
        self._stock =_stock
        self._estado =_estado
    
    def get_id(self):
        return self._id_libro
    def get_titulo(self):
        return self._titulo
    def get_id_autor(self):
        return self._id_autor
    def get_stock(self):
        return self._stock
    def get_estado(self):
        return self._estado
    