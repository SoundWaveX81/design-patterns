"""
creational pattern Abstract Factory

El patrón Abstract Factory es un patrón de diseño creacional que proporciona una interfaz para crear familias de objetos 
relacionados sin especificar sus clases concretas. Permite crear objetos de diferentes tipos que pertenecen a una misma 
familia de productos, asegurándose de que estos objetos sean compatibles entre sí.

Imagina que tienes una aplicación que debe funcionar en diferentes sistemas operativos, y cada sistema operativo tiene 
una interfaz de usuario específica (por ejemplo, botones, cuadros de texto). El patrón Abstract Factory nos permite 
crear una interfaz de fábrica abstracta que define métodos para crear botones y cuadros de texto. Luego, cada sistema 
operativo tiene su propia implementación concreta de esta interfaz de fábrica, que crea los botones y cuadros de texto 
compatibles con el sistema.

Ejemplo en Python:

Supongamos que tenemos una aplicación que debe funcionar en dos sistemas operativos: Windows y macOS. Necesitamos crear 
botones y cuadros de texto para cada sistema operativo, pero asegurándonos de que los elementos creados sean compatibles 
con el sistema en el que se ejecuta la aplicación.
"""

# Interfaz de fábrica abstracta para botones y cuadros de texto
class FabricaInterfaz:
    def crear_boton(self):
        pass

    def crear_cuadro_texto(self):
        pass

# Implementación concreta de fábrica para Windows
class FabricaInterfazWindows(FabricaInterfaz):
    def crear_boton(self):
        return BotonWindows()

    def crear_cuadro_texto(self):
        return CuadroTextoWindows()

# Implementación concreta de fábrica para macOS
class FabricaInterfazMacOS(FabricaInterfaz):
    def crear_boton(self):
        return BotonMacOS()

    def crear_cuadro_texto(self):
        return CuadroTextoMacOS()

# Interfaz de botones abstracta
class Boton:
    def pintar(self):
        pass

# Implementación concreta de botón para Windows
class BotonWindows(Boton):
    def pintar(self):
        print("Pintando botón en estilo Windows")

# Implementación concreta de botón para macOS
class BotonMacOS(Boton):
    def pintar(self):
        print("Pintando botón en estilo macOS")

# Interfaz de cuadros de texto abstracta
class CuadroTexto:
    def mostrar(self):
        pass

# Implementación concreta de cuadro de texto para Windows
class CuadroTextoWindows(CuadroTexto):
    def mostrar(self):
        print("Mostrando cuadro de texto en estilo Windows")

# Implementación concreta de cuadro de texto para macOS
class CuadroTextoMacOS(CuadroTexto):
    def mostrar(self):
        print("Mostrando cuadro de texto en estilo macOS")

"""
En este ejemplo, tenemos la interfaz de fábrica abstracta FabricaInterfaz con los métodos crear_boton() y 
crear_cuadro_texto(). Luego, tenemos dos implementaciones concretas de esta interfaz: FabricaInterfazWindows y 
FabricaInterfazMacOS, que crean botones y cuadros de texto específicos para Windows y macOS, respectivamente.

Luego, tenemos las clases abstractas Boton y CuadroTexto, con sus implementaciones concretas para Windows y macOS.

Ahora, podemos utilizar el patrón Abstract Factory para crear los elementos de la interfaz de usuario compatibles con el 
sistema operativo en el que se ejecuta la aplicación:
"""

# Función para interactuar con la fábrica y crear los elementos de la interfaz de usuario
def crear_interfaz(fabrica: FabricaInterfaz) -> tuple(Boton, CuadroTexto):
    boton = fabrica.crear_boton()
    cuadro_texto = fabrica.crear_cuadro_texto()
    return boton, cuadro_texto

# Ejemplo de uso en Windows
fabrica_windows = FabricaInterfazWindows()
boton_windows, cuadro_texto_windows = crear_interfaz(fabrica_windows)
boton_windows.pintar()  # Output: Pintando botón en estilo Windows
cuadro_texto_windows.mostrar()  # Output: Mostrando cuadro de texto en estilo Windows

# Ejemplo de uso en macOS
fabrica_macos = FabricaInterfazMacOS()
boton_macos, cuadro_texto_macos = crear_interfaz(fabrica_macos)
boton_macos.pintar()  # Output: Pintando botón en estilo macOS
cuadro_texto_macos.mostrar()  # Output: Mostrando cuadro de texto en estilo macOS

"""
En este ejemplo, hemos utilizado el patrón Abstract Factory para crear los botones y cuadros de texto específicos para 
Windows y macOS. Al utilizar la fábrica adecuada para cada sistema operativo, aseguramos que los elementos de la 
interfaz de usuario sean compatibles con el sistema en el que se está ejecutando la aplicación.

En resumen, el patrón Abstract Factory es útil cuando necesitas crear familias de objetos relacionados sin especificar 
sus clases concretas. Proporciona una interfaz abstracta para crear objetos, y cada implementación concreta de esta 
interfaz crea objetos compatibles con una determinada familia de productos. Esto permite una mayor flexibilidad y 
extensibilidad en la creación de objetos en tu código.
"""