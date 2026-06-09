import os
import sys
import pytest

# Aseguramos que Python encuentre la carpeta raíz 'app' desde los tests
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))

# Importamos los servicios y el modelo necesarios
from app.services.libro_services import LibrosServices
from app.services.autores_services import AutoresServices
from app.models.libro import Libro


@pytest.fixture
def biblioteca_setup():
    """
    Este fixture reemplaza al antiguo setUp().
    Inicia los servicios limpios y registra un autor base para cada test.
    """
    autores_service = AutoresServices()
    libros_service = LibrosServices(autores_service)

    # Creamos un autor de prueba que generará el ID 'AUT01'
    autor_prueba, _ = autores_service.crear_autor("Gabriel Garcia Marquez", "Colombiano")
    
    # Pasamos los servicios listos a las funciones de test mediante un diccionario
    return {
        "libros_service": libros_service,
        "autores_service": autores_service,
        "autor_prueba": autor_prueba
    }


def test_crear_libro_exitoso(biblioteca_setup):
    """1. Prueba que un libro nuevo se registre correctamente en el sistema"""
    libros_service = biblioteca_setup["libros_service"]

    # Intentamos crear el libro asociándolo al ID 'AUT01'
    libro, es_nuevo = libros_service.crear_libro("Cien anos de soledad", "AUT01", 5)

    # Verificaciones usando el 'assert' nativo de Python
    assert es_nuevo is True
    assert libro is not None
    assert libro.get_titulo() == "Cien anos de soledad"
    assert libro.get_stock() == 5


def test_crear_libro_autor_inexistente(biblioteca_setup):
    """2. Prueba que NO se pueda registrar un libro si el ID del autor no existe"""
    libros_service = biblioteca_setup["libros_service"]
    
    libro, es_nuevo = libros_service.crear_libro("Libro Huerfano", "AUT99", 3)

    assert libro is None
    assert es_nuevo is False


def test_crear_libro_duplicado_actualiza_stock(biblioteca_setup):
    """3. Prueba que si el libro ya existe, se sume al stock en lugar de duplicarse"""
    libros_service = biblioteca_setup["libros_service"]

    # Registramos el libro la primera vez con 5 ejemplares
    libros_service.crear_libro("Don Quijote", "AUT01", 5)

    # Intentamos registrar el mismo libro con 3 ejemplares más
    libro_repetido, es_nuevo = libros_service.crear_libro("Don Quijote", "AUT01", 3)

    # Verificaciones de la regla de negocio
    assert es_nuevo is False
    assert libro_repetido.get_stock() == 8  # 5 + 3 = 8 ejemplares en total


def test_buscar_libro_por_id_inexistente(biblioteca_setup):
    """4. Prueba el manejo de errores al buscar un libro que no existe"""
    libros_service = biblioteca_setup["libros_service"]

    # Buscamos un ID que nadie ha registrado
    resultado = libros_service.buscar_por_id("LIB99")

    # Debe retornar None de forma segura sin romper el programa
    assert resultado is None