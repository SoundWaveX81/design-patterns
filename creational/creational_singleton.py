"""
Creational pattern Singleton
El patrón Singleton es un patrón de diseño creacional que garantiza que una clase tenga solo una instancia y proporciona 
un punto de acceso global a esa instancia. Es útil cuando necesitas asegurarte de que una clase tenga una única 
instancia en todo el programa y que esta instancia sea accesible desde cualquier parte del código.

Imagina que tienes una clase que representa una configuración global de la aplicación. Quieres asegurarte de que solo 
haya una instancia de esta clase en todo el programa y que todas las partes del código puedan acceder y modificar la 
misma instancia de configuración.
"""

class Configuracion:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(Configuracion, cls).__new__(cls)
            cls._instancia.__initialized = False
        return cls._instancia

    def __init__(self):
        if not self.__initialized:
            # Aquí se pueden inicializar los atributos de configuración
            self.opcion1 = None
            self.opcion2 = None
            self.__initialized = True

# Ejemplo de uso del Singleton
configuracion1 = Configuracion()
configuracion1.opcion1 = "valor1"

configuracion2 = Configuracion()
print(configuracion2.opcion1)  # Output: valor1

"""
En este ejemplo, hemos definido la clase Configuracion como un Singleton. El método __new__ es el responsable de 
controlar la creación de instancias. Si la instancia _instancia aún no existe, crea una nueva instancia y la almacena en 
la variable de clase _instancia. De lo contrario, devuelve la instancia existente.

El método __init__ se llama después de que se crea una nueva instancia, pero como queremos asegurarnos de que solo se 
inicialicen los atributos una vez, utilizamos el atributo __initialized para garantizar que la inicialización solo 
ocurra la primera vez que se crea la instancia.

Ahora, cuando creamos múltiples instancias de Configuracion, todas se refieren a la misma instancia única, lo que 
garantiza que todas comparten y acceden a la misma configuración.

En resumen, el patrón Singleton es útil cuando necesitas asegurarte de que una clase tenga solo una instancia y que esta 
instancia sea accesible desde cualquier parte del código. Puede ser utilizado en situaciones donde necesitas compartir 
recursos globales o datos de configuración en una única instancia en todo el programa.
"""