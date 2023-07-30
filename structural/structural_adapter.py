"""
Structural pattern Adapter

El patrón Adapter es un patrón de diseño estructural que nos permite convertir la interfaz de una clase en otra interfaz 
que el cliente espera. En otras palabras, el Adapter actúa como un intermediario entre dos clases que tienen interfaces 
incompatibles y permite que trabajen juntas sin modificar su código original.

Imagina que tienes una clase OldPrinter que tiene un método print_old() que imprime un mensaje utilizando un formato 
antiguo. Luego, tienes una clase NewPrinter con un método print_new() que imprime un mensaje utilizando un formato más 
moderno. Ahora, supongamos que tienes una parte del código que utiliza la clase OldPrinter, pero necesitas utilizar la 
clase NewPrinter en su lugar. Aquí es donde el patrón Adapter entra en juego.

"""

# Clase OldPrinter con una interfaz antigua
class OldPrinter:
    def print_old(self, message):
        print(f"Mensaje antiguo: {message}")

# Clase NewPrinter con una interfaz nueva
class NewPrinter:
    def print_new(self, message):
        print(f"Mensaje nuevo: {message}")

# Clase Adapter que convierte la interfaz de OldPrinter en la de NewPrinter
class PrinterAdapter:
    def __init__(self, new_printer):
        self.new_printer = new_printer

    def print_old(self, message):
        # Llama al método de la clase NewPrinter
        self.new_printer.print_new(message)

# Función para usar el adaptador
def use_printer(printer):
    printer.print_old("Hola, mundo!")

# Crear una instancia de NewPrinter
new_printer = NewPrinter()

# Crear una instancia del adaptador, pasando NewPrinter como parámetro
adapter = PrinterAdapter(new_printer)

# Usar la función que espera una instancia de OldPrinter
use_printer(adapter)
