#  Sistema de Gestión Bibliotecaria — LDP GT2

Este proyecto consiste en el desarrollo de un **Sistema de Gestión Bibliotecaria basico**  organizado atraves del modelo en capas, este proyecto consta de la capa model,service y UI, al usar esta 
 **arquitectura limpia orientada a servicios**, hacemos que el programa tenga separación de responsabilades y permita ser eacalable en el futuro.

---

##  Integrantes del Equipo
* **Cesia Mariena Alfaro Hernandez**
* **Gabriel Antonio Call Ortiz**
* **Jefry Odir Brizuela Rivas**

---

Para poder hacer uso de este sistema necesitas tener lo siguiente:
**1. Preparación del Entorno (Tecnologías)**

**Python:** Es el lenguaje base. Descarga la versión más reciente (3.12+) desde python.org. Al instalarlo, asegúrate de marcar la casilla "Add Python to PATH"; esto es crucial para que la terminal reconozca el comando python.

**Visual Studio Code (VS Code):** Es tu editor de código. Descárgalo en code.visualstudio.com. Una vez instalado, abre VS Code y ve a la pestaña de Extensiones (el icono de cuadrados a la izquierda) e instala la extensión de Python (de Microsoft).

**Terminal (CLI):** Puedes usar la terminal integrada de VS Code (Ctrl + Ñ o Ctrl + J). Es donde ejecutaremos los comandos para interactuar con tu sistema.

**2.Ejecución**:Luego de asegurar tus tecnologias,clona este repositorio  y ejecuta el proyecto desde VS-Code, ve a la main  y empieza a interactuar con el programa.


##  Estructura y Arquitectura del Proyecto

**models/ (La estructura):** Esta capa actúa como el molde o plano de tus objetos. Su única función es definir qué datos componen una entidad (como un Libro o un Autor), garantizando que la información esté organizada de forma coherente y protegida mediante el uso de atributos privados.

**services/ (La lógica):** Es el corazón operativo del programa donde reside el conocimiento. Aquí es donde se aplican las reglas de negocio, como validar si un autor existe antes de registrar un libro o gestionar la suma automática del stock, funcionando como un intermediario inteligente que procesa las peticiones antes de tocar los datos.

**ui/ (La presentación):** Es la interfaz directa con el usuario final, encargada exclusivamente de la comunicación. Su rol es capturar las entradas del usuario a través de la consola y presentar los resultados de manera legible, manteniéndose totalmente aislada de la complejidad matemática o lógica de los servicio.


El sistema se organiza bajo el directorio raíz `aps`, estructurado en capas para asegurar que la lógica de negocio, los datos y la interfaz no se mezclen:

```text
├── aps/                  # Carpeta principal de la aplicación (Application)
│   ├── models/           # Definición y persistencia de las estructuras de datos
│   ├── services/         # Lógica de negocio principal (Reglas de préstamo, cálculo de multas)
│   ├── ui/               # Interfaz de Usuario (Menús interactivos, captura de datos por consola)
│   └── test/             # Pruebas unitarias para validar la robustez de los algoritmos
├── documentacion/        # Sistema realizado en  Pseint.
├── .gitignore            # Archivos y cachés excluidos de Git (ej. _pycache_/)
└── README.md             # Explicacion de proyecto.






