"""
Crational pattern Factory Method

El patrón Factory Method es un patrón de diseño creacional que proporciona una interfaz para crear objetos, pero delega 
la creación de las instancias concretas a las subclases. Esto significa que una clase abstracta define un método (el 
Factory Method) que debe ser implementado por sus subclases para crear objetos específicos. De esta manera, el patrón 
Factory Method permite que una clase delegue la responsabilidad de la creación de objetos a sus subclases, lo que 
proporciona una mayor flexibilidad y extensibilidad en la creación de objetos.

Imagina que tienes una clase Producto y varias subclases que representan diferentes tipos de productos (por ejemplo, 
ProductoA, ProductoB). En lugar de crear directamente instancias de las subclases en tu código, puedes utilizar un 
método de fábrica (Factory Method) en una clase abstracta Creador que permita a las subclases decidir qué tipo de objeto 
Producto crear.

Ejemplo en Python:

Supongamos que tenemos una clase abstracta Animal que define un método hacer_sonido() para los animales, y dos subclases 
concretas Perro y Gato, cada una representando un tipo diferente de animal.
"""

# Clase base (Producto)
class Animal:
    def hacer_sonido(self):
        pass

# Subclase concreta (Producto)
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"

# Subclase concreta (Producto)
class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"

# Clase creadora abstracta (Creator)
class Creador:
    def crear_animal(self):
        pass

# Subclase creadora concreta (Creator)
class CreadorAnimales(Creador):
    def crear_animal(self, tipo_animal: str) -> Animal:
        if tipo_animal == "perro":
            return Perro()
        elif tipo_animal == "gato":
            return Gato()
        else:
            raise ValueError(f"Tipo de animal desconocido: {tipo_animal}")

# Función para interactuar con el Creador y los Productos
def interactuar_con_animal(creador: CreadorAnimales, tipo_animal: str):
    animal = creador.crear_animal(tipo_animal)
    sonido = animal.hacer_sonido()
    print(f"El {tipo_animal} hace: {sonido}")

# Crear un Creador de animales
creador_animales = CreadorAnimales()

# Interactuar con los animales creados por el Creador
interactuar_con_animal(creador_animales, "perro")
# Output: El perro hace: Guau!

interactuar_con_animal(creador_animales, "gato")
# Output: El gato hace: Miau!

"""
En este ejemplo, tenemos la clase abstracta Animal que define un método hacer_sonido() y dos subclases concretas Perro y 
Gato, cada una representando un tipo diferente de animal.

Luego, definimos la clase creadora abstracta Creador, que tiene el Factory Method crear_animal(). Las subclases 
concretas de Creador implementan este Factory Method y deciden qué tipo de objeto Animal crear.

Finalmente, tenemos la función interactuar_con_animal() que toma un creador y un tipo de animal como argumentos y 
utiliza el Factory Method para crear el animal correspondiente. Luego, se muestra el sonido que hace el animal.

Al utilizar el patrón Factory Method, podemos agregar nuevos tipos de animales sin modificar el código existente. 
Simplemente necesitamos crear una nueva subclase de Animal y una subclase correspondiente de Creador que implemente el 
Factory Method para crear ese nuevo tipo de animal.

En resumen, el patrón Factory Method es útil cuando tienes una clase abstracta que necesita crear objetos, pero deseas 
delegar la responsabilidad de la creación a sus subclases. Esto permite una mayor flexibilidad y extensibilidad en la 
creación de objetos en tu código.
"""