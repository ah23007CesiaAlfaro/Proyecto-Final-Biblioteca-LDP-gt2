class Libro:
    def __init__(self, id_libro, titulo, id_autor, stock):
        self._id_libro = id_libro
        self._titulo = titulo
        self._id_autor = id_autor
        self._stock = stock

    def get_id(self):
        return self._id_libro

    def get_titulo(self):
        return self._titulo

    def get_id_autor(self):
        return self._id_autor

    def get_stock(self):
        return self._stock

    def set_titulo(self, nuevo_titulo):
        self._titulo = nuevo_titulo

    def set_stock(self, nuevo_stock):
        self._stock = nuevo_stock
