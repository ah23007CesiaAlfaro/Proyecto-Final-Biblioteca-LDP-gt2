import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))

from app.services.autores_services import AutoresServices


@pytest.fixture
def autores_setup():
    """
    Inicia el servicio de autores limpio y registra un autor base para cada test.
    """
    autores_service = AutoresServices()
    autor_prueba, _ = autores_service.crear_autor("Gabriel Garcia Marquez", "Colombiano")

    return {
        "autores_service": autores_service,
        "autor_prueba": autor_prueba
    }


# ---------- CREATE ----------

def test_crear_autor_exitoso(autores_setup):
    """1. Prueba que un autor nuevo se registre correctamente en el sistema"""
    autores_service = autores_setup["autores_service"]

    autor, es_nuevo = autores_service.crear_autor("Isabel Allende", "Chilena")

    assert es_nuevo is True
    assert autor is not None
    assert autor.get_id() == "AUT02"
    assert autor.get_nombre() == "Isabel Allende"
    assert autor.get_nacionalidad() == "Chilena"


def test_crear_autor_duplicado_no_se_repite(autores_setup):
    """2. Prueba que NO se duplique un autor si ya existe (mismo nombre)"""
    autores_service = autores_setup["autores_service"]
    autor_prueba = autores_setup["autor_prueba"]

    autor_repetido, es_nuevo = autores_service.crear_autor("Gabriel Garcia Marquez", "Colombiano")

    assert es_nuevo is False
    assert autor_repetido.get_id() == autor_prueba.get_id()
    assert len(autores_service.mostrar_autores()) == 1


def test_crear_autor_duplicado_ignora_mayusculas(autores_setup):
    """3. Prueba que la comparación de nombres no distinga mayúsculas/minúsculas"""
    autores_service = autores_setup["autores_service"]

    autor_repetido, es_nuevo = autores_service.crear_autor("GABRIEL GARCIA MARQUEZ", "Colombiano")

    assert es_nuevo is False
    assert len(autores_service.mostrar_autores()) == 1


# ---------- READ ----------

def test_mostrar_autores_lista_vacia():
    """4. Prueba que mostrar_autores devuelva una lista vacía si no hay autores"""
    autores_service = AutoresServices()

    resultado = autores_service.mostrar_autores()

    assert resultado == []


def test_mostrar_autores_con_registros(autores_setup):
    """5. Prueba que mostrar_autores devuelva todos los autores registrados"""
    autores_service = autores_setup["autores_service"]

    autores_service.crear_autor("Isabel Allende", "Chilena")
    resultado = autores_service.mostrar_autores()

    assert len(resultado) == 2
    assert resultado[0].get_nombre() == "Gabriel Garcia Marquez"
    assert resultado[1].get_nombre() == "Isabel Allende"


# ---------- UPDATE ----------

def test_actualizar_autor_existente_ambos_campos(autores_setup):
    """6. Prueba que se pueda actualizar nombre y nacionalidad de un autor existente"""
    autores_service = autores_setup["autores_service"]
    autor_prueba = autores_setup["autor_prueba"]

    autor_actualizado = autores_service.actualizar_autor(
        autor_prueba.get_id(),
        nuevo_nombre="Gabo",
        nueva_nacionalidad="Mexicano"
    )

    assert autor_actualizado is not None
    assert autor_actualizado.get_nombre() == "Gabo"
    assert autor_actualizado.get_nacionalidad() == "Mexicano"


def test_actualizar_autor_solo_nombre(autores_setup):
    """7. Prueba que se pueda actualizar solo el nombre, dejando la nacionalidad igual"""
    autores_service = autores_setup["autores_service"]
    autor_prueba = autores_setup["autor_prueba"]

    autor_actualizado = autores_service.actualizar_autor(
        autor_prueba.get_id(),
        nuevo_nombre="Gabo"
    )

    assert autor_actualizado.get_nombre() == "Gabo"
    assert autor_actualizado.get_nacionalidad() == "Colombiano"


def test_actualizar_autor_inexistente(autores_setup):
    """8. Prueba el manejo de errores al actualizar un autor que no existe"""
    autores_service = autores_setup["autores_service"]

    resultado = autores_service.actualizar_autor("AUT99", nuevo_nombre="No existe")

    assert resultado is None


# ---------- DELETE ----------

def test_eliminar_autor_existente(autores_setup):
    """9. Prueba que se pueda eliminar un autor existente correctamente"""
    autores_service = autores_setup["autores_service"]
    autor_prueba = autores_setup["autor_prueba"]

    autor_eliminado = autores_service.eliminar_autor(autor_prueba.get_id())

    assert autor_eliminado is not None
    assert autor_eliminado.get_id() == autor_prueba.get_id()
    assert len(autores_service.mostrar_autores()) == 0


def test_eliminar_autor_inexistente(autores_setup):
    """10. Prueba el manejo de errores al eliminar un autor que no existe"""
    autores_service = autores_setup["autores_service"]

    resultado = autores_service.eliminar_autor("AUT99")

    assert resultado is None
    assert len(autores_service.mostrar_autores()) == 1