"""
behavioural pattern Strategy
El patrón Strategy es un patrón de diseño de comportamiento que permite definir una familia de algoritmos 
intercambiables y encapsularlos en clases separadas. Los algoritmos son similares pero pueden variar en su 
implementación. Con el patrón Strategy, el cliente puede elegir y cambiar dinámicamente el algoritmo que debe utilizar 
sin afectar al contexto que lo utiliza.

Imagina que tienes una clase que realiza cierta operación y esta operación puede ser realizada de diferentes maneras. En 
lugar de tener múltiples condicionales en el código para cada variante del algoritmo, puedes utilizar el patrón Strategy 
para encapsular cada variante en una clase diferente y permitir que el cliente elija el algoritmo deseado en tiempo de 
ejecución.

Ejemplo en Python:

Supongamos que tenemos una clase Ordenamiento que realiza el proceso de ordenar una lista de números. Queremos utilizar 
el patrón Strategy para poder ordenar la lista de diferentes maneras, como orden ascendente o descendente, sin modificar 
la clase Ordenamiento.
"""

# Interface Estrategia (Strategy)
class EstrategiaOrdenamiento:
    def ordenar(self, lista):
        pass

# Implementación concreta de Estrategia (Strategy)
class EstrategiaOrdenAscendente(EstrategiaOrdenamiento):
    def ordenar(self, lista):
        return sorted(lista)

# Implementación concreta de Estrategia (Strategy)
class EstrategiaOrdenDescendente(EstrategiaOrdenamiento):
    def ordenar(self, lista):
        return sorted(lista, reverse=True)

# Contexto (Context)
class Ordenamiento:
    def __init__(self, estrategia):
        self.estrategia = estrategia

    def establecer_estrategia(self, estrategia):
        self.estrategia = estrategia

    def ordenar_lista(self, lista):
        return self.estrategia.ordenar(lista)

# Ejemplo de uso del patrón Strategy
lista_numeros = [5, 2, 8, 1, 9]

# Ordenamiento ascendente
estrategia_ascendente = EstrategiaOrdenAscendente()
ordenamiento = Ordenamiento(estrategia_ascendente)
resultado_ascendente = ordenamiento.ordenar_lista(lista_numeros)
print(resultado_ascendente)  # Output: [1, 2, 5, 8, 9]

# Ordenamiento descendente
estrategia_descendente = EstrategiaOrdenDescendente()
ordenamiento.establecer_estrategia(estrategia_descendente)
resultado_descendente = ordenamiento.ordenar_lista(lista_numeros)
print(resultado_descendente)  # Output: [9, 8, 5, 2, 1]

"""
En este ejemplo, tenemos la interfaz EstrategiaOrdenamiento que define el método ordenar() que será implementado por las 
clases concretas que representan diferentes algoritmos de ordenamiento.

Luego, tenemos dos implementaciones concretas de estrategias: EstrategiaOrdenAscendente y EstrategiaOrdenDescendente. 
Ambas implementan el método ordenar() de acuerdo a sus respectivos algoritmos de ordenamiento.

La clase Ordenamiento es el contexto que utiliza las estrategias. Tiene un atributo estrategia que representa la 
estrategia actualmente seleccionada para el ordenamiento. El método ordenar_lista() delega el trabajo de ordenamiento a 
la estrategia actual.

En el ejemplo, primero utilizamos el ordenamiento ascendente y luego cambiamos dinámicamente a la estrategia de 
ordenamiento descendente sin afectar el código del contexto Ordenamiento.

En resumen, el patrón Strategy es útil cuando tienes algoritmos que pueden variar en su implementación y quieres 
permitir que el cliente elija y cambie dinámicamente la estrategia que debe utilizar. Con este patrón, los algoritmos 
se encapsulan en clases separadas, lo que promueve la flexibilidad, reutilización y extensibilidad del código.
"""