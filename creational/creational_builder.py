"""
Creational pattern Builder
El patrón Builder es un patrón de diseño creacional que se utiliza para construir objetos complejos paso a paso. Permite 
separar la construcción de un objeto de su representación, lo que facilita la creación de diferentes variaciones del 
mismo objeto utilizando el mismo proceso de construcción.

Imagina que tienes una clase Producto que puede tener muchas partes y configuraciones diferentes. En lugar de crear un 
constructor con muchos argumentos y opciones, puedes utilizar el patrón Builder para dividir el proceso de construcción 
del objeto en pasos más manejables y personalizables.

Ejemplo en Python:

Supongamos que tenemos una clase Computadora que representa una computadora y tiene varias partes como procesador, 
memoria, disco duro, etc. Queremos utilizar el patrón Builder para construir computadoras con diferentes configuraciones 
de manera más sencilla.
"""

# Producto: Computadora
class Computadora:
    def __init__(self):
        self.procesador = None
        self.memoria = None
        self.disco_duro = None

    def __str__(self) -> str:
        return f"Computadora: Procesador={self.procesador}, Memoria={self.memoria}, Disco Duro={self.disco_duro}"

# Builder abstracto
class BuilderComputadora:
    def construir_procesador(self):
        pass

    def construir_memoria(self):
        pass

    def construir_disco_duro(self):
        pass

    def obtener_computadora(self):
        pass

# Builder concreto para una computadora básica
class BuilderComputadoraBasica(BuilderComputadora):
    def __init__(self):
        self.computadora = Computadora()

    def construir_procesador(self):
        self.computadora.procesador = "Procesador básico"

    def construir_memoria(self):
        self.computadora.memoria = "4 GB"

    def construir_disco_duro(self):
        self.computadora.disco_duro = "HDD 500 GB"

    def obtener_computadora(self) -> Computadora:
        return self.computadora

# Builder concreto para una computadora avanzada
class BuilderComputadoraAvanzada(BuilderComputadora):
    def __init__(self):
        self.computadora = Computadora()

    def construir_procesador(self):
        self.computadora.procesador = "Procesador de alto rendimiento"

    def construir_memoria(self):
        self.computadora.memoria = "16 GB"

    def construir_disco_duro(self):
        self.computadora.disco_duro = "SSD 1 TB"

    def obtener_computadora(self) -> Computadora:
        return self.computadora

# Director (opcional): Facilita la construcción de objetos
class Director:
    def __init__(self, builder: BuilderComputadora):
        self.builder = builder

    def construir_computadora(self):
        self.builder.construir_procesador()
        self.builder.construir_memoria()
        self.builder.construir_disco_duro()

# Ejemplo de uso del patrón Builder
builder_basico = BuilderComputadoraBasica()
director_basico = Director(builder_basico)
director_basico.construir_computadora()
computadora_basica = builder_basico.obtener_computadora()
print(computadora_basica)
# Output: Computadora: Procesador=Procesador básico, Memoria=4 GB, Disco Duro=HDD 500 GB

builder_avanzado = BuilderComputadoraAvanzada()
director_avanzado = Director(builder_avanzado)
director_avanzado.construir_computadora()
computadora_avanzada = builder_avanzado.obtener_computadora()
print(computadora_avanzada)
# Output: Computadora: Procesador=Procesador de alto rendimiento, Memoria=16 GB, Disco Duro=SSD 1 TB

"""
En este ejemplo, tenemos la clase Computadora, que es el producto que queremos construir con diferentes configuraciones. 
Luego, definimos el BuilderComputadora, que es una clase abstracta que define los pasos para construir una computadora. 
También tenemos dos implementaciones concretas de este builder: BuilderComputadoraBasica y BuilderComputadoraAvanzada, 
cada uno con diferentes configuraciones de componentes de computadora.

El Director es opcional y facilita la construcción de objetos utilizando un builder concreto. Ayuda a separar la lógica 
de construcción del cliente que utiliza los builders.

Finalmente, creamos dos computadoras diferentes usando los builders concretos. Cada computadora se construye paso a paso 
según su configuración, y el resultado es dos computadoras con diferentes especificaciones.

En resumen, el patrón Builder es útil cuando tienes un objeto complejo con muchas partes y configuraciones diferentes.
 Divide el proceso de construcción en pasos manejables y personalizables, lo que facilita la creación de diferentes 
 variantes del mismo objeto. Además, el patrón Builder promueve un código más limpio y flexible al evitar constructores 
 con muchos parámetros y opciones.
"""