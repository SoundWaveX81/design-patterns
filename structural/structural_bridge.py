""" 
Structural pattern Bridge 

El patrón Bridge es un patrón de diseño estructural que tiene como objetivo separar la abstracción (la interfaz o la 
abstracción de alto nivel) de su implementación (la implementación o la abstracción de bajo nivel). De esta manera, 
el patrón Bridge permite que ambas puedan variar de forma independiente, proporcionando una mayor flexibilidad y 
evitando una explosión combinatoria de clases.

Imagina que tienes una jerarquía de clases de formas (por ejemplo, círculos, cuadrados, triángulos) y una jerarquía de 
clases de colores (por ejemplo, rojo, verde, azul). Si deseas que cada forma pueda ser dibujada en diferentes colores, 
podrías terminar con una combinación de clases (por ejemplo, RojoCírculo, RojoCuadrado, VerdeCírculo, VerdeCuadrado, 
etc.), lo que aumentaría la complejidad.

Aquí es donde el patrón Bridge entra en juego. En lugar de tener una jerarquía combinada, tendrías dos jerarquías 
separadas: una para las formas y otra para los colores. Luego, una clase "Puente" (Bridge) conecta ambas jerarquías y 
permite que las formas y los colores varíen independientemente.

En este ejemplo, tenemos dos jerarquías: una para las formas (Shape) y otra para los colores (Color). Las clases 
RedColor y GreenColor son implementaciones concretas de colores. Luego, las clases Circle y Square son implementaciones 
concretas de formas. La clase Shape tiene una referencia a una instancia de Color, que actúa como el "Puente" entre 
ambas jerarquías.

En este ejemplo, podemos ver cómo el patrón Bridge nos permite tener formas y colores independientes, y podemos 
combinarlos de forma flexible para lograr diferentes combinaciones sin necesidad de crear una clase para cada posible 
combinación.

En resumen, el patrón Bridge es útil cuando tienes dos dimensiones de clases que varían de forma independiente y deseas 
evitar una combinación exponencial de clases concretas. Al separar las jerarquías con una "Abstracción" y una 
"Implementación", el patrón Bridge promueve un diseño más flexible y fácil de mantener.
"""


class Color:
    def fill(self) -> str:
        pass

class Shape:
    def __init__(self, color: Color) -> None:
        self.color = color

    def draw(self) -> str:
        pass

class RedColor(Color):
    def fill(self) -> str:
        return 'rojo'

class GreenColor(Color):
    def fill(self) -> str:
        return 'verde'

class Circle(Shape):

    def draw(self) -> str:
        return f'dibuja un circulo de color {self.color.fill()}'

class Square(Shape):

    def draw(self) -> str:
        return f'dibuja un cuadrado de color {self.color.fill()}'

red = RedColor()
green = GreenColor()

red_circle = Circle(red)
green_square = Square(green)


print(red_circle.draw())
print(green_square.draw())
