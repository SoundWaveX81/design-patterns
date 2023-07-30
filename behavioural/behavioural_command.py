"""
Behavioural pattern Command


El patrón Command es un patrón de diseño de comportamiento que convierte una solicitud o acción en un objeto 
independiente, permitiendo que la solicitud sea parametrizable y pueda ser encolada, deshecha, registrada o reutilizada. 
En esencia, el patrón Command encapsula una solicitud como un objeto, lo que permite el desacoplamiento entre el emisor 
de la solicitud (cliente) y el receptor que la lleva a cabo.

Imagina que tienes una aplicación con un menú que realiza diferentes acciones cuando el usuario selecciona una opción. 
En lugar de codificar directamente la lógica de cada acción en el menú, el patrón Command te permite encapsular cada 
acción como un objeto, lo que hace que el menú no necesite conocer los detalles de cómo se realiza cada acción.

Ejemplo en Python:

Supongamos que tenemos una clase Calculadora que realiza diferentes operaciones matemáticas (sumar, restar, multiplicar, 
dividir). Utilizaremos el patrón Command para encapsular cada operación como un objeto de comando.
"""

# Interfaz de Comando (Command)
class ComandoCalculadora:
    def ejecutar(self):
        pass

# Implementación concreta de Comando (Command)
class ComandoSumar(ComandoCalculadora):
    def __init__(self, calculadora, valor):
        self.calculadora = calculadora
        self.valor = valor

    def ejecutar(self):
        self.calculadora.sumar(self.valor)

# Implementación concreta de Comando (Command)
class ComandoRestar(ComandoCalculadora):
    def __init__(self, calculadora, valor):
        self.calculadora = calculadora
        self.valor = valor

    def ejecutar(self):
        self.calculadora.restar(self.valor)

# Implementación concreta de Comando (Command)
class ComandoMultiplicar(ComandoCalculadora):
    def __init__(self, calculadora, valor):
        self.calculadora = calculadora
        self.valor = valor

    def ejecutar(self):
        self.calculadora.multiplicar(self.valor)

# Implementación concreta de Comando (Command)
class ComandoDividir(ComandoCalculadora):
    def __init__(self, calculadora, valor):
        self.calculadora = calculadora
        self.valor = valor

    def ejecutar(self):
        self.calculadora.dividir(self.valor)

# Clase Receptora (Receiver)
class Calculadora:
    def __init__(self):
        self.valor = 0

    def sumar(self, valor):
        self.valor += valor

    def restar(self, valor):
        self.valor -= valor

    def multiplicar(self, valor):
        self.valor *= valor

    def dividir(self, valor):
        if valor != 0:
            self.valor /= valor

# Clase Invocador (Invoker)
class InvocadorCalculadora:
    def __init__(self):
        self.operaciones = []

    def agregar_operacion(self, operacion):
        self.operaciones.append(operacion)

    def ejecutar_operaciones(self):
        for operacion in self.operaciones:
            operacion.ejecutar()

# Ejemplo de uso del patrón Command
calculadora = Calculadora()
invocador = InvocadorCalculadora()

invocador.agregar_operacion(ComandoSumar(calculadora, 5))
invocador.agregar_operacion(ComandoRestar(calculadora, 2))
invocador.agregar_operacion(ComandoMultiplicar(calculadora, 3))
invocador.agregar_operacion(ComandoDividir(calculadora, 2))

invocador.ejecutar_operaciones()

print(calculadora.valor)  # Output: 8.0

"""
En este ejemplo, tenemos la clase ComandoCalculadora, que es la interfaz base para los comandos concretos (ComandoSumar, 
ComandoRestar, etc.). Cada comando concreto toma una instancia de Calculadora y un valor específico para realizar la 
operación.

La clase Calculadora es el receptor que ejecuta las operaciones matemáticas reales.

El InvocadorCalculadora es el invocador que agrega y ejecuta los comandos. Cuando el invocador recibe una solicitud para 
ejecutar los comandos, recorre cada comando y los ejecuta.

En el ejemplo, el InvocadorCalculadora agrega comandos de suma, resta, multiplicación y división a la lista de 
operaciones y luego los ejecuta secuencialmente. Como resultado, el valor de la Calculadora se modifica según las 
operaciones realizadas.

En resumen, el patrón Command es útil cuando necesitas desacoplar el emisor de una solicitud (cliente) del receptor que 
la lleva a cabo. Encapsula la solicitud como un objeto, lo que permite que la solicitud sea parametrizable y pueda ser 
encolada, deshecha, registrada o reutilizada. Esto promueve la flexibilidad y el mantenimiento del código, ya que puedes 
cambiar y agregar nuevas acciones sin afectar al cliente.
"""