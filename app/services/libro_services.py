from app.models.libro import Libro

class LibrosServices :
    def __init__(self):
        self._libros=[]
        self._id_contador=1

#FUNCION CREATE(C)
    def crear_libro (self,  titulo,  id_autor, stock, estado='Disponible') :
        for libro in self._libros:
            if libro.get_titulo().lower()==titulo.lower() and libro.get_id_autor()==id_autor:
                nuevo_stock=libro.get_stock()+int(stock)
                libro._stock= nuevo_stock
                return libro,False
            
        formato_id=f"LIB{self._id_contador:02d}"    

        nuevo_libro=Libro(formato_id, titulo,  id_autor, int(stock), estado)
        self._libros.append(nuevo_libro)
        self._id_contador +=1
        return nuevo_libro,True
    
    #FUNCION LEER(R)
    def mostrar_libros(self):
        return  self._libros
    
    #FUNCION ACTUALIZAR (UP)
    
    def actualizar_libro(self,id_libro,nuevo_titulo):
        for libro in self._libros: 
            if libro.get_id()==id_libro:
                libro._titulo=nuevo_titulo
                return libro 
        return None

    #FUNCION ELIMINAR (D)
    def eliminar_libro(self,id_libro):
        for i,libro in enumerate(self._libros):
            if libro.get_id()==id_libro:
                return self._libros.pop(i)
        return None   
      