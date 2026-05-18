from app.ui.libro_ui.crear_ui import crear
from app.ui.libro_ui.eliminar_ui import eliminar
from app.ui.libro_ui.leer_ui import listar
from app.ui.libro_ui.actualizar_ui import actualizar

def menu_libros(service):
    while True:
     
         print("\n" + "="*30)
         print("MODULO DE LIBROS")
         print ("1.Agregar Libro")
         print ("2.Mostrar Libros")
         print ("3.Actualizar  Libro")
         print ("4.Eliminar Libro")
         print  ("0. Salir")
         print("="*30)
         opcion= input("Seleccionar opcion")

         if opcion=="1":
              crear(service)
         elif opcion=="2":
              listar(service)
         elif opcion=="3":
              actualizar(service)  
             
         elif  opcion=="4":
              eliminar(service)

         elif opcion=="0":
              break
         else: 
              print ("opcion no valida" )   