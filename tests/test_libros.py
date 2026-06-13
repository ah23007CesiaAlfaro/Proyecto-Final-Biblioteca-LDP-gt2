import os
import sys
import pytest

# Aseguramos que Python encuentre la carpeta raíz 'app' desde los tests
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))

from app.services.libro_services import LibrosServices
from app.services.autores_services import AutoresServices
from app.models.libro import Libro

@pytest.fixture
def biblioteca_setup():
    """Configura los servicios y registra un autor base para cada test."""
    autores_service = AutoresServices()
    libros_service = LibrosServices(autores_service)
    autor_prueba, _ = autores_service.crear_autor("Gabriel Garcia Marquez", "Colombiano")
    
    return {
        "libros_service": libros_service,
        "autores_service": autores_service,
        "autor_prueba": autor_prueba
    }

# --- TESTS DE CREACIÓN (CREATE) ---

def test_crear_libro_exitoso(biblioteca_setup):
    libros_service = biblioteca_setup["libros_service"]
    libro, es_nuevo = libros_service.crear_libro("Cien anos de soledad", "AUT01", 5)
    assert es_nuevo is True
    assert libro is not None
    assert libro.get_titulo() == "Cien anos de soledad"

def test_crear_libro_autor_inexistente(biblioteca_setup):
    libros_service = biblioteca_setup["libros_service"]
    libro, es_nuevo = libros_service.crear_libro("Libro Huerfano", "AUT99", 3)
    assert libro is None
    assert es_nuevo is False

def test_crear_libro_duplicado_actualiza_stock(biblioteca_setup):
    libros_service = biblioteca_setup["libros_service"]
    libros_service.crear_libro("Don Quijote", "AUT01", 5)
    libro_repetido, es_nuevo = libros_service.crear_libro("Don Quijote", "AUT01", 3)
    assert es_nuevo is False
    assert libro_repetido.get_stock() == 8

# --- TESTS DE LECTURA (READ) ---

def test_buscar_libro_por_id_inexistente(biblioteca_setup):
    libros_service = biblioteca_setup["libros_service"]
    resultado = libros_service.buscar_por_id("LIB99")
    assert resultado is None

# --- TESTS DE ACTUALIZACIÓN (UPDATE) ---

def test_actualizar_libro_exitoso(biblioteca_setup):
    libros_service = biblioteca_setup["libros_service"]
    libro_original, _ = libros_service.crear_libro("Harry Potter", "AUT01", 10)
    id_libro = libro_original.get_id()
    
    libro_actualizado = libros_service.actualizar_libro(id_libro, nuevo_titulo="Harry Potter 2", nuevo_stock=20)
    
    assert libro_actualizado is not None
    assert libro_actualizado.get_titulo() == "Harry Potter 2"
    assert libro_actualizado.get_stock() == 20

def test_actualizar_libro_inexistente(biblioteca_setup):
    libros_service = biblioteca_setup["libros_service"]
    resultado = libros_service.actualizar_libro("LIB_FAKE", nuevo_titulo="No existo")
    assert resultado is None

# --- TESTS DE ELIMINACIÓN (DELETE) ---

def test_eliminar_libro_exitoso(biblioteca_setup):
    libros_service = biblioteca_setup["libros_service"]
    libro_a_borrar, _ = libros_service.crear_libro("Libro Temporal", "AUT01", 1)
    id_a_borrar = libro_a_borrar.get_id()
    
    libro_eliminado = libros_service.eliminar_libro(id_a_borrar)
    
    assert libro_eliminado is not None
    assert libro_eliminado.get_id() == id_a_borrar
    assert libros_service.buscar_por_id(id_a_borrar) is None

def test_eliminar_libro_inexistente(biblioteca_setup):
    libros_service = biblioteca_setup["libros_service"]
    resultado = libros_service.eliminar_libro("LIB_NO_EXISTE")
    assert resultado is None