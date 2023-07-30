"""
Creational pattern Prototype
El patrón Prototype es un patrón de diseño creacional que se utiliza para crear nuevos objetos copiando un prototipo 
existente, en lugar de crearlos desde cero. El objetivo del patrón Prototype es permitir la creación de nuevos objetos 
eficientemente, evitando la duplicación de código y evitando la complejidad de configurar objetos desde cero.

Imagina que tienes una clase Producto que es compleja de crear y configurar con múltiples atributos y configuraciones. 
En lugar de crear una instancia nueva y configurar cada atributo manualmente, puedes utilizar el patrón Prototype para 
clonar un objeto existente (un prototipo) y ajustar solo los atributos que necesitas cambiar.

Ejemplo en Python:

Supongamos que tenemos una clase Producto que representa un objeto complejo con muchos atributos.
"""

import copy

# Clase base: Prototipo (Producto)
class Producto:
    def __init__(self, nombre: str, precio: int, descripcion: str):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

    def clonar(self) -> copy:
        return copy.deepcopy(self)

# Ejemplo de uso del patrón Prototype
producto_prototipo = Producto("Producto básico", 100, "Este es un producto básico")

# Crear una copia del prototipo y ajustar atributos según sea necesario
producto_personalizado = producto_prototipo.clonar()
producto_personalizado.nombre = "Producto personalizado"
producto_personalizado.precio = 150
producto_personalizado.descripcion = "Este es un producto personalizado"

# Mostrar los productos
print(producto_prototipo.nombre, producto_prototipo.precio, producto_prototipo.descripcion)
# Output: Producto básico 100 Este es un producto básico

print(producto_personalizado.nombre, producto_personalizado.precio, producto_personalizado.descripcion)
# Output: Producto personalizado 150 Este es un producto personalizado

"""
En este ejemplo, hemos definido la clase Producto, que es el prototipo que queremos clonar. La clase tiene un método 
clonar() que utiliza la función deepcopy del módulo copy para crear una copia profunda del objeto, incluidos todos sus 
atributos.

Luego, creamos un producto_prototipo, que es una instancia del prototipo original con atributos predeterminados.

A continuación, utilizamos el método clonar() para crear una copia del prototipo, que llamamos producto_personalizado. 
Luego, ajustamos algunos atributos específicos en la copia personalizada.

Como resultado, tenemos dos objetos, producto_prototipo y producto_personalizado, que son similares pero tienen 
atributos diferentes.

En resumen, el patrón Prototype es útil cuando necesitas crear objetos complejos y quieres evitar la duplicación de 
código o la configuración manual de atributos en cada instancia nueva. Clonar un prototipo existente te permite crear 
nuevas instancias eficientemente, personalizando solo los atributos necesarios en cada copia.
"""