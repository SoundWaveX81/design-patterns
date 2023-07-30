"""
Behavioural Pattern Template Method

El patrón Template Method (Método Plantilla) es un patrón de diseño de comportamiento que define el esqueleto de un 
algoritmo en una clase base, pero deja que las subclases implementen algunos de los pasos del algoritmo. En otras 
palabras, el patrón Template Method define la estructura general del algoritmo, pero delega la implementación de ciertos 
detalles a las subclases.

En términos más sencillos, el patrón Template Method permite definir el "cómo" de un algoritmo en una clase base, 
mientras que los detalles específicos de cada paso del algoritmo se implementan en las subclases.

Ejemplo en Python:

Supongamos que tenemos una clase base Receta que representa la receta para preparar un plato de comida. La receta tiene 
pasos comunes para todas las recetas, como "preparar ingredientes", "cocinar" y "servir". Sin embargo, algunos de estos 
pasos pueden variar según el tipo de plato que estemos preparando.
"""

# Clase base: Receta
class Receta:
    def preparar_ingredientes(self):
        raise NotImplementedError()

    def cocinar(self):
        raise NotImplementedError()

    def servir(self):
        raise NotImplementedError()

    def seguir_receta(self):
        self.preparar_ingredientes()
        self.cocinar()
        self.servir()

# Implementación concreta de Receta (Pastel)
class RecetaPastel(Receta):
    def preparar_ingredientes(self):
        print("Preparando los ingredientes para el pastel.")

    def cocinar(self):
        print("Horneando el pastel.")

    def servir(self):
        print("Sirviendo el pastel.")

# Implementación concreta de Receta (Sopa)
class RecetaSopa(Receta):
    def preparar_ingredientes(self):
        print("Preparando los ingredientes para la sopa.")

    def cocinar(self):
        print("Cocinando la sopa.")

    def servir(self):
        print("Sirviendo la sopa.")

# Ejemplo de uso del patrón Template Method
receta_pastel = RecetaPastel()
receta_pastel.seguir_receta()
# Output:
# Preparando los ingredientes para el pastel.
# Horneando el pastel.
# Sirviendo el pastel.

receta_sopa = RecetaSopa()
receta_sopa.seguir_receta()
# Output:
# Preparando los ingredientes para la sopa.
# Cocinando la sopa.
# Sirviendo la sopa.

"""
En este ejemplo, tenemos la clase base Receta, que define el esqueleto del algoritmo con los métodos 
preparar_ingredientes(), cocinar() y servir(), pero deja su implementación a las subclases.

Luego, tenemos dos implementaciones concretas de recetas: RecetaPastel y RecetaSopa, que heredan de la clase base 
Receta. Cada una de estas subclases implementa los métodos específicos para preparar y cocinar su plato respectivo.

Al llamar al método seguir_receta() de una instancia de RecetaPastel, se ejecutan los pasos generales del algoritmo, 
pero como los métodos preparar_ingredientes(), cocinar() y servir() están implementados en la subclase RecetaPastel, se 
ejecutarán los pasos específicos para preparar y hornear un pastel. Lo mismo ocurre con RecetaSopa, que ejecutará los 
pasos específicos para preparar y cocinar una sopa.

En resumen, el patrón Template Method es útil cuando tienes un algoritmo con pasos comunes, pero algunos de esos pasos 
pueden variar según las subclases. Con este patrón, puedes definir la estructura general del algoritmo en una clase 
base, dejando que las subclases implementen los detalles específicos de cada paso. Esto promueve la reutilización del 
código y evita duplicar la lógica común en varias subclases.
"""