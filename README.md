Sistema de Gestión Bibliotecaria
_____________________________________
Este proyecto consiste en el desarrollo de un Sistema de Gestión Bibliotecaria implementado en PSeInt. El sistema permite administrar de manera eficiente el inventario de libros, el registro de autores, la gestión de socios y el control detallado de préstamos y multas mediante una estructura de datos basada en matrices.

Integrantes
____________________
Cesia Mariena Alfaro Hernandez

Gabriel Antonio Call Ortiz

Jefry Odir Brizuela Rivas

Descripción del Proyecto
_____________________________
El sistema ha sido diseñado bajo un enfoque de arquitectura modular, donde cada funcionalidad crítica reside en subprocesos independientes. Esto garantiza que la lógica de negocio (como el cálculo de multas o la actualización de stock) se ejecute de forma aislada, mejorando la mantenibilidad y escalabilidad del software.

Características Principales
_______________________________
1-Gestión de Inventario: Registro automático de autores y libros con generación de IDs únicos.
2-Control de Préstamos: Validación de disponibilidad de stock, límites de préstamos por socio (máximo 3) y bloqueo por multas pendientes.
3-Cálculo de Multas: Implementación de lógica de retraso (multa de $0.50 por día después de los 7 días de plazo).
4-Búsqueda Relacional: Sistema de "Búsqueda Cruzada" para vincular autores con sus respectivos libros sin redundancia de datos.
5-Persistencia en Memoria: Uso de matrices estructuradas para el almacenamiento de datos durante la ejecución.

Estructura Técnica
____________________________
El código utiliza un paradigma de programación estructurada:

Matrices Globales: Actúan como el repositorio maestro para la persistencia de información (libros, socios, autores, préstamos).

Variables Locales: Utilizadas en cada subproceso para cálculos temporales y contadores, garantizando el encapsulamiento de datos y evitando colisiones.

Conversión de Tipos: Implementación de funciones ConvertirANumero y ConvertirATexto para manipular datos almacenados como cadenas de texto en las matrices.

Instrucciones de Uso
______________________________
Asegúrese de tener instalado PSeInt.

Abra el archivo SistemaBibliotecario.psc en el entorno.

Presione F9 para ejecutar el programa.

Navegue a través del menú principal para realizar las operaciones de registro, gestión de préstamos, devoluciones o consultas de inventario.
