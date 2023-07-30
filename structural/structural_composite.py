"""
Structural pattern Composite

El patrón Composite es un patrón de diseño estructural que permite tratar tanto a los objetos individuales como a las 
composiciones de objetos de manera uniforme. El patrón Composite compone objetos en estructuras de árbol para 
representar jerarquías parte-todo. Esto significa que puedes tratar a los objetos individuales y a las agrupaciones de 
objetos (compuestos) de manera similar, lo que facilita trabajar con estructuras complejas de manera más sencilla.

Imagina que tienes una jerarquía de elementos gráficos, como formas (círculos, cuadrados) y grupos de formas (conjunto 
de formas). Quieres poder trabajar con una forma individual o con un grupo de formas como si fueran un solo objeto, 
aplicando operaciones de forma consistente.
"""

# Componente base de la jerarquía
class Componente:
    def dibujar(self):
        pass

# Clase Leaf (Hoja): Representa objetos individuales (formas)
class Forma(Componente):
    def __init__(self, nombre):
        self.nombre = nombre

    def dibujar(self):
        return f"Dibujando {self.nombre}"

# Clase Composite (Compuesto): Representa un grupo de objetos (conjunto de formas)
class GrupoFormas(Componente):
    def __init__(self):
        self.formas = []

    def agregar(self, forma):
        self.formas.append(forma)

    def dibujar(self):
        resultado = "Grupo de formas:\n"
        for forma in self.formas:
            resultado += forma.dibujar() + "\n"
        return resultado

"""
En este ejemplo, tenemos la clase base Componente que define una operación dibujar(). Luego, tenemos la clase Forma, que 
es una implementación concreta de un objeto individual (una forma).

A continuación, definimos la clase GrupoFormas, que también es una implementación de Componente. La clase GrupoFormas 
puede contener una lista de objetos Forma. De esta manera, podemos agregar formas individuales a un grupo de formas y 
tratar el grupo de formas como una entidad única.

Ahora, podemos usar el patrón Composite para trabajar con formas individuales y grupos de formas de manera uniforme:
"""

# Crear formas individuales
circulo = Forma("Círculo")
cuadrado = Forma("Cuadrado")
triangulo = Forma("Triángulo")

# Crear un grupo de formas y agregar formas individuales al grupo
grupo1 = GrupoFormas()
grupo1.agregar(circulo)
grupo1.agregar(cuadrado)

grupo2 = GrupoFormas()
grupo2.agregar(triangulo)

# Crear un grupo más grande y agregar los grupos anteriores al grupo compuesto
grupo_compuesto = GrupoFormas()
grupo_compuesto.agregar(grupo1)
grupo_compuesto.agregar(grupo2)

# Dibujar formas individuales
print(circulo.dibujar())   # Output: Dibujando Círculo
print(cuadrado.dibujar())  # Output: Dibujando Cuadrado

# Dibujar grupos de formas (compuestos)
print(grupo1.dibujar())
# Output:
# Grupo de formas:
# Dibujando Círculo
# Dibujando Cuadrado

print(grupo2.dibujar())
# Output:
# Grupo de formas:
# Dibujando Triángulo

print(grupo_compuesto.dibujar())
# Output:
# Grupo de formas:
# Dibujando Círculo
# Dibujando Cuadrado
# Grupo de formas:
# Dibujando Triángulo

"""
En este ejemplo, hemos creado formas individuales y grupos de formas utilizando el patrón Composite. Las formas 
individuales y los grupos de formas se tratan de manera uniforme mediante el método dibujar(), lo que nos permite 
trabajar con estructuras complejas de forma más sencilla y consistente.

En resumen, el patrón Composite es útil cuando necesitas tratar tanto a los objetos individuales como a las agrupaciones 
    de objetos de manera uniforme, lo que te permite trabajar con estructuras jerárquicas de forma más flexible y sencilla.
"""