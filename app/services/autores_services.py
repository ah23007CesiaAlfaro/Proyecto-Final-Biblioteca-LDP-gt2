from app.models.autor import Autor

class AutoresServices:
    def __init__(self):
        self._autores = []
        self._id_contador = 1

    # C
    def crear_autor(self, nombre, nacionalidad):
        for autor in self._autores:
            if autor.get_nombre().lower() == nombre.lower():
                return autor, False  # Ya existe
        formato_id = f"AUT{self._id_contador:02d}"
        nuevo_autor = Autor(formato_id, nombre, nacionalidad)
        self._autores.append(nuevo_autor)
        self._id_contador += 1
        return nuevo_autor, True

    # R
    def mostrar_autores(self):
        return self._autores

    # U
    def actualizar_autor(self, id_autor, nuevo_nombre=None, nueva_nacionalidad=None):
        for autor in self._autores:
            if autor.get_id() == id_autor:
                if nuevo_nombre:
                    autor.set_nombre(nuevo_nombre)
                if nueva_nacionalidad:
                    autor.set_nacionalidad(nueva_nacionalidad)
                return autor
        return None

    # D
    def eliminar_autor(self, id_autor):
        for i, autor in enumerate(self._autores):
            if autor.get_id() == id_autor:
                return self._autores.pop(i)
        return None
    