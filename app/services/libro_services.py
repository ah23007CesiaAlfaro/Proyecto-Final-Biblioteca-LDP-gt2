from app.models.libro import Libro
from app.services.autores_services import AutoresServices

class LibrosServices:
    def __init__(self, autores_service=None):
        self._libros = []
        self._contador = 1
       
        self.autores_service = autores_service if autores_service else AutoresServices()

    def crear_libro(self, titulo, id_autor, stock):
        # Validación: consulta al servicio de autores compartido
        autor = self.autores_service.buscar_por_id(id_autor)
        if not autor:
            return None, False

        # Lógica de actualización si ya existe
        for libro in self._libros:
            if libro.get_titulo().lower() == titulo.lower() and libro.get_id_autor() == id_autor:
                libro.set_stock(libro.get_stock() + int(stock))
                return libro, False
        
        # Lógica de creación si es nuevo
        id_libro = f"LIB{self._contador:02d}"
        nuevo = Libro(id_libro, titulo, id_autor, int(stock))
        self._libros.append(nuevo)
        self._contador += 1
        return nuevo, True

    def mostrar_libros(self):
        return self._libros

    def buscar_por_id(self, id_libro):
        for libro in self._libros:
            if libro.get_id() == id_libro:
                return libro
        return None

    def actualizar_libro(self, id_libro, nuevo_titulo=None, nuevo_stock=None):
        libro = self.buscar_por_id(id_libro)
        if libro:
            if nuevo_titulo:
                libro.set_titulo(nuevo_titulo)
            if nuevo_stock is not None:
                libro.set_stock(int(nuevo_stock))
            return libro
        return None

    def eliminar_libro(self, id_libro):
        for i, libro in enumerate(self._libros):
            if libro.get_id() == id_libro:
                return self._libros.pop(i)
        return None