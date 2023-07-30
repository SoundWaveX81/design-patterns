"""
Behavioural pattern Interpreter

El patrón Interpreter es un patrón de diseño de comportamiento que se utiliza para evaluar expresiones o lenguajes 
formales. Define una gramática para el lenguaje y proporciona una interpretación para las sentencias en esa gramática. 
El patrón Interpreter permite representar una gramática en forma de objetos y proporcionar un intérprete que evalúe las 
expresiones escritas en ese lenguaje.

En términos más sencillos, el patrón Interpreter es útil cuando necesitas definir un lenguaje y evaluar expresiones 
escritas en ese lenguaje.

Ejemplo en Python:

Supongamos que queremos crear un intérprete de expresiones matemáticas simples que puedan sumar y restar números.
"""

# Interfaz de Expresión
class Expresion:
    def evaluar(self):
        pass

# Implementación concreta de Expresión (Terminal)
class Numero(Expresion):
    def __init__(self, valor):
        self.valor = valor

    def evaluar(self):
        return self.valor

# Implementación concreta de Expresión (No terminal)
class Suma(Expresion):
    def __init__(self, izquierda, derecha):
        self.izquierda = izquierda
        self.derecha = derecha

    def evaluar(self):
        return self.izquierda.evaluar() + self.derecha.evaluar()

# Implementación concreta de Expresión (No terminal)
class Resta(Expresion):
    def __init__(self, izquierda, derecha):
        self.izquierda = izquierda
        self.derecha = derecha

    def evaluar(self):
        return self.izquierda.evaluar() - self.derecha.evaluar()

# Ejemplo de uso del patrón Interpreter
expresion = Resta(Suma(Numero(10), Numero(5)), Numero(2))
resultado = expresion.evaluar()
print(resultado)  # Output: 13

"""
En este ejemplo, tenemos la clase Expresion, que es la interfaz base para las expresiones concretas. Cada clase concreta 
(por ejemplo, Numero, Suma, Resta) implementa el método evaluar() para evaluar la expresión.

La clase Numero es una expresión terminal que simplemente contiene un valor numérico y devuelve ese valor cuando se 
evalúa.

Las clases Suma y Resta son expresiones no terminales que contienen dos expresiones (izquierda y derecha) y realizan la 
suma o resta de las evaluaciones de esas expresiones cuando son evaluadas.

En el ejemplo, creamos una expresión que representa la operación (10 + 5) - 2. Luego, evaluamos la expresión usando el 
método evaluar(), y el resultado es 13.

En resumen, el patrón Interpreter es útil cuando necesitas definir una gramática y un lenguaje para evaluar expresiones 
escritas en ese lenguaje. Con este patrón, puedes representar la gramática en forma de objetos y proporcionar un 
intérprete que evalúe las expresiones siguiendo las reglas de la gramática. Esto promueve la extensibilidad y el 
mantenimiento del código, ya que puedes agregar nuevas expresiones o reglas sin afectar el intérprete existente.
"""