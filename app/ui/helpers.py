# Definimos una línea decorativa constante para usar en los encabezados.
# Esto crea una barra visual fija de 40 caracteres de ancho (+ 38 guiones + 2 signos +).
LINEA = "+" + "-" * 38 + "+"

def titulo(texto):
    """
    Muestra un título centrado y decorado con líneas arriba y abajo.
    Sirve para organizar visualmente cada sección del programa.
    """
    print(f"\n{LINEA}")
    print(f"  {texto}")
    print(LINEA)

def pausar():
    """
    Detiene la ejecución del programa hasta que el usuario presione ENTER.
    Es vital para que el usuario pueda leer los mensajes antes de que la pantalla se limpie.
    """
    input("\n  Presione ENTER para continuar...")