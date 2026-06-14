#  Sistema de Gestión Bibliotecaria — LDP GT2

Este proyecto consiste en el desarrollo de un **Sistema de Gestión Bibliotecaria** avanzado, migrado y optimizado en **Python**. El sistema permite administrar de manera eficiente el inventario de libros, el registro de autores, la gestión de socios y el control detallado de préstamos y multas. 

A diferencia de las versiones iniciales, esta implementación en Python adopta una **arquitectura limpia orientada a servicios**, garantizando la separación de responsabilidades, la escalabilidad del código y la facilidad para realizar pruebas automatizadas.

---

##  Integrantes del Equipo
* **Cesia Mariena Alfaro Hernandez**
* **Gabriel Antonio Call Ortiz**
* **Jefry Odir Brizuela Rivas**

---

##  Estructura y Arquitectura del Proyecto

El sistema se organiza bajo el directorio raíz `aps`, estructurado en capas para asegurar que la lógica de negocio, los datos y la interfaz no se mezclen:

```text
├── aps/                  # Carpeta principal de la aplicación (Application)
│   ├── models/           # Definición y persistencia de las estructuras de datos (Matrices/Clases)
│   ├── services/         # Lógica de negocio principal (Reglas de préstamo, cálculo de multas)
│   ├── ui/               # Interfaz de Usuario (Menús interactivos, captura de datos por consola)
│   └── test/             # Pruebas unitarias para validar la robustez de los algoritmos
├── documentacion/        # Sistema realizado en  Pseint.
├── .gitignore            # Archivos y cachés excluidos de Git (ej. __pycache__/)
└── README.md             # Explicacion de proyecto.
