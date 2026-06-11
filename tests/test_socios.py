import os
import sys
import pytest

# Aseguramos que Python encuentre la carpeta raíz 'app' desde los tests
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))

from app.services.socios_services import SociosServices

@pytest.fixture
def socios_setup():
    """
    Inicia el servicio de socios limpio.
    Devuelve un diccionario para mantener exactamente la misma estructura que test_libros.py.
    """
    socios_service = SociosServices()
    
    return {
        "socios_service": socios_service
    }


def test_crear_socio_exitoso(socios_setup):
    """1. Prueba que un socio nuevo se registre con el ID y valores correctos"""
    socios_service = socios_setup["socios_service"]
    
    socio = socios_service.crear_socio("Juan Perez")
    
    assert socio is not None
    assert socio.get_nombre() == "Juan Perez"
    assert socio.get_id() == "SOC01"
    assert socio.get_libros_prestados() == 0
    assert socio.get_multas() == 0.0


def test_buscar_socio_por_id(socios_setup):
    """2. Prueba la búsqueda de un socio existente y el manejo de uno inexistente"""
    socios_service = socios_setup["socios_service"]
    
    socios_service.crear_socio("Ana Gomez")
    
    socio_encontrado = socios_service.buscar_por_id("SOC01")
    socio_no_encontrado = socios_service.buscar_por_id("SOC99")
    
    assert socio_encontrado is not None
    assert socio_encontrado.get_nombre() == "Ana Gomez"
    assert socio_no_encontrado is None


def test_actualizar_socio(socios_setup):
    """3. Prueba la actualización del nombre de un socio"""
    socios_service = socios_setup["socios_service"]
    
    socios_service.crear_socio("Carlos Diaz")
    
    socio_actualizado = socios_service.actualizar_socio("SOC01", "Carlos M. Diaz")
    socio_fallido = socios_service.actualizar_socio("SOC99", "Fantasma")
    
    assert socio_actualizado is not None
    assert socio_actualizado.get_nombre() == "Carlos M. Diaz"
    assert socio_fallido is None


def test_eliminar_socio(socios_setup):
    """4. Prueba la eliminación exitosa de un socio del sistema"""
    socios_service = socios_setup["socios_service"]
    
    socios_service.crear_socio("Luis Fernando")
    
    socio_eliminado = socios_service.eliminar_socio("SOC01")
    socio_buscado = socios_service.buscar_por_id("SOC01")
    
    assert socio_eliminado is not None
    assert socio_buscado is None