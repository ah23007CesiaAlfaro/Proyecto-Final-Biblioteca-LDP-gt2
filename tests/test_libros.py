import os
import sys
import pytest

# Ajuste dinámico del path: permite que los tests vean la carpeta 'app'
# como si fuera un módulo instalado, facilitando las importaciones.
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))

from app.services.libro_services import LibrosServices
from app.services.autores_services import AutoresServices
from app.models.libro import Libro

# Fixture: Prepara el terreno antes de cada prueba individual
@pytest.fixture
def biblioteca_setup():
    """Crea un entorno limpio con servicios inicializados y un autor base."""
    autores_service = AutoresServices()
    libros_service = LibrosServices(autores_service)
    # Registramos un autor para que los libros tengan un ID válido al que asociarse
    autor_prueba, _ = autores_service.crear_autor("Gabriel Garcia Marquez", "Colombiano")
    
    return {
        "libros_service": libros_service,
        "autores_service": autores_service,
        "autor_prueba": autor_prueba
    }

# --- TESTS DE CREACIÓN (CREATE) ---

def test_crear_libro_exitoso(biblioteca_setup):
    """Verifica que el sistema registra un nuevo libro correctamente con datos válidos."""
    libros_service = biblioteca_setup["libros_service"]
    libro, es_nuevo = libros_service.crear_libro("Cien anos de soledad", "AUT01", 5)
    
    # Comprobamos que el libro fue marcado como nuevo y se creó el objeto
    assert es_nuevo is True
    assert libro is not None
    assert libro.get_titulo() == "Cien anos de soledad"

def test_crear_libro_autor_inexistente(biblioteca_setup):
    """Valida que no se cree un libro si el ID del autor no existe en el sistema."""
    libros_service = biblioteca_setup["libros_service"]
    libro, es_nuevo = libros_service.crear_libro("Libro Huerfano", "AUT99", 3)
    
    # El resultado debe ser nulo porque la validación de integridad falló
    assert libro is None
    assert es_nuevo is False

def test_crear_libro_duplicado_actualiza_stock(biblioteca_setup):
    """Comprueba que en lugar de duplicar, el sistema incremente el stock del libro existente."""
    libros_service = biblioteca_setup["libros_service"]
    libros_service.crear_libro("Don Quijote", "AUT01", 5)
    
    # Intentamos añadir el mismo libro, el sistema debería sumar stock
    libro_repetido, es_nuevo = libros_service.crear_libro("Don Quijote", "AUT01", 3)
    
    assert es_nuevo is False
    assert libro_repetido.get_stock() == 8 # 5 iniciales + 3 nuevos

# --- TESTS DE LECTURA (READ) ---

def test_buscar_libro_por_id_inexistente(biblioteca_setup):
    """Confirma que la búsqueda por ID devuelve None si el libro no existe."""
    libros_service = biblioteca_setup["libros_service"]
    resultado = libros_service.buscar_por_id("LIB99")
    assert resultado is None

# --- TESTS DE ACTUALIZACIÓN (UPDATE) ---

def test_actualizar_libro_exitoso(biblioteca_setup):
    """Verifica que los atributos del libro se modifiquen correctamente al actualizar."""
    libros_service = biblioteca_setup["libros_service"]
    libro_original, _ = libros_service.crear_libro("Harry Potter", "AUT01", 10)
    id_libro = libro_original.get_id()
    
    # Actualizamos título y stock
    libro_actualizado = libros_service.actualizar_libro(id_libro, nuevo_titulo="Harry Potter 2", nuevo_stock=20)
    
    assert libro_actualizado is not None
    assert libro_actualizado.get_titulo() == "Harry Potter 2"
    assert libro_actualizado.get_stock() == 20

def test_actualizar_libro_inexistente(biblioteca_setup):
    """Asegura que intentar actualizar un libro inexistente devuelva None sin errores."""
    libros_service = biblioteca_setup["libros_service"]
    resultado = libros_service.actualizar_libro("LIB_FAKE", nuevo_titulo="No existo")
    assert resultado is None

# --- TESTS DE ELIMINACIÓN (DELETE) ---

def test_eliminar_libro_exitoso(biblioteca_setup):
    """Verifica que el libro se remueva de la lista y ya no sea accesible por búsqueda."""
    libros_service = biblioteca_setup["libros_service"]
    libro_a_borrar, _ = libros_service.crear_libro("Libro Temporal", "AUT01", 1)
    id_a_borrar = libro_a_borrar.get_id()
    
    # Ejecutamos la eliminación
    libro_eliminado = libros_service.eliminar_libro(id_a_borrar)
    
    assert libro_eliminado is not None
    assert libro_eliminado.get_id() == id_a_borrar
    # Verificación final: el libro ya no debería existir en el sistema
    assert libros_service.buscar_por_id(id_a_borrar) is None

def test_eliminar_libro_inexistente(biblioteca_setup):
    """Confirma que eliminar un ID inexistente no rompe el sistema (retorna None)."""
    libros_service = biblioteca_setup["libros_service"]
    resultado = libros_service.eliminar_libro("LIB_NO_EXISTE")
    assert resultado is None