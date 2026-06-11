import os
import sys
import pytest

# Aseguramos que Python encuentre la carpeta raíz 'app' desde los tests
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))

from app.services.prestamos_services import PrestamosServices
from app.services.socios_services import SociosServices
from app.services.libro_services import LibrosServices
from app.services.autores_services import AutoresServices


@pytest.fixture
def prestamos_setup():
    """
    Inicia todos los servicios reales.
    Prepara un Autor, un Libro y un Socio reales para realizar los tests de préstamos.
    """
    autores_service = AutoresServices()
    libros_service = LibrosServices(autores_service)
    socios_service = SociosServices()
    prestamos_service = PrestamosServices()
    
    # 1. Creamos un autor real para poder registrar un libro
    autor_prueba, _ = autores_service.crear_autor("J.R.R. Tolkien", "Britanico")
    
    # 2. Creamos un libro real con stock de 3 usando el autor anterior
    libro_prueba, _ = libros_service.crear_libro("El Senor de los Anillos", autor_prueba.get_id(), 3)
    
    # 3. Creamos un socio real
    socio_prueba = socios_service.crear_socio("Maria Lopez")
    
    return {
        "prestamos_service": prestamos_service,
        "socios_service": socios_service,
        "libros_service": libros_service,
        "autores_service": autores_service,
        "socio_prueba": socio_prueba,
        "libro_prueba": libro_prueba
    }


def test_realizar_prestamo_exitoso(prestamos_setup):
    """1. Prueba que un préstamo válido reduzca el stock y sume libros prestados"""
    prestamos_service = prestamos_setup["prestamos_service"]
    socio = prestamos_setup["socio_prueba"]
    libro = prestamos_setup["libro_prueba"]

    prestamo, mensaje = prestamos_service.realizar_prestamo(socio, libro)

    assert prestamo is not False
    assert prestamo.get_id() == "PRE01"
    assert socio.get_libros_prestados() == 1
    assert libro.get_stock() == 2


def test_realizar_prestamo_con_multa_pendiente(prestamos_setup):
    """2. Prueba que NO se le preste a un socio bloqueado por multas"""
    prestamos_service = prestamos_setup["prestamos_service"]
    socio = prestamos_setup["socio_prueba"]
    libro = prestamos_setup["libro_prueba"]

    # Alteramos el estado del socio real asignándole una multa
    socio.set_multas(1.50)

    resultado, mensaje = prestamos_service.realizar_prestamo(socio, libro)

    assert resultado is False
    assert "multa pendiente" in mensaje


def test_realizar_prestamo_limite_alcanzado(prestamos_setup):
    """3. Prueba la regla de negocio de máximo 3 libros por socio"""
    prestamos_service = prestamos_setup["prestamos_service"]
    socio = prestamos_setup["socio_prueba"]
    libro = prestamos_setup["libro_prueba"]

    # Modificamos el socio real indicando que ya tiene 3 libros
    socio.set_libros_prestados(3)

    resultado, mensaje = prestamos_service.realizar_prestamo(socio, libro)

    assert resultado is False
    assert "límite máximo" in mensaje


def test_realizar_prestamo_sin_stock(prestamos_setup):
    """4. Prueba la validación cuando no quedan ejemplares del libro"""
    prestamos_service = prestamos_setup["prestamos_service"]
    socio = prestamos_setup["socio_prueba"]
    libro = prestamos_setup["libro_prueba"]

    # Agotamos el stock del libro real
    libro.set_stock(0)

    resultado, mensaje = prestamos_service.realizar_prestamo(socio, libro)

    assert resultado is False
    assert "No hay ejemplares disponibles" in mensaje


def test_realizar_devolucion_a_tiempo(prestamos_setup):
    """5. Prueba que devolver antes de 7 días no genere cobros"""
    prestamos_service = prestamos_setup["prestamos_service"]
    socio = prestamos_setup["socio_prueba"]
    libro = prestamos_setup["libro_prueba"]

    # Ejecutamos un préstamo real para luego devolverlo
    prestamos_service.realizar_prestamo(socio, libro)

    # Devolvemos a los 5 días
    exito, multa, mensaje = prestamos_service.realizar_devolucion(socio, libro, dias=5)

    assert exito is True
    assert multa == 0.0
    assert socio.get_libros_prestados() == 0
    assert libro.get_stock() == 3  # El stock vuelve a su estado original (3)


def test_realizar_devolucion_con_retraso(prestamos_setup):
    """6. Prueba el cálculo matemático de días atrasados (0.50 por día extra)"""
    prestamos_service = prestamos_setup["prestamos_service"]
    socio = prestamos_setup["socio_prueba"]
    libro = prestamos_setup["libro_prueba"]

    # Ejecutamos el préstamo
    prestamos_service.realizar_prestamo(socio, libro)

    # Devolvemos a los 10 días (3 días de retraso x 0.50 = 1.50)
    exito, multa, mensaje = prestamos_service.realizar_devolucion(socio, libro, dias=10)

    assert exito is True
    assert multa == 1.50
    assert socio.get_multas() == 1.50


def test_pagar_multa_exitoso(prestamos_setup):
    """7. Prueba que se procese el pago completo de la multa y dé cambio"""
    prestamos_service = prestamos_setup["prestamos_service"]
    socio = prestamos_setup["socio_prueba"]

    # Asignamos una multa de $2 al socio real
    socio.set_multas(2.00)

    # El socio paga con un billete de $5.00
    exito, mensaje = prestamos_service.pagar_multa(socio, 5.00)

    assert exito is True
    assert socio.get_multas() == 0.0
    assert "Cambio: $3.00" in mensaje


def test_pagar_multa_insuficiente(prestamos_setup):
    """8. Prueba que se rechacen pagos parciales"""
    prestamos_service = prestamos_setup["prestamos_service"]
    socio = prestamos_setup["socio_prueba"]

    # Asignamos una multa de $5
    socio.set_multas(5.00)

    # Intenta pagar solo $3.00
    exito, mensaje = prestamos_service.pagar_multa(socio, 3.00)

    assert exito is False
    assert socio.get_multas() == 5.00  # La multa no debió bajar