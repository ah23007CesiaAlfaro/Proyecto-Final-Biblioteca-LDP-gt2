from app.models.socio import Socio

class SociosServices:
    def __init__(self):
        self._socios = []
        self._id_contador = 1

    # C
    def crear_socio(self, nombre):
        formato_id = f"SOC{self._id_contador:02d}"
        nuevo_socio = Socio(formato_id, nombre)
        self._socios.append(nuevo_socio)
        self._id_contador += 1
        return nuevo_socio

    # R
    def mostrar_socios(self):
        return self._socios
  
  
    def buscar_por_id(self, id_socio):
        for socio in self._socios:
            if socio.get_id() == id_socio:
                return socio
        return None

    # U
    def actualizar_socio(self, id_socio, nuevo_nombre):
        socio = self.buscar_por_id(id_socio)
        if socio:
            socio.set_nombre(nuevo_nombre)
            return socio
        return None

    # D
    def eliminar_socio(self, id_socio):
        for i, socio in enumerate(self._socios):
            if socio.get_id() == id_socio:
                return self._socios.pop(i)
        return None