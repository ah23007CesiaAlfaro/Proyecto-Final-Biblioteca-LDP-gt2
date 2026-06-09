import sys ,os 
sys.path.insert(0, os.path.join(os.path.dirname(__file__),".."))

import unittest
from app.services.libro_services import LibrosServices

class TestLibros(unittest.TestCase):

    def setUp(self):
        self.service=LibrosServices()

        #PRUEBA FUNCION CREATE
    def test_crear_libro(self):
        libro, nuevo=self.service.crear_libro("Cien años","AUT01",5)
        self.assertTrue(nuevo)
        self.assertAlmostEqual(libro.get_stock(),5)

    def test_libro_duplicado_suma_stock(self):
        self.service.crear_libro("Cien años", "AUT01", 3)
        libro, nuevo = self.service.crear_libro("Cien años", "AUT01", 2)
        self.assertFalse(nuevo)
        self.assertEqual(libro.get_stock(), 5) 

     # PRUEBA FUNCION READ 
    def test_mostrar_libros_vacio(self):
        libros = self.service.mostrar_libros()
        self.assertEqual(len(libros), 0)

    def test_mostrar_libros_con_datos(self):
        self.service.crear_libro("Cien años", "AUT01", 5)
        self.service.crear_libro("El principito", "AUT02", 3)
        libros = self.service.mostrar_libros()
        self.assertEqual(len(libros), 2)

    def test_buscar_por_id_existe(self):
        self.service.crear_libro("Cien años", "AUT01", 5)
        libro = self.service.buscar_por_id("LIB01")
        self.assertIsNotNone(libro)
        self.assertEqual(libro.get_titulo(), "Cien años")

    def test_buscar_por_id_no_existe(self):
        libro = self.service.buscar_por_id("LIB99")
        self.assertIsNone(libro)

    # PRUEBA FUNCION UPDATE 
    def test_actualizar_titulo(self):
        self.service.crear_libro("Titulo viejo", "AUT01", 5)
        libro = self.service.actualizar_libro("LIB01", nuevo_titulo="Titulo nuevo")
        self.assertEqual(libro.get_titulo(), "Titulo nuevo")

    def test_actualizar_stock(self):
        self.service.crear_libro("Cien años", "AUT01", 5)
        libro = self.service.actualizar_libro("LIB01", nuevo_stock=10)
        self.assertEqual(libro.get_stock(), 10)

    def test_actualizar_libro_inexistente(self):
        resultado = self.service.actualizar_libro("LIB99", nuevo_titulo="Algo")
        self.assertIsNone(resultado)

    # PRUEBA FUNCION DELETE 
    def test_eliminar_libro(self):
        self.service.crear_libro("Cien años", "AUT01", 5)
        eliminado = self.service.eliminar_libro("LIB01")
        self.assertIsNotNone(eliminado)
        self.assertIsNone(self.service.buscar_por_id("LIB01"))

    def test_eliminar_libro_inexistente(self):
        resultado = self.service.eliminar_libro("LIB99")
        self.assertIsNone(resultado)


if __name__ == "__main__":
    unittest.main()
 