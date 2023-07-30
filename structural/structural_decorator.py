"""
Structural pattern Decorator

El patrón Decorator es un patrón de diseño estructural que permite agregar funcionalidad adicional a un objeto de manera 
dinámica. Se logra envolviendo el objeto original dentro de objetos decoradores que proporcionan características 
adicionales sin modificar la estructura del objeto original. El Decorator sigue el principio de diseño 
"Abierto/Cerrado", lo que significa que puedes extender la funcionalidad de un objeto sin tener que modificar su código.

Imagina que tienes una clase base Componente que define una operación básica operacion(). Luego, tienes una clase 
ComponenteConcreto que implementa esa operación básica. Ahora, deseas agregar características adicionales a 
ComponenteConcreto, como opciones de decoración.
"""

# Clase base Componente
class Componente:
    def operacion(self):
        pass

# Clase ComponenteConcreto que implementa la operación básica
class ComponenteConcreto(Componente):
    def operacion(self):
        return "Operación básica"

# Clase Decorador
class Decorador(Componente):
    def __init__(self, componente):
        self._componente = componente

    def operacion(self):
        return self._componente.operacion()

# Clases de Decoradores Concretos
class DecoradorA(Decorador):
    def operacion(self):
        return f"Decorador A ({self._componente.operacion()})"

class DecoradorB(Decorador):
    def operacion(self):
        return f"Decorador B ({self._componente.operacion()})"
    
"""
En este ejemplo, tenemos la clase base Componente con un método operacion() que representa la operación básica. Luego, 
tenemos la clase ComponenteConcreto, que es una implementación concreta de Componente.

A continuación, definimos la clase Decorador, que también es una subclase de Componente. El Decorador tiene una 
referencia a un objeto Componente (el objeto que queremos decorar) y reenvía la llamada de operacion() al objeto 
Componente original. Esto se logra mediante el uso de la composición, donde el decorador contiene un componente y agrega 
funcionalidad a su operación.

Luego, creamos dos clases de decoradores concretos: DecoradorA y DecoradorB. Estas clases heredan de Decorador y agregan 
funcionalidad adicional a la operación del componente.

Ahora, podemos usar los decoradores para agregar características a un objeto ComponenteConcreto:
"""
# Crear una instancia de ComponenteConcreto
componente_concreto = ComponenteConcreto()

# Agregar el DecoradorA
componente_decorado_a = DecoradorA(componente_concreto)
print(componente_decorado_a.operacion())
# Output: Decorador A (Operación básica)

# Agregar el DecoradorB
componente_decorado_b = DecoradorB(componente_concreto)
print(componente_decorado_b.operacion())
# Output: Decorador B (Operación básica)

"""
En este ejemplo, hemos agregado el DecoradorA y el DecoradorB al objeto ComponenteConcreto, y cada decorador ha 
proporcionado una funcionalidad adicional sin afectar la estructura del objeto original.

En resumen, el patrón Decorator es útil cuando necesitas agregar funcionalidad a un objeto de manera flexible y 
dinámica, sin tener que modificar su código. Los decoradores te permiten componer funcionalidades y mantener tu código 
limpio y extensible.
"""